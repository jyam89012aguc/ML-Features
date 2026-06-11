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
def _f079_roic_slope(r, w):
    return (r - r.shift(w)) / w

def _f079_roic_improvement(r, w):
    sm = r.rolling(w, min_periods=max(1, w // 2)).mean()
    return sm - sm.shift(w)

def _f079_value_creation(r, w):
    sm = r.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = r.rolling(w, min_periods=max(1, w // 2)).std()
    return (r - sm) / sd.replace(0, np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v001_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v002_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v003_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (np.sign(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v004_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (_mean(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v005_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (_std(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v006_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (_z(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v007_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v008_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (np.sqrt(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v009_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (np.log1p(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v010_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v011_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (_mean(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v012_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (_std(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v013_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.ewm(span=5, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v014_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.ewm(span=5, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v015_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (_z(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v016_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v017_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v018_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v019_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v020_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.rolling(5, min_periods=max(2, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v021_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.rolling(5, min_periods=max(4, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v022_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim * prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v023_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim.pct_change(5).replace([np.inf, -np.inf], np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v024_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim - prim.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_5d_base_v025_signal(roic, closeadj):
    prim = _f079_roic_slope(roic, 5)
    result = (prim / prim.shift(5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v026_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v027_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v028_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (np.sign(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v029_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (_mean(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v030_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (_std(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v031_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (_z(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v032_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v033_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (np.sqrt(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v034_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (np.log1p(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v035_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v036_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (_mean(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v037_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (_std(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v038_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.ewm(span=5, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v039_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.ewm(span=5, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v040_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (_z(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v041_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v042_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v043_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v044_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v045_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.rolling(5, min_periods=max(2, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v046_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.rolling(5, min_periods=max(4, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v047_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim * prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v048_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim.pct_change(5).replace([np.inf, -np.inf], np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v049_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim - prim.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_5d_base_v050_signal(roic, closeadj):
    prim = _f079_roic_improvement(roic, 5)
    result = (prim / prim.shift(5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v051_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v052_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v053_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (np.sign(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v054_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (_mean(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v055_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (_std(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v056_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (_z(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v057_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v058_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (np.sqrt(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v059_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (np.log1p(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v060_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v061_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (_mean(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v062_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (_std(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v063_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.ewm(span=5, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v064_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.ewm(span=5, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v065_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (_z(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v066_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v067_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v068_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v069_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v070_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.rolling(5, min_periods=max(2, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v071_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.rolling(5, min_periods=max(4, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v072_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim * prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v073_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim.pct_change(5).replace([np.inf, -np.inf], np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v074_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim - prim.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_5d_base_v075_signal(roic, closeadj):
    prim = _f079_value_creation(roic, 5)
    result = (prim / prim.shift(5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f079rct_f079_roic_trend_roic_slope_5d_base_v001_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v002_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v003_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v004_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v005_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v006_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v007_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v008_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v009_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v010_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v011_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v012_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v013_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v014_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v015_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v016_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v017_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v018_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v019_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v020_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v021_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v022_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v023_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v024_signal,
    f079rct_f079_roic_trend_roic_slope_5d_base_v025_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v026_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v027_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v028_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v029_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v030_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v031_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v032_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v033_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v034_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v035_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v036_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v037_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v038_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v039_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v040_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v041_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v042_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v043_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v044_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v045_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v046_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v047_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v048_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v049_signal,
    f079rct_f079_roic_trend_roic_improvement_5d_base_v050_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v051_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v052_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v053_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v054_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v055_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v056_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v057_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v058_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v059_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v060_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v061_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v062_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v063_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v064_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v065_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v066_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v067_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v068_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v069_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v070_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v071_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v072_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v073_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v074_signal,
    f079rct_f079_roic_trend_value_creation_5d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F079_ROIC_TREND_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {"roic": roic, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f079_roic_slope", "_f079_roic_improvement", "_f079_value_creation",)
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
    print(f"OK f079_roic_trend_base_001_075_claude: {n_features} features pass")
