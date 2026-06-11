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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (volatility regime expansion) =====
def _f09_ret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f09_rvol(closeadj, w):
    r = _f09_ret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_bbwidth(closeadj, w):
    m = closeadj.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = closeadj.rolling(w, min_periods=max(2, w // 2)).std()
    return (4.0 * sd) / m.replace(0, np.nan)


def _f09_tr(high, low, closeadj):
    pc = closeadj.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f09_atr(high, low, closeadj, w):
    return _f09_tr(high, low, closeadj).rolling(w, min_periods=max(2, w // 2)).mean()


def _f09_volratio(closeadj, ws, wl):
    return _f09_rvol(closeadj, ws) / _f09_rvol(closeadj, wl).replace(0, np.nan)


def _f09_squeeze_pctl(closeadj, w, lookback):
    bw = _f09_bbwidth(closeadj, w)
    return bw.rolling(lookback, min_periods=max(5, lookback // 3)).rank(pct=True)


def _f09_parkinson(high, low, w):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    return (hl / (4.0 * np.log(2.0))).rolling(w, min_periods=max(2, w // 2)).mean() ** 0.5


def _slope(s, k):
    # 1st math derivative: rate of change of the base over k days
    return (s - s.shift(k)) / float(k)


# ============================================================
# slope of 21d realized-vol regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_rvolz_21d_slope_v001_signal(closeadj):
    base = _z(_f09_rvol(closeadj, 21), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d realized-vol regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_rvolz_63d_slope_v002_signal(closeadj):
    base = _z(_f09_rvol(closeadj, 63), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d realized-vol regime z (ROC 63d)
def f09vr_f09_volatility_regime_expansion_rvolz_126d_slope_v003_signal(closeadj):
    base = _z(_f09_rvol(closeadj, 126), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol ratio 5v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volratio_5v63_slope_v004_signal(closeadj):
    base = _f09_volratio(closeadj, 5, 63)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth-based compression ratio 21v126 (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volratio_21v126_slope_v005_signal(closeadj):
    base = _f09_bbwidth(closeadj, 21) / _f09_bbwidth(closeadj, 126).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of log vol ratio 5v21 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volratioz_5v21_slope_v006_signal(closeadj):
    base = np.log(_f09_volratio(closeadj, 5, 21).replace(0, np.nan))
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d Bollinger bandwidth (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbwidth_21d_slope_v007_signal(closeadj):
    base = _f09_bbwidth(closeadj, 21)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d Bollinger bandwidth (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbwidth_63d_slope_v008_signal(closeadj):
    base = _f09_bbwidth(closeadj, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d bandwidth z (ROC 63d)
def f09vr_f09_volatility_regime_expansion_bbwidthz_126d_slope_v009_signal(closeadj):
    base = _z(_f09_bbwidth(closeadj, 126), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d squeeze percentile (ROC 5d)
def f09vr_f09_volatility_regime_expansion_squeeze_21d_slope_v010_signal(closeadj):
    base = _f09_squeeze_pctl(closeadj, 21, 252)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d squeeze percentile (ROC 21d)
def f09vr_f09_volatility_regime_expansion_squeeze_63d_slope_v011_signal(closeadj):
    base = _f09_squeeze_pctl(closeadj, 63, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol (21d-vol std over 63d) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volofvol_slope_v012_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    base = rv.rolling(63, min_periods=21).std()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol coefficient of variation (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volofvolcv_slope_v013_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    base = rv.rolling(126, min_periods=42).std() / rv.rolling(126, min_periods=42).mean().replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR/price regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_atrpz_21d_slope_v014_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    base = _z(atrp, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR ratio 5v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_atrratio_5v63_slope_v015_signal(closeadj, high, low):
    base = _f09_atr(high, low, closeadj, 5) / _f09_atr(high, low, closeadj, 63).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of high-low range regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_hlrngz_slope_v016_signal(closeadj, high, low):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=7).mean()
    base = _z(rng, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of semi-vol spread (ROC 21d)
def f09vr_f09_volatility_regime_expansion_semivolspr_slope_v017_signal(closeadj):
    r = _f09_ret(closeadj)
    up = r.where(r > 0, 0.0).rolling(63, min_periods=21).std()
    dn = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    base = (dn - up) / (dn + up).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of squeeze persistence (ROC 21d)
def f09vr_f09_volatility_regime_expansion_sqzpersist_slope_v018_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    base = (pctl <= 0.25).astype(float).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol ratio (ROC 21d)
def f09vr_f09_volatility_regime_expansion_vovratio_slope_v019_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov_s = rv.rolling(42, min_periods=14).std()
    vov_l = rv.rolling(252, min_periods=84).std()
    base = vov_s / vov_l.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d realized-vol percentile (ROC 21d)
def f09vr_f09_volatility_regime_expansion_rvolpctl_slope_v020_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    base = rv.rolling(504, min_periods=126).rank(pct=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of absolute-return shock measure (ROC 5d)
def f09vr_f09_volatility_regime_expansion_retshock_slope_v021_signal(closeadj):
    r = _f09_ret(closeadj)
    rv = _f09_rvol(closeadj, 63)
    base = (r.abs() / rv.replace(0, np.nan)).rolling(21, min_periods=7).mean()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d-bandwidth coil ratio (bw vs its 252d max) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_coilratio_slope_v022_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 63)
    base = bw / bw.rolling(252, min_periods=84).max().replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intraday ATR release ratio (ATR vs its 126d min) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_releaseratio_slope_v023_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    base = atrp / atrp.rolling(126, min_periods=42).min().replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63v252 vol-ratio percentile rank (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volratio63v252rank_slope_v024_signal(closeadj):
    vr = _f09_volratio(closeadj, 63, 252)
    base = vr.rolling(504, min_periods=126).rank(pct=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol EMA displacement (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvoldisp_slope_v025_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    ew = rv.ewm(span=63, min_periods=21).mean()
    base = (rv - ew) / ew.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson vol regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_parkz_21d_slope_v026_signal(closeadj, high, low):
    base = _z(_f09_parkinson(high, low, 21), 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d realized-vol range position within 504d band, log-scaled (ROC 21d)
def f09vr_f09_volatility_regime_expansion_rvolrangepos_slope_v027_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    lo = rv.rolling(504, min_periods=126).min()
    base = np.log(rv.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of standardized vol acceleration (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volaccelstd_slope_v028_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    chg = rv - rv.shift(10)
    vov = rv.rolling(126, min_periods=42).std()
    base = chg / vov.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5v21 vol ratio (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volratio_5v21_slope_v029_signal(closeadj):
    base = _f09_volratio(closeadj, 5, 21).rolling(5, min_periods=3).mean()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of expansion fraction (ROC 21d)
def f09vr_f09_volatility_regime_expansion_expandfrac_slope_v030_signal(closeadj):
    base = (_f09_rvol(closeadj, 5) > _f09_rvol(closeadj, 63)).astype(float).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of regime z spread short-vs-long (ROC 21d)
def f09vr_f09_volatility_regime_expansion_regimezspr_slope_v031_signal(closeadj):
    z21 = _z(_f09_rvol(closeadj, 21), 252)
    z126 = _z(_f09_rvol(closeadj, 126), 504)
    base = z21 - z126
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth squeeze release log (ROC 21d)
def f09vr_f09_volatility_regime_expansion_sqzrelease_slope_v032_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 63)
    floor = bw.rolling(126, min_periods=42).min()
    base = np.log(bw.replace(0, np.nan) / floor.replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_vovz_slope_v033_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov = rv.rolling(63, min_periods=21).std()
    base = _z(vov, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of downside-vol regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_downvolz_slope_v034_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    base = _z(dn, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth term ratio 21v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbwterm_slope_v035_signal(closeadj):
    base = _f09_bbwidth(closeadj, 21) / _f09_bbwidth(closeadj, 63).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol curvature (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volcurv_slope_v036_signal(closeadj):
    base = _f09_rvol(closeadj, 21) - 2.0 * _f09_rvol(closeadj, 63) + _f09_rvol(closeadj, 126)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR%-mean-reversion gap (intraday, ROC 21d)
def f09vr_f09_volatility_regime_expansion_rvolmrgap_slope_v037_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    mn = atrp.rolling(252, min_periods=63).mean()
    base = (atrp - mn) / mn.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of shock-cluster dispersion (ROC 5d)
def f09vr_f09_volatility_regime_expansion_shockcluster_slope_v038_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    base = ar.rolling(21, min_periods=7).std() / ar.rolling(21, min_periods=7).mean().replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d vol year-over-year log change (ROC 63d)
def f09vr_f09_volatility_regime_expansion_volyoy_slope_v039_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    base = np.log(rv.replace(0, np.nan) / rv.shift(252).replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of compression->expansion balance (ROC 5d)
def f09vr_f09_volatility_regime_expansion_cebalance_slope_v040_signal(closeadj):
    base = np.log(_f09_volratio(closeadj, 5, 126).replace(0, np.nan)).ewm(span=10, min_periods=5).mean()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWMA vol regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_ewmvolz_slope_v041_signal(closeadj):
    r = _f09_ret(closeadj)
    ev = r.ewm(span=21, min_periods=10).std()
    base = _z(ev, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWMA-vs-simple vol divergence (ROC 5d)
def f09vr_f09_volatility_regime_expansion_ewmsimplediv_slope_v042_signal(closeadj):
    r = _f09_ret(closeadj)
    ev = r.ewm(span=21, min_periods=10).std()
    sv = _f09_rvol(closeadj, 21)
    base = (ev - sv) / sv.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of TTM-squeeze indicator (ROC 5d)
def f09vr_f09_volatility_regime_expansion_ttmsqueeze_slope_v043_signal(closeadj, high, low):
    m = closeadj.rolling(20, min_periods=10).mean()
    bb = 2.0 * closeadj.rolling(20, min_periods=10).std()
    kc = 1.5 * _f09_atr(high, low, closeadj, 20)
    base = (bb - kc) / m.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol skewness (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volskew_slope_v044_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    base = rv.rolling(63, min_periods=21).skew()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of return kurtosis (ROC 21d)
def f09vr_f09_volatility_regime_expansion_retkurt_slope_v045_signal(closeadj):
    base = _f09_ret(closeadj).rolling(63, min_periods=21).kurt()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of return skewness (ROC 21d)
def f09vr_f09_volatility_regime_expansion_retskew_slope_v046_signal(closeadj):
    base = _f09_ret(closeadj).rolling(63, min_periods=21).skew()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of true-range thrust vs longer ATR baseline (ROC 21d)
def f09vr_f09_volatility_regime_expansion_trthrust_slope_v047_signal(closeadj, high, low):
    tr = _f09_tr(high, low, closeadj)
    atr = tr.rolling(63, min_periods=21).mean()
    base = (tr / atr.replace(0, np.nan)).rolling(21, min_periods=7).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of normalized true-range z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_trz_slope_v048_signal(closeadj, high, low):
    trp = _f09_tr(high, low, closeadj) / closeadj.replace(0, np.nan)
    base = _z(trp, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson ratio 5v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_parkratio_slope_v049_signal(closeadj, high, low):
    base = _f09_parkinson(high, low, 5) / _f09_parkinson(high, low, 63).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson 63d regime z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_parkz_63d_slope_v050_signal(closeadj, high, low):
    base = _z(_f09_parkinson(high, low, 63), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of close-vs-intraday vol divergence (ROC 21d)
def f09vr_f09_volatility_regime_expansion_closeintradiv_slope_v051_signal(closeadj, high, low):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    pkz = _z(_f09_parkinson(high, low, 21), 252)
    base = rvz - pkz
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of squeeze-scale gap (ROC 5d)
def f09vr_f09_volatility_regime_expansion_sqzscalegap_slope_v052_signal(closeadj):
    base = _f09_squeeze_pctl(closeadj, 21, 252) - _f09_squeeze_pctl(closeadj, 63, 252)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d vol momentum (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volmom_slope_v053_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    base = np.log(rv.replace(0, np.nan) / rv.shift(21).replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of high-vol regime occupancy (ROC 21d)
def f09vr_f09_volatility_regime_expansion_highvolocc_slope_v054_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    pctl = rv.rolling(252, min_periods=63).rank(pct=True)
    base = (pctl >= 0.8).astype(float).rolling(252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol regime change-point measure (ROC 5d)
def f09vr_f09_volatility_regime_expansion_changepoint_slope_v055_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    recent = rv.rolling(21, min_periods=10).mean()
    prior = rv.shift(21).rolling(21, min_periods=10).mean()
    base = (recent - prior) / prior.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of downside expansion ratio (ROC 5d)
def f09vr_f09_volatility_regime_expansion_downexpratio_slope_v056_signal(closeadj):
    r = _f09_ret(closeadj)
    dn_s = r.where(r < 0, 0.0).rolling(5, min_periods=3).std()
    dn_l = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    base = dn_s / dn_l.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of upside expansion ratio with 10d numerator (ROC 5d)
def f09vr_f09_volatility_regime_expansion_upexpratio_slope_v057_signal(closeadj):
    r = _f09_ret(closeadj)
    up_s = r.where(r > 0, 0.0).rolling(10, min_periods=4).std()
    up_l = r.where(r > 0, 0.0).rolling(126, min_periods=42).std()
    base = up_s / up_l.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth trend efficiency (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbweff_slope_v058_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    net = (bw - bw.shift(63)).abs()
    path = bw.diff().abs().rolling(63, min_periods=21).sum()
    base = net / path.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol min/max compression ratio (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volminmax_slope_v059_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    base = rv.rolling(126, min_periods=42).min() / rv.rolling(126, min_periods=42).max().replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth-off-floor release (21d bw vs 126d min) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volofffloor_slope_v060_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    floor = bw.rolling(126, min_periods=42).min()
    base = np.log(bw.replace(0, np.nan) / floor.replace(0, np.nan))
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson-based normalized turbulence (range vol-of-vol / level) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_normturbulence_slope_v061_signal(closeadj, high, low):
    pk = _f09_parkinson(high, low, 21)
    vov = pk.rolling(63, min_periods=21).std()
    lvl = pk.rolling(63, min_periods=21).mean()
    base = vov / lvl.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of downside-share regime (ROC 21d)
def f09vr_f09_volatility_regime_expansion_downshare_slope_v062_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = (r.where(r < 0, 0.0) ** 2).rolling(63, min_periods=21).sum()
    tot = (r ** 2).rolling(63, min_periods=21).sum()
    base = dn / tot.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol z spread 5v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volzspread_slope_v063_signal(closeadj):
    z5 = _z(_f09_rvol(closeadj, 5), 252)
    z63 = _z(_f09_rvol(closeadj, 63), 504)
    base = z5 - z63
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth overshoot vs EMA (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbwovershoot_slope_v064_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    sm = bw.ewm(span=42, min_periods=14).mean()
    base = (bw - sm) / sm.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR% momentum (ROC 21d)
def f09vr_f09_volatility_regime_expansion_atrpmom_slope_v065_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    base = atrp - atrp.shift(63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of gap-vol ratio (close vs Parkinson) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_gapvolratio_slope_v066_signal(closeadj, high, low):
    base = _f09_rvol(closeadj, 21) / _f09_parkinson(high, low, 21).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth velocity 63d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbwvel63_slope_v067_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 63)
    base = (bw - bw.shift(21)) / bw.shift(21).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol amplitude (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volamplitude_slope_v068_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    mx = rv.rolling(252, min_periods=63).max()
    mn = rv.rolling(252, min_periods=63).min()
    me = rv.rolling(252, min_periods=63).mean()
    base = (mx - mn) / me.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max-day shock prominence (ROC 5d)
def f09vr_f09_volatility_regime_expansion_maxdayshock_slope_v069_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    mx = ar.rolling(21, min_periods=7).max()
    rv = _f09_rvol(closeadj, 63)
    base = mx / rv.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of compression index using bandwidth ratio 63v504 (ROC 21d)
def f09vr_f09_volatility_regime_expansion_compressidx_slope_v070_signal(closeadj):
    base = 1.0 - (_f09_bbwidth(closeadj, 63) / _f09_bbwidth(closeadj, 504).replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of regime churn (ROC 21d)
def f09vr_f09_volatility_regime_expansion_regimechurn_slope_v071_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    pctl = rv.rolling(252, min_periods=63).rank(pct=True)
    base = pctl.rolling(63, min_periods=21).std()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d slow vol drift (ROC 63d)
def f09vr_f09_volatility_regime_expansion_slowvoldrift_slope_v072_signal(closeadj):
    rv = _f09_rvol(closeadj, 126)
    base = np.log(rv.replace(0, np.nan) / rv.shift(126).replace(0, np.nan))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of close-vol-of-vol minus Parkinson-vol-of-vol divergence (ROC 21d)
def f09vr_f09_volatility_regime_expansion_parkvov_slope_v073_signal(closeadj, high, low):
    cc_vov = _f09_rvol(closeadj, 21).rolling(63, min_periods=21).std()
    pk_vov = _f09_parkinson(high, low, 21).rolling(63, min_periods=21).std()
    base = cc_vov - pk_vov
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of asymmetric vol z (ROC 21d)
def f09vr_f09_volatility_regime_expansion_asymvolz_slope_v074_signal(closeadj):
    r = _f09_ret(closeadj)
    up = r.where(r > 0, 0.0).rolling(21, min_periods=7).std()
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    base = _z(dn - up, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of normalized turbulence at 126d level (ROC 21d)
def f09vr_f09_volatility_regime_expansion_turbulence126_slope_v075_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    ew = rv.ewm(span=126, min_periods=42).mean()
    base = (rv - ew) / ew.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d-vs-21d realized-vol regime z gap (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvolz_5d_slope_v076_signal(closeadj):
    base = _z(_f09_rvol(closeadj, 5), 252) - _z(_f09_rvol(closeadj, 21), 252)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of up/down expansion asymmetry (ROC 5d)
def f09vr_f09_volatility_regime_expansion_updownexpasym_slope_v077_signal(closeadj):
    r = _f09_ret(closeadj)
    up_r = (r.where(r > 0, 0.0).rolling(5, min_periods=3).std()
            / r.where(r > 0, 0.0).rolling(63, min_periods=21).std().replace(0, np.nan))
    dn_r = (r.where(r < 0, 0.0).rolling(5, min_periods=3).std()
            / r.where(r < 0, 0.0).rolling(63, min_periods=21).std().replace(0, np.nan))
    base = up_r - dn_r
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 252d vol cone position (ROC 63d)
def f09vr_f09_volatility_regime_expansion_volconepos_slope_v078_signal(closeadj):
    rv = _f09_rvol(closeadj, 252)
    base = rv.rolling(1260, min_periods=252).rank(pct=True)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth IQR dispersion (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbwiqr_slope_v079_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    q75 = bw.rolling(252, min_periods=63).quantile(0.75)
    q25 = bw.rolling(252, min_periods=63).quantile(0.25)
    med = bw.rolling(252, min_periods=63).median()
    base = (q75 - q25) / med.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-under-ceiling headroom (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volunderceil_slope_v080_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    ceil = rv.rolling(126, min_periods=42).max()
    base = np.log(ceil.replace(0, np.nan) / rv.replace(0, np.nan))
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Bollinger-to-Keltner band ratio percentile within 252d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_banddiverge_slope_v081_signal(closeadj, high, low):
    bb = 4.0 * closeadj.rolling(21, min_periods=10).std()
    kb = 2.0 * _f09_atr(high, low, closeadj, 21)
    ratio = bb / kb.replace(0, np.nan)
    base = ratio.rolling(252, min_periods=63).rank(pct=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of short-horizon semivol asymmetry at 21d (ROC 5d)
def f09vr_f09_volatility_regime_expansion_semivolasym_slope_v082_signal(closeadj):
    r = _f09_ret(closeadj)
    up = r.where(r > 0, 0.0).rolling(21, min_periods=7).std()
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    base = (dn - up) / (dn + up).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d vol percentile rank vs 1260d (ROC 63d)
def f09vr_f09_volatility_regime_expansion_vollongrank_slope_v083_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    base = rv.rolling(1260, min_periods=252).rank(pct=True)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of downside-semivol 126d cycle phase in 1260d range (ROC 63d)
def f09vr_f09_volatility_regime_expansion_volcyclephase_slope_v084_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = r.where(r < 0, 0.0).rolling(126, min_periods=42).std()
    hi = dn.rolling(1260, min_periods=252).max()
    lo = dn.rolling(1260, min_periods=252).min()
    base = (dn - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth term ratio 63v126 (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbwterm63v126_slope_v085_signal(closeadj):
    base = _f09_bbwidth(closeadj, 63) / _f09_bbwidth(closeadj, 126).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-cluster autocorrelation (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volclusterac_slope_v086_signal(closeadj):
    ar = _f09_ret(closeadj).abs()

    def _ac1(a):
        a0 = a[:-1]
        a1 = a[1:]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return float(np.corrcoef(a0, a1)[0, 1])
    base = ar.rolling(63, min_periods=30).apply(_ac1, raw=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of squeeze-decay recency (ROC 5d)
def f09vr_f09_volatility_regime_expansion_sqzdecay_slope_v087_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    tight = (pctl <= 0.10).astype(float)

    def _dsl(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        gap = len(a) - 1 - idx[-1]
        return float(np.exp(-gap / 21.0))
    base = tight.rolling(126, min_periods=42).apply(_dsl, raw=True)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of expansion Sharpe (clean vol-change signal) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_expsharpe_slope_v088_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    chg = rv - rv.shift(21)
    noise = chg.rolling(63, min_periods=21).std()
    base = chg / noise.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intraday-vs-close vol gap (ROC 21d)
def f09vr_f09_volatility_regime_expansion_intravsclose_slope_v089_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    rv = _f09_rvol(closeadj, 21)
    base = atrp - rv
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol over 252d (slow turbulence) (ROC 63d)
def f09vr_f09_volatility_regime_expansion_slowvov_slope_v090_signal(closeadj):
    rv = _f09_rvol(closeadj, 63)
    base = rv.rolling(252, min_periods=84).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol 5v126 ratio percentile within 252d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volratio_5v126_slope_v091_signal(closeadj):
    vr = _f09_volratio(closeadj, 5, 126)
    base = vr.rolling(252, min_periods=63).rank(pct=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of return autocorrelation magnitude (vol-clustering strength) at 63d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_logvolratio_21v252_slope_v092_signal(closeadj):
    r2 = _f09_ret(closeadj) ** 2

    def _ac1(a):
        a0 = a[:-1]
        a1 = a[1:]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return float(np.corrcoef(a0, a1)[0, 1])
    base = r2.rolling(63, min_periods=30).apply(_ac1, raw=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol-to-bandwidth consistency z at 21d (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbwz21_slope_v093_signal(closeadj):
    ratio = _f09_rvol(closeadj, 21) / _f09_bbwidth(closeadj, 21).replace(0, np.nan)
    base = _z(ratio, 252)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of single-day true-range spike vs 21d ATR (fast intraday thrust, ROC 5d)
def f09vr_f09_volatility_regime_expansion_tratrpersist_slope_v094_signal(closeadj, high, low):
    tr = _f09_tr(high, low, closeadj)
    atr = tr.rolling(21, min_periods=7).mean()
    base = tr / atr.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol regime distance (signed sqrt of rvol63 z) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_regimedist_slope_v095_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 63), 504)
    base = np.sign(rvz) * (rvz.abs() ** 0.5)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of mean-reverting vol pressure (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volmrpressure_slope_v096_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    base = -np.sign(rvz) * (rvz ** 2)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of expansion-dwell streak weighting (ROC 5d)
def f09vr_f09_volatility_regime_expansion_expdwell_slope_v097_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    med = rv.rolling(252, min_periods=63).median()
    excess = ((rv - med) / med.replace(0, np.nan))
    base = excess.rolling(21, min_periods=7).mean()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max single-day shock vs 126d vol over a quarter window (ROC 21d)
def f09vr_f09_volatility_regime_expansion_shockrecency_slope_v098_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    rv = _f09_rvol(closeadj, 126)
    base = (ar / rv.replace(0, np.nan)).rolling(63, min_periods=21).max()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Keltner-squeeze depth persistence (fraction of squeeze-on, ROC 21d)
def f09vr_f09_volatility_regime_expansion_kcsqzdepth_slope_v099_signal(closeadj, high, low):
    bb = 2.0 * closeadj.rolling(20, min_periods=10).std()
    kc = 1.5 * _f09_atr(high, low, closeadj, 20)
    depth = ((kc - bb) / kc.replace(0, np.nan)).clip(lower=0)
    base = depth.rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of overnight-gap vol share (close-to-close minus intraday range) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volnormpos_slope_v100_signal(closeadj, high, low):
    cc = _f09_rvol(closeadj, 21)
    intraday = ((high - low) / closeadj.replace(0, np.nan)).rolling(21, min_periods=7).mean()
    base = (cc - intraday) / cc.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of return-range efficiency vol (ROC 21d)
def f09vr_f09_volatility_regime_expansion_rangeeff_slope_v101_signal(closeadj, high, low):
    rng = (high - low) / closeadj.replace(0, np.nan)
    body = _f09_ret(closeadj).abs()
    base = (body.rolling(21, min_periods=7).sum()
            / rng.rolling(21, min_periods=7).sum().replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 126d-bandwidth percentile within 1260d (long-horizon, ROC 63d)
def f09vr_f09_volatility_regime_expansion_bbwpctl504_slope_v102_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 126)
    base = bw.rolling(1260, min_periods=252).rank(pct=True)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d ATR intraday range level (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvol5_slope_v103_signal(closeadj, high, low):
    base = _f09_atr(high, low, closeadj, 5) / closeadj.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol vs intraday-ATR efficiency at 21d (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvol21_slope_v104_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    base = _f09_rvol(closeadj, 21) / atrp.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 63d-vol vs 63d-Parkinson efficiency ratio (ROC 21d)
def f09vr_f09_volatility_regime_expansion_rvol63_slope_v105_signal(closeadj, high, low):
    base = _f09_rvol(closeadj, 63) / _f09_parkinson(high, low, 63).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR% term-structure ratio 21v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_atrp63_slope_v106_signal(closeadj, high, low):
    a21 = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    a63 = _f09_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    base = a21 / a63.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson 63d range-vol momentum (log change over a month) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_park5_slope_v107_signal(closeadj, high, low):
    pk = _f09_parkinson(high, low, 63)
    base = np.log(pk.replace(0, np.nan) / pk.shift(21).replace(0, np.nan))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of downside-semivol squeeze percentile (down-vol rank in 252d) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_squeeze504_slope_v108_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    base = dn.rolling(252, min_periods=63).rank(pct=True)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-of-vol percentile rank within 504d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_vovnorm_slope_v109_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    vov = rv.rolling(63, min_periods=21).std()
    base = vov.rolling(504, min_periods=126).rank(pct=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of upside vol level (ROC 5d)
def f09vr_f09_volatility_regime_expansion_upvol_slope_v110_signal(closeadj):
    r = _f09_ret(closeadj)
    base = r.where(r > 0, 0.0).rolling(21, min_periods=7).std()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of downside vol level (ROC 5d)
def f09vr_f09_volatility_regime_expansion_downvol_slope_v111_signal(closeadj):
    r = _f09_ret(closeadj)
    base = r.where(r < 0, 0.0).rolling(21, min_periods=7).std()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 21d/63d vol ratio (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volratio_21v63_slope_v112_signal(closeadj):
    base = _f09_volratio(closeadj, 21, 63)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth 5d level (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbw5_slope_v113_signal(closeadj):
    base = _f09_bbwidth(closeadj, 5)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of true-range z over 504d (ROC 63d)
def f09vr_f09_volatility_regime_expansion_trz504_slope_v114_signal(closeadj, high, low):
    trp = _f09_tr(high, low, closeadj) / closeadj.replace(0, np.nan)
    base = _z(trp.rolling(63, min_periods=21).mean(), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol regime z spread 21v504 (ROC 21d)
def f09vr_f09_volatility_regime_expansion_regimezspr21v504_slope_v115_signal(closeadj):
    z21 = _z(_f09_rvol(closeadj, 21), 252)
    z252 = _z(_f09_rvol(closeadj, 252), 504)
    base = z21 - z252
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of realized-vol kurtosis 126d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_volkurt_slope_v116_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    base = rv.rolling(126, min_periods=42).kurt()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of EWMA fast/slow vol ratio (ROC 5d)
def f09vr_f09_volatility_regime_expansion_ewmratio_slope_v117_signal(closeadj):
    r = _f09_ret(closeadj)
    fast = r.ewm(span=10, min_periods=5).std()
    slow = r.ewm(span=63, min_periods=21).std()
    base = fast / slow.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of expansion breadth count (ROC 21d)
def f09vr_f09_volatility_regime_expansion_expbreadth_slope_v118_signal(closeadj):
    e1 = (_f09_volratio(closeadj, 5, 63) > 1.0).astype(float)
    e2 = (_f09_volratio(closeadj, 10, 126) > 1.0).astype(float)
    e3 = (_f09_volratio(closeadj, 21, 252) > 1.0).astype(float)
    base = (e1 + e2 + e3).rolling(10, min_periods=3).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol-z curvature (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvolzcurv_slope_v119_signal(closeadj):
    rvz = _z(_f09_rvol(closeadj, 21), 252)
    base = rvz - 2.0 * rvz.shift(10) + rvz.shift(20)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of low-vol occupancy (ROC 21d)
def f09vr_f09_volatility_regime_expansion_lowvolocc_slope_v120_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    pctl = rv.rolling(252, min_periods=63).rank(pct=True)
    base = (pctl <= 0.2).astype(float).rolling(252, min_periods=63).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson-vs-close efficiency z-scored vs history (ROC 5d)
def f09vr_f09_volatility_regime_expansion_parkcloseeff_slope_v121_signal(closeadj, high, low):
    ratio = _f09_parkinson(high, low, 63) / _f09_rvol(closeadj, 63).replace(0, np.nan)
    base = _z(ratio, 504)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intraday vol regime z spread 5v63 (Parkinson) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volzspr5v63_slope_v122_signal(closeadj, high, low):
    z5 = _z(_f09_parkinson(high, low, 5), 252)
    z63 = _z(_f09_parkinson(high, low, 63), 504)
    base = z5 - z63
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth acceleration base (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbwaccelbase_slope_v123_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    base = bw - bw.shift(5)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR% vol-cone position at 63d (intraday, ROC 63d)
def f09vr_f09_volatility_regime_expansion_volcone63_slope_v124_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 63) / closeadj.replace(0, np.nan)
    base = atrp.rolling(1260, min_periods=252).rank(pct=True)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of high-low range expansion z 63d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_hlexpz63_slope_v125_signal(closeadj, high, low):
    rng = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    base = _z(rng, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol expansion margin days (ROC 21d)
def f09vr_f09_volatility_regime_expansion_expdaysmargin_slope_v126_signal(closeadj):
    margin = (_f09_volratio(closeadj, 5, 63) - 1.2).clip(lower=0)
    base = margin.rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth re-expansion gated by squeeze (ROC 5d)
def f09vr_f09_volatility_regime_expansion_reexpand_slope_v127_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    prior_tight = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0).shift(5)
    delta = ((bw - bw.shift(5)) / bw.shift(5).replace(0, np.nan)).clip(lower=0)
    base = prior_tight * delta
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of trend-vol efficiency interaction (ROC 21d)
def f09vr_f09_volatility_regime_expansion_trendvol_slope_v128_signal(closeadj):
    trend = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    path = _f09_ret(closeadj).abs().rolling(63, min_periods=21).sum()
    eff = trend / path.replace(0, np.nan)
    volexp = (_f09_volratio(closeadj, 21, 126) - 1.0)
    base = eff * volexp
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of long-memory vol term curvature (ROC 63d)
def f09vr_f09_volatility_regime_expansion_voltermcurv_slope_v129_signal(closeadj):
    l21 = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    l126 = np.log(_f09_rvol(closeadj, 126).replace(0, np.nan))
    l504 = np.log(_f09_rvol(closeadj, 504).replace(0, np.nan))
    base = l21 - 2.0 * l126 + l504
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of band overshoot at 63d window (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbwovershoot63_slope_v130_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 63)
    sm = bw.ewm(span=126, min_periods=42).mean()
    base = (bw - sm) / sm.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth turning measure (bandwidth momentum) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_volturn_slope_v131_signal(closeadj):
    bwz = _z(_f09_bbwidth(closeadj, 21), 252)
    base = (bwz - bwz.shift(10))
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of conversion rate squeeze->expansion (ROC 21d)
def f09vr_f09_volatility_regime_expansion_conversion_slope_v132_signal(closeadj):
    pctl = _f09_squeeze_pctl(closeadj, 21, 252)
    was_tight = (0.2 - pctl.shift(10)).clip(lower=0)
    now_wide = (pctl - 0.6).clip(lower=0)
    base = (was_tight * now_wide).rolling(63, min_periods=21).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of max-day shock relative to longer vol (ROC 5d)
def f09vr_f09_volatility_regime_expansion_maxshocklong_slope_v133_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    mx = ar.rolling(10, min_periods=3).max()
    rv = _f09_rvol(closeadj, 126)
    base = mx / rv.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth velocity normalized (ROC 5d)
def f09vr_f09_volatility_regime_expansion_bbwvelnorm_slope_v134_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    base = (bw - bw.shift(5)) / bw.shift(5).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of intraday range thrust over 5d max (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rngthrustmax_slope_v135_signal(closeadj, high, low):
    tr = _f09_tr(high, low, closeadj)
    atr = tr.rolling(21, min_periods=7).mean()
    base = (tr / atr.replace(0, np.nan)).rolling(5, min_periods=3).max()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol regime cycle phase at 126d bandwidth (ROC 63d)
def f09vr_f09_volatility_regime_expansion_bbwcycle_slope_v136_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 126)
    hi = bw.rolling(1260, min_periods=252).max()
    lo = bw.rolling(1260, min_periods=252).min()
    base = (bw - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of return entropy proxy (abs-ret dispersion) (ROC 5d)
def f09vr_f09_volatility_regime_expansion_retentropy_slope_v137_signal(closeadj):
    ar = _f09_ret(closeadj).abs()
    base = ar.rolling(21, min_periods=7).std()
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of squeeze-then-fire interaction (ROC 5d)
def f09vr_f09_volatility_regime_expansion_sqzfire_slope_v138_signal(closeadj):
    sqz = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0)
    drift = _f09_ret(closeadj).rolling(5, min_periods=3).sum().abs()
    base = sqz * drift
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol ratio 10v126 rank (ROC 21d)
def f09vr_f09_volatility_regime_expansion_exprank10v126_slope_v139_signal(closeadj):
    vr = _f09_volratio(closeadj, 10, 126)
    base = vr.rolling(252, min_periods=63).rank(pct=True)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 504d realized-vol level (ROC 63d)
def f09vr_f09_volatility_regime_expansion_rvol504_slope_v140_signal(closeadj):
    base = _f09_rvol(closeadj, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR ratio 10v63 (ROC 5d)
def f09vr_f09_volatility_regime_expansion_atrratio10v63_slope_v141_signal(closeadj, high, low):
    base = _f09_atr(high, low, closeadj, 10) / _f09_atr(high, low, closeadj, 63).replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Bollinger bandwidth 126d (ROC 63d)
def f09vr_f09_volatility_regime_expansion_bbw126_slope_v142_signal(closeadj):
    base = _f09_bbwidth(closeadj, 126)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of Parkinson range vol-of-vol over 252d (intraday turbulence, ROC 63d)
def f09vr_f09_volatility_regime_expansion_vov63in252_slope_v143_signal(closeadj, high, low):
    pk = _f09_parkinson(high, low, 63)
    base = pk.rolling(252, min_periods=84).std()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of compression->expansion tilt (ewm log 5v126) (ROC 21d)
def f09vr_f09_volatility_regime_expansion_cetilt_slope_v144_signal(closeadj):
    base = np.log(_f09_volratio(closeadj, 5, 126).replace(0, np.nan)).ewm(span=21, min_periods=10).mean()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of 5d bandwidth percentile within 252d (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvolz5_504_slope_v145_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 5)
    base = bw.rolling(252, min_periods=63).rank(pct=True)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of ATR%-vs-rvol divergence (ROC 5d)
def f09vr_f09_volatility_regime_expansion_atrrvoldiv_slope_v146_signal(closeadj, high, low):
    atrp = _f09_atr(high, low, closeadj, 21) / closeadj.replace(0, np.nan)
    rv = _f09_rvol(closeadj, 21)
    base = (atrp - rv) / rv.replace(0, np.nan)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of vol percentile 21d in 252d (ROC 5d)
def f09vr_f09_volatility_regime_expansion_rvolpctl21_slope_v147_signal(closeadj):
    rv = _f09_rvol(closeadj, 21)
    base = rv.rolling(252, min_periods=63).rank(pct=True)
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of bandwidth quantile spread 90-10 (ROC 21d)
def f09vr_f09_volatility_regime_expansion_bbwq9010_slope_v148_signal(closeadj):
    bw = _f09_bbwidth(closeadj, 21)
    q90 = bw.rolling(252, min_periods=63).quantile(0.9)
    q10 = bw.rolling(252, min_periods=63).quantile(0.1)
    med = bw.rolling(252, min_periods=63).median()
    base = (q90 - q10) / med.replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of semivol downside z 63d (ROC 21d)
def f09vr_f09_volatility_regime_expansion_downvolz63_slope_v149_signal(closeadj):
    r = _f09_ret(closeadj)
    dn = r.where(r < 0, 0.0).rolling(63, min_periods=21).std()
    base = _z(dn, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of coil-and-fire composite (ROC 5d)
def f09vr_f09_volatility_regime_expansion_coilfire_slope_v150_signal(closeadj):
    prior_sqz = (0.5 - _f09_squeeze_pctl(closeadj, 21, 252)).clip(lower=0).shift(10)
    exp_z = _z(_f09_rvol(closeadj, 5), 252).clip(lower=0)
    base = prior_sqz * exp_z
    b = _slope(base, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vr_f09_volatility_regime_expansion_rvolz_21d_slope_v001_signal,
    f09vr_f09_volatility_regime_expansion_rvolz_63d_slope_v002_signal,
    f09vr_f09_volatility_regime_expansion_rvolz_126d_slope_v003_signal,
    f09vr_f09_volatility_regime_expansion_volratio_5v63_slope_v004_signal,
    f09vr_f09_volatility_regime_expansion_volratio_21v126_slope_v005_signal,
    f09vr_f09_volatility_regime_expansion_volratioz_5v21_slope_v006_signal,
    f09vr_f09_volatility_regime_expansion_bbwidth_21d_slope_v007_signal,
    f09vr_f09_volatility_regime_expansion_bbwidth_63d_slope_v008_signal,
    f09vr_f09_volatility_regime_expansion_bbwidthz_126d_slope_v009_signal,
    f09vr_f09_volatility_regime_expansion_squeeze_21d_slope_v010_signal,
    f09vr_f09_volatility_regime_expansion_squeeze_63d_slope_v011_signal,
    f09vr_f09_volatility_regime_expansion_volofvol_slope_v012_signal,
    f09vr_f09_volatility_regime_expansion_volofvolcv_slope_v013_signal,
    f09vr_f09_volatility_regime_expansion_atrpz_21d_slope_v014_signal,
    f09vr_f09_volatility_regime_expansion_atrratio_5v63_slope_v015_signal,
    f09vr_f09_volatility_regime_expansion_hlrngz_slope_v016_signal,
    f09vr_f09_volatility_regime_expansion_semivolspr_slope_v017_signal,
    f09vr_f09_volatility_regime_expansion_sqzpersist_slope_v018_signal,
    f09vr_f09_volatility_regime_expansion_vovratio_slope_v019_signal,
    f09vr_f09_volatility_regime_expansion_rvolpctl_slope_v020_signal,
    f09vr_f09_volatility_regime_expansion_retshock_slope_v021_signal,
    f09vr_f09_volatility_regime_expansion_coilratio_slope_v022_signal,
    f09vr_f09_volatility_regime_expansion_releaseratio_slope_v023_signal,
    f09vr_f09_volatility_regime_expansion_volratio63v252rank_slope_v024_signal,
    f09vr_f09_volatility_regime_expansion_rvoldisp_slope_v025_signal,
    f09vr_f09_volatility_regime_expansion_parkz_21d_slope_v026_signal,
    f09vr_f09_volatility_regime_expansion_rvolrangepos_slope_v027_signal,
    f09vr_f09_volatility_regime_expansion_volaccelstd_slope_v028_signal,
    f09vr_f09_volatility_regime_expansion_volratio_5v21_slope_v029_signal,
    f09vr_f09_volatility_regime_expansion_expandfrac_slope_v030_signal,
    f09vr_f09_volatility_regime_expansion_regimezspr_slope_v031_signal,
    f09vr_f09_volatility_regime_expansion_sqzrelease_slope_v032_signal,
    f09vr_f09_volatility_regime_expansion_vovz_slope_v033_signal,
    f09vr_f09_volatility_regime_expansion_downvolz_slope_v034_signal,
    f09vr_f09_volatility_regime_expansion_bbwterm_slope_v035_signal,
    f09vr_f09_volatility_regime_expansion_volcurv_slope_v036_signal,
    f09vr_f09_volatility_regime_expansion_rvolmrgap_slope_v037_signal,
    f09vr_f09_volatility_regime_expansion_shockcluster_slope_v038_signal,
    f09vr_f09_volatility_regime_expansion_volyoy_slope_v039_signal,
    f09vr_f09_volatility_regime_expansion_cebalance_slope_v040_signal,
    f09vr_f09_volatility_regime_expansion_ewmvolz_slope_v041_signal,
    f09vr_f09_volatility_regime_expansion_ewmsimplediv_slope_v042_signal,
    f09vr_f09_volatility_regime_expansion_ttmsqueeze_slope_v043_signal,
    f09vr_f09_volatility_regime_expansion_volskew_slope_v044_signal,
    f09vr_f09_volatility_regime_expansion_retkurt_slope_v045_signal,
    f09vr_f09_volatility_regime_expansion_retskew_slope_v046_signal,
    f09vr_f09_volatility_regime_expansion_trthrust_slope_v047_signal,
    f09vr_f09_volatility_regime_expansion_trz_slope_v048_signal,
    f09vr_f09_volatility_regime_expansion_parkratio_slope_v049_signal,
    f09vr_f09_volatility_regime_expansion_parkz_63d_slope_v050_signal,
    f09vr_f09_volatility_regime_expansion_closeintradiv_slope_v051_signal,
    f09vr_f09_volatility_regime_expansion_sqzscalegap_slope_v052_signal,
    f09vr_f09_volatility_regime_expansion_volmom_slope_v053_signal,
    f09vr_f09_volatility_regime_expansion_highvolocc_slope_v054_signal,
    f09vr_f09_volatility_regime_expansion_changepoint_slope_v055_signal,
    f09vr_f09_volatility_regime_expansion_downexpratio_slope_v056_signal,
    f09vr_f09_volatility_regime_expansion_upexpratio_slope_v057_signal,
    f09vr_f09_volatility_regime_expansion_bbweff_slope_v058_signal,
    f09vr_f09_volatility_regime_expansion_volminmax_slope_v059_signal,
    f09vr_f09_volatility_regime_expansion_volofffloor_slope_v060_signal,
    f09vr_f09_volatility_regime_expansion_normturbulence_slope_v061_signal,
    f09vr_f09_volatility_regime_expansion_downshare_slope_v062_signal,
    f09vr_f09_volatility_regime_expansion_volzspread_slope_v063_signal,
    f09vr_f09_volatility_regime_expansion_bbwovershoot_slope_v064_signal,
    f09vr_f09_volatility_regime_expansion_atrpmom_slope_v065_signal,
    f09vr_f09_volatility_regime_expansion_gapvolratio_slope_v066_signal,
    f09vr_f09_volatility_regime_expansion_bbwvel63_slope_v067_signal,
    f09vr_f09_volatility_regime_expansion_volamplitude_slope_v068_signal,
    f09vr_f09_volatility_regime_expansion_maxdayshock_slope_v069_signal,
    f09vr_f09_volatility_regime_expansion_compressidx_slope_v070_signal,
    f09vr_f09_volatility_regime_expansion_regimechurn_slope_v071_signal,
    f09vr_f09_volatility_regime_expansion_slowvoldrift_slope_v072_signal,
    f09vr_f09_volatility_regime_expansion_parkvov_slope_v073_signal,
    f09vr_f09_volatility_regime_expansion_asymvolz_slope_v074_signal,
    f09vr_f09_volatility_regime_expansion_turbulence126_slope_v075_signal,
    f09vr_f09_volatility_regime_expansion_rvolz_5d_slope_v076_signal,
    f09vr_f09_volatility_regime_expansion_updownexpasym_slope_v077_signal,
    f09vr_f09_volatility_regime_expansion_volconepos_slope_v078_signal,
    f09vr_f09_volatility_regime_expansion_bbwiqr_slope_v079_signal,
    f09vr_f09_volatility_regime_expansion_volunderceil_slope_v080_signal,
    f09vr_f09_volatility_regime_expansion_banddiverge_slope_v081_signal,
    f09vr_f09_volatility_regime_expansion_semivolasym_slope_v082_signal,
    f09vr_f09_volatility_regime_expansion_vollongrank_slope_v083_signal,
    f09vr_f09_volatility_regime_expansion_volcyclephase_slope_v084_signal,
    f09vr_f09_volatility_regime_expansion_bbwterm63v126_slope_v085_signal,
    f09vr_f09_volatility_regime_expansion_volclusterac_slope_v086_signal,
    f09vr_f09_volatility_regime_expansion_sqzdecay_slope_v087_signal,
    f09vr_f09_volatility_regime_expansion_expsharpe_slope_v088_signal,
    f09vr_f09_volatility_regime_expansion_intravsclose_slope_v089_signal,
    f09vr_f09_volatility_regime_expansion_slowvov_slope_v090_signal,
    f09vr_f09_volatility_regime_expansion_volratio_5v126_slope_v091_signal,
    f09vr_f09_volatility_regime_expansion_logvolratio_21v252_slope_v092_signal,
    f09vr_f09_volatility_regime_expansion_bbwz21_slope_v093_signal,
    f09vr_f09_volatility_regime_expansion_tratrpersist_slope_v094_signal,
    f09vr_f09_volatility_regime_expansion_regimedist_slope_v095_signal,
    f09vr_f09_volatility_regime_expansion_volmrpressure_slope_v096_signal,
    f09vr_f09_volatility_regime_expansion_expdwell_slope_v097_signal,
    f09vr_f09_volatility_regime_expansion_shockrecency_slope_v098_signal,
    f09vr_f09_volatility_regime_expansion_kcsqzdepth_slope_v099_signal,
    f09vr_f09_volatility_regime_expansion_volnormpos_slope_v100_signal,
    f09vr_f09_volatility_regime_expansion_rangeeff_slope_v101_signal,
    f09vr_f09_volatility_regime_expansion_bbwpctl504_slope_v102_signal,
    f09vr_f09_volatility_regime_expansion_rvol5_slope_v103_signal,
    f09vr_f09_volatility_regime_expansion_rvol21_slope_v104_signal,
    f09vr_f09_volatility_regime_expansion_rvol63_slope_v105_signal,
    f09vr_f09_volatility_regime_expansion_atrp63_slope_v106_signal,
    f09vr_f09_volatility_regime_expansion_park5_slope_v107_signal,
    f09vr_f09_volatility_regime_expansion_squeeze504_slope_v108_signal,
    f09vr_f09_volatility_regime_expansion_vovnorm_slope_v109_signal,
    f09vr_f09_volatility_regime_expansion_upvol_slope_v110_signal,
    f09vr_f09_volatility_regime_expansion_downvol_slope_v111_signal,
    f09vr_f09_volatility_regime_expansion_volratio_21v63_slope_v112_signal,
    f09vr_f09_volatility_regime_expansion_bbw5_slope_v113_signal,
    f09vr_f09_volatility_regime_expansion_trz504_slope_v114_signal,
    f09vr_f09_volatility_regime_expansion_regimezspr21v504_slope_v115_signal,
    f09vr_f09_volatility_regime_expansion_volkurt_slope_v116_signal,
    f09vr_f09_volatility_regime_expansion_ewmratio_slope_v117_signal,
    f09vr_f09_volatility_regime_expansion_expbreadth_slope_v118_signal,
    f09vr_f09_volatility_regime_expansion_rvolzcurv_slope_v119_signal,
    f09vr_f09_volatility_regime_expansion_lowvolocc_slope_v120_signal,
    f09vr_f09_volatility_regime_expansion_parkcloseeff_slope_v121_signal,
    f09vr_f09_volatility_regime_expansion_volzspr5v63_slope_v122_signal,
    f09vr_f09_volatility_regime_expansion_bbwaccelbase_slope_v123_signal,
    f09vr_f09_volatility_regime_expansion_volcone63_slope_v124_signal,
    f09vr_f09_volatility_regime_expansion_hlexpz63_slope_v125_signal,
    f09vr_f09_volatility_regime_expansion_expdaysmargin_slope_v126_signal,
    f09vr_f09_volatility_regime_expansion_reexpand_slope_v127_signal,
    f09vr_f09_volatility_regime_expansion_trendvol_slope_v128_signal,
    f09vr_f09_volatility_regime_expansion_voltermcurv_slope_v129_signal,
    f09vr_f09_volatility_regime_expansion_bbwovershoot63_slope_v130_signal,
    f09vr_f09_volatility_regime_expansion_volturn_slope_v131_signal,
    f09vr_f09_volatility_regime_expansion_conversion_slope_v132_signal,
    f09vr_f09_volatility_regime_expansion_maxshocklong_slope_v133_signal,
    f09vr_f09_volatility_regime_expansion_bbwvelnorm_slope_v134_signal,
    f09vr_f09_volatility_regime_expansion_rngthrustmax_slope_v135_signal,
    f09vr_f09_volatility_regime_expansion_bbwcycle_slope_v136_signal,
    f09vr_f09_volatility_regime_expansion_retentropy_slope_v137_signal,
    f09vr_f09_volatility_regime_expansion_sqzfire_slope_v138_signal,
    f09vr_f09_volatility_regime_expansion_exprank10v126_slope_v139_signal,
    f09vr_f09_volatility_regime_expansion_rvol504_slope_v140_signal,
    f09vr_f09_volatility_regime_expansion_atrratio10v63_slope_v141_signal,
    f09vr_f09_volatility_regime_expansion_bbw126_slope_v142_signal,
    f09vr_f09_volatility_regime_expansion_vov63in252_slope_v143_signal,
    f09vr_f09_volatility_regime_expansion_cetilt_slope_v144_signal,
    f09vr_f09_volatility_regime_expansion_rvolz5_504_slope_v145_signal,
    f09vr_f09_volatility_regime_expansion_atrrvoldiv_slope_v146_signal,
    f09vr_f09_volatility_regime_expansion_rvolpctl21_slope_v147_signal,
    f09vr_f09_volatility_regime_expansion_bbwq9010_slope_v148_signal,
    f09vr_f09_volatility_regime_expansion_downvolz63_slope_v149_signal,
    f09vr_f09_volatility_regime_expansion_coilfire_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_REGIME_EXPANSION_REGISTRY_2ND_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f09_volatility_regime_expansion_2nd_derivatives_001_150_claude: %d features pass" % n_features)
