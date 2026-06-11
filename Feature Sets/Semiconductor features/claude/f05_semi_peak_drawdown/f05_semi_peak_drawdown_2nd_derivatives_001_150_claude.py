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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f05_dd(c, w):
    peak = c.rolling(w, min_periods=max(1, w // 2)).max()
    return (c - peak) / peak.replace(0, np.nan)


def _f05_runup(c, w):
    trough = c.rolling(w, min_periods=max(1, w // 2)).min()
    return (c - trough) / trough.replace(0, np.nan)


def _f05_log_dd(c, w):
    peak = c.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(c.replace(0, np.nan) / peak.replace(0, np.nan))

# 5d slope of 21d drawdown
def f05pd_f05_semi_peak_drawdown_dd_21d_slope_v001_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d drawdown
def f05pd_f05_semi_peak_drawdown_dd_21d_slope_v002_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d drawdown
def f05pd_f05_semi_peak_drawdown_dd_21d_slope_v003_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d drawdown
def f05pd_f05_semi_peak_drawdown_dd_21d_slope_v004_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d drawdown
def f05pd_f05_semi_peak_drawdown_dd_21d_slope_v005_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d drawdown
def f05pd_f05_semi_peak_drawdown_dd_63d_slope_v006_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d drawdown
def f05pd_f05_semi_peak_drawdown_dd_63d_slope_v007_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d drawdown
def f05pd_f05_semi_peak_drawdown_dd_63d_slope_v008_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d drawdown
def f05pd_f05_semi_peak_drawdown_dd_63d_slope_v009_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d drawdown
def f05pd_f05_semi_peak_drawdown_dd_63d_slope_v010_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d drawdown
def f05pd_f05_semi_peak_drawdown_dd_126d_slope_v011_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d drawdown
def f05pd_f05_semi_peak_drawdown_dd_126d_slope_v012_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d drawdown
def f05pd_f05_semi_peak_drawdown_dd_126d_slope_v013_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d drawdown
def f05pd_f05_semi_peak_drawdown_dd_126d_slope_v014_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d drawdown
def f05pd_f05_semi_peak_drawdown_dd_126d_slope_v015_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d drawdown
def f05pd_f05_semi_peak_drawdown_dd_252d_slope_v016_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d drawdown
def f05pd_f05_semi_peak_drawdown_dd_252d_slope_v017_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d drawdown
def f05pd_f05_semi_peak_drawdown_dd_252d_slope_v018_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d drawdown
def f05pd_f05_semi_peak_drawdown_dd_252d_slope_v019_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d drawdown
def f05pd_f05_semi_peak_drawdown_dd_252d_slope_v020_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d drawdown
def f05pd_f05_semi_peak_drawdown_dd_504d_slope_v021_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d drawdown
def f05pd_f05_semi_peak_drawdown_dd_504d_slope_v022_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d drawdown
def f05pd_f05_semi_peak_drawdown_dd_504d_slope_v023_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d drawdown
def f05pd_f05_semi_peak_drawdown_dd_504d_slope_v024_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d drawdown
def f05pd_f05_semi_peak_drawdown_dd_504d_slope_v025_signal(closeadj, high, low):
    base = _f05_dd(closeadj, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_21d_slope_v026_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_21d_slope_v027_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_21d_slope_v028_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_21d_slope_v029_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_21d_slope_v030_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_63d_slope_v031_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_63d_slope_v032_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_63d_slope_v033_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_63d_slope_v034_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_63d_slope_v035_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_126d_slope_v036_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_126d_slope_v037_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_126d_slope_v038_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_126d_slope_v039_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_126d_slope_v040_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_252d_slope_v041_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_252d_slope_v042_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_252d_slope_v043_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_252d_slope_v044_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_252d_slope_v045_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_504d_slope_v046_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_504d_slope_v047_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_504d_slope_v048_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_504d_slope_v049_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d log drawdown
def f05pd_f05_semi_peak_drawdown_logdd_504d_slope_v050_signal(closeadj, high, low):
    base = _f05_log_dd(closeadj, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d run-up
def f05pd_f05_semi_peak_drawdown_runup_21d_slope_v051_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d run-up
def f05pd_f05_semi_peak_drawdown_runup_21d_slope_v052_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d run-up
def f05pd_f05_semi_peak_drawdown_runup_21d_slope_v053_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d run-up
def f05pd_f05_semi_peak_drawdown_runup_21d_slope_v054_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d run-up
def f05pd_f05_semi_peak_drawdown_runup_21d_slope_v055_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d run-up
def f05pd_f05_semi_peak_drawdown_runup_63d_slope_v056_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d run-up
def f05pd_f05_semi_peak_drawdown_runup_63d_slope_v057_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d run-up
def f05pd_f05_semi_peak_drawdown_runup_63d_slope_v058_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d run-up
def f05pd_f05_semi_peak_drawdown_runup_63d_slope_v059_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d run-up
def f05pd_f05_semi_peak_drawdown_runup_63d_slope_v060_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d run-up
def f05pd_f05_semi_peak_drawdown_runup_126d_slope_v061_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d run-up
def f05pd_f05_semi_peak_drawdown_runup_126d_slope_v062_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d run-up
def f05pd_f05_semi_peak_drawdown_runup_126d_slope_v063_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d run-up
def f05pd_f05_semi_peak_drawdown_runup_126d_slope_v064_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d run-up
def f05pd_f05_semi_peak_drawdown_runup_126d_slope_v065_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d run-up
def f05pd_f05_semi_peak_drawdown_runup_252d_slope_v066_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d run-up
def f05pd_f05_semi_peak_drawdown_runup_252d_slope_v067_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d run-up
def f05pd_f05_semi_peak_drawdown_runup_252d_slope_v068_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d run-up
def f05pd_f05_semi_peak_drawdown_runup_252d_slope_v069_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d run-up
def f05pd_f05_semi_peak_drawdown_runup_252d_slope_v070_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d run-up
def f05pd_f05_semi_peak_drawdown_runup_504d_slope_v071_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d run-up
def f05pd_f05_semi_peak_drawdown_runup_504d_slope_v072_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d run-up
def f05pd_f05_semi_peak_drawdown_runup_504d_slope_v073_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d run-up
def f05pd_f05_semi_peak_drawdown_runup_504d_slope_v074_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d run-up
def f05pd_f05_semi_peak_drawdown_runup_504d_slope_v075_signal(closeadj, high, low):
    base = _f05_runup(closeadj, 504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_21d_slope_v076_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_21d_slope_v077_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_21d_slope_v078_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_21d_slope_v079_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_21d_slope_v080_signal(closeadj, high, low):
    hi = _max(high, 21)
    lo = _min(low, 21)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_63d_slope_v081_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_63d_slope_v082_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_63d_slope_v083_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_63d_slope_v084_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_63d_slope_v085_signal(closeadj, high, low):
    hi = _max(high, 63)
    lo = _min(low, 63)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_126d_slope_v086_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_126d_slope_v087_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_126d_slope_v088_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_126d_slope_v089_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_126d_slope_v090_signal(closeadj, high, low):
    hi = _max(high, 126)
    lo = _min(low, 126)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_252d_slope_v091_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_252d_slope_v092_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_252d_slope_v093_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_252d_slope_v094_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_252d_slope_v095_signal(closeadj, high, low):
    hi = _max(high, 252)
    lo = _min(low, 252)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_504d_slope_v096_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_504d_slope_v097_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_504d_slope_v098_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_504d_slope_v099_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d close position in range
def f05pd_f05_semi_peak_drawdown_closepos_504d_slope_v100_signal(closeadj, high, low):
    hi = _max(high, 504)
    lo = _min(low, 504)
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_21d_slope_v101_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    base = (closeadj < peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_21d_slope_v102_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    base = (closeadj < peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_21d_slope_v103_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    base = (closeadj < peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_21d_slope_v104_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    base = (closeadj < peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_21d_slope_v105_signal(closeadj, high, low):
    peak = _max(closeadj, 21)
    base = (closeadj < peak).astype(float).rolling(21, min_periods=max(1, 21 // 2)).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_63d_slope_v106_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    base = (closeadj < peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_63d_slope_v107_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    base = (closeadj < peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_63d_slope_v108_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    base = (closeadj < peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_63d_slope_v109_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    base = (closeadj < peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_63d_slope_v110_signal(closeadj, high, low):
    peak = _max(closeadj, 63)
    base = (closeadj < peak).astype(float).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_126d_slope_v111_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    base = (closeadj < peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_126d_slope_v112_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    base = (closeadj < peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_126d_slope_v113_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    base = (closeadj < peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_126d_slope_v114_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    base = (closeadj < peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_126d_slope_v115_signal(closeadj, high, low):
    peak = _max(closeadj, 126)
    base = (closeadj < peak).astype(float).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_252d_slope_v116_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    base = (closeadj < peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_252d_slope_v117_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    base = (closeadj < peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_252d_slope_v118_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    base = (closeadj < peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_252d_slope_v119_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    base = (closeadj < peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_252d_slope_v120_signal(closeadj, high, low):
    peak = _max(closeadj, 252)
    base = (closeadj < peak).astype(float).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_504d_slope_v121_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    base = (closeadj < peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_504d_slope_v122_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    base = (closeadj < peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_504d_slope_v123_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    base = (closeadj < peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_504d_slope_v124_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    base = (closeadj < peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d underwater fraction
def f05pd_f05_semi_peak_drawdown_underwaterfrac_504d_slope_v125_signal(closeadj, high, low):
    peak = _max(closeadj, 504)
    base = (closeadj < peak).astype(float).rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_21d_slope_v126_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    base = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_21d_slope_v127_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    base = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_21d_slope_v128_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    base = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_21d_slope_v129_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    base = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_21d_slope_v130_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 21)
    base = (d ** 2).rolling(21, min_periods=max(1, 21 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_63d_slope_v131_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    base = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_63d_slope_v132_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    base = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_63d_slope_v133_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    base = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_63d_slope_v134_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    base = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_63d_slope_v135_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 63)
    base = (d ** 2).rolling(63, min_periods=max(1, 63 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_126d_slope_v136_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    base = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_126d_slope_v137_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    base = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_126d_slope_v138_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    base = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_126d_slope_v139_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    base = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_126d_slope_v140_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 126)
    base = (d ** 2).rolling(126, min_periods=max(1, 126 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_252d_slope_v141_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    base = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_252d_slope_v142_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    base = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_252d_slope_v143_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    base = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_252d_slope_v144_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    base = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_252d_slope_v145_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 252)
    base = (d ** 2).rolling(252, min_periods=max(1, 252 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_504d_slope_v146_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    base = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_504d_slope_v147_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    base = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_504d_slope_v148_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    base = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_504d_slope_v149_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    base = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d ulcer index
def f05pd_f05_semi_peak_drawdown_ulcer_504d_slope_v150_signal(closeadj, high, low):
    d = _f05_dd(closeadj, 504)
    base = (d ** 2).rolling(504, min_periods=max(1, 504 // 2)).mean() ** 0.5
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


