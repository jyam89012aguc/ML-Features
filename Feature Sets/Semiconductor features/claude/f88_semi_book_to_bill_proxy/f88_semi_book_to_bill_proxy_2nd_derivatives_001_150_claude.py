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
def _f88bb_recv_growth(s, n=63):
    return s.pct_change(periods=n)


def _f88bb_inv_growth(s, n=63):
    return s.pct_change(periods=n)


def _f88bb_book_bill(rcv, inv, n=63):
    return rcv.pct_change(periods=n) - inv.pct_change(periods=n)


def _f88bb_rev_growth(s, n=63):
    return s.pct_change(periods=n)


# 5d slope of 21d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_21d_slope_v001_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_21d_slope_v002_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_21d_slope_v003_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_21d_slope_v004_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_21d_slope_v005_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_63d_slope_v006_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_63d_slope_v007_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_63d_slope_v008_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_63d_slope_v009_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_63d_slope_v010_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_126d_slope_v011_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_126d_slope_v012_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_126d_slope_v013_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_126d_slope_v014_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_126d_slope_v015_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_252d_slope_v016_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_252d_slope_v017_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_252d_slope_v018_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_252d_slope_v019_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_252d_slope_v020_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_504d_slope_v021_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_504d_slope_v022_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_504d_slope_v023_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_504d_slope_v024_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d lvl
def f88bb_f88_semi_book_to_bill_proxy_lvl_504d_slope_v025_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _mean(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d z
def f88bb_f88_semi_book_to_bill_proxy_z_21d_slope_v026_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d z
def f88bb_f88_semi_book_to_bill_proxy_z_21d_slope_v027_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d z
def f88bb_f88_semi_book_to_bill_proxy_z_21d_slope_v028_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d z
def f88bb_f88_semi_book_to_bill_proxy_z_21d_slope_v029_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d z
def f88bb_f88_semi_book_to_bill_proxy_z_21d_slope_v030_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d z
def f88bb_f88_semi_book_to_bill_proxy_z_63d_slope_v031_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d z
def f88bb_f88_semi_book_to_bill_proxy_z_63d_slope_v032_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d z
def f88bb_f88_semi_book_to_bill_proxy_z_63d_slope_v033_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d z
def f88bb_f88_semi_book_to_bill_proxy_z_63d_slope_v034_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d z
def f88bb_f88_semi_book_to_bill_proxy_z_63d_slope_v035_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d z
def f88bb_f88_semi_book_to_bill_proxy_z_126d_slope_v036_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d z
def f88bb_f88_semi_book_to_bill_proxy_z_126d_slope_v037_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d z
def f88bb_f88_semi_book_to_bill_proxy_z_126d_slope_v038_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d z
def f88bb_f88_semi_book_to_bill_proxy_z_126d_slope_v039_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d z
def f88bb_f88_semi_book_to_bill_proxy_z_126d_slope_v040_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d z
def f88bb_f88_semi_book_to_bill_proxy_z_252d_slope_v041_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d z
def f88bb_f88_semi_book_to_bill_proxy_z_252d_slope_v042_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d z
def f88bb_f88_semi_book_to_bill_proxy_z_252d_slope_v043_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d z
def f88bb_f88_semi_book_to_bill_proxy_z_252d_slope_v044_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d z
def f88bb_f88_semi_book_to_bill_proxy_z_252d_slope_v045_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d z
def f88bb_f88_semi_book_to_bill_proxy_z_504d_slope_v046_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d z
def f88bb_f88_semi_book_to_bill_proxy_z_504d_slope_v047_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d z
def f88bb_f88_semi_book_to_bill_proxy_z_504d_slope_v048_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d z
def f88bb_f88_semi_book_to_bill_proxy_z_504d_slope_v049_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d z
def f88bb_f88_semi_book_to_bill_proxy_z_504d_slope_v050_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _z(x, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_63d_slope_v051_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_63d_slope_v052_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_63d_slope_v053_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_63d_slope_v054_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_63d_slope_v055_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_126d_slope_v056_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_126d_slope_v057_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_126d_slope_v058_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_126d_slope_v059_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_126d_slope_v060_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_252d_slope_v061_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_252d_slope_v062_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_252d_slope_v063_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_252d_slope_v064_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d dd
def f88bb_f88_semi_book_to_bill_proxy_dd_252d_slope_v065_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _max(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_63d_slope_v066_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_63d_slope_v067_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_63d_slope_v068_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_63d_slope_v069_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_63d_slope_v070_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_126d_slope_v071_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_126d_slope_v072_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_126d_slope_v073_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_126d_slope_v074_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d runup
def f88bb_f88_semi_book_to_bill_proxy_runup_126d_slope_v075_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_63d_slope_v076_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_63d_slope_v077_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_63d_slope_v078_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_63d_slope_v079_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_63d_slope_v080_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 63) - _min(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_126d_slope_v081_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_126d_slope_v082_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_126d_slope_v083_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_126d_slope_v084_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d rng
def f88bb_f88_semi_book_to_bill_proxy_rng_126d_slope_v085_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _max(x, 126) - _min(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d pos
def f88bb_f88_semi_book_to_bill_proxy_pos_126d_slope_v086_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d pos
def f88bb_f88_semi_book_to_bill_proxy_pos_126d_slope_v087_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d pos
def f88bb_f88_semi_book_to_bill_proxy_pos_126d_slope_v088_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d pos
def f88bb_f88_semi_book_to_bill_proxy_pos_126d_slope_v089_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d pos
def f88bb_f88_semi_book_to_bill_proxy_pos_126d_slope_v090_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    lo = _min(x, 126)
    hi = _max(x, 126)
    base = (x - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d std
def f88bb_f88_semi_book_to_bill_proxy_std_63d_slope_v091_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d std
def f88bb_f88_semi_book_to_bill_proxy_std_63d_slope_v092_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d std
def f88bb_f88_semi_book_to_bill_proxy_std_63d_slope_v093_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d std
def f88bb_f88_semi_book_to_bill_proxy_std_63d_slope_v094_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d std
def f88bb_f88_semi_book_to_bill_proxy_std_63d_slope_v095_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d std
def f88bb_f88_semi_book_to_bill_proxy_std_126d_slope_v096_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d std
def f88bb_f88_semi_book_to_bill_proxy_std_126d_slope_v097_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d std
def f88bb_f88_semi_book_to_bill_proxy_std_126d_slope_v098_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d std
def f88bb_f88_semi_book_to_bill_proxy_std_126d_slope_v099_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d std
def f88bb_f88_semi_book_to_bill_proxy_std_126d_slope_v100_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d std
def f88bb_f88_semi_book_to_bill_proxy_std_252d_slope_v101_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d std
def f88bb_f88_semi_book_to_bill_proxy_std_252d_slope_v102_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d std
def f88bb_f88_semi_book_to_bill_proxy_std_252d_slope_v103_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d std
def f88bb_f88_semi_book_to_bill_proxy_std_252d_slope_v104_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d std
def f88bb_f88_semi_book_to_bill_proxy_std_252d_slope_v105_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = _std(x, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_63d_slope_v106_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_63d_slope_v107_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_63d_slope_v108_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_63d_slope_v109_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_63d_slope_v110_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_126d_slope_v111_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_126d_slope_v112_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_126d_slope_v113_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_126d_slope_v114_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d hit
def f88bb_f88_semi_book_to_bill_proxy_hit_126d_slope_v115_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = (x > 0).astype(float).rolling(126, min_periods=63).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d signcum
def f88bb_f88_semi_book_to_bill_proxy_signcum_126d_slope_v116_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d signcum
def f88bb_f88_semi_book_to_bill_proxy_signcum_126d_slope_v117_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d signcum
def f88bb_f88_semi_book_to_bill_proxy_signcum_126d_slope_v118_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d signcum
def f88bb_f88_semi_book_to_bill_proxy_signcum_126d_slope_v119_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d signcum
def f88bb_f88_semi_book_to_bill_proxy_signcum_126d_slope_v120_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = pd.Series(np.sign(x), index=x.index).rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_63d_slope_v121_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_63d_slope_v122_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_63d_slope_v123_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_63d_slope_v124_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_63d_slope_v125_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(63, min_periods=32).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_252d_slope_v126_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_252d_slope_v127_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_252d_slope_v128_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_252d_slope_v129_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cum
def f88bb_f88_semi_book_to_bill_proxy_cum_252d_slope_v130_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    base = x.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d condup
def f88bb_f88_semi_book_to_bill_proxy_condup_126d_slope_v131_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d condup
def f88bb_f88_semi_book_to_bill_proxy_condup_126d_slope_v132_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d condup
def f88bb_f88_semi_book_to_bill_proxy_condup_126d_slope_v133_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d condup
def f88bb_f88_semi_book_to_bill_proxy_condup_126d_slope_v134_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d condup
def f88bb_f88_semi_book_to_bill_proxy_condup_126d_slope_v135_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y > 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d conddn
def f88bb_f88_semi_book_to_bill_proxy_conddn_126d_slope_v136_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d conddn
def f88bb_f88_semi_book_to_bill_proxy_conddn_126d_slope_v137_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d conddn
def f88bb_f88_semi_book_to_bill_proxy_conddn_126d_slope_v138_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d conddn
def f88bb_f88_semi_book_to_bill_proxy_conddn_126d_slope_v139_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d conddn
def f88bb_f88_semi_book_to_bill_proxy_conddn_126d_slope_v140_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x.where(y < 0), 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d corr
def f88bb_f88_semi_book_to_bill_proxy_corr_126d_slope_v141_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d corr
def f88bb_f88_semi_book_to_bill_proxy_corr_126d_slope_v142_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d corr
def f88bb_f88_semi_book_to_bill_proxy_corr_126d_slope_v143_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d corr
def f88bb_f88_semi_book_to_bill_proxy_corr_126d_slope_v144_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d corr
def f88bb_f88_semi_book_to_bill_proxy_corr_126d_slope_v145_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = x.rolling(126, min_periods=63).corr(y)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d ratio
def f88bb_f88_semi_book_to_bill_proxy_ratio_126d_slope_v146_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d ratio
def f88bb_f88_semi_book_to_bill_proxy_ratio_126d_slope_v147_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d ratio
def f88bb_f88_semi_book_to_bill_proxy_ratio_126d_slope_v148_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d ratio
def f88bb_f88_semi_book_to_bill_proxy_ratio_126d_slope_v149_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d ratio
def f88bb_f88_semi_book_to_bill_proxy_ratio_126d_slope_v150_signal(receivables, inventory, revenue, closeadj):
    x = _f88bb_book_bill(receivables, inventory, 63)
    y = _f88bb_rev_growth(revenue, 63)
    base = _mean(x, 126) / _mean(y, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
