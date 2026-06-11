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
def _f18_amihud(closeadj, volume):
    ret = closeadj.pct_change().abs()
    dv = closeadj * volume
    return ret / dv.replace(0, np.nan)


def _f18_log_amihud(closeadj, volume):
    a = _f18_amihud(closeadj, volume)
    return np.log(a.replace(0, np.nan).abs() + 1e-30)


# 21d level of log Amihud illiquidity vs 21d mean
def f18ai_f18_semi_amihud_illiquidity_ailevel_21d_base_v001_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _mean(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of log Amihud illiquidity vs 63d mean
def f18ai_f18_semi_amihud_illiquidity_ailevel_63d_base_v002_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _mean(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of log Amihud illiquidity vs 126d mean
def f18ai_f18_semi_amihud_illiquidity_ailevel_126d_base_v003_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of log Amihud illiquidity vs 252d mean
def f18ai_f18_semi_amihud_illiquidity_ailevel_252d_base_v004_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of log Amihud illiquidity vs 504d mean
def f18ai_f18_semi_amihud_illiquidity_ailevel_504d_base_v005_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aiz_21d_base_v006_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _z(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aiz_63d_base_v007_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aiz_126d_base_v008_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aiz_252d_base_v009_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aiz_504d_base_v010_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of log Amihud illiquidity (median/MAD)
def f18ai_f18_semi_amihud_illiquidity_airobustz_21d_base_v011_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of log Amihud illiquidity (median/MAD)
def f18ai_f18_semi_amihud_illiquidity_airobustz_63d_base_v012_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of log Amihud illiquidity (median/MAD)
def f18ai_f18_semi_amihud_illiquidity_airobustz_126d_base_v013_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of log Amihud illiquidity (median/MAD)
def f18ai_f18_semi_amihud_illiquidity_airobustz_252d_base_v014_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of log Amihud illiquidity (median/MAD)
def f18ai_f18_semi_amihud_illiquidity_airobustz_504d_base_v015_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimax_21d_base_v016_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimax_63d_base_v017_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimax_126d_base_v018_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimax_252d_base_v019_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimax_504d_base_v020_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimin_21d_base_v021_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimin_63d_base_v022_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimin_126d_base_v023_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimin_252d_base_v024_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aimin_504d_base_v025_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_airng_21d_base_v026_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 21) - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_airng_63d_base_v027_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 63) - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_airng_126d_base_v028_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 126) - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_airng_252d_base_v029_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 252) - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_airng_504d_base_v030_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = _max(s, 504) - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aipos_21d_base_v031_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    lo = _min(s, 21)
    hi = _max(s, 21)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aipos_63d_base_v032_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    lo = _min(s, 63)
    hi = _max(s, 63)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aipos_126d_base_v033_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    lo = _min(s, 126)
    hi = _max(s, 126)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aipos_252d_base_v034_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    lo = _min(s, 252)
    hi = _max(s, 252)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aipos_504d_base_v035_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    lo = _min(s, 504)
    hi = _max(s, 504)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of log Amihud illiquidity from peak
def f18ai_f18_semi_amihud_illiquidity_aidd_21d_base_v036_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of log Amihud illiquidity from peak
def f18ai_f18_semi_amihud_illiquidity_aidd_63d_base_v037_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of log Amihud illiquidity from peak
def f18ai_f18_semi_amihud_illiquidity_aidd_126d_base_v038_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of log Amihud illiquidity from peak
def f18ai_f18_semi_amihud_illiquidity_aidd_252d_base_v039_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of log Amihud illiquidity from peak
def f18ai_f18_semi_amihud_illiquidity_aidd_504d_base_v040_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of log Amihud illiquidity above trough
def f18ai_f18_semi_amihud_illiquidity_aiup_21d_base_v041_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of log Amihud illiquidity above trough
def f18ai_f18_semi_amihud_illiquidity_aiup_63d_base_v042_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of log Amihud illiquidity above trough
def f18ai_f18_semi_amihud_illiquidity_aiup_126d_base_v043_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of log Amihud illiquidity above trough
def f18ai_f18_semi_amihud_illiquidity_aiup_252d_base_v044_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of log Amihud illiquidity above trough
def f18ai_f18_semi_amihud_illiquidity_aiup_504d_base_v045_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    result = s - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aistd_21d_base_v046_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = _std(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aistd_63d_base_v047_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = _std(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aistd_126d_base_v048_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = _std(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aistd_252d_base_v049_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = _std(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aistd_504d_base_v050_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = _std(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aiskew_21d_base_v051_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aiskew_63d_base_v052_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aiskew_126d_base_v053_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aiskew_252d_base_v054_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aiskew_504d_base_v055_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aikurt_21d_base_v056_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aikurt_63d_base_v057_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aikurt_126d_base_v058_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aikurt_252d_base_v059_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of log Amihud illiquidity changes
def f18ai_f18_semi_amihud_illiquidity_aikurt_504d_base_v060_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume).diff()
    result = s.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative change in log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aisigncum_21d_base_v061_signal(closeadj, volume):
    d = _f18_log_amihud(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aisigncum_63d_base_v062_signal(closeadj, volume):
    d = _f18_log_amihud(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aisigncum_126d_base_v063_signal(closeadj, volume):
    d = _f18_log_amihud(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aisigncum_252d_base_v064_signal(closeadj, volume):
    d = _f18_log_amihud(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in log Amihud illiquidity
def f18ai_f18_semi_amihud_illiquidity_aisigncum_504d_base_v065_signal(closeadj, volume):
    d = _f18_log_amihud(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aihits_21d_base_v066_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aihits_63d_base_v067_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aihits_126d_base_v068_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aihits_252d_base_v069_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aihits_504d_base_v070_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aifrac_21d_base_v071_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aifrac_63d_base_v072_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aifrac_126d_base_v073_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aifrac_252d_base_v074_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days log Amihud illiquidity z > 1
def f18ai_f18_semi_amihud_illiquidity_aifrac_504d_base_v075_signal(closeadj, volume):
    s = _f18_log_amihud(closeadj, volume)
    z = _z(s, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)

