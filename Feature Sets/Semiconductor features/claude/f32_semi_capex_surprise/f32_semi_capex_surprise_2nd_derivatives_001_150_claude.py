import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


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
def _f32cs_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f32cs_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f32cs_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f32cs_diff(a, b):
    return a - b


# 5d slope of 21d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_21d_slope_v001_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_21d_slope_v002_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_21d_slope_v003_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_21d_slope_v004_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_21d_slope_v005_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d levelrel of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_63d_slope_v006_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d levelrel of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_63d_slope_v007_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d levelrel of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_63d_slope_v008_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d levelrel of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_63d_slope_v009_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d levelrel of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_63d_slope_v010_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_126d_slope_v011_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_126d_slope_v012_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_126d_slope_v013_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_126d_slope_v014_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_126d_slope_v015_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _mean(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_252d_slope_v016_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_252d_slope_v017_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_252d_slope_v018_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_252d_slope_v019_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d z of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_252d_slope_v020_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d robz of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrobz_504d_slope_v021_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d robz of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrobz_504d_slope_v022_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d robz of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrobz_504d_slope_v023_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robz of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrobz_504d_slope_v024_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d robz of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrobz_504d_slope_v025_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_21d_slope_v026_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_21d_slope_v027_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_21d_slope_v028_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_21d_slope_v029_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_21d_slope_v030_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_63d_slope_v031_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _min(M, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_63d_slope_v032_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _min(M, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_63d_slope_v033_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _min(M, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_63d_slope_v034_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _min(M, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_63d_slope_v035_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _min(M, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d rng of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_126d_slope_v036_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d rng of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_126d_slope_v037_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d rng of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_126d_slope_v038_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d rng of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_126d_slope_v039_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d rng of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_126d_slope_v040_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _max(M, 126) - _min(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pos of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpos_252d_slope_v041_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pos of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpos_252d_slope_v042_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pos of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpos_252d_slope_v043_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d pos of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpos_252d_slope_v044_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d pos of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpos_252d_slope_v045_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d dd of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdd_504d_slope_v046_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d dd of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdd_504d_slope_v047_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d dd of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdd_504d_slope_v048_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d dd of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdd_504d_slope_v049_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d dd of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdd_504d_slope_v050_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 504)
    base = M - peak
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d up of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurup_21d_slope_v051_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d up of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurup_21d_slope_v052_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d up of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurup_21d_slope_v053_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d up of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurup_21d_slope_v054_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d up of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurup_21d_slope_v055_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 21)
    base = M - trough
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_63d_slope_v056_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_63d_slope_v057_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_63d_slope_v058_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_63d_slope_v059_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_63d_slope_v060_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_126d_slope_v061_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_126d_slope_v062_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_126d_slope_v063_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_126d_slope_v064_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_126d_slope_v065_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(126, min_periods=63).skew()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d kurt of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_252d_slope_v066_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d kurt of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_252d_slope_v067_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d kurt of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_252d_slope_v068_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d kurt of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_252d_slope_v069_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d kurt of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_252d_slope_v070_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.rolling(252, min_periods=126).kurt()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d hits of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_504d_slope_v071_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d hits of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_504d_slope_v072_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d hits of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_504d_slope_v073_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d hits of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_504d_slope_v074_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d hits of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_504d_slope_v075_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d signcum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_21d_slope_v076_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d signcum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_21d_slope_v077_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d signcum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_21d_slope_v078_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d signcum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_21d_slope_v079_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d signcum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsursigncum_21d_slope_v080_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d cum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_63d_slope_v081_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_63d_slope_v082_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d cum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_63d_slope_v083_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d cum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_63d_slope_v084_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d cum of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcum_63d_slope_v085_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d emafast of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremafast_126d_slope_v086_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d emafast of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremafast_126d_slope_v087_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d emafast of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremafast_126d_slope_v088_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d emafast of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremafast_126d_slope_v089_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d emafast of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremafast_126d_slope_v090_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d emaslow of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremaslow_252d_slope_v091_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d emaslow of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremaslow_252d_slope_v092_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d emaslow of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremaslow_252d_slope_v093_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d emaslow of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremaslow_252d_slope_v094_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d emaslow of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsuremaslow_252d_slope_v095_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d zabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_504d_slope_v096_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d zabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_504d_slope_v097_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d zabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_504d_slope_v098_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d zabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_504d_slope_v099_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d zabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurzabs_504d_slope_v100_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504).abs()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d posmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_21d_slope_v101_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d posmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_21d_slope_v102_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d posmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_21d_slope_v103_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d posmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_21d_slope_v104_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d posmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurposmean_21d_slope_v105_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d negmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_63d_slope_v106_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d negmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_63d_slope_v107_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d negmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_63d_slope_v108_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d negmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_63d_slope_v109_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d negmean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurnegmean_63d_slope_v110_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d cvar of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_126d_slope_v111_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d cvar of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_126d_slope_v112_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d cvar of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_126d_slope_v113_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d cvar of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_126d_slope_v114_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d cvar of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcvar_126d_slope_v115_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d logabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlogabs_252d_slope_v116_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d logabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlogabs_252d_slope_v117_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d logabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlogabs_252d_slope_v118_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d logabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlogabs_252d_slope_v119_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d logabs of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlogabs_252d_slope_v120_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d diff of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_504d_slope_v121_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d diff of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_504d_slope_v122_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d diff of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_504d_slope_v123_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d diff of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_504d_slope_v124_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d diff of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurdiff_504d_slope_v125_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff(periods=504)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pctchg of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_21d_slope_v126_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pctchg of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_21d_slope_v127_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pctchg of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_21d_slope_v128_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d pctchg of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_21d_slope_v129_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 21d pctchg of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurpctchg_21d_slope_v130_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.pct_change(periods=21)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d xover of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurxover_63d_slope_v131_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d xover of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurxover_63d_slope_v132_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d xover of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurxover_63d_slope_v133_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d xover of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurxover_63d_slope_v134_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 63d xover of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurxover_63d_slope_v135_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M - _mean(M, 126)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d trend of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_126d_slope_v136_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d trend of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_126d_slope_v137_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d trend of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_126d_slope_v138_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d trend of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_126d_slope_v139_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 126d trend of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurtrend_126d_slope_v140_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d highmask of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhighmask_252d_slope_v141_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d highmask of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhighmask_252d_slope_v142_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d highmask of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhighmask_252d_slope_v143_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d highmask of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhighmask_252d_slope_v144_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 252d highmask of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhighmask_252d_slope_v145_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d compositez of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcompositez_504d_slope_v146_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d compositez of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcompositez_504d_slope_v147_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d compositez of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcompositez_504d_slope_v148_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d compositez of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcompositez_504d_slope_v149_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d slope of 504d compositez of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurcompositez_504d_slope_v150_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    base = _z(M, 504) + _z(M, 252)
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


