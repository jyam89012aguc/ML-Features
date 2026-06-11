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
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives: range-based volatility estimators =====
# Pure range-vol building blocks (Parkinson / Garman-Klass / Rogers-Satchell /
# Yang-Zhang / ATR). >21d aggregates that need a level normalize by closeadj.
# NOTE: this family is RANGE-BASED VOLATILITY ESTIMATORS ONLY. It deliberately
# emits no close-location-in-range / CLV (that is f13) and no close-to-close
# single-window realized-vol levels (that is f10).
def _f11_log_hl(high, low):
    return np.log(high.replace(0, np.nan) / low.replace(0, np.nan))


def _f11_parkinson(high, low, w):
    r2 = _f11_log_hl(high, low) ** 2
    c = 1.0 / (4.0 * np.log(2.0))
    return np.sqrt((c * r2).rolling(w, min_periods=max(2, w // 2)).mean())


def _f11_gk_term(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    return 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2


def _f11_garman_klass(open, high, low, close, w):
    t = _f11_gk_term(open, high, low, close)
    return np.sqrt(t.rolling(w, min_periods=max(2, w // 2)).mean().clip(lower=0))


def _f11_rs_term(open, high, low, close):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    return hc * ho + lc * lo


def _f11_rogers_satchell(open, high, low, close, w):
    t = _f11_rs_term(open, high, low, close)
    return np.sqrt(t.rolling(w, min_periods=max(2, w // 2)).mean().clip(lower=0))


def _f11_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11_atr(high, low, close, w):
    return _f11_true_range(high, low, close).rolling(
        w, min_periods=max(2, w // 2)).mean()


def _f11_overnight(open, close):
    return np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))


def _f11_intraday(open, close):
    return np.log(close.replace(0, np.nan) / open.replace(0, np.nan))


def _f11_yang_zhang(open, high, low, close, w):
    o = _f11_overnight(open, close)
    c = _f11_intraday(open, close)
    vo = ((o - o.rolling(w, min_periods=max(2, w // 2)).mean()) ** 2).rolling(
        w, min_periods=max(2, w // 2)).mean()
    vc = ((c - c.rolling(w, min_periods=max(2, w // 2)).mean()) ** 2).rolling(
        w, min_periods=max(2, w // 2)).mean()
    rs = _f11_rs_term(open, high, low, close).rolling(
        w, min_periods=max(2, w // 2)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    return np.sqrt((vo + k * vc + (1.0 - k) * rs).clip(lower=0))


# ============================================================
# Parkinson volatility, 21d (raw range-vol level)
def f11re_f11_range_vol_estimators_park_21d_base_v001_signal(high, low):
    b = _f11_parkinson(high, low, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d normalized by closeadj level (>21d level estimator)
def f11re_f11_range_vol_estimators_park_63d_base_v002_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 63)
    b = pk / closeadj.replace(0, np.nan) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 126d vs 252d term-structure ratio (medium vs long range-vol curve)
def f11re_f11_range_vol_estimators_park_126d_base_v003_signal(high, low):
    s = _f11_parkinson(high, low, 126)
    l = _f11_parkinson(high, low, 252)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 252d de-meaned vs its own 252d trailing mean (long vol anomaly)
def f11re_f11_range_vol_estimators_park_252d_base_v004_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 252) / closeadj.replace(0, np.nan)
    b = pk - pk.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson term structure: short 21d / long 126d (vol regime)
def f11re_f11_range_vol_estimators_parkterm_21v126_base_v005_signal(high, low):
    s = _f11_parkinson(high, low, 21)
    l = _f11_parkinson(high, low, 126)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson z-score vs its own 252d history (de-trended vol level)
def f11re_f11_range_vol_estimators_parkz_63d_base_v006_signal(high, low):
    pk = _f11_parkinson(high, low, 63)
    b = _z(pk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass volatility, 21d, expressed RELATIVE to Parkinson 21d
# (close-move content the pure-range estimator misses). Decorrelates from raw GK.
def f11re_f11_range_vol_estimators_gk_21d_base_v007_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    pk = _f11_parkinson(high, low, 21)
    b = (gk - pk) / (gk + pk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 63d normalized by closeadj, z-scored vs own 252d history (>21d level z)
def f11re_f11_range_vol_estimators_gk_63d_base_v008_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 63) / closeadj.replace(0, np.nan)
    b = _z(gk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 63d vol-of-vol over 252d (long-horizon GK instability; dispersion facet
# distinct from both the term-ratio and the short-window GK vol-of-vol)
def f11re_f11_range_vol_estimators_gk_126d_base_v009_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 63)
    b = _std(gk, 252) / _mean(gk, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 252d percentile rank vs 504d history (long GK regime position)
def f11re_f11_range_vol_estimators_gk_252d_base_v010_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 252) / closeadj.replace(0, np.nan)
    b = _rank(gk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass term structure 21d/63d
def f11re_f11_range_vol_estimators_gkterm_21v63_base_v011_signal(open, high, low, close):
    s = _f11_garman_klass(open, high, low, close, 21)
    l = _f11_garman_klass(open, high, low, close, 63)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vol-of-vol over 63d (GK instability), decorrelated from GK z-level
def f11re_f11_range_vol_estimators_gkz_63d_base_v012_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    b = _std(gk, 63) / _mean(gk, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 21d relative to Garman-Klass 21d (drift vs gap+close content)
def f11re_f11_range_vol_estimators_rs_21d_base_v013_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    gk = _f11_garman_klass(open, high, low, close, 21)
    b = rs / gk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 63d relative to Parkinson 63d (drift/trend content of range)
def f11re_f11_range_vol_estimators_rs_63d_base_v014_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    pk = _f11_parkinson(high, low, 63)
    b = (rs / pk.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 126d z-scored vs own 252d history (drift-free vol regime level)
def f11re_f11_range_vol_estimators_rs_126d_base_v015_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    b = _z(rs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 252d slope over a quarter, relative to level (long drift-free trend)
def f11re_f11_range_vol_estimators_rs_252d_base_v016_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 252)
    b = _slope(rs, 126) / rs.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell term structure 21d/126d
def f11re_f11_range_vol_estimators_rsterm_21v126_base_v017_signal(open, high, low, close):
    s = _f11_rogers_satchell(open, high, low, close, 21)
    l = _f11_rogers_satchell(open, high, low, close, 126)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell drift-content z: RS/Parkinson ratio z-scored (trend-regime in range)
def f11re_f11_range_vol_estimators_rsz_63d_base_v018_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    pk = _f11_parkinson(high, low, 63)
    b = _z(rs / pk.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price, 14d (normalized true range, intraday<=21d uses close)
def f11re_f11_range_vol_estimators_atr_14d_base_v019_signal(high, low, close):
    atr = _f11_atr(high, low, close, 14)
    b = atr / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 14d z-scored vs own 126d history (de-trended true-range level)
def f11re_f11_range_vol_estimators_atrp_14d_base_v020_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 14) / close.replace(0, np.nan)
    b = _z(atrp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 5d vs 21d displacement (fast-vs-base true-range expansion, raw difference)
def f11re_f11_range_vol_estimators_atrp_21d_base_v021_signal(high, low, close):
    fast = _f11_atr(high, low, close, 5) / close.replace(0, np.nan)
    base = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = fast - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price, 63d, normalized by closeadj (>21d level estimator)
def f11re_f11_range_vol_estimators_atrp_63d_base_v022_signal(high, low, close, closeadj):
    atr = _f11_atr(high, low, close, 63)
    b = atr / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 126d slope over a quarter relative to level (slow true-range trend)
def f11re_f11_range_vol_estimators_atrp_126d_base_v023_signal(high, low, close, closeadj):
    atrp = _f11_atr(high, low, close, 126) / closeadj.replace(0, np.nan)
    b = _slope(atrp, 63) / atrp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price term structure 14d/63d (vol expansion regime)
def f11re_f11_range_vol_estimators_atrterm_14v63_base_v024_signal(high, low, close):
    s = _f11_atr(high, low, close, 14) / close.replace(0, np.nan)
    l = _f11_atr(high, low, close, 63) / close.replace(0, np.nan)
    b = s / l.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price z vs own 252d history
def f11re_f11_range_vol_estimators_atrpz_21d_base_v025_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _z(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range z-score, 21d window (single-day TR vs 21d typical)
def f11re_f11_range_vol_estimators_trz_21d_base_v026_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    b = _z(tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range z-score, 63d window
def f11re_f11_range_vol_estimators_trz_63d_base_v027_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    b = _z(tr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range 5d-avg z vs 126d history (smoothed range shock vs longer baseline)
def f11re_f11_range_vol_estimators_trz_126d_base_v028_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    sm = tr.rolling(5, min_periods=3).mean()
    b = _z(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-implied vol vs close-to-close realized vol DIVERGENCE, 21d
# (range-premium = how much the range estimator exceeds the close-vol; not a
# single-window close-vol level, so distinct from f10).
def f11re_f11_range_vol_estimators_parkrvdiv_21d_base_v029_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 21)
    rv = closeadj.pct_change().rolling(21, min_periods=11).std()
    b = pk / rv.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vs close-vol divergence, 63d (range-premium regime)
def f11re_f11_range_vol_estimators_gkrvdiv_63d_base_v030_signal(open, high, low, close, closeadj):
    gk = _f11_garman_klass(open, high, low, close, 63)
    rv = closeadj.pct_change().rolling(63, min_periods=32).std()
    b = gk / rv.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR vs RMS-range (Parkinson) divergence, 21d (mean true range vs root-mean-square
# log-range -> fat-tail shape of the range distribution, not a gap premium)
def f11re_f11_range_vol_estimators_atrgap_21d_base_v031_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    pk = _f11_parkinson(high, low, 21)
    b = atrp / pk.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR vs simple range divergence, 63d (slow gap-in-true-range premium)
def f11re_f11_range_vol_estimators_atrgap_63d_base_v032_signal(high, low, close):
    atr = _f11_atr(high, low, close, 63)
    simple = _mean(high - low, 63)
    b = atr / simple.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell 21d vol-cone position over 252d (drift-free estimator cone level;
# distinct estimator from the Parkinson cone)
def f11re_f11_range_vol_estimators_parkconemid_base_v033_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    mn = rs.rolling(252, min_periods=126).min()
    mx = rs.rolling(252, min_periods=126).max()
    b = (rs - mn) / (mx - mn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs Garman-Klass spread, z-scored (short-horizon estimator disagreement)
def f11re_f11_range_vol_estimators_pkgkspr_21d_base_v034_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 21)
    gk = _f11_garman_klass(open, high, low, close, 21)
    spr = (pk - gk) / (pk + gk).replace(0, np.nan)
    b = _z(spr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs Rogers-Satchell spread momentum, 126d (slow drift-content shift)
def f11re_f11_range_vol_estimators_pkrsspr_126d_base_v035_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 126)
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    spr = (pk - rs) / (pk + rs).replace(0, np.nan)
    b = spr - spr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vs Rogers-Satchell spread, 63d (gap+close vs drift-free content)
def f11re_f11_range_vol_estimators_gkrsspr_63d_base_v036_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 63)
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    b = (gk - rs) / (gk + rs).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson momentum: change in 21d Parkinson over a month (vol acceleration)
def f11re_f11_range_vol_estimators_parkmom_21d_base_v037_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = pk - pk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass momentum over a month, relative to level (medium GK acceleration)
def f11re_f11_range_vol_estimators_gkmom_63d_base_v038_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 63)
    b = (gk - gk.shift(21)) / gk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price momentum over a month
def f11re_f11_range_vol_estimators_atrpmom_21d_base_v039_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = atrp - atrp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 5d single-bar percentile rank vs 252d history (fast vol spike regime)
def f11re_f11_range_vol_estimators_parkrank_63d_base_v040_signal(high, low):
    pk = _f11_parkinson(high, low, 5)
    b = _rank(pk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 21d percentile rank vs 126d history (medium GK regime position)
def f11re_f11_range_vol_estimators_gkrank_63d_base_v041_signal(open, high, low, close):
    gk = _f11_garman_klass(open, high, low, close, 21)
    b = _rank(gk, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price percentile rank vs 252d history
def f11re_f11_range_vol_estimators_atrprank_21d_base_v042_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = _rank(atrp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Vol-of-vol: dispersion of Parkinson over 63d (range-vol instability)
def f11re_f11_range_vol_estimators_parkvov_63d_base_v043_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = _std(pk, 63) / _mean(pk, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Vol-of-vol of ATR/price over 63d
def f11re_f11_range_vol_estimators_atrvov_63d_base_v044_signal(high, low, close):
    atrp = _f11_atr(high, low, close, 14) / close.replace(0, np.nan)
    b = _std(atrp, 63) / _mean(atrp, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range expansion intensity: avg positive TR z-excess over last 21d (gappy launch days)
def f11re_f11_range_vol_estimators_trexp_21d_base_v045_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    z = _z(tr, 63)
    excess = (z - 1.0).clip(lower=0)
    b = excess.rolling(21, min_periods=11).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range contraction streak scaled by contraction depth (squeeze build-up)
def f11re_f11_range_vol_estimators_trcontract_base_v046_signal(high, low, close):
    short = _f11_atr(high, low, close, 5)
    long = _f11_atr(high, low, close, 21)
    ratio = short / long.replace(0, np.nan)
    contracted = (ratio < 1.0).astype(float)
    grp = (contracted == 0).cumsum()
    run = contracted.groupby(grp).cumsum()
    b = run * (1.0 - ratio).clip(lower=0).rolling(5, min_periods=2).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson term structure z (regime change in vol curve)
def f11re_f11_range_vol_estimators_parktermz_base_v047_signal(high, low):
    s = _f11_parkinson(high, low, 21)
    l = _f11_parkinson(high, low, 63)
    ratio = s / l.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-gap shock asymmetry: rolling skewness of overnight log-gaps, 63d
# (sign/shape of the gap distribution rather than its magnitude premium)
def f11re_f11_range_vol_estimators_gkyz_21d_base_v048_signal(open, close):
    o = _f11_overnight(open, close)
    b = o.rolling(63, min_periods=32).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GKYZ 63d gap-aware vol momentum over a quarter (gap-vol expansion rate)
def f11re_f11_range_vol_estimators_gkyz_63d_base_v049_signal(open, high, low, close):
    o = _f11_overnight(open, close)
    t = o ** 2 + _f11_gk_term(open, high, low, close)
    gkyz = np.sqrt(t.rolling(63, min_periods=32).mean().clip(lower=0))
    b = gkyz / gkyz.shift(63).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Overnight-gap variance share: gap term as fraction of GKYZ total (gap-driven vol)
def f11re_f11_range_vol_estimators_gapshare_63d_base_v050_signal(open, high, low, close):
    o = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan)) ** 2
    tot = o + _f11_gk_term(open, high, low, close)
    b = o.rolling(63, min_periods=32).mean() / tot.rolling(
        63, min_periods=32).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell vs Garman-Klass 126d divergence (long-horizon drift-free vs gap+close
# content; long-window estimator disagreement, distinct from the 21d gap-premium cluster)
def f11re_f11_range_vol_estimators_yzgk_21d_base_v051_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 126)
    gk = _f11_garman_klass(open, high, low, close, 126)
    b = (rs - gk) / (rs + gk).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang intraday-session share: close-to-open variance as fraction of YZ variance,
# 63d (how much of the full estimator is the intraday session move). Structurally the
# session leg, not the overnight-gap leg captured by gapshare.
def f11re_f11_range_vol_estimators_yzterm_21v63_base_v052_signal(open, high, low, close):
    c = _f11_intraday(open, close)
    vc = ((c - c.rolling(63, min_periods=32).mean()) ** 2).rolling(
        63, min_periods=32).mean()
    yzv = _f11_yang_zhang(open, high, low, close, 63) ** 2
    b = vc / yzv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs Yang-Zhang efficiency divergence, 63d: pure-range estimator vs the
# full drift-robust estimator (how much overnight+drift content the range misses).
# An estimator-vs-estimator divergence, not a raw range-distribution CoV (that is f13).
def f11re_f11_range_vol_estimators_parkeff_63d_base_v053_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 63)
    yz = _f11_yang_zhang(open, high, low, close, 63)
    b = (pk - yz) / (pk + yz).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass coefficient of variation of daily terms, 63d (intra-window GK roughness)
def f11re_f11_range_vol_estimators_gkrough_63d_base_v054_signal(open, high, low, close):
    t = _f11_gk_term(open, high, low, close).clip(lower=0)
    b = _std(t, 63) / _mean(t, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Vol compression: 21d Parkinson vs its trailing 252d median (squeeze vs typical)
def f11re_f11_range_vol_estimators_parkcomp_base_v055_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    med = pk.rolling(252, min_periods=126).median()
    b = np.log(pk.replace(0, np.nan) / med.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range sign-magnitude: signed by close direction, magnitude by TR/close, 21d
def f11re_f11_range_vol_estimators_trsignmag_21d_base_v056_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    direction = np.sign(close - close.shift(1))
    b = _mean(direction * tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell directional decomposition: up-leg vs down-leg variance share, 63d
# (drift sign embedded in the RS estimator; not a candle close-location)
def f11re_f11_range_vol_estimators_rsdrift_63d_base_v057_signal(open, high, low, close):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open.replace(0, np.nan))
    up = (hc * ho)
    dn = (lc * lo)
    b = _mean(up - dn, 63) / _mean((up + dn).abs(), 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price expansion gauge: 21d atrp minus 63d atrp (short minus medium level)
def f11re_f11_range_vol_estimators_atrpexpand_base_v058_signal(high, low, close):
    s = _f11_atr(high, low, close, 21) / close.replace(0, np.nan)
    l = _f11_atr(high, low, close, 63) / close.replace(0, np.nan)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson EWMA (persistent range-vol level)
def f11re_f11_range_vol_estimators_parkewma_base_v059_signal(high, low):
    r2 = _f11_log_hl(high, low) ** 2
    c = 1.0 / (4.0 * np.log(2.0))
    b = np.sqrt((c * r2).ewm(span=42, min_periods=21).mean())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson displacement from EWMA (vol shock vs persistent level)
def f11re_f11_range_vol_estimators_parkdisp_base_v060_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = pk - pk.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang vol-of-vol over 63d (full-estimator instability)
def f11re_f11_range_vol_estimators_yzvov_63d_base_v061_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 21)
    b = _std(yz, 63) / _mean(yz, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Max single-day TR over 63d relative to typical (tail-range / blowoff)
def f11re_f11_range_vol_estimators_trtail_63d_base_v062_signal(high, low, close):
    tr = _f11_true_range(high, low, close) / close.replace(0, np.nan)
    mx = tr.rolling(63, min_periods=32).max()
    med = tr.rolling(63, min_periods=32).median()
    b = mx / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rogers-Satchell normalized by closeadj, ranked vs 504d (long drift-free regime)
def f11re_f11_range_vol_estimators_rsrank504_base_v063_signal(open, high, low, close):
    rs = _f11_rogers_satchell(open, high, low, close, 63)
    b = _rank(rs, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson curvature: second difference of 21d Parkinson (vol acceleration shape)
def f11re_f11_range_vol_estimators_parkcurv_base_v064_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    b = pk - 2.0 * pk.shift(21) + pk.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 63d vs its 252d median (slow vol cheap/expensive level)
def f11re_f11_range_vol_estimators_atrpmed_base_v065_signal(high, low, close, closeadj):
    atrp = _f11_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    med = atrp.rolling(252, min_periods=126).median()
    b = atrp / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range-vol consensus: avg relative deviation of estimators from their 126d median
def f11re_f11_range_vol_estimators_volbreadth_base_v066_signal(open, high, low, close):
    pk = _f11_parkinson(high, low, 21)
    gk = _f11_garman_klass(open, high, low, close, 21)
    rs = _f11_rogers_satchell(open, high, low, close, 21)
    dp = pk / pk.rolling(126, min_periods=63).median().replace(0, np.nan) - 1.0
    dg = gk / gk.rolling(126, min_periods=63).median().replace(0, np.nan) - 1.0
    dr = rs / rs.rolling(126, min_periods=63).median().replace(0, np.nan) - 1.0
    b = (dp + dg + dr) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Intraday-range vol vs overnight-gap vol ratio (where vol lives), 21d
def f11re_f11_range_vol_estimators_intravsover_base_v067_signal(open, high, low, close):
    intraday = _f11_parkinson(high, low, 21)
    overnight = _std(_f11_overnight(open, close), 21)
    b = intraday / overnight.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 126d normalized by closeadj, mean-reversion vs 21d avg (>21d)
def f11re_f11_range_vol_estimators_parkmr_126d_base_v068_signal(high, low, closeadj):
    pk = _f11_parkinson(high, low, 126) / closeadj.replace(0, np.nan)
    b = pk - pk.rolling(21, min_periods=11).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# True-range coefficient of variation, 63d (range instability)
def f11re_f11_range_vol_estimators_trcv_63d_base_v069_signal(high, low, close):
    tr = _f11_true_range(high, low, close)
    b = _std(tr, 63) / _mean(tr, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang vol-of-vol over 126d (long-horizon full-estimator instability)
def f11re_f11_range_vol_estimators_yzz_126d_base_v070_signal(open, high, low, close):
    yz = _f11_yang_zhang(open, high, low, close, 21)
    b = _std(yz, 126) / _mean(yz, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson tanh-bounded quarter-over-quarter log change (squashed vol drift)
def f11re_f11_range_vol_estimators_parktanh_base_v071_signal(high, low):
    pk = _f11_parkinson(high, low, 63)
    chg = np.log(pk.replace(0, np.nan) / pk.shift(63).replace(0, np.nan))
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Down-leg vs up-leg intraday range energy ratio, 21d (high-vs-close leg vs
# close-vs-low leg; raw ratio of the two RS-style half-ranges, not a normalized spread)
def f11re_f11_range_vol_estimators_gkpkratio_base_v072_signal(high, low, close):
    upleg = np.log(high.replace(0, np.nan) / close.replace(0, np.nan)) ** 2
    dnleg = np.log(close.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    u = _mean(upleg, 21)
    d = _mean(dnleg, 21)
    b = d / u.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR slope normalized by ATR level (relative expansion rate)
def f11re_f11_range_vol_estimators_atrslope_63d_base_v073_signal(high, low, close):
    atr = _f11_atr(high, low, close, 63)
    b = _slope(atr, 21) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Range-vol streak: consecutive-day expansion run scaled by mean expansion magnitude
def f11re_f11_range_vol_estimators_parkstreak_base_v074_signal(high, low):
    s = _f11_parkinson(high, low, 5)
    l = _f11_parkinson(high, low, 63)
    ratio = s / l.replace(0, np.nan)
    hot = (ratio > 1.0).astype(float)
    grp = (hot == 0).cumsum()
    run = hot.groupby(grp).cumsum()
    b = run * (ratio - 1.0).clip(lower=0).rolling(5, min_periods=2).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Vol-cone position: where 21d Parkinson sits in its 252d min-max cone (cone level)
def f11re_f11_range_vol_estimators_parkcone_base_v075_signal(high, low):
    pk = _f11_parkinson(high, low, 21)
    mn = pk.rolling(252, min_periods=126).min()
    mx = pk.rolling(252, min_periods=126).max()
    b = (pk - mn) / (mx - mn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11re_f11_range_vol_estimators_park_21d_base_v001_signal,
    f11re_f11_range_vol_estimators_park_63d_base_v002_signal,
    f11re_f11_range_vol_estimators_park_126d_base_v003_signal,
    f11re_f11_range_vol_estimators_park_252d_base_v004_signal,
    f11re_f11_range_vol_estimators_parkterm_21v126_base_v005_signal,
    f11re_f11_range_vol_estimators_parkz_63d_base_v006_signal,
    f11re_f11_range_vol_estimators_gk_21d_base_v007_signal,
    f11re_f11_range_vol_estimators_gk_63d_base_v008_signal,
    f11re_f11_range_vol_estimators_gk_126d_base_v009_signal,
    f11re_f11_range_vol_estimators_gk_252d_base_v010_signal,
    f11re_f11_range_vol_estimators_gkterm_21v63_base_v011_signal,
    f11re_f11_range_vol_estimators_gkz_63d_base_v012_signal,
    f11re_f11_range_vol_estimators_rs_21d_base_v013_signal,
    f11re_f11_range_vol_estimators_rs_63d_base_v014_signal,
    f11re_f11_range_vol_estimators_rs_126d_base_v015_signal,
    f11re_f11_range_vol_estimators_rs_252d_base_v016_signal,
    f11re_f11_range_vol_estimators_rsterm_21v126_base_v017_signal,
    f11re_f11_range_vol_estimators_rsz_63d_base_v018_signal,
    f11re_f11_range_vol_estimators_atr_14d_base_v019_signal,
    f11re_f11_range_vol_estimators_atrp_14d_base_v020_signal,
    f11re_f11_range_vol_estimators_atrp_21d_base_v021_signal,
    f11re_f11_range_vol_estimators_atrp_63d_base_v022_signal,
    f11re_f11_range_vol_estimators_atrp_126d_base_v023_signal,
    f11re_f11_range_vol_estimators_atrterm_14v63_base_v024_signal,
    f11re_f11_range_vol_estimators_atrpz_21d_base_v025_signal,
    f11re_f11_range_vol_estimators_trz_21d_base_v026_signal,
    f11re_f11_range_vol_estimators_trz_63d_base_v027_signal,
    f11re_f11_range_vol_estimators_trz_126d_base_v028_signal,
    f11re_f11_range_vol_estimators_parkrvdiv_21d_base_v029_signal,
    f11re_f11_range_vol_estimators_gkrvdiv_63d_base_v030_signal,
    f11re_f11_range_vol_estimators_atrgap_21d_base_v031_signal,
    f11re_f11_range_vol_estimators_atrgap_63d_base_v032_signal,
    f11re_f11_range_vol_estimators_parkconemid_base_v033_signal,
    f11re_f11_range_vol_estimators_pkgkspr_21d_base_v034_signal,
    f11re_f11_range_vol_estimators_pkrsspr_126d_base_v035_signal,
    f11re_f11_range_vol_estimators_gkrsspr_63d_base_v036_signal,
    f11re_f11_range_vol_estimators_parkmom_21d_base_v037_signal,
    f11re_f11_range_vol_estimators_gkmom_63d_base_v038_signal,
    f11re_f11_range_vol_estimators_atrpmom_21d_base_v039_signal,
    f11re_f11_range_vol_estimators_parkrank_63d_base_v040_signal,
    f11re_f11_range_vol_estimators_gkrank_63d_base_v041_signal,
    f11re_f11_range_vol_estimators_atrprank_21d_base_v042_signal,
    f11re_f11_range_vol_estimators_parkvov_63d_base_v043_signal,
    f11re_f11_range_vol_estimators_atrvov_63d_base_v044_signal,
    f11re_f11_range_vol_estimators_trexp_21d_base_v045_signal,
    f11re_f11_range_vol_estimators_trcontract_base_v046_signal,
    f11re_f11_range_vol_estimators_parktermz_base_v047_signal,
    f11re_f11_range_vol_estimators_gkyz_21d_base_v048_signal,
    f11re_f11_range_vol_estimators_gkyz_63d_base_v049_signal,
    f11re_f11_range_vol_estimators_gapshare_63d_base_v050_signal,
    f11re_f11_range_vol_estimators_yzgk_21d_base_v051_signal,
    f11re_f11_range_vol_estimators_yzterm_21v63_base_v052_signal,
    f11re_f11_range_vol_estimators_parkeff_63d_base_v053_signal,
    f11re_f11_range_vol_estimators_gkrough_63d_base_v054_signal,
    f11re_f11_range_vol_estimators_parkcomp_base_v055_signal,
    f11re_f11_range_vol_estimators_trsignmag_21d_base_v056_signal,
    f11re_f11_range_vol_estimators_rsdrift_63d_base_v057_signal,
    f11re_f11_range_vol_estimators_atrpexpand_base_v058_signal,
    f11re_f11_range_vol_estimators_parkewma_base_v059_signal,
    f11re_f11_range_vol_estimators_parkdisp_base_v060_signal,
    f11re_f11_range_vol_estimators_yzvov_63d_base_v061_signal,
    f11re_f11_range_vol_estimators_trtail_63d_base_v062_signal,
    f11re_f11_range_vol_estimators_rsrank504_base_v063_signal,
    f11re_f11_range_vol_estimators_parkcurv_base_v064_signal,
    f11re_f11_range_vol_estimators_atrpmed_base_v065_signal,
    f11re_f11_range_vol_estimators_volbreadth_base_v066_signal,
    f11re_f11_range_vol_estimators_intravsover_base_v067_signal,
    f11re_f11_range_vol_estimators_parkmr_126d_base_v068_signal,
    f11re_f11_range_vol_estimators_trcv_63d_base_v069_signal,
    f11re_f11_range_vol_estimators_yzz_126d_base_v070_signal,
    f11re_f11_range_vol_estimators_parktanh_base_v071_signal,
    f11re_f11_range_vol_estimators_gkpkratio_base_v072_signal,
    f11re_f11_range_vol_estimators_atrslope_63d_base_v073_signal,
    f11re_f11_range_vol_estimators_parkstreak_base_v074_signal,
    f11re_f11_range_vol_estimators_parkcone_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RANGE_VOL_ESTIMATORS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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
