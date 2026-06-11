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
def _f67_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f67_safe_pct(x, n):
    return x.pct_change(n)


def _f67_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f67_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 1)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v001_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 1)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v002_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 1)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v003_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 1)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v004_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 1)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v005_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 2)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v006_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 2)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v007_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 2)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v008_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 2)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v009_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 2)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v010_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 3)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v011_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 3)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v012_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 3)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v013_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 3)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v014_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 3)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v015_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 4)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v016_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 4)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v017_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 4)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v018_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 4)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v019_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 4)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v020_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 5)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v021_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 5)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v022_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 5)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v023_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 5)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v024_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 5)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v025_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 6)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v026_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 6)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v027_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 6)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v028_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 6)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v029_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 6)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v030_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 7)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v031_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 7)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v032_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 7)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v033_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 7)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v034_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 7)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v035_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 8)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v036_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 8)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v037_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 8)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v038_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 8)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v039_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 8)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v040_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 9)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v041_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 9)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v042_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 9)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v043_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 9)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v044_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 9)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v045_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 10)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v046_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 10)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v047_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 10)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v048_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 10)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v049_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 10)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v050_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 11)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v051_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 11)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v052_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 11)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v053_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 11)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v054_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 11)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v055_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 12)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v056_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 12)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v057_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 12)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v058_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 12)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v059_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 12)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v060_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 13)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v061_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 13)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v062_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 13)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v063_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 13)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v064_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 13)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v065_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 14)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v066_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 14)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v067_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 14)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v068_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 14)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v069_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 14)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v070_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 15)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v071_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 15)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v072_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 15)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v073_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 15)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v074_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 15)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v075_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 16)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v076_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 16)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v077_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 16)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v078_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 16)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v079_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 16)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v080_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 17)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v081_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 17)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v082_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 17)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v083_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 17)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v084_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 17)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v085_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 18)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v086_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 18)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v087_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 18)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v088_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 18)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v089_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 18)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v090_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 19)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v091_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 19)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v092_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 19)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v093_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 19)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v094_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 19)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v095_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 20)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v096_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 20)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v097_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 20)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v098_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 20)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v099_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 20)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v100_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 21)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v101_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 21)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v102_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 21)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v103_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 21)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v104_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 21)
def f67sb_f67_semi_sbc_burden_sb_21d_slope_v105_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 22)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v106_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 22)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v107_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 22)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v108_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 22)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v109_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 22)
def f67sb_f67_semi_sbc_burden_sb_63d_slope_v110_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 23)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v111_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 23)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v112_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 23)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v113_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 23)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v114_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 23)
def f67sb_f67_semi_sbc_burden_sb_126d_slope_v115_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 24)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v116_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 24)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v117_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 24)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v118_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 24)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v119_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 24)
def f67sb_f67_semi_sbc_burden_sb_252d_slope_v120_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 25)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v121_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 25)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v122_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 25)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v123_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 25)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v124_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 25)
def f67sb_f67_semi_sbc_burden_sb_504d_slope_v125_signal(sbcomp, revenue, fcf, closeadj):
    m = sbcomp / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 26)
def f67sb_f67_semi_sbc_burden_sb_fcf_21d_slope_v126_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 26)
def f67sb_f67_semi_sbc_burden_sb_fcf_21d_slope_v127_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 26)
def f67sb_f67_semi_sbc_burden_sb_fcf_21d_slope_v128_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 26)
def f67sb_f67_semi_sbc_burden_sb_fcf_21d_slope_v129_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 26)
def f67sb_f67_semi_sbc_burden_sb_fcf_21d_slope_v130_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 27)
def f67sb_f67_semi_sbc_burden_sb_fcf_63d_slope_v131_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 27)
def f67sb_f67_semi_sbc_burden_sb_fcf_63d_slope_v132_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 27)
def f67sb_f67_semi_sbc_burden_sb_fcf_63d_slope_v133_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 27)
def f67sb_f67_semi_sbc_burden_sb_fcf_63d_slope_v134_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 27)
def f67sb_f67_semi_sbc_burden_sb_fcf_63d_slope_v135_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 28)
def f67sb_f67_semi_sbc_burden_sb_fcf_126d_slope_v136_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 28)
def f67sb_f67_semi_sbc_burden_sb_fcf_126d_slope_v137_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 28)
def f67sb_f67_semi_sbc_burden_sb_fcf_126d_slope_v138_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 28)
def f67sb_f67_semi_sbc_burden_sb_fcf_126d_slope_v139_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 28)
def f67sb_f67_semi_sbc_burden_sb_fcf_126d_slope_v140_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 29)
def f67sb_f67_semi_sbc_burden_sb_fcf_252d_slope_v141_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 29)
def f67sb_f67_semi_sbc_burden_sb_fcf_252d_slope_v142_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 29)
def f67sb_f67_semi_sbc_burden_sb_fcf_252d_slope_v143_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 29)
def f67sb_f67_semi_sbc_burden_sb_fcf_252d_slope_v144_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 29)
def f67sb_f67_semi_sbc_burden_sb_fcf_252d_slope_v145_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 30)
def f67sb_f67_semi_sbc_burden_sb_fcf_504d_slope_v146_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 30)
def f67sb_f67_semi_sbc_burden_sb_fcf_504d_slope_v147_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 30)
def f67sb_f67_semi_sbc_burden_sb_fcf_504d_slope_v148_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 30)
def f67sb_f67_semi_sbc_burden_sb_fcf_504d_slope_v149_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d stock-based comp burden (sbcomp / revenue and sbcomp / fcf) (recipe 30)
def f67sb_f67_semi_sbc_burden_sb_fcf_504d_slope_v150_signal(sbcomp, revenue, fcf, closeadj):
    s2 = sbcomp / fcf.replace(0, np.nan)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
