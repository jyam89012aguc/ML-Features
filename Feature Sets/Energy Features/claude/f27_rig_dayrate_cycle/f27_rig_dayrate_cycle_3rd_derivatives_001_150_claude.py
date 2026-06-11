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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f27_revenue_growth(revenue, w):
    return revenue.pct_change(periods=w)


def _f27_dayrate_pulse(revenue, ppnenet, w):
    rpa = revenue / ppnenet.replace(0, np.nan)
    g = rpa.pct_change(periods=w)
    sd = rpa.rolling(w, min_periods=max(1, w // 2)).std()
    return g * sd


def _f27_dayrate_cycle_position(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return (revenue - m) / sd.replace(0, np.nan)


# ===== features =====

def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xc_jsw5_jerk_v001_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xc_jsw5_jerk_v002_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xc_jsw5_jerk_v003_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xc_jsw5_jerk_v004_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xc_jsw5_jerk_v005_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xc_jsw5_jerk_v006_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xc_jsw5_jerk_v007_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xc_jsw5_jerk_v008_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xc_jsw5_jerk_v009_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xc_jsw5_jerk_v010_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xc_jsw5_jerk_v011_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xc_jsw5_jerk_v012_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xc_jsw5_jerk_v013_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xc_jsw5_jerk_v014_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xc_jsw5_jerk_v015_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xc_jsw5_jerk_v016_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xc_jsw5_jerk_v017_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xc_jsw5_jerk_v018_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xc_jsw5_jerk_v019_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xc_jsw5_jerk_v020_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xc_jsw5_jerk_v021_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 126)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xc_jsw5_jerk_v022_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xc_jsw5_jerk_v023_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xc_jsw5_jerk_v024_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 189)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xc_jsw5_jerk_v025_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xc_jsw5_jerk_v026_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xc_jsw5_jerk_v027_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 252)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xc_jsw5_jerk_v028_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xc_jsw5_jerk_v029_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xc_jsw5_jerk_v030_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 378)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xc_jsw5_jerk_v031_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xc_jsw5_jerk_v032_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xc_jsw5_jerk_v033_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 504)
    base = (base) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xc2_jsw5_jerk_v034_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xc2_jsw5_jerk_v035_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xc2_jsw5_jerk_v036_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xc2_jsw5_jerk_v037_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xc2_jsw5_jerk_v038_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xc2_jsw5_jerk_v039_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xc2_jsw5_jerk_v040_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xc2_jsw5_jerk_v041_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xc2_jsw5_jerk_v042_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xc2_jsw5_jerk_v043_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xc2_jsw5_jerk_v044_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xc2_jsw5_jerk_v045_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xc2_jsw5_jerk_v046_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xc2_jsw5_jerk_v047_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xc2_jsw5_jerk_v048_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xc2_jsw5_jerk_v049_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xc2_jsw5_jerk_v050_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xc2_jsw5_jerk_v051_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xc2_jsw5_jerk_v052_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xc2_jsw5_jerk_v053_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xc2_jsw5_jerk_v054_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 126)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xc2_jsw5_jerk_v055_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xc2_jsw5_jerk_v056_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xc2_jsw5_jerk_v057_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 189)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xc2_jsw5_jerk_v058_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xc2_jsw5_jerk_v059_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xc2_jsw5_jerk_v060_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 252)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xc2_jsw5_jerk_v061_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xc2_jsw5_jerk_v062_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xc2_jsw5_jerk_v063_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 378)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xc2_jsw5_jerk_v064_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xc2_jsw5_jerk_v065_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xc2_jsw5_jerk_v066_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 504)
    base = (base) * closeadj * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xmc_jsw5_jerk_v067_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xmc_jsw5_jerk_v068_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xmc_jsw5_jerk_v069_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xmc_jsw5_jerk_v070_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xmc_jsw5_jerk_v071_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xmc_jsw5_jerk_v072_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xmc_jsw5_jerk_v073_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xmc_jsw5_jerk_v074_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xmc_jsw5_jerk_v075_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xmc_jsw5_jerk_v076_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xmc_jsw5_jerk_v077_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xmc_jsw5_jerk_v078_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xmc_jsw5_jerk_v079_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xmc_jsw5_jerk_v080_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xmc_jsw5_jerk_v081_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xmc_jsw5_jerk_v082_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xmc_jsw5_jerk_v083_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xmc_jsw5_jerk_v084_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xmc_jsw5_jerk_v085_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xmc_jsw5_jerk_v086_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xmc_jsw5_jerk_v087_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 126)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xmc_jsw5_jerk_v088_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xmc_jsw5_jerk_v089_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xmc_jsw5_jerk_v090_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 189)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xmc_jsw5_jerk_v091_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xmc_jsw5_jerk_v092_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xmc_jsw5_jerk_v093_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 252)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xmc_jsw5_jerk_v094_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xmc_jsw5_jerk_v095_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xmc_jsw5_jerk_v096_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 378)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xmc_jsw5_jerk_v097_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xmc_jsw5_jerk_v098_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xmc_jsw5_jerk_v099_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 504)
    base = (base) * _mean(closeadj, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xzc_jsw5_jerk_v100_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xzc_jsw5_jerk_v101_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xzc_jsw5_jerk_v102_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xzc_jsw5_jerk_v103_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xzc_jsw5_jerk_v104_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xzc_jsw5_jerk_v105_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xzc_jsw5_jerk_v106_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xzc_jsw5_jerk_v107_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xzc_jsw5_jerk_v108_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xzc_jsw5_jerk_v109_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xzc_jsw5_jerk_v110_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xzc_jsw5_jerk_v111_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xzc_jsw5_jerk_v112_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xzc_jsw5_jerk_v113_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xzc_jsw5_jerk_v114_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xzc_jsw5_jerk_v115_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xzc_jsw5_jerk_v116_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xzc_jsw5_jerk_v117_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xzc_jsw5_jerk_v118_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xzc_jsw5_jerk_v119_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xzc_jsw5_jerk_v120_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 126)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xzc_jsw5_jerk_v121_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xzc_jsw5_jerk_v122_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xzc_jsw5_jerk_v123_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 189)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xzc_jsw5_jerk_v124_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xzc_jsw5_jerk_v125_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xzc_jsw5_jerk_v126_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 252)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xzc_jsw5_jerk_v127_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xzc_jsw5_jerk_v128_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xzc_jsw5_jerk_v129_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 378)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xzc_jsw5_jerk_v130_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xzc_jsw5_jerk_v131_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xzc_jsw5_jerk_v132_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 504)
    base = (base) * (_z(closeadj, 63) + 1.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_5d_base_dmc_jsw5_jerk_v133_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_dmc_jsw5_jerk_v134_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_dmc_jsw5_jerk_v135_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 5)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_10d_base_dmc_jsw5_jerk_v136_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_dmc_jsw5_jerk_v137_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_dmc_jsw5_jerk_v138_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 10)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_21d_base_dmc_jsw5_jerk_v139_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_dmc_jsw5_jerk_v140_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_dmc_jsw5_jerk_v141_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 21)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_42d_base_dmc_jsw5_jerk_v142_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_dmc_jsw5_jerk_v143_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_dmc_jsw5_jerk_v144_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 42)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_63d_base_dmc_jsw5_jerk_v145_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_dmc_jsw5_jerk_v146_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_dmc_jsw5_jerk_v147_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 63)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_revg_84d_base_dmc_jsw5_jerk_v148_signal(revenue, closeadj):
    base = _f27_revenue_growth(revenue, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_dmc_jsw5_jerk_v149_signal(revenue, ppnenet, closeadj):
    base = _f27_dayrate_pulse(revenue, ppnenet, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_dmc_jsw5_jerk_v150_signal(revenue, closeadj):
    base = _f27_dayrate_cycle_position(revenue, 84)
    base = (base) * closeadj / _mean(closeadj, 252).replace(0, np.nan)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xc_jsw5_jerk_v001_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xc_jsw5_jerk_v002_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xc_jsw5_jerk_v003_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xc_jsw5_jerk_v004_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xc_jsw5_jerk_v005_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xc_jsw5_jerk_v006_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xc_jsw5_jerk_v007_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xc_jsw5_jerk_v008_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xc_jsw5_jerk_v009_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xc_jsw5_jerk_v010_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xc_jsw5_jerk_v011_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xc_jsw5_jerk_v012_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xc_jsw5_jerk_v013_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xc_jsw5_jerk_v014_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xc_jsw5_jerk_v015_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xc_jsw5_jerk_v016_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xc_jsw5_jerk_v017_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xc_jsw5_jerk_v018_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xc_jsw5_jerk_v019_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xc_jsw5_jerk_v020_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xc_jsw5_jerk_v021_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xc_jsw5_jerk_v022_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xc_jsw5_jerk_v023_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xc_jsw5_jerk_v024_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xc_jsw5_jerk_v025_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xc_jsw5_jerk_v026_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xc_jsw5_jerk_v027_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xc_jsw5_jerk_v028_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xc_jsw5_jerk_v029_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xc_jsw5_jerk_v030_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xc_jsw5_jerk_v031_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xc_jsw5_jerk_v032_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xc_jsw5_jerk_v033_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xc2_jsw5_jerk_v034_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xc2_jsw5_jerk_v035_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xc2_jsw5_jerk_v036_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xc2_jsw5_jerk_v037_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xc2_jsw5_jerk_v038_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xc2_jsw5_jerk_v039_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xc2_jsw5_jerk_v040_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xc2_jsw5_jerk_v041_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xc2_jsw5_jerk_v042_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xc2_jsw5_jerk_v043_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xc2_jsw5_jerk_v044_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xc2_jsw5_jerk_v045_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xc2_jsw5_jerk_v046_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xc2_jsw5_jerk_v047_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xc2_jsw5_jerk_v048_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xc2_jsw5_jerk_v049_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xc2_jsw5_jerk_v050_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xc2_jsw5_jerk_v051_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xc2_jsw5_jerk_v052_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xc2_jsw5_jerk_v053_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xc2_jsw5_jerk_v054_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xc2_jsw5_jerk_v055_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xc2_jsw5_jerk_v056_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xc2_jsw5_jerk_v057_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xc2_jsw5_jerk_v058_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xc2_jsw5_jerk_v059_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xc2_jsw5_jerk_v060_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xc2_jsw5_jerk_v061_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xc2_jsw5_jerk_v062_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xc2_jsw5_jerk_v063_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xc2_jsw5_jerk_v064_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xc2_jsw5_jerk_v065_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xc2_jsw5_jerk_v066_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xmc_jsw5_jerk_v067_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xmc_jsw5_jerk_v068_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xmc_jsw5_jerk_v069_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xmc_jsw5_jerk_v070_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xmc_jsw5_jerk_v071_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xmc_jsw5_jerk_v072_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xmc_jsw5_jerk_v073_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xmc_jsw5_jerk_v074_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xmc_jsw5_jerk_v075_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xmc_jsw5_jerk_v076_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xmc_jsw5_jerk_v077_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xmc_jsw5_jerk_v078_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xmc_jsw5_jerk_v079_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xmc_jsw5_jerk_v080_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xmc_jsw5_jerk_v081_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xmc_jsw5_jerk_v082_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xmc_jsw5_jerk_v083_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xmc_jsw5_jerk_v084_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xmc_jsw5_jerk_v085_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xmc_jsw5_jerk_v086_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xmc_jsw5_jerk_v087_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xmc_jsw5_jerk_v088_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xmc_jsw5_jerk_v089_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xmc_jsw5_jerk_v090_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xmc_jsw5_jerk_v091_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xmc_jsw5_jerk_v092_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xmc_jsw5_jerk_v093_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xmc_jsw5_jerk_v094_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xmc_jsw5_jerk_v095_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xmc_jsw5_jerk_v096_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xmc_jsw5_jerk_v097_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xmc_jsw5_jerk_v098_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xmc_jsw5_jerk_v099_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_xzc_jsw5_jerk_v100_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_xzc_jsw5_jerk_v101_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_xzc_jsw5_jerk_v102_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_xzc_jsw5_jerk_v103_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_xzc_jsw5_jerk_v104_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_xzc_jsw5_jerk_v105_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_xzc_jsw5_jerk_v106_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_xzc_jsw5_jerk_v107_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_xzc_jsw5_jerk_v108_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_xzc_jsw5_jerk_v109_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_xzc_jsw5_jerk_v110_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_xzc_jsw5_jerk_v111_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_xzc_jsw5_jerk_v112_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_xzc_jsw5_jerk_v113_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_xzc_jsw5_jerk_v114_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_xzc_jsw5_jerk_v115_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_xzc_jsw5_jerk_v116_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_xzc_jsw5_jerk_v117_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_126d_base_xzc_jsw5_jerk_v118_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_126d_base_xzc_jsw5_jerk_v119_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_126d_base_xzc_jsw5_jerk_v120_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_189d_base_xzc_jsw5_jerk_v121_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_189d_base_xzc_jsw5_jerk_v122_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_189d_base_xzc_jsw5_jerk_v123_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_252d_base_xzc_jsw5_jerk_v124_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_252d_base_xzc_jsw5_jerk_v125_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_252d_base_xzc_jsw5_jerk_v126_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_378d_base_xzc_jsw5_jerk_v127_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_378d_base_xzc_jsw5_jerk_v128_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_378d_base_xzc_jsw5_jerk_v129_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_504d_base_xzc_jsw5_jerk_v130_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_504d_base_xzc_jsw5_jerk_v131_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_504d_base_xzc_jsw5_jerk_v132_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_5d_base_dmc_jsw5_jerk_v133_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_5d_base_dmc_jsw5_jerk_v134_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_5d_base_dmc_jsw5_jerk_v135_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_10d_base_dmc_jsw5_jerk_v136_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_10d_base_dmc_jsw5_jerk_v137_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_10d_base_dmc_jsw5_jerk_v138_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_21d_base_dmc_jsw5_jerk_v139_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_21d_base_dmc_jsw5_jerk_v140_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_21d_base_dmc_jsw5_jerk_v141_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_42d_base_dmc_jsw5_jerk_v142_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_42d_base_dmc_jsw5_jerk_v143_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_42d_base_dmc_jsw5_jerk_v144_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_63d_base_dmc_jsw5_jerk_v145_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_63d_base_dmc_jsw5_jerk_v146_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_63d_base_dmc_jsw5_jerk_v147_signal,
    f27rdc_f27_rig_dayrate_cycle_revg_84d_base_dmc_jsw5_jerk_v148_signal,
    f27rdc_f27_rig_dayrate_cycle_drpulse_84d_base_dmc_jsw5_jerk_v149_signal,
    f27rdc_f27_rig_dayrate_cycle_drcyc_84d_base_dmc_jsw5_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_RIG_DAYRATE_CYCLE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda,
        "assets": assets, "equity": equity, "debt": debt, "cashneq": cashneq,
        "deferredrev": deferredrev, "ppnenet": ppnenet, "ebitdamargin": ebitdamargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f27_revenue_growth', '_f27_dayrate_pulse', '_f27_dayrate_cycle_position',)
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
    print(f"OK f27_rig_dayrate_cycle_3rd_derivatives_001_150_claude: {n_features} features pass")
