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
def _f19_turnover(volume, sharesbas):
    return volume / sharesbas.replace(0, np.nan)


def _f19_log_turnover(volume, sharesbas):
    t = _f19_turnover(volume, sharesbas)
    return np.log(t.replace(0, np.nan).abs() + 1e-30)


# 21d level of log turnover vs 21d mean
def f19tr_f19_semi_turnover_regime_tolevel_21d_base_v001_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _mean(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d level of log turnover vs 63d mean
def f19tr_f19_semi_turnover_regime_tolevel_63d_base_v002_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _mean(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d level of log turnover vs 126d mean
def f19tr_f19_semi_turnover_regime_tolevel_126d_base_v003_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d level of log turnover vs 252d mean
def f19tr_f19_semi_turnover_regime_tolevel_252d_base_v004_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d level of log turnover vs 504d mean
def f19tr_f19_semi_turnover_regime_tolevel_504d_base_v005_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of log turnover
def f19tr_f19_semi_turnover_regime_toz_21d_base_v006_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log turnover
def f19tr_f19_semi_turnover_regime_toz_63d_base_v007_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log turnover
def f19tr_f19_semi_turnover_regime_toz_126d_base_v008_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log turnover
def f19tr_f19_semi_turnover_regime_toz_252d_base_v009_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log turnover
def f19tr_f19_semi_turnover_regime_toz_504d_base_v010_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z of log turnover (median/MAD)
def f19tr_f19_semi_turnover_regime_torobustz_21d_base_v011_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(21, min_periods=10).median()
    mad = (s - med).abs().rolling(21, min_periods=10).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z of log turnover (median/MAD)
def f19tr_f19_semi_turnover_regime_torobustz_63d_base_v012_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(63, min_periods=31).median()
    mad = (s - med).abs().rolling(63, min_periods=31).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z of log turnover (median/MAD)
def f19tr_f19_semi_turnover_regime_torobustz_126d_base_v013_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(126, min_periods=63).median()
    mad = (s - med).abs().rolling(126, min_periods=63).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z of log turnover (median/MAD)
def f19tr_f19_semi_turnover_regime_torobustz_252d_base_v014_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(252, min_periods=126).median()
    mad = (s - med).abs().rolling(252, min_periods=126).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z of log turnover (median/MAD)
def f19tr_f19_semi_turnover_regime_torobustz_504d_base_v015_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    med = s.rolling(504, min_periods=252).median()
    mad = (s - med).abs().rolling(504, min_periods=252).median()
    result = (s - med) / (1.4826 * mad).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_21d_base_v016_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_63d_base_v017_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_126d_base_v018_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_252d_base_v019_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max of log turnover
def f19tr_f19_semi_turnover_regime_tomax_504d_base_v020_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d min of log turnover
def f19tr_f19_semi_turnover_regime_tomin_21d_base_v021_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d min of log turnover
def f19tr_f19_semi_turnover_regime_tomin_63d_base_v022_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d min of log turnover
def f19tr_f19_semi_turnover_regime_tomin_126d_base_v023_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min of log turnover
def f19tr_f19_semi_turnover_regime_tomin_252d_base_v024_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d min of log turnover
def f19tr_f19_semi_turnover_regime_tomin_504d_base_v025_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d range of log turnover
def f19tr_f19_semi_turnover_regime_torng_21d_base_v026_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 21) - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d range of log turnover
def f19tr_f19_semi_turnover_regime_torng_63d_base_v027_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 63) - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d range of log turnover
def f19tr_f19_semi_turnover_regime_torng_126d_base_v028_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 126) - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of log turnover
def f19tr_f19_semi_turnover_regime_torng_252d_base_v029_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 252) - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of log turnover
def f19tr_f19_semi_turnover_regime_torng_504d_base_v030_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = _max(s, 504) - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d position-in-range of log turnover
def f19tr_f19_semi_turnover_regime_topos_21d_base_v031_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    lo = _min(s, 21)
    hi = _max(s, 21)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d position-in-range of log turnover
def f19tr_f19_semi_turnover_regime_topos_63d_base_v032_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    lo = _min(s, 63)
    hi = _max(s, 63)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d position-in-range of log turnover
def f19tr_f19_semi_turnover_regime_topos_126d_base_v033_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    lo = _min(s, 126)
    hi = _max(s, 126)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d position-in-range of log turnover
def f19tr_f19_semi_turnover_regime_topos_252d_base_v034_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    lo = _min(s, 252)
    hi = _max(s, 252)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d position-in-range of log turnover
