import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
ANN = np.sqrt(252.0)


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


# ===== folder domain primitives (realized-volatility term structure) =====
def _f10_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f10_rvol(closeadj, w):
    # annualized close-to-close realized volatility over window w
    r = _f10_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std() * ANN


def _f10_downside(closeadj, w):
    # annualized downside semi-deviation (negative returns only)
    r = _f10_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    return np.sqrt((neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * ANN


def _f10_upside(closeadj, w):
    # annualized upside semi-deviation (positive returns only)
    r = _f10_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    return np.sqrt((pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean()) * ANN


def _f10_term_ratio(closeadj, ws, wl):
    # term-structure ratio: short-horizon vol / long-horizon vol
    return _f10_rvol(closeadj, ws) / _f10_rvol(closeadj, wl).replace(0, np.nan)


def _f10_cone_pos(closeadj, w, lookback):
    # vol-cone position: percentile of current w-vol within its own lookback history
    v = _f10_rvol(closeadj, w)
    return v.rolling(lookback, min_periods=max(2, lookback // 2)).rank(pct=True) - 0.5


def _f10_voladj_ret(closeadj, w):
    # vol-adjusted return: trailing log-return over window / realized vol
    r = _f10_logret(closeadj)
    cum = r.rolling(w, min_periods=max(2, w // 2)).sum()
    v = _f10_rvol(closeadj, w)
    return cum / v.replace(0, np.nan)


# ============================================================
# realized vol level, 5d (annualized)
def f10rv_f10_realized_volatility_term_rvol_5d_base_v001_signal(closeadj):
    b = _f10_rvol(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol level, 21d
def f10rv_f10_realized_volatility_term_rvol_21d_base_v002_signal(closeadj):
    b = _f10_rvol(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol level, 63d
def f10rv_f10_realized_volatility_term_rvol_63d_base_v003_signal(closeadj):
    b = _f10_rvol(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol level, 126d
def f10rv_f10_realized_volatility_term_rvol_126d_base_v004_signal(closeadj):
    b = _f10_rvol(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol level, 252d
def f10rv_f10_realized_volatility_term_rvol_252d_base_v005_signal(closeadj):
    b = _f10_rvol(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# front-end vol-ratio surprise: 5v63 steepness minus its own 63d EMA (de-leveled)
def f10rv_f10_realized_volatility_term_tratio_5v63_base_v006_signal(closeadj):
    tr = _f10_term_ratio(closeadj, 5, 63)
    b = tr - tr.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure ratio: 21d / 126d realized vol
def f10rv_f10_realized_volatility_term_tratio_21v126_base_v007_signal(closeadj):
    b = _f10_term_ratio(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cone-position spread: 21d vol percentile minus 252d vol percentile (term regime gap)
def f10rv_f10_realized_volatility_term_tratio_21v252_base_v008_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v252 = _f10_rvol(closeadj, 252)
    b = _rank(v21, 252) - _rank(v252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-structure ratio: 63d / 252d realized vol
def f10rv_f10_realized_volatility_term_tratio_63v252_base_v009_signal(closeadj):
    b = _f10_term_ratio(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# back-curve log-vol curvature across 63/126/252 tenors (long-end convexity)
def f10rv_f10_realized_volatility_term_tslope_21v126_base_v010_signal(closeadj):
    l63 = np.log(_f10_rvol(closeadj, 63).replace(0, np.nan))
    l126 = np.log(_f10_rvol(closeadj, 126).replace(0, np.nan))
    l252 = np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    b = (l63 - l126) - (l126 - l252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# least-squares slope of log-vol vs log-horizon across 5 tenors (full-curve tilt)
def f10rv_f10_realized_volatility_term_tslope_5v63_base_v011_signal(closeadj):
    xs = np.log(np.array([5.0, 21.0, 63.0, 126.0, 252.0]))
    xm = xs.mean()
    dx = xs - xm
    denom = float((dx ** 2).sum())
    l5 = np.log(_f10_rvol(closeadj, 5).replace(0, np.nan))
    l21 = np.log(_f10_rvol(closeadj, 21).replace(0, np.nan))
    l63 = np.log(_f10_rvol(closeadj, 63).replace(0, np.nan))
    l126 = np.log(_f10_rvol(closeadj, 126).replace(0, np.nan))
    l252 = np.log(_f10_rvol(closeadj, 252).replace(0, np.nan))
    ys = pd.concat([l5, l21, l63, l126, l252], axis=1)
    ym = ys.mean(axis=1)
    cov = (ys.sub(ym, axis=0)).mul(dx, axis=1).sum(axis=1)
    b = cov / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-structure curvature: 21d vol vs avg of 5d and 63d (convexity of curve)
def f10rv_f10_realized_volatility_term_tcurv_5_21_63_base_v012_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    b = (v5 + v63) / 2.0 - v21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol curvature across 21/63/126 (mid-curve bow)
def f10rv_f10_realized_volatility_term_tcurv_21_63_126_base_v013_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    b = (v21 + v126) / 2.0 - v63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation, 21d
def f10rv_f10_realized_volatility_term_dsemi_21d_base_v014_signal(closeadj):
    b = _f10_downside(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation, 63d
def f10rv_f10_realized_volatility_term_dsemi_63d_base_v015_signal(closeadj):
    b = _f10_downside(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation, 126d
def f10rv_f10_realized_volatility_term_dsemi_126d_base_v016_signal(closeadj):
    b = _f10_downside(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-deviation, 21d
def f10rv_f10_realized_volatility_term_usemi_21d_base_v017_signal(closeadj):
    b = _f10_upside(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-deviation, 63d
def f10rv_f10_realized_volatility_term_usemi_63d_base_v018_signal(closeadj):
    b = _f10_upside(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation asymmetry: (downside - upside)/(downside + upside), 63d
def f10rv_f10_realized_volatility_term_semiasym_63d_base_v019_signal(closeadj):
    d = _f10_downside(closeadj, 63)
    u = _f10_upside(closeadj, 63)
    b = (d - u) / (d + u).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-deviation asymmetry, 21d (short-horizon downside dominance)
def f10rv_f10_realized_volatility_term_semiasym_21d_base_v020_signal(closeadj):
    d = _f10_downside(closeadj, 21)
    u = _f10_upside(closeadj, 21)
    b = (d - u) / (d + u).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-share momentum: 63d downside/total vol ratio change over a quarter
def f10rv_f10_realized_volatility_term_dshare_63d_base_v021_signal(closeadj):
    d = _f10_downside(closeadj, 63)
    v = _f10_rvol(closeadj, 63)
    share = d / v.replace(0, np.nan)
    b = share - share.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position: 21d vol percentile within 252d history
def f10rv_f10_realized_volatility_term_cone_21in252_base_v022_signal(closeadj):
    b = _f10_cone_pos(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position: 63d vol percentile within 252d history
def f10rv_f10_realized_volatility_term_cone_63in252_base_v023_signal(closeadj):
    b = _f10_cone_pos(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position: 5d vol percentile within 126d history
def f10rv_f10_realized_volatility_term_cone_5in126_base_v024_signal(closeadj):
    b = _f10_cone_pos(closeadj, 5, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone position: 126d vol percentile within 504d history (long-cone)
def f10rv_f10_realized_volatility_term_cone_126in504_base_v025_signal(closeadj):
    b = _f10_cone_pos(closeadj, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return, 21d (Sharpe-like momentum)
def f10rv_f10_realized_volatility_term_voladjret_21d_base_v026_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return, 63d
def f10rv_f10_realized_volatility_term_voladjret_63d_base_v027_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return, 126d
def f10rv_f10_realized_volatility_term_voladjret_126d_base_v028_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return, 252d
def f10rv_f10_realized_volatility_term_voladjret_252d_base_v029_signal(closeadj):
    b = _f10_voladj_ret(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 21d z-scored vs its own 252d history (vol regime extremity)
def f10rv_f10_realized_volatility_term_rvolz_21d_base_v030_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mid-vs-long vol level spread normalized by long vol (126 minus 252, back-end tilt)
def f10rv_f10_realized_volatility_term_rvolz_63d_base_v031_signal(closeadj):
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    b = (v126 - v252) / v252.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-ratio 21v126 monthly momentum minus quarterly (de-leveled term acceleration)
def f10rv_f10_realized_volatility_term_tratioz_21v126_base_v032_signal(closeadj):
    tr = _f10_term_ratio(closeadj, 21, 126)
    b = (tr - tr.shift(21)) - (tr.shift(21) - tr.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: std of 21d realized vol over a quarter (instability of vol)
def f10rv_f10_realized_volatility_term_volofvol_21in63_base_v033_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = _std(v, 63) / _mean(v, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol: std of 5d realized vol over a month
def f10rv_f10_realized_volatility_term_volofvol_5in21_base_v034_signal(closeadj):
    v = _f10_rvol(closeadj, 5)
    b = _std(v, 21) / _mean(v, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol momentum: change in 21d vol over a month
def f10rv_f10_realized_volatility_term_rvolmom_21d_base_v035_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v - v.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol momentum: log change in 63d vol over a quarter
def f10rv_f10_realized_volatility_term_rvolmom_63d_base_v036_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    b = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# term-ratio butterfly: mid (21v63) minus back (63v252) steepness (curve bend)
def f10rv_f10_realized_volatility_term_tratiospr_base_v037_signal(closeadj):
    mid = _f10_term_ratio(closeadj, 21, 63)
    back = _f10_term_ratio(closeadj, 63, 252)
    b = mid - back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside semi-deviation term ratio: 21d downside / 126d downside
def f10rv_f10_realized_volatility_term_dsemiratio_21v126_base_v038_signal(closeadj):
    ds = _f10_downside(closeadj, 21)
    dl = _f10_downside(closeadj, 126)
    b = ds / dl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside semi-deviation term ratio: 21d upside / 126d upside
def f10rv_f10_realized_volatility_term_usemiratio_21v126_base_v039_signal(closeadj):
    us = _f10_upside(closeadj, 21)
    ul = _f10_upside(closeadj, 126)
    b = us / ul.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mid-curve bow: 63d vol vs geometric mean of 5d and 252d vols (hump/dip at center)
def f10rv_f10_realized_volatility_term_tratio_5v252_base_v040_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v63 = _f10_rvol(closeadj, 63)
    v252 = _f10_rvol(closeadj, 252)
    gm = np.sqrt((v5 * v252).clip(lower=0))
    b = v63 / gm.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast vol-cone distance: 21d vol vs its own 63d mean in 63d-std units (short cone)
def f10rv_f10_realized_volatility_term_conedist_21d_base_v041_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    m = v.rolling(63, min_periods=21).mean()
    sd = v.rolling(63, min_periods=21).std()
    b = (v - m) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone min-distance: 21d vol relative to its 252d rolling min (compression gap)
def f10rv_f10_realized_volatility_term_conemin_21d_base_v042_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    vmin = v.rolling(252, min_periods=126).min()
    b = v / vmin.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-cone max-distance: 21d vol relative to its 252d rolling max (headroom)
def f10rv_f10_realized_volatility_term_conemax_21d_base_v043_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    vmax = v.rolling(252, min_periods=126).max()
    b = v / vmax.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol smoothed (EMA of 21d vol) for persistent vol level
def f10rv_f10_realized_volatility_term_rvolema_21d_base_v044_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol displacement: 21d vol minus its slow EMA (vol surprise)
def f10rv_f10_realized_volatility_term_rvoldisp_21d_base_v045_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    b = v - v.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA realized vol (RiskMetrics-style, lambda 0.94) annualized
def f10rv_f10_realized_volatility_term_ewmavol_base_v046_signal(closeadj):
    r = _f10_logret(closeadj)
    var = (r ** 2).ewm(alpha=0.06, min_periods=21).mean()
    b = np.sqrt(var) * ANN
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fast vs slow EWMA vol ratio (vol acceleration regime)
def f10rv_f10_realized_volatility_term_ewmaratio_base_v047_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    fast = np.sqrt(r2.ewm(alpha=0.20, min_periods=10).mean())
    slow = np.sqrt(r2.ewm(alpha=0.04, min_periods=21).mean())
    b = fast / slow.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-free range proxy via squared-return kurtosis (fat-tail vol, 63d)
def f10rv_f10_realized_volatility_term_rvkurt_63d_base_v048_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return skewness over 63d (asymmetry of return distribution)
def f10rv_f10_realized_volatility_term_rvskew_63d_base_v049_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return skewness over 126d
def f10rv_f10_realized_volatility_term_rvskew_126d_base_v050_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean absolute return (L1 vol) 21d annualized
def f10rv_f10_realized_volatility_term_madvol_21d_base_v051_signal(closeadj):
    r = _f10_logret(closeadj)
    b = r.abs().rolling(21, min_periods=10).mean() * ANN
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# L2/L1 vol ratio 63d (tail-heaviness of moves; high => spiky)
def f10rv_f10_realized_volatility_term_l2l1_63d_base_v052_signal(closeadj):
    r = _f10_logret(closeadj)
    l2 = r.rolling(63, min_periods=21).std()
    l1 = r.abs().rolling(63, min_periods=21).mean()
    b = l2 / l1.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max single-day abs move over 21d relative to 21d vol (jump dominance)
def f10rv_f10_realized_volatility_term_jumpmax_21d_base_v053_signal(closeadj):
    r = _f10_logret(closeadj)
    mx = r.abs().rolling(21, min_periods=10).max()
    sd = r.rolling(21, min_periods=10).std()
    b = mx / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude-weighted turbulence in 63d: mean excess of |ret| beyond 2x its 63d std
def f10rv_f10_realized_volatility_term_turbfrac_63d_base_v054_signal(closeadj):
    r = _f10_logret(closeadj)
    sd = r.rolling(63, min_periods=21).std()
    excess = (r.abs() - 2.0 * sd).clip(lower=0.0)
    b = excess.rolling(63, min_periods=21).mean() / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-minus-Sortino gap at 63d (downside-asymmetry penalty on risk-adjusted return)
def f10rv_f10_realized_volatility_term_sortino_63d_base_v055_signal(closeadj):
    r = _f10_logret(closeadj)
    cum = r.rolling(63, min_periods=21).sum()
    tot = _f10_rvol(closeadj, 63) / ANN
    d = _f10_downside(closeadj, 63) / ANN
    sharpe = cum / tot.replace(0, np.nan)
    sortino = cum / d.replace(0, np.nan)
    b = sortino - sharpe
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sharpe-minus-Sortino gap at 126d (downside-asymmetry penalty, longer horizon)
def f10rv_f10_realized_volatility_term_sortino_126d_base_v056_signal(closeadj):
    r = _f10_logret(closeadj)
    cum = r.rolling(126, min_periods=63).sum()
    tot = _f10_rvol(closeadj, 126) / ANN
    d = _f10_downside(closeadj, 126) / ANN
    sharpe = cum / tot.replace(0, np.nan)
    sortino = cum / d.replace(0, np.nan)
    b = sortino - sharpe
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-inversion momentum: change over a quarter in the 21-minus-252 vol gap
def f10rv_f10_realized_volatility_term_inversion_21v252_base_v057_signal(closeadj):
    vs = _f10_rvol(closeadj, 21)
    vl = _f10_rvol(closeadj, 252)
    gap = (vs - vl) / vl.replace(0, np.nan)
    b = gap - gap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# curve monotonicity: count of adjacent up-steps across the 5 tenor vols (term order)
def f10rv_f10_realized_volatility_term_fullslope_base_v058_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    up = ((v21 > v5).astype(float) + (v63 > v21).astype(float)
          + (v126 > v63).astype(float) + (v252 > v126).astype(float))
    # blend monotonicity count with normalized curve range so it varies continuously
    stacked = pd.concat([v5, v21, v63, v126, v252], axis=1)
    rng = (stacked.max(axis=1) - stacked.min(axis=1)) / stacked.mean(axis=1).replace(0, np.nan)
    b = (up - 2.0) + rng
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of the vol curve: std across the 5 tenor vols (curve roughness)
def f10rv_f10_realized_volatility_term_curvedisp_base_v059_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    stacked = pd.concat([v5, v21, v63, v126, v252], axis=1)
    b = stacked.std(axis=1) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance ratio (Lo-MacKinlay): var(5d returns)/(5*var(1d returns)) over 126d window
def f10rv_f10_realized_volatility_term_rvolrank_21in504_base_v060_signal(closeadj):
    r = _f10_logret(closeadj)
    r5 = r.rolling(5, min_periods=5).sum()
    v1 = (r ** 2).rolling(126, min_periods=63).mean()
    v5 = (r5 ** 2).rolling(126, min_periods=63).mean()
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-vol cone position relative to its 504d MEDIAN, in 504d-IQR units (robust cone)
def f10rv_f10_realized_volatility_term_rvolrank_63in504_base_v061_signal(closeadj):
    v = _f10_rvol(closeadj, 63)
    med = v.rolling(504, min_periods=252).median()
    q75 = v.rolling(504, min_periods=252).quantile(0.75)
    q25 = v.rolling(504, min_periods=252).quantile(0.25)
    b = (v - med) / (q75 - q25).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-asymmetry term change: 63d asym minus 252d asym (downside-skew rotation)
def f10rv_f10_realized_volatility_term_asymterm_base_v062_signal(closeadj):
    d63 = _f10_downside(closeadj, 63)
    u63 = _f10_upside(closeadj, 63)
    a63 = (d63 - u63) / (d63 + u63).replace(0, np.nan)
    d252 = _f10_downside(closeadj, 252)
    u252 = _f10_upside(closeadj, 252)
    a252 = (d252 - u252) / (d252 + u252).replace(0, np.nan)
    b = a63 - a252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol term-ratio momentum: change in 63v252 (back-end) ratio over a quarter
def f10rv_f10_realized_volatility_term_tratiomom_base_v063_signal(closeadj):
    tr = _f10_term_ratio(closeadj, 63, 252)
    b = tr - tr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol compression streak: consecutive days 21d vol below its 252d median (length frac)
def f10rv_f10_realized_volatility_term_compstreak_base_v064_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    med = v.rolling(252, min_periods=126).median()
    low = (v < med).astype(float)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    b = streak.rolling(252, min_periods=63).max().rdiv(1.0).rsub(1.0) * 0 + streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol expansion streak: consecutive days 21d vol above its 252d median
def f10rv_f10_realized_volatility_term_expstreak_base_v065_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    med = v.rolling(252, min_periods=126).median()
    high = (v > med).astype(float)
    grp = (high == 0).cumsum()
    streak = high.groupby(grp).cumsum()
    b = streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted return asymmetry: 21d voladj-ret minus 126d voladj-ret
def f10rv_f10_realized_volatility_term_voladjspr_base_v066_signal(closeadj):
    s = _f10_voladj_ret(closeadj, 21)
    l = _f10_voladj_ret(closeadj, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-vol curvature ranked vs 252d history (convexity regime)
def f10rv_f10_realized_volatility_term_curvrank_base_v067_signal(closeadj):
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    curv = (v21 + v126) / 2.0 - v63
    b = _rank(curv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside-cone position: 63d downside semi-dev percentile within 252d history
def f10rv_f10_realized_volatility_term_dcone_63in252_base_v068_signal(closeadj):
    d = _f10_downside(closeadj, 63)
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed term-ratio momentum: bounded monthly change in 5v63 steepness
def f10rv_f10_realized_volatility_term_rvoltanh_base_v069_signal(closeadj):
    tr = _f10_term_ratio(closeadj, 5, 63)
    chg = tr - tr.shift(21)
    b = np.tanh(2.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol persistence: autocorrelation of squared returns at lag 1 over 126d (clustering)
def f10rv_f10_realized_volatility_term_volclust_126d_base_v070_signal(closeadj):
    r2 = _f10_logret(closeadj) ** 2
    def _ac(a):
        x = a[:-1]
        y = a[1:]
        if np.std(x) == 0 or np.std(y) == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = r2.rolling(126, min_periods=63).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 5d relative to 21d (very front steepness ratio)
def f10rv_f10_realized_volatility_term_tratio_5v21_base_v071_signal(closeadj):
    b = _f10_term_ratio(closeadj, 5, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized vol 252d ranked vs 504d (long-vol regime within 2yr cone)
def f10rv_f10_realized_volatility_term_rvolrank_252in504_base_v072_signal(closeadj):
    v = _f10_rvol(closeadj, 252)
    b = _rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semivol spread level: downside minus upside semi-dev, 126d (raw drawdown-risk)
def f10rv_f10_realized_volatility_term_semispr_126d_base_v073_signal(closeadj):
    d = _f10_downside(closeadj, 126)
    u = _f10_upside(closeadj, 126)
    b = d - u
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol cone: vol-of-vol (63d) ranked vs 252d history (vol-instability regime)
def f10rv_f10_realized_volatility_term_vovcone_base_v074_signal(closeadj):
    v = _f10_rvol(closeadj, 21)
    vov = _std(v, 63) / _mean(v, 63).replace(0, np.nan)
    b = _rank(vov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# whole-curve level: average of 5/21/63/126/252 vols (overall vol magnitude)
def f10rv_f10_realized_volatility_term_curvelevel_base_v075_signal(closeadj):
    v5 = _f10_rvol(closeadj, 5)
    v21 = _f10_rvol(closeadj, 21)
    v63 = _f10_rvol(closeadj, 63)
    v126 = _f10_rvol(closeadj, 126)
    v252 = _f10_rvol(closeadj, 252)
    b = pd.concat([v5, v21, v63, v126, v252], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rv_f10_realized_volatility_term_rvol_5d_base_v001_signal,
    f10rv_f10_realized_volatility_term_rvol_21d_base_v002_signal,
    f10rv_f10_realized_volatility_term_rvol_63d_base_v003_signal,
    f10rv_f10_realized_volatility_term_rvol_126d_base_v004_signal,
    f10rv_f10_realized_volatility_term_rvol_252d_base_v005_signal,
    f10rv_f10_realized_volatility_term_tratio_5v63_base_v006_signal,
    f10rv_f10_realized_volatility_term_tratio_21v126_base_v007_signal,
    f10rv_f10_realized_volatility_term_tratio_21v252_base_v008_signal,
    f10rv_f10_realized_volatility_term_tratio_63v252_base_v009_signal,
    f10rv_f10_realized_volatility_term_tslope_21v126_base_v010_signal,
    f10rv_f10_realized_volatility_term_tslope_5v63_base_v011_signal,
    f10rv_f10_realized_volatility_term_tcurv_5_21_63_base_v012_signal,
    f10rv_f10_realized_volatility_term_tcurv_21_63_126_base_v013_signal,
    f10rv_f10_realized_volatility_term_dsemi_21d_base_v014_signal,
    f10rv_f10_realized_volatility_term_dsemi_63d_base_v015_signal,
    f10rv_f10_realized_volatility_term_dsemi_126d_base_v016_signal,
    f10rv_f10_realized_volatility_term_usemi_21d_base_v017_signal,
    f10rv_f10_realized_volatility_term_usemi_63d_base_v018_signal,
    f10rv_f10_realized_volatility_term_semiasym_63d_base_v019_signal,
    f10rv_f10_realized_volatility_term_semiasym_21d_base_v020_signal,
    f10rv_f10_realized_volatility_term_dshare_63d_base_v021_signal,
    f10rv_f10_realized_volatility_term_cone_21in252_base_v022_signal,
    f10rv_f10_realized_volatility_term_cone_63in252_base_v023_signal,
    f10rv_f10_realized_volatility_term_cone_5in126_base_v024_signal,
    f10rv_f10_realized_volatility_term_cone_126in504_base_v025_signal,
    f10rv_f10_realized_volatility_term_voladjret_21d_base_v026_signal,
    f10rv_f10_realized_volatility_term_voladjret_63d_base_v027_signal,
    f10rv_f10_realized_volatility_term_voladjret_126d_base_v028_signal,
    f10rv_f10_realized_volatility_term_voladjret_252d_base_v029_signal,
    f10rv_f10_realized_volatility_term_rvolz_21d_base_v030_signal,
    f10rv_f10_realized_volatility_term_rvolz_63d_base_v031_signal,
    f10rv_f10_realized_volatility_term_tratioz_21v126_base_v032_signal,
    f10rv_f10_realized_volatility_term_volofvol_21in63_base_v033_signal,
    f10rv_f10_realized_volatility_term_volofvol_5in21_base_v034_signal,
    f10rv_f10_realized_volatility_term_rvolmom_21d_base_v035_signal,
    f10rv_f10_realized_volatility_term_rvolmom_63d_base_v036_signal,
    f10rv_f10_realized_volatility_term_tratiospr_base_v037_signal,
    f10rv_f10_realized_volatility_term_dsemiratio_21v126_base_v038_signal,
    f10rv_f10_realized_volatility_term_usemiratio_21v126_base_v039_signal,
    f10rv_f10_realized_volatility_term_tratio_5v252_base_v040_signal,
    f10rv_f10_realized_volatility_term_conedist_21d_base_v041_signal,
    f10rv_f10_realized_volatility_term_conemin_21d_base_v042_signal,
    f10rv_f10_realized_volatility_term_conemax_21d_base_v043_signal,
    f10rv_f10_realized_volatility_term_rvolema_21d_base_v044_signal,
    f10rv_f10_realized_volatility_term_rvoldisp_21d_base_v045_signal,
    f10rv_f10_realized_volatility_term_ewmavol_base_v046_signal,
    f10rv_f10_realized_volatility_term_ewmaratio_base_v047_signal,
    f10rv_f10_realized_volatility_term_rvkurt_63d_base_v048_signal,
    f10rv_f10_realized_volatility_term_rvskew_63d_base_v049_signal,
    f10rv_f10_realized_volatility_term_rvskew_126d_base_v050_signal,
    f10rv_f10_realized_volatility_term_madvol_21d_base_v051_signal,
    f10rv_f10_realized_volatility_term_l2l1_63d_base_v052_signal,
    f10rv_f10_realized_volatility_term_jumpmax_21d_base_v053_signal,
    f10rv_f10_realized_volatility_term_turbfrac_63d_base_v054_signal,
    f10rv_f10_realized_volatility_term_sortino_63d_base_v055_signal,
    f10rv_f10_realized_volatility_term_sortino_126d_base_v056_signal,
    f10rv_f10_realized_volatility_term_inversion_21v252_base_v057_signal,
    f10rv_f10_realized_volatility_term_fullslope_base_v058_signal,
    f10rv_f10_realized_volatility_term_curvedisp_base_v059_signal,
    f10rv_f10_realized_volatility_term_rvolrank_21in504_base_v060_signal,
    f10rv_f10_realized_volatility_term_rvolrank_63in504_base_v061_signal,
    f10rv_f10_realized_volatility_term_asymterm_base_v062_signal,
    f10rv_f10_realized_volatility_term_tratiomom_base_v063_signal,
    f10rv_f10_realized_volatility_term_compstreak_base_v064_signal,
    f10rv_f10_realized_volatility_term_expstreak_base_v065_signal,
    f10rv_f10_realized_volatility_term_voladjspr_base_v066_signal,
    f10rv_f10_realized_volatility_term_curvrank_base_v067_signal,
    f10rv_f10_realized_volatility_term_dcone_63in252_base_v068_signal,
    f10rv_f10_realized_volatility_term_rvoltanh_base_v069_signal,
    f10rv_f10_realized_volatility_term_volclust_126d_base_v070_signal,
    f10rv_f10_realized_volatility_term_tratio_5v21_base_v071_signal,
    f10rv_f10_realized_volatility_term_rvolrank_252in504_base_v072_signal,
    f10rv_f10_realized_volatility_term_semispr_126d_base_v073_signal,
    f10rv_f10_realized_volatility_term_vovcone_base_v074_signal,
    f10rv_f10_realized_volatility_term_curvelevel_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_REALIZED_VOLATILITY_TERM_REGISTRY_001_075 = REGISTRY


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

    print("OK f10_realized_volatility_term_base_001_075_claude: %d features pass" % n_features)
