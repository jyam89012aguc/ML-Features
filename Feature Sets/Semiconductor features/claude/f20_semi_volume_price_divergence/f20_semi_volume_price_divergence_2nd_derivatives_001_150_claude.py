import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f20_ret(closeadj):
    return closeadj.pct_change()


def _f20_log_vol(volume):
    return np.log(volume.replace(0, np.nan).abs())


def _f20_divergence(closeadj, volume):
    r = _f20_ret(closeadj)
    v = _f20_log_vol(volume).diff()
    return v * (-np.sign(r))


# 5d slope of 21d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_21d_slope_v001_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_21d_slope_v002_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_21d_slope_v003_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_21d_slope_v004_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_21d_slope_v005_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_63d_slope_v006_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_63d_slope_v007_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_63d_slope_v008_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_63d_slope_v009_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_63d_slope_v010_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_126d_slope_v011_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_126d_slope_v012_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_126d_slope_v013_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_126d_slope_v014_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_126d_slope_v015_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_252d_slope_v016_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_252d_slope_v017_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_252d_slope_v018_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_252d_slope_v019_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_252d_slope_v020_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_504d_slope_v021_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_504d_slope_v022_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_504d_slope_v023_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_504d_slope_v024_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d level of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdlevel_504d_slope_v025_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_21d_slope_v026_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_21d_slope_v027_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_21d_slope_v028_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_21d_slope_v029_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_21d_slope_v030_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_63d_slope_v031_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_63d_slope_v032_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_63d_slope_v033_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_63d_slope_v034_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_63d_slope_v035_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_126d_slope_v036_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_126d_slope_v037_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_126d_slope_v038_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_126d_slope_v039_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_126d_slope_v040_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_252d_slope_v041_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_252d_slope_v042_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_252d_slope_v043_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_252d_slope_v044_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_252d_slope_v045_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_504d_slope_v046_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_504d_slope_v047_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_504d_slope_v048_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_504d_slope_v049_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d z of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdz_504d_slope_v050_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_21d_slope_v051_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_21d_slope_v052_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_21d_slope_v053_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_21d_slope_v054_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_21d_slope_v055_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_63d_slope_v056_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_63d_slope_v057_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_63d_slope_v058_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_63d_slope_v059_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_63d_slope_v060_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_126d_slope_v061_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_126d_slope_v062_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_126d_slope_v063_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_126d_slope_v064_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_126d_slope_v065_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_252d_slope_v066_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_252d_slope_v067_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_252d_slope_v068_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_252d_slope_v069_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_252d_slope_v070_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_504d_slope_v071_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_504d_slope_v072_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_504d_slope_v073_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_504d_slope_v074_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robustz of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrobustz_504d_slope_v075_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_21d_slope_v076_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_21d_slope_v077_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_21d_slope_v078_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_21d_slope_v079_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_21d_slope_v080_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_63d_slope_v081_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_63d_slope_v082_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_63d_slope_v083_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_63d_slope_v084_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_63d_slope_v085_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_126d_slope_v086_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_126d_slope_v087_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_126d_slope_v088_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_126d_slope_v089_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_126d_slope_v090_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_252d_slope_v091_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_252d_slope_v092_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_252d_slope_v093_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_252d_slope_v094_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_252d_slope_v095_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_504d_slope_v096_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_504d_slope_v097_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_504d_slope_v098_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_504d_slope_v099_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d std of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdstd_504d_slope_v100_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_21d_slope_v101_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_21d_slope_v102_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_21d_slope_v103_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_21d_slope_v104_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_21d_slope_v105_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_63d_slope_v106_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_63d_slope_v107_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_63d_slope_v108_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_63d_slope_v109_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_63d_slope_v110_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_126d_slope_v111_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_126d_slope_v112_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_126d_slope_v113_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_126d_slope_v114_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_126d_slope_v115_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_252d_slope_v116_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_252d_slope_v117_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_252d_slope_v118_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_252d_slope_v119_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_252d_slope_v120_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_504d_slope_v121_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_504d_slope_v122_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_504d_slope_v123_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_504d_slope_v124_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d max of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdmax_504d_slope_v125_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_21d_slope_v126_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_21d_slope_v127_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_21d_slope_v128_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_21d_slope_v129_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_21d_slope_v130_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_63d_slope_v131_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_63d_slope_v132_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_63d_slope_v133_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_63d_slope_v134_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_63d_slope_v135_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_126d_slope_v136_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_126d_slope_v137_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_126d_slope_v138_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_126d_slope_v139_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_126d_slope_v140_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_252d_slope_v141_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_252d_slope_v142_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_252d_slope_v143_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_252d_slope_v144_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_252d_slope_v145_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_504d_slope_v146_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_504d_slope_v147_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_504d_slope_v148_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_504d_slope_v149_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d range of volume-price divergence
def f20vpd_f20_semi_volume_price_divergence_vpdrange_504d_slope_v150_signal(closeadj, volume):
    s = _f20_divergence(closeadj, volume)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

