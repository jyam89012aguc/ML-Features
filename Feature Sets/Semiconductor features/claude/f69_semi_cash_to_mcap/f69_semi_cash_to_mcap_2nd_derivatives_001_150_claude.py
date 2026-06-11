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
def _f69_build_metric(*args):
    return None  # placeholder (helper unused; metric built inline per feature)


def _f69_safe_pct(x, n):
    return x.pct_change(n)


def _f69_safe_log(x):
    return np.log(x.replace(0, np.nan).abs())


def _f69_zscore(s, w):
    return (s - s.rolling(w, min_periods=max(1, w // 2)).mean()) / s.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)

# 5d slope of 21d cash to market cap (cashneq / marketcap) (recipe 1)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v001_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d cash to market cap (cashneq / marketcap) (recipe 1)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v002_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d cash to market cap (cashneq / marketcap) (recipe 1)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v003_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d cash to market cap (cashneq / marketcap) (recipe 1)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v004_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d cash to market cap (cashneq / marketcap) (recipe 1)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v005_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cash to market cap (cashneq / marketcap) (recipe 2)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v006_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cash to market cap (cashneq / marketcap) (recipe 2)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v007_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cash to market cap (cashneq / marketcap) (recipe 2)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v008_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cash to market cap (cashneq / marketcap) (recipe 2)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v009_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cash to market cap (cashneq / marketcap) (recipe 2)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v010_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d cash to market cap (cashneq / marketcap) (recipe 3)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v011_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d cash to market cap (cashneq / marketcap) (recipe 3)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v012_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d cash to market cap (cashneq / marketcap) (recipe 3)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v013_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d cash to market cap (cashneq / marketcap) (recipe 3)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v014_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d cash to market cap (cashneq / marketcap) (recipe 3)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v015_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cash to market cap (cashneq / marketcap) (recipe 4)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v016_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cash to market cap (cashneq / marketcap) (recipe 4)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v017_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cash to market cap (cashneq / marketcap) (recipe 4)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v018_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cash to market cap (cashneq / marketcap) (recipe 4)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v019_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cash to market cap (cashneq / marketcap) (recipe 4)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v020_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d cash to market cap (cashneq / marketcap) (recipe 5)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v021_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d cash to market cap (cashneq / marketcap) (recipe 5)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v022_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d cash to market cap (cashneq / marketcap) (recipe 5)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v023_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d cash to market cap (cashneq / marketcap) (recipe 5)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v024_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d cash to market cap (cashneq / marketcap) (recipe 5)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v025_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m - _mean(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d cash to market cap (cashneq / marketcap) (recipe 6)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v026_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d cash to market cap (cashneq / marketcap) (recipe 6)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v027_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d cash to market cap (cashneq / marketcap) (recipe 6)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v028_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d cash to market cap (cashneq / marketcap) (recipe 6)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v029_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d cash to market cap (cashneq / marketcap) (recipe 6)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v030_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cash to market cap (cashneq / marketcap) (recipe 7)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v031_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cash to market cap (cashneq / marketcap) (recipe 7)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v032_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cash to market cap (cashneq / marketcap) (recipe 7)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v033_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cash to market cap (cashneq / marketcap) (recipe 7)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v034_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cash to market cap (cashneq / marketcap) (recipe 7)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v035_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d cash to market cap (cashneq / marketcap) (recipe 8)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v036_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d cash to market cap (cashneq / marketcap) (recipe 8)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v037_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d cash to market cap (cashneq / marketcap) (recipe 8)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v038_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d cash to market cap (cashneq / marketcap) (recipe 8)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v039_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d cash to market cap (cashneq / marketcap) (recipe 8)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v040_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cash to market cap (cashneq / marketcap) (recipe 9)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v041_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cash to market cap (cashneq / marketcap) (recipe 9)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v042_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cash to market cap (cashneq / marketcap) (recipe 9)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v043_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cash to market cap (cashneq / marketcap) (recipe 9)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v044_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cash to market cap (cashneq / marketcap) (recipe 9)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v045_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d cash to market cap (cashneq / marketcap) (recipe 10)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v046_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d cash to market cap (cashneq / marketcap) (recipe 10)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v047_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d cash to market cap (cashneq / marketcap) (recipe 10)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v048_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d cash to market cap (cashneq / marketcap) (recipe 10)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v049_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d cash to market cap (cashneq / marketcap) (recipe 10)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v050_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _z(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d cash to market cap (cashneq / marketcap) (recipe 11)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v051_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d cash to market cap (cashneq / marketcap) (recipe 11)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v052_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d cash to market cap (cashneq / marketcap) (recipe 11)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v053_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d cash to market cap (cashneq / marketcap) (recipe 11)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v054_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d cash to market cap (cashneq / marketcap) (recipe 11)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v055_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cash to market cap (cashneq / marketcap) (recipe 12)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v056_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cash to market cap (cashneq / marketcap) (recipe 12)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v057_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cash to market cap (cashneq / marketcap) (recipe 12)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v058_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cash to market cap (cashneq / marketcap) (recipe 12)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v059_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cash to market cap (cashneq / marketcap) (recipe 12)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v060_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d cash to market cap (cashneq / marketcap) (recipe 13)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v061_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d cash to market cap (cashneq / marketcap) (recipe 13)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v062_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d cash to market cap (cashneq / marketcap) (recipe 13)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v063_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d cash to market cap (cashneq / marketcap) (recipe 13)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v064_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d cash to market cap (cashneq / marketcap) (recipe 13)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v065_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cash to market cap (cashneq / marketcap) (recipe 14)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v066_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cash to market cap (cashneq / marketcap) (recipe 14)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v067_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cash to market cap (cashneq / marketcap) (recipe 14)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v068_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cash to market cap (cashneq / marketcap) (recipe 14)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v069_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cash to market cap (cashneq / marketcap) (recipe 14)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v070_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d cash to market cap (cashneq / marketcap) (recipe 15)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v071_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d cash to market cap (cashneq / marketcap) (recipe 15)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v072_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d cash to market cap (cashneq / marketcap) (recipe 15)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v073_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d cash to market cap (cashneq / marketcap) (recipe 15)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v074_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d cash to market cap (cashneq / marketcap) (recipe 15)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v075_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = _std(m, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d cash to market cap (cashneq / marketcap) (recipe 16)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v076_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d cash to market cap (cashneq / marketcap) (recipe 16)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v077_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d cash to market cap (cashneq / marketcap) (recipe 16)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v078_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d cash to market cap (cashneq / marketcap) (recipe 16)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v079_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d cash to market cap (cashneq / marketcap) (recipe 16)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v080_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cash to market cap (cashneq / marketcap) (recipe 17)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v081_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cash to market cap (cashneq / marketcap) (recipe 17)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v082_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cash to market cap (cashneq / marketcap) (recipe 17)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v083_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cash to market cap (cashneq / marketcap) (recipe 17)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v084_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cash to market cap (cashneq / marketcap) (recipe 17)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v085_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d cash to market cap (cashneq / marketcap) (recipe 18)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v086_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d cash to market cap (cashneq / marketcap) (recipe 18)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v087_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d cash to market cap (cashneq / marketcap) (recipe 18)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v088_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d cash to market cap (cashneq / marketcap) (recipe 18)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v089_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d cash to market cap (cashneq / marketcap) (recipe 18)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v090_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cash to market cap (cashneq / marketcap) (recipe 19)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v091_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cash to market cap (cashneq / marketcap) (recipe 19)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v092_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cash to market cap (cashneq / marketcap) (recipe 19)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v093_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cash to market cap (cashneq / marketcap) (recipe 19)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v094_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cash to market cap (cashneq / marketcap) (recipe 19)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v095_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(252, min_periods=126).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d cash to market cap (cashneq / marketcap) (recipe 20)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v096_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d cash to market cap (cashneq / marketcap) (recipe 20)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v097_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d cash to market cap (cashneq / marketcap) (recipe 20)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v098_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d cash to market cap (cashneq / marketcap) (recipe 20)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v099_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d cash to market cap (cashneq / marketcap) (recipe 20)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v100_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.rolling(504, min_periods=252).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d cash to market cap (cashneq / marketcap) (recipe 21)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v101_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d cash to market cap (cashneq / marketcap) (recipe 21)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v102_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d cash to market cap (cashneq / marketcap) (recipe 21)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v103_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d cash to market cap (cashneq / marketcap) (recipe 21)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v104_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d cash to market cap (cashneq / marketcap) (recipe 21)
def f69cm_f69_semi_cash_to_mcap_cm_21d_slope_v105_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cash to market cap (cashneq / marketcap) (recipe 22)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v106_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cash to market cap (cashneq / marketcap) (recipe 22)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v107_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cash to market cap (cashneq / marketcap) (recipe 22)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v108_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cash to market cap (cashneq / marketcap) (recipe 22)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v109_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cash to market cap (cashneq / marketcap) (recipe 22)
def f69cm_f69_semi_cash_to_mcap_cm_63d_slope_v110_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d cash to market cap (cashneq / marketcap) (recipe 23)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v111_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d cash to market cap (cashneq / marketcap) (recipe 23)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v112_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d cash to market cap (cashneq / marketcap) (recipe 23)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v113_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d cash to market cap (cashneq / marketcap) (recipe 23)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v114_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d cash to market cap (cashneq / marketcap) (recipe 23)
def f69cm_f69_semi_cash_to_mcap_cm_126d_slope_v115_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cash to market cap (cashneq / marketcap) (recipe 24)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v116_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cash to market cap (cashneq / marketcap) (recipe 24)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v117_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cash to market cap (cashneq / marketcap) (recipe 24)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v118_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cash to market cap (cashneq / marketcap) (recipe 24)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v119_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cash to market cap (cashneq / marketcap) (recipe 24)
def f69cm_f69_semi_cash_to_mcap_cm_252d_slope_v120_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d cash to market cap (cashneq / marketcap) (recipe 25)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v121_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d cash to market cap (cashneq / marketcap) (recipe 25)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v122_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d cash to market cap (cashneq / marketcap) (recipe 25)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v123_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d cash to market cap (cashneq / marketcap) (recipe 25)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v124_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d cash to market cap (cashneq / marketcap) (recipe 25)
def f69cm_f69_semi_cash_to_mcap_cm_504d_slope_v125_signal(cashneq, marketcap, closeadj):
    m = cashneq / marketcap.replace(0, np.nan)
    base = m.pct_change(504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 21d cash to market cap (cashneq / marketcap) (recipe 26)
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_slope_v126_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 21d cash to market cap (cashneq / marketcap) (recipe 26)
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_slope_v127_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 21d cash to market cap (cashneq / marketcap) (recipe 26)
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_slope_v128_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 21d cash to market cap (cashneq / marketcap) (recipe 26)
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_slope_v129_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 21d cash to market cap (cashneq / marketcap) (recipe 26)
def f69cm_f69_semi_cash_to_mcap_cash_g_21d_slope_v130_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 63d cash to market cap (cashneq / marketcap) (recipe 27)
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_slope_v131_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 63d cash to market cap (cashneq / marketcap) (recipe 27)
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_slope_v132_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 63d cash to market cap (cashneq / marketcap) (recipe 27)
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_slope_v133_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 63d cash to market cap (cashneq / marketcap) (recipe 27)
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_slope_v134_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 63d cash to market cap (cashneq / marketcap) (recipe 27)
def f69cm_f69_semi_cash_to_mcap_cash_g_63d_slope_v135_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 126d cash to market cap (cashneq / marketcap) (recipe 28)
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_slope_v136_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 126d cash to market cap (cashneq / marketcap) (recipe 28)
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_slope_v137_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 126d cash to market cap (cashneq / marketcap) (recipe 28)
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_slope_v138_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 126d cash to market cap (cashneq / marketcap) (recipe 28)
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_slope_v139_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 126d cash to market cap (cashneq / marketcap) (recipe 28)
def f69cm_f69_semi_cash_to_mcap_cash_g_126d_slope_v140_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 252d cash to market cap (cashneq / marketcap) (recipe 29)
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_slope_v141_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 252d cash to market cap (cashneq / marketcap) (recipe 29)
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_slope_v142_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 252d cash to market cap (cashneq / marketcap) (recipe 29)
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_slope_v143_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 252d cash to market cap (cashneq / marketcap) (recipe 29)
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_slope_v144_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 252d cash to market cap (cashneq / marketcap) (recipe 29)
def f69cm_f69_semi_cash_to_mcap_cash_g_252d_slope_v145_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)

# 5d slope of 504d cash to market cap (cashneq / marketcap) (recipe 30)
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_slope_v146_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of 504d cash to market cap (cashneq / marketcap) (recipe 30)
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_slope_v147_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of 504d cash to market cap (cashneq / marketcap) (recipe 30)
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_slope_v148_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of 504d cash to market cap (cashneq / marketcap) (recipe 30)
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_slope_v149_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of 504d cash to market cap (cashneq / marketcap) (recipe 30)
def f69cm_f69_semi_cash_to_mcap_cash_g_504d_slope_v150_signal(cashneq, marketcap, closeadj):
    s2 = cashneq.pct_change(63)
    base = _z(s2, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
