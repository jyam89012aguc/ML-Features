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
def _f31cpe_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f31cpe_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f31cpe_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f31cpe_diff(a, b):
    return a - b


# 21d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_21d_base_v001_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_63d_base_v002_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_126d_base_v003_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_252d_base_v004_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_504d_base_v005_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_21d_base_v006_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_63d_base_v007_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_126d_base_v008_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_252d_base_v009_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_504d_base_v010_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_21d_base_v011_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_63d_base_v012_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_126d_base_v013_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_252d_base_v014_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_504d_base_v015_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_21d_base_v016_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_63d_base_v017_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_126d_base_v018_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_252d_base_v019_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_504d_base_v020_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of capex efficiency (capex/ppne) (median/MAD)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_21d_base_v021_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of capex efficiency (capex/ppne) (median/MAD)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_63d_base_v022_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of capex efficiency (capex/ppne) (median/MAD)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_126d_base_v023_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of capex efficiency (capex/ppne) (median/MAD)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_252d_base_v024_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of capex efficiency (capex/ppne) (median/MAD)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_504d_base_v025_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_21d_base_v026_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_63d_base_v027_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_126d_base_v028_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_252d_base_v029_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_504d_base_v030_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_21d_base_v031_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_63d_base_v032_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_126d_base_v033_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_252d_base_v034_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_504d_base_v035_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_21d_base_v036_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_63d_base_v037_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_126d_base_v038_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_252d_base_v039_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_504d_base_v040_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of capex efficiency (capex/ppne) in rolling range
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_21d_base_v041_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of capex efficiency (capex/ppne) in rolling range
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_63d_base_v042_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of capex efficiency (capex/ppne) in rolling range
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_126d_base_v043_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of capex efficiency (capex/ppne) in rolling range
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_252d_base_v044_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of capex efficiency (capex/ppne) in rolling range
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_504d_base_v045_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of capex efficiency (capex/ppne) from rolling peak
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_21d_base_v046_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of capex efficiency (capex/ppne) from rolling peak
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_63d_base_v047_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of capex efficiency (capex/ppne) from rolling peak
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_126d_base_v048_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of capex efficiency (capex/ppne) from rolling peak
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_252d_base_v049_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of capex efficiency (capex/ppne) from rolling peak
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_504d_base_v050_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of capex efficiency (capex/ppne) above rolling trough
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_21d_base_v051_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of capex efficiency (capex/ppne) above rolling trough
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_63d_base_v052_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of capex efficiency (capex/ppne) above rolling trough
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_126d_base_v053_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of capex efficiency (capex/ppne) above rolling trough
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_252d_base_v054_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of capex efficiency (capex/ppne) above rolling trough
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_504d_base_v055_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_21d_base_v056_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_63d_base_v057_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_126d_base_v058_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_252d_base_v059_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_504d_base_v060_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_21d_base_v061_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_63d_base_v062_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_126d_base_v063_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_252d_base_v064_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_504d_base_v065_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_21d_base_v066_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_63d_base_v067_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_126d_base_v068_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_252d_base_v069_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_504d_base_v070_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_21d_base_v071_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_63d_base_v072_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_126d_base_v073_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_252d_base_v074_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_504d_base_v075_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


