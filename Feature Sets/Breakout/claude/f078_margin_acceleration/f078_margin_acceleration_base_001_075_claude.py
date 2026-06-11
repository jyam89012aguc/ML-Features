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
def _f078_margin_diff(em, w):
    return em.diff(w)

def _f078_margin_acceleration(em, w):
    d1 = em.diff(w)
    return d1.diff(w)

def _f078_inflection_strength(em, gm, w):
    em_a = em.diff(w).diff(w)
    gm_a = gm.diff(w).diff(w)
    return em_a + gm_a


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v001_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v002_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v003_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (np.sign(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v004_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (_mean(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v005_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (_std(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v006_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (_z(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v007_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v008_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (np.sqrt(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v009_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (np.log1p(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v010_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v011_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (_mean(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v012_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (_std(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v013_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.ewm(span=5, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v014_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.ewm(span=5, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v015_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (_z(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v016_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v017_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v018_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v019_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v020_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(2, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v021_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(4, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v022_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim * prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v023_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim.pct_change(5).replace([np.inf, -np.inf], np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v024_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim - prim.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_5d_base_v025_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_diff(ebitdamargin, 5)
    result = (prim / prim.shift(5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v026_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v027_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v028_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (np.sign(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v029_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (_mean(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v030_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (_std(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v031_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (_z(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v032_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v033_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (np.sqrt(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v034_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (np.log1p(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v035_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v036_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (_mean(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v037_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (_std(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v038_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.ewm(span=5, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v039_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.ewm(span=5, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v040_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (_z(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v041_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v042_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v043_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v044_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v045_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(2, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v046_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.rolling(5, min_periods=max(4, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v047_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim * prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v048_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim.pct_change(5).replace([np.inf, -np.inf], np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v049_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim - prim.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v050_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_margin_acceleration(ebitdamargin, 5)
    result = (prim / prim.shift(5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v051_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v052_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v053_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (np.sign(prim)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v054_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (_mean(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v055_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (_std(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v056_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (_z(prim, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v057_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v058_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (np.sqrt(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v059_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (np.log1p(prim.abs())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v060_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.diff(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v061_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (_mean(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v062_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (_std(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v063_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.ewm(span=5, adjust=False).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v064_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.ewm(span=5, adjust=False).std()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v065_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (_z(prim, max(2, 5 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v066_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).sum()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v067_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).max()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v068_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v069_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.rolling(5, min_periods=max(1, 5 // 2)).median()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v070_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.rolling(5, min_periods=max(2, 5 // 2)).skew()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v071_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.rolling(5, min_periods=max(4, 5 // 2)).kurt()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v072_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim * prim * prim) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v073_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim.pct_change(5).replace([np.inf, -np.inf], np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v074_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim - prim.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_5d_base_v075_signal(ebitdamargin, grossmargin, closeadj):
    prim = _f078_inflection_strength(ebitdamargin, grossmargin, 5)
    result = (prim / prim.shift(5).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v001_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v002_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v003_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v004_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v005_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v006_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v007_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v008_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v009_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v010_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v011_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v012_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v013_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v014_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v015_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v016_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v017_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v018_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v019_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v020_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v021_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v022_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v023_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v024_signal,
    f078mac_f078_margin_acceleration_margin_diff_5d_base_v025_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v026_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v027_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v028_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v029_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v030_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v031_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v032_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v033_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v034_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v035_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v036_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v037_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v038_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v039_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v040_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v041_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v042_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v043_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v044_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v045_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v046_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v047_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v048_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v049_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_5d_base_v050_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v051_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v052_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v053_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v054_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v055_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v056_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v057_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v058_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v059_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v060_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v061_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v062_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v063_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v064_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v065_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v066_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v067_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v068_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v069_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v070_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v071_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v072_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v073_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v074_signal,
    f078mac_f078_margin_acceleration_inflection_strength_5d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F078_MARGIN_ACCELERATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    cols = {"ebitdamargin": ebitdamargin, "grossmargin": grossmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f078_margin_diff", "_f078_margin_acceleration", "_f078_inflection_strength",)
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
    print(f"OK f078_margin_acceleration_base_001_075_claude: {n_features} features pass")
