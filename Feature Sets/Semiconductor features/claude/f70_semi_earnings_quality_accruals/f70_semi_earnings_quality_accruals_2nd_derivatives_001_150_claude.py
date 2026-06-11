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
def _f70_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f70_safe_pct(x, n):
    return x.pct_change(n)


def _f70_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f70_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 1)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v001_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 1)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v002_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 1)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v003_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 1)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v004_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 1)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v005_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 2)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v006_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 2)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v007_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 2)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v008_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 2)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v009_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 2)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v010_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 3)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v011_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 3)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v012_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 3)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v013_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 3)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v014_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 3)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v015_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 4)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v016_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 4)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v017_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 4)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v018_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 4)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v019_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 4)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v020_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 5)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v021_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 5)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v022_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 5)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v023_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 5)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v024_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 5)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v025_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 6)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v026_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 6)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v027_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 6)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v028_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 6)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v029_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 6)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v030_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 7)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v031_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 7)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v032_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 7)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v033_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 7)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v034_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 7)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v035_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 8)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v036_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 8)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v037_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 8)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v038_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 8)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v039_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 8)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v040_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 9)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v041_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 9)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v042_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 9)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v043_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 9)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v044_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 9)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v045_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 10)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v046_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 10)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v047_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 10)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v048_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 10)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v049_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 10)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v050_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 11)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v051_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 11)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v052_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 11)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v053_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 11)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v054_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 11)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v055_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 12)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v056_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 12)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v057_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 12)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v058_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 12)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v059_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 12)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v060_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 13)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v061_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 13)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v062_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 13)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v063_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 13)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v064_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 13)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v065_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 14)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v066_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 14)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v067_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 14)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v068_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 14)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v069_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 14)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v070_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 15)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v071_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 15)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v072_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 15)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v073_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 15)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v074_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 15)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v075_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 16)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v076_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 16)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v077_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 16)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v078_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 16)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v079_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 16)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v080_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 17)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v081_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 17)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v082_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 17)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v083_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 17)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v084_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 17)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v085_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 18)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v086_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 18)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v087_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 18)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v088_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 18)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v089_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 18)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v090_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 19)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v091_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 19)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v092_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 19)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v093_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 19)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v094_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 19)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v095_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 20)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v096_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 20)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v097_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 20)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v098_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 20)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v099_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 20)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v100_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 21)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v101_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 21)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v102_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 21)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v103_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 21)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v104_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 21)
def f70ea_f70_semi_earnings_quality_accruals_ea_21d_slope_v105_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 22)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v106_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 22)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v107_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 22)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v108_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 22)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v109_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 22)
def f70ea_f70_semi_earnings_quality_accruals_ea_63d_slope_v110_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 23)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v111_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 23)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v112_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 23)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v113_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 23)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v114_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 23)
def f70ea_f70_semi_earnings_quality_accruals_ea_126d_slope_v115_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 24)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v116_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 24)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v117_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 24)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v118_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 24)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v119_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 24)
def f70ea_f70_semi_earnings_quality_accruals_ea_252d_slope_v120_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 25)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v121_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 25)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v122_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 25)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v123_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 25)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v124_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 25)
def f70ea_f70_semi_earnings_quality_accruals_ea_504d_slope_v125_signal(netinc, ocf, assets, closeadj):
    m = (netinc - ocf) / assets.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 26)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_slope_v126_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 26)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_slope_v127_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 26)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_slope_v128_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 26)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_slope_v129_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d earnings quality / accruals ((netinc - ocf) / assets) (recipe 26)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_21d_slope_v130_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 27)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_slope_v131_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 27)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_slope_v132_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 27)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_slope_v133_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 27)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_slope_v134_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d earnings quality / accruals ((netinc - ocf) / assets) (recipe 27)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_63d_slope_v135_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 28)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_slope_v136_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 28)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_slope_v137_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 28)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_slope_v138_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 28)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_slope_v139_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d earnings quality / accruals ((netinc - ocf) / assets) (recipe 28)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_126d_slope_v140_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 29)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_slope_v141_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 29)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_slope_v142_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 29)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_slope_v143_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 29)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_slope_v144_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d earnings quality / accruals ((netinc - ocf) / assets) (recipe 29)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_252d_slope_v145_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 30)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_slope_v146_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 30)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_slope_v147_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 30)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_slope_v148_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 30)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_slope_v149_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d earnings quality / accruals ((netinc - ocf) / assets) (recipe 30)
def f70ea_f70_semi_earnings_quality_accruals_ni_oc_504d_slope_v150_signal(netinc, ocf, assets, closeadj):
    s2 = (netinc - ocf)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
