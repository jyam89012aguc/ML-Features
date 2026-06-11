import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _z(s, w):
    return (s - _mean(s, w)) / _std(s, w).replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f90rcp_rev_yoy(s):
    return s.pct_change(periods=252)


def _f90rcp_capex_yoy(s):
    return s.pct_change(periods=252)


def _f90rcp_phase(rev, cx):
    r = rev.pct_change(periods=252)
    c = cx.pct_change(periods=252)
    return r - c


# 5d slope of 21d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_21d_slope_v001_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_21d_slope_v002_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_21d_slope_v003_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_21d_slope_v004_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_21d_slope_v005_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_63d_slope_v006_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_63d_slope_v007_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_63d_slope_v008_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_63d_slope_v009_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_63d_slope_v010_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_126d_slope_v011_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_126d_slope_v012_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_126d_slope_v013_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_126d_slope_v014_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_126d_slope_v015_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_252d_slope_v016_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_252d_slope_v017_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_252d_slope_v018_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_252d_slope_v019_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_252d_slope_v020_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_504d_slope_v021_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_504d_slope_v022_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_504d_slope_v023_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_504d_slope_v024_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d lvl
def f90rcp_f90_semi_revenue_cycle_phase_lvl_504d_slope_v025_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z
def f90rcp_f90_semi_revenue_cycle_phase_z_21d_slope_v026_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z
def f90rcp_f90_semi_revenue_cycle_phase_z_21d_slope_v027_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z
def f90rcp_f90_semi_revenue_cycle_phase_z_21d_slope_v028_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d z
def f90rcp_f90_semi_revenue_cycle_phase_z_21d_slope_v029_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d z
def f90rcp_f90_semi_revenue_cycle_phase_z_21d_slope_v030_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z
def f90rcp_f90_semi_revenue_cycle_phase_z_63d_slope_v031_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z
def f90rcp_f90_semi_revenue_cycle_phase_z_63d_slope_v032_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z
def f90rcp_f90_semi_revenue_cycle_phase_z_63d_slope_v033_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d z
def f90rcp_f90_semi_revenue_cycle_phase_z_63d_slope_v034_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d z
def f90rcp_f90_semi_revenue_cycle_phase_z_63d_slope_v035_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z
def f90rcp_f90_semi_revenue_cycle_phase_z_126d_slope_v036_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z
def f90rcp_f90_semi_revenue_cycle_phase_z_126d_slope_v037_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z
def f90rcp_f90_semi_revenue_cycle_phase_z_126d_slope_v038_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d z
def f90rcp_f90_semi_revenue_cycle_phase_z_126d_slope_v039_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d z
def f90rcp_f90_semi_revenue_cycle_phase_z_126d_slope_v040_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z
def f90rcp_f90_semi_revenue_cycle_phase_z_252d_slope_v041_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z
def f90rcp_f90_semi_revenue_cycle_phase_z_252d_slope_v042_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z
def f90rcp_f90_semi_revenue_cycle_phase_z_252d_slope_v043_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d z
def f90rcp_f90_semi_revenue_cycle_phase_z_252d_slope_v044_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d z
def f90rcp_f90_semi_revenue_cycle_phase_z_252d_slope_v045_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z
def f90rcp_f90_semi_revenue_cycle_phase_z_504d_slope_v046_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z
def f90rcp_f90_semi_revenue_cycle_phase_z_504d_slope_v047_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z
def f90rcp_f90_semi_revenue_cycle_phase_z_504d_slope_v048_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d z
def f90rcp_f90_semi_revenue_cycle_phase_z_504d_slope_v049_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d z
def f90rcp_f90_semi_revenue_cycle_phase_z_504d_slope_v050_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_63d_slope_v051_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_63d_slope_v052_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_63d_slope_v053_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_63d_slope_v054_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_63d_slope_v055_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_126d_slope_v056_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_126d_slope_v057_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_126d_slope_v058_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_126d_slope_v059_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_126d_slope_v060_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_252d_slope_v061_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_252d_slope_v062_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_252d_slope_v063_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_252d_slope_v064_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d dd
def f90rcp_f90_semi_revenue_cycle_phase_dd_252d_slope_v065_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_63d_slope_v066_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_63d_slope_v067_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_63d_slope_v068_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_63d_slope_v069_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_63d_slope_v070_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_126d_slope_v071_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_126d_slope_v072_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_126d_slope_v073_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_126d_slope_v074_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d runup
def f90rcp_f90_semi_revenue_cycle_phase_runup_126d_slope_v075_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_63d_slope_v076_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_63d_slope_v077_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_63d_slope_v078_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_63d_slope_v079_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_63d_slope_v080_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_126d_slope_v081_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_126d_slope_v082_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_126d_slope_v083_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_126d_slope_v084_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d rng
def f90rcp_f90_semi_revenue_cycle_phase_rng_126d_slope_v085_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pos
def f90rcp_f90_semi_revenue_cycle_phase_pos_126d_slope_v086_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pos
def f90rcp_f90_semi_revenue_cycle_phase_pos_126d_slope_v087_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pos
def f90rcp_f90_semi_revenue_cycle_phase_pos_126d_slope_v088_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d pos
def f90rcp_f90_semi_revenue_cycle_phase_pos_126d_slope_v089_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d pos
def f90rcp_f90_semi_revenue_cycle_phase_pos_126d_slope_v090_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d std
def f90rcp_f90_semi_revenue_cycle_phase_std_63d_slope_v091_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d std
def f90rcp_f90_semi_revenue_cycle_phase_std_63d_slope_v092_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d std
def f90rcp_f90_semi_revenue_cycle_phase_std_63d_slope_v093_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d std
def f90rcp_f90_semi_revenue_cycle_phase_std_63d_slope_v094_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d std
def f90rcp_f90_semi_revenue_cycle_phase_std_63d_slope_v095_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d std
def f90rcp_f90_semi_revenue_cycle_phase_std_126d_slope_v096_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d std
def f90rcp_f90_semi_revenue_cycle_phase_std_126d_slope_v097_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d std
def f90rcp_f90_semi_revenue_cycle_phase_std_126d_slope_v098_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d std
def f90rcp_f90_semi_revenue_cycle_phase_std_126d_slope_v099_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d std
def f90rcp_f90_semi_revenue_cycle_phase_std_126d_slope_v100_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d std
def f90rcp_f90_semi_revenue_cycle_phase_std_252d_slope_v101_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d std
def f90rcp_f90_semi_revenue_cycle_phase_std_252d_slope_v102_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d std
def f90rcp_f90_semi_revenue_cycle_phase_std_252d_slope_v103_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d std
def f90rcp_f90_semi_revenue_cycle_phase_std_252d_slope_v104_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d std
def f90rcp_f90_semi_revenue_cycle_phase_std_252d_slope_v105_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_63d_slope_v106_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_63d_slope_v107_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_63d_slope_v108_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_63d_slope_v109_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_63d_slope_v110_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_126d_slope_v111_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_126d_slope_v112_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_126d_slope_v113_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_126d_slope_v114_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d hit
def f90rcp_f90_semi_revenue_cycle_phase_hit_126d_slope_v115_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d signcum
def f90rcp_f90_semi_revenue_cycle_phase_signcum_126d_slope_v116_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d signcum
def f90rcp_f90_semi_revenue_cycle_phase_signcum_126d_slope_v117_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d signcum
def f90rcp_f90_semi_revenue_cycle_phase_signcum_126d_slope_v118_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d signcum
def f90rcp_f90_semi_revenue_cycle_phase_signcum_126d_slope_v119_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d signcum
def f90rcp_f90_semi_revenue_cycle_phase_signcum_126d_slope_v120_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_63d_slope_v121_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_63d_slope_v122_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_63d_slope_v123_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_63d_slope_v124_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_63d_slope_v125_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_252d_slope_v126_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_252d_slope_v127_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_252d_slope_v128_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_252d_slope_v129_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cum
def f90rcp_f90_semi_revenue_cycle_phase_cum_252d_slope_v130_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d condup
def f90rcp_f90_semi_revenue_cycle_phase_condup_126d_slope_v131_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d condup
def f90rcp_f90_semi_revenue_cycle_phase_condup_126d_slope_v132_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d condup
def f90rcp_f90_semi_revenue_cycle_phase_condup_126d_slope_v133_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d condup
def f90rcp_f90_semi_revenue_cycle_phase_condup_126d_slope_v134_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d condup
def f90rcp_f90_semi_revenue_cycle_phase_condup_126d_slope_v135_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d conddn
def f90rcp_f90_semi_revenue_cycle_phase_conddn_126d_slope_v136_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d conddn
def f90rcp_f90_semi_revenue_cycle_phase_conddn_126d_slope_v137_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d conddn
def f90rcp_f90_semi_revenue_cycle_phase_conddn_126d_slope_v138_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d conddn
def f90rcp_f90_semi_revenue_cycle_phase_conddn_126d_slope_v139_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d conddn
def f90rcp_f90_semi_revenue_cycle_phase_conddn_126d_slope_v140_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d corr
def f90rcp_f90_semi_revenue_cycle_phase_corr_126d_slope_v141_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d corr
def f90rcp_f90_semi_revenue_cycle_phase_corr_126d_slope_v142_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d corr
def f90rcp_f90_semi_revenue_cycle_phase_corr_126d_slope_v143_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d corr
def f90rcp_f90_semi_revenue_cycle_phase_corr_126d_slope_v144_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d corr
def f90rcp_f90_semi_revenue_cycle_phase_corr_126d_slope_v145_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ratio
def f90rcp_f90_semi_revenue_cycle_phase_ratio_126d_slope_v146_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ratio
def f90rcp_f90_semi_revenue_cycle_phase_ratio_126d_slope_v147_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ratio
def f90rcp_f90_semi_revenue_cycle_phase_ratio_126d_slope_v148_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d ratio
def f90rcp_f90_semi_revenue_cycle_phase_ratio_126d_slope_v149_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d ratio
def f90rcp_f90_semi_revenue_cycle_phase_ratio_126d_slope_v150_signal(revenue, capex, closeadj):
    x = _f90rcp_phase(revenue, capex)
    y = _f90rcp_rev_yoy(revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
