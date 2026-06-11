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
def _f34igr_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f34igr_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f34igr_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f34igr_diff(a, b):
    return a - b


# 21d level of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevel_21d_base_v001_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevel_63d_base_v002_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevel_126d_base_v003_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevel_252d_base_v004_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevel_504d_base_v005_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevelrel_21d_base_v006_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevelrel_63d_base_v007_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevelrel_126d_base_v008_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevelrel_252d_base_v009_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M - _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevlevelrel_504d_base_v010_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmean_21d_base_v011_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmean_63d_base_v012_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmean_126d_base_v013_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmean_252d_base_v014_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmean_504d_base_v015_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevz_21d_base_v016_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevz_63d_base_v017_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevz_126d_base_v018_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevz_252d_base_v019_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevz_504d_base_v020_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of inventory growth minus revenue growth (median/MAD)
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrobz_21d_base_v021_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of inventory growth minus revenue growth (median/MAD)
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrobz_63d_base_v022_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of inventory growth minus revenue growth (median/MAD)
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrobz_126d_base_v023_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of inventory growth minus revenue growth (median/MAD)
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrobz_252d_base_v024_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of inventory growth minus revenue growth (median/MAD)
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrobz_504d_base_v025_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmax_21d_base_v026_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmax_63d_base_v027_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmax_126d_base_v028_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmax_252d_base_v029_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmax_504d_base_v030_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmin_21d_base_v031_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmin_63d_base_v032_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmin_126d_base_v033_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmin_252d_base_v034_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevmin_504d_base_v035_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrng_21d_base_v036_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrng_63d_base_v037_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrng_126d_base_v038_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrng_252d_base_v039_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevrng_504d_base_v040_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of inventory growth minus revenue growth in rolling range
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevpos_21d_base_v041_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of inventory growth minus revenue growth in rolling range
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevpos_63d_base_v042_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of inventory growth minus revenue growth in rolling range
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevpos_126d_base_v043_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of inventory growth minus revenue growth in rolling range
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevpos_252d_base_v044_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of inventory growth minus revenue growth in rolling range
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevpos_504d_base_v045_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of inventory growth minus revenue growth from rolling peak
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevdd_21d_base_v046_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of inventory growth minus revenue growth from rolling peak
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevdd_63d_base_v047_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of inventory growth minus revenue growth from rolling peak
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevdd_126d_base_v048_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of inventory growth minus revenue growth from rolling peak
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevdd_252d_base_v049_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of inventory growth minus revenue growth from rolling peak
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevdd_504d_base_v050_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of inventory growth minus revenue growth above rolling trough
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevup_21d_base_v051_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of inventory growth minus revenue growth above rolling trough
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevup_63d_base_v052_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of inventory growth minus revenue growth above rolling trough
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevup_126d_base_v053_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of inventory growth minus revenue growth above rolling trough
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevup_252d_base_v054_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of inventory growth minus revenue growth above rolling trough
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevup_504d_base_v055_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevstd_21d_base_v056_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevstd_63d_base_v057_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevstd_126d_base_v058_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevstd_252d_base_v059_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevstd_504d_base_v060_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevskew_21d_base_v061_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevskew_63d_base_v062_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevskew_126d_base_v063_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevskew_252d_base_v064_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevskew_504d_base_v065_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevkurt_21d_base_v066_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevkurt_63d_base_v067_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevkurt_126d_base_v068_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevkurt_252d_base_v069_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevkurt_504d_base_v070_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevhits_21d_base_v071_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevhits_63d_base_v072_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevhits_126d_base_v073_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevhits_252d_base_v074_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in inventory growth minus revenue growth
def f34igr_f34_semi_inventory_growth_vs_revenue_invrevhits_504d_base_v075_signal(inventory, revenue, closeadj):
    M = _f34igr_diff(_f34igr_log_change(inventory, 63), _f34igr_log_change(revenue, 63))
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


