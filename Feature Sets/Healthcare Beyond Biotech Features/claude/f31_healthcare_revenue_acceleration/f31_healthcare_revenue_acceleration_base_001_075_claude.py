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
def _f31_revenue_growth_accel(revenue, w):
    g = revenue.pct_change(periods=w)
    return g - g.shift(w)


def _f31_acceleration_persistence(revenue, w):
    g = revenue.pct_change(periods=w)
    a = g - g.shift(w)
    return _mean(a, w) / _std(a, w).replace(0, np.nan)


def _f31_growth_quality(revenue, ebitda, w):
    rg = revenue.pct_change(periods=w)
    eg = ebitda.pct_change(periods=w)
    return _mean(eg - rg, w)


# ---- features ----

def f31hra_f31_healthcare_revenue_acceleration_accel_21d_base_v001_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_63d_base_v002_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_126d_base_v003_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_252d_base_v004_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_504d_base_v005_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_5d_base_v006_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_10d_base_v007_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_42d_base_v008_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_189d_base_v009_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accel_378d_base_v010_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmean_21d_base_v011_signal(revenue, closeadj):
    result = _mean(_f31_revenue_growth_accel(revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmean_63d_base_v012_signal(revenue, closeadj):
    result = _mean(_f31_revenue_growth_accel(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmean_126d_base_v013_signal(revenue, closeadj):
    result = _mean(_f31_revenue_growth_accel(revenue, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmean_252d_base_v014_signal(revenue, closeadj):
    result = _mean(_f31_revenue_growth_accel(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmean_504d_base_v015_signal(revenue, closeadj):
    result = _mean(_f31_revenue_growth_accel(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelstd_63d_base_v016_signal(revenue, closeadj):
    result = _std(_f31_revenue_growth_accel(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelstd_126d_base_v017_signal(revenue, closeadj):
    result = _std(_f31_revenue_growth_accel(revenue, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelstd_252d_base_v018_signal(revenue, closeadj):
    result = _std(_f31_revenue_growth_accel(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelstd_504d_base_v019_signal(revenue, closeadj):
    result = _std(_f31_revenue_growth_accel(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelz_63d_base_v020_signal(revenue, closeadj):
    result = _z(_f31_revenue_growth_accel(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelz_126d_base_v021_signal(revenue, closeadj):
    result = _z(_f31_revenue_growth_accel(revenue, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelz_252d_base_v022_signal(revenue, closeadj):
    result = _z(_f31_revenue_growth_accel(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_21d_base_v023_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_63d_base_v024_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_126d_base_v025_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_252d_base_v026_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persist_504d_base_v027_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_21d_base_v028_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_63d_base_v029_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_126d_base_v030_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_252d_base_v031_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_quality_504d_base_v032_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelema_21d_base_v033_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    result = base.ewm(span=21, min_periods=10).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelema_63d_base_v034_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelema_252d_base_v035_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxprice_63d_base_v036_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxprice_252d_base_v037_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelsign_63d_base_v038_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = np.sign(base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelsign_252d_base_v039_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelsq_63d_base_v040_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelsq_252d_base_v041_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistmean_63d_base_v042_signal(revenue, closeadj):
    result = _mean(_f31_acceleration_persistence(revenue, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistmean_252d_base_v043_signal(revenue, closeadj):
    result = _mean(_f31_acceleration_persistence(revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxprice_63d_base_v044_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistxprice_252d_base_v045_signal(revenue, closeadj):
    result = _f31_acceleration_persistence(revenue, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualitymean_63d_base_v046_signal(revenue, ebitda, closeadj):
    result = _mean(_f31_growth_quality(revenue, ebitda, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualitymean_252d_base_v047_signal(revenue, ebitda, closeadj):
    result = _mean(_f31_growth_quality(revenue, ebitda, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityz_63d_base_v048_signal(revenue, ebitda, closeadj):
    result = _z(_f31_growth_quality(revenue, ebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityz_252d_base_v049_signal(revenue, ebitda, closeadj):
    result = _z(_f31_growth_quality(revenue, ebitda, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityema_63d_base_v050_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityema_252d_base_v051_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmax_252d_base_v052_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelmin_252d_base_v053_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelrange_252d_base_v054_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelrank_63d_base_v055_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    rank = base.rolling(63, min_periods=20).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelrank_252d_base_v056_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelrank_504d_base_v057_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    rank = base.rolling(504, min_periods=126).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistz_63d_base_v058_signal(revenue, closeadj):
    result = _z(_f31_acceleration_persistence(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persistz_252d_base_v059_signal(revenue, closeadj):
    result = _z(_f31_acceleration_persistence(revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_persiststd_252d_base_v060_signal(revenue, closeadj):
    result = _std(_f31_acceleration_persistence(revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxprice_63d_base_v061_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityxprice_252d_base_v062_signal(revenue, ebitda, closeadj):
    result = _f31_growth_quality(revenue, ebitda, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualitystd_252d_base_v063_signal(revenue, ebitda, closeadj):
    result = _std(_f31_growth_quality(revenue, ebitda, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualitysq_252d_base_v064_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = base * base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualitysign_252d_base_v065_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 252)
    result = np.sign(base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityrank_252d_base_v066_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    rank = base.rolling(252, min_periods=63).rank(pct=True)
    result = rank * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxclose_42d_base_v067_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 42) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelxclose_189d_base_v068_signal(revenue, closeadj):
    result = _f31_revenue_growth_accel(revenue, 189) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accellog_63d_base_v069_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accellog_252d_base_v070_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 252)
    sg = np.sign(base)
    result = sg * np.log1p(base.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualityratio_63v252_base_v071_signal(revenue, ebitda, closeadj):
    a = _f31_growth_quality(revenue, ebitda, 63)
    b = _f31_growth_quality(revenue, ebitda, 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelratio_63v252_base_v072_signal(revenue, closeadj):
    a = _mean(_f31_revenue_growth_accel(revenue, 63), 63)
    b = _mean(_f31_revenue_growth_accel(revenue, 252), 252).replace(0, np.nan)
    result = (a / b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelcumsum_63d_base_v073_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 21)
    result = base.rolling(63, min_periods=20).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_accelcumsum_252d_base_v074_signal(revenue, closeadj):
    base = _f31_revenue_growth_accel(revenue, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f31hra_f31_healthcare_revenue_acceleration_qualitycumsum_252d_base_v075_signal(revenue, ebitda, closeadj):
    base = _f31_growth_quality(revenue, ebitda, 63)
    result = base.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31hra_f31_healthcare_revenue_acceleration_accel_21d_base_v001_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_63d_base_v002_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_126d_base_v003_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_252d_base_v004_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_504d_base_v005_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_5d_base_v006_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_10d_base_v007_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_42d_base_v008_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_189d_base_v009_signal,
    f31hra_f31_healthcare_revenue_acceleration_accel_378d_base_v010_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmean_21d_base_v011_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmean_63d_base_v012_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmean_126d_base_v013_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmean_252d_base_v014_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmean_504d_base_v015_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelstd_63d_base_v016_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelstd_126d_base_v017_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelstd_252d_base_v018_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelstd_504d_base_v019_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelz_63d_base_v020_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelz_126d_base_v021_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelz_252d_base_v022_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_21d_base_v023_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_63d_base_v024_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_126d_base_v025_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_252d_base_v026_signal,
    f31hra_f31_healthcare_revenue_acceleration_persist_504d_base_v027_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_21d_base_v028_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_63d_base_v029_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_126d_base_v030_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_252d_base_v031_signal,
    f31hra_f31_healthcare_revenue_acceleration_quality_504d_base_v032_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelema_21d_base_v033_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelema_63d_base_v034_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelema_252d_base_v035_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxprice_63d_base_v036_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxprice_252d_base_v037_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelsign_63d_base_v038_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelsign_252d_base_v039_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelsq_63d_base_v040_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelsq_252d_base_v041_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistmean_63d_base_v042_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistmean_252d_base_v043_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxprice_63d_base_v044_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistxprice_252d_base_v045_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualitymean_63d_base_v046_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualitymean_252d_base_v047_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityz_63d_base_v048_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityz_252d_base_v049_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityema_63d_base_v050_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityema_252d_base_v051_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmax_252d_base_v052_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelmin_252d_base_v053_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelrange_252d_base_v054_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelrank_63d_base_v055_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelrank_252d_base_v056_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelrank_504d_base_v057_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistz_63d_base_v058_signal,
    f31hra_f31_healthcare_revenue_acceleration_persistz_252d_base_v059_signal,
    f31hra_f31_healthcare_revenue_acceleration_persiststd_252d_base_v060_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxprice_63d_base_v061_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityxprice_252d_base_v062_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualitystd_252d_base_v063_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualitysq_252d_base_v064_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualitysign_252d_base_v065_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityrank_252d_base_v066_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxclose_42d_base_v067_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelxclose_189d_base_v068_signal,
    f31hra_f31_healthcare_revenue_acceleration_accellog_63d_base_v069_signal,
    f31hra_f31_healthcare_revenue_acceleration_accellog_252d_base_v070_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualityratio_63v252_base_v071_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelratio_63v252_base_v072_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelcumsum_63d_base_v073_signal,
    f31hra_f31_healthcare_revenue_acceleration_accelcumsum_252d_base_v074_signal,
    f31hra_f31_healthcare_revenue_acceleration_qualitycumsum_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_HEALTHCARE_REVENUE_ACCELERATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "ebitda": ebitda,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_revenue_growth_accel", "_f31_acceleration_persistence", "_f31_growth_quality")
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
    print(f"OK f31_healthcare_revenue_acceleration_base_001_075_claude: {n_features} features pass")
