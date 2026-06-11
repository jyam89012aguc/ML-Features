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


# ===== folder domain primitives (range-based volatility estimators) =====
def _f10_parkinson_term(high, low):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    return (hl * hl) / (4.0 * np.log(2.0))


def _f10_garman_klass_term(open_, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    return 0.5 * hl * hl - (2.0 * np.log(2.0) - 1.0) * co * co


def _f10_rogers_satchell_term(open_, high, low, close):
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    return ho * hc + lo * lc


def _f10_overnight_term(open_, close):
    o = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return o * o


def _f10_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


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


def _f10_yz_vol(open_, high, low, close, w):
    on = _f10_overnight_term(open_, close).rolling(w, min_periods=max(5, w // 3)).mean()
    rs = _f10_rogers_satchell_term(open_, high, low, close).clip(lower=0).rolling(w, min_periods=max(5, w // 3)).mean()
    co = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    oc = (co * co).rolling(w, min_periods=max(5, w // 3)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    return np.sqrt((on + k * oc + (1.0 - k) * rs).clip(lower=0))


# ============================================================
# ---- Parkinson-anchored structures (76-90) ----

# Parkinson vol risk-adjusted momentum: 21d return per 21d Parkinson vol, smoothed
def f10rv_f10_range_vol_estimators_pkmomratio_21d_base_v076_signal(high, low, close):
    pk = _f10_pk_vol(high, low, 21) / close.replace(0, np.nan)
    ret = (close / close.shift(21) - 1.0)
    raw = ret / pk.replace(0, np.nan)
    b = raw.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol exponential weighting vs simple: EWMA(span21) PK term vs SMA(63)
def f10rv_f10_range_vol_estimators_pkewmsma_base_v077_signal(high, low):
    t = _f10_parkinson_term(high, low)
    ew = np.sqrt(t.ewm(span=21, min_periods=10).mean())
    sm = np.sqrt(t.rolling(63, min_periods=21).mean())
    b = ew / sm.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson term Sharpe: mean/std of daily Parkinson variance over 63d (stability)
def f10rv_f10_range_vol_estimators_pkstab_63d_base_v078_signal(high, low):
    t = _f10_parkinson_term(high, low)
    m = t.rolling(63, min_periods=21).mean()
    s = t.rolling(63, min_periods=21).std()
    b = m / s.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol jump indicator: max daily PK term over 21d vs the 21d mean term
def f10rv_f10_range_vol_estimators_pkjump_21d_base_v079_signal(high, low):
    t = _f10_parkinson_term(high, low)
    mx = t.rolling(21, min_periods=10).max()
    mn = t.rolling(21, min_periods=10).mean()
    b = mx / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol drawup: current 63d PK relative to its 252d max (vol stretch)
def f10rv_f10_range_vol_estimators_pkstretch_63d_base_v080_signal(high, low):
    pk = _f10_pk_vol(high, low, 63)
    mx = pk.rolling(252, min_periods=126).max()
    b = pk / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol trough: current 63d PK relative to its 252d min (compression depth)
def f10rv_f10_range_vol_estimators_pkcompress_63d_base_v081_signal(high, low):
    pk = _f10_pk_vol(high, low, 63)
    mn = pk.rolling(252, min_periods=126).min()
    b = pk / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol regime position within its 252d high-low band
def f10rv_f10_range_vol_estimators_pkconepos_63d_base_v082_signal(high, low):
    pk = _f10_pk_vol(high, low, 63)
    hi = pk.rolling(252, min_periods=126).max()
    lo = pk.rolling(252, min_periods=126).min()
    b = (pk - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol acceleration: change in 21d PK slope over a month (range jerk-ish)
def f10rv_f10_range_vol_estimators_pkaccel_21d_base_v083_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    slope = np.log(pk.replace(0, np.nan) / pk.shift(21).replace(0, np.nan))
    b = slope - slope.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Garman-Klass-anchored structures (84-95) ----

# GK vol risk-adjusted return (63d return per 63d GK vol)
def f10rv_f10_range_vol_estimators_gkmomratio_63d_base_v084_signal(open, high, low, close, closeadj):
    gk = _f10_gk_vol(open, high, low, close, 63) / closeadj.replace(0, np.nan)
    ret = (closeadj / closeadj.shift(63) - 1.0)
    b = ret / gk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol regime position within 252d band
def f10rv_f10_range_vol_estimators_gkconepos_63d_base_v085_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    hi = gk.rolling(252, min_periods=126).max()
    lo = gk.rolling(252, min_periods=126).min()
    b = (gk - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol stability: mean/std of daily GK variance over 63d
def f10rv_f10_range_vol_estimators_gkstab_63d_base_v086_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    m = t.rolling(63, min_periods=21).mean()
    s = t.rolling(63, min_periods=21).std()
    b = m / s.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol mean-reversion z: 21d GK relative to 126d GK in 126d-vol units
def f10rv_f10_range_vol_estimators_gkmrz_base_v087_signal(open, high, low, close):
    s = _f10_gk_vol(open, high, low, close, 21)
    l = _f10_gk_vol(open, high, low, close, 126)
    gap = s - l
    b = gap / gap.rolling(126, min_periods=63).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol semivariance split: GK vol on up-close days vs down-close days (63d)
def f10rv_f10_range_vol_estimators_gksemi_63d_base_v088_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    up = close >= open
    vu = np.sqrt(t.where(up).rolling(63, min_periods=21).mean())
    vd = np.sqrt(t.where(~up).rolling(63, min_periods=21).mean())
    b = (vd - vu) / (vd + vu).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol fast-vs-slow EWMA divergence at 5/42 spans (early regime turn)
def f10rv_f10_range_vol_estimators_gkewmdiv_base_v089_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    f = np.sqrt(t.ewm(span=5, min_periods=3).mean())
    s = np.sqrt(t.ewm(span=42, min_periods=21).mean())
    b = np.log(f.replace(0, np.nan) / s.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Rogers-Satchell-anchored structures (90-100) ----

# RS up-leg vs down-leg vol ratio over 63d (range directional bias)
def f10rv_f10_range_vol_estimators_rsupdown_63d_base_v090_signal(open, high, low, close):
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    up = np.sqrt((ho * hc).clip(lower=0).rolling(63, min_periods=21).mean())
    dn = np.sqrt((lo * lc).clip(lower=0).rolling(63, min_periods=21).mean())
    b = np.log((up + 1e-9) / (dn + 1e-9))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS vol acceleration: change in 63d RS log-slope over a month (range jerk, RS)
def f10rv_f10_range_vol_estimators_rsaccel_63d_base_v091_signal(open, high, low, close):
    rs = _f10_rs_vol(open, high, low, close, 63)
    slope = np.log(rs.replace(0, np.nan) / rs.shift(21).replace(0, np.nan))
    b = slope - slope.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS vol slope over a quarter (long range-vol momentum)
def f10rv_f10_range_vol_estimators_rsslope_63d_base_v092_signal(open, high, low, close, closeadj):
    rs = _f10_rs_vol(open, high, low, close, 63) / closeadj.replace(0, np.nan)
    b = np.log(rs.replace(0, np.nan) / rs.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS vol kurtosis of daily terms over 63d (range fat-tails, RS variant)
def f10rv_f10_range_vol_estimators_rskurt_63d_base_v093_signal(open, high, low, close):
    t = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0)
    b = t.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS vs Parkinson divergence: drift-robust vs symmetric estimator gap (63d)
def f10rv_f10_range_vol_estimators_rspkspread_63d_base_v094_signal(open, high, low, close):
    rs = _f10_rs_vol(open, high, low, close, 63)
    pk = _f10_pk_vol(high, low, 63)
    b = (rs - pk) / (rs + pk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Yang-Zhang & overnight structures (95-108) ----

# overnight-vol vs intraday-RS-vol ratio over 21d (gap-risk dominance, short)
def f10rv_f10_range_vol_estimators_ovintraratio_21d_base_v095_signal(open, high, low, close):
    on = np.sqrt(_f10_overnight_term(open, close).rolling(21, min_periods=10).mean())
    intr = _f10_rs_vol(open, high, low, close, 21)
    b = on / intr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap-vol slope: change in 63d overnight vol over a month
def f10rv_f10_range_vol_estimators_ovslope_63d_base_v096_signal(open, close):
    on = np.sqrt(_f10_overnight_term(open, close).rolling(63, min_periods=21).mean())
    b = np.log(on.replace(0, np.nan) / on.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ vol compression depth: how far 21d YZ vol is below its 126d 25th percentile
def f10rv_f10_range_vol_estimators_yzcompress_21d_base_v097_signal(open, high, low, close):
    yz = _f10_yz_vol(open, high, low, close, 21)
    q25 = yz.rolling(126, min_periods=63).quantile(0.25)
    b = (q25 - yz) / q25.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ-minus-GK estimator gap (63d): incremental overnight/open info over GK
def f10rv_f10_range_vol_estimators_yzgkspread_63d_base_v098_signal(open, high, low, close):
    yz = _f10_yz_vol(open, high, low, close, 63)
    gk = _f10_gk_vol(open, high, low, close, 63)
    b = (yz - gk) / (yz + gk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-vol z-score change: acceleration of gap-risk regime (63d z, 21d diff)
def f10rv_f10_range_vol_estimators_ovzaccel_base_v099_signal(open, close):
    on = np.sqrt(_f10_overnight_term(open, close).rolling(63, min_periods=21).mean())
    z = _z(on, 252)
    b = z - z.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- ATR & true-range structures (100-118) ----

# ATR% regime position within 252d band
def f10rv_f10_range_vol_estimators_atrconepos_21d_base_v100_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    hi = atrp.rolling(252, min_periods=126).max()
    lo = atrp.rolling(252, min_periods=126).min()
    b = (atrp - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR% acceleration: change in 14d ATR slope over two weeks
def f10rv_f10_range_vol_estimators_atraccel_14d_base_v101_signal(high, low, close):
    atr = _f10_atr(high, low, close, 14)
    slope = np.log(atr.replace(0, np.nan) / atr.shift(5).replace(0, np.nan))
    b = slope - slope.shift(10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR% risk-adjusted momentum: 21d return per 21d ATR%
def f10rv_f10_range_vol_estimators_atrmom_21d_base_v102_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    ret = (close / close.shift(21) - 1.0)
    b = ret / atrp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Chande-style range expansion: sum of up-true-range vs down-true-range over 21d
def f10rv_f10_range_vol_estimators_trdir_21d_base_v103_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    up = close > close.shift(1)
    su = tr.where(up).rolling(21, min_periods=8).sum()
    sd = tr.where(~up).rolling(21, min_periods=8).sum()
    b = (su - sd) / (su + sd).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range stability: ATR-to-range-std ratio over 63d (smooth vs erratic range)
def f10rv_f10_range_vol_estimators_trstab_63d_base_v104_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    m = tr.rolling(63, min_periods=21).mean()
    s = tr.rolling(63, min_periods=21).std()
    b = m / s.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized average true range slope vs price slope (range vs trend, 21d)
def f10rv_f10_range_vol_estimators_trvspx_21d_base_v105_signal(high, low, close):
    atrslope = np.log(_f10_atr(high, low, close, 21).replace(0, np.nan)
                      / _f10_atr(high, low, close, 21).shift(21).replace(0, np.nan))
    pxslope = np.log(close.replace(0, np.nan) / close.shift(21).replace(0, np.nan))
    b = atrslope - pxslope
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range percentile rank vs 252d history, smoothed 5d (range regime, smoothed)
def f10rv_f10_range_vol_estimators_trrank_63d_base_v106_signal(high, low, close):
    trp = (_f10_true_range(high, low, close) / close.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = _rank(trp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 63d range traversed by the single widest day (range concentration)
def f10rv_f10_range_vol_estimators_trgini_63d_base_v107_signal(high, low, close):
    trp = _f10_true_range(high, low, close) / close.replace(0, np.nan)
    mx = trp.rolling(63, min_periods=21).max()
    s = trp.rolling(63, min_periods=21).sum()
    b = mx / s.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-to-Parkinson long ratio (linear vs log range estimator, 63d)
def f10rv_f10_range_vol_estimators_atrpk_63d_base_v108_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 63) / close.replace(0, np.nan)
    pkp = _f10_pk_vol(high, low, 63) / close.replace(0, np.nan)
    b = atrp / pkp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- high-low range vs close structures (109-122) ----

# high-low range % slope over a month (range trend)
def f10rv_f10_range_vol_estimators_hlrslope_21d_base_v109_signal(high, low, close):
    hl = ((high - low) / close.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = np.log(hl.replace(0, np.nan) / hl.shift(21).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range % regime position within 252d band
def f10rv_f10_range_vol_estimators_hlrconepos_63d_base_v110_signal(high, low, close):
    hl = ((high - low) / close.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    hi = hl.rolling(252, min_periods=126).max()
    lo = hl.rolling(252, min_periods=126).min()
    b = (hl - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close position in high-low range slope (where close settles, momentum, 21d)
def f10rv_f10_range_vol_estimators_clposslope_21d_base_v111_signal(high, low, close):
    pos = ((close - low) / (high - low).replace(0, np.nan)).rolling(21, min_periods=10).mean()
    b = pos - pos.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range gap vs body: (high-low) vs |close-open| over 21d (wick dominance)
def f10rv_f10_range_vol_estimators_wickdom_21d_base_v112_signal(open, high, low, close):
    rng = (high - low)
    body = (close - open).abs()
    wick = (rng - body).clip(lower=0)
    b = (wick / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range entropy proxy: dispersion of daily ranges over 63d (CoV)
def f10rv_f10_range_vol_estimators_hlrcov_63d_base_v113_signal(high, low, close):
    hl = (high - low) / close.replace(0, np.nan)
    m = hl.rolling(63, min_periods=21).mean()
    s = hl.rolling(63, min_periods=21).std()
    b = s / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-shadow vs lower-shadow vol asymmetry over 63d (range skew, intraday)
def f10rv_f10_range_vol_estimators_shadowvolasym_63d_base_v114_signal(open, high, low, close):
    upper = np.log(high.replace(0, np.nan) / np.maximum(open, close).replace(0, np.nan)).clip(lower=0)
    lower = np.log(np.minimum(open, close).replace(0, np.nan) / low.replace(0, np.nan)).clip(lower=0)
    su = np.sqrt((upper * upper).rolling(63, min_periods=21).mean())
    sl = np.sqrt((lower * lower).rolling(63, min_periods=21).mean())
    b = (su - sl) / (su + sl).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- cross-estimator & regime structures (115-150) ----

# Parkinson-to-close-to-close vol ratio (jump premium, 63d, normalized)
def f10rv_f10_range_vol_estimators_pkccratio_63d_base_v115_signal(high, low, closeadj):
    pk = _f10_pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    cc = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = pk / cc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vs-realized jump premium slope: change in PK/close-to-close ratio (63d)
def f10rv_f10_range_vol_estimators_jumppremslope_63d_base_v116_signal(high, low, closeadj):
    pk = _f10_pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    cc = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = pk / cc.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# three-estimator agreement: 1 - normalized dispersion of {PK,GK,RS} (model trust)
def f10rv_f10_range_vol_estimators_estagree_63d_base_v117_signal(open, high, low, close):
    pk = _f10_pk_vol(high, low, 63) / close.replace(0, np.nan)
    gk = _f10_gk_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    rs = _f10_rs_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    st = pd.concat([pk, gk, rs], axis=1)
    b = st.std(axis=1) / st.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# estimator-dispersion slope: change in cross-estimator disagreement over a month
def f10rv_f10_range_vol_estimators_estdispslope_63d_base_v118_signal(open, high, low, close):
    pk = _f10_pk_vol(high, low, 63) / close.replace(0, np.nan)
    gk = _f10_gk_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    rs = _f10_rs_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    disp = pd.concat([pk, gk, rs], axis=1).std(axis=1)
    b = disp - disp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ-to-Parkinson gap-premium slope: change in gap content over a quarter
def f10rv_f10_range_vol_estimators_yzpkslope_63d_base_v119_signal(open, high, low, close):
    yz = _f10_yz_vol(open, high, low, close, 63)
    pk = _f10_pk_vol(high, low, 63)
    ratio = yz / pk.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of Parkinson: std of 21d PK vol over 126d, normalized
def f10rv_f10_range_vol_estimators_volofpkvol_126d_base_v120_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    m = pk.rolling(126, min_periods=63).mean()
    b = pk.rolling(126, min_periods=63).std() / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol of ATR: std of 21d ATR% over 126d, normalized
def f10rv_f10_range_vol_estimators_volofatrvol_126d_base_v121_signal(high, low, close):
    atrp = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    m = atrp.rolling(126, min_periods=63).mean()
    b = atrp.rolling(126, min_periods=63).std() / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol regime flip count: standardized sign changes of 21d PK slope over 63d
def f10rv_f10_range_vol_estimators_pkflip_63d_base_v122_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    slope = np.log(pk.replace(0, np.nan) / pk.shift(5).replace(0, np.nan))
    flips = (np.sign(slope) != np.sign(slope.shift(1))).astype(float)
    raw = flips.rolling(63, min_periods=21).sum() / 63.0
    b = raw + 0.5 * slope.abs().rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-range vol vs upside-range vol via true-range on red/green days (63d)
def f10rv_f10_range_vol_estimators_trsemi_63d_base_v123_signal(high, low, close):
    tr = _f10_true_range(high, low, close) / close.replace(0, np.nan)
    up = close >= close.shift(1)
    vu = np.sqrt((tr * tr).where(up).rolling(63, min_periods=21).mean())
    vd = np.sqrt((tr * tr).where(~up).rolling(63, min_periods=21).mean())
    b = (vd - vu) / (vd + vu).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol term-structure curvature: 21/63/252 PK convexity, normalized
def f10rv_f10_range_vol_estimators_pkconv_base_v124_signal(high, low):
    s = _f10_pk_vol(high, low, 21)
    m = _f10_pk_vol(high, low, 63)
    l = _f10_pk_vol(high, low, 252)
    b = (s - 2.0 * m + l) / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol term-structure curvature for GK (21/63/252 convexity)
def f10rv_f10_range_vol_estimators_gkconv_base_v125_signal(open, high, low, close):
    s = _f10_gk_vol(open, high, low, close, 21)
    m = _f10_gk_vol(open, high, low, close, 63)
    l = _f10_gk_vol(open, high, low, close, 252)
    b = (s - 2.0 * m + l) / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR Keltner-style band width vs price (range-vol envelope, 21d)
def f10rv_f10_range_vol_estimators_keltner_21d_base_v126_signal(high, low, close):
    atr = _f10_atr(high, low, close, 21)
    ema = close.ewm(span=21, min_periods=10).mean()
    b = (2.0 * atr) / ema.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol vs trend efficiency: PK vol over net move per total range traveled (63d)
def f10rv_f10_range_vol_estimators_pkchop_63d_base_v127_signal(high, low, closeadj):
    pk = _f10_pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    net = (closeadj / closeadj.shift(63) - 1.0).abs()
    b = pk / (net.replace(0, np.nan) + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight share of true range over 63d (how much TR is gap vs intraday)
def f10rv_f10_range_vol_estimators_trgapshare_63d_base_v128_signal(high, low, close):
    tr = _f10_true_range(high, low, close)
    hl = (high - low)
    gap = (tr - hl).clip(lower=0)
    b = (gap.rolling(63, min_periods=21).sum()
         / tr.rolling(63, min_periods=21).sum().replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol skew over windows: 21d PK minus median of 21d PK over 252d, scaled
def f10rv_f10_range_vol_estimators_pkmedgap_21d_base_v129_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    med = pk.rolling(252, min_periods=126).median()
    iqr = (pk.rolling(252, min_periods=126).quantile(0.75)
           - pk.rolling(252, min_periods=126).quantile(0.25))
    b = (pk - med) / iqr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol robust z (median/IQR) over 252d
def f10rv_f10_range_vol_estimators_gkrobz_63d_base_v130_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    med = gk.rolling(252, min_periods=126).median()
    iqr = (gk.rolling(252, min_periods=126).quantile(0.75)
           - gk.rolling(252, min_periods=126).quantile(0.25))
    b = (gk - med) / iqr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion breakout: today's TR vs the 63d max TR (new-range-high proximity)
def f10rv_f10_range_vol_estimators_trbreakout_63d_base_v131_signal(high, low, close):
    tr = _f10_true_range(high, low, close) / close.replace(0, np.nan)
    mx = tr.rolling(63, min_periods=21).max()
    b = (tr / mx.replace(0, np.nan)).rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze depth: how far 21d PK vol sits below its 126d 25th percentile (compression)
def f10rv_f10_range_vol_estimators_pksqueeze_21d_base_v132_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    q25 = pk.rolling(126, min_periods=63).quantile(0.25)
    b = (q25 - pk) / q25.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-after-squeeze: 5d PK relative to the 63d-min PK (release pressure)
def f10rv_f10_range_vol_estimators_pkrelease_base_v133_signal(high, low):
    fast = _f10_pk_vol(high, low, 5)
    floor = _f10_pk_vol(high, low, 21).rolling(63, min_periods=21).min()
    b = fast / floor.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional range bias: signed range weighted by close-vs-open over 21d
def f10rv_f10_range_vol_estimators_dirrange_21d_base_v134_signal(open, high, low, close):
    rng = (high - low) / close.replace(0, np.nan)
    sign = np.sign(close - open)
    b = (sign * rng).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol beta to its own lag: persistence regression slope of 21d PK over 126d
def f10rv_f10_range_vol_estimators_pkpersist_126d_base_v135_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    b = pk.rolling(126, min_periods=63).corr(pk.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK-vs-ATR estimator gap slope: change in (GK/ATR) over a quarter
def f10rv_f10_range_vol_estimators_gkatrslope_63d_base_v136_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63) / close.replace(0, np.nan)
    atrp = _f10_atr(high, low, close, 63) / close.replace(0, np.nan)
    ratio = gk / atrp.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed Parkinson vol shock: bounded single-day PK term z (63d)
def f10rv_f10_range_vol_estimators_pkshocktanh_base_v137_signal(high, low):
    t = _f10_parkinson_term(high, low)
    z = _z(t, 63)
    b = np.tanh(0.5 * z)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol regime z over a long window: 63d PK z vs 504d history (structural)
def f10rv_f10_range_vol_estimators_pkz_504d_base_v138_signal(high, low, closeadj):
    pk = _f10_pk_vol(high, low, 63) / closeadj.replace(0, np.nan)
    b = _z(pk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vol kurtosis: tail-heaviness of gap returns over 63d (gap shocks)
def f10rv_f10_range_vol_estimators_ovkurt_63d_base_v139_signal(open, close):
    o = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    b = o.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday vol kurtosis: tail-heaviness of close-to-open returns over 63d
def f10rv_f10_range_vol_estimators_intrakurt_63d_base_v140_signal(open, close):
    c = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    b = c.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol asymmetry: PK term on high-close days vs low-close days (63d)
def f10rv_f10_range_vol_estimators_pkclposasym_63d_base_v141_signal(high, low, close):
    t = _f10_parkinson_term(high, low)
    pos = (close - low) / (high - low).replace(0, np.nan)
    top = pos > 0.5
    vt = np.sqrt(t.where(top).rolling(63, min_periods=21).mean())
    vb = np.sqrt(t.where(~top).rolling(63, min_periods=21).mean())
    b = (vt - vb) / (vt + vb).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR-normalized return dispersion: std of (daily move/ATR) over 21d (risk units)
def f10rv_f10_range_vol_estimators_atrunitdisp_21d_base_v142_signal(high, low, close):
    atr = _f10_atr(high, low, close, 21)
    move = (close - close.shift(1))
    u = move / atr.replace(0, np.nan)
    b = u.rolling(21, min_periods=10).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol long-vs-short crossover momentum (GK 5d EWMA vs 63d SMA, slope)
def f10rv_f10_range_vol_estimators_gkcrossmom_base_v143_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    fast = np.sqrt(t.ewm(span=5, min_periods=3).mean())
    slow = np.sqrt(t.rolling(63, min_periods=21).mean())
    cross = fast / slow.replace(0, np.nan) - 1.0
    b = cross - cross.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-vol vs total-vol ratio slope: change in overnight share of YZ vol (63d)
def f10rv_f10_range_vol_estimators_yzgaploadslope_63d_base_v144_signal(open, high, low, close):
    on = _f10_overnight_term(open, close).rolling(63, min_periods=21).mean()
    rs = _f10_rogers_satchell_term(open, high, low, close).clip(lower=0).rolling(63, min_periods=21).mean()
    load = on / (on + rs).replace(0, np.nan)
    b = load - load.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol mean-reversion target gap: 21d ATR% minus 252d ATR%, in 252d-vol units
def f10rv_f10_range_vol_estimators_atrmrz_base_v145_signal(high, low, close, closeadj):
    s = _f10_atr(high, low, close, 21) / close.replace(0, np.nan)
    l = (_f10_atr(high, low, close, 252) / closeadj.replace(0, np.nan))
    gap = s - l
    b = gap / gap.rolling(252, min_periods=126).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range autocorrelation over 126d (range clustering, long)
def f10rv_f10_range_vol_estimators_hlracf_126d_base_v146_signal(high, low, close):
    hl = (high - low) / close.replace(0, np.nan)
    b = hl.rolling(126, min_periods=63).corr(hl.shift(5))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# estimator-spread regime: (GK-PK)/(GK+PK) z over 252d (jump-regime detector)
def f10rv_f10_range_vol_estimators_gkpkspreadz_base_v147_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    pk = _f10_pk_vol(high, low, 63)
    spr = (gk - pk) / (gk + pk).replace(0, np.nan)
    b = _z(spr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK range-vol drawdown: time spent within 10% of the 252d GK-vol peak (63d)
def f10rv_f10_range_vol_estimators_gkvolpeaktime_base_v148_signal(open, high, low, close):
    gk = _f10_gk_vol(open, high, low, close, 63)
    peak = gk.rolling(252, min_periods=126).max()
    near = (gk >= 0.9 * peak).astype(float)
    raw = near.rolling(63, min_periods=21).mean()
    b = raw + 0.5 * (gk / peak.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol expansion breadth: fraction of last 63d the 21d PK rose week-over-week
def f10rv_f10_range_vol_estimators_pkexpbreadth_base_v149_signal(high, low):
    pk = _f10_pk_vol(high, low, 21)
    step = np.log(pk.replace(0, np.nan) / pk.shift(5).replace(0, np.nan))
    pos = step.clip(lower=0).rolling(63, min_periods=21).mean()
    neg = (-step).clip(lower=0).rolling(63, min_periods=21).mean()
    b = pos / (pos + neg).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite range-vol pressure: GK semivariance bias x range-expansion regime (63d)
def f10rv_f10_range_vol_estimators_rvpressure_63d_base_v150_signal(open, high, low, close):
    t = _f10_garman_klass_term(open, high, low, close).clip(lower=0)
    up = close >= open
    vu = np.sqrt(t.where(up).rolling(63, min_periods=21).mean())
    vd = np.sqrt(t.where(~up).rolling(63, min_periods=21).mean())
    bias = (vd - vu) / (vd + vu).replace(0, np.nan)
    hl = ((high - low) / close.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    expand = hl / hl.rolling(126, min_periods=63).mean().replace(0, np.nan) - 1.0
    b = bias * expand
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_range_vol_estimators_pkmomratio_21d_base_v076_signal,
    f10rv_f10_range_vol_estimators_pkewmsma_base_v077_signal,
    f10rv_f10_range_vol_estimators_pkstab_63d_base_v078_signal,
    f10rv_f10_range_vol_estimators_pkjump_21d_base_v079_signal,
    f10rv_f10_range_vol_estimators_pkstretch_63d_base_v080_signal,
    f10rv_f10_range_vol_estimators_pkcompress_63d_base_v081_signal,
    f10rv_f10_range_vol_estimators_pkconepos_63d_base_v082_signal,
    f10rv_f10_range_vol_estimators_pkaccel_21d_base_v083_signal,
    f10rv_f10_range_vol_estimators_gkmomratio_63d_base_v084_signal,
    f10rv_f10_range_vol_estimators_gkconepos_63d_base_v085_signal,
    f10rv_f10_range_vol_estimators_gkstab_63d_base_v086_signal,
    f10rv_f10_range_vol_estimators_gkmrz_base_v087_signal,
    f10rv_f10_range_vol_estimators_gksemi_63d_base_v088_signal,
    f10rv_f10_range_vol_estimators_gkewmdiv_base_v089_signal,
    f10rv_f10_range_vol_estimators_rsupdown_63d_base_v090_signal,
    f10rv_f10_range_vol_estimators_rsaccel_63d_base_v091_signal,
    f10rv_f10_range_vol_estimators_rsslope_63d_base_v092_signal,
    f10rv_f10_range_vol_estimators_rskurt_63d_base_v093_signal,
    f10rv_f10_range_vol_estimators_rspkspread_63d_base_v094_signal,
    f10rv_f10_range_vol_estimators_ovintraratio_21d_base_v095_signal,
    f10rv_f10_range_vol_estimators_ovslope_63d_base_v096_signal,
    f10rv_f10_range_vol_estimators_yzcompress_21d_base_v097_signal,
    f10rv_f10_range_vol_estimators_yzgkspread_63d_base_v098_signal,
    f10rv_f10_range_vol_estimators_ovzaccel_base_v099_signal,
    f10rv_f10_range_vol_estimators_atrconepos_21d_base_v100_signal,
    f10rv_f10_range_vol_estimators_atraccel_14d_base_v101_signal,
    f10rv_f10_range_vol_estimators_atrmom_21d_base_v102_signal,
    f10rv_f10_range_vol_estimators_trdir_21d_base_v103_signal,
    f10rv_f10_range_vol_estimators_trstab_63d_base_v104_signal,
    f10rv_f10_range_vol_estimators_trvspx_21d_base_v105_signal,
    f10rv_f10_range_vol_estimators_trrank_63d_base_v106_signal,
    f10rv_f10_range_vol_estimators_trgini_63d_base_v107_signal,
    f10rv_f10_range_vol_estimators_atrpk_63d_base_v108_signal,
    f10rv_f10_range_vol_estimators_hlrslope_21d_base_v109_signal,
    f10rv_f10_range_vol_estimators_hlrconepos_63d_base_v110_signal,
    f10rv_f10_range_vol_estimators_clposslope_21d_base_v111_signal,
    f10rv_f10_range_vol_estimators_wickdom_21d_base_v112_signal,
    f10rv_f10_range_vol_estimators_hlrcov_63d_base_v113_signal,
    f10rv_f10_range_vol_estimators_shadowvolasym_63d_base_v114_signal,
    f10rv_f10_range_vol_estimators_pkccratio_63d_base_v115_signal,
    f10rv_f10_range_vol_estimators_jumppremslope_63d_base_v116_signal,
    f10rv_f10_range_vol_estimators_estagree_63d_base_v117_signal,
    f10rv_f10_range_vol_estimators_estdispslope_63d_base_v118_signal,
    f10rv_f10_range_vol_estimators_yzpkslope_63d_base_v119_signal,
    f10rv_f10_range_vol_estimators_volofpkvol_126d_base_v120_signal,
    f10rv_f10_range_vol_estimators_volofatrvol_126d_base_v121_signal,
    f10rv_f10_range_vol_estimators_pkflip_63d_base_v122_signal,
    f10rv_f10_range_vol_estimators_trsemi_63d_base_v123_signal,
    f10rv_f10_range_vol_estimators_pkconv_base_v124_signal,
    f10rv_f10_range_vol_estimators_gkconv_base_v125_signal,
    f10rv_f10_range_vol_estimators_keltner_21d_base_v126_signal,
    f10rv_f10_range_vol_estimators_pkchop_63d_base_v127_signal,
    f10rv_f10_range_vol_estimators_trgapshare_63d_base_v128_signal,
    f10rv_f10_range_vol_estimators_pkmedgap_21d_base_v129_signal,
    f10rv_f10_range_vol_estimators_gkrobz_63d_base_v130_signal,
    f10rv_f10_range_vol_estimators_trbreakout_63d_base_v131_signal,
    f10rv_f10_range_vol_estimators_pksqueeze_21d_base_v132_signal,
    f10rv_f10_range_vol_estimators_pkrelease_base_v133_signal,
    f10rv_f10_range_vol_estimators_dirrange_21d_base_v134_signal,
    f10rv_f10_range_vol_estimators_pkpersist_126d_base_v135_signal,
    f10rv_f10_range_vol_estimators_gkatrslope_63d_base_v136_signal,
    f10rv_f10_range_vol_estimators_pkshocktanh_base_v137_signal,
    f10rv_f10_range_vol_estimators_pkz_504d_base_v138_signal,
    f10rv_f10_range_vol_estimators_ovkurt_63d_base_v139_signal,
    f10rv_f10_range_vol_estimators_intrakurt_63d_base_v140_signal,
    f10rv_f10_range_vol_estimators_pkclposasym_63d_base_v141_signal,
    f10rv_f10_range_vol_estimators_atrunitdisp_21d_base_v142_signal,
    f10rv_f10_range_vol_estimators_gkcrossmom_base_v143_signal,
    f10rv_f10_range_vol_estimators_yzgaploadslope_63d_base_v144_signal,
    f10rv_f10_range_vol_estimators_atrmrz_base_v145_signal,
    f10rv_f10_range_vol_estimators_hlracf_126d_base_v146_signal,
    f10rv_f10_range_vol_estimators_gkpkspreadz_base_v147_signal,
    f10rv_f10_range_vol_estimators_gkvolpeaktime_base_v148_signal,
    f10rv_f10_range_vol_estimators_pkexpbreadth_base_v149_signal,
    f10rv_f10_range_vol_estimators_rvpressure_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RANGE_VOL_ESTIMATORS_REGISTRY_076_150 = REGISTRY


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

    print("OK f10_range_vol_estimators_base_076_150_claude: %d features pass" % n_features)
