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
def _f61_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f61_safe_pct(x, n):
    return x.pct_change(n)


def _f61_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f61_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d curv of 21d R&D / gross profit (recipe 1)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v001_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d R&D / gross profit (recipe 1)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v002_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d R&D / gross profit (recipe 1)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v003_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d R&D / gross profit (recipe 1)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v004_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d R&D / gross profit (recipe 1)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v005_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d R&D / gross profit (recipe 2)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v006_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d R&D / gross profit (recipe 2)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v007_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d R&D / gross profit (recipe 2)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v008_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d R&D / gross profit (recipe 2)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v009_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d R&D / gross profit (recipe 2)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v010_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d R&D / gross profit (recipe 3)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v011_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d R&D / gross profit (recipe 3)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v012_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d R&D / gross profit (recipe 3)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v013_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d R&D / gross profit (recipe 3)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v014_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d R&D / gross profit (recipe 3)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v015_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d R&D / gross profit (recipe 4)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v016_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d R&D / gross profit (recipe 4)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v017_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d R&D / gross profit (recipe 4)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v018_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d R&D / gross profit (recipe 4)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v019_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d R&D / gross profit (recipe 4)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v020_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d R&D / gross profit (recipe 5)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v021_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d R&D / gross profit (recipe 5)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v022_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d R&D / gross profit (recipe 5)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v023_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d R&D / gross profit (recipe 5)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v024_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d R&D / gross profit (recipe 5)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v025_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d R&D / gross profit (recipe 6)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v026_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d R&D / gross profit (recipe 6)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v027_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d R&D / gross profit (recipe 6)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v028_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d R&D / gross profit (recipe 6)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v029_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d R&D / gross profit (recipe 6)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v030_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d R&D / gross profit (recipe 7)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v031_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d R&D / gross profit (recipe 7)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v032_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d R&D / gross profit (recipe 7)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v033_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d R&D / gross profit (recipe 7)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v034_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d R&D / gross profit (recipe 7)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v035_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d R&D / gross profit (recipe 8)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v036_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d R&D / gross profit (recipe 8)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v037_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d R&D / gross profit (recipe 8)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v038_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d R&D / gross profit (recipe 8)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v039_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d R&D / gross profit (recipe 8)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v040_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d R&D / gross profit (recipe 9)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v041_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d R&D / gross profit (recipe 9)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v042_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d R&D / gross profit (recipe 9)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v043_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d R&D / gross profit (recipe 9)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v044_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d R&D / gross profit (recipe 9)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v045_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d R&D / gross profit (recipe 10)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v046_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d R&D / gross profit (recipe 10)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v047_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d R&D / gross profit (recipe 10)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v048_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d R&D / gross profit (recipe 10)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v049_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d R&D / gross profit (recipe 10)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v050_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d R&D / gross profit (recipe 11)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v051_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d R&D / gross profit (recipe 11)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v052_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d R&D / gross profit (recipe 11)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v053_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d R&D / gross profit (recipe 11)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v054_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d R&D / gross profit (recipe 11)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v055_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d R&D / gross profit (recipe 12)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v056_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d R&D / gross profit (recipe 12)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v057_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d R&D / gross profit (recipe 12)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v058_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d R&D / gross profit (recipe 12)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v059_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d R&D / gross profit (recipe 12)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v060_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d R&D / gross profit (recipe 13)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v061_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d R&D / gross profit (recipe 13)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v062_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d R&D / gross profit (recipe 13)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v063_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d R&D / gross profit (recipe 13)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v064_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d R&D / gross profit (recipe 13)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v065_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d R&D / gross profit (recipe 14)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v066_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d R&D / gross profit (recipe 14)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v067_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d R&D / gross profit (recipe 14)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v068_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d R&D / gross profit (recipe 14)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v069_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d R&D / gross profit (recipe 14)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v070_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d R&D / gross profit (recipe 15)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v071_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d R&D / gross profit (recipe 15)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v072_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d R&D / gross profit (recipe 15)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v073_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d R&D / gross profit (recipe 15)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v074_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d R&D / gross profit (recipe 15)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v075_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d R&D / gross profit (recipe 16)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v076_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d R&D / gross profit (recipe 16)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v077_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d R&D / gross profit (recipe 16)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v078_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d R&D / gross profit (recipe 16)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v079_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d R&D / gross profit (recipe 16)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v080_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d R&D / gross profit (recipe 17)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v081_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d R&D / gross profit (recipe 17)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v082_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d R&D / gross profit (recipe 17)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v083_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d R&D / gross profit (recipe 17)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v084_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d R&D / gross profit (recipe 17)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v085_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d R&D / gross profit (recipe 18)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v086_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d R&D / gross profit (recipe 18)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v087_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d R&D / gross profit (recipe 18)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v088_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d R&D / gross profit (recipe 18)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v089_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d R&D / gross profit (recipe 18)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v090_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d R&D / gross profit (recipe 19)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v091_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d R&D / gross profit (recipe 19)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v092_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d R&D / gross profit (recipe 19)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v093_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d R&D / gross profit (recipe 19)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v094_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d R&D / gross profit (recipe 19)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v095_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d R&D / gross profit (recipe 20)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v096_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d R&D / gross profit (recipe 20)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v097_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d R&D / gross profit (recipe 20)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v098_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d R&D / gross profit (recipe 20)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v099_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d R&D / gross profit (recipe 20)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v100_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d R&D / gross profit (recipe 21)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v101_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d R&D / gross profit (recipe 21)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v102_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d R&D / gross profit (recipe 21)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v103_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d R&D / gross profit (recipe 21)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v104_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d R&D / gross profit (recipe 21)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_21d_curv_v105_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d R&D / gross profit (recipe 22)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v106_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d R&D / gross profit (recipe 22)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v107_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d R&D / gross profit (recipe 22)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v108_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d R&D / gross profit (recipe 22)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v109_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d R&D / gross profit (recipe 22)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_63d_curv_v110_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d R&D / gross profit (recipe 23)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v111_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d R&D / gross profit (recipe 23)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v112_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d R&D / gross profit (recipe 23)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v113_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d R&D / gross profit (recipe 23)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v114_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d R&D / gross profit (recipe 23)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_126d_curv_v115_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d R&D / gross profit (recipe 24)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v116_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d R&D / gross profit (recipe 24)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v117_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d R&D / gross profit (recipe 24)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v118_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d R&D / gross profit (recipe 24)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v119_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d R&D / gross profit (recipe 24)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_252d_curv_v120_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d R&D / gross profit (recipe 25)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v121_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d R&D / gross profit (recipe 25)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v122_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d R&D / gross profit (recipe 25)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v123_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d R&D / gross profit (recipe 25)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v124_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d R&D / gross profit (recipe 25)
def f61rdgp_f61_semi_rd_to_gross_profit_rdgp_504d_curv_v125_signal(rnd, gp, closeadj):
    m = rnd / gp.replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d R&D / gross profit (recipe 26)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_21d_curv_v126_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d R&D / gross profit (recipe 26)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_21d_curv_v127_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d R&D / gross profit (recipe 26)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_21d_curv_v128_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d R&D / gross profit (recipe 26)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_21d_curv_v129_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d R&D / gross profit (recipe 26)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_21d_curv_v130_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d R&D / gross profit (recipe 27)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_63d_curv_v131_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d R&D / gross profit (recipe 27)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_63d_curv_v132_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d R&D / gross profit (recipe 27)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_63d_curv_v133_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d R&D / gross profit (recipe 27)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_63d_curv_v134_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d R&D / gross profit (recipe 27)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_63d_curv_v135_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d R&D / gross profit (recipe 28)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_126d_curv_v136_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d R&D / gross profit (recipe 28)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_126d_curv_v137_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d R&D / gross profit (recipe 28)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_126d_curv_v138_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d R&D / gross profit (recipe 28)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_126d_curv_v139_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d R&D / gross profit (recipe 28)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_126d_curv_v140_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d R&D / gross profit (recipe 29)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_252d_curv_v141_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d R&D / gross profit (recipe 29)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_252d_curv_v142_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d R&D / gross profit (recipe 29)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_252d_curv_v143_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d R&D / gross profit (recipe 29)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_252d_curv_v144_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d R&D / gross profit (recipe 29)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_252d_curv_v145_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d R&D / gross profit (recipe 30)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_504d_curv_v146_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d R&D / gross profit (recipe 30)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_504d_curv_v147_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d R&D / gross profit (recipe 30)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_504d_curv_v148_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d R&D / gross profit (recipe 30)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_504d_curv_v149_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d R&D / gross profit (recipe 30)
def f61rdgp_f61_semi_rd_to_gross_profit_gp_lvl_504d_curv_v150_signal(rnd, gp, closeadj):
    s2 = gp
    base = _z(s2, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
