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
def _f93mc_inv_rev(inv, rev):
    return inv / rev.replace(0, np.nan)


def _f93mc_inv_basket(inv, bas):
    return inv.pct_change(periods=63) - bas.pct_change(periods=63)


def _f93mc_memglut(inv, rev, bas):
    spike = (inv / rev.replace(0, np.nan)).pct_change(periods=63)
    bspike = bas.pct_change(periods=63)
    return spike - bspike


# 5d slope of 21d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_21d_slope_v001_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_21d_slope_v002_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_21d_slope_v003_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_21d_slope_v004_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_21d_slope_v005_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_63d_slope_v006_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_63d_slope_v007_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_63d_slope_v008_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_63d_slope_v009_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_63d_slope_v010_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_126d_slope_v011_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_126d_slope_v012_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_126d_slope_v013_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_126d_slope_v014_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_126d_slope_v015_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_252d_slope_v016_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_252d_slope_v017_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_252d_slope_v018_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_252d_slope_v019_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_252d_slope_v020_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_504d_slope_v021_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_504d_slope_v022_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_504d_slope_v023_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_504d_slope_v024_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d lvl
def f93mc_f93_semi_memory_cycle_proxy_lvl_504d_slope_v025_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z
def f93mc_f93_semi_memory_cycle_proxy_z_21d_slope_v026_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z
def f93mc_f93_semi_memory_cycle_proxy_z_21d_slope_v027_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z
def f93mc_f93_semi_memory_cycle_proxy_z_21d_slope_v028_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d z
def f93mc_f93_semi_memory_cycle_proxy_z_21d_slope_v029_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d z
def f93mc_f93_semi_memory_cycle_proxy_z_21d_slope_v030_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z
def f93mc_f93_semi_memory_cycle_proxy_z_63d_slope_v031_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z
def f93mc_f93_semi_memory_cycle_proxy_z_63d_slope_v032_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z
def f93mc_f93_semi_memory_cycle_proxy_z_63d_slope_v033_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d z
def f93mc_f93_semi_memory_cycle_proxy_z_63d_slope_v034_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d z
def f93mc_f93_semi_memory_cycle_proxy_z_63d_slope_v035_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z
def f93mc_f93_semi_memory_cycle_proxy_z_126d_slope_v036_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z
def f93mc_f93_semi_memory_cycle_proxy_z_126d_slope_v037_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z
def f93mc_f93_semi_memory_cycle_proxy_z_126d_slope_v038_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d z
def f93mc_f93_semi_memory_cycle_proxy_z_126d_slope_v039_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d z
def f93mc_f93_semi_memory_cycle_proxy_z_126d_slope_v040_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z
def f93mc_f93_semi_memory_cycle_proxy_z_252d_slope_v041_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z
def f93mc_f93_semi_memory_cycle_proxy_z_252d_slope_v042_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z
def f93mc_f93_semi_memory_cycle_proxy_z_252d_slope_v043_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d z
def f93mc_f93_semi_memory_cycle_proxy_z_252d_slope_v044_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d z
def f93mc_f93_semi_memory_cycle_proxy_z_252d_slope_v045_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z
def f93mc_f93_semi_memory_cycle_proxy_z_504d_slope_v046_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z
def f93mc_f93_semi_memory_cycle_proxy_z_504d_slope_v047_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z
def f93mc_f93_semi_memory_cycle_proxy_z_504d_slope_v048_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d z
def f93mc_f93_semi_memory_cycle_proxy_z_504d_slope_v049_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d z
def f93mc_f93_semi_memory_cycle_proxy_z_504d_slope_v050_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_63d_slope_v051_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_63d_slope_v052_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_63d_slope_v053_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_63d_slope_v054_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_63d_slope_v055_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_126d_slope_v056_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_126d_slope_v057_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_126d_slope_v058_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_126d_slope_v059_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_126d_slope_v060_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_252d_slope_v061_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_252d_slope_v062_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_252d_slope_v063_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_252d_slope_v064_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d dd
def f93mc_f93_semi_memory_cycle_proxy_dd_252d_slope_v065_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_63d_slope_v066_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_63d_slope_v067_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_63d_slope_v068_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_63d_slope_v069_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_63d_slope_v070_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_126d_slope_v071_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_126d_slope_v072_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_126d_slope_v073_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_126d_slope_v074_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d runup
def f93mc_f93_semi_memory_cycle_proxy_runup_126d_slope_v075_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_63d_slope_v076_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_63d_slope_v077_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_63d_slope_v078_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_63d_slope_v079_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_63d_slope_v080_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_126d_slope_v081_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_126d_slope_v082_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_126d_slope_v083_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_126d_slope_v084_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d rng
def f93mc_f93_semi_memory_cycle_proxy_rng_126d_slope_v085_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pos
def f93mc_f93_semi_memory_cycle_proxy_pos_126d_slope_v086_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pos
def f93mc_f93_semi_memory_cycle_proxy_pos_126d_slope_v087_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pos
def f93mc_f93_semi_memory_cycle_proxy_pos_126d_slope_v088_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d pos
def f93mc_f93_semi_memory_cycle_proxy_pos_126d_slope_v089_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d pos
def f93mc_f93_semi_memory_cycle_proxy_pos_126d_slope_v090_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d std
def f93mc_f93_semi_memory_cycle_proxy_std_63d_slope_v091_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d std
def f93mc_f93_semi_memory_cycle_proxy_std_63d_slope_v092_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d std
def f93mc_f93_semi_memory_cycle_proxy_std_63d_slope_v093_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d std
def f93mc_f93_semi_memory_cycle_proxy_std_63d_slope_v094_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d std
def f93mc_f93_semi_memory_cycle_proxy_std_63d_slope_v095_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d std
def f93mc_f93_semi_memory_cycle_proxy_std_126d_slope_v096_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d std
def f93mc_f93_semi_memory_cycle_proxy_std_126d_slope_v097_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d std
def f93mc_f93_semi_memory_cycle_proxy_std_126d_slope_v098_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d std
def f93mc_f93_semi_memory_cycle_proxy_std_126d_slope_v099_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d std
def f93mc_f93_semi_memory_cycle_proxy_std_126d_slope_v100_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d std
def f93mc_f93_semi_memory_cycle_proxy_std_252d_slope_v101_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d std
def f93mc_f93_semi_memory_cycle_proxy_std_252d_slope_v102_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d std
def f93mc_f93_semi_memory_cycle_proxy_std_252d_slope_v103_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d std
def f93mc_f93_semi_memory_cycle_proxy_std_252d_slope_v104_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d std
def f93mc_f93_semi_memory_cycle_proxy_std_252d_slope_v105_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_63d_slope_v106_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_63d_slope_v107_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_63d_slope_v108_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_63d_slope_v109_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_63d_slope_v110_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_126d_slope_v111_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_126d_slope_v112_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_126d_slope_v113_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_126d_slope_v114_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d hit
def f93mc_f93_semi_memory_cycle_proxy_hit_126d_slope_v115_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d signcum
def f93mc_f93_semi_memory_cycle_proxy_signcum_126d_slope_v116_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d signcum
def f93mc_f93_semi_memory_cycle_proxy_signcum_126d_slope_v117_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d signcum
def f93mc_f93_semi_memory_cycle_proxy_signcum_126d_slope_v118_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d signcum
def f93mc_f93_semi_memory_cycle_proxy_signcum_126d_slope_v119_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d signcum
def f93mc_f93_semi_memory_cycle_proxy_signcum_126d_slope_v120_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_63d_slope_v121_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_63d_slope_v122_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_63d_slope_v123_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_63d_slope_v124_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_63d_slope_v125_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_252d_slope_v126_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_252d_slope_v127_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_252d_slope_v128_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_252d_slope_v129_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cum
def f93mc_f93_semi_memory_cycle_proxy_cum_252d_slope_v130_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d condup
def f93mc_f93_semi_memory_cycle_proxy_condup_126d_slope_v131_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d condup
def f93mc_f93_semi_memory_cycle_proxy_condup_126d_slope_v132_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d condup
def f93mc_f93_semi_memory_cycle_proxy_condup_126d_slope_v133_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d condup
def f93mc_f93_semi_memory_cycle_proxy_condup_126d_slope_v134_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d condup
def f93mc_f93_semi_memory_cycle_proxy_condup_126d_slope_v135_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d conddn
def f93mc_f93_semi_memory_cycle_proxy_conddn_126d_slope_v136_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d conddn
def f93mc_f93_semi_memory_cycle_proxy_conddn_126d_slope_v137_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d conddn
def f93mc_f93_semi_memory_cycle_proxy_conddn_126d_slope_v138_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d conddn
def f93mc_f93_semi_memory_cycle_proxy_conddn_126d_slope_v139_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d conddn
def f93mc_f93_semi_memory_cycle_proxy_conddn_126d_slope_v140_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d corr
def f93mc_f93_semi_memory_cycle_proxy_corr_126d_slope_v141_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d corr
def f93mc_f93_semi_memory_cycle_proxy_corr_126d_slope_v142_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d corr
def f93mc_f93_semi_memory_cycle_proxy_corr_126d_slope_v143_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d corr
def f93mc_f93_semi_memory_cycle_proxy_corr_126d_slope_v144_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d corr
def f93mc_f93_semi_memory_cycle_proxy_corr_126d_slope_v145_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ratio
def f93mc_f93_semi_memory_cycle_proxy_ratio_126d_slope_v146_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ratio
def f93mc_f93_semi_memory_cycle_proxy_ratio_126d_slope_v147_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ratio
def f93mc_f93_semi_memory_cycle_proxy_ratio_126d_slope_v148_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d ratio
def f93mc_f93_semi_memory_cycle_proxy_ratio_126d_slope_v149_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d ratio
def f93mc_f93_semi_memory_cycle_proxy_ratio_126d_slope_v150_signal(inventory, revenue, semi_basket_inventory, closeadj):
    x = _f93mc_memglut(inventory, revenue, semi_basket_inventory)
    y = _f93mc_inv_rev(inventory, revenue)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
