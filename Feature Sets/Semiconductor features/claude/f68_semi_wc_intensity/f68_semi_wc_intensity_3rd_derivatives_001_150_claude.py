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
def _f68_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f68_safe_pct(x, n):
    return x.pct_change(n)


def _f68_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f68_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 1)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v001_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 1)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v002_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 1)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v003_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 1)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v004_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 1)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v005_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 2)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v006_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 2)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v007_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 2)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v008_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 2)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v009_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 2)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v010_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 3)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v011_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 3)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v012_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 3)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v013_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 3)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v014_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 3)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v015_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 4)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v016_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 4)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v017_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 4)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v018_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 4)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v019_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 4)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v020_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 5)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v021_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 5)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v022_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 5)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v023_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 5)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v024_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 5)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v025_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 6)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v026_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 6)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v027_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 6)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v028_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 6)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v029_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 6)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v030_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 7)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v031_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 7)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v032_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 7)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v033_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 7)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v034_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 7)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v035_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 8)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v036_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 8)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v037_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 8)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v038_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 8)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v039_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 8)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v040_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 9)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v041_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 9)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v042_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 9)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v043_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 9)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v044_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 9)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v045_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 10)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v046_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 10)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v047_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 10)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v048_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 10)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v049_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 10)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v050_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 11)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v051_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 11)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v052_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 11)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v053_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 11)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v054_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 11)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v055_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 12)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v056_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 12)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v057_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 12)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v058_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 12)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v059_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 12)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v060_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 13)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v061_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 13)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v062_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 13)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v063_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 13)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v064_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 13)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v065_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 14)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v066_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 14)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v067_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 14)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v068_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 14)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v069_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 14)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v070_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 15)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v071_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 15)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v072_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 15)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v073_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 15)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v074_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 15)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v075_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 16)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v076_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 16)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v077_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 16)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v078_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 16)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v079_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 16)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v080_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 17)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v081_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 17)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v082_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 17)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v083_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 17)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v084_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 17)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v085_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 18)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v086_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 18)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v087_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 18)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v088_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 18)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v089_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 18)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v090_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 19)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v091_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 19)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v092_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 19)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v093_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 19)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v094_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 19)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v095_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 20)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v096_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 20)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v097_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 20)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v098_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 20)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v099_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 20)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v100_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 21)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v101_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 21)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v102_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 21)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v103_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 21)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v104_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 21)
def f68wc_f68_semi_wc_intensity_wc_21d_curv_v105_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 22)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v106_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 22)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v107_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 22)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v108_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 22)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v109_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 22)
def f68wc_f68_semi_wc_intensity_wc_63d_curv_v110_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 23)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v111_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 23)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v112_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 23)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v113_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 23)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v114_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 23)
def f68wc_f68_semi_wc_intensity_wc_126d_curv_v115_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 24)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v116_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 24)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v117_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 24)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v118_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 24)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v119_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 24)
def f68wc_f68_semi_wc_intensity_wc_252d_curv_v120_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 25)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v121_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 25)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v122_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 25)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v123_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 25)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v124_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 25)
def f68wc_f68_semi_wc_intensity_wc_504d_curv_v125_signal(inventory, receivables, payables, revenue, closeadj):
    m = (inventory + receivables - payables) / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 26)
def f68wc_f68_semi_wc_intensity_inv_int_21d_curv_v126_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 26)
def f68wc_f68_semi_wc_intensity_inv_int_21d_curv_v127_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 26)
def f68wc_f68_semi_wc_intensity_inv_int_21d_curv_v128_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 26)
def f68wc_f68_semi_wc_intensity_inv_int_21d_curv_v129_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d working capital intensity ((inv + recv - pay) / revenue) (recipe 26)
def f68wc_f68_semi_wc_intensity_inv_int_21d_curv_v130_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 27)
def f68wc_f68_semi_wc_intensity_inv_int_63d_curv_v131_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 27)
def f68wc_f68_semi_wc_intensity_inv_int_63d_curv_v132_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 27)
def f68wc_f68_semi_wc_intensity_inv_int_63d_curv_v133_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 27)
def f68wc_f68_semi_wc_intensity_inv_int_63d_curv_v134_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d working capital intensity ((inv + recv - pay) / revenue) (recipe 27)
def f68wc_f68_semi_wc_intensity_inv_int_63d_curv_v135_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 28)
def f68wc_f68_semi_wc_intensity_inv_int_126d_curv_v136_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 28)
def f68wc_f68_semi_wc_intensity_inv_int_126d_curv_v137_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 28)
def f68wc_f68_semi_wc_intensity_inv_int_126d_curv_v138_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 28)
def f68wc_f68_semi_wc_intensity_inv_int_126d_curv_v139_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d working capital intensity ((inv + recv - pay) / revenue) (recipe 28)
def f68wc_f68_semi_wc_intensity_inv_int_126d_curv_v140_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 29)
def f68wc_f68_semi_wc_intensity_inv_int_252d_curv_v141_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 29)
def f68wc_f68_semi_wc_intensity_inv_int_252d_curv_v142_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 29)
def f68wc_f68_semi_wc_intensity_inv_int_252d_curv_v143_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 29)
def f68wc_f68_semi_wc_intensity_inv_int_252d_curv_v144_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d working capital intensity ((inv + recv - pay) / revenue) (recipe 29)
def f68wc_f68_semi_wc_intensity_inv_int_252d_curv_v145_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 30)
def f68wc_f68_semi_wc_intensity_inv_int_504d_curv_v146_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 30)
def f68wc_f68_semi_wc_intensity_inv_int_504d_curv_v147_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 30)
def f68wc_f68_semi_wc_intensity_inv_int_504d_curv_v148_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 30)
def f68wc_f68_semi_wc_intensity_inv_int_504d_curv_v149_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d working capital intensity ((inv + recv - pay) / revenue) (recipe 30)
def f68wc_f68_semi_wc_intensity_inv_int_504d_curv_v150_signal(inventory, receivables, payables, revenue, closeadj):
    s2 = inventory / revenue.replace(0, np.nan)
    base = _z(s2, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
