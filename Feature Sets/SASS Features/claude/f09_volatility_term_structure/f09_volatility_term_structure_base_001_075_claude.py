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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (close-to-close realized volatility term structure) =====
def _f09_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f09_rvol(closeadj, w):
    # annualized close-to-close realized volatility over window w
    r = _f09_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252.0)


def _f09_rvol_raw(closeadj, w):
    # non-annualized period std of log returns
    r = _f09_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_downvol(closeadj, w):
    # downside semi-deviation (annualized): std-like of negative returns only
    r = _f09_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    ss = (neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(ss) * np.sqrt(252.0)


def _f09_upvol(closeadj, w):
    r = _f09_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    ss = (pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(ss) * np.sqrt(252.0)


def _f09_volratio(closeadj, ws, wl):
    # term-structure slope as ratio short/long
    return _f09_rvol(closeadj, ws) / _f09_rvol(closeadj, wl).replace(0, np.nan)


def _f09_volslope(closeadj, ws, wl):
    # log-vol difference across two horizons normalized by log-horizon span (regression slope of 2 points)
    vs = _f09_rvol(closeadj, ws)
    vl = _f09_rvol(closeadj, wl)
    span = np.log(float(wl)) - np.log(float(ws))
    return (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span


def _f09_volcone(closeadj, w, hist):
    # vol-cone position: percentile rank of current realized vol vs its own history
    v = _f09_rvol(closeadj, w)
    return v.rolling(hist, min_periods=max(5, hist // 4)).rank(pct=True) - 0.5


def _f09_voladjret(closeadj, w):
    # vol-adjusted return: cumulative log return over w divided by realized vol over w
    r = _f09_logret(closeadj)
    cum = r.rolling(w, min_periods=max(2, w // 2)).sum()
    return cum / _f09_rvol_raw(closeadj, w).replace(0, np.nan)


def _f09_volcurv(closeadj, ws, wm, wl):
    # curvature: second difference of log-vol across three log-spaced horizons
    vs = np.log(_f09_rvol(closeadj, ws).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, wm).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, wl).replace(0, np.nan))
    return (vs - 2.0 * vm + vl)


# ============================================================
# --- realized vol levels at the canonical horizons (5/21/63/126/252) ---
def f09vt_f09_volatility_term_structure_rvol_5d_base_v001_signal(closeadj):
    b = _f09_rvol(closeadj, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_21d_base_v002_signal(closeadj):
    b = _f09_rvol(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_63d_base_v003_signal(closeadj):
    b = _f09_rvol(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_126d_base_v004_signal(closeadj):
    b = _f09_rvol(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_252d_base_v005_signal(closeadj):
    b = _f09_rvol(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol ratio short/long (term-structure slope, level form) ---
def f09vt_f09_volatility_term_structure_volratio_21v63_base_v006_signal(closeadj):
    # de-meaned mid-horizon slope (less dominated by raw short-vol level than 5v63)
    b = _f09_volratio(closeadj, 21, 63) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_21v126_base_v007_signal(closeadj):
    b = _f09_volratio(closeadj, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratiomom_21v252_base_v008_signal(closeadj):
    # momentum of the 21/252 term-structure slope (change over a month; level removed)
    rr = _f09_volratio(closeadj, 21, 252)
    b = rr - rr.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_63v252_base_v009_signal(closeadj):
    b = _f09_volratio(closeadj, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_5v21_base_v010_signal(closeadj):
    b = _f09_volratio(closeadj, 5, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope (log-vol regression across two horizons) ---
def f09vt_f09_volatility_term_structure_volslope_5v63_base_v011_signal(closeadj):
    b = _f09_volslope(closeadj, 5, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upslope_21v126_base_v012_signal(closeadj):
    # term-structure slope of the UPSIDE semi-deviation (distinct from total/downside slope)
    vs = _f09_upvol(closeadj, 21)
    vl = _f09_upvol(closeadj, 126)
    span = np.log(126.0) - np.log(21.0)
    b = (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downslope_21v126_base_v013_signal(closeadj):
    # term-structure slope of the DOWNSIDE semi-deviation (distinct from total-vol slope)
    vs = _f09_downvol(closeadj, 21)
    vl = _f09_downvol(closeadj, 126)
    span = np.log(126.0) - np.log(21.0)
    b = (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure curvature (3-point second difference of log-vol) ---
def f09vt_f09_volatility_term_structure_volcurv_5_21_63_base_v014_signal(closeadj):
    b = _f09_volcurv(closeadj, 5, 21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcurv_21_63_252_base_v015_signal(closeadj):
    b = _f09_volcurv(closeadj, 21, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcurv_21_63_126_base_v016_signal(closeadj):
    b = _f09_volcurv(closeadj, 21, 63, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position (percentile of current vol vs its own history) ---
def f09vt_f09_volatility_term_structure_volcone_21d_base_v017_signal(closeadj):
    b = _f09_volcone(closeadj, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_63d_base_v018_signal(closeadj):
    b = _f09_volcone(closeadj, 63, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_126d_base_v019_signal(closeadj):
    b = _f09_volcone(closeadj, 126, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_5d_base_v020_signal(closeadj):
    b = _f09_volcone(closeadj, 5, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside vs upside vol (semi-deviation asymmetry) ---
def f09vt_f09_volatility_term_structure_downvol_21d_base_v021_signal(closeadj):
    b = _f09_downvol(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downvol_63d_base_v022_signal(closeadj):
    b = _f09_downvol(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upvol_63d_base_v023_signal(closeadj):
    b = _f09_upvol(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskew_21d_base_v024_signal(closeadj):
    # downside-minus-upside semi-deviation (vol asymmetry)
    b = _f09_downvol(closeadj, 21) - _f09_upvol(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskew_63d_base_v025_signal(closeadj):
    b = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskewratiomom_63d_base_v026_signal(closeadj):
    # change in the downside/upside semi-deviation ratio (asymmetry momentum)
    rr = _f09_downvol(closeadj, 63) / _f09_upvol(closeadj, 63).replace(0, np.nan)
    b = rr - rr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskewratio_126d_base_v027_signal(closeadj):
    b = _f09_downvol(closeadj, 126) / _f09_upvol(closeadj, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return (Sharpe-like over the term structure) ---
def f09vt_f09_volatility_term_structure_voladjret_21d_base_v028_signal(closeadj):
    b = _f09_voladjret(closeadj, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_63d_base_v029_signal(closeadj):
    b = _f09_voladjret(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_126d_base_v030_signal(closeadj):
    b = _f09_voladjret(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_252d_base_v031_signal(closeadj):
    b = _f09_voladjret(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol level z-scored vs its own history (de-trended vol level) ---
def f09vt_f09_volatility_term_structure_rvolz_21d_base_v032_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvolz_63d_base_v033_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = _z(v, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvolz_126d_base_v034_signal(closeadj):
    # long-horizon vol momentum: change in the 126d vol over a half-year (vol trend, not level)
    v = _f09_rvol(closeadj, 126)
    b = v - v.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol ratio z-scored (term-structure slope de-trended) ---
def f09vt_f09_volatility_term_structure_volratioz_63v126_base_v035_signal(closeadj):
    # mid-vs-long slope, z-scored vs its own history (distinct window pair from v007)
    rr = _f09_volratio(closeadj, 63, 126)
    b = _z(rr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratioz_5v63_base_v036_signal(closeadj):
    rr = _f09_volratio(closeadj, 5, 63)
    b = _z(rr, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- twist: front-end slope minus back-end slope (term-structure twist) ---
def f09vt_f09_volatility_term_structure_twist_base_v037_signal(closeadj):
    front = _f09_volslope(closeadj, 5, 63)
    back = _f09_volslope(closeadj, 63, 252)
    b = front - back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slopemom_5v63_base_v038_signal(closeadj):
    sl = _f09_volslope(closeadj, 5, 63)
    b = sl - sl.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside vol term structure, normalized slope form (back-end downside) ---
def f09vt_f09_volatility_term_structure_downratio_63v252_base_v039_signal(closeadj):
    vs = _f09_downvol(closeadj, 63)
    vl = _f09_downvol(closeadj, 252)
    b = (vs - vl) / (vs + vl).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upvolcone_63d_base_v040_signal(closeadj):
    # upside vol-cone position (upside-vol regime percentile; distinct from upside slope)
    uv = _f09_upvol(closeadj, 63)
    b = uv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position spread (short cone vs long cone disagreement) ---
def f09vt_f09_volatility_term_structure_conespread_21v126_base_v041_signal(closeadj):
    c1 = _f09_volcone(closeadj, 21, 252)
    c2 = _f09_volcone(closeadj, 126, 504)
    b = c1 - c2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol of the realized vol (vol-of-vol) ---
def f09vt_f09_volatility_term_structure_volofvol_63d_base_v042_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = v.pct_change().rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volofvol_126d_base_v043_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = v.pct_change().rolling(126, min_periods=42).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term structure of vol-of-vol: short-window vov relative to long-window vov ---
def f09vt_f09_volatility_term_structure_vovterm_base_v044_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    chg = v.pct_change()
    vov_short = chg.rolling(42, min_periods=21).std()
    vov_long = chg.rolling(252, min_periods=63).std()
    b = vov_short / vov_long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voldiff_63v126_base_v045_signal(closeadj):
    # normalized mid/long term-structure slope (scale-free; distinct window pair)
    vs = _f09_rvol(closeadj, 63)
    vl = _f09_rvol(closeadj, 126)
    b = (vs - vl) / (vs + vl).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone extremity (squared distance from median cone position) ---
def f09vt_f09_volatility_term_structure_coneextreme_63d_base_v046_signal(closeadj):
    c = _f09_volcone(closeadj, 63, 504)
    b = np.sign(c) * (c ** 2) * 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return spread short vs long (term-structure Sharpe slope) ---
def f09vt_f09_volatility_term_structure_sharpespread_21v126_base_v047_signal(closeadj):
    b = _f09_voladjret(closeadj, 21) - _f09_voladjret(closeadj, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- Sortino-to-Sharpe ratio at the long horizon, z-scored (pure downside-penalty regime) ---
def f09vt_f09_volatility_term_structure_sortino_252d_base_v048_signal(closeadj):
    tot = _f09_rvol(closeadj, 252)
    dv = _f09_downvol(closeadj, 252)
    raw = tot / dv.replace(0, np.nan)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sharperatio_spread_base_v049_signal(closeadj):
    # vol-adjusted-return term-structure spread: short Sharpe minus long Sharpe
    r = _f09_logret(closeadj)
    short = r.rolling(21, min_periods=10).sum() / _f09_rvol_raw(closeadj, 21).replace(0, np.nan)
    long = r.rolling(252, min_periods=63).sum() / _f09_rvol_raw(closeadj, 252).replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-horizon vol dispersion (term-structure roughness) ---
def f09vt_f09_volatility_term_structure_voldispersion_base_v050_signal(closeadj):
    v1 = _f09_rvol(closeadj, 5)
    v2 = _f09_rvol(closeadj, 21)
    v3 = _f09_rvol(closeadj, 63)
    v4 = _f09_rvol(closeadj, 252)
    b = pd.concat([v1, v2, v3, v4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope via OLS across many log-horizons ---
def f09vt_f09_volatility_term_structure_olsslope_base_v051_signal(closeadj):
    ws = [5, 10, 21, 42, 63, 126, 252]
    logw = np.log(np.array(ws, dtype=float))
    logw = logw - logw.mean()
    denom = float((logw ** 2).sum())
    vols = [np.log(_f09_rvol(closeadj, w).replace(0, np.nan)) for w in ws]
    mat = pd.concat(vols, axis=1)
    mat.columns = range(len(ws))
    centered = mat.sub(mat.mean(axis=1), axis=0)
    num = (centered * logw).sum(axis=1)
    b = num / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol level percentile vs cross-time (vol regime level) ---
def f09vt_f09_volatility_term_structure_volpct_252d_base_v052_signal(closeadj):
    v = _f09_rvol(closeadj, 252)
    b = _rank(v, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol acceleration: short-vol momentum (change in 21d vol over a month) ---
def f09vt_f09_volatility_term_structure_volmom_252d_base_v053_signal(closeadj):
    # long-run vol trend: log change in 252d realized vol over a quarter
    v = _f09_rvol(closeadj, 252)
    b = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volaccel_21d_base_v054_signal(closeadj):
    # vol acceleration: second difference of log 21d vol (is vol-rise speeding up)
    lv = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    b = lv - 2.0 * lv.shift(21) + lv.shift(42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- asymmetry term structure as a ratio of short-skew to long-skew (sign-aware) ---
def f09vt_f09_volatility_term_structure_asymratio_base_v055_signal(closeadj):
    short = _f09_downvol(closeadj, 21) - _f09_upvol(closeadj, 21)
    long = _f09_downvol(closeadj, 252) - _f09_upvol(closeadj, 252)
    denom = (short.abs() + long.abs()).replace(0, np.nan)
    b = (short - long) / denom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position weighted by term-structure slope (extreme-and-steep) ---
def f09vt_f09_volatility_term_structure_conexslope_63d_base_v056_signal(closeadj):
    c = _f09_volcone(closeadj, 63, 504)
    sl = _f09_volslope(closeadj, 21, 252)
    b = c * sl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- backwardation flag persistence: fraction of time short>long vol ---
def f09vt_f09_volatility_term_structure_backwardation_base_v057_signal(closeadj):
    rr = _f09_volratio(closeadj, 21, 252)
    flag = (rr > 1.0).astype(float)
    persist = flag.rolling(63, min_periods=21).mean()
    b = persist + 0.5 * (rr - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-adjusted return ranked vs own history ---
def f09vt_f09_volatility_term_structure_sharperank_63d_base_v058_signal(closeadj):
    sh = _f09_voladjret(closeadj, 63)
    b = _rank(sh, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope smoothed (persistent slope regime) ---
def f09vt_f09_volatility_term_structure_slopeema_base_v059_signal(closeadj):
    sl = _f09_volslope(closeadj, 21, 252)
    b = sl.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol ratio momentum (change in the short/long slope over a quarter) ---
def f09vt_f09_volatility_term_structure_ratiomom_21v126_base_v060_signal(closeadj):
    rr = _f09_volratio(closeadj, 21, 126)
    b = rr - rr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- annualized vol gap between semidev sum and total vol (fat-tail proxy) ---
def f09vt_f09_volatility_term_structure_semisumgap_63d_base_v061_signal(closeadj):
    tot = _f09_rvol(closeadj, 63)
    dv = _f09_downvol(closeadj, 63)
    uv = _f09_upvol(closeadj, 63)
    combined = np.sqrt(dv ** 2 + uv ** 2)
    b = combined - tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-cone position change (cone momentum) ---
def f09vt_f09_volatility_term_structure_conemom_21d_base_v062_signal(closeadj):
    c = _f09_volcone(closeadj, 21, 252)
    b = c - c.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- front-end backwardation momentum (change in the 5v126 ratio; level removed) ---
def f09vt_f09_volatility_term_structure_ratiomom_5v126_base_v063_signal(closeadj):
    rr = _f09_volratio(closeadj, 5, 126)
    b = rr - rr.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol curvature on a distinct triple, z-scored (humped term structure de-trended) ---
def f09vt_f09_volatility_term_structure_curvz_base_v064_signal(closeadj):
    cv = _f09_volcurv(closeadj, 5, 42, 126)
    b = _z(cv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- realized vol of short window minus EMA-vol (vol displacement) ---
def f09vt_f09_volatility_term_structure_voldisp_21d_base_v065_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = v - v.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside vol cone position (downside vol regime) ---
def f09vt_f09_volatility_term_structure_downcone_63d_base_v066_signal(closeadj):
    dv = _f09_downvol(closeadj, 63)
    b = dv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slope sign persistence (contango vs backwardation regime) ---
def f09vt_f09_volatility_term_structure_slopesign_base_v067_signal(closeadj):
    sl = _f09_volslope(closeadj, 21, 252)
    sign = np.sign(sl)
    b = sign.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- short shock scaled by long-run vol regime (regime-normalized impulse) ---
def f09vt_f09_volatility_term_structure_regimesharpe_base_v068_signal(closeadj):
    r = _f09_logret(closeadj)
    cum = r.rolling(5, min_periods=3).sum()
    vlong = _f09_rvol_raw(closeadj, 252)
    b = cum / vlong.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-share term-structure spread (short downside dominance vs long) ---
def f09vt_f09_volatility_term_structure_downshare_spread_base_v069_signal(closeadj):
    short = _f09_downvol(closeadj, 21) / _f09_rvol(closeadj, 21).replace(0, np.nan)
    long = _f09_downvol(closeadj, 126) / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downshare_cone_base_v070_signal(closeadj):
    # vol-cone position of the 21d downside-share (downside-dominance regime percentile)
    dv = _f09_downvol(closeadj, 21)
    tot = _f09_rvol(closeadj, 21)
    share = dv / tot.replace(0, np.nan)
    b = share.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-horizon vol cone average (broad regime position) ---
def f09vt_f09_volatility_term_structure_conebroad_base_v071_signal(closeadj):
    c1 = _f09_volcone(closeadj, 21, 252)
    c2 = _f09_volcone(closeadj, 63, 504)
    c3 = _f09_volcone(closeadj, 126, 504)
    b = pd.concat([c1, c2, c3], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- convexity of the DOWNSIDE vol term structure (short+long minus 2*mid, ratio form) ---
def f09vt_f09_volatility_term_structure_convratio_base_v072_signal(closeadj):
    vs = _f09_downvol(closeadj, 5)
    vm = _f09_downvol(closeadj, 63)
    vl = _f09_downvol(closeadj, 252)
    b = (vs + vl) / (2.0 * vm).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- exceedance hit-rate plus magnitude: how often AND how far 21d vol sits above its 252d median ---
def f09vt_f09_volatility_term_structure_volhitrate_21d_base_v073_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    base = v.rolling(252, min_periods=63).median()
    above = (v > base).astype(float)
    rate = above.rolling(63, min_periods=21).mean() - 0.5
    excess = ((v - base) / base.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 0.5 * excess
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- semi-dev asymmetry ranked vs history (skew-in-vol regime) ---
def f09vt_f09_volatility_term_structure_skewrank_63d_base_v074_signal(closeadj):
    sk = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    b = _rank(sk, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- downside-skew interacted with vol-cone position (extreme asymmetric stress) ---
def f09vt_f09_volatility_term_structure_skewstress_base_v075_signal(closeadj):
    skew = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    cone = _f09_volcone(closeadj, 63, 504)
    b = skew * cone
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09vt_f09_volatility_term_structure_rvol_5d_base_v001_signal,
    f09vt_f09_volatility_term_structure_rvol_21d_base_v002_signal,
    f09vt_f09_volatility_term_structure_rvol_63d_base_v003_signal,
    f09vt_f09_volatility_term_structure_rvol_126d_base_v004_signal,
    f09vt_f09_volatility_term_structure_rvol_252d_base_v005_signal,
    f09vt_f09_volatility_term_structure_volratio_21v63_base_v006_signal,
    f09vt_f09_volatility_term_structure_volratio_21v126_base_v007_signal,
    f09vt_f09_volatility_term_structure_volratiomom_21v252_base_v008_signal,
    f09vt_f09_volatility_term_structure_volratio_63v252_base_v009_signal,
    f09vt_f09_volatility_term_structure_volratio_5v21_base_v010_signal,
    f09vt_f09_volatility_term_structure_volslope_5v63_base_v011_signal,
    f09vt_f09_volatility_term_structure_upslope_21v126_base_v012_signal,
    f09vt_f09_volatility_term_structure_downslope_21v126_base_v013_signal,
    f09vt_f09_volatility_term_structure_volcurv_5_21_63_base_v014_signal,
    f09vt_f09_volatility_term_structure_volcurv_21_63_252_base_v015_signal,
    f09vt_f09_volatility_term_structure_volcurv_21_63_126_base_v016_signal,
    f09vt_f09_volatility_term_structure_volcone_21d_base_v017_signal,
    f09vt_f09_volatility_term_structure_volcone_63d_base_v018_signal,
    f09vt_f09_volatility_term_structure_volcone_126d_base_v019_signal,
    f09vt_f09_volatility_term_structure_volcone_5d_base_v020_signal,
    f09vt_f09_volatility_term_structure_downvol_21d_base_v021_signal,
    f09vt_f09_volatility_term_structure_downvol_63d_base_v022_signal,
    f09vt_f09_volatility_term_structure_upvol_63d_base_v023_signal,
    f09vt_f09_volatility_term_structure_volskew_21d_base_v024_signal,
    f09vt_f09_volatility_term_structure_volskew_63d_base_v025_signal,
    f09vt_f09_volatility_term_structure_volskewratiomom_63d_base_v026_signal,
    f09vt_f09_volatility_term_structure_volskewratio_126d_base_v027_signal,
    f09vt_f09_volatility_term_structure_voladjret_21d_base_v028_signal,
    f09vt_f09_volatility_term_structure_voladjret_63d_base_v029_signal,
    f09vt_f09_volatility_term_structure_voladjret_126d_base_v030_signal,
    f09vt_f09_volatility_term_structure_voladjret_252d_base_v031_signal,
    f09vt_f09_volatility_term_structure_rvolz_21d_base_v032_signal,
    f09vt_f09_volatility_term_structure_rvolz_63d_base_v033_signal,
    f09vt_f09_volatility_term_structure_rvolz_126d_base_v034_signal,
    f09vt_f09_volatility_term_structure_volratioz_63v126_base_v035_signal,
    f09vt_f09_volatility_term_structure_volratioz_5v63_base_v036_signal,
    f09vt_f09_volatility_term_structure_twist_base_v037_signal,
    f09vt_f09_volatility_term_structure_slopemom_5v63_base_v038_signal,
    f09vt_f09_volatility_term_structure_downratio_63v252_base_v039_signal,
    f09vt_f09_volatility_term_structure_upvolcone_63d_base_v040_signal,
    f09vt_f09_volatility_term_structure_conespread_21v126_base_v041_signal,
    f09vt_f09_volatility_term_structure_volofvol_63d_base_v042_signal,
    f09vt_f09_volatility_term_structure_volofvol_126d_base_v043_signal,
    f09vt_f09_volatility_term_structure_vovterm_base_v044_signal,
    f09vt_f09_volatility_term_structure_voldiff_63v126_base_v045_signal,
    f09vt_f09_volatility_term_structure_coneextreme_63d_base_v046_signal,
    f09vt_f09_volatility_term_structure_sharpespread_21v126_base_v047_signal,
    f09vt_f09_volatility_term_structure_sortino_252d_base_v048_signal,
    f09vt_f09_volatility_term_structure_sharperatio_spread_base_v049_signal,
    f09vt_f09_volatility_term_structure_voldispersion_base_v050_signal,
    f09vt_f09_volatility_term_structure_olsslope_base_v051_signal,
    f09vt_f09_volatility_term_structure_volpct_252d_base_v052_signal,
    f09vt_f09_volatility_term_structure_volmom_252d_base_v053_signal,
    f09vt_f09_volatility_term_structure_volaccel_21d_base_v054_signal,
    f09vt_f09_volatility_term_structure_asymratio_base_v055_signal,
    f09vt_f09_volatility_term_structure_conexslope_63d_base_v056_signal,
    f09vt_f09_volatility_term_structure_backwardation_base_v057_signal,
    f09vt_f09_volatility_term_structure_sharperank_63d_base_v058_signal,
    f09vt_f09_volatility_term_structure_slopeema_base_v059_signal,
    f09vt_f09_volatility_term_structure_ratiomom_21v126_base_v060_signal,
    f09vt_f09_volatility_term_structure_semisumgap_63d_base_v061_signal,
    f09vt_f09_volatility_term_structure_conemom_21d_base_v062_signal,
    f09vt_f09_volatility_term_structure_ratiomom_5v126_base_v063_signal,
    f09vt_f09_volatility_term_structure_curvz_base_v064_signal,
    f09vt_f09_volatility_term_structure_voldisp_21d_base_v065_signal,
    f09vt_f09_volatility_term_structure_downcone_63d_base_v066_signal,
    f09vt_f09_volatility_term_structure_slopesign_base_v067_signal,
    f09vt_f09_volatility_term_structure_regimesharpe_base_v068_signal,
    f09vt_f09_volatility_term_structure_downshare_spread_base_v069_signal,
    f09vt_f09_volatility_term_structure_downshare_cone_base_v070_signal,
    f09vt_f09_volatility_term_structure_conebroad_base_v071_signal,
    f09vt_f09_volatility_term_structure_convratio_base_v072_signal,
    f09vt_f09_volatility_term_structure_volhitrate_21d_base_v073_signal,
    f09vt_f09_volatility_term_structure_skewrank_63d_base_v074_signal,
    f09vt_f09_volatility_term_structure_skewstress_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_TERM_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f09_volatility_term_structure_base_001_075_claude: %d features pass" % n_features)
