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
def _f56_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f56_safe_pct(x, n):
    return x.pct_change(n)


def _f56_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f56_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d slope of 21d consecutive R&D YoY increase streak (recipe 1)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v001_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d consecutive R&D YoY increase streak (recipe 1)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v002_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d consecutive R&D YoY increase streak (recipe 1)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v003_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d consecutive R&D YoY increase streak (recipe 1)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v004_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d consecutive R&D YoY increase streak (recipe 1)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v005_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d consecutive R&D YoY increase streak (recipe 2)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v006_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d consecutive R&D YoY increase streak (recipe 2)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v007_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d consecutive R&D YoY increase streak (recipe 2)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v008_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d consecutive R&D YoY increase streak (recipe 2)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v009_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d consecutive R&D YoY increase streak (recipe 2)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v010_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d consecutive R&D YoY increase streak (recipe 3)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v011_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d consecutive R&D YoY increase streak (recipe 3)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v012_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d consecutive R&D YoY increase streak (recipe 3)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v013_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d consecutive R&D YoY increase streak (recipe 3)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v014_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d consecutive R&D YoY increase streak (recipe 3)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v015_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d consecutive R&D YoY increase streak (recipe 4)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v016_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d consecutive R&D YoY increase streak (recipe 4)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v017_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d consecutive R&D YoY increase streak (recipe 4)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v018_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d consecutive R&D YoY increase streak (recipe 4)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v019_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d consecutive R&D YoY increase streak (recipe 4)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v020_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d consecutive R&D YoY increase streak (recipe 5)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v021_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d consecutive R&D YoY increase streak (recipe 5)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v022_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d consecutive R&D YoY increase streak (recipe 5)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v023_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d consecutive R&D YoY increase streak (recipe 5)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v024_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d consecutive R&D YoY increase streak (recipe 5)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v025_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d consecutive R&D YoY increase streak (recipe 6)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v026_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d consecutive R&D YoY increase streak (recipe 6)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v027_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d consecutive R&D YoY increase streak (recipe 6)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v028_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d consecutive R&D YoY increase streak (recipe 6)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v029_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d consecutive R&D YoY increase streak (recipe 6)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v030_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d consecutive R&D YoY increase streak (recipe 7)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v031_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d consecutive R&D YoY increase streak (recipe 7)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v032_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d consecutive R&D YoY increase streak (recipe 7)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v033_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d consecutive R&D YoY increase streak (recipe 7)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v034_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d consecutive R&D YoY increase streak (recipe 7)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v035_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d consecutive R&D YoY increase streak (recipe 8)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v036_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d consecutive R&D YoY increase streak (recipe 8)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v037_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d consecutive R&D YoY increase streak (recipe 8)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v038_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d consecutive R&D YoY increase streak (recipe 8)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v039_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d consecutive R&D YoY increase streak (recipe 8)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v040_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d consecutive R&D YoY increase streak (recipe 9)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v041_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d consecutive R&D YoY increase streak (recipe 9)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v042_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d consecutive R&D YoY increase streak (recipe 9)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v043_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d consecutive R&D YoY increase streak (recipe 9)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v044_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d consecutive R&D YoY increase streak (recipe 9)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v045_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d consecutive R&D YoY increase streak (recipe 10)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v046_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d consecutive R&D YoY increase streak (recipe 10)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v047_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d consecutive R&D YoY increase streak (recipe 10)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v048_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d consecutive R&D YoY increase streak (recipe 10)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v049_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d consecutive R&D YoY increase streak (recipe 10)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v050_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d consecutive R&D YoY increase streak (recipe 11)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v051_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d consecutive R&D YoY increase streak (recipe 11)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v052_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d consecutive R&D YoY increase streak (recipe 11)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v053_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d consecutive R&D YoY increase streak (recipe 11)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v054_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d consecutive R&D YoY increase streak (recipe 11)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v055_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d consecutive R&D YoY increase streak (recipe 12)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v056_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d consecutive R&D YoY increase streak (recipe 12)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v057_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d consecutive R&D YoY increase streak (recipe 12)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v058_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d consecutive R&D YoY increase streak (recipe 12)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v059_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d consecutive R&D YoY increase streak (recipe 12)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v060_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d consecutive R&D YoY increase streak (recipe 13)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v061_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d consecutive R&D YoY increase streak (recipe 13)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v062_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d consecutive R&D YoY increase streak (recipe 13)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v063_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d consecutive R&D YoY increase streak (recipe 13)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v064_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d consecutive R&D YoY increase streak (recipe 13)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v065_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d consecutive R&D YoY increase streak (recipe 14)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v066_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d consecutive R&D YoY increase streak (recipe 14)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v067_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d consecutive R&D YoY increase streak (recipe 14)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v068_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d consecutive R&D YoY increase streak (recipe 14)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v069_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d consecutive R&D YoY increase streak (recipe 14)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v070_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d consecutive R&D YoY increase streak (recipe 15)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v071_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d consecutive R&D YoY increase streak (recipe 15)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v072_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d consecutive R&D YoY increase streak (recipe 15)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v073_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d consecutive R&D YoY increase streak (recipe 15)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v074_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d consecutive R&D YoY increase streak (recipe 15)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v075_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d consecutive R&D YoY increase streak (recipe 16)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v076_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d consecutive R&D YoY increase streak (recipe 16)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v077_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d consecutive R&D YoY increase streak (recipe 16)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v078_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d consecutive R&D YoY increase streak (recipe 16)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v079_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d consecutive R&D YoY increase streak (recipe 16)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v080_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d consecutive R&D YoY increase streak (recipe 17)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v081_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d consecutive R&D YoY increase streak (recipe 17)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v082_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d consecutive R&D YoY increase streak (recipe 17)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v083_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d consecutive R&D YoY increase streak (recipe 17)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v084_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d consecutive R&D YoY increase streak (recipe 17)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v085_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d consecutive R&D YoY increase streak (recipe 18)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v086_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d consecutive R&D YoY increase streak (recipe 18)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v087_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d consecutive R&D YoY increase streak (recipe 18)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v088_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d consecutive R&D YoY increase streak (recipe 18)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v089_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d consecutive R&D YoY increase streak (recipe 18)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v090_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d consecutive R&D YoY increase streak (recipe 19)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v091_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d consecutive R&D YoY increase streak (recipe 19)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v092_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d consecutive R&D YoY increase streak (recipe 19)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v093_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d consecutive R&D YoY increase streak (recipe 19)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v094_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d consecutive R&D YoY increase streak (recipe 19)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v095_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d consecutive R&D YoY increase streak (recipe 20)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v096_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d consecutive R&D YoY increase streak (recipe 20)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v097_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d consecutive R&D YoY increase streak (recipe 20)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v098_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d consecutive R&D YoY increase streak (recipe 20)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v099_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d consecutive R&D YoY increase streak (recipe 20)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v100_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d consecutive R&D YoY increase streak (recipe 21)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v101_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d consecutive R&D YoY increase streak (recipe 21)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v102_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d consecutive R&D YoY increase streak (recipe 21)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v103_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d consecutive R&D YoY increase streak (recipe 21)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v104_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d consecutive R&D YoY increase streak (recipe 21)
def f56rdg_f56_semi_rd_growth_streak_rdg_21d_slope_v105_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d consecutive R&D YoY increase streak (recipe 22)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v106_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d consecutive R&D YoY increase streak (recipe 22)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v107_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d consecutive R&D YoY increase streak (recipe 22)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v108_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d consecutive R&D YoY increase streak (recipe 22)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v109_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d consecutive R&D YoY increase streak (recipe 22)
def f56rdg_f56_semi_rd_growth_streak_rdg_63d_slope_v110_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d consecutive R&D YoY increase streak (recipe 23)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v111_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d consecutive R&D YoY increase streak (recipe 23)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v112_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d consecutive R&D YoY increase streak (recipe 23)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v113_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d consecutive R&D YoY increase streak (recipe 23)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v114_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d consecutive R&D YoY increase streak (recipe 23)
def f56rdg_f56_semi_rd_growth_streak_rdg_126d_slope_v115_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d consecutive R&D YoY increase streak (recipe 24)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v116_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d consecutive R&D YoY increase streak (recipe 24)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v117_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d consecutive R&D YoY increase streak (recipe 24)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v118_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d consecutive R&D YoY increase streak (recipe 24)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v119_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d consecutive R&D YoY increase streak (recipe 24)
def f56rdg_f56_semi_rd_growth_streak_rdg_252d_slope_v120_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d consecutive R&D YoY increase streak (recipe 25)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v121_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d consecutive R&D YoY increase streak (recipe 25)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v122_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d consecutive R&D YoY increase streak (recipe 25)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v123_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d consecutive R&D YoY increase streak (recipe 25)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v124_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d consecutive R&D YoY increase streak (recipe 25)
def f56rdg_f56_semi_rd_growth_streak_rdg_504d_slope_v125_signal(rnd, closeadj):
    m = rnd.pct_change(252)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d consecutive R&D YoY increase streak (recipe 26)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_21d_slope_v126_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d consecutive R&D YoY increase streak (recipe 26)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_21d_slope_v127_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d consecutive R&D YoY increase streak (recipe 26)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_21d_slope_v128_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d consecutive R&D YoY increase streak (recipe 26)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_21d_slope_v129_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d consecutive R&D YoY increase streak (recipe 26)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_21d_slope_v130_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d consecutive R&D YoY increase streak (recipe 27)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_63d_slope_v131_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d consecutive R&D YoY increase streak (recipe 27)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_63d_slope_v132_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d consecutive R&D YoY increase streak (recipe 27)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_63d_slope_v133_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d consecutive R&D YoY increase streak (recipe 27)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_63d_slope_v134_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d consecutive R&D YoY increase streak (recipe 27)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_63d_slope_v135_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d consecutive R&D YoY increase streak (recipe 28)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_126d_slope_v136_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d consecutive R&D YoY increase streak (recipe 28)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_126d_slope_v137_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d consecutive R&D YoY increase streak (recipe 28)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_126d_slope_v138_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d consecutive R&D YoY increase streak (recipe 28)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_126d_slope_v139_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d consecutive R&D YoY increase streak (recipe 28)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_126d_slope_v140_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d consecutive R&D YoY increase streak (recipe 29)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_252d_slope_v141_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d consecutive R&D YoY increase streak (recipe 29)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_252d_slope_v142_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d consecutive R&D YoY increase streak (recipe 29)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_252d_slope_v143_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d consecutive R&D YoY increase streak (recipe 29)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_252d_slope_v144_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d consecutive R&D YoY increase streak (recipe 29)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_252d_slope_v145_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d consecutive R&D YoY increase streak (recipe 30)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_504d_slope_v146_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d consecutive R&D YoY increase streak (recipe 30)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_504d_slope_v147_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d consecutive R&D YoY increase streak (recipe 30)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_504d_slope_v148_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d consecutive R&D YoY increase streak (recipe 30)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_504d_slope_v149_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d consecutive R&D YoY increase streak (recipe 30)
def f56rdg_f56_semi_rd_growth_streak_rd_lvl_504d_slope_v150_signal(rnd, closeadj):
    s2 = rnd
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
