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


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f91ca_rev_amp(s, n=252):
    mp = max(1, n // 2)
    return (s.rolling(n, min_periods=mp).max() - s.rolling(n, min_periods=mp).min()) / s.rolling(n, min_periods=mp).mean().replace(0, np.nan)


def _f91ca_capex_amp(s, n=252):
    mp = max(1, n // 2)
    return (s.rolling(n, min_periods=mp).max() - s.rolling(n, min_periods=mp).min()) / s.rolling(n, min_periods=mp).mean().replace(0, np.nan)


def _f91ca_combined(rev, cx, n=252):
    mp = max(1, n // 2)
    ra = (rev.rolling(n, min_periods=mp).max() - rev.rolling(n, min_periods=mp).min()) / rev.rolling(n, min_periods=mp).mean().replace(0, np.nan)
    ca = (cx.rolling(n, min_periods=mp).max() - cx.rolling(n, min_periods=mp).min()) / cx.rolling(n, min_periods=mp).mean().replace(0, np.nan)
    return ra + ca


# 5d curv of 21d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_21d_curv_v001_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_21d_curv_v002_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_21d_curv_v003_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_21d_curv_v004_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_21d_curv_v005_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_63d_curv_v006_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_63d_curv_v007_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_63d_curv_v008_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_63d_curv_v009_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_63d_curv_v010_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_126d_curv_v011_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_126d_curv_v012_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_126d_curv_v013_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_126d_curv_v014_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_126d_curv_v015_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_252d_curv_v016_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_252d_curv_v017_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_252d_curv_v018_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_252d_curv_v019_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_252d_curv_v020_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_504d_curv_v021_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_504d_curv_v022_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_504d_curv_v023_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_504d_curv_v024_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d lvl
def f91ca_f91_semi_cycle_amplitude_lvl_504d_curv_v025_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _mean(x, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d z
def f91ca_f91_semi_cycle_amplitude_z_21d_curv_v026_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d z
def f91ca_f91_semi_cycle_amplitude_z_21d_curv_v027_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d z
def f91ca_f91_semi_cycle_amplitude_z_21d_curv_v028_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d z
def f91ca_f91_semi_cycle_amplitude_z_21d_curv_v029_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d z
def f91ca_f91_semi_cycle_amplitude_z_21d_curv_v030_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d z
def f91ca_f91_semi_cycle_amplitude_z_63d_curv_v031_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d z
def f91ca_f91_semi_cycle_amplitude_z_63d_curv_v032_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d z
def f91ca_f91_semi_cycle_amplitude_z_63d_curv_v033_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d z
def f91ca_f91_semi_cycle_amplitude_z_63d_curv_v034_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d z
def f91ca_f91_semi_cycle_amplitude_z_63d_curv_v035_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d z
def f91ca_f91_semi_cycle_amplitude_z_126d_curv_v036_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d z
def f91ca_f91_semi_cycle_amplitude_z_126d_curv_v037_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d z
def f91ca_f91_semi_cycle_amplitude_z_126d_curv_v038_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d z
def f91ca_f91_semi_cycle_amplitude_z_126d_curv_v039_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d z
def f91ca_f91_semi_cycle_amplitude_z_126d_curv_v040_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d z
def f91ca_f91_semi_cycle_amplitude_z_252d_curv_v041_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d z
def f91ca_f91_semi_cycle_amplitude_z_252d_curv_v042_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d z
def f91ca_f91_semi_cycle_amplitude_z_252d_curv_v043_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d z
def f91ca_f91_semi_cycle_amplitude_z_252d_curv_v044_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d z
def f91ca_f91_semi_cycle_amplitude_z_252d_curv_v045_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d z
def f91ca_f91_semi_cycle_amplitude_z_504d_curv_v046_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d z
def f91ca_f91_semi_cycle_amplitude_z_504d_curv_v047_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d z
def f91ca_f91_semi_cycle_amplitude_z_504d_curv_v048_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d z
def f91ca_f91_semi_cycle_amplitude_z_504d_curv_v049_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d z
def f91ca_f91_semi_cycle_amplitude_z_504d_curv_v050_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _z(x, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d dd
def f91ca_f91_semi_cycle_amplitude_dd_63d_curv_v051_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d dd
def f91ca_f91_semi_cycle_amplitude_dd_63d_curv_v052_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d dd
def f91ca_f91_semi_cycle_amplitude_dd_63d_curv_v053_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d dd
def f91ca_f91_semi_cycle_amplitude_dd_63d_curv_v054_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d dd
def f91ca_f91_semi_cycle_amplitude_dd_63d_curv_v055_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d dd
def f91ca_f91_semi_cycle_amplitude_dd_126d_curv_v056_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d dd
def f91ca_f91_semi_cycle_amplitude_dd_126d_curv_v057_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d dd
def f91ca_f91_semi_cycle_amplitude_dd_126d_curv_v058_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d dd
def f91ca_f91_semi_cycle_amplitude_dd_126d_curv_v059_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d dd
def f91ca_f91_semi_cycle_amplitude_dd_126d_curv_v060_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d dd
def f91ca_f91_semi_cycle_amplitude_dd_252d_curv_v061_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d dd
def f91ca_f91_semi_cycle_amplitude_dd_252d_curv_v062_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d dd
def f91ca_f91_semi_cycle_amplitude_dd_252d_curv_v063_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d dd
def f91ca_f91_semi_cycle_amplitude_dd_252d_curv_v064_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d dd
def f91ca_f91_semi_cycle_amplitude_dd_252d_curv_v065_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _max(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d runup
def f91ca_f91_semi_cycle_amplitude_runup_63d_curv_v066_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d runup
def f91ca_f91_semi_cycle_amplitude_runup_63d_curv_v067_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d runup
def f91ca_f91_semi_cycle_amplitude_runup_63d_curv_v068_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d runup
def f91ca_f91_semi_cycle_amplitude_runup_63d_curv_v069_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d runup
def f91ca_f91_semi_cycle_amplitude_runup_63d_curv_v070_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d runup
def f91ca_f91_semi_cycle_amplitude_runup_126d_curv_v071_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d runup
def f91ca_f91_semi_cycle_amplitude_runup_126d_curv_v072_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d runup
def f91ca_f91_semi_cycle_amplitude_runup_126d_curv_v073_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d runup
def f91ca_f91_semi_cycle_amplitude_runup_126d_curv_v074_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d runup
def f91ca_f91_semi_cycle_amplitude_runup_126d_curv_v075_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x - _min(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d rng
def f91ca_f91_semi_cycle_amplitude_rng_63d_curv_v076_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d rng
def f91ca_f91_semi_cycle_amplitude_rng_63d_curv_v077_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d rng
def f91ca_f91_semi_cycle_amplitude_rng_63d_curv_v078_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d rng
def f91ca_f91_semi_cycle_amplitude_rng_63d_curv_v079_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d rng
def f91ca_f91_semi_cycle_amplitude_rng_63d_curv_v080_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 63) - _min(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d rng
def f91ca_f91_semi_cycle_amplitude_rng_126d_curv_v081_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d rng
def f91ca_f91_semi_cycle_amplitude_rng_126d_curv_v082_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d rng
def f91ca_f91_semi_cycle_amplitude_rng_126d_curv_v083_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d rng
def f91ca_f91_semi_cycle_amplitude_rng_126d_curv_v084_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d rng
def f91ca_f91_semi_cycle_amplitude_rng_126d_curv_v085_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _max(x, 126) - _min(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d pos
def f91ca_f91_semi_cycle_amplitude_pos_126d_curv_v086_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d pos
def f91ca_f91_semi_cycle_amplitude_pos_126d_curv_v087_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d pos
def f91ca_f91_semi_cycle_amplitude_pos_126d_curv_v088_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d pos
def f91ca_f91_semi_cycle_amplitude_pos_126d_curv_v089_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d pos
def f91ca_f91_semi_cycle_amplitude_pos_126d_curv_v090_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d std
def f91ca_f91_semi_cycle_amplitude_std_63d_curv_v091_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d std
def f91ca_f91_semi_cycle_amplitude_std_63d_curv_v092_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d std
def f91ca_f91_semi_cycle_amplitude_std_63d_curv_v093_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d std
def f91ca_f91_semi_cycle_amplitude_std_63d_curv_v094_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d std
def f91ca_f91_semi_cycle_amplitude_std_63d_curv_v095_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d std
def f91ca_f91_semi_cycle_amplitude_std_126d_curv_v096_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d std
def f91ca_f91_semi_cycle_amplitude_std_126d_curv_v097_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d std
def f91ca_f91_semi_cycle_amplitude_std_126d_curv_v098_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d std
def f91ca_f91_semi_cycle_amplitude_std_126d_curv_v099_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d std
def f91ca_f91_semi_cycle_amplitude_std_126d_curv_v100_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d std
def f91ca_f91_semi_cycle_amplitude_std_252d_curv_v101_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d std
def f91ca_f91_semi_cycle_amplitude_std_252d_curv_v102_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d std
def f91ca_f91_semi_cycle_amplitude_std_252d_curv_v103_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d std
def f91ca_f91_semi_cycle_amplitude_std_252d_curv_v104_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d std
def f91ca_f91_semi_cycle_amplitude_std_252d_curv_v105_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = _std(x, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d hit
def f91ca_f91_semi_cycle_amplitude_hit_63d_curv_v106_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d hit
def f91ca_f91_semi_cycle_amplitude_hit_63d_curv_v107_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d hit
def f91ca_f91_semi_cycle_amplitude_hit_63d_curv_v108_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d hit
def f91ca_f91_semi_cycle_amplitude_hit_63d_curv_v109_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d hit
def f91ca_f91_semi_cycle_amplitude_hit_63d_curv_v110_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d hit
def f91ca_f91_semi_cycle_amplitude_hit_126d_curv_v111_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d hit
def f91ca_f91_semi_cycle_amplitude_hit_126d_curv_v112_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d hit
def f91ca_f91_semi_cycle_amplitude_hit_126d_curv_v113_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d hit
def f91ca_f91_semi_cycle_amplitude_hit_126d_curv_v114_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d hit
def f91ca_f91_semi_cycle_amplitude_hit_126d_curv_v115_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d signcum
def f91ca_f91_semi_cycle_amplitude_signcum_126d_curv_v116_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d signcum
def f91ca_f91_semi_cycle_amplitude_signcum_126d_curv_v117_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d signcum
def f91ca_f91_semi_cycle_amplitude_signcum_126d_curv_v118_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d signcum
def f91ca_f91_semi_cycle_amplitude_signcum_126d_curv_v119_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d signcum
def f91ca_f91_semi_cycle_amplitude_signcum_126d_curv_v120_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d cum
def f91ca_f91_semi_cycle_amplitude_cum_63d_curv_v121_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d cum
def f91ca_f91_semi_cycle_amplitude_cum_63d_curv_v122_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d cum
def f91ca_f91_semi_cycle_amplitude_cum_63d_curv_v123_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d cum
def f91ca_f91_semi_cycle_amplitude_cum_63d_curv_v124_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d cum
def f91ca_f91_semi_cycle_amplitude_cum_63d_curv_v125_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d cum
def f91ca_f91_semi_cycle_amplitude_cum_252d_curv_v126_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d cum
def f91ca_f91_semi_cycle_amplitude_cum_252d_curv_v127_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d cum
def f91ca_f91_semi_cycle_amplitude_cum_252d_curv_v128_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d cum
def f91ca_f91_semi_cycle_amplitude_cum_252d_curv_v129_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d cum
def f91ca_f91_semi_cycle_amplitude_cum_252d_curv_v130_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    base = x.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d condup
def f91ca_f91_semi_cycle_amplitude_condup_126d_curv_v131_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d condup
def f91ca_f91_semi_cycle_amplitude_condup_126d_curv_v132_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d condup
def f91ca_f91_semi_cycle_amplitude_condup_126d_curv_v133_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d condup
def f91ca_f91_semi_cycle_amplitude_condup_126d_curv_v134_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d condup
def f91ca_f91_semi_cycle_amplitude_condup_126d_curv_v135_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y > 0), 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d conddn
def f91ca_f91_semi_cycle_amplitude_conddn_126d_curv_v136_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d conddn
def f91ca_f91_semi_cycle_amplitude_conddn_126d_curv_v137_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d conddn
def f91ca_f91_semi_cycle_amplitude_conddn_126d_curv_v138_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d conddn
def f91ca_f91_semi_cycle_amplitude_conddn_126d_curv_v139_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d conddn
def f91ca_f91_semi_cycle_amplitude_conddn_126d_curv_v140_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x.where(y < 0), 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d corr
def f91ca_f91_semi_cycle_amplitude_corr_126d_curv_v141_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d corr
def f91ca_f91_semi_cycle_amplitude_corr_126d_curv_v142_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d corr
def f91ca_f91_semi_cycle_amplitude_corr_126d_curv_v143_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d corr
def f91ca_f91_semi_cycle_amplitude_corr_126d_curv_v144_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d corr
def f91ca_f91_semi_cycle_amplitude_corr_126d_curv_v145_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d ratio
def f91ca_f91_semi_cycle_amplitude_ratio_126d_curv_v146_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d ratio
def f91ca_f91_semi_cycle_amplitude_ratio_126d_curv_v147_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d ratio
def f91ca_f91_semi_cycle_amplitude_ratio_126d_curv_v148_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d ratio
def f91ca_f91_semi_cycle_amplitude_ratio_126d_curv_v149_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d ratio
def f91ca_f91_semi_cycle_amplitude_ratio_126d_curv_v150_signal(revenue, capex, closeadj):
    x = _f91ca_combined(revenue, capex, 252)
    y = _f91ca_rev_amp(revenue, 252)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
