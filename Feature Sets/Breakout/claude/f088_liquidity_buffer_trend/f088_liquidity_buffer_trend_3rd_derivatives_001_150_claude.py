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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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

def f088lbt_f088_liquidity_buffer_trend_crs_5d_jerk_v001_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_5d_jerk_v002_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_5d_jerk_v003_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_10d_jerk_v004_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_10d_jerk_v005_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_10d_jerk_v006_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_21d_jerk_v007_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_21d_jerk_v008_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_21d_jerk_v009_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_42d_jerk_v010_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_42d_jerk_v011_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_42d_jerk_v012_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_63d_jerk_v013_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_63d_jerk_v014_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_63d_jerk_v015_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_126d_jerk_v016_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_126d_jerk_v017_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_126d_jerk_v018_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_189d_jerk_v019_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_189d_jerk_v020_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_189d_jerk_v021_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_252d_jerk_v022_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_252d_jerk_v023_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_252d_jerk_v024_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_378d_jerk_v025_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_378d_jerk_v026_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_378d_jerk_v027_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_504d_jerk_v028_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_504d_jerk_v029_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_504d_jerk_v030_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_5d_jerk_v031_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_5d_jerk_v032_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_5d_jerk_v033_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_10d_jerk_v034_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_10d_jerk_v035_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_10d_jerk_v036_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_21d_jerk_v037_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_21d_jerk_v038_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_21d_jerk_v039_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_42d_jerk_v040_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_42d_jerk_v041_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_42d_jerk_v042_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_63d_jerk_v043_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_63d_jerk_v044_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_63d_jerk_v045_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_126d_jerk_v046_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_126d_jerk_v047_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_126d_jerk_v048_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_189d_jerk_v049_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_189d_jerk_v050_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_189d_jerk_v051_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_252d_jerk_v052_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_252d_jerk_v053_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_252d_jerk_v054_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_378d_jerk_v055_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_378d_jerk_v056_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_378d_jerk_v057_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_504d_jerk_v058_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_504d_jerk_v059_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_504d_jerk_v060_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_5d_jerk_v061_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_5d_jerk_v062_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_5d_jerk_v063_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_10d_jerk_v064_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_10d_jerk_v065_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_10d_jerk_v066_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_21d_jerk_v067_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_21d_jerk_v068_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_21d_jerk_v069_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_42d_jerk_v070_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_42d_jerk_v071_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_42d_jerk_v072_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_63d_jerk_v073_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_63d_jerk_v074_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_63d_jerk_v075_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_126d_jerk_v076_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_126d_jerk_v077_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_126d_jerk_v078_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_189d_jerk_v079_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_189d_jerk_v080_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_189d_jerk_v081_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_252d_jerk_v082_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_252d_jerk_v083_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_252d_jerk_v084_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_378d_jerk_v085_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_378d_jerk_v086_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_378d_jerk_v087_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_504d_jerk_v088_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_504d_jerk_v089_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_504d_jerk_v090_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_5d_jerk_v091_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_5d_jerk_v092_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_5d_jerk_v093_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 5)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_10d_jerk_v094_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_10d_jerk_v095_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_10d_jerk_v096_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 10)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_21d_jerk_v097_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_21d_jerk_v098_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_21d_jerk_v099_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 21)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_42d_jerk_v100_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_42d_jerk_v101_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_42d_jerk_v102_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 42)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_63d_jerk_v103_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_63d_jerk_v104_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_63d_jerk_v105_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 63)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_126d_jerk_v106_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_126d_jerk_v107_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_126d_jerk_v108_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 126)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_189d_jerk_v109_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_189d_jerk_v110_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_189d_jerk_v111_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 189)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_252d_jerk_v112_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_252d_jerk_v113_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_252d_jerk_v114_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 252)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_378d_jerk_v115_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_378d_jerk_v116_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_378d_jerk_v117_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 378)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssq_504d_jerk_v118_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsq_504d_jerk_v119_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsq_504d_jerk_v120_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 504)) * closeadj * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_5d_jerk_v121_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_5d_jerk_v122_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_5d_jerk_v123_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 5)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_10d_jerk_v124_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_10d_jerk_v125_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_10d_jerk_v126_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 10)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_21d_jerk_v127_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_21d_jerk_v128_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_21d_jerk_v129_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 21)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_42d_jerk_v130_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_42d_jerk_v131_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_42d_jerk_v132_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 42)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_63d_jerk_v133_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_63d_jerk_v134_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_63d_jerk_v135_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 63)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_126d_jerk_v136_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_126d_jerk_v137_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_126d_jerk_v138_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 126)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_189d_jerk_v139_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_189d_jerk_v140_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_189d_jerk_v141_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 189)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_252d_jerk_v142_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_252d_jerk_v143_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_252d_jerk_v144_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 252)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_378d_jerk_v145_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_378d_jerk_v146_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_378d_jerk_v147_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 378)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsab_504d_jerk_v148_signal(currentratio, closeadj):
    base = (_f088_current_ratio_slope(currentratio, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtab_504d_jerk_v149_signal(currentratio, closeadj):
    base = (_f088_liquidity_trend(currentratio, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqab_504d_jerk_v150_signal(currentratio, closeadj):
    base = (_f088_liquidity_quality(currentratio, 504)).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f088lbt_f088_liquidity_buffer_trend_crs_5d_jerk_v001_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_5d_jerk_v002_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_5d_jerk_v003_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_10d_jerk_v004_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_10d_jerk_v005_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_10d_jerk_v006_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_21d_jerk_v007_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_21d_jerk_v008_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_21d_jerk_v009_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_42d_jerk_v010_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_42d_jerk_v011_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_42d_jerk_v012_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_63d_jerk_v013_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_63d_jerk_v014_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_63d_jerk_v015_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_126d_jerk_v016_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_126d_jerk_v017_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_126d_jerk_v018_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_189d_jerk_v019_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_189d_jerk_v020_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_189d_jerk_v021_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_252d_jerk_v022_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_252d_jerk_v023_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_252d_jerk_v024_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_378d_jerk_v025_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_378d_jerk_v026_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_378d_jerk_v027_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_504d_jerk_v028_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_504d_jerk_v029_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_504d_jerk_v030_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_5d_jerk_v031_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_5d_jerk_v032_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_5d_jerk_v033_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_10d_jerk_v034_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_10d_jerk_v035_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_10d_jerk_v036_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_21d_jerk_v037_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_21d_jerk_v038_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_21d_jerk_v039_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_42d_jerk_v040_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_42d_jerk_v041_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_42d_jerk_v042_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_63d_jerk_v043_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_63d_jerk_v044_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_63d_jerk_v045_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_126d_jerk_v046_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_126d_jerk_v047_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_126d_jerk_v048_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_189d_jerk_v049_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_189d_jerk_v050_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_189d_jerk_v051_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_252d_jerk_v052_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_252d_jerk_v053_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_252d_jerk_v054_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_378d_jerk_v055_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_378d_jerk_v056_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_378d_jerk_v057_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_504d_jerk_v058_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_504d_jerk_v059_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_504d_jerk_v060_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_5d_jerk_v061_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_5d_jerk_v062_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_5d_jerk_v063_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_10d_jerk_v064_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_10d_jerk_v065_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_10d_jerk_v066_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_21d_jerk_v067_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_21d_jerk_v068_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_21d_jerk_v069_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_42d_jerk_v070_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_42d_jerk_v071_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_42d_jerk_v072_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_63d_jerk_v073_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_63d_jerk_v074_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_63d_jerk_v075_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_126d_jerk_v076_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_126d_jerk_v077_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_126d_jerk_v078_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_189d_jerk_v079_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_189d_jerk_v080_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_189d_jerk_v081_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_252d_jerk_v082_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_252d_jerk_v083_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_252d_jerk_v084_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_378d_jerk_v085_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_378d_jerk_v086_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_378d_jerk_v087_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_504d_jerk_v088_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_504d_jerk_v089_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_504d_jerk_v090_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_5d_jerk_v091_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_5d_jerk_v092_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_5d_jerk_v093_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_10d_jerk_v094_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_10d_jerk_v095_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_10d_jerk_v096_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_21d_jerk_v097_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_21d_jerk_v098_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_21d_jerk_v099_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_42d_jerk_v100_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_42d_jerk_v101_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_42d_jerk_v102_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_63d_jerk_v103_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_63d_jerk_v104_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_63d_jerk_v105_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_126d_jerk_v106_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_126d_jerk_v107_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_126d_jerk_v108_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_189d_jerk_v109_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_189d_jerk_v110_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_189d_jerk_v111_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_252d_jerk_v112_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_252d_jerk_v113_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_252d_jerk_v114_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_378d_jerk_v115_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_378d_jerk_v116_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_378d_jerk_v117_signal,
    f088lbt_f088_liquidity_buffer_trend_crssq_504d_jerk_v118_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsq_504d_jerk_v119_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsq_504d_jerk_v120_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_5d_jerk_v121_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_5d_jerk_v122_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_5d_jerk_v123_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_10d_jerk_v124_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_10d_jerk_v125_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_10d_jerk_v126_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_21d_jerk_v127_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_21d_jerk_v128_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_21d_jerk_v129_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_42d_jerk_v130_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_42d_jerk_v131_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_42d_jerk_v132_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_63d_jerk_v133_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_63d_jerk_v134_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_63d_jerk_v135_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_126d_jerk_v136_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_126d_jerk_v137_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_126d_jerk_v138_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_189d_jerk_v139_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_189d_jerk_v140_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_189d_jerk_v141_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_252d_jerk_v142_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_252d_jerk_v143_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_252d_jerk_v144_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_378d_jerk_v145_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_378d_jerk_v146_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_378d_jerk_v147_signal,
    f088lbt_f088_liquidity_buffer_trend_crsab_504d_jerk_v148_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtab_504d_jerk_v149_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqab_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F088_LIQUIDITY_BUFFER_TREND_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f088_liquidity_buffer_trend_3rd_derivatives_001_150_claude: {n_features} features pass")
