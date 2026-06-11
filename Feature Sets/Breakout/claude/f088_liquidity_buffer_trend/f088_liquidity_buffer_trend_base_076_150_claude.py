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
def _f088_current_ratio_slope(currentratio, w):
    return currentratio.diff(periods=w) / currentratio.abs().shift(w).replace(0, np.nan)


def _f088_liquidity_trend(currentratio, w):
    m = currentratio.rolling(w, min_periods=max(1, w // 2)).mean()
    return currentratio - m


def _f088_liquidity_quality(currentratio, w):
    sl = currentratio.diff(periods=w)
    sd = currentratio.rolling(w, min_periods=max(1, w // 2)).std()
    return sl / sd.replace(0, np.nan)

def f088lbt_f088_liquidity_buffer_trend_crstanh_5d_base_v001_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_5d_base_v002_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_5d_base_v003_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_10d_base_v004_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_10d_base_v005_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_10d_base_v006_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_21d_base_v007_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_21d_base_v008_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_21d_base_v009_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_42d_base_v010_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_42d_base_v011_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_42d_base_v012_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_63d_base_v013_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_63d_base_v014_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_63d_base_v015_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_126d_base_v016_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_126d_base_v017_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_126d_base_v018_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_189d_base_v019_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_189d_base_v020_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_189d_base_v021_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_252d_base_v022_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_252d_base_v023_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_252d_base_v024_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_378d_base_v025_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_378d_base_v026_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_378d_base_v027_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crstanh_504d_base_v028_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqttanh_504d_base_v029_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqtanh_504d_base_v030_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_5d_base_v031_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_5d_base_v032_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_5d_base_v033_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_10d_base_v034_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_10d_base_v035_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_10d_base_v036_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_21d_base_v037_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_21d_base_v038_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_21d_base_v039_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_42d_base_v040_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_42d_base_v041_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_42d_base_v042_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_63d_base_v043_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_63d_base_v044_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_63d_base_v045_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_126d_base_v046_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_126d_base_v047_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_126d_base_v048_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_189d_base_v049_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_189d_base_v050_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_189d_base_v051_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_252d_base_v052_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_252d_base_v053_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_252d_base_v054_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_378d_base_v055_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_378d_base_v056_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_378d_base_v057_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsclip_504d_base_v058_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtclip_504d_base_v059_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqclip_504d_base_v060_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsvar_5d_base_v061_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtvar_5d_base_v062_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqvar_5d_base_v063_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsvar_10d_base_v064_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtvar_10d_base_v065_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqvar_10d_base_v066_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsvar_21d_base_v067_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtvar_21d_base_v068_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqvar_21d_base_v069_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsvar_42d_base_v070_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtvar_42d_base_v071_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqvar_42d_base_v072_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsvar_63d_base_v073_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtvar_63d_base_v074_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqvar_63d_base_v075_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f088lbt_f088_liquidity_buffer_trend_crstanh_5d_base_v001_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_5d_base_v002_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_5d_base_v003_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_10d_base_v004_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_10d_base_v005_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_10d_base_v006_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_21d_base_v007_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_21d_base_v008_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_21d_base_v009_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_42d_base_v010_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_42d_base_v011_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_42d_base_v012_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_63d_base_v013_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_63d_base_v014_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_63d_base_v015_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_126d_base_v016_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_126d_base_v017_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_126d_base_v018_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_189d_base_v019_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_189d_base_v020_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_189d_base_v021_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_252d_base_v022_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_252d_base_v023_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_252d_base_v024_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_378d_base_v025_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_378d_base_v026_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_378d_base_v027_signal,
    f088lbt_f088_liquidity_buffer_trend_crstanh_504d_base_v028_signal,
    f088lbt_f088_liquidity_buffer_trend_lqttanh_504d_base_v029_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqtanh_504d_base_v030_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_5d_base_v031_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_5d_base_v032_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_5d_base_v033_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_10d_base_v034_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_10d_base_v035_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_10d_base_v036_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_21d_base_v037_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_21d_base_v038_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_21d_base_v039_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_42d_base_v040_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_42d_base_v041_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_42d_base_v042_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_63d_base_v043_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_63d_base_v044_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_63d_base_v045_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_126d_base_v046_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_126d_base_v047_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_126d_base_v048_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_189d_base_v049_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_189d_base_v050_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_189d_base_v051_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_252d_base_v052_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_252d_base_v053_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_252d_base_v054_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_378d_base_v055_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_378d_base_v056_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_378d_base_v057_signal,
    f088lbt_f088_liquidity_buffer_trend_crsclip_504d_base_v058_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtclip_504d_base_v059_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqclip_504d_base_v060_signal,
    f088lbt_f088_liquidity_buffer_trend_crsvar_5d_base_v061_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtvar_5d_base_v062_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqvar_5d_base_v063_signal,
    f088lbt_f088_liquidity_buffer_trend_crsvar_10d_base_v064_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtvar_10d_base_v065_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqvar_10d_base_v066_signal,
    f088lbt_f088_liquidity_buffer_trend_crsvar_21d_base_v067_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtvar_21d_base_v068_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqvar_21d_base_v069_signal,
    f088lbt_f088_liquidity_buffer_trend_crsvar_42d_base_v070_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtvar_42d_base_v071_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqvar_42d_base_v072_signal,
    f088lbt_f088_liquidity_buffer_trend_crsvar_63d_base_v073_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtvar_63d_base_v074_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqvar_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F088_LIQUIDITY_BUFFER_TREND_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    currentratio = pd.Series(1.5 + 0.3 * np.sin(np.arange(n) / 250.0) + 0.05 * np.random.randn(n), name="currentratio")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"currentratio": currentratio, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f088_current_ratio_slope", "_f088_liquidity_trend", "_f088_liquidity_quality",)
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
    print(f"OK f088_liquidity_buffer_trend_base_076_150_claude: {n_features} features pass")
