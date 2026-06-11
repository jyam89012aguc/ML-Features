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
def _f20_ret(closeadj):
    return closeadj.pct_change()


def _f20_log_vol(volume):
    return np.log(volume.replace(0, np.nan).abs())


def _f20_divergence(closeadj, volume):
    r = _f20_ret(closeadj)
    v = _f20_log_vol(volume).diff()
    return v * (-np.sign(r))


# 21d level of volume-price divergence vs 21d mean
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_21d_base_v001_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _mean(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of volume-price divergence vs 63d mean
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_63d_base_v002_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _mean(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of volume-price divergence vs 126d mean
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_126d_base_v003_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of volume-price divergence vs 252d mean
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_252d_base_v004_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of volume-price divergence vs 504d mean
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_504d_base_v005_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_21d_base_v006_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _z(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_63d_base_v007_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_126d_base_v008_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_252d_base_v009_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_504d_base_v010_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of volume-price divergence (median/MAD)
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_21d_base_v011_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of volume-price divergence (median/MAD)
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_63d_base_v012_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of volume-price divergence (median/MAD)
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_126d_base_v013_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of volume-price divergence (median/MAD)
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_252d_base_v014_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of volume-price divergence (median/MAD)
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_504d_base_v015_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_21d_base_v016_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_63d_base_v017_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_126d_base_v018_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_252d_base_v019_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_504d_base_v020_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmin_21d_base_v021_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmin_63d_base_v022_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmin_126d_base_v023_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmin_252d_base_v024_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmin_504d_base_v025_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrng_21d_base_v026_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 21) - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrng_63d_base_v027_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 63) - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrng_126d_base_v028_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 126) - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrng_252d_base_v029_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 252) - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrng_504d_base_v030_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = _max(s, 504) - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdpos_21d_base_v031_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    lo = _min(s, 21)
    hi = _max(s, 21)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdpos_63d_base_v032_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    lo = _min(s, 63)
    hi = _max(s, 63)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdpos_126d_base_v033_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    lo = _min(s, 126)
    hi = _max(s, 126)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdpos_252d_base_v034_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    lo = _min(s, 252)
    hi = _max(s, 252)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdpos_504d_base_v035_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    lo = _min(s, 504)
    hi = _max(s, 504)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of volume-price divergence from peak
def f20vpd_f20_semi_volume_price_divergence_vpddd_21d_base_v036_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of volume-price divergence from peak
def f20vpd_f20_semi_volume_price_divergence_vpddd_63d_base_v037_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of volume-price divergence from peak
def f20vpd_f20_semi_volume_price_divergence_vpddd_126d_base_v038_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of volume-price divergence from peak
def f20vpd_f20_semi_volume_price_divergence_vpddd_252d_base_v039_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of volume-price divergence from peak
def f20vpd_f20_semi_volume_price_divergence_vpddd_504d_base_v040_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of volume-price divergence above trough
def f20vpd_f20_semi_volume_price_divergence_vpdup_21d_base_v041_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of volume-price divergence above trough
def f20vpd_f20_semi_volume_price_divergence_vpdup_63d_base_v042_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of volume-price divergence above trough
def f20vpd_f20_semi_volume_price_divergence_vpdup_126d_base_v043_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of volume-price divergence above trough
def f20vpd_f20_semi_volume_price_divergence_vpdup_252d_base_v044_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of volume-price divergence above trough
def f20vpd_f20_semi_volume_price_divergence_vpdup_504d_base_v045_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    result = s - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdstd_21d_base_v046_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = _std(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdstd_63d_base_v047_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = _std(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdstd_126d_base_v048_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = _std(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdstd_252d_base_v049_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = _std(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdstd_504d_base_v050_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = _std(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdskew_21d_base_v051_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdskew_63d_base_v052_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdskew_126d_base_v053_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdskew_252d_base_v054_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdskew_504d_base_v055_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdkurt_21d_base_v056_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdkurt_63d_base_v057_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdkurt_126d_base_v058_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdkurt_252d_base_v059_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of volume-price divergence changes
def f20vpd_f20_semi_volume_price_divergence_vpdkurt_504d_base_v060_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume).diff()
    result = s.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative change in volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdsigncum_21d_base_v061_signal(closeadj, volume):
    d = _f20_divergence(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdsigncum_63d_base_v062_signal(closeadj, volume):
    d = _f20_divergence(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdsigncum_126d_base_v063_signal(closeadj, volume):
    d = _f20_divergence(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdsigncum_252d_base_v064_signal(closeadj, volume):
    d = _f20_divergence(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdsigncum_504d_base_v065_signal(closeadj, volume):
    d = _f20_divergence(closeadj, volume).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdhits_21d_base_v066_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdhits_63d_base_v067_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdhits_126d_base_v068_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdhits_252d_base_v069_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdhits_504d_base_v070_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdfrac_21d_base_v071_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdfrac_63d_base_v072_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdfrac_126d_base_v073_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdfrac_252d_base_v074_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days volume-price divergence z > 1
def f20vpd_f20_semi_volume_price_divergence_vpdfrac_504d_base_v075_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    z = _z(s, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)

