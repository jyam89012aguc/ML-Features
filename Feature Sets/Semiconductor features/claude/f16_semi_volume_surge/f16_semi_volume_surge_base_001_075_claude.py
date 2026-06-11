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
def _f16_log_vol(volume):
    return np.log(volume.replace(0, np.nan).abs())


def _f16_surge_ratio(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _f16_log_surge(volume, w):
    return np.log(volume.replace(0, np.nan) / _mean(volume, w).replace(0, np.nan))


# 21d log-volume level vs 21d mean
def f16vs_f16_semi_volume_surge_vollevel_21d_base_v001_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _mean(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-volume level vs 63d mean
def f16vs_f16_semi_volume_surge_vollevel_63d_base_v002_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _mean(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-volume level vs 126d mean
def f16vs_f16_semi_volume_surge_vollevel_126d_base_v003_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _mean(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-volume level vs 252d mean
def f16vs_f16_semi_volume_surge_vollevel_252d_base_v004_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _mean(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-volume level vs 504d mean
def f16vs_f16_semi_volume_surge_vollevel_504d_base_v005_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _mean(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of log-volume
def f16vs_f16_semi_volume_surge_volz_21d_base_v006_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log-volume
def f16vs_f16_semi_volume_surge_volz_63d_base_v007_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log-volume
def f16vs_f16_semi_volume_surge_volz_126d_base_v008_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log-volume
def f16vs_f16_semi_volume_surge_volz_252d_base_v009_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log-volume
def f16vs_f16_semi_volume_surge_volz_504d_base_v010_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _z(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of log-volume (median/MAD)
def f16vs_f16_semi_volume_surge_volrobustz_21d_base_v011_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    med = v.rolling(21, min_periods=11).median()
    mad = (v - med).abs().rolling(21, min_periods=11).median()
    result = (v - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of log-volume (median/MAD)
def f16vs_f16_semi_volume_surge_volrobustz_63d_base_v012_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    med = v.rolling(63, min_periods=32).median()
    mad = (v - med).abs().rolling(63, min_periods=32).median()
    result = (v - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of log-volume (median/MAD)
def f16vs_f16_semi_volume_surge_volrobustz_126d_base_v013_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    med = v.rolling(126, min_periods=63).median()
    mad = (v - med).abs().rolling(126, min_periods=63).median()
    result = (v - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of log-volume (median/MAD)
def f16vs_f16_semi_volume_surge_volrobustz_252d_base_v014_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    med = v.rolling(252, min_periods=126).median()
    mad = (v - med).abs().rolling(252, min_periods=126).median()
    result = (v - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of log-volume (median/MAD)
def f16vs_f16_semi_volume_surge_volrobustz_504d_base_v015_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    med = v.rolling(504, min_periods=252).median()
    mad = (v - med).abs().rolling(504, min_periods=252).median()
    result = (v - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d surge ratio (volume / 21d mean)
def f16vs_f16_semi_volume_surge_surge_21d_base_v016_signal(volume, closeadj):
    result = _f16_surge_ratio(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d surge ratio (volume / 63d mean)
def f16vs_f16_semi_volume_surge_surge_63d_base_v017_signal(volume, closeadj):
    result = _f16_surge_ratio(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d surge ratio (volume / 126d mean)
def f16vs_f16_semi_volume_surge_surge_126d_base_v018_signal(volume, closeadj):
    result = _f16_surge_ratio(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d surge ratio (volume / 252d mean)
def f16vs_f16_semi_volume_surge_surge_252d_base_v019_signal(volume, closeadj):
    result = _f16_surge_ratio(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d surge ratio (volume / 504d mean)
def f16vs_f16_semi_volume_surge_surge_504d_base_v020_signal(volume, closeadj):
    result = _f16_surge_ratio(volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log-surge ratio
def f16vs_f16_semi_volume_surge_logsurge_21d_base_v021_signal(volume, closeadj):
    result = _f16_log_surge(volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d log-surge ratio
def f16vs_f16_semi_volume_surge_logsurge_63d_base_v022_signal(volume, closeadj):
    result = _f16_log_surge(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d log-surge ratio
def f16vs_f16_semi_volume_surge_logsurge_126d_base_v023_signal(volume, closeadj):
    result = _f16_log_surge(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log-surge ratio
def f16vs_f16_semi_volume_surge_logsurge_252d_base_v024_signal(volume, closeadj):
    result = _f16_log_surge(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log-surge ratio
def f16vs_f16_semi_volume_surge_logsurge_504d_base_v025_signal(volume, closeadj):
    result = _f16_log_surge(volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of log-volume
def f16vs_f16_semi_volume_surge_volmax_21d_base_v026_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of log-volume
def f16vs_f16_semi_volume_surge_volmax_63d_base_v027_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of log-volume
def f16vs_f16_semi_volume_surge_volmax_126d_base_v028_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of log-volume
def f16vs_f16_semi_volume_surge_volmax_252d_base_v029_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of log-volume
def f16vs_f16_semi_volume_surge_volmax_504d_base_v030_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of log-volume
def f16vs_f16_semi_volume_surge_volmin_21d_base_v031_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _min(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of log-volume
def f16vs_f16_semi_volume_surge_volmin_63d_base_v032_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _min(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of log-volume
def f16vs_f16_semi_volume_surge_volmin_126d_base_v033_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _min(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of log-volume
def f16vs_f16_semi_volume_surge_volmin_252d_base_v034_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _min(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of log-volume
def f16vs_f16_semi_volume_surge_volmin_504d_base_v035_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _min(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of log-volume (max - min)
def f16vs_f16_semi_volume_surge_volrng_21d_base_v036_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 21) - _min(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of log-volume
def f16vs_f16_semi_volume_surge_volrng_63d_base_v037_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 63) - _min(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of log-volume
def f16vs_f16_semi_volume_surge_volrng_126d_base_v038_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 126) - _min(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of log-volume
def f16vs_f16_semi_volume_surge_volrng_252d_base_v039_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 252) - _min(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of log-volume
def f16vs_f16_semi_volume_surge_volrng_504d_base_v040_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = _max(v, 504) - _min(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of log-volume
def f16vs_f16_semi_volume_surge_volpos_21d_base_v041_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    lo = _min(v, 21)
    hi = _max(v, 21)
    result = (v - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of log-volume
def f16vs_f16_semi_volume_surge_volpos_63d_base_v042_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    lo = _min(v, 63)
    hi = _max(v, 63)
    result = (v - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of log-volume
def f16vs_f16_semi_volume_surge_volpos_126d_base_v043_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    lo = _min(v, 126)
    hi = _max(v, 126)
    result = (v - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of log-volume
def f16vs_f16_semi_volume_surge_volpos_252d_base_v044_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    lo = _min(v, 252)
    hi = _max(v, 252)
    result = (v - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of log-volume
def f16vs_f16_semi_volume_surge_volpos_504d_base_v045_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    lo = _min(v, 504)
    hi = _max(v, 504)
    result = (v - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of log-volume from peak
def f16vs_f16_semi_volume_surge_voldd_21d_base_v046_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _max(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of log-volume from peak
def f16vs_f16_semi_volume_surge_voldd_63d_base_v047_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _max(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of log-volume from peak
def f16vs_f16_semi_volume_surge_voldd_126d_base_v048_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _max(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of log-volume from peak
def f16vs_f16_semi_volume_surge_voldd_252d_base_v049_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _max(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of log-volume from peak
def f16vs_f16_semi_volume_surge_voldd_504d_base_v050_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _max(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of log-volume above trough
def f16vs_f16_semi_volume_surge_volup_21d_base_v051_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _min(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of log-volume above trough
def f16vs_f16_semi_volume_surge_volup_63d_base_v052_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _min(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of log-volume above trough
def f16vs_f16_semi_volume_surge_volup_126d_base_v053_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _min(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of log-volume above trough
def f16vs_f16_semi_volume_surge_volup_252d_base_v054_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _min(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of log-volume above trough
def f16vs_f16_semi_volume_surge_volup_504d_base_v055_signal(volume, closeadj):
    v = _f16_log_vol(volume)
    result = v - _min(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of log-volume changes
def f16vs_f16_semi_volume_surge_volstd_21d_base_v056_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = _std(v, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of log-volume changes
def f16vs_f16_semi_volume_surge_volstd_63d_base_v057_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = _std(v, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of log-volume changes
def f16vs_f16_semi_volume_surge_volstd_126d_base_v058_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = _std(v, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of log-volume changes
def f16vs_f16_semi_volume_surge_volstd_252d_base_v059_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = _std(v, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of log-volume changes
def f16vs_f16_semi_volume_surge_volstd_504d_base_v060_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = _std(v, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of log-volume changes
def f16vs_f16_semi_volume_surge_volskew_21d_base_v061_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of log-volume changes
def f16vs_f16_semi_volume_surge_volskew_63d_base_v062_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of log-volume changes
def f16vs_f16_semi_volume_surge_volskew_126d_base_v063_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of log-volume changes
def f16vs_f16_semi_volume_surge_volskew_252d_base_v064_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of log-volume changes
def f16vs_f16_semi_volume_surge_volskew_504d_base_v065_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of log-volume changes
def f16vs_f16_semi_volume_surge_volkurt_21d_base_v066_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of log-volume changes
def f16vs_f16_semi_volume_surge_volkurt_63d_base_v067_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of log-volume changes
def f16vs_f16_semi_volume_surge_volkurt_126d_base_v068_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of log-volume changes
def f16vs_f16_semi_volume_surge_volkurt_252d_base_v069_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of log-volume changes
def f16vs_f16_semi_volume_surge_volkurt_504d_base_v070_signal(volume, closeadj):
    v = _f16_log_vol(volume).diff()
    result = v.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of surge days (volume > 1.5x 21d mean)
def f16vs_f16_semi_volume_surge_surgehits_21d_base_v071_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 21)
    result = (ratio > 1.5).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of surge days
def f16vs_f16_semi_volume_surge_surgehits_63d_base_v072_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 63)
    result = (ratio > 1.5).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of surge days
def f16vs_f16_semi_volume_surge_surgehits_126d_base_v073_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 126)
    result = (ratio > 1.5).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of surge days
def f16vs_f16_semi_volume_surge_surgehits_252d_base_v074_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 252)
    result = (ratio > 1.5).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of surge days
def f16vs_f16_semi_volume_surge_surgehits_504d_base_v075_signal(volume, closeadj):
    ratio = _f16_surge_ratio(volume, 504)
    result = (ratio > 1.5).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)
