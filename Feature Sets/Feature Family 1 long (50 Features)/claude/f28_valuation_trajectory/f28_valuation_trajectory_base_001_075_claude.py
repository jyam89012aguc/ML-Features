import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f28_valuation_traj(multiple, w):
    base = _mean(multiple, w)
    return _diff(base, w) / base.abs().replace(0, np.nan).shift(w)


def _f28_pe_change(pe, w):
    return _diff(_mean(pe, w), w) / _mean(pe.abs(), w).replace(0, np.nan)


def _f28_multiple_zscore(multiple, w_short, w_long):
    return _z(_mean(multiple, w_short), w_long)


# 21d PE change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pechg_21d_base_v001_signal(pe, marketcap):
    result = _f28_pe_change(pe, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pechg_63d_base_v002_signal(pe, marketcap):
    result = _f28_pe_change(pe, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d PE change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pechg_126d_base_v003_signal(pe, marketcap):
    result = _f28_pe_change(pe, 126) * np.log(_mean(marketcap, 126).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pechg_252d_base_v004_signal(pe, marketcap):
    result = _f28_pe_change(pe, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pechg_504d_base_v005_signal(pe, marketcap):
    result = _f28_pe_change(pe, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PB change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pbchg_21d_base_v006_signal(pb, marketcap):
    result = _f28_pe_change(pb, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PB change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pbchg_63d_base_v007_signal(pb, marketcap):
    result = _f28_pe_change(pb, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PB change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pbchg_252d_base_v008_signal(pb, marketcap):
    result = _f28_pe_change(pb, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PB change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pbchg_504d_base_v009_signal(pb, marketcap):
    result = _f28_pe_change(pb, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PS change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pschg_21d_base_v010_signal(ps, marketcap):
    result = _f28_pe_change(ps, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PS change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pschg_63d_base_v011_signal(ps, marketcap):
    result = _f28_pe_change(ps, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PS change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pschg_252d_base_v012_signal(ps, marketcap):
    result = _f28_pe_change(ps, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PS change trajectory weighted by marketcap
def f28vt_f28_valuation_trajectory_pschg_504d_base_v013_signal(ps, marketcap):
    result = _f28_pe_change(ps, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d valuation trajectory PE
def f28vt_f28_valuation_trajectory_petraj_21d_base_v014_signal(pe, marketcap):
    result = _f28_valuation_traj(pe, 21) * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valuation trajectory PE
def f28vt_f28_valuation_trajectory_petraj_63d_base_v015_signal(pe, marketcap):
    result = _f28_valuation_traj(pe, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valuation trajectory PE
def f28vt_f28_valuation_trajectory_petraj_252d_base_v016_signal(pe, marketcap):
    result = _f28_valuation_traj(pe, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d valuation trajectory PE
def f28vt_f28_valuation_trajectory_petraj_504d_base_v017_signal(pe, marketcap):
    result = _f28_valuation_traj(pe, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valuation trajectory PB
def f28vt_f28_valuation_trajectory_pbtraj_63d_base_v018_signal(pb, marketcap):
    result = _f28_valuation_traj(pb, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valuation trajectory PB
def f28vt_f28_valuation_trajectory_pbtraj_252d_base_v019_signal(pb, marketcap):
    result = _f28_valuation_traj(pb, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d valuation trajectory PB
def f28vt_f28_valuation_trajectory_pbtraj_504d_base_v020_signal(pb, marketcap):
    result = _f28_valuation_traj(pb, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valuation trajectory PS
def f28vt_f28_valuation_trajectory_pstraj_63d_base_v021_signal(ps, marketcap):
    result = _f28_valuation_traj(ps, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valuation trajectory PS
def f28vt_f28_valuation_trajectory_pstraj_252d_base_v022_signal(ps, marketcap):
    result = _f28_valuation_traj(ps, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d valuation trajectory PS
def f28vt_f28_valuation_trajectory_pstraj_504d_base_v023_signal(ps, marketcap):
    result = _f28_valuation_traj(ps, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBITDA trajectory
def f28vt_f28_valuation_trajectory_evebitdatraj_63d_base_v024_signal(evebitda, marketcap):
    result = _f28_valuation_traj(evebitda, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA trajectory
def f28vt_f28_valuation_trajectory_evebitdatraj_252d_base_v025_signal(evebitda, marketcap):
    result = _f28_valuation_traj(evebitda, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV/EBITDA trajectory
def f28vt_f28_valuation_trajectory_evebitdatraj_504d_base_v026_signal(evebitda, marketcap):
    result = _f28_valuation_traj(evebitda, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBIT trajectory
def f28vt_f28_valuation_trajectory_evebittraj_63d_base_v027_signal(evebit, marketcap):
    result = _f28_valuation_traj(evebit, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBIT trajectory
def f28vt_f28_valuation_trajectory_evebittraj_252d_base_v028_signal(evebit, marketcap):
    result = _f28_valuation_traj(evebit, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV/EBIT trajectory
def f28vt_f28_valuation_trajectory_evebittraj_504d_base_v029_signal(evebit, marketcap):
    result = _f28_valuation_traj(evebit, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV change trajectory
def f28vt_f28_valuation_trajectory_evchg_63d_base_v030_signal(ev, marketcap):
    result = _f28_pe_change(ev, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV change trajectory
def f28vt_f28_valuation_trajectory_evchg_252d_base_v031_signal(ev, marketcap):
    result = _f28_pe_change(ev, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV change trajectory
def f28vt_f28_valuation_trajectory_evchg_504d_base_v032_signal(ev, marketcap):
    result = _f28_pe_change(ev, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap change trajectory
def f28vt_f28_valuation_trajectory_mcapchg_63d_base_v033_signal(marketcap):
    result = _f28_pe_change(marketcap, 63) * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap change trajectory
def f28vt_f28_valuation_trajectory_mcapchg_252d_base_v034_signal(marketcap):
    result = _f28_pe_change(marketcap, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap change trajectory
def f28vt_f28_valuation_trajectory_mcapchg_504d_base_v035_signal(marketcap):
    result = _f28_pe_change(marketcap, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PE z-score over 252d
def f28vt_f28_valuation_trajectory_pez_252d_base_v036_signal(pe, marketcap):
    result = _f28_multiple_zscore(pe, 21, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE z-score over 504d
def f28vt_f28_valuation_trajectory_pez_504d_base_v037_signal(pe, marketcap):
    result = _f28_multiple_zscore(pe, 63, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PB z-score over 252d
def f28vt_f28_valuation_trajectory_pbz_252d_base_v038_signal(pb, marketcap):
    result = _f28_multiple_zscore(pb, 21, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PB z-score over 504d
def f28vt_f28_valuation_trajectory_pbz_504d_base_v039_signal(pb, marketcap):
    result = _f28_multiple_zscore(pb, 63, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PS z-score over 252d
def f28vt_f28_valuation_trajectory_psz_252d_base_v040_signal(ps, marketcap):
    result = _f28_multiple_zscore(ps, 21, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PS z-score over 504d
def f28vt_f28_valuation_trajectory_psz_504d_base_v041_signal(ps, marketcap):
    result = _f28_multiple_zscore(ps, 63, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBITDA z-score 252d
def f28vt_f28_valuation_trajectory_evebitdaz_252d_base_v042_signal(evebitda, marketcap):
    result = _f28_multiple_zscore(evebitda, 21, 252) * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA z-score 504d
def f28vt_f28_valuation_trajectory_evebitdaz_504d_base_v043_signal(evebitda, marketcap):
    result = _f28_multiple_zscore(evebitda, 63, 504) * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-PE level
def f28vt_f28_valuation_trajectory_pelog_21d_base_v044_signal(pe, marketcap):
    base = np.log(_mean(pe, 21).abs().replace(0, np.nan))
    result = base * np.log(_mean(marketcap, 21).replace(0, np.nan).abs()) + _f28_pe_change(pe, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-PE level
def f28vt_f28_valuation_trajectory_pelog_63d_base_v045_signal(pe, marketcap):
    base = np.log(_mean(pe, 63).abs().replace(0, np.nan))
    result = base * np.log(_mean(marketcap, 63).replace(0, np.nan).abs()) + _f28_pe_change(pe, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-PE level
def f28vt_f28_valuation_trajectory_pelog_252d_base_v046_signal(pe, marketcap):
    base = np.log(_mean(pe, 252).abs().replace(0, np.nan))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d PE change trajectory
def f28vt_f28_valuation_trajectory_pechg_5d_base_v047_signal(pe, marketcap):
    result = _f28_pe_change(pe, 5) * np.log(_mean(marketcap, 5).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 10d PE change trajectory
def f28vt_f28_valuation_trajectory_pechg_10d_base_v048_signal(pe, marketcap):
    result = _f28_pe_change(pe, 10) * np.log(_mean(marketcap, 10).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 42d PE change trajectory
def f28vt_f28_valuation_trajectory_pechg_42d_base_v049_signal(pe, marketcap):
    result = _f28_pe_change(pe, 42) * np.log(_mean(marketcap, 42).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 189d PE change trajectory
def f28vt_f28_valuation_trajectory_pechg_189d_base_v050_signal(pe, marketcap):
    result = _f28_pe_change(pe, 189) * np.log(_mean(marketcap, 189).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 378d PE change trajectory
def f28vt_f28_valuation_trajectory_pechg_378d_base_v051_signal(pe, marketcap):
    result = _f28_pe_change(pe, 378) * np.log(_mean(marketcap, 378).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PE change squared (severity)
def f28vt_f28_valuation_trajectory_pechgsq_21d_base_v052_signal(pe, marketcap):
    g = _f28_pe_change(pe, 21)
    result = g * g.abs() * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE change squared
def f28vt_f28_valuation_trajectory_pechgsq_63d_base_v053_signal(pe, marketcap):
    g = _f28_pe_change(pe, 63)
    result = g * g.abs() * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE change squared
def f28vt_f28_valuation_trajectory_pechgsq_252d_base_v054_signal(pe, marketcap):
    g = _f28_pe_change(pe, 252)
    result = g * g.abs() * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE change squared
def f28vt_f28_valuation_trajectory_pechgsq_504d_base_v055_signal(pe, marketcap):
    g = _f28_pe_change(pe, 504)
    result = g * g.abs() * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA PE change
def f28vt_f28_valuation_trajectory_pechgema_21d_base_v056_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).ewm(span=21, adjust=False, min_periods=10).mean()
    result = base * np.log(_mean(marketcap, 21).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA PE change
def f28vt_f28_valuation_trajectory_pechgema_63d_base_v057_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63).ewm(span=63, adjust=False, min_periods=21).mean()
    result = base * np.log(_mean(marketcap, 63).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA PE change
def f28vt_f28_valuation_trajectory_pechgema_252d_base_v058_signal(pe, marketcap):
    base = _f28_pe_change(pe, 252).ewm(span=252, adjust=False, min_periods=63).mean()
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of months with PE rising (rolling sum)
def f28vt_f28_valuation_trajectory_pechgupcnt_252d_base_v059_signal(pe, marketcap):
    flag = (_f28_pe_change(pe, 21) > 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of quarters with PB rising
def f28vt_f28_valuation_trajectory_pbchgupcnt_504d_base_v060_signal(pb, marketcap):
    flag = (_f28_pe_change(pb, 63) > 0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of months with PS contracting
def f28vt_f28_valuation_trajectory_pschgdowncnt_252d_base_v061_signal(ps, marketcap):
    flag = (_f28_pe_change(ps, 21) < 0).astype(float)
    result = flag.rolling(252, min_periods=63).sum() * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of PE / PB trajectory
def f28vt_f28_valuation_trajectory_pevpb_252d_base_v062_signal(pe, pb, marketcap):
    base = _safe_div(_mean(pe, 252), _mean(pb, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of PE / PS trajectory
def f28vt_f28_valuation_trajectory_pevps_504d_base_v063_signal(pe, ps, marketcap):
    base = _safe_div(_mean(pe, 504), _mean(ps, 504))
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of EVEBITDA / PE trajectory
def f28vt_f28_valuation_trajectory_evbvspe_252d_base_v064_signal(evebitda, pe, marketcap):
    base = _safe_div(_mean(evebitda, 252), _mean(pe, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_valuation_traj(evebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE std × marketcap (vol of valuation)
def f28vt_f28_valuation_trajectory_pestd_252d_base_v065_signal(pe, marketcap):
    base = _std(_f28_pe_change(pe, 21), 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE std × marketcap
def f28vt_f28_valuation_trajectory_pestd_504d_base_v066_signal(pe, marketcap):
    base = _std(_f28_pe_change(pe, 63), 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PB std × marketcap
def f28vt_f28_valuation_trajectory_pbstd_252d_base_v067_signal(pb, marketcap):
    base = _std(_f28_pe_change(pb, 21), 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PS std × marketcap
def f28vt_f28_valuation_trajectory_psstd_504d_base_v068_signal(ps, marketcap):
    base = _std(_f28_pe_change(ps, 63), 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PE level × marketcap (compound size)
def f28vt_f28_valuation_trajectory_pelvl_21d_base_v069_signal(pe, marketcap):
    base = _mean(pe, 21)
    result = base * np.log(_mean(marketcap, 21).replace(0, np.nan).abs()) + _f28_pe_change(pe, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE level × marketcap
def f28vt_f28_valuation_trajectory_pelvl_252d_base_v070_signal(pe, marketcap):
    base = _mean(pe, 252)
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE level × marketcap
def f28vt_f28_valuation_trajectory_pelvl_504d_base_v071_signal(pe, marketcap):
    base = _mean(pe, 504)
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of PE current vs 252d mean PE
def f28vt_f28_valuation_trajectory_pevsmean_252d_base_v072_signal(pe, marketcap):
    base = _safe_div(pe, _mean(pe, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio of PE current vs 504d mean PE
def f28vt_f28_valuation_trajectory_pevsmean_504d_base_v073_signal(pe, marketcap):
    base = _safe_div(pe, _mean(pe, 504))
    result = base * np.log(_mean(marketcap, 504).replace(0, np.nan).abs()) + _f28_pe_change(pe, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of PB current vs 252d mean
def f28vt_f28_valuation_trajectory_pbvsmean_252d_base_v074_signal(pb, marketcap):
    base = _safe_div(pb, _mean(pb, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(pb, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of PS current vs 252d mean
def f28vt_f28_valuation_trajectory_psvsmean_252d_base_v075_signal(ps, marketcap):
    base = _safe_div(ps, _mean(ps, 252))
    result = base * np.log(_mean(marketcap, 252).replace(0, np.nan).abs()) + _f28_pe_change(ps, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28vt_f28_valuation_trajectory_pechg_21d_base_v001_signal,
    f28vt_f28_valuation_trajectory_pechg_63d_base_v002_signal,
    f28vt_f28_valuation_trajectory_pechg_126d_base_v003_signal,
    f28vt_f28_valuation_trajectory_pechg_252d_base_v004_signal,
    f28vt_f28_valuation_trajectory_pechg_504d_base_v005_signal,
    f28vt_f28_valuation_trajectory_pbchg_21d_base_v006_signal,
    f28vt_f28_valuation_trajectory_pbchg_63d_base_v007_signal,
    f28vt_f28_valuation_trajectory_pbchg_252d_base_v008_signal,
    f28vt_f28_valuation_trajectory_pbchg_504d_base_v009_signal,
    f28vt_f28_valuation_trajectory_pschg_21d_base_v010_signal,
    f28vt_f28_valuation_trajectory_pschg_63d_base_v011_signal,
    f28vt_f28_valuation_trajectory_pschg_252d_base_v012_signal,
    f28vt_f28_valuation_trajectory_pschg_504d_base_v013_signal,
    f28vt_f28_valuation_trajectory_petraj_21d_base_v014_signal,
    f28vt_f28_valuation_trajectory_petraj_63d_base_v015_signal,
    f28vt_f28_valuation_trajectory_petraj_252d_base_v016_signal,
    f28vt_f28_valuation_trajectory_petraj_504d_base_v017_signal,
    f28vt_f28_valuation_trajectory_pbtraj_63d_base_v018_signal,
    f28vt_f28_valuation_trajectory_pbtraj_252d_base_v019_signal,
    f28vt_f28_valuation_trajectory_pbtraj_504d_base_v020_signal,
    f28vt_f28_valuation_trajectory_pstraj_63d_base_v021_signal,
    f28vt_f28_valuation_trajectory_pstraj_252d_base_v022_signal,
    f28vt_f28_valuation_trajectory_pstraj_504d_base_v023_signal,
    f28vt_f28_valuation_trajectory_evebitdatraj_63d_base_v024_signal,
    f28vt_f28_valuation_trajectory_evebitdatraj_252d_base_v025_signal,
    f28vt_f28_valuation_trajectory_evebitdatraj_504d_base_v026_signal,
    f28vt_f28_valuation_trajectory_evebittraj_63d_base_v027_signal,
    f28vt_f28_valuation_trajectory_evebittraj_252d_base_v028_signal,
    f28vt_f28_valuation_trajectory_evebittraj_504d_base_v029_signal,
    f28vt_f28_valuation_trajectory_evchg_63d_base_v030_signal,
    f28vt_f28_valuation_trajectory_evchg_252d_base_v031_signal,
    f28vt_f28_valuation_trajectory_evchg_504d_base_v032_signal,
    f28vt_f28_valuation_trajectory_mcapchg_63d_base_v033_signal,
    f28vt_f28_valuation_trajectory_mcapchg_252d_base_v034_signal,
    f28vt_f28_valuation_trajectory_mcapchg_504d_base_v035_signal,
    f28vt_f28_valuation_trajectory_pez_252d_base_v036_signal,
    f28vt_f28_valuation_trajectory_pez_504d_base_v037_signal,
    f28vt_f28_valuation_trajectory_pbz_252d_base_v038_signal,
    f28vt_f28_valuation_trajectory_pbz_504d_base_v039_signal,
    f28vt_f28_valuation_trajectory_psz_252d_base_v040_signal,
    f28vt_f28_valuation_trajectory_psz_504d_base_v041_signal,
    f28vt_f28_valuation_trajectory_evebitdaz_252d_base_v042_signal,
    f28vt_f28_valuation_trajectory_evebitdaz_504d_base_v043_signal,
    f28vt_f28_valuation_trajectory_pelog_21d_base_v044_signal,
    f28vt_f28_valuation_trajectory_pelog_63d_base_v045_signal,
    f28vt_f28_valuation_trajectory_pelog_252d_base_v046_signal,
    f28vt_f28_valuation_trajectory_pechg_5d_base_v047_signal,
    f28vt_f28_valuation_trajectory_pechg_10d_base_v048_signal,
    f28vt_f28_valuation_trajectory_pechg_42d_base_v049_signal,
    f28vt_f28_valuation_trajectory_pechg_189d_base_v050_signal,
    f28vt_f28_valuation_trajectory_pechg_378d_base_v051_signal,
    f28vt_f28_valuation_trajectory_pechgsq_21d_base_v052_signal,
    f28vt_f28_valuation_trajectory_pechgsq_63d_base_v053_signal,
    f28vt_f28_valuation_trajectory_pechgsq_252d_base_v054_signal,
    f28vt_f28_valuation_trajectory_pechgsq_504d_base_v055_signal,
    f28vt_f28_valuation_trajectory_pechgema_21d_base_v056_signal,
    f28vt_f28_valuation_trajectory_pechgema_63d_base_v057_signal,
    f28vt_f28_valuation_trajectory_pechgema_252d_base_v058_signal,
    f28vt_f28_valuation_trajectory_pechgupcnt_252d_base_v059_signal,
    f28vt_f28_valuation_trajectory_pbchgupcnt_504d_base_v060_signal,
    f28vt_f28_valuation_trajectory_pschgdowncnt_252d_base_v061_signal,
    f28vt_f28_valuation_trajectory_pevpb_252d_base_v062_signal,
    f28vt_f28_valuation_trajectory_pevps_504d_base_v063_signal,
    f28vt_f28_valuation_trajectory_evbvspe_252d_base_v064_signal,
    f28vt_f28_valuation_trajectory_pestd_252d_base_v065_signal,
    f28vt_f28_valuation_trajectory_pestd_504d_base_v066_signal,
    f28vt_f28_valuation_trajectory_pbstd_252d_base_v067_signal,
    f28vt_f28_valuation_trajectory_psstd_504d_base_v068_signal,
    f28vt_f28_valuation_trajectory_pelvl_21d_base_v069_signal,
    f28vt_f28_valuation_trajectory_pelvl_252d_base_v070_signal,
    f28vt_f28_valuation_trajectory_pelvl_504d_base_v071_signal,
    f28vt_f28_valuation_trajectory_pevsmean_252d_base_v072_signal,
    f28vt_f28_valuation_trajectory_pevsmean_504d_base_v073_signal,
    f28vt_f28_valuation_trajectory_pbvsmean_252d_base_v074_signal,
    f28vt_f28_valuation_trajectory_psvsmean_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_VALUATION_TRAJECTORY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = pd.Series((marketcap + debt).values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {
        "closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit,
        "evebitda": evebitda, "pe": pe, "pb": pb, "ps": ps,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_valuation_traj", "_f28_pe_change", "_f28_multiple_zscore")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_valuation_trajectory_base_001_075_claude: {n_features} features pass")