def f19tr_f19_semi_turnover_regime_topos_504d_base_v035_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    lo = _min(s, 504)
    hi = _max(s, 504)
    result = (s - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of log turnover from peak
def f19tr_f19_semi_turnover_regime_todd_21d_base_v036_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _max(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of log turnover from peak
def f19tr_f19_semi_turnover_regime_todd_63d_base_v037_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _max(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of log turnover from peak
def f19tr_f19_semi_turnover_regime_todd_126d_base_v038_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _max(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of log turnover from peak
def f19tr_f19_semi_turnover_regime_todd_252d_base_v039_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _max(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of log turnover from peak
def f19tr_f19_semi_turnover_regime_todd_504d_base_v040_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _max(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of log turnover above trough
def f19tr_f19_semi_turnover_regime_toup_21d_base_v041_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _min(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of log turnover above trough
def f19tr_f19_semi_turnover_regime_toup_63d_base_v042_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _min(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of log turnover above trough
def f19tr_f19_semi_turnover_regime_toup_126d_base_v043_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _min(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of log turnover above trough
def f19tr_f19_semi_turnover_regime_toup_252d_base_v044_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _min(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of log turnover above trough
def f19tr_f19_semi_turnover_regime_toup_504d_base_v045_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    result = s - _min(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of log turnover changes
def f19tr_f19_semi_turnover_regime_tostd_21d_base_v046_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = _std(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of log turnover changes
def f19tr_f19_semi_turnover_regime_tostd_63d_base_v047_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = _std(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of log turnover changes
def f19tr_f19_semi_turnover_regime_tostd_126d_base_v048_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = _std(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of log turnover changes
def f19tr_f19_semi_turnover_regime_tostd_252d_base_v049_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = _std(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of log turnover changes
def f19tr_f19_semi_turnover_regime_tostd_504d_base_v050_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = _std(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of log turnover changes
def f19tr_f19_semi_turnover_regime_toskew_21d_base_v051_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(21, min_periods=10).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of log turnover changes
def f19tr_f19_semi_turnover_regime_toskew_63d_base_v052_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(63, min_periods=31).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of log turnover changes
def f19tr_f19_semi_turnover_regime_toskew_126d_base_v053_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of log turnover changes
def f19tr_f19_semi_turnover_regime_toskew_252d_base_v054_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of log turnover changes
def f19tr_f19_semi_turnover_regime_toskew_504d_base_v055_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of log turnover changes
def f19tr_f19_semi_turnover_regime_tokurt_21d_base_v056_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(21, min_periods=10).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of log turnover changes
def f19tr_f19_semi_turnover_regime_tokurt_63d_base_v057_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(63, min_periods=31).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of log turnover changes
def f19tr_f19_semi_turnover_regime_tokurt_126d_base_v058_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of log turnover changes
def f19tr_f19_semi_turnover_regime_tokurt_252d_base_v059_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of log turnover changes
def f19tr_f19_semi_turnover_regime_tokurt_504d_base_v060_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas).diff()
    result = s.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tosigncum_21d_base_v061_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tosigncum_63d_base_v062_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tosigncum_126d_base_v063_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tosigncum_252d_base_v064_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cumulative change in log turnover
def f19tr_f19_semi_turnover_regime_tosigncum_504d_base_v065_signal(volume, sharesbas):
    d = _f19_log_turnover(volume, sharesbas).diff()
    result = pd.Series(np.sign(d), index=d.index).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tohits_21d_base_v066_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=10).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tohits_63d_base_v067_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=31).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tohits_126d_base_v068_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tohits_252d_base_v069_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tohits_504d_base_v070_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tofrac_21d_base_v071_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 21)
    result = (z > 1).astype(float).rolling(21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tofrac_63d_base_v072_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 63)
    result = (z > 1).astype(float).rolling(63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tofrac_126d_base_v073_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 126)
    result = (z > 1).astype(float).rolling(126, min_periods=63).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tofrac_252d_base_v074_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 252)
    result = (z > 1).astype(float).rolling(252, min_periods=126).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days log turnover z > 1
def f19tr_f19_semi_turnover_regime_tofrac_504d_base_v075_signal(volume, sharesbas):
    s = _f19_log_turnover(volume, sharesbas)
    z = _z(s, 504)
    result = (z > 1).astype(float).rolling(504, min_periods=252).mean()
    return result.replace([np.inf, -np.inf], np.nan)

