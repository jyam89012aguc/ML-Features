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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f058_rolling_variance(close, w):
    ret = np.log(close.replace(0, np.nan).abs()).diff()
    return ret.rolling(w, min_periods=max(1, w // 2)).var()


def _f058_hurst_proxy(close, w):
    ret = np.log(close.replace(0, np.nan).abs()).diff()
    var_w = ret.rolling(w, min_periods=max(1, w // 2)).var()
    var_1 = ret.rolling(max(2, w // 4), min_periods=2).var()
    return 0.5 * np.log(var_w / var_1.replace(0, np.nan)).abs() / float(np.log(max(2, w)))


def _f058_persistence_score(close, w):
    ret = np.log(close.replace(0, np.nan).abs()).diff()
    m = ret.rolling(w, min_periods=max(1, w // 2)).mean()
    centered = ret - m
    num = (centered * centered.shift(1)).rolling(w, min_periods=max(1, w // 2)).mean()
    den = (centered * centered).rolling(w, min_periods=max(1, w // 2)).mean()
    return num / den.replace(0, np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_5d_base_v001_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 5), _mean(_f058_rolling_variance(closeadj, 5), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_10d_base_v002_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 10), _mean(_f058_rolling_variance(closeadj, 10), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_21d_base_v003_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 21), _mean(_f058_rolling_variance(closeadj, 21), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_42d_base_v004_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 42), _mean(_f058_rolling_variance(closeadj, 42), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_63d_base_v005_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 63), _mean(_f058_rolling_variance(closeadj, 63), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_126d_base_v006_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 126), _mean(_f058_rolling_variance(closeadj, 126), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_189d_base_v007_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 189), _mean(_f058_rolling_variance(closeadj, 189), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_252d_base_v008_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 252), _mean(_f058_rolling_variance(closeadj, 252), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_378d_base_v009_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 378), _mean(_f058_rolling_variance(closeadj, 378), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarxclose_504d_base_v010_signal(closeadj):
    result = _safe_div(_f058_rolling_variance(closeadj, 504), _mean(_f058_rolling_variance(closeadj, 504), 252).abs()) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_5d_base_v011_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_10d_base_v012_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 10) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_21d_base_v013_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 21) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_42d_base_v014_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 42) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_63d_base_v015_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 63) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_126d_base_v016_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 126) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_189d_base_v017_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 189) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_252d_base_v018_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_378d_base_v019_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 378) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstxclose_504d_base_v020_signal(closeadj):
    result = _f058_hurst_proxy(closeadj, 504) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_5d_base_v021_signal(closeadj):
    result = _f058_persistence_score(closeadj, 5) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_10d_base_v022_signal(closeadj):
    result = _f058_persistence_score(closeadj, 10) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_21d_base_v023_signal(closeadj):
    result = _f058_persistence_score(closeadj, 21) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_42d_base_v024_signal(closeadj):
    result = _f058_persistence_score(closeadj, 42) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_63d_base_v025_signal(closeadj):
    result = _f058_persistence_score(closeadj, 63) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_126d_base_v026_signal(closeadj):
    result = _f058_persistence_score(closeadj, 126) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_189d_base_v027_signal(closeadj):
    result = _f058_persistence_score(closeadj, 189) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_252d_base_v028_signal(closeadj):
    result = _f058_persistence_score(closeadj, 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_378d_base_v029_signal(closeadj):
    result = _f058_persistence_score(closeadj, 378) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_persxclose_504d_base_v030_signal(closeadj):
    result = _f058_persistence_score(closeadj, 504) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_5d_base_v031_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_10d_base_v032_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_21d_base_v033_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_42d_base_v034_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_63d_base_v035_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_126d_base_v036_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_189d_base_v037_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_252d_base_v038_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_378d_base_v039_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvarzc252_504d_base_v040_signal(closeadj):
    result = _z(_f058_rolling_variance(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_5d_base_v041_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_10d_base_v042_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_21d_base_v043_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_42d_base_v044_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_63d_base_v045_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_126d_base_v046_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_189d_base_v047_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_252d_base_v048_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_378d_base_v049_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrstzc252_504d_base_v050_signal(closeadj):
    result = _z(_f058_hurst_proxy(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_5d_base_v051_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 5), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_10d_base_v052_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 10), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_21d_base_v053_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 21), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_42d_base_v054_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 42), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_63d_base_v055_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 63), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_126d_base_v056_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 126), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_189d_base_v057_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 189), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_252d_base_v058_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 252), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_378d_base_v059_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 378), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_perszc252_504d_base_v060_signal(closeadj):
    result = _z(_f058_persistence_score(closeadj, 504), 252) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_5d_base_v061_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 5), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_10d_base_v062_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 10), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_21d_base_v063_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 21), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_42d_base_v064_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 42), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_63d_base_v065_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 63), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_126d_base_v066_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 126), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_189d_base_v067_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 189), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_252d_base_v068_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 252), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_378d_base_v069_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 378), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_rvartanh_504d_base_v070_signal(closeadj):
    result = np.tanh(_z(_f058_rolling_variance(closeadj, 504), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrsttanh_5d_base_v071_signal(closeadj):
    result = np.tanh(_z(_f058_hurst_proxy(closeadj, 5), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrsttanh_10d_base_v072_signal(closeadj):
    result = np.tanh(_z(_f058_hurst_proxy(closeadj, 10), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrsttanh_21d_base_v073_signal(closeadj):
    result = np.tanh(_z(_f058_hurst_proxy(closeadj, 21), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrsttanh_42d_base_v074_signal(closeadj):
    result = np.tanh(_z(_f058_hurst_proxy(closeadj, 42), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


def f058hex_f058_hurst_exponent_hrsttanh_63d_base_v075_signal(closeadj):
    result = np.tanh(_z(_f058_hurst_proxy(closeadj, 63), 252)) * _safe_div(closeadj, _mean(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f058hex_f058_hurst_exponent_rvarxclose_5d_base_v001_signal,
    f058hex_f058_hurst_exponent_rvarxclose_10d_base_v002_signal,
    f058hex_f058_hurst_exponent_rvarxclose_21d_base_v003_signal,
    f058hex_f058_hurst_exponent_rvarxclose_42d_base_v004_signal,
    f058hex_f058_hurst_exponent_rvarxclose_63d_base_v005_signal,
    f058hex_f058_hurst_exponent_rvarxclose_126d_base_v006_signal,
    f058hex_f058_hurst_exponent_rvarxclose_189d_base_v007_signal,
    f058hex_f058_hurst_exponent_rvarxclose_252d_base_v008_signal,
    f058hex_f058_hurst_exponent_rvarxclose_378d_base_v009_signal,
    f058hex_f058_hurst_exponent_rvarxclose_504d_base_v010_signal,
    f058hex_f058_hurst_exponent_hrstxclose_5d_base_v011_signal,
    f058hex_f058_hurst_exponent_hrstxclose_10d_base_v012_signal,
    f058hex_f058_hurst_exponent_hrstxclose_21d_base_v013_signal,
    f058hex_f058_hurst_exponent_hrstxclose_42d_base_v014_signal,
    f058hex_f058_hurst_exponent_hrstxclose_63d_base_v015_signal,
    f058hex_f058_hurst_exponent_hrstxclose_126d_base_v016_signal,
    f058hex_f058_hurst_exponent_hrstxclose_189d_base_v017_signal,
    f058hex_f058_hurst_exponent_hrstxclose_252d_base_v018_signal,
    f058hex_f058_hurst_exponent_hrstxclose_378d_base_v019_signal,
    f058hex_f058_hurst_exponent_hrstxclose_504d_base_v020_signal,
    f058hex_f058_hurst_exponent_persxclose_5d_base_v021_signal,
    f058hex_f058_hurst_exponent_persxclose_10d_base_v022_signal,
    f058hex_f058_hurst_exponent_persxclose_21d_base_v023_signal,
    f058hex_f058_hurst_exponent_persxclose_42d_base_v024_signal,
    f058hex_f058_hurst_exponent_persxclose_63d_base_v025_signal,
    f058hex_f058_hurst_exponent_persxclose_126d_base_v026_signal,
    f058hex_f058_hurst_exponent_persxclose_189d_base_v027_signal,
    f058hex_f058_hurst_exponent_persxclose_252d_base_v028_signal,
    f058hex_f058_hurst_exponent_persxclose_378d_base_v029_signal,
    f058hex_f058_hurst_exponent_persxclose_504d_base_v030_signal,
    f058hex_f058_hurst_exponent_rvarzc252_5d_base_v031_signal,
    f058hex_f058_hurst_exponent_rvarzc252_10d_base_v032_signal,
    f058hex_f058_hurst_exponent_rvarzc252_21d_base_v033_signal,
    f058hex_f058_hurst_exponent_rvarzc252_42d_base_v034_signal,
    f058hex_f058_hurst_exponent_rvarzc252_63d_base_v035_signal,
    f058hex_f058_hurst_exponent_rvarzc252_126d_base_v036_signal,
    f058hex_f058_hurst_exponent_rvarzc252_189d_base_v037_signal,
    f058hex_f058_hurst_exponent_rvarzc252_252d_base_v038_signal,
    f058hex_f058_hurst_exponent_rvarzc252_378d_base_v039_signal,
    f058hex_f058_hurst_exponent_rvarzc252_504d_base_v040_signal,
    f058hex_f058_hurst_exponent_hrstzc252_5d_base_v041_signal,
    f058hex_f058_hurst_exponent_hrstzc252_10d_base_v042_signal,
    f058hex_f058_hurst_exponent_hrstzc252_21d_base_v043_signal,
    f058hex_f058_hurst_exponent_hrstzc252_42d_base_v044_signal,
    f058hex_f058_hurst_exponent_hrstzc252_63d_base_v045_signal,
    f058hex_f058_hurst_exponent_hrstzc252_126d_base_v046_signal,
    f058hex_f058_hurst_exponent_hrstzc252_189d_base_v047_signal,
    f058hex_f058_hurst_exponent_hrstzc252_252d_base_v048_signal,
    f058hex_f058_hurst_exponent_hrstzc252_378d_base_v049_signal,
    f058hex_f058_hurst_exponent_hrstzc252_504d_base_v050_signal,
    f058hex_f058_hurst_exponent_perszc252_5d_base_v051_signal,
    f058hex_f058_hurst_exponent_perszc252_10d_base_v052_signal,
    f058hex_f058_hurst_exponent_perszc252_21d_base_v053_signal,
    f058hex_f058_hurst_exponent_perszc252_42d_base_v054_signal,
    f058hex_f058_hurst_exponent_perszc252_63d_base_v055_signal,
    f058hex_f058_hurst_exponent_perszc252_126d_base_v056_signal,
    f058hex_f058_hurst_exponent_perszc252_189d_base_v057_signal,
    f058hex_f058_hurst_exponent_perszc252_252d_base_v058_signal,
    f058hex_f058_hurst_exponent_perszc252_378d_base_v059_signal,
    f058hex_f058_hurst_exponent_perszc252_504d_base_v060_signal,
    f058hex_f058_hurst_exponent_rvartanh_5d_base_v061_signal,
    f058hex_f058_hurst_exponent_rvartanh_10d_base_v062_signal,
    f058hex_f058_hurst_exponent_rvartanh_21d_base_v063_signal,
    f058hex_f058_hurst_exponent_rvartanh_42d_base_v064_signal,
    f058hex_f058_hurst_exponent_rvartanh_63d_base_v065_signal,
    f058hex_f058_hurst_exponent_rvartanh_126d_base_v066_signal,
    f058hex_f058_hurst_exponent_rvartanh_189d_base_v067_signal,
    f058hex_f058_hurst_exponent_rvartanh_252d_base_v068_signal,
    f058hex_f058_hurst_exponent_rvartanh_378d_base_v069_signal,
    f058hex_f058_hurst_exponent_rvartanh_504d_base_v070_signal,
    f058hex_f058_hurst_exponent_hrsttanh_5d_base_v071_signal,
    f058hex_f058_hurst_exponent_hrsttanh_10d_base_v072_signal,
    f058hex_f058_hurst_exponent_hrsttanh_21d_base_v073_signal,
    f058hex_f058_hurst_exponent_hrsttanh_42d_base_v074_signal,
    f058hex_f058_hurst_exponent_hrsttanh_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F058_HURST_EXPONENT_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f058_rolling_variance", "_f058_hurst_proxy", "_f058_persistence_score",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f058_hurst_exponent_base_001_075_claude: {n_features} features pass")
