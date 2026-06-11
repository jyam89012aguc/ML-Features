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


# ===== folder domain primitives =====
def _f32cs_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f32cs_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f32cs_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f32cs_diff(a, b):
    return a - b


# 21d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_21d_base_v001_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_63d_base_v002_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_126d_base_v003_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_252d_base_v004_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevel_504d_base_v005_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_21d_base_v006_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_63d_base_v007_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_126d_base_v008_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_252d_base_v009_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurlevelrel_504d_base_v010_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_21d_base_v011_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_63d_base_v012_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_126d_base_v013_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_252d_base_v014_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmean_504d_base_v015_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_21d_base_v016_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_63d_base_v017_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_126d_base_v018_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_252d_base_v019_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurz_504d_base_v020_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of capex surprise vs 4q rolling expectation (median/MAD)
def f32cs_f32_semi_capex_surprise_cpsurrobz_21d_base_v021_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of capex surprise vs 4q rolling expectation (median/MAD)
def f32cs_f32_semi_capex_surprise_cpsurrobz_63d_base_v022_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of capex surprise vs 4q rolling expectation (median/MAD)
def f32cs_f32_semi_capex_surprise_cpsurrobz_126d_base_v023_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of capex surprise vs 4q rolling expectation (median/MAD)
def f32cs_f32_semi_capex_surprise_cpsurrobz_252d_base_v024_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of capex surprise vs 4q rolling expectation (median/MAD)
def f32cs_f32_semi_capex_surprise_cpsurrobz_504d_base_v025_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_21d_base_v026_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_63d_base_v027_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_126d_base_v028_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_252d_base_v029_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmax_504d_base_v030_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_21d_base_v031_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_63d_base_v032_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_126d_base_v033_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_252d_base_v034_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurmin_504d_base_v035_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_21d_base_v036_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_63d_base_v037_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_126d_base_v038_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_252d_base_v039_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurrng_504d_base_v040_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of capex surprise vs 4q rolling expectation in rolling range
def f32cs_f32_semi_capex_surprise_cpsurpos_21d_base_v041_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of capex surprise vs 4q rolling expectation in rolling range
def f32cs_f32_semi_capex_surprise_cpsurpos_63d_base_v042_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of capex surprise vs 4q rolling expectation in rolling range
def f32cs_f32_semi_capex_surprise_cpsurpos_126d_base_v043_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of capex surprise vs 4q rolling expectation in rolling range
def f32cs_f32_semi_capex_surprise_cpsurpos_252d_base_v044_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of capex surprise vs 4q rolling expectation in rolling range
def f32cs_f32_semi_capex_surprise_cpsurpos_504d_base_v045_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of capex surprise vs 4q rolling expectation from rolling peak
def f32cs_f32_semi_capex_surprise_cpsurdd_21d_base_v046_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of capex surprise vs 4q rolling expectation from rolling peak
def f32cs_f32_semi_capex_surprise_cpsurdd_63d_base_v047_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of capex surprise vs 4q rolling expectation from rolling peak
def f32cs_f32_semi_capex_surprise_cpsurdd_126d_base_v048_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of capex surprise vs 4q rolling expectation from rolling peak
def f32cs_f32_semi_capex_surprise_cpsurdd_252d_base_v049_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of capex surprise vs 4q rolling expectation from rolling peak
def f32cs_f32_semi_capex_surprise_cpsurdd_504d_base_v050_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of capex surprise vs 4q rolling expectation above rolling trough
def f32cs_f32_semi_capex_surprise_cpsurup_21d_base_v051_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of capex surprise vs 4q rolling expectation above rolling trough
def f32cs_f32_semi_capex_surprise_cpsurup_63d_base_v052_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of capex surprise vs 4q rolling expectation above rolling trough
def f32cs_f32_semi_capex_surprise_cpsurup_126d_base_v053_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of capex surprise vs 4q rolling expectation above rolling trough
def f32cs_f32_semi_capex_surprise_cpsurup_252d_base_v054_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of capex surprise vs 4q rolling expectation above rolling trough
def f32cs_f32_semi_capex_surprise_cpsurup_504d_base_v055_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_21d_base_v056_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_63d_base_v057_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_126d_base_v058_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_252d_base_v059_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurstd_504d_base_v060_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_21d_base_v061_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_63d_base_v062_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_126d_base_v063_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_252d_base_v064_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurskew_504d_base_v065_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_21d_base_v066_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_63d_base_v067_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_126d_base_v068_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_252d_base_v069_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurkurt_504d_base_v070_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_21d_base_v071_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_63d_base_v072_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_126d_base_v073_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_252d_base_v074_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in capex surprise vs 4q rolling expectation
def f32cs_f32_semi_capex_surprise_cpsurhits_504d_base_v075_signal(capex, closeadj):
    exp4q = _mean(capex, 84)
    M = _f32cs_ratio(capex - exp4q, exp4q.abs())
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


