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
def _f36dio_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f36dio_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f36dio_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f36dio_diff(a, b):
    return a - b


# 21d level of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevel_21d_base_v001_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevel_63d_base_v002_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevel_126d_base_v003_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevel_252d_base_v004_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevel_504d_base_v005_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M
    return result.replace([np.inf, -np.inf], np.nan)


# 21d level vs 63d mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevelrel_21d_base_v006_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M - _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level vs 126d mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevelrel_63d_base_v007_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M - _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level vs 252d mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevelrel_126d_base_v008_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M - _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level vs 504d mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevelrel_252d_base_v009_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M - _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level vs 756d mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendlevelrel_504d_base_v010_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M - _mean(M, 756)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmean_21d_base_v011_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _mean(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmean_63d_base_v012_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _mean(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmean_126d_base_v013_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _mean(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmean_252d_base_v014_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _mean(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling mean of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmean_504d_base_v015_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _mean(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendz_21d_base_v016_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _z(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendz_63d_base_v017_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _z(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendz_126d_base_v018_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _z(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendz_252d_base_v019_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _z(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendz_504d_base_v020_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _z(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z-score of days inventory outstanding trend (revenue-proxy) (median/MAD)
def f36dio_f36_semi_dio_trend_diotrendrobz_21d_base_v021_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    med = M.rolling(21, min_periods=10).median()
    mad = (M - med).abs().rolling(21, min_periods=10).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z-score of days inventory outstanding trend (revenue-proxy) (median/MAD)
def f36dio_f36_semi_dio_trend_diotrendrobz_63d_base_v022_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    med = M.rolling(63, min_periods=31).median()
    mad = (M - med).abs().rolling(63, min_periods=31).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z-score of days inventory outstanding trend (revenue-proxy) (median/MAD)
def f36dio_f36_semi_dio_trend_diotrendrobz_126d_base_v023_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    med = M.rolling(126, min_periods=63).median()
    mad = (M - med).abs().rolling(126, min_periods=63).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z-score of days inventory outstanding trend (revenue-proxy) (median/MAD)
def f36dio_f36_semi_dio_trend_diotrendrobz_252d_base_v024_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    mad = (M - med).abs().rolling(252, min_periods=126).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z-score of days inventory outstanding trend (revenue-proxy) (median/MAD)
def f36dio_f36_semi_dio_trend_diotrendrobz_504d_base_v025_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    result = (M - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmax_21d_base_v026_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmax_63d_base_v027_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmax_126d_base_v028_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmax_252d_base_v029_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmax_504d_base_v030_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmin_21d_base_v031_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmin_63d_base_v032_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmin_126d_base_v033_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmin_252d_base_v034_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendmin_504d_base_v035_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendrng_21d_base_v036_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 21) - _min(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendrng_63d_base_v037_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 63) - _min(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendrng_126d_base_v038_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 126) - _min(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendrng_252d_base_v039_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 252) - _min(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendrng_504d_base_v040_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _max(M, 504) - _min(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position of days inventory outstanding trend (revenue-proxy) in rolling range
def f36dio_f36_semi_dio_trend_diotrendpos_21d_base_v041_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    lo = _min(M, 21)
    hi = _max(M, 21)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position of days inventory outstanding trend (revenue-proxy) in rolling range
def f36dio_f36_semi_dio_trend_diotrendpos_63d_base_v042_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    lo = _min(M, 63)
    hi = _max(M, 63)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position of days inventory outstanding trend (revenue-proxy) in rolling range
def f36dio_f36_semi_dio_trend_diotrendpos_126d_base_v043_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    lo = _min(M, 126)
    hi = _max(M, 126)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position of days inventory outstanding trend (revenue-proxy) in rolling range
def f36dio_f36_semi_dio_trend_diotrendpos_252d_base_v044_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    lo = _min(M, 252)
    hi = _max(M, 252)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position of days inventory outstanding trend (revenue-proxy) in rolling range
def f36dio_f36_semi_dio_trend_diotrendpos_504d_base_v045_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    lo = _min(M, 504)
    hi = _max(M, 504)
    result = (M - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of days inventory outstanding trend (revenue-proxy) from rolling peak
def f36dio_f36_semi_dio_trend_diotrenddd_21d_base_v046_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    peak = _max(M, 21)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of days inventory outstanding trend (revenue-proxy) from rolling peak
def f36dio_f36_semi_dio_trend_diotrenddd_63d_base_v047_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    peak = _max(M, 63)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of days inventory outstanding trend (revenue-proxy) from rolling peak
def f36dio_f36_semi_dio_trend_diotrenddd_126d_base_v048_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    peak = _max(M, 126)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of days inventory outstanding trend (revenue-proxy) from rolling peak
def f36dio_f36_semi_dio_trend_diotrenddd_252d_base_v049_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    peak = _max(M, 252)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of days inventory outstanding trend (revenue-proxy) from rolling peak
def f36dio_f36_semi_dio_trend_diotrenddd_504d_base_v050_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    peak = _max(M, 504)
    result = M - peak
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of days inventory outstanding trend (revenue-proxy) above rolling trough
def f36dio_f36_semi_dio_trend_diotrendup_21d_base_v051_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    trough = _min(M, 21)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of days inventory outstanding trend (revenue-proxy) above rolling trough
def f36dio_f36_semi_dio_trend_diotrendup_63d_base_v052_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    trough = _min(M, 63)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of days inventory outstanding trend (revenue-proxy) above rolling trough
def f36dio_f36_semi_dio_trend_diotrendup_126d_base_v053_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    trough = _min(M, 126)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of days inventory outstanding trend (revenue-proxy) above rolling trough
def f36dio_f36_semi_dio_trend_diotrendup_252d_base_v054_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    trough = _min(M, 252)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of days inventory outstanding trend (revenue-proxy) above rolling trough
def f36dio_f36_semi_dio_trend_diotrendup_504d_base_v055_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    trough = _min(M, 504)
    result = M - trough
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendstd_21d_base_v056_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _std(M, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendstd_63d_base_v057_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _std(M, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendstd_126d_base_v058_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _std(M, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendstd_252d_base_v059_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _std(M, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendstd_504d_base_v060_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = _std(M, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendskew_21d_base_v061_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendskew_63d_base_v062_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendskew_126d_base_v063_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendskew_252d_base_v064_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendskew_504d_base_v065_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendkurt_21d_base_v066_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendkurt_63d_base_v067_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendkurt_126d_base_v068_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendkurt_252d_base_v069_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendkurt_504d_base_v070_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = M.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d hit ratio of positive change in days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendhits_21d_base_v071_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = (M.diff() > 0).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d hit ratio of positive change in days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendhits_63d_base_v072_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = (M.diff() > 0).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d hit ratio of positive change in days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendhits_126d_base_v073_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = (M.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d hit ratio of positive change in days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendhits_252d_base_v074_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = (M.diff() > 0).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d hit ratio of positive change in days inventory outstanding trend (revenue-proxy)
def f36dio_f36_semi_dio_trend_diotrendhits_504d_base_v075_signal(inventory, revenue, closeadj):
    M = _f36dio_ratio(inventory, revenue) * 365
    result = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)


