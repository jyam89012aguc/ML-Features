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
def _f99li_litho(cx, pp):
    return cx / pp.replace(0, np.nan)


def _f99li_growth(s, n=63):
    return s.pct_change(periods=n)


def _f99li_growth_litho(cx, pp, n=63):
    return (cx / pp.replace(0, np.nan)).pct_change(periods=n)


# 5d slope of 21d lvl
def f99li_f99_semi_litho_intensity_lvl_21d_slope_v001_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d lvl
def f99li_f99_semi_litho_intensity_lvl_21d_slope_v002_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d lvl
def f99li_f99_semi_litho_intensity_lvl_21d_slope_v003_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d lvl
def f99li_f99_semi_litho_intensity_lvl_21d_slope_v004_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d lvl
def f99li_f99_semi_litho_intensity_lvl_21d_slope_v005_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d lvl
def f99li_f99_semi_litho_intensity_lvl_63d_slope_v006_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d lvl
def f99li_f99_semi_litho_intensity_lvl_63d_slope_v007_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d lvl
def f99li_f99_semi_litho_intensity_lvl_63d_slope_v008_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d lvl
def f99li_f99_semi_litho_intensity_lvl_63d_slope_v009_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d lvl
def f99li_f99_semi_litho_intensity_lvl_63d_slope_v010_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d lvl
def f99li_f99_semi_litho_intensity_lvl_126d_slope_v011_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d lvl
def f99li_f99_semi_litho_intensity_lvl_126d_slope_v012_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d lvl
def f99li_f99_semi_litho_intensity_lvl_126d_slope_v013_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d lvl
def f99li_f99_semi_litho_intensity_lvl_126d_slope_v014_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d lvl
def f99li_f99_semi_litho_intensity_lvl_126d_slope_v015_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d lvl
def f99li_f99_semi_litho_intensity_lvl_252d_slope_v016_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d lvl
def f99li_f99_semi_litho_intensity_lvl_252d_slope_v017_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d lvl
def f99li_f99_semi_litho_intensity_lvl_252d_slope_v018_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d lvl
def f99li_f99_semi_litho_intensity_lvl_252d_slope_v019_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d lvl
def f99li_f99_semi_litho_intensity_lvl_252d_slope_v020_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d lvl
def f99li_f99_semi_litho_intensity_lvl_504d_slope_v021_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d lvl
def f99li_f99_semi_litho_intensity_lvl_504d_slope_v022_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d lvl
def f99li_f99_semi_litho_intensity_lvl_504d_slope_v023_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d lvl
def f99li_f99_semi_litho_intensity_lvl_504d_slope_v024_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d lvl
def f99li_f99_semi_litho_intensity_lvl_504d_slope_v025_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z
def f99li_f99_semi_litho_intensity_z_21d_slope_v026_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z
def f99li_f99_semi_litho_intensity_z_21d_slope_v027_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z
def f99li_f99_semi_litho_intensity_z_21d_slope_v028_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d z
def f99li_f99_semi_litho_intensity_z_21d_slope_v029_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d z
def f99li_f99_semi_litho_intensity_z_21d_slope_v030_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z
def f99li_f99_semi_litho_intensity_z_63d_slope_v031_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z
def f99li_f99_semi_litho_intensity_z_63d_slope_v032_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z
def f99li_f99_semi_litho_intensity_z_63d_slope_v033_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d z
def f99li_f99_semi_litho_intensity_z_63d_slope_v034_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d z
def f99li_f99_semi_litho_intensity_z_63d_slope_v035_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z
def f99li_f99_semi_litho_intensity_z_126d_slope_v036_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z
def f99li_f99_semi_litho_intensity_z_126d_slope_v037_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z
def f99li_f99_semi_litho_intensity_z_126d_slope_v038_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d z
def f99li_f99_semi_litho_intensity_z_126d_slope_v039_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d z
def f99li_f99_semi_litho_intensity_z_126d_slope_v040_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z
def f99li_f99_semi_litho_intensity_z_252d_slope_v041_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z
def f99li_f99_semi_litho_intensity_z_252d_slope_v042_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z
def f99li_f99_semi_litho_intensity_z_252d_slope_v043_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d z
def f99li_f99_semi_litho_intensity_z_252d_slope_v044_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d z
def f99li_f99_semi_litho_intensity_z_252d_slope_v045_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z
def f99li_f99_semi_litho_intensity_z_504d_slope_v046_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z
def f99li_f99_semi_litho_intensity_z_504d_slope_v047_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z
def f99li_f99_semi_litho_intensity_z_504d_slope_v048_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d z
def f99li_f99_semi_litho_intensity_z_504d_slope_v049_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d z
def f99li_f99_semi_litho_intensity_z_504d_slope_v050_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dd
def f99li_f99_semi_litho_intensity_dd_63d_slope_v051_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dd
def f99li_f99_semi_litho_intensity_dd_63d_slope_v052_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dd
def f99li_f99_semi_litho_intensity_dd_63d_slope_v053_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d dd
def f99li_f99_semi_litho_intensity_dd_63d_slope_v054_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d dd
def f99li_f99_semi_litho_intensity_dd_63d_slope_v055_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dd
def f99li_f99_semi_litho_intensity_dd_126d_slope_v056_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dd
def f99li_f99_semi_litho_intensity_dd_126d_slope_v057_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dd
def f99li_f99_semi_litho_intensity_dd_126d_slope_v058_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d dd
def f99li_f99_semi_litho_intensity_dd_126d_slope_v059_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d dd
def f99li_f99_semi_litho_intensity_dd_126d_slope_v060_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dd
def f99li_f99_semi_litho_intensity_dd_252d_slope_v061_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dd
def f99li_f99_semi_litho_intensity_dd_252d_slope_v062_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dd
def f99li_f99_semi_litho_intensity_dd_252d_slope_v063_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d dd
def f99li_f99_semi_litho_intensity_dd_252d_slope_v064_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d dd
def f99li_f99_semi_litho_intensity_dd_252d_slope_v065_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d runup
def f99li_f99_semi_litho_intensity_runup_63d_slope_v066_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d runup
def f99li_f99_semi_litho_intensity_runup_63d_slope_v067_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d runup
def f99li_f99_semi_litho_intensity_runup_63d_slope_v068_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d runup
def f99li_f99_semi_litho_intensity_runup_63d_slope_v069_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d runup
def f99li_f99_semi_litho_intensity_runup_63d_slope_v070_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d runup
def f99li_f99_semi_litho_intensity_runup_126d_slope_v071_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d runup
def f99li_f99_semi_litho_intensity_runup_126d_slope_v072_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d runup
def f99li_f99_semi_litho_intensity_runup_126d_slope_v073_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d runup
def f99li_f99_semi_litho_intensity_runup_126d_slope_v074_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d runup
def f99li_f99_semi_litho_intensity_runup_126d_slope_v075_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rng
def f99li_f99_semi_litho_intensity_rng_63d_slope_v076_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rng
def f99li_f99_semi_litho_intensity_rng_63d_slope_v077_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rng
def f99li_f99_semi_litho_intensity_rng_63d_slope_v078_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d rng
def f99li_f99_semi_litho_intensity_rng_63d_slope_v079_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d rng
def f99li_f99_semi_litho_intensity_rng_63d_slope_v080_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rng
def f99li_f99_semi_litho_intensity_rng_126d_slope_v081_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rng
def f99li_f99_semi_litho_intensity_rng_126d_slope_v082_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rng
def f99li_f99_semi_litho_intensity_rng_126d_slope_v083_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d rng
def f99li_f99_semi_litho_intensity_rng_126d_slope_v084_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d rng
def f99li_f99_semi_litho_intensity_rng_126d_slope_v085_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pos
def f99li_f99_semi_litho_intensity_pos_126d_slope_v086_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pos
def f99li_f99_semi_litho_intensity_pos_126d_slope_v087_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pos
def f99li_f99_semi_litho_intensity_pos_126d_slope_v088_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d pos
def f99li_f99_semi_litho_intensity_pos_126d_slope_v089_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d pos
def f99li_f99_semi_litho_intensity_pos_126d_slope_v090_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d std
def f99li_f99_semi_litho_intensity_std_63d_slope_v091_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d std
def f99li_f99_semi_litho_intensity_std_63d_slope_v092_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d std
def f99li_f99_semi_litho_intensity_std_63d_slope_v093_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d std
def f99li_f99_semi_litho_intensity_std_63d_slope_v094_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d std
def f99li_f99_semi_litho_intensity_std_63d_slope_v095_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d std
def f99li_f99_semi_litho_intensity_std_126d_slope_v096_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d std
def f99li_f99_semi_litho_intensity_std_126d_slope_v097_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d std
def f99li_f99_semi_litho_intensity_std_126d_slope_v098_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d std
def f99li_f99_semi_litho_intensity_std_126d_slope_v099_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d std
def f99li_f99_semi_litho_intensity_std_126d_slope_v100_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d std
def f99li_f99_semi_litho_intensity_std_252d_slope_v101_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d std
def f99li_f99_semi_litho_intensity_std_252d_slope_v102_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d std
def f99li_f99_semi_litho_intensity_std_252d_slope_v103_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d std
def f99li_f99_semi_litho_intensity_std_252d_slope_v104_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d std
def f99li_f99_semi_litho_intensity_std_252d_slope_v105_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d hit
def f99li_f99_semi_litho_intensity_hit_63d_slope_v106_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d hit
def f99li_f99_semi_litho_intensity_hit_63d_slope_v107_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d hit
def f99li_f99_semi_litho_intensity_hit_63d_slope_v108_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d hit
def f99li_f99_semi_litho_intensity_hit_63d_slope_v109_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d hit
def f99li_f99_semi_litho_intensity_hit_63d_slope_v110_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d hit
def f99li_f99_semi_litho_intensity_hit_126d_slope_v111_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d hit
def f99li_f99_semi_litho_intensity_hit_126d_slope_v112_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d hit
def f99li_f99_semi_litho_intensity_hit_126d_slope_v113_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d hit
def f99li_f99_semi_litho_intensity_hit_126d_slope_v114_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d hit
def f99li_f99_semi_litho_intensity_hit_126d_slope_v115_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d signcum
def f99li_f99_semi_litho_intensity_signcum_126d_slope_v116_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d signcum
def f99li_f99_semi_litho_intensity_signcum_126d_slope_v117_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d signcum
def f99li_f99_semi_litho_intensity_signcum_126d_slope_v118_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d signcum
def f99li_f99_semi_litho_intensity_signcum_126d_slope_v119_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d signcum
def f99li_f99_semi_litho_intensity_signcum_126d_slope_v120_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cum
def f99li_f99_semi_litho_intensity_cum_63d_slope_v121_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cum
def f99li_f99_semi_litho_intensity_cum_63d_slope_v122_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cum
def f99li_f99_semi_litho_intensity_cum_63d_slope_v123_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cum
def f99li_f99_semi_litho_intensity_cum_63d_slope_v124_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cum
def f99li_f99_semi_litho_intensity_cum_63d_slope_v125_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cum
def f99li_f99_semi_litho_intensity_cum_252d_slope_v126_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cum
def f99li_f99_semi_litho_intensity_cum_252d_slope_v127_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cum
def f99li_f99_semi_litho_intensity_cum_252d_slope_v128_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cum
def f99li_f99_semi_litho_intensity_cum_252d_slope_v129_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cum
def f99li_f99_semi_litho_intensity_cum_252d_slope_v130_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d condup
def f99li_f99_semi_litho_intensity_condup_126d_slope_v131_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d condup
def f99li_f99_semi_litho_intensity_condup_126d_slope_v132_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d condup
def f99li_f99_semi_litho_intensity_condup_126d_slope_v133_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d condup
def f99li_f99_semi_litho_intensity_condup_126d_slope_v134_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d condup
def f99li_f99_semi_litho_intensity_condup_126d_slope_v135_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d conddn
def f99li_f99_semi_litho_intensity_conddn_126d_slope_v136_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d conddn
def f99li_f99_semi_litho_intensity_conddn_126d_slope_v137_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d conddn
def f99li_f99_semi_litho_intensity_conddn_126d_slope_v138_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d conddn
def f99li_f99_semi_litho_intensity_conddn_126d_slope_v139_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d conddn
def f99li_f99_semi_litho_intensity_conddn_126d_slope_v140_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d corr
def f99li_f99_semi_litho_intensity_corr_126d_slope_v141_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d corr
def f99li_f99_semi_litho_intensity_corr_126d_slope_v142_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d corr
def f99li_f99_semi_litho_intensity_corr_126d_slope_v143_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d corr
def f99li_f99_semi_litho_intensity_corr_126d_slope_v144_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d corr
def f99li_f99_semi_litho_intensity_corr_126d_slope_v145_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ratio
def f99li_f99_semi_litho_intensity_ratio_126d_slope_v146_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ratio
def f99li_f99_semi_litho_intensity_ratio_126d_slope_v147_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ratio
def f99li_f99_semi_litho_intensity_ratio_126d_slope_v148_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d ratio
def f99li_f99_semi_litho_intensity_ratio_126d_slope_v149_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d ratio
def f99li_f99_semi_litho_intensity_ratio_126d_slope_v150_signal(capex, ppne, closeadj):
    x = _f99li_litho(capex, ppne)
    y = _f99li_growth(capex, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
