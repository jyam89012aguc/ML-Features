import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _logp(s):
    return np.log(s.replace(0, np.nan))


# ===== folder domain primitives (range-based volatility estimators) =====
# All return a per-day variance/variance-like contribution; rolling-mean then sqrt
# yields the annualized-or-raw vol estimate. Kept as primitives but each feature
# wraps them in different surrounding math so pairs stay decorrelated.

def _f10_parkinson_term(high, low):
    # Parkinson single-day variance proxy: (1/(4 ln2)) * (ln(H/L))^2
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    return (hl * hl) / (4.0 * np.log(2.0))


def _f10_garman_klass_term(open_, high, low, close):
    # Garman-Klass single-day variance proxy
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    return 0.5 * hl * hl - (2.0 * np.log(2.0) - 1.0) * co * co


def _f10_rogers_satchell_term(open_, high, low, close):
    # Rogers-Satchell single-day variance proxy (drift-independent)
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    return ho * hc + lo * lc


def _f10_overnight_term(open_, close):
    # overnight (close-to-open) squared log return: the YZ "open jump" component
    o = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return o * o


def _f10_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f10_hl_range(high, low, close):
    # plain high-low range normalized by close (per-day amplitude)
    return (high - low) / close.replace(0, np.nan)


def _f10_pk_vol(high, low, w):
    return np.sqrt(_f10_parkinson_term(high, low).rolling(w, min_periods=max(1, w // 2)).mean())


def _f10_gk_vol(open_, high, low, close, w):
    t = _f10_garman_klass_term(open_, high, low, close).clip(lower=0)
    return np.sqrt(t.rolling(w, min_periods=max(1, w // 2)).mean())


def _f10_rs_vol(open_, high, low, close, w):
    t = _f10_rogers_satchell_term(open_, high, low, close).clip(lower=0)
    return np.sqrt(t.rolling(w, min_periods=max(1, w // 2)).mean())


def _f10_atr(high, low, close, w):
    return _f10_true_range(high, low, close).rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# ---- Parkinson estimator family ----

# Parkinson vol over 5d, normalized by close (intraday range vol level)
def f10rv_f10_range_vol_estimators_pkvol_5d_base_v001_signal(high, low, close):
    pk = _f10_pk_vol(high, low, 5)
    b = pk / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol over 21d, normalized by close
def f10rv_f10_range_vol_estimators_pkvol_21d_base_v002_signal(high, low, close):
    b = _f10_pk_vol(high, low, 21) / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d vol residual from its own slow EMA (de-leveled range-vol cycle)
def f10rv_f10_range_vol_estimators_pkresid_63d_base_v003_signal(high, low, closeadj):
    pk = _f10_pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    b = pk / pk.ewm(span=252, min_periods=63).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 252d-vs-63d long-horizon range-vol gap (structural vol slope)
def f10rv_f10_range_vol_estimators_pkgap_252v63_base_v004_signal(high, low, closeadj):
    long = _f10_pk_vol(high, low, 252) / closeadj.replace(0, np.nan)
    short = _f10_pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    b = np.log(long.replace(0, np.nan) / short.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol term-structure ratio (21d / 63d) — short vs medium range-vol
def f10rv_f10_range_vol_estimators_pkratio_21v63_base_v005_signal(high, low):
    s = _f10_pk_vol(high, low, 21)
    l = _f10_pk_vol(high, low, 63)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol z-score vs own 252d history (de-trended level)
def f10rv_f10_range_vol_estimators_pkz_63d_base_v006_signal(high, low):
    pk = _f10_pk_vol(high, low, 63)
    b = _z(pk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson per-day term z-score (single-day range shock vs 63d norm)
def f10rv_f10_range_vol_estimators_pkshock_1d_base_v007_signal(high, low):
    t = _f10_parkinson_term(high, low)
    b = _z(t, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson term skew: rolling skewness of daily Parkinson variance (fat-tail range)
def f10rv_f10_range_vol_estimators_pkskew_63d_base_v008_signal(high, low):
    t = _f10_parkinson_term(high, low)
    b = t.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Garman-Klass estimator family ----

# GK-vs-Parkinson 5d ratio: open/close info content vs pure range at short horizon
def f10rv_f10_range_vol_estimators_gkpkratio_5d_base_v009_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 5)
    pk = _f10_pk_vol(high, low, 5)
    b = gk / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK body-vs-range balance: close-open variance share of GK estimator (21d)
def f10rv_f10_range_vol_estimators_gkbodyshare_21d_base_v010_signal(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    hl_term = (0.5 * hl * hl).rolling(21, min_periods=10).mean()
    co_term = ((2.0 * np.log(2.0) - 1.0) * co * co).rolling(21, min_periods=10).mean()
    b = co_term / (hl_term + co_term).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 63d vol residual from its own 252d median band (de-leveled GK cycle)
def f10rv_f10_range_vol_estimators_gkresid_63d_base_v011_signal(open, high, low, close, closeadj):
    gk = _f10_gk_vol(open, high, low, close, 63) / closeadj.replace(0, np.nan)
    med = gk.rolling(252, min_periods=63).median()
    b = gk / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 126d-vs-21d range-vol curvature (medium-vs-short GK term slope)
def f10rv_f10_range_vol_estimators_gkgap_126v21_base_v012_signal(open, high, low, close, closeadj):
    long = _f10_gk_vol(open, high, low, close, 126) / closeadj.replace(0, np.nan)
    short = _f10_gk_vol(open, high, low, close, 21) / closeadj.replace(0, np.nan)
    b = np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol acceleration: change in the 21d-vol log-slope (range-vol convexity)
def f10rv_f10_range_vol_estimators_gkaccel_21d_base_v013_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 21)
    slope = np.log(gk.replace(0, np.nan) / gk.shift(5).replace(0, np.nan))
    b = slope - slope.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol z-score vs own 252d history
def f10rv_f10_range_vol_estimators_gkz_63d_base_v014_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    b = _z(gk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol slope: log-change of the 63d GK vol over a month (vol momentum)
def f10rv_f10_range_vol_estimators_gkslope_63d_base_v015_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    b = np.log(gk.replace(0, np.nan) / gk.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK term kurtosis: tail-heaviness of daily GK variance over 63d (range tail risk)
def f10rv_f10_range_vol_estimators_gkkurt_63d_base_v016_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    b = t.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Rogers-Satchell estimator family ----

# RS-vs-GK 5d ratio: drift-robust vs symmetric estimator at short horizon
def f10rv_f10_range_vol_estimators_rsgkratio_5d_base_v017_signal(open, high, low, close):
    rs = _f10_rs_vol(open, high, low, close, 5)
    gk = _f10_gk_vol(open, high, low, close, 5)
    b = rs / gk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS 21d vol relative to its own 126d EMA (short-horizon RS vol pulse)
def f10rv_f10_range_vol_estimators_rspulse_21d_base_v018_signal(open, high, low, close):
    rs = _f10_rs_vol(open, high, low, close, 21) / close.replace(0, np.nan)
    b = rs / rs.ewm(span=126, min_periods=42).mean().replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS 63d vol cone percentile vs its own 504d history (long RS regime position)
def f10rv_f10_range_vol_estimators_rsconerk_63d_base_v019_signal(open, high, low, close, closeadj):
    rs = _f10_rs_vol(open, high, low, close, 63) / closeadj.replace(0, np.nan)
    b = _rank(rs, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS 252d-vs-63d long structural range-vol slope
def f10rv_f10_range_vol_estimators_rsgap_252v63_base_v020_signal(open, high, low, close, closeadj):
    long = _f10_rs_vol(open, high, low, close, 252) / closeadj.replace(0, np.nan)
    short = _f10_rs_vol(open, high, low, close, 63) / closeadj.replace(0, np.nan)
    b = np.log(long.replace(0, np.nan) / short.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS vol term-structure ratio (21d / 63d)
def f10rv_f10_range_vol_estimators_rsratio_21v63_base_v021_signal(open, high, low, close):
    s = _f10_rs_vol(open, high, low, close, 21)
    l = _f10_rs_vol(open, high, low, close, 63)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS term skew: asymmetry of daily Rogers-Satchell variance over 63d
def f10rv_f10_range_vol_estimators_rsskew_63d_base_v022_signal(open, high, low, close):
    t = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0)
    b = t.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS drift signature: directional bias from the up-leg vs down-leg RS components
def f10rv_f10_range_vol_estimators_rsdrift_21d_base_v023_signal(open, high, low, close):
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    up = (ho * hc).rolling(21, min_periods=10).mean()
    dn = (lo * lc).rolling(21, min_periods=10).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS downside-leg share: low-side range variance as a fraction of total RS (63d)
def f10rv_f10_range_vol_estimators_rsdownshare_63d_base_v024_signal(open, high, low, close):
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    up = (ho * hc).clip(lower=0).rolling(63, min_periods=21).mean()
    dn = (lo * lc).clip(lower=0).rolling(63, min_periods=21).mean()
    b = dn / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Yang-Zhang-style estimator family ----

# YZ 21d vol vs Parkinson 21d: full-info vol premium over pure-range vol (gap load)
def f10rv_f10_range_vol_estimators_yzpkratio_21d_base_v025_signal(open, high, low, close):
    w = 21
    on = _f10_overnight_term(open, close).rolling(w, min_periods=10).mean()
    rs = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(w, min_periods=10).mean()
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    oc = (co * co).rolling(w, min_periods=10).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    yz = np.sqrt((on + k * oc + (1.0 - k) * rs).clip(lower=0))
    pk = _f10_pk_vol(high, low, w)
    b = yz / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ 63d vol slope: log-change of YZ range-vol over a quarter (vol trend)
def f10rv_f10_range_vol_estimators_yzslope_63d_base_v026_signal(open, high, low, close, closeadj):
    w = 63
    on = _f10_overnight_term(open, close).rolling(w, min_periods=21).mean()
    rs = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(w, min_periods=21).mean()
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    oc = (co * co).rolling(w, min_periods=21).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    yz = np.sqrt((on + k * oc + (1.0 - k) * rs).clip(lower=0)) / closeadj.replace(0, np.nan)
    b = np.log(yz.replace(0, np.nan) / yz.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-vs-intraday vol split: how much of YZ vol is gap-driven (21d)
def f10rv_f10_range_vol_estimators_yzgapshare_21d_base_v027_signal(open, high, low, close):
    on = _f10_overnight_term(open, close).rolling(21, min_periods=10).mean()
    rs = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(21, min_periods=10).mean()
    b = on / (on + rs).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-vol z-score vs 252d history (gap-risk regime)
def f10rv_f10_range_vol_estimators_yzovz_63d_base_v028_signal(open, close):
    on = np.sqrt(_f10_overnight_term(open, close).rolling(63, min_periods=21).mean())
    b = _z(on, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ-minus-RS spread (63d): how much the gap/open terms add over drift-robust RS
def f10rv_f10_range_vol_estimators_yzrsspread_63d_base_v029_signal(open, high, low, close):
    w = 63
    on = _f10_overnight_term(open, close).rolling(w, min_periods=21).mean()
    rsv = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(w, min_periods=21).mean()
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    oc = (co * co).rolling(w, min_periods=21).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    yz = np.sqrt((on + k * oc + (1.0 - k) * rsv).clip(lower=0))
    rs = _f10_rs_vol(open, high, low, close, w)
    b = (yz - rs) / (yz + rs).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ vol-of-vol: variability of the 21d YZ vol over 63d (range-vol instability)
def f10rv_f10_range_vol_estimators_yzvov_63d_base_v030_signal(open, high, low, close):
    w = 21
    on = _f10_overnight_term(open, close).rolling(w, min_periods=10).mean()
    rs = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(w, min_periods=10).mean()
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    oc = (co * co).rolling(w, min_periods=10).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    yz = np.sqrt((on + k * oc + (1.0 - k) * rs).clip(lower=0))
    m = yz.rolling(63, min_periods=21).mean()
    b = yz.rolling(63, min_periods=21).std() / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ATR & ATR/price family ----

# ATR over 5d, normalized by close
def f10rv_f10_range_vol_estimators_atr_5d_base_v031_signal(high, low, close):
    b = _f10_atr(high, low, close, 5) / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR over 14d (classic Wilder window), normalized by close
def f10rv_f10_range_vol_estimators_atr_14d_base_v032_signal(high, low, close):
    b = _f10_atr(high, low, close, 14) / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR over 21d, normalized by close (ATR%)
def f10rv_f10_range_vol_estimators_atr_21d_base_v033_signal(high, low, close):
    b = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR over 63d, normalized by closeadj
def f10rv_f10_range_vol_estimators_atr_63d_base_v034_signal(high, low, close, closeadj):
    b = _f10_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR% 252d cone percentile vs its own 504d history (structural ATR regime)
def f10rv_f10_range_vol_estimators_atrconerk_252d_base_v035_signal(high, low, close, closeadj):
    atrp = _f10_atr(high, low, close, 252) / closeadj.replace(0, np.nan)
    b = _rank(atrp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR% term-structure ratio (14d / 63d)
def f10rv_f10_range_vol_estimators_atrratio_14v63_base_v036_signal(high, low, close):
    s = _f10_atr(high, low, close, 14) / close.replace(0, np.nan)
    l = _f10_atr(high, low, close, 63) / close.replace(0, np.nan)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR% z-score vs own 252d history (de-trended ATR level)
def f10rv_f10_range_vol_estimators_atrz_21d_base_v037_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _z(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR slope: log-change of 21d ATR over a week (range expansion speed)
def f10rv_f10_range_vol_estimators_atrslope_21d_base_v038_signal(high, low, close):
    atr = _f10_atr(high, low, close, 21)
    b = np.log(atr.replace(0, np.nan) / atr.shift(5).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR% cone percentile vs 252d history
def f10rv_f10_range_vol_estimators_atrconerk_21d_base_v039_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _rank(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- True-range z-score family ----

# single-day true-range z vs 21d
def f10rv_f10_range_vol_estimators_trz_21d_base_v040_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    b = _z(tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range autocorrelation (lag-1) over 63d: range clustering / persistence
def f10rv_f10_range_vol_estimators_tracf_63d_base_v041_signal(high, low, close):
    tr = _f10_true_range(high, low, close) / close.replace(0, np.nan)
    b = tr.rolling(63, min_periods=21).corr(tr.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range-as-percent-of-close z vs 252d (scale-free TR shock)
def f10rv_f10_range_vol_estimators_trpz_252d_base_v042_signal(high, low, close):
    trp = _f10_true_range(high, low, close) / close.replace(0, np.nan)
    b = _z(trp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 21d with true-range > 2*sigma (TR shock frequency)
def f10rv_f10_range_vol_estimators_trshockfreq_21d_base_v043_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    z = _z(tr, 63)
    excess = (z - 1.5).clip(lower=0)
    b = excess.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max single-day true-range z within last 21d (worst recent range spike)
def f10rv_f10_range_vol_estimators_trmaxz_21d_base_v044_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    z = _z(tr, 63)
    b = z.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range gap component: TR minus same-day high-low (gap-driven range share)
def f10rv_f10_range_vol_estimators_trgap_21d_base_v045_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    hl = (high - low)
    gap = (tr - hl) / close.replace(0, np.nan)
    b = gap.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- High-low range vs close family ----

# weekly range vs monthly range: 5d mean HL range relative to 21d mean (range pulse)
def f10rv_f10_range_vol_estimators_hlrpulse_5v21_base_v046_signal(high, low, close):
    hl = _f10_hl_range(high, low, close)
    s = hl.rolling(5, min_periods=3).mean()
    l = hl.rolling(21, min_periods=10).mean()
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range % smoothed 21d
def f10rv_f10_range_vol_estimators_hlr_21d_base_v047_signal(high, low, close):
    hl = _f10_hl_range(high, low, close)
    b = hl.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range % smoothed 63d, normalized by closeadj
def f10rv_f10_range_vol_estimators_hlr_63d_base_v048_signal(high, low, closeadj):
    hl = (high - low) / closeadj.replace(0, np.nan)
    b = hl.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range vs same-day true-range: intraday range share of total range (21d)
def f10rv_f10_range_vol_estimators_hltrshare_21d_base_v049_signal(high, low, close):
    hl = (high - low)
    tr = _f10_true_range(high, low, close)
    share = hl / tr.replace(0, np.nan)
    b = share.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion regime: 5d avg range vs 63d avg range (multi-week range trend)
def f10rv_f10_range_vol_estimators_rngexp_5v63_base_v050_signal(high, low, close):
    hl = (high - low) / close.replace(0, np.nan)
    s = hl.rolling(5, min_periods=3).mean()
    l = hl.rolling(63, min_periods=21).mean()
    b = np.log(s.replace(0, np.nan) / l.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range contraction streak: consecutive days of narrowing high-low range
def f10rv_f10_range_vol_estimators_rngcontract_21d_base_v051_signal(high, low):
    hl = (high - low)
    logchg = np.log(hl.replace(0, np.nan) / hl.shift(1).replace(0, np.nan))
    contraction = (-logchg).clip(lower=0)
    b = contraction.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range % percentile rank vs 252d history (range cone)
def f10rv_f10_range_vol_estimators_hlrrk_63d_base_v052_signal(high, low, close):
    hl = _f10_hl_range(high, low, close).rolling(63, min_periods=21).mean()
    b = _rank(hl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- cross-estimator comparisons (estimator disagreement / structure) ----

# Parkinson-minus-close-to-close vol: range vs realized (jump indicator, 21d)
def f10rv_f10_range_vol_estimators_pkmccratio_21d_base_v053_signal(high, low, close):
    pk = _f10_pk_vol(high, low, 21)
    cc = close.pct_change().rolling(21, min_periods=10).std()
    b = pk / (close.replace(0, np.nan) * cc / close.replace(0, np.nan)).replace(0, np.nan)
    # equivalently pk_vol / (close*cc) but keep ratio of vols
    b = pk / (close.replace(0, np.nan) * cc).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK-minus-Parkinson spread: extra info captured by open/close (estimator gap)
def f10rv_f10_range_vol_estimators_gkpkspread_63d_base_v054_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    pk = _f10_pk_vol(high, low, 63)
    b = (gk - pk) / (gk + pk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS-minus-GK spread: drift sensitivity of the estimators (63d)
def f10rv_f10_range_vol_estimators_rsgkspread_63d_base_v055_signal(open, high, low, close):
    rs = _f10_rs_vol(open, high, low, close, 63)
    gk = _f10_gk_vol(open, high, low, close, 63)
    b = (rs - gk) / (rs + gk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-vs-Parkinson ratio: linear-range vs log-range estimator (21d)
def f10rv_f10_range_vol_estimators_atrpkratio_21d_base_v056_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    pk = _f10_pk_vol(high, low, 21) / close.replace(0, np.nan)
    b = atrp / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap-vol share trend: change in gap-driven vol fraction over a quarter
def f10rv_f10_range_vol_estimators_gapsharetrend_63d_base_v057_signal(open, high, low, close):
    on = _f10_overnight_term(open, close).rolling(63, min_periods=21).mean()
    rs = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(63, min_periods=21).mean()
    share = on / (on + rs).replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# estimator dispersion: std across {PK, GK, RS} normalized vols (model risk, 63d)
def f10rv_f10_range_vol_estimators_estdisp_63d_base_v058_signal(open, high, low, close):
    pk = _f10_pk_vol(high, low, 63) / close.replace(0, np.nan)
    gk = _f10_gk_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    rs = _f10_rs_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    b = pd.concat([pk, gk, rs], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- vol-of-range and asymmetry ----

# vol-of-Parkinson: std of daily Parkinson terms over 63d (instability of range)
def f10rv_f10_range_vol_estimators_volofpk_63d_base_v059_signal(high, low):
    t = _f10_parkinson_term(high, low)
    m = t.rolling(63, min_periods=21).mean()
    b = t.rolling(63, min_periods=21).std() / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-ATR: coefficient of variation of true-range over 63d
def f10rv_f10_range_vol_estimators_volofatr_63d_base_v060_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    m = tr.rolling(63, min_periods=21).mean()
    b = tr.rolling(63, min_periods=21).std() / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside-range vs downside-range asymmetry: up-day ranges vs down-day ranges (21d)
def f10rv_f10_range_vol_estimators_rngasym_21d_base_v061_signal(open, high, low, close):
    hl = (high - low) / close.replace(0, np.nan)
    up = close > open
    up_r = hl.where(up).rolling(21, min_periods=8).mean()
    dn_r = hl.where(~up).rolling(21, min_periods=8).mean()
    b = (up_r - dn_r) / (up_r + dn_r).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position-in-range: where close sits in the day's high-low, avg over 21d
def f10rv_f10_range_vol_estimators_clpos_21d_base_v062_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    b = pos.rolling(21, min_periods=10).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range skew: ratio of upper-shadow range to lower-shadow range vs open (21d)
def f10rv_f10_range_vol_estimators_shadowskew_21d_base_v063_signal(open, high, low):
    upper = (high - open).clip(lower=0)
    lower = (open - low).clip(lower=0)
    su = upper.rolling(21, min_periods=10).mean()
    sl = lower.rolling(21, min_periods=10).mean()
    b = (su - sl) / (su + sl).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- regime / expansion structure ----

# Parkinson vol expansion: current 21d PK vs its own 126d median band
def f10rv_f10_range_vol_estimators_pkexpand_21d_base_v064_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    med = pk.rolling(126, min_periods=63).median()
    b = pk / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR compression flag persistence: fraction of 63d with ATR% in bottom quartile
def f10rv_f10_range_vol_estimators_atrsqueeze_63d_base_v065_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    rk = _rank(atrp, 252) + 0.5
    depth = (0.25 - rk).clip(lower=0)
    b = depth.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range vol acceleration sign × magnitude: signed sqrt of 63d PK slope
def f10rv_f10_range_vol_estimators_pksignmag_63d_base_v066_signal(high, low):
    pk = _f10_pk_vol(high, low, 63)
    chg = np.log(pk.replace(0, np.nan) / pk.shift(21).replace(0, np.nan))
    b = np.sign(chg) * np.sqrt(chg.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol curvature: 63d PK relative to the average of its 21d and 252d PK
def f10rv_f10_range_vol_estimators_pkcurv_63d_base_v067_signal(high, low):
    s = _f10_pk_vol(high, low, 21)
    m = _f10_pk_vol(high, low, 63)
    l = _f10_pk_vol(high, low, 252)
    b = (2.0 * m - s - l) / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK fast-EWM vs slow-EWM range-vol crossover (vol regime turn signal)
def f10rv_f10_range_vol_estimators_gkewmcross_base_v068_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    fast = np.sqrt(t.ewm(span=10, min_periods=5).mean())
    slow = np.sqrt(t.ewm(span=63, min_periods=21).mean())
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA vs SMA range-vol divergence: ATR EWMA minus 21d ATR (regime turn)
def f10rv_f10_range_vol_estimators_atrewmadiv_21d_base_v069_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    ew = tr.ewm(span=21, min_periods=10).mean()
    sma = tr.rolling(21, min_periods=10).mean()
    b = (ew - sma) / sma.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional distinct structures to reach 75 ----

# Parkinson efficiency: range-vol per unit of net move (choppiness, 21d)
def f10rv_f10_range_vol_estimators_pkeff_21d_base_v070_signal(high, low, close):
    pk = _f10_pk_vol(high, low, 21)
    net = (close / close.shift(21) - 1.0).abs()
    b = pk / (net.replace(0, np.nan) + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-vol vs overnight-vol balance (63d): where risk lives
def f10rv_f10_range_vol_estimators_intraovbal_63d_base_v071_signal(open, high, low, close):
    intr = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(63, min_periods=21).mean()
    ov = _f10_overnight_term(open, close).rolling(63, min_periods=21).mean()
    b = (intr - ov) / (intr + ov).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol trend consistency: hit-rate of rising 21d PK over 63d
def f10rv_f10_range_vol_estimators_pktrendhit_63d_base_v072_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    step = np.log(pk.replace(0, np.nan) / pk.shift(5).replace(0, np.nan))
    pos = step.clip(lower=0).rolling(63, min_periods=21).sum()
    neg = (-step).clip(lower=0).rolling(63, min_periods=21).sum()
    b = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized true-range entropy-ish dispersion: range concentration over 21d
def f10rv_f10_range_vol_estimators_trconc_21d_base_v073_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    s = tr.rolling(21, min_periods=10).sum()
    mx = tr.rolling(21, min_periods=10).max()
    b = mx / s.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 252d vol percentile rank vs 504d history (long-horizon range-vol cone)
def f10rv_f10_range_vol_estimators_gkconerk_252d_base_v074_signal(open, high, low, close, closeadj):
    gk = _f10_gk_vol(open, high, low, close, 252) / closeadj.replace(0, np.nan)
    b = _rank(gk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol risk-adjusted return: 21d net return per unit Parkinson vol
def f10rv_f10_range_vol_estimators_pksharpe_21d_base_v075_signal(high, low, close):
    pk = _f10_pk_vol(high, low, 21) / close.replace(0, np.nan)
    ret = close / close.shift(21) - 1.0
    b = ret / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_range_vol_estimators_pkvol_5d_base_v001_signal,
    f10rv_f10_range_vol_estimators_pkvol_21d_base_v002_signal,
    f10rv_f10_range_vol_estimators_pkresid_63d_base_v003_signal,
    f10rv_f10_range_vol_estimators_pkgap_252v63_base_v004_signal,
    f10rv_f10_range_vol_estimators_pkratio_21v63_base_v005_signal,
    f10rv_f10_range_vol_estimators_pkz_63d_base_v006_signal,
    f10rv_f10_range_vol_estimators_pkshock_1d_base_v007_signal,
    f10rv_f10_range_vol_estimators_pkskew_63d_base_v008_signal,
    f10rv_f10_range_vol_estimators_gkpkratio_5d_base_v009_signal,
    f10rv_f10_range_vol_estimators_gkbodyshare_21d_base_v010_signal,
    f10rv_f10_range_vol_estimators_gkresid_63d_base_v011_signal,
    f10rv_f10_range_vol_estimators_gkgap_126v21_base_v012_signal,
    f10rv_f10_range_vol_estimators_gkaccel_21d_base_v013_signal,
    f10rv_f10_range_vol_estimators_gkz_63d_base_v014_signal,
    f10rv_f10_range_vol_estimators_gkslope_63d_base_v015_signal,
    f10rv_f10_range_vol_estimators_gkkurt_63d_base_v016_signal,
    f10rv_f10_range_vol_estimators_rsgkratio_5d_base_v017_signal,
    f10rv_f10_range_vol_estimators_rspulse_21d_base_v018_signal,
    f10rv_f10_range_vol_estimators_rsconerk_63d_base_v019_signal,
    f10rv_f10_range_vol_estimators_rsgap_252v63_base_v020_signal,
    f10rv_f10_range_vol_estimators_rsratio_21v63_base_v021_signal,
    f10rv_f10_range_vol_estimators_rsskew_63d_base_v022_signal,
    f10rv_f10_range_vol_estimators_rsdrift_21d_base_v023_signal,
    f10rv_f10_range_vol_estimators_rsdownshare_63d_base_v024_signal,
    f10rv_f10_range_vol_estimators_yzpkratio_21d_base_v025_signal,
    f10rv_f10_range_vol_estimators_yzslope_63d_base_v026_signal,
    f10rv_f10_range_vol_estimators_yzgapshare_21d_base_v027_signal,
    f10rv_f10_range_vol_estimators_yzovz_63d_base_v028_signal,
    f10rv_f10_range_vol_estimators_yzrsspread_63d_base_v029_signal,
    f10rv_f10_range_vol_estimators_yzvov_63d_base_v030_signal,
    f10rv_f10_range_vol_estimators_atr_5d_base_v031_signal,
    f10rv_f10_range_vol_estimators_atr_14d_base_v032_signal,
    f10rv_f10_range_vol_estimators_atr_21d_base_v033_signal,
    f10rv_f10_range_vol_estimators_atr_63d_base_v034_signal,
    f10rv_f10_range_vol_estimators_atrconerk_252d_base_v035_signal,
    f10rv_f10_range_vol_estimators_atrratio_14v63_base_v036_signal,
    f10rv_f10_range_vol_estimators_atrz_21d_base_v037_signal,
    f10rv_f10_range_vol_estimators_atrslope_21d_base_v038_signal,
    f10rv_f10_range_vol_estimators_atrconerk_21d_base_v039_signal,
    f10rv_f10_range_vol_estimators_trz_21d_base_v040_signal,
    f10rv_f10_range_vol_estimators_tracf_63d_base_v041_signal,
    f10rv_f10_range_vol_estimators_trpz_252d_base_v042_signal,
    f10rv_f10_range_vol_estimators_trshockfreq_21d_base_v043_signal,
    f10rv_f10_range_vol_estimators_trmaxz_21d_base_v044_signal,
    f10rv_f10_range_vol_estimators_trgap_21d_base_v045_signal,
    f10rv_f10_range_vol_estimators_hlrpulse_5v21_base_v046_signal,
    f10rv_f10_range_vol_estimators_hlr_21d_base_v047_signal,
    f10rv_f10_range_vol_estimators_hlr_63d_base_v048_signal,
    f10rv_f10_range_vol_estimators_hltrshare_21d_base_v049_signal,
    f10rv_f10_range_vol_estimators_rngexp_5v63_base_v050_signal,
    f10rv_f10_range_vol_estimators_rngcontract_21d_base_v051_signal,
    f10rv_f10_range_vol_estimators_hlrrk_63d_base_v052_signal,
    f10rv_f10_range_vol_estimators_pkmccratio_21d_base_v053_signal,
    f10rv_f10_range_vol_estimators_gkpkspread_63d_base_v054_signal,
    f10rv_f10_range_vol_estimators_rsgkspread_63d_base_v055_signal,
    f10rv_f10_range_vol_estimators_atrpkratio_21d_base_v056_signal,
    f10rv_f10_range_vol_estimators_gapsharetrend_63d_base_v057_signal,
    f10rv_f10_range_vol_estimators_estdisp_63d_base_v058_signal,
    f10rv_f10_range_vol_estimators_volofpk_63d_base_v059_signal,
    f10rv_f10_range_vol_estimators_volofatr_63d_base_v060_signal,
    f10rv_f10_range_vol_estimators_rngasym_21d_base_v061_signal,
    f10rv_f10_range_vol_estimators_clpos_21d_base_v062_signal,
    f10rv_f10_range_vol_estimators_shadowskew_21d_base_v063_signal,
    f10rv_f10_range_vol_estimators_pkexpand_21d_base_v064_signal,
    f10rv_f10_range_vol_estimators_atrsqueeze_63d_base_v065_signal,
    f10rv_f10_range_vol_estimators_pksignmag_63d_base_v066_signal,
    f10rv_f10_range_vol_estimators_pkcurv_63d_base_v067_signal,
    f10rv_f10_range_vol_estimators_gkewmcross_base_v068_signal,
    f10rv_f10_range_vol_estimators_atrewmadiv_21d_base_v069_signal,
    f10rv_f10_range_vol_estimators_pkeff_21d_base_v070_signal,
    f10rv_f10_range_vol_estimators_intraovbal_63d_base_v071_signal,
    f10rv_f10_range_vol_estimators_pktrendhit_63d_base_v072_signal,
    f10rv_f10_range_vol_estimators_trconc_21d_base_v073_signal,
    f10rv_f10_range_vol_estimators_gkconerk_252d_base_v074_signal,
    f10rv_f10_range_vol_estimators_pksharpe_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RANGE_VOL_ESTIMATORS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f10_range_vol_estimators_base_001_075_claude: %d features pass" % n_features)
