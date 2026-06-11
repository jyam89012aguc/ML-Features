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


def _f09_logret(closeadj):
    return np.log(closeadj.replace(0, np.nan)).diff()


def _f09_rvol(closeadj, w):
    r = _f09_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(252.0)


def _f09_rvol_raw(closeadj, w):
    r = _f09_logret(closeadj)
    return r.rolling(w, min_periods=max(2, w // 2)).std()


def _f09_ewvol(closeadj, span):
    r = _f09_logret(closeadj)
    return r.ewm(span=span, min_periods=max(2, span // 2)).std() * np.sqrt(252.0)


def _f09_downvol(closeadj, w):
    r = _f09_logret(closeadj)
    neg = r.where(r < 0, 0.0)
    ss = (neg ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(ss) * np.sqrt(252.0)


def _f09_upvol(closeadj, w):
    r = _f09_logret(closeadj)
    pos = r.where(r > 0, 0.0)
    ss = (pos ** 2).rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(ss) * np.sqrt(252.0)


def _f09_mad_vol(closeadj, w):
    r = _f09_logret(closeadj)
    mu = r.rolling(w, min_periods=max(2, w // 2)).mean()
    return (r - mu).abs().rolling(w, min_periods=max(2, w // 2)).mean() * np.sqrt(252.0)


def _f09_volratio(closeadj, ws, wl):
    return _f09_rvol(closeadj, ws) / _f09_rvol(closeadj, wl).replace(0, np.nan)


def _f09_volslope(closeadj, ws, wl):
    vs = _f09_rvol(closeadj, ws)
    vl = _f09_rvol(closeadj, wl)
    span = np.log(float(wl)) - np.log(float(ws))
    return (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span


def _f09_volcone(closeadj, w, hist):
    v = _f09_rvol(closeadj, w)
    return v.rolling(hist, min_periods=max(5, hist // 4)).rank(pct=True) - 0.5


def _f09_voladjret(closeadj, w):
    r = _f09_logret(closeadj)
    cum = r.rolling(w, min_periods=max(2, w // 2)).sum()
    return cum / _f09_rvol_raw(closeadj, w).replace(0, np.nan)


def _f09_volcurv(closeadj, ws, wm, wl):
    vs = np.log(_f09_rvol(closeadj, ws).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, wm).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, wl).replace(0, np.nan))
    return (vs - 2.0 * vm + vl)


def f09vt_f09_volatility_term_structure_rvol_5d_jerk_v001_signal(closeadj):
    b = _f09_rvol(closeadj, 5)
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_21d_jerk_v002_signal(closeadj):
    b = _f09_rvol(closeadj, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_63d_jerk_v003_signal(closeadj):
    b = _f09_rvol(closeadj, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_126d_jerk_v004_signal(closeadj):
    b = _f09_rvol(closeadj, 126)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvol_252d_jerk_v005_signal(closeadj):
    b = _f09_rvol(closeadj, 252)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_21v63_jerk_v006_signal(closeadj):
    b = _f09_volratio(closeadj, 21, 63) - 1.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_21v126_jerk_v007_signal(closeadj):
    b = _f09_volratio(closeadj, 21, 126)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratiomom_21v252_jerk_v008_signal(closeadj):
    rr = _f09_volratio(closeadj, 21, 252)
    b = rr - rr.shift(21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_63v252_jerk_v009_signal(closeadj):
    b = _f09_volratio(closeadj, 63, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratio_5v21_jerk_v010_signal(closeadj):
    b = _f09_volratio(closeadj, 5, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volslope_5v63_jerk_v011_signal(closeadj):
    b = _f09_volslope(closeadj, 5, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upslope_21v126_jerk_v012_signal(closeadj):
    vs = _f09_upvol(closeadj, 21)
    vl = _f09_upvol(closeadj, 126)
    span = np.log(126.0) - np.log(21.0)
    b = (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downslope_21v126_jerk_v013_signal(closeadj):
    vs = _f09_downvol(closeadj, 21)
    vl = _f09_downvol(closeadj, 126)
    span = np.log(126.0) - np.log(21.0)
    b = (np.log(vl.replace(0, np.nan)) - np.log(vs.replace(0, np.nan))) / span
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcurv_5_21_63_jerk_v014_signal(closeadj):
    b = _f09_volcurv(closeadj, 5, 21, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcurv_21_63_252_jerk_v015_signal(closeadj):
    b = _f09_volcurv(closeadj, 21, 63, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcurv_21_63_126_jerk_v016_signal(closeadj):
    b = _f09_volcurv(closeadj, 21, 63, 126)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_21d_jerk_v017_signal(closeadj):
    b = _f09_volcone(closeadj, 21, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_63d_jerk_v018_signal(closeadj):
    b = _f09_volcone(closeadj, 63, 504)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_126d_jerk_v019_signal(closeadj):
    b = _f09_volcone(closeadj, 126, 504)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcone_5d_jerk_v020_signal(closeadj):
    b = _f09_volcone(closeadj, 5, 126)
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = _d.ewm(span=max(3, 5), min_periods=max(2, 5 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downvol_21d_jerk_v021_signal(closeadj):
    b = _f09_downvol(closeadj, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downvol_63d_jerk_v022_signal(closeadj):
    b = _f09_downvol(closeadj, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upvol_63d_jerk_v023_signal(closeadj):
    b = _f09_upvol(closeadj, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskew_21d_jerk_v024_signal(closeadj):
    b = _f09_downvol(closeadj, 21) - _f09_upvol(closeadj, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskew_63d_jerk_v025_signal(closeadj):
    b = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskewratiomom_63d_jerk_v026_signal(closeadj):
    rr = _f09_downvol(closeadj, 63) / _f09_upvol(closeadj, 63).replace(0, np.nan)
    b = rr - rr.shift(63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskewratio_126d_jerk_v027_signal(closeadj):
    b = _f09_downvol(closeadj, 126) / _f09_upvol(closeadj, 126).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_21d_jerk_v028_signal(closeadj):
    b = _f09_voladjret(closeadj, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_63d_jerk_v029_signal(closeadj):
    b = _f09_voladjret(closeadj, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_126d_jerk_v030_signal(closeadj):
    b = _f09_voladjret(closeadj, 126)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_252d_jerk_v031_signal(closeadj):
    b = _f09_voladjret(closeadj, 252)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvolz_21d_jerk_v032_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = _z(v, 252)
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvolz_63d_jerk_v033_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = _z(v, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_rvolz_126d_jerk_v034_signal(closeadj):
    v = _f09_rvol(closeadj, 126)
    b = v - v.shift(126)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratioz_63v126_jerk_v035_signal(closeadj):
    rr = _f09_volratio(closeadj, 63, 126)
    b = _z(rr, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volratioz_5v63_jerk_v036_signal(closeadj):
    rr = _f09_volratio(closeadj, 5, 63)
    b = _z(rr, 126)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_twist_jerk_v037_signal(closeadj):
    front = _f09_volslope(closeadj, 5, 63)
    back = _f09_volslope(closeadj, 63, 252)
    b = front - back
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slopemom_5v63_jerk_v038_signal(closeadj):
    sl = _f09_volslope(closeadj, 5, 63)
    b = sl - sl.shift(5)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downratio_63v252_jerk_v039_signal(closeadj):
    vs = _f09_downvol(closeadj, 63)
    vl = _f09_downvol(closeadj, 252)
    b = (vs - vl) / (vs + vl).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upvolcone_63d_jerk_v040_signal(closeadj):
    uv = _f09_upvol(closeadj, 63)
    b = uv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_conespread_21v126_jerk_v041_signal(closeadj):
    c1 = _f09_volcone(closeadj, 21, 252)
    c2 = _f09_volcone(closeadj, 126, 504)
    b = c1 - c2
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volofvol_63d_jerk_v042_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = v.pct_change().rolling(63, min_periods=21).std()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volofvol_126d_jerk_v043_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = v.pct_change().rolling(126, min_periods=42).std()
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_vovterm_jerk_v044_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    chg = v.pct_change()
    vov_short = chg.rolling(42, min_periods=21).std()
    vov_long = chg.rolling(252, min_periods=63).std()
    b = vov_short / vov_long.replace(0, np.nan) - 1.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voldiff_63v126_jerk_v045_signal(closeadj):
    vs = _f09_rvol(closeadj, 63)
    vl = _f09_rvol(closeadj, 126)
    b = (vs - vl) / (vs + vl).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_coneextreme_63d_jerk_v046_signal(closeadj):
    c = _f09_volcone(closeadj, 63, 504)
    b = np.sign(c) * (c ** 2) * 4.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sharpespread_21v126_jerk_v047_signal(closeadj):
    b = _f09_voladjret(closeadj, 21) - _f09_voladjret(closeadj, 126)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sortino_252d_jerk_v048_signal(closeadj):
    tot = _f09_rvol(closeadj, 252)
    dv = _f09_downvol(closeadj, 252)
    raw = tot / dv.replace(0, np.nan)
    b = _z(raw, 252)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sharperatio_spread_jerk_v049_signal(closeadj):
    r = _f09_logret(closeadj)
    short = r.rolling(21, min_periods=10).sum() / _f09_rvol_raw(closeadj, 21).replace(0, np.nan)
    long = r.rolling(252, min_periods=63).sum() / _f09_rvol_raw(closeadj, 252).replace(0, np.nan)
    b = short - long
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voldispersion_jerk_v050_signal(closeadj):
    v1 = _f09_rvol(closeadj, 5)
    v2 = _f09_rvol(closeadj, 21)
    v3 = _f09_rvol(closeadj, 63)
    v4 = _f09_rvol(closeadj, 252)
    b = pd.concat([v1, v2, v3, v4], axis=1).std(axis=1)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_olsslope_jerk_v051_signal(closeadj):
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
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volpct_252d_jerk_v052_signal(closeadj):
    v = _f09_rvol(closeadj, 252)
    b = _rank(v, 504)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volmom_252d_jerk_v053_signal(closeadj):
    v = _f09_rvol(closeadj, 252)
    b = np.log(v.replace(0, np.nan) / v.shift(63).replace(0, np.nan))
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volaccel_21d_jerk_v054_signal(closeadj):
    lv = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    b = lv - 2.0 * lv.shift(21) + lv.shift(42)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_asymratio_jerk_v055_signal(closeadj):
    short = _f09_downvol(closeadj, 21) - _f09_upvol(closeadj, 21)
    long = _f09_downvol(closeadj, 252) - _f09_upvol(closeadj, 252)
    denom = (short.abs() + long.abs()).replace(0, np.nan)
    b = (short - long) / denom
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_conexslope_63d_jerk_v056_signal(closeadj):
    c = _f09_volcone(closeadj, 63, 504)
    sl = _f09_volslope(closeadj, 21, 252)
    b = c * sl
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_backwardation_jerk_v057_signal(closeadj):
    rr = _f09_volratio(closeadj, 21, 252)
    flag = (rr > 1.0).astype(float)
    persist = flag.rolling(63, min_periods=21).mean()
    b = persist + 0.5 * (rr - 1.0)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sharperank_63d_jerk_v058_signal(closeadj):
    sh = _f09_voladjret(closeadj, 63)
    b = _rank(sh, 504)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slopeema_jerk_v059_signal(closeadj):
    sl = _f09_volslope(closeadj, 21, 252)
    b = sl.ewm(span=42, min_periods=21).mean()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ratiomom_21v126_jerk_v060_signal(closeadj):
    rr = _f09_volratio(closeadj, 21, 126)
    b = rr - rr.shift(63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_semisumgap_63d_jerk_v061_signal(closeadj):
    tot = _f09_rvol(closeadj, 63)
    dv = _f09_downvol(closeadj, 63)
    uv = _f09_upvol(closeadj, 63)
    combined = np.sqrt(dv ** 2 + uv ** 2)
    b = combined - tot
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_conemom_21d_jerk_v062_signal(closeadj):
    c = _f09_volcone(closeadj, 21, 252)
    b = c - c.shift(21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ratiomom_5v126_jerk_v063_signal(closeadj):
    rr = _f09_volratio(closeadj, 5, 126)
    b = rr - rr.shift(5)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_curvz_jerk_v064_signal(closeadj):
    cv = _f09_volcurv(closeadj, 5, 42, 126)
    b = _z(cv, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voldisp_21d_jerk_v065_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    b = v - v.ewm(span=63, min_periods=21).mean()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = np.sign(_d) * _d.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downcone_63d_jerk_v066_signal(closeadj):
    dv = _f09_downvol(closeadj, 63)
    b = dv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slopesign_jerk_v067_signal(closeadj):
    sl = _f09_volslope(closeadj, 21, 252)
    sign = np.sign(sl)
    b = sign.rolling(63, min_periods=21).mean()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_regimesharpe_jerk_v068_signal(closeadj):
    r = _f09_logret(closeadj)
    cum = r.rolling(5, min_periods=3).sum()
    vlong = _f09_rvol_raw(closeadj, 252)
    b = cum / vlong.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downshare_spread_jerk_v069_signal(closeadj):
    short = _f09_downvol(closeadj, 21) / _f09_rvol(closeadj, 21).replace(0, np.nan)
    long = _f09_downvol(closeadj, 126) / _f09_rvol(closeadj, 126).replace(0, np.nan)
    b = short - long
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downshare_cone_jerk_v070_signal(closeadj):
    dv = _f09_downvol(closeadj, 21)
    tot = _f09_rvol(closeadj, 21)
    share = dv / tot.replace(0, np.nan)
    b = share.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_conebroad_jerk_v071_signal(closeadj):
    c1 = _f09_volcone(closeadj, 21, 252)
    c2 = _f09_volcone(closeadj, 63, 504)
    c3 = _f09_volcone(closeadj, 126, 504)
    b = pd.concat([c1, c2, c3], axis=1).mean(axis=1)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_convratio_jerk_v072_signal(closeadj):
    vs = _f09_downvol(closeadj, 5)
    vm = _f09_downvol(closeadj, 63)
    vl = _f09_downvol(closeadj, 252)
    b = (vs + vl) / (2.0 * vm).replace(0, np.nan) - 1.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volhitrate_21d_jerk_v073_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    base = v.rolling(252, min_periods=63).median()
    above = (v > base).astype(float)
    rate = above.rolling(63, min_periods=21).mean() - 0.5
    excess = ((v - base) / base.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 0.5 * excess
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_skewrank_63d_jerk_v074_signal(closeadj):
    sk = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    b = _rank(sk, 504)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_skewstress_jerk_v075_signal(closeadj):
    skew = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    cone = _f09_volcone(closeadj, 63, 504)
    b = skew * cone
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewvol_10_jerk_v076_signal(closeadj):
    b = _f09_ewvol(closeadj, 10)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewvol_42_jerk_v077_signal(closeadj):
    b = _f09_ewvol(closeadj, 42)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewgap_21_jerk_v078_signal(closeadj):
    b = _f09_ewvol(closeadj, 21) - _f09_rvol(closeadj, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewratio_jerk_v079_signal(closeadj):
    fast = _f09_ewvol(closeadj, 10)
    slow = _f09_ewvol(closeadj, 63)
    b = (fast - slow) / (fast + slow).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_madvol_21_jerk_v080_signal(closeadj):
    b = _f09_mad_vol(closeadj, 21)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_madstd_63_jerk_v081_signal(closeadj):
    mad = _f09_mad_vol(closeadj, 63)
    sd = _f09_rvol(closeadj, 63)
    # for a normal, mad/std ~ 0.8; deviations flag fat tails
    b = mad / sd.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_madslope_jerk_v082_signal(closeadj):
    vs = _f09_mad_vol(closeadj, 21)
    vl = _f09_mad_vol(closeadj, 126)
    b = (vs - vl) / (vs + vl).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcluster_63_jerk_v083_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2

    def _ac(a):
        a0 = a[1:]
        a1 = a[:-1]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return np.corrcoef(a0, a1)[0, 1]

    b = r2.rolling(63, min_periods=42).apply(_ac, raw=True)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcluster_126_jerk_v084_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2

    def _ac(a):
        a0 = a[1:]
        a1 = a[:-1]
        if a0.std() == 0 or a1.std() == 0:
            return np.nan
        return np.corrcoef(a0, a1)[0, 1]

    b = r2.rolling(126, min_periods=63).apply(_ac, raw=True)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_varratio_jerk_v085_signal(closeadj):
    r = _f09_logret(closeadj)
    v21 = r.rolling(21, min_periods=10).var()
    v63 = r.rolling(63, min_periods=21).var()
    # if returns were iid, var scales linearly; ratio of per-day variances reveals mean-reversion/trending
    b = v63 / v21.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_cone_252d_jerk_v086_signal(closeadj):
    b = _f09_volcone(closeadj, 252, 1260)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_cone_42d_jerk_v087_signal(closeadj):
    b = _f09_volcone(closeadj, 42, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_coneslope_jerk_v088_signal(closeadj):
    c_short = _f09_volcone(closeadj, 5, 126)
    c_long = _f09_volcone(closeadj, 126, 504)
    b = c_short - c_long
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_regslope5_jerk_v089_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
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
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_regfit_jerk_v090_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
    logw = np.log(np.array(ws, dtype=float))
    logw = logw - logw.mean()
    denom = float((logw ** 2).sum())
    vols = [np.log(_f09_rvol(closeadj, w).replace(0, np.nan)) for w in ws]
    mat = pd.concat(vols, axis=1)
    mat.columns = range(len(ws))
    centered = mat.sub(mat.mean(axis=1), axis=0)
    slope = (centered * logw).sum(axis=1) / denom
    fitted = pd.DataFrame({k: slope * logw[k] for k in range(len(ws))})
    ss_res = ((centered - fitted) ** 2).sum(axis=1)
    ss_tot = (centered ** 2).sum(axis=1).replace(0, np.nan)
    b = 1.0 - ss_res / ss_tot
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_5d_jerk_v091_signal(closeadj):
    b = _f09_voladjret(closeadj, 5)
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voladjret_42d_jerk_v092_signal(closeadj):
    b = _f09_voladjret(closeadj, 42)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sharpemom_63d_jerk_v093_signal(closeadj):
    sh = _f09_voladjret(closeadj, 63)
    b = sh - sh.shift(63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volrank_5d_jerk_v094_signal(closeadj):
    v = _f09_rvol(closeadj, 5)
    b = _rank(v, 252)
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = np.sign(_d) * _d.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volrank_126d_jerk_v095_signal(closeadj):
    v = _f09_rvol(closeadj, 126)
    b = _rank(v, 504)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upcone_126d_jerk_v096_signal(closeadj):
    uv = _f09_upvol(closeadj, 126)
    b = uv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downmom_21d_jerk_v097_signal(closeadj):
    dv = _f09_downvol(closeadj, 21)
    b = np.log(dv.replace(0, np.nan) / dv.shift(21).replace(0, np.nan))
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_upmom_63d_jerk_v098_signal(closeadj):
    uv = _f09_upvol(closeadj, 63)
    b = np.log(uv.replace(0, np.nan) / uv.shift(63).replace(0, np.nan))
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volskew_252d_jerk_v099_signal(closeadj):
    b = _f09_downvol(closeadj, 252) - _f09_upvol(closeadj, 252)
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_vovrank_jerk_v100_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    vov = v.pct_change().rolling(63, min_periods=21).std()
    b = _rank(vov, 252)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_vovmom_jerk_v101_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    vov = v.pct_change().rolling(63, min_periods=21).std()
    b = vov - vov.shift(63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_retskew_63d_jerk_v102_signal(closeadj):
    r = _f09_logret(closeadj)
    b = r.rolling(63, min_periods=21).skew()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_retkurt_126d_jerk_v103_signal(closeadj):
    r = _f09_logret(closeadj)
    b = r.rolling(126, min_periods=42).kurt()
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewcurv_jerk_v104_signal(closeadj):
    vs = np.log(_f09_ewvol(closeadj, 10).replace(0, np.nan))
    vm = np.log(_f09_ewvol(closeadj, 42).replace(0, np.nan))
    vl = np.log(_f09_ewvol(closeadj, 126).replace(0, np.nan))
    b = vs - 2.0 * vm + vl
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_jumpshare_21d_jerk_v105_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    mx = r2.rolling(21, min_periods=10).max()
    tot = r2.rolling(21, min_periods=10).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_jumpshare_63d_jerk_v106_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    mx = r2.rolling(63, min_periods=21).max()
    tot = r2.rolling(63, min_periods=21).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_contvol_share_jerk_v107_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    med = r2.rolling(63, min_periods=21).median()
    mean = r2.rolling(63, min_periods=21).mean()
    b = med / mean.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_bipower_jerk_v108_signal(closeadj):
    ar = _f09_logret(closeadj).abs()
    bipow = (ar * ar.shift(1)).rolling(63, min_periods=21).mean() * (np.pi / 2.0)
    rv = (_f09_logret(closeadj) ** 2).rolling(63, min_periods=21).mean()
    b = 1.0 - bipow / rv.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_conespr_21v252_jerk_v109_signal(closeadj):
    c1 = _f09_volcone(closeadj, 21, 252)
    c2 = _f09_volcone(closeadj, 252, 1260)
    b = c1 - c2
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_condsharpe_jerk_v110_signal(closeadj):
    sh = _f09_voladjret(closeadj, 63)
    slope_sign = np.sign(_f09_volslope(closeadj, 21, 252))
    b = sh * slope_sign
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_logdisp_jerk_v111_signal(closeadj):
    v1 = np.log(_f09_rvol(closeadj, 5).replace(0, np.nan))
    v2 = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    v3 = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    v4 = np.log(_f09_rvol(closeadj, 126).replace(0, np.nan))
    v5 = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    b = pd.concat([v1, v2, v3, v4, v5], axis=1).std(axis=1)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_termrange_jerk_v112_signal(closeadj):
    v1 = _f09_rvol(closeadj, 5)
    v2 = _f09_rvol(closeadj, 21)
    v3 = _f09_rvol(closeadj, 63)
    v4 = _f09_rvol(closeadj, 252)
    stacked = pd.concat([v1, v2, v3, v4], axis=1)
    b = (stacked.max(axis=1) - stacked.min(axis=1)) / stacked.mean(axis=1).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_geoarith_jerk_v113_signal(closeadj):
    ws = [5, 21, 63, 126, 252]
    vols = [_f09_rvol(closeadj, w) for w in ws]
    mat = pd.concat(vols, axis=1)
    mat.columns = range(len(ws))
    geo = np.exp(np.log(mat.replace(0, np.nan)).mean(axis=1))
    arith = mat.mean(axis=1).replace(0, np.nan)
    b = geo / arith - 1.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volmeanrev_jerk_v114_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    dev = v - v.rolling(252, min_periods=63).mean()
    fwd_chg = v.shift(-21) - v
    # rolling correlation of deviation with forward change (negative => mean-reverting)
    b = dev.rolling(252, min_periods=63).corr(fwd_chg)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewcone_jerk_v115_signal(closeadj):
    ev = _f09_ewvol(closeadj, 21)
    b = ev.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downcone_126d_jerk_v116_signal(closeadj):
    dv = _f09_downvol(closeadj, 126)
    b = dv.rolling(1260, min_periods=252).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(63) + result.shift(126)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_semitwist_jerk_v117_signal(closeadj):
    span = np.log(63.0) - np.log(5.0)
    dn = (np.log(_f09_downvol(closeadj, 63).replace(0, np.nan))
          - np.log(_f09_downvol(closeadj, 5).replace(0, np.nan))) / span
    up = (np.log(_f09_upvol(closeadj, 63).replace(0, np.nan))
          - np.log(_f09_upvol(closeadj, 5).replace(0, np.nan))) / span
    b = dn - up
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_curvmom_jerk_v118_signal(closeadj):
    vs = np.log(_f09_rvol(closeadj, 5).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, 42).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    curv = vs - 2.0 * vm + vl
    b = curv - curv.shift(63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_varratio5_jerk_v119_signal(closeadj):
    r1 = _f09_logret(closeadj)
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    var1 = r1.rolling(126, min_periods=42).var()
    var5 = r5.rolling(126, min_periods=42).var()
    b = var5 / (5.0 * var1).replace(0, np.nan) - 1.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volzlong_63d_jerk_v120_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = _z(v, 504)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_frontspike_jerk_v121_signal(closeadj):
    ratio = _f09_rvol(closeadj, 5) / _f09_rvol(closeadj, 252).replace(0, np.nan)
    b = ratio - ratio.shift(5)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_butterfly_jerk_v122_signal(closeadj):
    vs = _f09_rvol(closeadj, 21)
    vm = _f09_rvol(closeadj, 63)
    vl = _f09_rvol(closeadj, 252)
    b = vm - 0.5 * (vs + vl)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_ewconeslope_jerk_v123_signal(closeadj):
    ev_s = _f09_ewvol(closeadj, 10)
    ev_l = _f09_ewvol(closeadj, 63)
    c_s = ev_s.rolling(252, min_periods=63).rank(pct=True)
    c_l = ev_l.rolling(252, min_periods=63).rank(pct=True)
    b = c_s - c_l
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slowvov_jerk_v124_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = v.pct_change(21).rolling(252, min_periods=63).std()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_invfreq_jerk_v125_signal(closeadj):
    v5 = _f09_rvol(closeadj, 5)
    v63 = _f09_rvol(closeadj, 63)
    inv = (v5 > v63).astype(float)
    freq = inv.rolling(63, min_periods=21).mean() - 0.5
    mag = ((v5 - v63) / v63.replace(0, np.nan)).clip(lower=0).rolling(63, min_periods=21).mean()
    b = freq + mag
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_shortsortino_jerk_v126_signal(closeadj):
    r = _f09_logret(closeadj)
    cum = r.rolling(21, min_periods=10).sum()
    dv = _f09_downvol(closeadj, 21) / np.sqrt(252.0)
    b = cum / dv.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_sharpeterm_jerk_v127_signal(closeadj):
    b = _f09_voladjret(closeadj, 5) - _f09_voladjret(closeadj, 63)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_curvsign_jerk_v128_signal(closeadj):
    vs = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    curv = vs - 2.0 * vm + vl
    b = np.sign(curv).rolling(63, min_periods=21).mean()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_multidayvol_jerk_v129_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v5 = r5.rolling(63, min_periods=21).std()
    v1 = _f09_rvol_raw(closeadj, 63) * np.sqrt(5.0)
    b = v5 / v1.replace(0, np.nan) - 1.0
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_weeklyvolcone_jerk_v130_signal(closeadj):
    r5 = np.log(closeadj.replace(0, np.nan)).diff(5)
    v5 = r5.rolling(63, min_periods=21).std()
    b = v5.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_asymcone_jerk_v131_signal(closeadj):
    dc = _f09_downvol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    uc = _f09_upvol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    b = dc - uc
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slopexvov_jerk_v132_signal(closeadj):
    slope = _f09_volslope(closeadj, 21, 126)
    v = _f09_rvol(closeadj, 21)
    vov = v.pct_change().rolling(63, min_periods=21).std()
    b = slope * vov
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = np.sign(_d) * _d.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voltimetrend_jerk_v133_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    w = 126

    def _sl(a):
        m = len(a)
        t = np.arange(m, dtype=float)
        t = t - t.mean()
        denom = float((t ** 2).sum())
        if denom == 0:
            return np.nan
        a = a - a.mean()
        return float((a * t).sum()) / denom

    b = v.rolling(w, min_periods=63).apply(_sl, raw=True)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volcv_jerk_v134_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    sd = v.rolling(126, min_periods=42).std()
    mu = v.rolling(126, min_periods=42).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volpeakprox_jerk_v135_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    mx = v.rolling(252, min_periods=63).max()
    b = v / mx.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voltroughprox_jerk_v136_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    mn = v.rolling(252, min_periods=63).min()
    b = np.log(v.replace(0, np.nan) / mn.replace(0, np.nan))
    result = b
    _d = result - 2.0 * result.shift(5) + result.shift(10)
    b = _d.ewm(span=max(3, 5), min_periods=max(2, 5 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volrangepos_jerk_v137_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    mx = v.rolling(252, min_periods=63).max()
    mn = v.rolling(252, min_periods=63).min()
    b = (v - mn) / (mx - mn).replace(0, np.nan) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = np.sign(_d) * _d.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_skewtrend_jerk_v138_signal(closeadj):
    sk = _f09_downvol(closeadj, 63) - _f09_upvol(closeadj, 63)
    b = sk - sk.rolling(126, min_periods=42).mean()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_r2disp_jerk_v139_signal(closeadj):
    r2 = _f09_logret(closeadj) ** 2
    sd = r2.rolling(63, min_periods=21).std()
    mu = r2.rolling(63, min_periods=21).mean()
    b = sd / mu.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_recencystress_jerk_v140_signal(closeadj):
    fast = _f09_ewvol(closeadj, 5)
    slow = _f09_rvol(closeadj, 252)
    b = (fast - slow) / slow.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_slopevol_jerk_v141_signal(closeadj):
    sl = _f09_volslope(closeadj, 21, 252)
    b = sl.rolling(126, min_periods=42).std()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _z(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_longsortino_jerk_v142_signal(closeadj):
    r = _f09_logret(closeadj)
    cum = r.rolling(252, min_periods=63).sum()
    dv = _f09_downvol(closeadj, 252) / np.sqrt(252.0)
    b = cum / dv.replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_convrank_jerk_v143_signal(closeadj):
    vs = np.log(_f09_rvol(closeadj, 21).replace(0, np.nan))
    vm = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    vl = np.log(_f09_rvol(closeadj, 252).replace(0, np.nan))
    curv = vs - 2.0 * vm + vl
    b = curv.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = np.sign(_d) * _d.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_volaccel_63d_jerk_v144_signal(closeadj):
    lv = np.log(_f09_rvol(closeadj, 63).replace(0, np.nan))
    b = lv - 2.0 * lv.shift(63) + lv.shift(126)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_madconespr_jerk_v145_signal(closeadj):
    mc = _f09_mad_vol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    sc = _f09_rvol(closeadj, 63).rolling(504, min_periods=126).rank(pct=True)
    b = mc - sc
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_downweightvol_jerk_v146_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    share = _f09_downvol(closeadj, 63) / v.replace(0, np.nan)
    b = v * (share - 0.7071)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _rank(_d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_vovslope_jerk_v147_signal(closeadj):
    v = _f09_rvol(closeadj, 21)
    chg = v.pct_change()
    vov_s = chg.rolling(42, min_periods=21).std()
    vov_l = chg.rolling(126, min_periods=42).std()
    b = (vov_s - vov_l) / (vov_s + vov_l).replace(0, np.nan)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_voldispslow_jerk_v148_signal(closeadj):
    v = _f09_rvol(closeadj, 63)
    b = v - v.ewm(span=252, min_periods=63).mean()
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d.ewm(span=max(3, 21), min_periods=max(2, 21 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_termskew_jerk_v149_signal(closeadj):
    v1 = _f09_rvol(closeadj, 5)
    v2 = _f09_rvol(closeadj, 21)
    v3 = _f09_rvol(closeadj, 63)
    v4 = _f09_rvol(closeadj, 126)
    v5 = _f09_rvol(closeadj, 252)
    mat = pd.concat([v1, v2, v3, v4, v5], axis=1)
    mu = mat.mean(axis=1)
    sd = mat.std(axis=1).replace(0, np.nan)
    m3 = ((mat.sub(mu, axis=0)) ** 3).mean(axis=1)
    b = m3 / (sd ** 3)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f09vt_f09_volatility_term_structure_stresscomposite_jerk_v150_signal(closeadj):
    slope = _f09_volslope(closeadj, 5, 63)
    cone = _f09_volcone(closeadj, 21, 252)
    skew = _f09_downvol(closeadj, 21) - _f09_upvol(closeadj, 21)
    b = slope + cone + np.tanh(50.0 * skew)
    result = b
    _d = result - 2.0 * result.shift(21) + result.shift(42)
    b = _d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f09vt_f09_volatility_term_structure_rvol_5d_jerk_v001_signal,
    f09vt_f09_volatility_term_structure_rvol_21d_jerk_v002_signal,
    f09vt_f09_volatility_term_structure_rvol_63d_jerk_v003_signal,
    f09vt_f09_volatility_term_structure_rvol_126d_jerk_v004_signal,
    f09vt_f09_volatility_term_structure_rvol_252d_jerk_v005_signal,
    f09vt_f09_volatility_term_structure_volratio_21v63_jerk_v006_signal,
    f09vt_f09_volatility_term_structure_volratio_21v126_jerk_v007_signal,
    f09vt_f09_volatility_term_structure_volratiomom_21v252_jerk_v008_signal,
    f09vt_f09_volatility_term_structure_volratio_63v252_jerk_v009_signal,
    f09vt_f09_volatility_term_structure_volratio_5v21_jerk_v010_signal,
    f09vt_f09_volatility_term_structure_volslope_5v63_jerk_v011_signal,
    f09vt_f09_volatility_term_structure_upslope_21v126_jerk_v012_signal,
    f09vt_f09_volatility_term_structure_downslope_21v126_jerk_v013_signal,
    f09vt_f09_volatility_term_structure_volcurv_5_21_63_jerk_v014_signal,
    f09vt_f09_volatility_term_structure_volcurv_21_63_252_jerk_v015_signal,
    f09vt_f09_volatility_term_structure_volcurv_21_63_126_jerk_v016_signal,
    f09vt_f09_volatility_term_structure_volcone_21d_jerk_v017_signal,
    f09vt_f09_volatility_term_structure_volcone_63d_jerk_v018_signal,
    f09vt_f09_volatility_term_structure_volcone_126d_jerk_v019_signal,
    f09vt_f09_volatility_term_structure_volcone_5d_jerk_v020_signal,
    f09vt_f09_volatility_term_structure_downvol_21d_jerk_v021_signal,
    f09vt_f09_volatility_term_structure_downvol_63d_jerk_v022_signal,
    f09vt_f09_volatility_term_structure_upvol_63d_jerk_v023_signal,
    f09vt_f09_volatility_term_structure_volskew_21d_jerk_v024_signal,
    f09vt_f09_volatility_term_structure_volskew_63d_jerk_v025_signal,
    f09vt_f09_volatility_term_structure_volskewratiomom_63d_jerk_v026_signal,
    f09vt_f09_volatility_term_structure_volskewratio_126d_jerk_v027_signal,
    f09vt_f09_volatility_term_structure_voladjret_21d_jerk_v028_signal,
    f09vt_f09_volatility_term_structure_voladjret_63d_jerk_v029_signal,
    f09vt_f09_volatility_term_structure_voladjret_126d_jerk_v030_signal,
    f09vt_f09_volatility_term_structure_voladjret_252d_jerk_v031_signal,
    f09vt_f09_volatility_term_structure_rvolz_21d_jerk_v032_signal,
    f09vt_f09_volatility_term_structure_rvolz_63d_jerk_v033_signal,
    f09vt_f09_volatility_term_structure_rvolz_126d_jerk_v034_signal,
    f09vt_f09_volatility_term_structure_volratioz_63v126_jerk_v035_signal,
    f09vt_f09_volatility_term_structure_volratioz_5v63_jerk_v036_signal,
    f09vt_f09_volatility_term_structure_twist_jerk_v037_signal,
    f09vt_f09_volatility_term_structure_slopemom_5v63_jerk_v038_signal,
    f09vt_f09_volatility_term_structure_downratio_63v252_jerk_v039_signal,
    f09vt_f09_volatility_term_structure_upvolcone_63d_jerk_v040_signal,
    f09vt_f09_volatility_term_structure_conespread_21v126_jerk_v041_signal,
    f09vt_f09_volatility_term_structure_volofvol_63d_jerk_v042_signal,
    f09vt_f09_volatility_term_structure_volofvol_126d_jerk_v043_signal,
    f09vt_f09_volatility_term_structure_vovterm_jerk_v044_signal,
    f09vt_f09_volatility_term_structure_voldiff_63v126_jerk_v045_signal,
    f09vt_f09_volatility_term_structure_coneextreme_63d_jerk_v046_signal,
    f09vt_f09_volatility_term_structure_sharpespread_21v126_jerk_v047_signal,
    f09vt_f09_volatility_term_structure_sortino_252d_jerk_v048_signal,
    f09vt_f09_volatility_term_structure_sharperatio_spread_jerk_v049_signal,
    f09vt_f09_volatility_term_structure_voldispersion_jerk_v050_signal,
    f09vt_f09_volatility_term_structure_olsslope_jerk_v051_signal,
    f09vt_f09_volatility_term_structure_volpct_252d_jerk_v052_signal,
    f09vt_f09_volatility_term_structure_volmom_252d_jerk_v053_signal,
    f09vt_f09_volatility_term_structure_volaccel_21d_jerk_v054_signal,
    f09vt_f09_volatility_term_structure_asymratio_jerk_v055_signal,
    f09vt_f09_volatility_term_structure_conexslope_63d_jerk_v056_signal,
    f09vt_f09_volatility_term_structure_backwardation_jerk_v057_signal,
    f09vt_f09_volatility_term_structure_sharperank_63d_jerk_v058_signal,
    f09vt_f09_volatility_term_structure_slopeema_jerk_v059_signal,
    f09vt_f09_volatility_term_structure_ratiomom_21v126_jerk_v060_signal,
    f09vt_f09_volatility_term_structure_semisumgap_63d_jerk_v061_signal,
    f09vt_f09_volatility_term_structure_conemom_21d_jerk_v062_signal,
    f09vt_f09_volatility_term_structure_ratiomom_5v126_jerk_v063_signal,
    f09vt_f09_volatility_term_structure_curvz_jerk_v064_signal,
    f09vt_f09_volatility_term_structure_voldisp_21d_jerk_v065_signal,
    f09vt_f09_volatility_term_structure_downcone_63d_jerk_v066_signal,
    f09vt_f09_volatility_term_structure_slopesign_jerk_v067_signal,
    f09vt_f09_volatility_term_structure_regimesharpe_jerk_v068_signal,
    f09vt_f09_volatility_term_structure_downshare_spread_jerk_v069_signal,
    f09vt_f09_volatility_term_structure_downshare_cone_jerk_v070_signal,
    f09vt_f09_volatility_term_structure_conebroad_jerk_v071_signal,
    f09vt_f09_volatility_term_structure_convratio_jerk_v072_signal,
    f09vt_f09_volatility_term_structure_volhitrate_21d_jerk_v073_signal,
    f09vt_f09_volatility_term_structure_skewrank_63d_jerk_v074_signal,
    f09vt_f09_volatility_term_structure_skewstress_jerk_v075_signal,
    f09vt_f09_volatility_term_structure_ewvol_10_jerk_v076_signal,
    f09vt_f09_volatility_term_structure_ewvol_42_jerk_v077_signal,
    f09vt_f09_volatility_term_structure_ewgap_21_jerk_v078_signal,
    f09vt_f09_volatility_term_structure_ewratio_jerk_v079_signal,
    f09vt_f09_volatility_term_structure_madvol_21_jerk_v080_signal,
    f09vt_f09_volatility_term_structure_madstd_63_jerk_v081_signal,
    f09vt_f09_volatility_term_structure_madslope_jerk_v082_signal,
    f09vt_f09_volatility_term_structure_volcluster_63_jerk_v083_signal,
    f09vt_f09_volatility_term_structure_volcluster_126_jerk_v084_signal,
    f09vt_f09_volatility_term_structure_varratio_jerk_v085_signal,
    f09vt_f09_volatility_term_structure_cone_252d_jerk_v086_signal,
    f09vt_f09_volatility_term_structure_cone_42d_jerk_v087_signal,
    f09vt_f09_volatility_term_structure_coneslope_jerk_v088_signal,
    f09vt_f09_volatility_term_structure_regslope5_jerk_v089_signal,
    f09vt_f09_volatility_term_structure_regfit_jerk_v090_signal,
    f09vt_f09_volatility_term_structure_voladjret_5d_jerk_v091_signal,
    f09vt_f09_volatility_term_structure_voladjret_42d_jerk_v092_signal,
    f09vt_f09_volatility_term_structure_sharpemom_63d_jerk_v093_signal,
    f09vt_f09_volatility_term_structure_volrank_5d_jerk_v094_signal,
    f09vt_f09_volatility_term_structure_volrank_126d_jerk_v095_signal,
    f09vt_f09_volatility_term_structure_upcone_126d_jerk_v096_signal,
    f09vt_f09_volatility_term_structure_downmom_21d_jerk_v097_signal,
    f09vt_f09_volatility_term_structure_upmom_63d_jerk_v098_signal,
    f09vt_f09_volatility_term_structure_volskew_252d_jerk_v099_signal,
    f09vt_f09_volatility_term_structure_vovrank_jerk_v100_signal,
    f09vt_f09_volatility_term_structure_vovmom_jerk_v101_signal,
    f09vt_f09_volatility_term_structure_retskew_63d_jerk_v102_signal,
    f09vt_f09_volatility_term_structure_retkurt_126d_jerk_v103_signal,
    f09vt_f09_volatility_term_structure_ewcurv_jerk_v104_signal,
    f09vt_f09_volatility_term_structure_jumpshare_21d_jerk_v105_signal,
    f09vt_f09_volatility_term_structure_jumpshare_63d_jerk_v106_signal,
    f09vt_f09_volatility_term_structure_contvol_share_jerk_v107_signal,
    f09vt_f09_volatility_term_structure_bipower_jerk_v108_signal,
    f09vt_f09_volatility_term_structure_conespr_21v252_jerk_v109_signal,
    f09vt_f09_volatility_term_structure_condsharpe_jerk_v110_signal,
    f09vt_f09_volatility_term_structure_logdisp_jerk_v111_signal,
    f09vt_f09_volatility_term_structure_termrange_jerk_v112_signal,
    f09vt_f09_volatility_term_structure_geoarith_jerk_v113_signal,
    f09vt_f09_volatility_term_structure_volmeanrev_jerk_v114_signal,
    f09vt_f09_volatility_term_structure_ewcone_jerk_v115_signal,
    f09vt_f09_volatility_term_structure_downcone_126d_jerk_v116_signal,
    f09vt_f09_volatility_term_structure_semitwist_jerk_v117_signal,
    f09vt_f09_volatility_term_structure_curvmom_jerk_v118_signal,
    f09vt_f09_volatility_term_structure_varratio5_jerk_v119_signal,
    f09vt_f09_volatility_term_structure_volzlong_63d_jerk_v120_signal,
    f09vt_f09_volatility_term_structure_frontspike_jerk_v121_signal,
    f09vt_f09_volatility_term_structure_butterfly_jerk_v122_signal,
    f09vt_f09_volatility_term_structure_ewconeslope_jerk_v123_signal,
    f09vt_f09_volatility_term_structure_slowvov_jerk_v124_signal,
    f09vt_f09_volatility_term_structure_invfreq_jerk_v125_signal,
    f09vt_f09_volatility_term_structure_shortsortino_jerk_v126_signal,
    f09vt_f09_volatility_term_structure_sharpeterm_jerk_v127_signal,
    f09vt_f09_volatility_term_structure_curvsign_jerk_v128_signal,
    f09vt_f09_volatility_term_structure_multidayvol_jerk_v129_signal,
    f09vt_f09_volatility_term_structure_weeklyvolcone_jerk_v130_signal,
    f09vt_f09_volatility_term_structure_asymcone_jerk_v131_signal,
    f09vt_f09_volatility_term_structure_slopexvov_jerk_v132_signal,
    f09vt_f09_volatility_term_structure_voltimetrend_jerk_v133_signal,
    f09vt_f09_volatility_term_structure_volcv_jerk_v134_signal,
    f09vt_f09_volatility_term_structure_volpeakprox_jerk_v135_signal,
    f09vt_f09_volatility_term_structure_voltroughprox_jerk_v136_signal,
    f09vt_f09_volatility_term_structure_volrangepos_jerk_v137_signal,
    f09vt_f09_volatility_term_structure_skewtrend_jerk_v138_signal,
    f09vt_f09_volatility_term_structure_r2disp_jerk_v139_signal,
    f09vt_f09_volatility_term_structure_recencystress_jerk_v140_signal,
    f09vt_f09_volatility_term_structure_slopevol_jerk_v141_signal,
    f09vt_f09_volatility_term_structure_longsortino_jerk_v142_signal,
    f09vt_f09_volatility_term_structure_convrank_jerk_v143_signal,
    f09vt_f09_volatility_term_structure_volaccel_63d_jerk_v144_signal,
    f09vt_f09_volatility_term_structure_madconespr_jerk_v145_signal,
    f09vt_f09_volatility_term_structure_downweightvol_jerk_v146_signal,
    f09vt_f09_volatility_term_structure_vovslope_jerk_v147_signal,
    f09vt_f09_volatility_term_structure_voldispslow_jerk_v148_signal,
    f09vt_f09_volatility_term_structure_termskew_jerk_v149_signal,
    f09vt_f09_volatility_term_structure_stresscomposite_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_VOLATILITY_TERM_STRUCTURE_REGISTRY_3RD_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}
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
    print("OK f09_volatility_term_structure_3rd_derivatives_001_150_claude: %d features pass" % n_features)
