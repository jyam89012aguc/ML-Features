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

def f088lbt_f088_liquidity_buffer_trend_crs_5d_base_v001_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_5d_base_v002_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_5d_base_v003_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_10d_base_v004_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_10d_base_v005_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_10d_base_v006_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_21d_base_v007_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_21d_base_v008_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_21d_base_v009_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_42d_base_v010_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_42d_base_v011_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_42d_base_v012_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_63d_base_v013_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_63d_base_v014_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_63d_base_v015_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_126d_base_v016_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_126d_base_v017_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_126d_base_v018_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_189d_base_v019_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_189d_base_v020_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_189d_base_v021_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_252d_base_v022_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_252d_base_v023_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_252d_base_v024_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_378d_base_v025_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_378d_base_v026_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_378d_base_v027_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crs_504d_base_v028_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqt_504d_base_v029_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqq_504d_base_v030_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_5d_base_v031_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_5d_base_v032_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_5d_base_v033_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_10d_base_v034_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_10d_base_v035_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_10d_base_v036_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_21d_base_v037_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_21d_base_v038_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_21d_base_v039_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_42d_base_v040_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_42d_base_v041_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_42d_base_v042_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_63d_base_v043_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_63d_base_v044_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_63d_base_v045_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_126d_base_v046_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_126d_base_v047_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_126d_base_v048_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_189d_base_v049_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_189d_base_v050_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_189d_base_v051_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_252d_base_v052_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_252d_base_v053_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_252d_base_v054_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_378d_base_v055_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_378d_base_v056_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_378d_base_v057_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crsabs_504d_base_v058_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtabs_504d_base_v059_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqabs_504d_base_v060_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssqrt_5d_base_v061_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsqrt_5d_base_v062_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsqrt_5d_base_v063_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssqrt_10d_base_v064_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsqrt_10d_base_v065_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsqrt_10d_base_v066_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssqrt_21d_base_v067_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsqrt_21d_base_v068_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsqrt_21d_base_v069_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssqrt_42d_base_v070_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsqrt_42d_base_v071_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsqrt_42d_base_v072_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_crssqrt_63d_base_v073_signal(currentratio, closeadj):
    base = _f088_current_ratio_slope(currentratio, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqtsqrt_63d_base_v074_signal(currentratio, closeadj):
    base = _f088_liquidity_trend(currentratio, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f088lbt_f088_liquidity_buffer_trend_lqqsqrt_63d_base_v075_signal(currentratio, closeadj):
    base = _f088_liquidity_quality(currentratio, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f088lbt_f088_liquidity_buffer_trend_crs_5d_base_v001_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_5d_base_v002_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_5d_base_v003_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_10d_base_v004_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_10d_base_v005_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_10d_base_v006_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_21d_base_v007_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_21d_base_v008_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_21d_base_v009_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_42d_base_v010_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_42d_base_v011_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_42d_base_v012_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_63d_base_v013_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_63d_base_v014_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_63d_base_v015_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_126d_base_v016_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_126d_base_v017_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_126d_base_v018_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_189d_base_v019_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_189d_base_v020_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_189d_base_v021_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_252d_base_v022_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_252d_base_v023_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_252d_base_v024_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_378d_base_v025_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_378d_base_v026_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_378d_base_v027_signal,
    f088lbt_f088_liquidity_buffer_trend_crs_504d_base_v028_signal,
    f088lbt_f088_liquidity_buffer_trend_lqt_504d_base_v029_signal,
    f088lbt_f088_liquidity_buffer_trend_lqq_504d_base_v030_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_5d_base_v031_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_5d_base_v032_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_5d_base_v033_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_10d_base_v034_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_10d_base_v035_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_10d_base_v036_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_21d_base_v037_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_21d_base_v038_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_21d_base_v039_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_42d_base_v040_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_42d_base_v041_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_42d_base_v042_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_63d_base_v043_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_63d_base_v044_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_63d_base_v045_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_126d_base_v046_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_126d_base_v047_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_126d_base_v048_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_189d_base_v049_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_189d_base_v050_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_189d_base_v051_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_252d_base_v052_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_252d_base_v053_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_252d_base_v054_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_378d_base_v055_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_378d_base_v056_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_378d_base_v057_signal,
    f088lbt_f088_liquidity_buffer_trend_crsabs_504d_base_v058_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtabs_504d_base_v059_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqabs_504d_base_v060_signal,
    f088lbt_f088_liquidity_buffer_trend_crssqrt_5d_base_v061_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsqrt_5d_base_v062_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsqrt_5d_base_v063_signal,
    f088lbt_f088_liquidity_buffer_trend_crssqrt_10d_base_v064_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsqrt_10d_base_v065_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsqrt_10d_base_v066_signal,
    f088lbt_f088_liquidity_buffer_trend_crssqrt_21d_base_v067_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsqrt_21d_base_v068_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsqrt_21d_base_v069_signal,
    f088lbt_f088_liquidity_buffer_trend_crssqrt_42d_base_v070_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsqrt_42d_base_v071_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsqrt_42d_base_v072_signal,
    f088lbt_f088_liquidity_buffer_trend_crssqrt_63d_base_v073_signal,
    f088lbt_f088_liquidity_buffer_trend_lqtsqrt_63d_base_v074_signal,
    f088lbt_f088_liquidity_buffer_trend_lqqsqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F088_LIQUIDITY_BUFFER_TREND_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f088_liquidity_buffer_trend_base_001_075_claude: {n_features} features pass")
