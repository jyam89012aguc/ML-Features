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
def _f35ib_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f35ib_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f35ib_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f35ib_diff(a, b):
    return a - b


# 21d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_21d_base_v001_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 21)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_63d_base_v002_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_126d_base_v003_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 126)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_252d_base_v004_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 252)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_504d_base_v005_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 504)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_21d_base_v006_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_63d_base_v007_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_126d_base_v008_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_252d_base_v009_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M - _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_504d_base_v010_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 504)
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_21d_base_v011_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_63d_base_v012_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_126d_base_v013_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_252d_base_v014_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_504d_base_v015_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_21d_base_v016_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_63d_base_v017_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_126d_base_v018_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_252d_base_v019_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_504d_base_v020_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of sequential inventory burn (negative log change) (median/MAD)
def f35ib_f35_semi_inventory_burn_invburnrobz_21d_base_v021_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of sequential inventory burn (negative log change) (median/MAD)
def f35ib_f35_semi_inventory_burn_invburnrobz_63d_base_v022_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of sequential inventory burn (negative log change) (median/MAD)
def f35ib_f35_semi_inventory_burn_invburnrobz_126d_base_v023_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of sequential inventory burn (negative log change) (median/MAD)
def f35ib_f35_semi_inventory_burn_invburnrobz_252d_base_v024_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of sequential inventory burn (negative log change) (median/MAD)
def f35ib_f35_semi_inventory_burn_invburnrobz_504d_base_v025_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_21d_base_v026_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_63d_base_v027_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_126d_base_v028_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_252d_base_v029_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_504d_base_v030_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_21d_base_v031_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_63d_base_v032_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_126d_base_v033_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_252d_base_v034_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_504d_base_v035_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_21d_base_v036_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_63d_base_v037_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_126d_base_v038_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_252d_base_v039_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_504d_base_v040_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of sequential inventory burn (negative log change) in rolling range
def f35ib_f35_semi_inventory_burn_invburnpos_21d_base_v041_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of sequential inventory burn (negative log change) in rolling range
def f35ib_f35_semi_inventory_burn_invburnpos_63d_base_v042_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of sequential inventory burn (negative log change) in rolling range
def f35ib_f35_semi_inventory_burn_invburnpos_126d_base_v043_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of sequential inventory burn (negative log change) in rolling range
def f35ib_f35_semi_inventory_burn_invburnpos_252d_base_v044_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of sequential inventory burn (negative log change) in rolling range
def f35ib_f35_semi_inventory_burn_invburnpos_504d_base_v045_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of sequential inventory burn (negative log change) from rolling peak
def f35ib_f35_semi_inventory_burn_invburndd_21d_base_v046_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of sequential inventory burn (negative log change) from rolling peak
def f35ib_f35_semi_inventory_burn_invburndd_63d_base_v047_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of sequential inventory burn (negative log change) from rolling peak
def f35ib_f35_semi_inventory_burn_invburndd_126d_base_v048_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of sequential inventory burn (negative log change) from rolling peak
def f35ib_f35_semi_inventory_burn_invburndd_252d_base_v049_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of sequential inventory burn (negative log change) from rolling peak
def f35ib_f35_semi_inventory_burn_invburndd_504d_base_v050_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of sequential inventory burn (negative log change) above rolling trough
def f35ib_f35_semi_inventory_burn_invburnup_21d_base_v051_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of sequential inventory burn (negative log change) above rolling trough
def f35ib_f35_semi_inventory_burn_invburnup_63d_base_v052_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of sequential inventory burn (negative log change) above rolling trough
def f35ib_f35_semi_inventory_burn_invburnup_126d_base_v053_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of sequential inventory burn (negative log change) above rolling trough
def f35ib_f35_semi_inventory_burn_invburnup_252d_base_v054_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of sequential inventory burn (negative log change) above rolling trough
def f35ib_f35_semi_inventory_burn_invburnup_504d_base_v055_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_21d_base_v056_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_63d_base_v057_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_126d_base_v058_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_252d_base_v059_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_504d_base_v060_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_21d_base_v061_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_63d_base_v062_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_126d_base_v063_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_252d_base_v064_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_504d_base_v065_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_21d_base_v066_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_63d_base_v067_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_126d_base_v068_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_252d_base_v069_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_504d_base_v070_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_21d_base_v071_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_63d_base_v072_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_126d_base_v073_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_252d_base_v074_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_504d_base_v075_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


