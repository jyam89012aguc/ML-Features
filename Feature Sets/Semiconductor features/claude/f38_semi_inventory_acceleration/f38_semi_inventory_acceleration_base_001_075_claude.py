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
def _f38ia_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f38ia_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f38ia_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f38ia_diff(a, b):
    return a - b


# 21d level of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevel_21d_base_v001_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevel_63d_base_v002_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevel_126d_base_v003_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevel_252d_base_v004_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevel_504d_base_v005_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevelrel_21d_base_v006_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevelrel_63d_base_v007_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevelrel_126d_base_v008_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevelrel_252d_base_v009_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M - _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacclevelrel_504d_base_v010_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmean_21d_base_v011_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmean_63d_base_v012_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmean_126d_base_v013_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmean_252d_base_v014_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmean_504d_base_v015_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccz_21d_base_v016_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccz_63d_base_v017_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccz_126d_base_v018_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccz_252d_base_v019_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccz_504d_base_v020_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of inventory acceleration (2nd diff) (median/MAD)
def f38ia_f38_semi_inventory_acceleration_invaccrobz_21d_base_v021_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of inventory acceleration (2nd diff) (median/MAD)
def f38ia_f38_semi_inventory_acceleration_invaccrobz_63d_base_v022_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of inventory acceleration (2nd diff) (median/MAD)
def f38ia_f38_semi_inventory_acceleration_invaccrobz_126d_base_v023_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of inventory acceleration (2nd diff) (median/MAD)
def f38ia_f38_semi_inventory_acceleration_invaccrobz_252d_base_v024_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of inventory acceleration (2nd diff) (median/MAD)
def f38ia_f38_semi_inventory_acceleration_invaccrobz_504d_base_v025_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmax_21d_base_v026_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmax_63d_base_v027_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmax_126d_base_v028_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmax_252d_base_v029_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmax_504d_base_v030_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmin_21d_base_v031_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmin_63d_base_v032_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmin_126d_base_v033_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmin_252d_base_v034_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccmin_504d_base_v035_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccrng_21d_base_v036_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccrng_63d_base_v037_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccrng_126d_base_v038_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccrng_252d_base_v039_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccrng_504d_base_v040_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of inventory acceleration (2nd diff) in rolling range
def f38ia_f38_semi_inventory_acceleration_invaccpos_21d_base_v041_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of inventory acceleration (2nd diff) in rolling range
def f38ia_f38_semi_inventory_acceleration_invaccpos_63d_base_v042_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of inventory acceleration (2nd diff) in rolling range
def f38ia_f38_semi_inventory_acceleration_invaccpos_126d_base_v043_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of inventory acceleration (2nd diff) in rolling range
def f38ia_f38_semi_inventory_acceleration_invaccpos_252d_base_v044_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of inventory acceleration (2nd diff) in rolling range
def f38ia_f38_semi_inventory_acceleration_invaccpos_504d_base_v045_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of inventory acceleration (2nd diff) from rolling peak
def f38ia_f38_semi_inventory_acceleration_invaccdd_21d_base_v046_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of inventory acceleration (2nd diff) from rolling peak
def f38ia_f38_semi_inventory_acceleration_invaccdd_63d_base_v047_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of inventory acceleration (2nd diff) from rolling peak
def f38ia_f38_semi_inventory_acceleration_invaccdd_126d_base_v048_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of inventory acceleration (2nd diff) from rolling peak
def f38ia_f38_semi_inventory_acceleration_invaccdd_252d_base_v049_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of inventory acceleration (2nd diff) from rolling peak
def f38ia_f38_semi_inventory_acceleration_invaccdd_504d_base_v050_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of inventory acceleration (2nd diff) above rolling trough
def f38ia_f38_semi_inventory_acceleration_invaccup_21d_base_v051_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of inventory acceleration (2nd diff) above rolling trough
def f38ia_f38_semi_inventory_acceleration_invaccup_63d_base_v052_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of inventory acceleration (2nd diff) above rolling trough
def f38ia_f38_semi_inventory_acceleration_invaccup_126d_base_v053_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of inventory acceleration (2nd diff) above rolling trough
def f38ia_f38_semi_inventory_acceleration_invaccup_252d_base_v054_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of inventory acceleration (2nd diff) above rolling trough
def f38ia_f38_semi_inventory_acceleration_invaccup_504d_base_v055_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccstd_21d_base_v056_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccstd_63d_base_v057_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccstd_126d_base_v058_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccstd_252d_base_v059_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccstd_504d_base_v060_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccskew_21d_base_v061_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccskew_63d_base_v062_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccskew_126d_base_v063_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccskew_252d_base_v064_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invaccskew_504d_base_v065_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacckurt_21d_base_v066_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacckurt_63d_base_v067_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacckurt_126d_base_v068_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacckurt_252d_base_v069_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacckurt_504d_base_v070_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacchits_21d_base_v071_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacchits_63d_base_v072_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacchits_126d_base_v073_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacchits_252d_base_v074_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in inventory acceleration (2nd diff)
def f38ia_f38_semi_inventory_acceleration_invacchits_504d_base_v075_signal(inventory, closeadj):
    M = _f38ia_log_change(inventory, 21).diff(periods=21)
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


