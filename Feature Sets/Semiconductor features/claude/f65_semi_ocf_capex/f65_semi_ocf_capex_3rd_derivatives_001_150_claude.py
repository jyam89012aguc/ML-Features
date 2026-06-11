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
def _f65_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f65_safe_pct(x, n):
    return x.pct_change(n)


def _f65_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f65_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d curv of 21d operating CF / capex coverage (recipe 1)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v001_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d operating CF / capex coverage (recipe 1)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v002_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d operating CF / capex coverage (recipe 1)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v003_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d operating CF / capex coverage (recipe 1)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v004_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d operating CF / capex coverage (recipe 1)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v005_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d operating CF / capex coverage (recipe 2)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v006_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d operating CF / capex coverage (recipe 2)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v007_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d operating CF / capex coverage (recipe 2)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v008_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d operating CF / capex coverage (recipe 2)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v009_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d operating CF / capex coverage (recipe 2)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v010_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d operating CF / capex coverage (recipe 3)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v011_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d operating CF / capex coverage (recipe 3)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v012_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d operating CF / capex coverage (recipe 3)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v013_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d operating CF / capex coverage (recipe 3)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v014_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d operating CF / capex coverage (recipe 3)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v015_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d operating CF / capex coverage (recipe 4)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v016_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d operating CF / capex coverage (recipe 4)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v017_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d operating CF / capex coverage (recipe 4)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v018_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d operating CF / capex coverage (recipe 4)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v019_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d operating CF / capex coverage (recipe 4)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v020_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d operating CF / capex coverage (recipe 5)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v021_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d operating CF / capex coverage (recipe 5)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v022_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d operating CF / capex coverage (recipe 5)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v023_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d operating CF / capex coverage (recipe 5)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v024_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d operating CF / capex coverage (recipe 5)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v025_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d operating CF / capex coverage (recipe 6)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v026_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d operating CF / capex coverage (recipe 6)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v027_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d operating CF / capex coverage (recipe 6)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v028_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d operating CF / capex coverage (recipe 6)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v029_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d operating CF / capex coverage (recipe 6)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v030_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d operating CF / capex coverage (recipe 7)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v031_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d operating CF / capex coverage (recipe 7)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v032_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d operating CF / capex coverage (recipe 7)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v033_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d operating CF / capex coverage (recipe 7)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v034_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d operating CF / capex coverage (recipe 7)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v035_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d operating CF / capex coverage (recipe 8)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v036_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d operating CF / capex coverage (recipe 8)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v037_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d operating CF / capex coverage (recipe 8)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v038_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d operating CF / capex coverage (recipe 8)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v039_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d operating CF / capex coverage (recipe 8)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v040_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d operating CF / capex coverage (recipe 9)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v041_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d operating CF / capex coverage (recipe 9)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v042_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d operating CF / capex coverage (recipe 9)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v043_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d operating CF / capex coverage (recipe 9)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v044_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d operating CF / capex coverage (recipe 9)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v045_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d operating CF / capex coverage (recipe 10)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v046_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d operating CF / capex coverage (recipe 10)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v047_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d operating CF / capex coverage (recipe 10)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v048_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d operating CF / capex coverage (recipe 10)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v049_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d operating CF / capex coverage (recipe 10)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v050_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _z(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d operating CF / capex coverage (recipe 11)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v051_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d operating CF / capex coverage (recipe 11)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v052_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d operating CF / capex coverage (recipe 11)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v053_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d operating CF / capex coverage (recipe 11)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v054_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d operating CF / capex coverage (recipe 11)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v055_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d operating CF / capex coverage (recipe 12)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v056_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d operating CF / capex coverage (recipe 12)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v057_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d operating CF / capex coverage (recipe 12)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v058_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d operating CF / capex coverage (recipe 12)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v059_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d operating CF / capex coverage (recipe 12)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v060_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d operating CF / capex coverage (recipe 13)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v061_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d operating CF / capex coverage (recipe 13)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v062_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d operating CF / capex coverage (recipe 13)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v063_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d operating CF / capex coverage (recipe 13)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v064_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d operating CF / capex coverage (recipe 13)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v065_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d operating CF / capex coverage (recipe 14)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v066_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d operating CF / capex coverage (recipe 14)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v067_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d operating CF / capex coverage (recipe 14)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v068_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d operating CF / capex coverage (recipe 14)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v069_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d operating CF / capex coverage (recipe 14)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v070_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d operating CF / capex coverage (recipe 15)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v071_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d operating CF / capex coverage (recipe 15)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v072_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d operating CF / capex coverage (recipe 15)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v073_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d operating CF / capex coverage (recipe 15)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v074_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d operating CF / capex coverage (recipe 15)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v075_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = _std(m, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d operating CF / capex coverage (recipe 16)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v076_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d operating CF / capex coverage (recipe 16)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v077_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d operating CF / capex coverage (recipe 16)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v078_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d operating CF / capex coverage (recipe 16)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v079_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d operating CF / capex coverage (recipe 16)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v080_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d operating CF / capex coverage (recipe 17)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v081_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d operating CF / capex coverage (recipe 17)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v082_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d operating CF / capex coverage (recipe 17)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v083_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d operating CF / capex coverage (recipe 17)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v084_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d operating CF / capex coverage (recipe 17)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v085_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d operating CF / capex coverage (recipe 18)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v086_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d operating CF / capex coverage (recipe 18)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v087_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d operating CF / capex coverage (recipe 18)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v088_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d operating CF / capex coverage (recipe 18)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v089_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d operating CF / capex coverage (recipe 18)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v090_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d operating CF / capex coverage (recipe 19)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v091_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d operating CF / capex coverage (recipe 19)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v092_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d operating CF / capex coverage (recipe 19)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v093_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d operating CF / capex coverage (recipe 19)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v094_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d operating CF / capex coverage (recipe 19)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v095_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d operating CF / capex coverage (recipe 20)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v096_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d operating CF / capex coverage (recipe 20)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v097_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d operating CF / capex coverage (recipe 20)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v098_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d operating CF / capex coverage (recipe 20)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v099_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d operating CF / capex coverage (recipe 20)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v100_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d operating CF / capex coverage (recipe 21)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v101_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d operating CF / capex coverage (recipe 21)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v102_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d operating CF / capex coverage (recipe 21)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v103_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d operating CF / capex coverage (recipe 21)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v104_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d operating CF / capex coverage (recipe 21)
def f65oc_f65_semi_ocf_capex_oc_21d_curv_v105_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d operating CF / capex coverage (recipe 22)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v106_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d operating CF / capex coverage (recipe 22)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v107_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d operating CF / capex coverage (recipe 22)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v108_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d operating CF / capex coverage (recipe 22)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v109_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d operating CF / capex coverage (recipe 22)
def f65oc_f65_semi_ocf_capex_oc_63d_curv_v110_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d operating CF / capex coverage (recipe 23)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v111_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d operating CF / capex coverage (recipe 23)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v112_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d operating CF / capex coverage (recipe 23)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v113_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d operating CF / capex coverage (recipe 23)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v114_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d operating CF / capex coverage (recipe 23)
def f65oc_f65_semi_ocf_capex_oc_126d_curv_v115_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d operating CF / capex coverage (recipe 24)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v116_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d operating CF / capex coverage (recipe 24)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v117_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d operating CF / capex coverage (recipe 24)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v118_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d operating CF / capex coverage (recipe 24)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v119_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d operating CF / capex coverage (recipe 24)
def f65oc_f65_semi_ocf_capex_oc_252d_curv_v120_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d operating CF / capex coverage (recipe 25)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v121_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d operating CF / capex coverage (recipe 25)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v122_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d operating CF / capex coverage (recipe 25)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v123_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d operating CF / capex coverage (recipe 25)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v124_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d operating CF / capex coverage (recipe 25)
def f65oc_f65_semi_ocf_capex_oc_504d_curv_v125_signal(ocf, capex, closeadj):
    m = ocf / capex.abs().replace(0, np.nan)
    base = m.pct_change(504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 21d operating CF / capex coverage (recipe 26)
def f65oc_f65_semi_ocf_capex_ocf_g_21d_curv_v126_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 21d operating CF / capex coverage (recipe 26)
def f65oc_f65_semi_ocf_capex_ocf_g_21d_curv_v127_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 21d operating CF / capex coverage (recipe 26)
def f65oc_f65_semi_ocf_capex_ocf_g_21d_curv_v128_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 21d operating CF / capex coverage (recipe 26)
def f65oc_f65_semi_ocf_capex_ocf_g_21d_curv_v129_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 21d operating CF / capex coverage (recipe 26)
def f65oc_f65_semi_ocf_capex_ocf_g_21d_curv_v130_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 63d operating CF / capex coverage (recipe 27)
def f65oc_f65_semi_ocf_capex_ocf_g_63d_curv_v131_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 63d operating CF / capex coverage (recipe 27)
def f65oc_f65_semi_ocf_capex_ocf_g_63d_curv_v132_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 63d operating CF / capex coverage (recipe 27)
def f65oc_f65_semi_ocf_capex_ocf_g_63d_curv_v133_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 63d operating CF / capex coverage (recipe 27)
def f65oc_f65_semi_ocf_capex_ocf_g_63d_curv_v134_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 63d operating CF / capex coverage (recipe 27)
def f65oc_f65_semi_ocf_capex_ocf_g_63d_curv_v135_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 126d operating CF / capex coverage (recipe 28)
def f65oc_f65_semi_ocf_capex_ocf_g_126d_curv_v136_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 126d operating CF / capex coverage (recipe 28)
def f65oc_f65_semi_ocf_capex_ocf_g_126d_curv_v137_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 126d operating CF / capex coverage (recipe 28)
def f65oc_f65_semi_ocf_capex_ocf_g_126d_curv_v138_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 126d operating CF / capex coverage (recipe 28)
def f65oc_f65_semi_ocf_capex_ocf_g_126d_curv_v139_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 126d operating CF / capex coverage (recipe 28)
def f65oc_f65_semi_ocf_capex_ocf_g_126d_curv_v140_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 252d operating CF / capex coverage (recipe 29)
def f65oc_f65_semi_ocf_capex_ocf_g_252d_curv_v141_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 252d operating CF / capex coverage (recipe 29)
def f65oc_f65_semi_ocf_capex_ocf_g_252d_curv_v142_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 252d operating CF / capex coverage (recipe 29)
def f65oc_f65_semi_ocf_capex_ocf_g_252d_curv_v143_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 252d operating CF / capex coverage (recipe 29)
def f65oc_f65_semi_ocf_capex_ocf_g_252d_curv_v144_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 252d operating CF / capex coverage (recipe 29)
def f65oc_f65_semi_ocf_capex_ocf_g_252d_curv_v145_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d curv of 504d operating CF / capex coverage (recipe 30)
def f65oc_f65_semi_ocf_capex_ocf_g_504d_curv_v146_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d curv of 504d operating CF / capex coverage (recipe 30)
def f65oc_f65_semi_ocf_capex_ocf_g_504d_curv_v147_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d curv of 504d operating CF / capex coverage (recipe 30)
def f65oc_f65_semi_ocf_capex_ocf_g_504d_curv_v148_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d curv of 504d operating CF / capex coverage (recipe 30)
def f65oc_f65_semi_ocf_capex_ocf_g_504d_curv_v149_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d curv of 504d operating CF / capex coverage (recipe 30)
def f65oc_f65_semi_ocf_capex_ocf_g_504d_curv_v150_signal(ocf, capex, closeadj):
    s2 = ocf.pct_change(63)
    base = _z(s2, 504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
