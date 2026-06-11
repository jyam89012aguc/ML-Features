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
def _f62_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f62_safe_pct(x, n):
    return x.pct_change(n)


def _f62_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f62_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d slope of 21d FCF margin (fcf / revenue) (recipe 1)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v001_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d FCF margin (fcf / revenue) (recipe 1)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v002_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d FCF margin (fcf / revenue) (recipe 1)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v003_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d FCF margin (fcf / revenue) (recipe 1)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v004_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d FCF margin (fcf / revenue) (recipe 1)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v005_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d FCF margin (fcf / revenue) (recipe 2)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v006_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d FCF margin (fcf / revenue) (recipe 2)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v007_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d FCF margin (fcf / revenue) (recipe 2)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v008_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d FCF margin (fcf / revenue) (recipe 2)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v009_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d FCF margin (fcf / revenue) (recipe 2)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v010_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d FCF margin (fcf / revenue) (recipe 3)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v011_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d FCF margin (fcf / revenue) (recipe 3)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v012_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d FCF margin (fcf / revenue) (recipe 3)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v013_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d FCF margin (fcf / revenue) (recipe 3)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v014_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d FCF margin (fcf / revenue) (recipe 3)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v015_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d FCF margin (fcf / revenue) (recipe 4)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v016_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d FCF margin (fcf / revenue) (recipe 4)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v017_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d FCF margin (fcf / revenue) (recipe 4)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v018_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d FCF margin (fcf / revenue) (recipe 4)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v019_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d FCF margin (fcf / revenue) (recipe 4)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v020_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d FCF margin (fcf / revenue) (recipe 5)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v021_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d FCF margin (fcf / revenue) (recipe 5)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v022_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d FCF margin (fcf / revenue) (recipe 5)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v023_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d FCF margin (fcf / revenue) (recipe 5)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v024_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d FCF margin (fcf / revenue) (recipe 5)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v025_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d FCF margin (fcf / revenue) (recipe 6)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v026_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d FCF margin (fcf / revenue) (recipe 6)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v027_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d FCF margin (fcf / revenue) (recipe 6)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v028_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d FCF margin (fcf / revenue) (recipe 6)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v029_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d FCF margin (fcf / revenue) (recipe 6)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v030_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d FCF margin (fcf / revenue) (recipe 7)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v031_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d FCF margin (fcf / revenue) (recipe 7)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v032_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d FCF margin (fcf / revenue) (recipe 7)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v033_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d FCF margin (fcf / revenue) (recipe 7)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v034_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d FCF margin (fcf / revenue) (recipe 7)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v035_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d FCF margin (fcf / revenue) (recipe 8)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v036_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d FCF margin (fcf / revenue) (recipe 8)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v037_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d FCF margin (fcf / revenue) (recipe 8)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v038_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d FCF margin (fcf / revenue) (recipe 8)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v039_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d FCF margin (fcf / revenue) (recipe 8)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v040_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d FCF margin (fcf / revenue) (recipe 9)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v041_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d FCF margin (fcf / revenue) (recipe 9)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v042_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d FCF margin (fcf / revenue) (recipe 9)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v043_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d FCF margin (fcf / revenue) (recipe 9)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v044_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d FCF margin (fcf / revenue) (recipe 9)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v045_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d FCF margin (fcf / revenue) (recipe 10)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v046_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d FCF margin (fcf / revenue) (recipe 10)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v047_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d FCF margin (fcf / revenue) (recipe 10)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v048_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d FCF margin (fcf / revenue) (recipe 10)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v049_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d FCF margin (fcf / revenue) (recipe 10)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v050_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d FCF margin (fcf / revenue) (recipe 11)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v051_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d FCF margin (fcf / revenue) (recipe 11)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v052_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d FCF margin (fcf / revenue) (recipe 11)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v053_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d FCF margin (fcf / revenue) (recipe 11)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v054_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d FCF margin (fcf / revenue) (recipe 11)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v055_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d FCF margin (fcf / revenue) (recipe 12)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v056_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d FCF margin (fcf / revenue) (recipe 12)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v057_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d FCF margin (fcf / revenue) (recipe 12)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v058_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d FCF margin (fcf / revenue) (recipe 12)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v059_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d FCF margin (fcf / revenue) (recipe 12)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v060_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d FCF margin (fcf / revenue) (recipe 13)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v061_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d FCF margin (fcf / revenue) (recipe 13)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v062_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d FCF margin (fcf / revenue) (recipe 13)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v063_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d FCF margin (fcf / revenue) (recipe 13)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v064_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d FCF margin (fcf / revenue) (recipe 13)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v065_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d FCF margin (fcf / revenue) (recipe 14)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v066_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d FCF margin (fcf / revenue) (recipe 14)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v067_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d FCF margin (fcf / revenue) (recipe 14)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v068_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d FCF margin (fcf / revenue) (recipe 14)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v069_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d FCF margin (fcf / revenue) (recipe 14)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v070_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d FCF margin (fcf / revenue) (recipe 15)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v071_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d FCF margin (fcf / revenue) (recipe 15)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v072_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d FCF margin (fcf / revenue) (recipe 15)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v073_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d FCF margin (fcf / revenue) (recipe 15)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v074_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d FCF margin (fcf / revenue) (recipe 15)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v075_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d FCF margin (fcf / revenue) (recipe 16)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v076_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d FCF margin (fcf / revenue) (recipe 16)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v077_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d FCF margin (fcf / revenue) (recipe 16)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v078_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d FCF margin (fcf / revenue) (recipe 16)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v079_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d FCF margin (fcf / revenue) (recipe 16)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v080_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d FCF margin (fcf / revenue) (recipe 17)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v081_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d FCF margin (fcf / revenue) (recipe 17)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v082_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d FCF margin (fcf / revenue) (recipe 17)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v083_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d FCF margin (fcf / revenue) (recipe 17)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v084_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d FCF margin (fcf / revenue) (recipe 17)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v085_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d FCF margin (fcf / revenue) (recipe 18)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v086_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d FCF margin (fcf / revenue) (recipe 18)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v087_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d FCF margin (fcf / revenue) (recipe 18)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v088_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d FCF margin (fcf / revenue) (recipe 18)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v089_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d FCF margin (fcf / revenue) (recipe 18)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v090_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d FCF margin (fcf / revenue) (recipe 19)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v091_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d FCF margin (fcf / revenue) (recipe 19)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v092_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d FCF margin (fcf / revenue) (recipe 19)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v093_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d FCF margin (fcf / revenue) (recipe 19)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v094_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d FCF margin (fcf / revenue) (recipe 19)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v095_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d FCF margin (fcf / revenue) (recipe 20)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v096_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d FCF margin (fcf / revenue) (recipe 20)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v097_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d FCF margin (fcf / revenue) (recipe 20)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v098_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d FCF margin (fcf / revenue) (recipe 20)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v099_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d FCF margin (fcf / revenue) (recipe 20)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v100_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d FCF margin (fcf / revenue) (recipe 21)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v101_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d FCF margin (fcf / revenue) (recipe 21)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v102_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d FCF margin (fcf / revenue) (recipe 21)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v103_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d FCF margin (fcf / revenue) (recipe 21)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v104_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d FCF margin (fcf / revenue) (recipe 21)
def f62fm_f62_semi_fcf_margin_fm_21d_slope_v105_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d FCF margin (fcf / revenue) (recipe 22)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v106_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d FCF margin (fcf / revenue) (recipe 22)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v107_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d FCF margin (fcf / revenue) (recipe 22)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v108_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d FCF margin (fcf / revenue) (recipe 22)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v109_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d FCF margin (fcf / revenue) (recipe 22)
def f62fm_f62_semi_fcf_margin_fm_63d_slope_v110_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d FCF margin (fcf / revenue) (recipe 23)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v111_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d FCF margin (fcf / revenue) (recipe 23)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v112_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d FCF margin (fcf / revenue) (recipe 23)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v113_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d FCF margin (fcf / revenue) (recipe 23)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v114_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d FCF margin (fcf / revenue) (recipe 23)
def f62fm_f62_semi_fcf_margin_fm_126d_slope_v115_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d FCF margin (fcf / revenue) (recipe 24)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v116_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d FCF margin (fcf / revenue) (recipe 24)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v117_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d FCF margin (fcf / revenue) (recipe 24)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v118_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d FCF margin (fcf / revenue) (recipe 24)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v119_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d FCF margin (fcf / revenue) (recipe 24)
def f62fm_f62_semi_fcf_margin_fm_252d_slope_v120_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d FCF margin (fcf / revenue) (recipe 25)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v121_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d FCF margin (fcf / revenue) (recipe 25)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v122_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d FCF margin (fcf / revenue) (recipe 25)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v123_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d FCF margin (fcf / revenue) (recipe 25)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v124_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d FCF margin (fcf / revenue) (recipe 25)
def f62fm_f62_semi_fcf_margin_fm_504d_slope_v125_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d FCF margin (fcf / revenue) (recipe 26)
def f62fm_f62_semi_fcf_margin_fcf_g_21d_slope_v126_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d FCF margin (fcf / revenue) (recipe 26)
def f62fm_f62_semi_fcf_margin_fcf_g_21d_slope_v127_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d FCF margin (fcf / revenue) (recipe 26)
def f62fm_f62_semi_fcf_margin_fcf_g_21d_slope_v128_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d FCF margin (fcf / revenue) (recipe 26)
def f62fm_f62_semi_fcf_margin_fcf_g_21d_slope_v129_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d FCF margin (fcf / revenue) (recipe 26)
def f62fm_f62_semi_fcf_margin_fcf_g_21d_slope_v130_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d FCF margin (fcf / revenue) (recipe 27)
def f62fm_f62_semi_fcf_margin_fcf_g_63d_slope_v131_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d FCF margin (fcf / revenue) (recipe 27)
def f62fm_f62_semi_fcf_margin_fcf_g_63d_slope_v132_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d FCF margin (fcf / revenue) (recipe 27)
def f62fm_f62_semi_fcf_margin_fcf_g_63d_slope_v133_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d FCF margin (fcf / revenue) (recipe 27)
def f62fm_f62_semi_fcf_margin_fcf_g_63d_slope_v134_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d FCF margin (fcf / revenue) (recipe 27)
def f62fm_f62_semi_fcf_margin_fcf_g_63d_slope_v135_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d FCF margin (fcf / revenue) (recipe 28)
def f62fm_f62_semi_fcf_margin_fcf_g_126d_slope_v136_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d FCF margin (fcf / revenue) (recipe 28)
def f62fm_f62_semi_fcf_margin_fcf_g_126d_slope_v137_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d FCF margin (fcf / revenue) (recipe 28)
def f62fm_f62_semi_fcf_margin_fcf_g_126d_slope_v138_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d FCF margin (fcf / revenue) (recipe 28)
def f62fm_f62_semi_fcf_margin_fcf_g_126d_slope_v139_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d FCF margin (fcf / revenue) (recipe 28)
def f62fm_f62_semi_fcf_margin_fcf_g_126d_slope_v140_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d FCF margin (fcf / revenue) (recipe 29)
def f62fm_f62_semi_fcf_margin_fcf_g_252d_slope_v141_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d FCF margin (fcf / revenue) (recipe 29)
def f62fm_f62_semi_fcf_margin_fcf_g_252d_slope_v142_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d FCF margin (fcf / revenue) (recipe 29)
def f62fm_f62_semi_fcf_margin_fcf_g_252d_slope_v143_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d FCF margin (fcf / revenue) (recipe 29)
def f62fm_f62_semi_fcf_margin_fcf_g_252d_slope_v144_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d FCF margin (fcf / revenue) (recipe 29)
def f62fm_f62_semi_fcf_margin_fcf_g_252d_slope_v145_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d FCF margin (fcf / revenue) (recipe 30)
def f62fm_f62_semi_fcf_margin_fcf_g_504d_slope_v146_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d FCF margin (fcf / revenue) (recipe 30)
def f62fm_f62_semi_fcf_margin_fcf_g_504d_slope_v147_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d FCF margin (fcf / revenue) (recipe 30)
def f62fm_f62_semi_fcf_margin_fcf_g_504d_slope_v148_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d FCF margin (fcf / revenue) (recipe 30)
def f62fm_f62_semi_fcf_margin_fcf_g_504d_slope_v149_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d FCF margin (fcf / revenue) (recipe 30)
def f62fm_f62_semi_fcf_margin_fcf_g_504d_slope_v150_signal(fcf, revenue, closeadj):
    s2 = fcf.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
