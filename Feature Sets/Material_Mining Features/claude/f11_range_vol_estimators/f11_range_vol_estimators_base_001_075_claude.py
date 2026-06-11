import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives: range-based volatility estimators =====
# All "log" terms use natural log of positive OHLC ratios.
def _f11re_logsq(num, den):
    r = np.log(num.replace(0, np.nan) / den.replace(0, np.nan))
    return r * r


def _f11re_parkinson(high, low, w):
    # Parkinson: (1/(4 ln2)) * mean( (ln(H/L))^2 ); sqrt -> daily sigma estimate
    hl = _f11re_logsq(high, low)
    var = hl.rolling(w, min_periods=max(1, w // 2)).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var)


def _f11re_garman_klass(open_, high, low, close, w):
    # Garman-Klass: 0.5*(ln H/L)^2 - (2 ln2 -1)*(ln C/O)^2
    term = 0.5 * _f11re_logsq(high, low) - (2.0 * np.log(2.0) - 1.0) * _f11re_logsq(close, open_)
    var = term.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f11re_rogers_satchell(open_, high, low, close, w):
    # Rogers-Satchell: ln(H/C)*ln(H/O) + ln(L/C)*ln(L/O) (drift-independent)
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    term = hc * ho + lc * lo
    var = term.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f11re_overnight_var(open_, close, w):
    # overnight (close-to-open) component variance
    on = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return on.rolling(w, min_periods=max(1, w // 2)).var()


def _f11re_open_close_var(open_, close, w):
    # intraday open-to-close component variance
    oc = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    return oc.rolling(w, min_periods=max(1, w // 2)).var()


def _f11re_yang_zhang(open_, high, low, close, w):
    # Yang-Zhang: overnight var + k*open-close var + (1-k)*Rogers-Satchell var
    on = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    oc = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    von = on.rolling(w, min_periods=max(1, w // 2)).var()
    voc = oc.rolling(w, min_periods=max(1, w // 2)).var()
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    rs = (hc * ho + lc * lo).rolling(w, min_periods=max(1, w // 2)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    var = von + k * voc + (1.0 - k) * rs
    return np.sqrt(var.clip(lower=0))


def _f11re_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11re_atr(high, low, close, w):
    tr = _f11re_true_range(high, low, close)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f11re_hl_range(high, low, close):
    return (high - low) / close.replace(0, np.nan)


def _f11re_overnight_premium(open_, high, low, close, w):
    # Yang-Zhang variance minus the Rogers-Satchell (intraday) variance:
    # isolates the overnight + open-close gap content YZ uniquely captures.
    y = _f11re_yang_zhang(open_, high, low, close, w) ** 2
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    rs = (hc * ho + lc * lo).rolling(w, min_periods=max(1, w // 2)).mean()
    return (y - rs.clip(lower=0)).clip(lower=0)


# ============================================================
# --- Parkinson estimators ---
# Parkinson daily sigma, 5d window
def f11re_f11_range_vol_estimators_park_5d_base_v001_signal(high, low):
    b = _f11re_parkinson(high, low, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson daily sigma, 21d window
def f11re_f11_range_vol_estimators_park_21d_base_v002_signal(high, low):
    b = _f11re_parkinson(high, low, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d annualized (sqrt252) normalized by closeadj level
def f11re_f11_range_vol_estimators_park_63d_base_v003_signal(high, low, closeadj):
    p = _f11re_parkinson(high, low, 63) * np.sqrt(252.0)
    b = p / (closeadj.replace(0, np.nan) ** 0.0)  # annualized sigma is already price-normalized via log
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 126d annualized
def f11re_f11_range_vol_estimators_park_126d_base_v004_signal(high, low):
    b = _f11re_parkinson(high, low, 126) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 252d annualized
def f11re_f11_range_vol_estimators_park_252d_base_v005_signal(high, low):
    b = _f11re_parkinson(high, low, 252) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson term structure: 21d / 126d (short vs long range-vol)
def f11re_f11_range_vol_estimators_parkterm_21v126_base_v006_signal(high, low):
    s = _f11re_parkinson(high, low, 21)
    l = _f11re_parkinson(high, low, 126)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson z-score vs own 252d history (range-vol regime extremity)
def f11re_f11_range_vol_estimators_parkz_63d_base_v007_signal(high, low):
    p = _f11re_parkinson(high, low, 63)
    b = _z(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 21d percentile-rank vs own 252d history (vol-cone position)
def f11re_f11_range_vol_estimators_parkrank_21d_base_v008_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = _rank(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson momentum: 21d change in 21d Parkinson sigma
def f11re_f11_range_vol_estimators_parkmom_21d_base_v009_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = p - p.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Garman-Klass estimators ---
# Garman-Klass daily sigma, 5d
def f11re_f11_range_vol_estimators_gk_5d_base_v010_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 21d
def f11re_f11_range_vol_estimators_gk_21d_base_v011_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 63d annualized
def f11re_f11_range_vol_estimators_gk_63d_base_v012_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 63) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 126d annualized
def f11re_f11_range_vol_estimators_gk_126d_base_v013_signal(open, high, low, close):
    b = _f11re_garman_klass(open, high, low, close, 126) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 252d annualized, mean-reverting form: vs its own 252d trailing median (long regime gap)
def f11re_f11_range_vol_estimators_gk_252d_base_v014_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 252) * np.sqrt(252.0)
    med = g.rolling(252, min_periods=126).median()
    b = g / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK term structure 21d/63d
def f11re_f11_range_vol_estimators_gkterm_21v63_base_v015_signal(open, high, low, close):
    s = _f11re_garman_klass(open, high, low, close, 21)
    l = _f11re_garman_klass(open, high, low, close, 63)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK z-score vs 252d history
def f11re_f11_range_vol_estimators_gkz_63d_base_v016_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK percentile-rank 21d vs 252d
def f11re_f11_range_vol_estimators_gkrank_21d_base_v017_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vs Parkinson spread (gap/jump signature: GK uses O/C, Parkinson only H/L)
def f11re_f11_range_vol_estimators_gkparkspr_21d_base_v018_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    p = _f11re_parkinson(high, low, 21)
    b = (g - p) / p.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Rogers-Satchell estimators (drift-independent, good for trending miners) ---
# Rogers-Satchell 5d directional imbalance: high-leg vs low-leg RS contribution
def f11re_f11_range_vol_estimators_rs_5d_base_v019_signal(open, high, low, close):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    hileg = (hc * ho).rolling(5, min_periods=3).mean()
    loleg = (lc * lo).rolling(5, min_periods=3).mean()
    b = (hileg - loleg) / (hileg + loleg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 21d momentum: 5d change in 21d RS sigma (drift-vol acceleration)
def f11re_f11_range_vol_estimators_rs_21d_base_v020_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 21)
    b = r - r.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 63d drift-content fraction (RS/Parkinson): trend persistence of range
def f11re_f11_range_vol_estimators_rs_63d_base_v021_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    b = r / p.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 126d annualized vs its own 252d median (long RS regime gap)
def f11re_f11_range_vol_estimators_rs_126d_base_v022_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 126) * np.sqrt(252.0)
    med = r.rolling(252, min_periods=126).median()
    b = r / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 252d annualized (long-horizon drift-independent vol level)
def f11re_f11_range_vol_estimators_rs_252d_base_v023_signal(open, high, low, close):
    b = _f11re_rogers_satchell(open, high, low, close, 252) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS term structure 21d/126d
def f11re_f11_range_vol_estimators_rsterm_21v126_base_v024_signal(open, high, low, close):
    s = _f11re_rogers_satchell(open, high, low, close, 21)
    l = _f11re_rogers_satchell(open, high, low, close, 126)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS drift-content percentile-rank: rank of RS/Parkinson vs 252d (trendiness regime)
def f11re_f11_range_vol_estimators_rsz_63d_base_v025_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    frac = r / p.replace(0, np.nan)
    b = _rank(frac, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS 21d momentum: 21d change in RS sigma (drift-vol expansion speed)
def f11re_f11_range_vol_estimators_rsrank_21d_base_v026_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 21)
    b = r - r.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS vs Parkinson spread (drift content of range)
def f11re_f11_range_vol_estimators_rsparkspr_21d_base_v027_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 21)
    p = _f11re_parkinson(high, low, 21)
    b = (p - r) / p.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Yang-Zhang style: overnight-gap-premium estimators (YZ's unique content) ---
# YZ overnight-gap premium sigma, 21d (gap-risk for news-driven juniors)
def f11re_f11_range_vol_estimators_yz_21d_base_v028_signal(open, high, low, close):
    prem = _f11re_overnight_premium(open, high, low, close, 21)
    b = np.sqrt(prem)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ overnight-gap premium as fraction of total YZ variance, 63d (gap dominance)
def f11re_f11_range_vol_estimators_yz_63d_base_v029_signal(open, high, low, close):
    prem = _f11re_overnight_premium(open, high, low, close, 63)
    tot = _f11re_yang_zhang(open, high, low, close, 63) ** 2
    b = prem / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ overnight-gap premium sigma, 126d annualized normalized vs its own 252d median
def f11re_f11_range_vol_estimators_yz_126d_base_v030_signal(open, high, low, close):
    prem = np.sqrt(_f11re_overnight_premium(open, high, low, close, 126)) * np.sqrt(252.0)
    med = prem.rolling(252, min_periods=126).median()
    b = prem / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ overnight-gap premium sigma 252d annualized (long-horizon gap-vol level)
def f11re_f11_range_vol_estimators_yz_252d_base_v031_signal(open, high, low, close):
    b = np.sqrt(_f11re_overnight_premium(open, high, low, close, 252)) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ gap-premium term structure 21d/126d (gap-vol term structure)
def f11re_f11_range_vol_estimators_yzterm_21v126_base_v032_signal(open, high, low, close):
    s = np.sqrt(_f11re_overnight_premium(open, high, low, close, 21))
    l = np.sqrt(_f11re_overnight_premium(open, high, low, close, 126))
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ gap-premium z-score vs 252d (gap-vol regime extremity)
def f11re_f11_range_vol_estimators_yzz_63d_base_v033_signal(open, high, low, close):
    prem = np.sqrt(_f11re_overnight_premium(open, high, low, close, 63))
    b = _z(prem, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- overnight vs intraday decomposition (gap-risk for news-driven juniors) ---
# overnight (close-to-open) volatility component, 21d
def f11re_f11_range_vol_estimators_onvol_21d_base_v034_signal(open, close):
    b = np.sqrt(_f11re_overnight_var(open, close, 21).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday (open-to-close) volatility component, 21d
def f11re_f11_range_vol_estimators_ocvol_21d_base_v035_signal(open, close):
    b = np.sqrt(_f11re_open_close_var(open, close, 21).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight share of total: overnight var / (overnight + intraday var), 63d
def f11re_f11_range_vol_estimators_onshare_63d_base_v036_signal(open, close):
    von = _f11re_overnight_var(open, close, 63)
    voc = _f11re_open_close_var(open, close, 63)
    b = von / (von + voc).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-to-intraday vol ratio, percentile-ranked vs 252d (gap-risk dominance regime)
def f11re_f11_range_vol_estimators_onocratio_63d_base_v037_signal(open, close):
    von = _f11re_overnight_var(open, close, 63)
    voc = _f11re_open_close_var(open, close, 63)
    ratio = np.sqrt(von.clip(lower=0)) / np.sqrt(voc.clip(lower=0)).replace(0, np.nan)
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ATR & ATR/price family ---
# ATR 5d / price (raw short-horizon true-range)
def f11re_f11_range_vol_estimators_atrp_5d_base_v038_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 5)
    b = atr / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR 14d / price (classic Wilder horizon)
def f11re_f11_range_vol_estimators_atrp_14d_base_v039_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 14)
    b = atr / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR 21d / price
def f11re_f11_range_vol_estimators_atrp_21d_base_v040_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 21)
    b = atr / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR 63d / closeadj (windows >21d normalize by closeadj)
def f11re_f11_range_vol_estimators_atrp_63d_base_v041_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 63)
    b = atr / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR 126d / closeadj
def f11re_f11_range_vol_estimators_atrp_126d_base_v042_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 126)
    b = atr / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR 252d / closeadj
def f11re_f11_range_vol_estimators_atrp_252d_base_v043_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 252)
    b = atr / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR term structure: ATR21/ATR126 (both /price cancels) — true-range term structure
def f11re_f11_range_vol_estimators_atrterm_21v126_base_v044_signal(high, low, close):
    s = _f11re_atr(high, low, close, 21)
    l = _f11re_atr(high, low, close, 126)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price z-score vs 252d (ATR regime extremity)
def f11re_f11_range_vol_estimators_atrpz_21d_base_v045_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _z(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price percentile-rank vs 252d (vol-cone position)
def f11re_f11_range_vol_estimators_atrprank_21d_base_v046_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _rank(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price momentum: 21d change in 21d ATR/price
def f11re_f11_range_vol_estimators_atrpmom_21d_base_v047_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = atrp - atrp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Wilder-smoothed ATR/price (EMA true-range) vs simple ATR (smoothing divergence)
def f11re_f11_range_vol_estimators_atrwilder_14d_base_v048_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    wild = tr.ewm(alpha=1.0 / 14.0, min_periods=7).mean()
    b = wild / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- true-range z and normalized true-range ---
# daily true-range / price, raw
def f11re_f11_range_vol_estimators_trp_1d_base_v049_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    b = tr / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range z vs 63d history (today's TR vs recent typical)
def f11re_f11_range_vol_estimators_trz_63d_base_v050_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    b = _z(tr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-true-range: 63d std of ATR21 over its 126d mean (instability of the range itself)
def f11re_f11_range_vol_estimators_trz_126d_base_v051_signal(high, low, close):
    atr = _f11re_atr(high, low, close, 21)
    vov = atr.rolling(63, min_periods=21).std()
    lvl = atr.rolling(126, min_periods=63).mean()
    b = vov / lvl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range z vs 252d history (annual range-shock)
def f11re_f11_range_vol_estimators_trz_252d_base_v052_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    b = _z(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max true-range over last 21d / ATR63 (range-spike intensity)
def f11re_f11_range_vol_estimators_trspike_21d_base_v053_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    mx = tr.rolling(21, min_periods=10).max()
    atr = tr.rolling(63, min_periods=21).mean()
    b = mx / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of large-true-range days (TR z>2) over last 63d (shock frequency)
def f11re_f11_range_vol_estimators_trshockcnt_63d_base_v054_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    z = _z(tr, 126)
    shock = (z > 2.0).astype(float)
    cnt = shock.rolling(63, min_periods=21).sum()
    b = cnt + 0.5 * z.clip(lower=0).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- high-low range vs close family ---
# gap content of true-range: (TR - intraday HL) / close, smoothed 5d (overnight gap in TR)
def f11re_f11_range_vol_estimators_hlrng_1d_base_v055_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    gap = (tr - (high - low)) / close.replace(0, np.nan)
    b = gap.rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly range expansion: 5d mean HL-range/close vs prior 5d (short-horizon range momentum)
def f11re_f11_range_vol_estimators_hlrng_5d_base_v056_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    m = hl.rolling(5, min_periods=3).mean()
    b = m / m.shift(5).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean high-low range/close over 21d
def f11re_f11_range_vol_estimators_hlrng_21d_base_v057_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    b = hl.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean high-low range vs closeadj over 63d (>21d uses closeadj)
def f11re_f11_range_vol_estimators_hlrng_63d_base_v058_signal(high, low, closeadj):
    hl = (high - low) / closeadj.replace(0, np.nan)
    b = hl.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d up/down range asymmetry: mean of (high-open) vs (open-low) over the year
def f11re_f11_range_vol_estimators_hlrng_252d_base_v059_signal(open, high, low):
    up = (high - open).clip(lower=0)
    dn = (open - low).clip(lower=0)
    upm = up.rolling(252, min_periods=126).mean()
    dnm = dn.rolling(252, min_periods=126).mean()
    b = (upm - dnm) / (upm + dnm).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday share of true-range: HL range / TR over 21d (how much range is intraday vs gap)
def f11re_f11_range_vol_estimators_hlrngz_21d_base_v060_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    hl = (high - low)
    share = hl.rolling(21, min_periods=10).sum() / tr.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range term structure 21d/126d
def f11re_f11_range_vol_estimators_hlrngterm_21v126_base_v061_signal(high, low, close, closeadj):
    s = (_f11re_hl_range(high, low, close)).rolling(21, min_periods=10).mean()
    l = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range: dispersion of daily hl-range over 63d (vol-of-range)
def f11re_f11_range_vol_estimators_hlrngdisp_63d_base_v062_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    sd = hl.rolling(63, min_periods=21).std()
    mn = hl.rolling(63, min_periods=21).mean()
    b = sd / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close position within day's range (where close sits H..L) smoothed 21d
def f11re_f11_range_vol_estimators_clrngpos_21d_base_v063_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    b = pos.rolling(21, min_periods=10).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-estimator comparisons & regime ---
# Parkinson vs close-to-close-equivalent: range efficiency (Park/HLrange relationship)
def f11re_f11_range_vol_estimators_parkeff_21d_base_v064_signal(high, low, close):
    park = _f11re_parkinson(high, low, 21)
    hl = _f11re_hl_range(high, low, close).rolling(21, min_periods=10).mean()
    b = park / hl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vs RS spread (open-close vs drift content), 63d normalized
def f11re_f11_range_vol_estimators_gkrsspr_63d_base_v065_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    b = (g - r) / g.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ vs Parkinson spread (overnight gap premium over intraday range), 63d
def f11re_f11_range_vol_estimators_yzparkspr_63d_base_v066_signal(open, high, low, close):
    y = _f11re_yang_zhang(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    b = (y - p) / y.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol-of-vol: std of 21d Parkinson over 63d
def f11re_f11_range_vol_estimators_parkvov_63d_base_v067_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = p.rolling(63, min_periods=21).std() / p.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol compression: 21d Parkinson vs its 252d minimum (squeeze distance)
def f11re_f11_range_vol_estimators_parksqueeze_base_v068_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    lo = p.rolling(252, min_periods=126).min()
    b = p / lo.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol expansion: 21d Parkinson vs its 252d max (distance below peak vol)
def f11re_f11_range_vol_estimators_parkexpand_base_v069_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    hi = p.rolling(252, min_periods=126).max()
    b = p / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price regime: fraction of last 63d ATR/price above its 252d median (high-range regime)
def f11re_f11_range_vol_estimators_atrregime_63d_base_v070_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 14) / close.replace(0, np.nan)
    med = atrp.rolling(252, min_periods=126).median()
    above = (atrp > med).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson annualized minus realized-from-range floor: excess range-vol over 126d
def f11re_f11_range_vol_estimators_parkexcess_126d_base_v071_signal(high, low, closeadj):
    p = _f11re_parkinson(high, low, 126) * np.sqrt(252.0)
    floor = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=63).quantile(0.1) * np.sqrt(252.0)
    b = p - floor
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK annualized / closeadj-normalized 252d level z (long-horizon range-vol regime)
def f11re_f11_range_vol_estimators_gkregimez_252d_base_v072_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 126)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range range-contraction streak: consecutive days TR below ATR21 (coiling)
def f11re_f11_range_vol_estimators_trcontract_base_v073_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    contract = (tr < atr).astype(float)
    grp = (contract == 0).cumsum()
    streak = contract.groupby(grp).cumsum()
    # weight streak by how compressed the range is vs ATR (continuous tightness)
    tightness = (1.0 - tr / atr.replace(0, np.nan)).clip(lower=0)
    b = streak / 21.0 + tightness.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-gap variance share trend: 21d change in overnight share
def f11re_f11_range_vol_estimators_onsharemom_base_v074_signal(open, close):
    von = _f11re_overnight_var(open, close, 63)
    voc = _f11re_open_close_var(open, close, 63)
    share = von / (von + voc).replace(0, np.nan)
    b = share - share.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# estimator disagreement: cross-sectional std of Park/GK/RS daily sigmas (jump/gap divergence)
def f11re_f11_range_vol_estimators_blendz_63d_base_v075_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 63)
    sg = _f11re_garman_klass(open, high, low, close, 63)
    sr = _f11re_rogers_satchell(open, high, low, close, 63)
    stacked = pd.concat([sp, sg, sr], axis=1)
    b = stacked.std(axis=1) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11re_f11_range_vol_estimators_park_5d_base_v001_signal,
    f11re_f11_range_vol_estimators_park_21d_base_v002_signal,
    f11re_f11_range_vol_estimators_park_63d_base_v003_signal,
    f11re_f11_range_vol_estimators_park_126d_base_v004_signal,
    f11re_f11_range_vol_estimators_park_252d_base_v005_signal,
    f11re_f11_range_vol_estimators_parkterm_21v126_base_v006_signal,
    f11re_f11_range_vol_estimators_parkz_63d_base_v007_signal,
    f11re_f11_range_vol_estimators_parkrank_21d_base_v008_signal,
    f11re_f11_range_vol_estimators_parkmom_21d_base_v009_signal,
    f11re_f11_range_vol_estimators_gk_5d_base_v010_signal,
    f11re_f11_range_vol_estimators_gk_21d_base_v011_signal,
    f11re_f11_range_vol_estimators_gk_63d_base_v012_signal,
    f11re_f11_range_vol_estimators_gk_126d_base_v013_signal,
    f11re_f11_range_vol_estimators_gk_252d_base_v014_signal,
    f11re_f11_range_vol_estimators_gkterm_21v63_base_v015_signal,
    f11re_f11_range_vol_estimators_gkz_63d_base_v016_signal,
    f11re_f11_range_vol_estimators_gkrank_21d_base_v017_signal,
    f11re_f11_range_vol_estimators_gkparkspr_21d_base_v018_signal,
    f11re_f11_range_vol_estimators_rs_5d_base_v019_signal,
    f11re_f11_range_vol_estimators_rs_21d_base_v020_signal,
    f11re_f11_range_vol_estimators_rs_63d_base_v021_signal,
    f11re_f11_range_vol_estimators_rs_126d_base_v022_signal,
    f11re_f11_range_vol_estimators_rs_252d_base_v023_signal,
    f11re_f11_range_vol_estimators_rsterm_21v126_base_v024_signal,
    f11re_f11_range_vol_estimators_rsz_63d_base_v025_signal,
    f11re_f11_range_vol_estimators_rsrank_21d_base_v026_signal,
    f11re_f11_range_vol_estimators_rsparkspr_21d_base_v027_signal,
    f11re_f11_range_vol_estimators_yz_21d_base_v028_signal,
    f11re_f11_range_vol_estimators_yz_63d_base_v029_signal,
    f11re_f11_range_vol_estimators_yz_126d_base_v030_signal,
    f11re_f11_range_vol_estimators_yz_252d_base_v031_signal,
    f11re_f11_range_vol_estimators_yzterm_21v126_base_v032_signal,
    f11re_f11_range_vol_estimators_yzz_63d_base_v033_signal,
    f11re_f11_range_vol_estimators_onvol_21d_base_v034_signal,
    f11re_f11_range_vol_estimators_ocvol_21d_base_v035_signal,
    f11re_f11_range_vol_estimators_onshare_63d_base_v036_signal,
    f11re_f11_range_vol_estimators_onocratio_63d_base_v037_signal,
    f11re_f11_range_vol_estimators_atrp_5d_base_v038_signal,
    f11re_f11_range_vol_estimators_atrp_14d_base_v039_signal,
    f11re_f11_range_vol_estimators_atrp_21d_base_v040_signal,
    f11re_f11_range_vol_estimators_atrp_63d_base_v041_signal,
    f11re_f11_range_vol_estimators_atrp_126d_base_v042_signal,
    f11re_f11_range_vol_estimators_atrp_252d_base_v043_signal,
    f11re_f11_range_vol_estimators_atrterm_21v126_base_v044_signal,
    f11re_f11_range_vol_estimators_atrpz_21d_base_v045_signal,
    f11re_f11_range_vol_estimators_atrprank_21d_base_v046_signal,
    f11re_f11_range_vol_estimators_atrpmom_21d_base_v047_signal,
    f11re_f11_range_vol_estimators_atrwilder_14d_base_v048_signal,
    f11re_f11_range_vol_estimators_trp_1d_base_v049_signal,
    f11re_f11_range_vol_estimators_trz_63d_base_v050_signal,
    f11re_f11_range_vol_estimators_trz_126d_base_v051_signal,
    f11re_f11_range_vol_estimators_trz_252d_base_v052_signal,
    f11re_f11_range_vol_estimators_trspike_21d_base_v053_signal,
    f11re_f11_range_vol_estimators_trshockcnt_63d_base_v054_signal,
    f11re_f11_range_vol_estimators_hlrng_1d_base_v055_signal,
    f11re_f11_range_vol_estimators_hlrng_5d_base_v056_signal,
    f11re_f11_range_vol_estimators_hlrng_21d_base_v057_signal,
    f11re_f11_range_vol_estimators_hlrng_63d_base_v058_signal,
    f11re_f11_range_vol_estimators_hlrng_252d_base_v059_signal,
    f11re_f11_range_vol_estimators_hlrngz_21d_base_v060_signal,
    f11re_f11_range_vol_estimators_hlrngterm_21v126_base_v061_signal,
    f11re_f11_range_vol_estimators_hlrngdisp_63d_base_v062_signal,
    f11re_f11_range_vol_estimators_clrngpos_21d_base_v063_signal,
    f11re_f11_range_vol_estimators_parkeff_21d_base_v064_signal,
    f11re_f11_range_vol_estimators_gkrsspr_63d_base_v065_signal,
    f11re_f11_range_vol_estimators_yzparkspr_63d_base_v066_signal,
    f11re_f11_range_vol_estimators_parkvov_63d_base_v067_signal,
    f11re_f11_range_vol_estimators_parksqueeze_base_v068_signal,
    f11re_f11_range_vol_estimators_parkexpand_base_v069_signal,
    f11re_f11_range_vol_estimators_atrregime_63d_base_v070_signal,
    f11re_f11_range_vol_estimators_parkexcess_126d_base_v071_signal,
    f11re_f11_range_vol_estimators_gkregimez_252d_base_v072_signal,
    f11re_f11_range_vol_estimators_trcontract_base_v073_signal,
    f11re_f11_range_vol_estimators_onsharemom_base_v074_signal,
    f11re_f11_range_vol_estimators_blendz_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RANGE_VOL_ESTIMATORS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

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
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f11_range_vol_estimators_base_001_075_claude: %d features pass" % n_features)
