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
def _f19_turnover(volume, sharesbas):
    return volume / sharesbas.replace(0, np.nan)


def _f19_log_turnover(volume, sharesbas):
    t = _f19_turnover(volume, sharesbas)
    return np.log(t.replace(0, np.nan).abs() + 1e-30)


# 5d slope of 21d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_21d_slope_v001_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_21d_slope_v002_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_21d_slope_v003_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_21d_slope_v004_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_21d_slope_v005_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_63d_slope_v006_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_63d_slope_v007_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_63d_slope_v008_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_63d_slope_v009_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_63d_slope_v010_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_126d_slope_v011_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_126d_slope_v012_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_126d_slope_v013_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_126d_slope_v014_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_126d_slope_v015_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_252d_slope_v016_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_252d_slope_v017_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_252d_slope_v018_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_252d_slope_v019_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_252d_slope_v020_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_504d_slope_v021_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_504d_slope_v022_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_504d_slope_v023_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_504d_slope_v024_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d level of log turnover
def f19tr_f19_semi_turnover_regime_tolevel_504d_slope_v025_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = s - _mean(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_21d_slope_v026_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_21d_slope_v027_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_21d_slope_v028_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_21d_slope_v029_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_21d_slope_v030_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_63d_slope_v031_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_63d_slope_v032_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_63d_slope_v033_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_63d_slope_v034_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_63d_slope_v035_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_126d_slope_v036_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_126d_slope_v037_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_126d_slope_v038_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_126d_slope_v039_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_126d_slope_v040_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_252d_slope_v041_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_252d_slope_v042_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_252d_slope_v043_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_252d_slope_v044_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_252d_slope_v045_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_504d_slope_v046_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_504d_slope_v047_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_504d_slope_v048_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_504d_slope_v049_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d z of log turnover
def f19tr_f19_semi_turnover_regime_toz_504d_slope_v050_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _z(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_21d_slope_v051_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_21d_slope_v052_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_21d_slope_v053_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_21d_slope_v054_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_21d_slope_v055_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_63d_slope_v056_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_63d_slope_v057_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_63d_slope_v058_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_63d_slope_v059_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_63d_slope_v060_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_126d_slope_v061_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_126d_slope_v062_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_126d_slope_v063_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_126d_slope_v064_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_126d_slope_v065_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_252d_slope_v066_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_252d_slope_v067_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_252d_slope_v068_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_252d_slope_v069_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_252d_slope_v070_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_504d_slope_v071_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_504d_slope_v072_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_504d_slope_v073_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_504d_slope_v074_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d robustz of log turnover
def f19tr_f19_semi_turnover_regime_torobustz_504d_slope_v075_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    base = (s - med) / (1.4826 * mad).replace(0, np.nan)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_21d_slope_v076_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_21d_slope_v077_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_21d_slope_v078_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_21d_slope_v079_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_21d_slope_v080_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_63d_slope_v081_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_63d_slope_v082_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_63d_slope_v083_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_63d_slope_v084_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_63d_slope_v085_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_126d_slope_v086_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_126d_slope_v087_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_126d_slope_v088_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_126d_slope_v089_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_126d_slope_v090_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_252d_slope_v091_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_252d_slope_v092_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_252d_slope_v093_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_252d_slope_v094_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_252d_slope_v095_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_504d_slope_v096_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_504d_slope_v097_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_504d_slope_v098_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_504d_slope_v099_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d std of log turnover
def f19tr_f19_semi_turnover_regime_tostd_504d_slope_v100_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    d = s.diff()
    base = _std(d, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_21d_slope_v101_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_21d_slope_v102_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_21d_slope_v103_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_21d_slope_v104_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_21d_slope_v105_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_63d_slope_v106_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_63d_slope_v107_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_63d_slope_v108_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_63d_slope_v109_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_63d_slope_v110_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_126d_slope_v111_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_126d_slope_v112_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_126d_slope_v113_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_126d_slope_v114_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_126d_slope_v115_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_252d_slope_v116_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_252d_slope_v117_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_252d_slope_v118_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_252d_slope_v119_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_252d_slope_v120_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_504d_slope_v121_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_504d_slope_v122_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_504d_slope_v123_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_504d_slope_v124_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_504d_slope_v125_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_21d_slope_v126_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_21d_slope_v127_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_21d_slope_v128_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_21d_slope_v129_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 21d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_21d_slope_v130_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 21) - _min(s, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_63d_slope_v131_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_63d_slope_v132_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_63d_slope_v133_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_63d_slope_v134_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 63d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_63d_slope_v135_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 63) - _min(s, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_126d_slope_v136_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_126d_slope_v137_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_126d_slope_v138_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_126d_slope_v139_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 126d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_126d_slope_v140_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 126) - _min(s, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_252d_slope_v141_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_252d_slope_v142_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_252d_slope_v143_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_252d_slope_v144_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 252d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_252d_slope_v145_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 252) - _min(s, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_504d_slope_v146_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_504d_slope_v147_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_504d_slope_v148_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_504d_slope_v149_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d slope of 504d range of log turnover
def f19tr_f19_semi_turnover_regime_torange_504d_slope_v150_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    base = _max(s, 504) - _min(s, 504)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

