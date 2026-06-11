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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan).shift(w)


# ===== folder domain primitives =====
def _f28_valuation_traj(multiple, w):
    base = _mean(multiple, w)
    return _diff(base, w) / base.abs().replace(0, np.nan).shift(w)


def _f28_pe_change(pe, w):
    return _diff(_mean(pe, w), w) / _mean(pe.abs(), w).replace(0, np.nan)


def _f28_multiple_zscore(multiple, w_short, w_long):
    return _z(_mean(multiple, w_short), w_long)


def _ln_mcap(marketcap, w):
    return np.log(_mean(marketcap, w).replace(0, np.nan).abs())


# 5d slope of 21d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_21d_slope_v001_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_21d_slope_v002_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_63d_slope_v003_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_63d_slope_v004_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_63d_slope_v005_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_126d_slope_v006_signal(pe, marketcap):
    base = _f28_pe_change(pe, 126) * _ln_mcap(marketcap, 126)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_126d_slope_v007_signal(pe, marketcap):
    base = _f28_pe_change(pe, 126) * _ln_mcap(marketcap, 126)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_252d_slope_v008_signal(pe, marketcap):
    base = _f28_pe_change(pe, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_252d_slope_v009_signal(pe, marketcap):
    base = _f28_pe_change(pe, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_504d_slope_v010_signal(pe, marketcap):
    base = _f28_pe_change(pe, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d PE change × log mcap
def f28vt_f28_valuation_trajectory_pechg_504d_slope_v011_signal(pe, marketcap):
    base = _f28_pe_change(pe, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d PB change × log mcap
def f28vt_f28_valuation_trajectory_pbchg_21d_slope_v012_signal(pb, marketcap):
    base = _f28_pe_change(pb, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PB change × log mcap
def f28vt_f28_valuation_trajectory_pbchg_63d_slope_v013_signal(pb, marketcap):
    base = _f28_pe_change(pb, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PB change × log mcap
def f28vt_f28_valuation_trajectory_pbchg_252d_slope_v014_signal(pb, marketcap):
    base = _f28_pe_change(pb, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PB change × log mcap
def f28vt_f28_valuation_trajectory_pbchg_504d_slope_v015_signal(pb, marketcap):
    base = _f28_pe_change(pb, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d PS change × log mcap
def f28vt_f28_valuation_trajectory_pschg_21d_slope_v016_signal(ps, marketcap):
    base = _f28_pe_change(ps, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PS change × log mcap
def f28vt_f28_valuation_trajectory_pschg_63d_slope_v017_signal(ps, marketcap):
    base = _f28_pe_change(ps, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PS change × log mcap
def f28vt_f28_valuation_trajectory_pschg_252d_slope_v018_signal(ps, marketcap):
    base = _f28_pe_change(ps, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PS change × log mcap
def f28vt_f28_valuation_trajectory_pschg_504d_slope_v019_signal(ps, marketcap):
    base = _f28_pe_change(ps, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d PE traj × log mcap
def f28vt_f28_valuation_trajectory_petraj_21d_slope_v020_signal(pe, marketcap):
    base = _f28_valuation_traj(pe, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PE traj × log mcap
def f28vt_f28_valuation_trajectory_petraj_63d_slope_v021_signal(pe, marketcap):
    base = _f28_valuation_traj(pe, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PE traj × log mcap
def f28vt_f28_valuation_trajectory_petraj_252d_slope_v022_signal(pe, marketcap):
    base = _f28_valuation_traj(pe, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PE traj × log mcap
def f28vt_f28_valuation_trajectory_petraj_504d_slope_v023_signal(pe, marketcap):
    base = _f28_valuation_traj(pe, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PB traj × log mcap
def f28vt_f28_valuation_trajectory_pbtraj_63d_slope_v024_signal(pb, marketcap):
    base = _f28_valuation_traj(pb, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PB traj × log mcap
def f28vt_f28_valuation_trajectory_pbtraj_252d_slope_v025_signal(pb, marketcap):
    base = _f28_valuation_traj(pb, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PB traj × log mcap
def f28vt_f28_valuation_trajectory_pbtraj_504d_slope_v026_signal(pb, marketcap):
    base = _f28_valuation_traj(pb, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PS traj × log mcap
def f28vt_f28_valuation_trajectory_pstraj_63d_slope_v027_signal(ps, marketcap):
    base = _f28_valuation_traj(ps, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PS traj × log mcap
def f28vt_f28_valuation_trajectory_pstraj_252d_slope_v028_signal(ps, marketcap):
    base = _f28_valuation_traj(ps, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PS traj × log mcap
def f28vt_f28_valuation_trajectory_pstraj_504d_slope_v029_signal(ps, marketcap):
    base = _f28_valuation_traj(ps, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EV/EBITDA traj × log mcap
def f28vt_f28_valuation_trajectory_evebitdatraj_63d_slope_v030_signal(evebitda, marketcap):
    base = _f28_valuation_traj(evebitda, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EV/EBITDA traj × log mcap
def f28vt_f28_valuation_trajectory_evebitdatraj_252d_slope_v031_signal(evebitda, marketcap):
    base = _f28_valuation_traj(evebitda, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EV/EBITDA traj × log mcap
def f28vt_f28_valuation_trajectory_evebitdatraj_504d_slope_v032_signal(evebitda, marketcap):
    base = _f28_valuation_traj(evebitda, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EV/EBIT traj × log mcap
def f28vt_f28_valuation_trajectory_evebittraj_63d_slope_v033_signal(evebit, marketcap):
    base = _f28_valuation_traj(evebit, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EV/EBIT traj × log mcap
def f28vt_f28_valuation_trajectory_evebittraj_252d_slope_v034_signal(evebit, marketcap):
    base = _f28_valuation_traj(evebit, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EV/EBIT traj × log mcap
def f28vt_f28_valuation_trajectory_evebittraj_504d_slope_v035_signal(evebit, marketcap):
    base = _f28_valuation_traj(evebit, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EV change × log mcap
def f28vt_f28_valuation_trajectory_evchg_63d_slope_v036_signal(ev, marketcap):
    base = _f28_pe_change(ev, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EV change × log mcap
def f28vt_f28_valuation_trajectory_evchg_252d_slope_v037_signal(ev, marketcap):
    base = _f28_pe_change(ev, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EV change × log mcap
def f28vt_f28_valuation_trajectory_evchg_504d_slope_v038_signal(ev, marketcap):
    base = _f28_pe_change(ev, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d marketcap change × log mcap
def f28vt_f28_valuation_trajectory_mcapchg_63d_slope_v039_signal(marketcap):
    base = _f28_pe_change(marketcap, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d marketcap change × log mcap
def f28vt_f28_valuation_trajectory_mcapchg_252d_slope_v040_signal(marketcap):
    base = _f28_pe_change(marketcap, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d marketcap change × log mcap
def f28vt_f28_valuation_trajectory_mcapchg_504d_slope_v041_signal(marketcap):
    base = _f28_pe_change(marketcap, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PE z × log mcap
def f28vt_f28_valuation_trajectory_pez_252d_slope_v042_signal(pe, marketcap):
    base = _f28_multiple_zscore(pe, 21, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PE z × log mcap
def f28vt_f28_valuation_trajectory_pez_504d_slope_v043_signal(pe, marketcap):
    base = _f28_multiple_zscore(pe, 63, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PB z × log mcap
def f28vt_f28_valuation_trajectory_pbz_252d_slope_v044_signal(pb, marketcap):
    base = _f28_multiple_zscore(pb, 21, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PB z × log mcap
def f28vt_f28_valuation_trajectory_pbz_504d_slope_v045_signal(pb, marketcap):
    base = _f28_multiple_zscore(pb, 63, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PS z × log mcap
def f28vt_f28_valuation_trajectory_psz_252d_slope_v046_signal(ps, marketcap):
    base = _f28_multiple_zscore(ps, 21, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PS z × log mcap
def f28vt_f28_valuation_trajectory_psz_504d_slope_v047_signal(ps, marketcap):
    base = _f28_multiple_zscore(ps, 63, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EV/EBITDA z × log mcap
def f28vt_f28_valuation_trajectory_evebitdaz_252d_slope_v048_signal(evebitda, marketcap):
    base = _f28_multiple_zscore(evebitda, 21, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d EV/EBITDA z × log mcap
def f28vt_f28_valuation_trajectory_evebitdaz_504d_slope_v049_signal(evebitda, marketcap):
    base = _f28_multiple_zscore(evebitda, 63, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log-PE × log mcap
def f28vt_f28_valuation_trajectory_pelog_21d_slope_v050_signal(pe, marketcap):
    base = np.log(_mean(pe, 21).abs().replace(0, np.nan)) * _ln_mcap(marketcap, 21) + _f28_pe_change(pe, 21) * 0.0
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log-PE × log mcap
def f28vt_f28_valuation_trajectory_pelog_63d_slope_v051_signal(pe, marketcap):
    base = np.log(_mean(pe, 63).abs().replace(0, np.nan)) * _ln_mcap(marketcap, 63) + _f28_pe_change(pe, 63) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log-PE × log mcap
def f28vt_f28_valuation_trajectory_pelog_252d_slope_v052_signal(pe, marketcap):
    base = np.log(_mean(pe, 252).abs().replace(0, np.nan)) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 5d PE chg
def f28vt_f28_valuation_trajectory_pechg_5d_slope_v053_signal(pe, marketcap):
    base = _f28_pe_change(pe, 5) * _ln_mcap(marketcap, 5)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 10d PE chg
def f28vt_f28_valuation_trajectory_pechg_10d_slope_v054_signal(pe, marketcap):
    base = _f28_pe_change(pe, 10) * _ln_mcap(marketcap, 10)
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 42d PE chg
def f28vt_f28_valuation_trajectory_pechg_42d_slope_v055_signal(pe, marketcap):
    base = _f28_pe_change(pe, 42) * _ln_mcap(marketcap, 42)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 189d PE chg
def f28vt_f28_valuation_trajectory_pechg_189d_slope_v056_signal(pe, marketcap):
    base = _f28_pe_change(pe, 189) * _ln_mcap(marketcap, 189)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 378d PE chg
def f28vt_f28_valuation_trajectory_pechg_378d_slope_v057_signal(pe, marketcap):
    base = _f28_pe_change(pe, 378) * _ln_mcap(marketcap, 378)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d PE chg sq
def f28vt_f28_valuation_trajectory_pechgsq_21d_slope_v058_signal(pe, marketcap):
    g = _f28_pe_change(pe, 21)
    base = g * g.abs() * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d PE chg sq
def f28vt_f28_valuation_trajectory_pechgsq_63d_slope_v059_signal(pe, marketcap):
    g = _f28_pe_change(pe, 63)
    base = g * g.abs() * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d PE chg sq
def f28vt_f28_valuation_trajectory_pechgsq_252d_slope_v060_signal(pe, marketcap):
    g = _f28_pe_change(pe, 252)
    base = g * g.abs() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d PE chg sq
def f28vt_f28_valuation_trajectory_pechgsq_504d_slope_v061_signal(pe, marketcap):
    g = _f28_pe_change(pe, 504)
    base = g * g.abs() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA PE chg 21d × log mcap
def f28vt_f28_valuation_trajectory_pechgema_21d_slope_v062_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).ewm(span=21, adjust=False, min_periods=10).mean() * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EMA PE chg 63d × log mcap
def f28vt_f28_valuation_trajectory_pechgema_63d_slope_v063_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63).ewm(span=63, adjust=False, min_periods=21).mean() * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EMA PE chg 252d × log mcap
def f28vt_f28_valuation_trajectory_pechgema_252d_slope_v064_signal(pe, marketcap):
    base = _f28_pe_change(pe, 252).ewm(span=252, adjust=False, min_periods=63).mean() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE upcount 252d × log mcap
def f28vt_f28_valuation_trajectory_pechgupcnt_252d_slope_v065_signal(pe, marketcap):
    flag = (_f28_pe_change(pe, 21) > 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PB upcount 504d × log mcap
def f28vt_f28_valuation_trajectory_pbchgupcnt_504d_slope_v066_signal(pb, marketcap):
    flag = (_f28_pe_change(pb, 63) > 0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PS downcount 252d × log mcap
def f28vt_f28_valuation_trajectory_pschgdowncnt_252d_slope_v067_signal(ps, marketcap):
    flag = (_f28_pe_change(ps, 21) < 0).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE/PB ratio 252d × log mcap
def f28vt_f28_valuation_trajectory_pevpb_252d_slope_v068_signal(pe, pb, marketcap):
    base = _safe_div(_mean(pe, 252), _mean(pb, 252)) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE/PS ratio 504d × log mcap
def f28vt_f28_valuation_trajectory_pevps_504d_slope_v069_signal(pe, ps, marketcap):
    base = _safe_div(_mean(pe, 504), _mean(ps, 504)) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evebitda/pe 252d × log mcap
def f28vt_f28_valuation_trajectory_evbvspe_252d_slope_v070_signal(evebitda, pe, marketcap):
    base = _safe_div(_mean(evebitda, 252), _mean(pe, 252)) * _ln_mcap(marketcap, 252) + _f28_valuation_traj(evebitda, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE std 252d × log mcap
def f28vt_f28_valuation_trajectory_pestd_252d_slope_v071_signal(pe, marketcap):
    base = _std(_f28_pe_change(pe, 21), 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE std 504d × log mcap
def f28vt_f28_valuation_trajectory_pestd_504d_slope_v072_signal(pe, marketcap):
    base = _std(_f28_pe_change(pe, 63), 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PB std 252d × log mcap
def f28vt_f28_valuation_trajectory_pbstd_252d_slope_v073_signal(pb, marketcap):
    base = _std(_f28_pe_change(pb, 21), 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PS std 504d × log mcap
def f28vt_f28_valuation_trajectory_psstd_504d_slope_v074_signal(ps, marketcap):
    base = _std(_f28_pe_change(ps, 63), 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of PE level × log mcap 21d
def f28vt_f28_valuation_trajectory_pelvl_21d_slope_v075_signal(pe, marketcap):
    base = _mean(pe, 21) * _ln_mcap(marketcap, 21) + _f28_pe_change(pe, 21) * 0.0
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE level × log mcap 252d
def f28vt_f28_valuation_trajectory_pelvl_252d_slope_v076_signal(pe, marketcap):
    base = _mean(pe, 252) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE level × log mcap 504d
def f28vt_f28_valuation_trajectory_pelvl_504d_slope_v077_signal(pe, marketcap):
    base = _mean(pe, 504) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE vs mean 252d × log mcap
def f28vt_f28_valuation_trajectory_pevsmean_252d_slope_v078_signal(pe, marketcap):
    base = _safe_div(pe, _mean(pe, 252)) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE vs mean 504d × log mcap
def f28vt_f28_valuation_trajectory_pevsmean_504d_slope_v079_signal(pe, marketcap):
    base = _safe_div(pe, _mean(pe, 504)) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PB vs mean 252d × log mcap
def f28vt_f28_valuation_trajectory_pbvsmean_252d_slope_v080_signal(pb, marketcap):
    base = _safe_div(pb, _mean(pb, 252)) * _ln_mcap(marketcap, 252) + _f28_pe_change(pb, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PS vs mean 252d × log mcap
def f28vt_f28_valuation_trajectory_psvsmean_252d_slope_v081_signal(ps, marketcap):
    base = _safe_div(ps, _mean(ps, 252)) * _ln_mcap(marketcap, 252) + _f28_pe_change(ps, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EVEBIT vs mean 504d × log mcap
def f28vt_f28_valuation_trajectory_evebitvsmean_504d_slope_v082_signal(evebit, marketcap):
    base = _safe_div(evebit, _mean(evebit, 504)) * _ln_mcap(marketcap, 504) + _f28_valuation_traj(evebit, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBITDA vs mean 252d × log mcap
def f28vt_f28_valuation_trajectory_evebitdavsmean_252d_slope_v083_signal(evebitda, marketcap):
    base = _safe_div(evebitda, _mean(evebitda, 252)) * _ln_mcap(marketcap, 252) + _f28_valuation_traj(evebitda, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mcap z 504d
def f28vt_f28_valuation_trajectory_mcapz_504d_slope_v084_signal(marketcap):
    base = _f28_multiple_zscore(marketcap, 63, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mcap z 252d
def f28vt_f28_valuation_trajectory_mcapz_252d_slope_v085_signal(marketcap):
    base = _f28_multiple_zscore(marketcap, 21, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EV z 252d × log mcap
def f28vt_f28_valuation_trajectory_evz_252d_slope_v086_signal(ev, marketcap):
    base = _f28_multiple_zscore(ev, 21, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EV z 504d × log mcap
def f28vt_f28_valuation_trajectory_evz_504d_slope_v087_signal(ev, marketcap):
    base = _f28_multiple_zscore(ev, 63, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of PE chg abs 21d × log mcap
def f28vt_f28_valuation_trajectory_pechgabs_21d_slope_v088_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).abs() * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE chg abs 252d × log mcap
def f28vt_f28_valuation_trajectory_pechgabs_252d_slope_v089_signal(pe, marketcap):
    base = _f28_pe_change(pe, 252).abs() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE chg abs 504d × log mcap
def f28vt_f28_valuation_trajectory_pechgabs_504d_slope_v090_signal(pe, marketcap):
    base = _f28_pe_change(pe, 504).abs() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PB chg abs 252d × log mcap
def f28vt_f28_valuation_trajectory_pbchgabs_252d_slope_v091_signal(pb, marketcap):
    base = _f28_pe_change(pb, 252).abs() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PS chg abs 252d × log mcap
def f28vt_f28_valuation_trajectory_pschgabs_252d_slope_v092_signal(ps, marketcap):
    base = _f28_pe_change(ps, 252).abs() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE CV 252d × log mcap
def f28vt_f28_valuation_trajectory_pecv_252d_slope_v093_signal(pe, marketcap):
    base = _safe_div(_std(pe, 252), _mean(pe.abs(), 252)) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE CV 504d × log mcap
def f28vt_f28_valuation_trajectory_pecv_504d_slope_v094_signal(pe, marketcap):
    base = _safe_div(_std(pe, 504), _mean(pe.abs(), 504)) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBITDA CV 252d × log mcap
def f28vt_f28_valuation_trajectory_evebitdacv_252d_slope_v095_signal(evebitda, marketcap):
    base = _safe_div(_std(evebitda, 252), _mean(evebitda.abs(), 252)) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of PE chg ratio 21v63 × log mcap
def f28vt_f28_valuation_trajectory_pechgratio_21v63_slope_v096_signal(pe, marketcap):
    sg = _f28_pe_change(pe, 21)
    lg = _f28_pe_change(pe, 63).replace(0, np.nan)
    base = (sg / lg) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of PE chg ratio 63v252 × log mcap
def f28vt_f28_valuation_trajectory_pechgratio_63v252_slope_v097_signal(pe, marketcap):
    sg = _f28_pe_change(pe, 63)
    lg = _f28_pe_change(pe, 252).replace(0, np.nan)
    base = (sg / lg) * _ln_mcap(marketcap, 252)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of pe chg×mom 21d × log mcap
def f28vt_f28_valuation_trajectory_pechgxmom_21d_slope_v098_signal(pe, marketcap):
    mom = marketcap.pct_change(21)
    base = _f28_pe_change(pe, 21) * (1.0 + mom) * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pe chg×mom 63d × log mcap
def f28vt_f28_valuation_trajectory_pechgxmom_63d_slope_v099_signal(pe, marketcap):
    mom = marketcap.pct_change(63)
    base = _f28_pe_change(pe, 63) * (1.0 + mom) * _ln_mcap(marketcap, 63)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pe chg×mom 252d × log mcap
def f28vt_f28_valuation_trajectory_pechgxmom_252d_slope_v100_signal(pe, marketcap):
    mom = marketcap.pct_change(252)
    base = _f28_pe_change(pe, 252) * (1.0 + mom) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE accel 252 × log mcap
def f28vt_f28_valuation_trajectory_peaccel_252d_slope_v101_signal(pe, marketcap):
    g = _f28_pe_change(pe, 63)
    base = _diff(g, 63) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE accel 504 × log mcap
def f28vt_f28_valuation_trajectory_peaccel_504d_slope_v102_signal(pe, marketcap):
    g = _f28_pe_change(pe, 252)
    base = _diff(g, 252) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE area 252d × log mcap
def f28vt_f28_valuation_trajectory_pearea_252d_slope_v103_signal(pe, marketcap):
    base = (pe - _mean(pe, 252)).rolling(252, min_periods=63).sum() * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE area 504d × log mcap
def f28vt_f28_valuation_trajectory_pearea_504d_slope_v104_signal(pe, marketcap):
    base = (pe - _mean(pe, 504)).rolling(504, min_periods=126).sum() * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE chg skew 252d × log mcap
def f28vt_f28_valuation_trajectory_pechgskew_252d_slope_v105_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).rolling(252, min_periods=63).skew() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE chg skew 504d × log mcap
def f28vt_f28_valuation_trajectory_pechgskew_504d_slope_v106_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63).rolling(504, min_periods=126).skew() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE chg kurt 252d × log mcap
def f28vt_f28_valuation_trajectory_pechgkurt_252d_slope_v107_signal(pe, marketcap):
    base = _f28_pe_change(pe, 21).rolling(252, min_periods=63).kurt() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE chg kurt 504d × log mcap
def f28vt_f28_valuation_trajectory_pechgkurt_504d_slope_v108_signal(pe, marketcap):
    base = _f28_pe_change(pe, 63).rolling(504, min_periods=126).kurt() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite 252d × log mcap
def f28vt_f28_valuation_trajectory_composite_252d_slope_v109_signal(pe, pb, ps, marketcap):
    base = (_f28_pe_change(pe, 252) + _f28_pe_change(pb, 252) + _f28_pe_change(ps, 252)) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of composite 504d × log mcap
def f28vt_f28_valuation_trajectory_composite_504d_slope_v110_signal(pe, pb, ps, marketcap):
    base = (_f28_pe_change(pe, 504) + _f28_pe_change(pb, 504) + _f28_pe_change(ps, 504)) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of evtraj×mcap 252d
def f28vt_f28_valuation_trajectory_evtrajxmcap_252d_slope_v111_signal(ev, marketcap):
    base = _f28_valuation_traj(ev, 252) * _ln_mcap(marketcap, 252) ** 2.0 / 100.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mcaptraj×mcap 504d
def f28vt_f28_valuation_trajectory_mcaptrajxmcap_504d_slope_v112_signal(marketcap):
    base = _f28_valuation_traj(marketcap, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pe×pb 252d × log mcap
def f28vt_f28_valuation_trajectory_pexpb_252d_slope_v113_signal(pe, pb, marketcap):
    base = _mean(pe, 252) * _mean(pb, 252) * _ln_mcap(marketcap, 252) / 100.0 + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of pe×ps 504d × log mcap
def f28vt_f28_valuation_trajectory_pexps_504d_slope_v114_signal(pe, ps, marketcap):
    base = _mean(pe, 504) * _mean(ps, 504) * _ln_mcap(marketcap, 504) / 100.0 + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of pelvl×mcap 21d
def f28vt_f28_valuation_trajectory_pelvlxmcap_21d_slope_v115_signal(pe, marketcap):
    base = _mean(pe, 21) * _ln_mcap(marketcap, 21) + _f28_pe_change(pe, 21) * 0.0
    result = _slope(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pelvl×mcap 252d
def f28vt_f28_valuation_trajectory_pelvlxmcap_252d_slope_v116_signal(pe, marketcap):
    base = _mean(pe, 252) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of pelvl×mcap 504d
def f28vt_f28_valuation_trajectory_pelvlxmcap_504d_slope_v117_signal(pe, marketcap):
    base = _mean(pe, 504) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE diff 504 × log mcap
def f28vt_f28_valuation_trajectory_pediff_504_slope_v118_signal(pe, marketcap):
    base = (pe - _mean(pe, 504)) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PB diff 504 × log mcap
def f28vt_f28_valuation_trajectory_pbdiff_504_slope_v119_signal(pb, marketcap):
    base = (pb - _mean(pb, 504)) * _ln_mcap(marketcap, 504) + _f28_pe_change(pb, 504) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PS diff 504 × log mcap
def f28vt_f28_valuation_trajectory_psdiff_504_slope_v120_signal(ps, marketcap):
    base = (ps - _mean(ps, 504)) * _ln_mcap(marketcap, 504) + _f28_pe_change(ps, 504) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBIT diff 504 × log mcap
def f28vt_f28_valuation_trajectory_evebitdiff_504_slope_v121_signal(evebit, marketcap):
    base = (evebit - _mean(evebit, 504)) * _ln_mcap(marketcap, 504) + _f28_valuation_traj(evebit, 504) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBITDA diff 504 × log mcap
def f28vt_f28_valuation_trajectory_evebitdadiff_504_slope_v122_signal(evebitda, marketcap):
    base = (evebitda - _mean(evebitda, 504)) * _ln_mcap(marketcap, 504) + _f28_valuation_traj(evebitda, 504) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pevsmin 252d × log mcap
def f28vt_f28_valuation_trajectory_pevsmin_252d_slope_v123_signal(pe, marketcap):
    base = pe / _mean(pe, 252).replace(0, np.nan) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE sum 504d × log mcap
def f28vt_f28_valuation_trajectory_pesum_504d_slope_v124_signal(pe, marketcap):
    base = pe.rolling(504, min_periods=126).sum() / 504.0 * _ln_mcap(marketcap, 504) + _f28_valuation_traj(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE sum 252d × log mcap
def f28vt_f28_valuation_trajectory_pesum_252d_slope_v125_signal(pe, marketcap):
    base = pe.rolling(252, min_periods=63).sum() / 252.0 * _ln_mcap(marketcap, 252) + _f28_valuation_traj(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBITDA sum 252d × log mcap
def f28vt_f28_valuation_trajectory_evebitdasum_252d_slope_v126_signal(evebitda, marketcap):
    base = evebitda.rolling(252, min_periods=63).sum() / 252.0 * _ln_mcap(marketcap, 252) + _f28_valuation_traj(evebitda, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of pe sign sum 252d × log mcap
def f28vt_f28_valuation_trajectory_pesignsum_252d_slope_v127_signal(pe, marketcap):
    g = _f28_pe_change(pe, 21)
    sign = np.sign(g).fillna(0)
    base = sign.rolling(252, min_periods=63).sum() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of pe sign sum 504d × log mcap
def f28vt_f28_valuation_trajectory_pesignsum_504d_slope_v128_signal(pe, marketcap):
    g = _f28_pe_change(pe, 63)
    sign = np.sign(g).fillna(0)
    base = sign.rolling(504, min_periods=126).sum() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EV×mcap 252d
def f28vt_f28_valuation_trajectory_evxmcap_252d_slope_v129_signal(ev, marketcap):
    base = _f28_pe_change(ev, 252) * _ln_mcap(marketcap, 252) ** 2.0 / 100.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EV×mcap 504d
def f28vt_f28_valuation_trajectory_evxmcap_504d_slope_v130_signal(ev, marketcap):
    base = _f28_pe_change(ev, 504) * _ln_mcap(marketcap, 504) ** 2.0 / 100.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBITDA cum chg 252d × log mcap
def f28vt_f28_valuation_trajectory_evebitdacumchg_252d_slope_v131_signal(evebitda, marketcap):
    g = _f28_pe_change(evebitda, 21)
    base = g.rolling(252, min_periods=63).sum() * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EVEBITDA cum chg 504d × log mcap
def f28vt_f28_valuation_trajectory_evebitdacumchg_504d_slope_v132_signal(evebitda, marketcap):
    g = _f28_pe_change(evebitda, 63)
    base = g.rolling(504, min_periods=126).sum() * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of mcap vol 21d × log mcap
def f28vt_f28_valuation_trajectory_mcapvol_21d_slope_v133_signal(marketcap):
    base = _std(marketcap.pct_change(), 21) * _ln_mcap(marketcap, 21) + _f28_pe_change(marketcap, 21) * 0.0
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mcap vol 252d × log mcap
def f28vt_f28_valuation_trajectory_mcapvol_252d_slope_v134_signal(marketcap):
    base = _std(marketcap.pct_change(), 252) * _ln_mcap(marketcap, 252) + _f28_pe_change(marketcap, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EV vol 504d × log mcap
def f28vt_f28_valuation_trajectory_evvol_504d_slope_v135_signal(ev, marketcap):
    base = _std(ev.pct_change(), 504) * _ln_mcap(marketcap, 504) + _f28_pe_change(ev, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EVEBIT chg 21d × log mcap
def f28vt_f28_valuation_trajectory_evebitchg_21d_slope_v136_signal(evebit, marketcap):
    base = _f28_pe_change(evebit, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EVEBIT chg 63d × log mcap
def f28vt_f28_valuation_trajectory_evebitchg_63d_slope_v137_signal(evebit, marketcap):
    base = _f28_pe_change(evebit, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EVEBITDA chg 21d × log mcap
def f28vt_f28_valuation_trajectory_evebitdachg_21d_slope_v138_signal(evebitda, marketcap):
    base = _f28_pe_change(evebitda, 21) * _ln_mcap(marketcap, 21)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EVEBITDA chg 63d × log mcap
def f28vt_f28_valuation_trajectory_evebitdachg_63d_slope_v139_signal(evebitda, marketcap):
    base = _f28_pe_change(evebitda, 63) * _ln_mcap(marketcap, 63)
    result = _slope(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EVEBITDA chg 252d × log mcap
def f28vt_f28_valuation_trajectory_evebitdachg_252d_slope_v140_signal(evebitda, marketcap):
    base = _f28_pe_change(evebitda, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of EVEBITDA chg 504d × log mcap
def f28vt_f28_valuation_trajectory_evebitdachg_504d_slope_v141_signal(evebitda, marketcap):
    base = _f28_pe_change(evebitda, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of mcap/PS 252d
def f28vt_f28_valuation_trajectory_mcapps_252d_slope_v142_signal(ps, marketcap):
    base = _safe_div(_mean(marketcap, 252), _mean(ps, 252)) / 1e6 + _f28_pe_change(ps, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of mcap/PB 504d
def f28vt_f28_valuation_trajectory_mcappb_504d_slope_v143_signal(pb, marketcap):
    base = _safe_div(_mean(marketcap, 504), _mean(pb, 504)) / 1e6 + _f28_pe_change(pb, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of harm PE 252d × log mcap
def f28vt_f28_valuation_trajectory_peharm_252d_slope_v144_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    base = _safe_div(pd.Series(1.0, index=pe.index), _mean(inv, 252)) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of harm PE 504d × log mcap
def f28vt_f28_valuation_trajectory_peharm_504d_slope_v145_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    base = _safe_div(pd.Series(1.0, index=pe.index), _mean(inv, 504)) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of earnings yield traj 252d × log mcap
def f28vt_f28_valuation_trajectory_eyldtraj_252d_slope_v146_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    base = _f28_valuation_traj(inv, 252) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of earnings yield traj 504d × log mcap
def f28vt_f28_valuation_trajectory_eyldtraj_504d_slope_v147_signal(pe, marketcap):
    inv = _safe_div(pd.Series(1.0, index=pe.index), pe)
    base = _f28_valuation_traj(inv, 504) * _ln_mcap(marketcap, 504)
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of PE vol ratio 252d × log mcap
def f28vt_f28_valuation_trajectory_pevolratio_252d_slope_v148_signal(pe, marketcap):
    sv = _std(pe.pct_change(), 63)
    lv = _std(pe.pct_change(), 252).replace(0, np.nan)
    base = (sv / lv) * _ln_mcap(marketcap, 252) + _f28_pe_change(pe, 252) * 0.0
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of PE vol ratio 504d × log mcap
def f28vt_f28_valuation_trajectory_pevolratio_504d_slope_v149_signal(pe, marketcap):
    sv = _std(pe.pct_change(), 126)
    lv = _std(pe.pct_change(), 504).replace(0, np.nan)
    base = (sv / lv) * _ln_mcap(marketcap, 504) + _f28_pe_change(pe, 504) * 0.0
    result = _slope(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of comp val short 252d × log mcap
def f28vt_f28_valuation_trajectory_compvalshort_252d_slope_v150_signal(evebitda, pe, ps, marketcap):
    base = (_f28_pe_change(evebitda, 252) + _f28_pe_change(pe, 252) + _f28_pe_change(ps, 252)) * _ln_mcap(marketcap, 252)
    result = _slope(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28vt_f28_valuation_trajectory_pechg_21d_slope_v001_signal,
    f28vt_f28_valuation_trajectory_pechg_21d_slope_v002_signal,
    f28vt_f28_valuation_trajectory_pechg_63d_slope_v003_signal,
    f28vt_f28_valuation_trajectory_pechg_63d_slope_v004_signal,
    f28vt_f28_valuation_trajectory_pechg_63d_slope_v005_signal,
    f28vt_f28_valuation_trajectory_pechg_126d_slope_v006_signal,
    f28vt_f28_valuation_trajectory_pechg_126d_slope_v007_signal,
    f28vt_f28_valuation_trajectory_pechg_252d_slope_v008_signal,
    f28vt_f28_valuation_trajectory_pechg_252d_slope_v009_signal,
    f28vt_f28_valuation_trajectory_pechg_504d_slope_v010_signal,
    f28vt_f28_valuation_trajectory_pechg_504d_slope_v011_signal,
    f28vt_f28_valuation_trajectory_pbchg_21d_slope_v012_signal,
    f28vt_f28_valuation_trajectory_pbchg_63d_slope_v013_signal,
    f28vt_f28_valuation_trajectory_pbchg_252d_slope_v014_signal,
    f28vt_f28_valuation_trajectory_pbchg_504d_slope_v015_signal,
    f28vt_f28_valuation_trajectory_pschg_21d_slope_v016_signal,
    f28vt_f28_valuation_trajectory_pschg_63d_slope_v017_signal,
    f28vt_f28_valuation_trajectory_pschg_252d_slope_v018_signal,
    f28vt_f28_valuation_trajectory_pschg_504d_slope_v019_signal,
    f28vt_f28_valuation_trajectory_petraj_21d_slope_v020_signal,
    f28vt_f28_valuation_trajectory_petraj_63d_slope_v021_signal,
    f28vt_f28_valuation_trajectory_petraj_252d_slope_v022_signal,
    f28vt_f28_valuation_trajectory_petraj_504d_slope_v023_signal,
    f28vt_f28_valuation_trajectory_pbtraj_63d_slope_v024_signal,
    f28vt_f28_valuation_trajectory_pbtraj_252d_slope_v025_signal,
    f28vt_f28_valuation_trajectory_pbtraj_504d_slope_v026_signal,
    f28vt_f28_valuation_trajectory_pstraj_63d_slope_v027_signal,
    f28vt_f28_valuation_trajectory_pstraj_252d_slope_v028_signal,
    f28vt_f28_valuation_trajectory_pstraj_504d_slope_v029_signal,
    f28vt_f28_valuation_trajectory_evebitdatraj_63d_slope_v030_signal,
    f28vt_f28_valuation_trajectory_evebitdatraj_252d_slope_v031_signal,
    f28vt_f28_valuation_trajectory_evebitdatraj_504d_slope_v032_signal,
    f28vt_f28_valuation_trajectory_evebittraj_63d_slope_v033_signal,
    f28vt_f28_valuation_trajectory_evebittraj_252d_slope_v034_signal,
    f28vt_f28_valuation_trajectory_evebittraj_504d_slope_v035_signal,
    f28vt_f28_valuation_trajectory_evchg_63d_slope_v036_signal,
    f28vt_f28_valuation_trajectory_evchg_252d_slope_v037_signal,
    f28vt_f28_valuation_trajectory_evchg_504d_slope_v038_signal,
    f28vt_f28_valuation_trajectory_mcapchg_63d_slope_v039_signal,
    f28vt_f28_valuation_trajectory_mcapchg_252d_slope_v040_signal,
    f28vt_f28_valuation_trajectory_mcapchg_504d_slope_v041_signal,
    f28vt_f28_valuation_trajectory_pez_252d_slope_v042_signal,
    f28vt_f28_valuation_trajectory_pez_504d_slope_v043_signal,
    f28vt_f28_valuation_trajectory_pbz_252d_slope_v044_signal,
    f28vt_f28_valuation_trajectory_pbz_504d_slope_v045_signal,
    f28vt_f28_valuation_trajectory_psz_252d_slope_v046_signal,
    f28vt_f28_valuation_trajectory_psz_504d_slope_v047_signal,
    f28vt_f28_valuation_trajectory_evebitdaz_252d_slope_v048_signal,
    f28vt_f28_valuation_trajectory_evebitdaz_504d_slope_v049_signal,
    f28vt_f28_valuation_trajectory_pelog_21d_slope_v050_signal,
    f28vt_f28_valuation_trajectory_pelog_63d_slope_v051_signal,
    f28vt_f28_valuation_trajectory_pelog_252d_slope_v052_signal,
    f28vt_f28_valuation_trajectory_pechg_5d_slope_v053_signal,
    f28vt_f28_valuation_trajectory_pechg_10d_slope_v054_signal,
    f28vt_f28_valuation_trajectory_pechg_42d_slope_v055_signal,
    f28vt_f28_valuation_trajectory_pechg_189d_slope_v056_signal,
    f28vt_f28_valuation_trajectory_pechg_378d_slope_v057_signal,
    f28vt_f28_valuation_trajectory_pechgsq_21d_slope_v058_signal,
    f28vt_f28_valuation_trajectory_pechgsq_63d_slope_v059_signal,
    f28vt_f28_valuation_trajectory_pechgsq_252d_slope_v060_signal,
    f28vt_f28_valuation_trajectory_pechgsq_504d_slope_v061_signal,
    f28vt_f28_valuation_trajectory_pechgema_21d_slope_v062_signal,
    f28vt_f28_valuation_trajectory_pechgema_63d_slope_v063_signal,
    f28vt_f28_valuation_trajectory_pechgema_252d_slope_v064_signal,
    f28vt_f28_valuation_trajectory_pechgupcnt_252d_slope_v065_signal,
    f28vt_f28_valuation_trajectory_pbchgupcnt_504d_slope_v066_signal,
    f28vt_f28_valuation_trajectory_pschgdowncnt_252d_slope_v067_signal,
    f28vt_f28_valuation_trajectory_pevpb_252d_slope_v068_signal,
    f28vt_f28_valuation_trajectory_pevps_504d_slope_v069_signal,
    f28vt_f28_valuation_trajectory_evbvspe_252d_slope_v070_signal,
    f28vt_f28_valuation_trajectory_pestd_252d_slope_v071_signal,
    f28vt_f28_valuation_trajectory_pestd_504d_slope_v072_signal,
    f28vt_f28_valuation_trajectory_pbstd_252d_slope_v073_signal,
    f28vt_f28_valuation_trajectory_psstd_504d_slope_v074_signal,
    f28vt_f28_valuation_trajectory_pelvl_21d_slope_v075_signal,
    f28vt_f28_valuation_trajectory_pelvl_252d_slope_v076_signal,
    f28vt_f28_valuation_trajectory_pelvl_504d_slope_v077_signal,
    f28vt_f28_valuation_trajectory_pevsmean_252d_slope_v078_signal,
    f28vt_f28_valuation_trajectory_pevsmean_504d_slope_v079_signal,
    f28vt_f28_valuation_trajectory_pbvsmean_252d_slope_v080_signal,
    f28vt_f28_valuation_trajectory_psvsmean_252d_slope_v081_signal,
    f28vt_f28_valuation_trajectory_evebitvsmean_504d_slope_v082_signal,
    f28vt_f28_valuation_trajectory_evebitdavsmean_252d_slope_v083_signal,
    f28vt_f28_valuation_trajectory_mcapz_504d_slope_v084_signal,
    f28vt_f28_valuation_trajectory_mcapz_252d_slope_v085_signal,
    f28vt_f28_valuation_trajectory_evz_252d_slope_v086_signal,
    f28vt_f28_valuation_trajectory_evz_504d_slope_v087_signal,
    f28vt_f28_valuation_trajectory_pechgabs_21d_slope_v088_signal,
    f28vt_f28_valuation_trajectory_pechgabs_252d_slope_v089_signal,
    f28vt_f28_valuation_trajectory_pechgabs_504d_slope_v090_signal,
    f28vt_f28_valuation_trajectory_pbchgabs_252d_slope_v091_signal,
    f28vt_f28_valuation_trajectory_pschgabs_252d_slope_v092_signal,
    f28vt_f28_valuation_trajectory_pecv_252d_slope_v093_signal,
    f28vt_f28_valuation_trajectory_pecv_504d_slope_v094_signal,
    f28vt_f28_valuation_trajectory_evebitdacv_252d_slope_v095_signal,
    f28vt_f28_valuation_trajectory_pechgratio_21v63_slope_v096_signal,
    f28vt_f28_valuation_trajectory_pechgratio_63v252_slope_v097_signal,
    f28vt_f28_valuation_trajectory_pechgxmom_21d_slope_v098_signal,
    f28vt_f28_valuation_trajectory_pechgxmom_63d_slope_v099_signal,
    f28vt_f28_valuation_trajectory_pechgxmom_252d_slope_v100_signal,
    f28vt_f28_valuation_trajectory_peaccel_252d_slope_v101_signal,
    f28vt_f28_valuation_trajectory_peaccel_504d_slope_v102_signal,
    f28vt_f28_valuation_trajectory_pearea_252d_slope_v103_signal,
    f28vt_f28_valuation_trajectory_pearea_504d_slope_v104_signal,
    f28vt_f28_valuation_trajectory_pechgskew_252d_slope_v105_signal,
    f28vt_f28_valuation_trajectory_pechgskew_504d_slope_v106_signal,
    f28vt_f28_valuation_trajectory_pechgkurt_252d_slope_v107_signal,
    f28vt_f28_valuation_trajectory_pechgkurt_504d_slope_v108_signal,
    f28vt_f28_valuation_trajectory_composite_252d_slope_v109_signal,
    f28vt_f28_valuation_trajectory_composite_504d_slope_v110_signal,
    f28vt_f28_valuation_trajectory_evtrajxmcap_252d_slope_v111_signal,
    f28vt_f28_valuation_trajectory_mcaptrajxmcap_504d_slope_v112_signal,
    f28vt_f28_valuation_trajectory_pexpb_252d_slope_v113_signal,
    f28vt_f28_valuation_trajectory_pexps_504d_slope_v114_signal,
    f28vt_f28_valuation_trajectory_pelvlxmcap_21d_slope_v115_signal,
    f28vt_f28_valuation_trajectory_pelvlxmcap_252d_slope_v116_signal,
    f28vt_f28_valuation_trajectory_pelvlxmcap_504d_slope_v117_signal,
    f28vt_f28_valuation_trajectory_pediff_504_slope_v118_signal,
    f28vt_f28_valuation_trajectory_pbdiff_504_slope_v119_signal,
    f28vt_f28_valuation_trajectory_psdiff_504_slope_v120_signal,
    f28vt_f28_valuation_trajectory_evebitdiff_504_slope_v121_signal,
    f28vt_f28_valuation_trajectory_evebitdadiff_504_slope_v122_signal,
    f28vt_f28_valuation_trajectory_pevsmin_252d_slope_v123_signal,
    f28vt_f28_valuation_trajectory_pesum_504d_slope_v124_signal,
    f28vt_f28_valuation_trajectory_pesum_252d_slope_v125_signal,
    f28vt_f28_valuation_trajectory_evebitdasum_252d_slope_v126_signal,
    f28vt_f28_valuation_trajectory_pesignsum_252d_slope_v127_signal,
    f28vt_f28_valuation_trajectory_pesignsum_504d_slope_v128_signal,
    f28vt_f28_valuation_trajectory_evxmcap_252d_slope_v129_signal,
    f28vt_f28_valuation_trajectory_evxmcap_504d_slope_v130_signal,
    f28vt_f28_valuation_trajectory_evebitdacumchg_252d_slope_v131_signal,
    f28vt_f28_valuation_trajectory_evebitdacumchg_504d_slope_v132_signal,
    f28vt_f28_valuation_trajectory_mcapvol_21d_slope_v133_signal,
    f28vt_f28_valuation_trajectory_mcapvol_252d_slope_v134_signal,
    f28vt_f28_valuation_trajectory_evvol_504d_slope_v135_signal,
    f28vt_f28_valuation_trajectory_evebitchg_21d_slope_v136_signal,
    f28vt_f28_valuation_trajectory_evebitchg_63d_slope_v137_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_21d_slope_v138_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_63d_slope_v139_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_252d_slope_v140_signal,
    f28vt_f28_valuation_trajectory_evebitdachg_504d_slope_v141_signal,
    f28vt_f28_valuation_trajectory_mcapps_252d_slope_v142_signal,
    f28vt_f28_valuation_trajectory_mcappb_504d_slope_v143_signal,
    f28vt_f28_valuation_trajectory_peharm_252d_slope_v144_signal,
    f28vt_f28_valuation_trajectory_peharm_504d_slope_v145_signal,
    f28vt_f28_valuation_trajectory_eyldtraj_252d_slope_v146_signal,
    f28vt_f28_valuation_trajectory_eyldtraj_504d_slope_v147_signal,
    f28vt_f28_valuation_trajectory_pevolratio_252d_slope_v148_signal,
    f28vt_f28_valuation_trajectory_pevolratio_504d_slope_v149_signal,
    f28vt_f28_valuation_trajectory_compvalshort_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_VALUATION_TRAJECTORY_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
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
        "marketcap": marketcap, "ev": ev, "evebit": evebit,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f28_valuation_trajectory_2nd_derivatives_001_150_claude: {n_features} features pass")
