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
def _f37iat_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f37iat_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f37iat_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f37iat_diff(a, b):
    return a - b


# 21d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_21d_base_v001_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_63d_base_v002_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_126d_base_v003_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_252d_base_v004_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_504d_base_v005_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_21d_base_v006_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_63d_base_v007_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_126d_base_v008_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_252d_base_v009_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_504d_base_v010_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_21d_base_v011_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_63d_base_v012_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_126d_base_v013_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_252d_base_v014_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_504d_base_v015_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_21d_base_v016_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_63d_base_v017_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_126d_base_v018_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_252d_base_v019_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_504d_base_v020_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of inventory to assets ratio (median/MAD)
def f37iat_f37_semi_inventory_to_assets_invastrobz_21d_base_v021_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of inventory to assets ratio (median/MAD)
def f37iat_f37_semi_inventory_to_assets_invastrobz_63d_base_v022_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of inventory to assets ratio (median/MAD)
def f37iat_f37_semi_inventory_to_assets_invastrobz_126d_base_v023_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of inventory to assets ratio (median/MAD)
def f37iat_f37_semi_inventory_to_assets_invastrobz_252d_base_v024_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of inventory to assets ratio (median/MAD)
def f37iat_f37_semi_inventory_to_assets_invastrobz_504d_base_v025_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_21d_base_v026_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_63d_base_v027_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_126d_base_v028_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_252d_base_v029_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_504d_base_v030_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_21d_base_v031_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_63d_base_v032_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_126d_base_v033_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_252d_base_v034_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_504d_base_v035_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_21d_base_v036_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_63d_base_v037_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_126d_base_v038_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_252d_base_v039_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_504d_base_v040_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of inventory to assets ratio in rolling range
def f37iat_f37_semi_inventory_to_assets_invastpos_21d_base_v041_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of inventory to assets ratio in rolling range
def f37iat_f37_semi_inventory_to_assets_invastpos_63d_base_v042_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of inventory to assets ratio in rolling range
def f37iat_f37_semi_inventory_to_assets_invastpos_126d_base_v043_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of inventory to assets ratio in rolling range
def f37iat_f37_semi_inventory_to_assets_invastpos_252d_base_v044_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of inventory to assets ratio in rolling range
def f37iat_f37_semi_inventory_to_assets_invastpos_504d_base_v045_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of inventory to assets ratio from rolling peak
def f37iat_f37_semi_inventory_to_assets_invastdd_21d_base_v046_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of inventory to assets ratio from rolling peak
def f37iat_f37_semi_inventory_to_assets_invastdd_63d_base_v047_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of inventory to assets ratio from rolling peak
def f37iat_f37_semi_inventory_to_assets_invastdd_126d_base_v048_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of inventory to assets ratio from rolling peak
def f37iat_f37_semi_inventory_to_assets_invastdd_252d_base_v049_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of inventory to assets ratio from rolling peak
def f37iat_f37_semi_inventory_to_assets_invastdd_504d_base_v050_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of inventory to assets ratio above rolling trough
def f37iat_f37_semi_inventory_to_assets_invastup_21d_base_v051_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of inventory to assets ratio above rolling trough
def f37iat_f37_semi_inventory_to_assets_invastup_63d_base_v052_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of inventory to assets ratio above rolling trough
def f37iat_f37_semi_inventory_to_assets_invastup_126d_base_v053_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of inventory to assets ratio above rolling trough
def f37iat_f37_semi_inventory_to_assets_invastup_252d_base_v054_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of inventory to assets ratio above rolling trough
def f37iat_f37_semi_inventory_to_assets_invastup_504d_base_v055_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_21d_base_v056_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_63d_base_v057_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_126d_base_v058_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_252d_base_v059_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_504d_base_v060_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_21d_base_v061_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_63d_base_v062_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_126d_base_v063_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_252d_base_v064_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_504d_base_v065_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_21d_base_v066_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_63d_base_v067_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_126d_base_v068_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_252d_base_v069_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_504d_base_v070_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_21d_base_v071_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_63d_base_v072_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_126d_base_v073_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_252d_base_v074_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_504d_base_v075_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


