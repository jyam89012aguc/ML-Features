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
def _f095_quality_signal(roic, w):
    return _mean(roic, w)


def _f095_low_share_growth(sharesbas, w):
    return -sharesbas.pct_change(w).fillna(0)


def _f095_skilled_proxy(roic, sharesbas, w):
    q = _mean(roic, w)
    low_g = -sharesbas.pct_change(w).fillna(0)
    return q + low_g


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_5d_base_v001_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_5d_base_v002_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_5d_base_v003_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_10d_base_v004_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_10d_base_v005_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_10d_base_v006_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_21d_base_v007_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_21d_base_v008_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_21d_base_v009_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_42d_base_v010_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_42d_base_v011_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_42d_base_v012_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_63d_base_v013_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_63d_base_v014_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_63d_base_v015_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_126d_base_v016_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_126d_base_v017_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_126d_base_v018_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_189d_base_v019_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_189d_base_v020_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_189d_base_v021_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_252d_base_v022_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_252d_base_v023_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_252d_base_v024_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_378d_base_v025_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_378d_base_v026_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_378d_base_v027_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsraw_504d_base_v028_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrraw_504d_base_v029_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyraw_504d_base_v030_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_5d_base_v031_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_5d_base_v032_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_5d_base_v033_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_10d_base_v034_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_10d_base_v035_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_10d_base_v036_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_21d_base_v037_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_21d_base_v038_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_21d_base_v039_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_42d_base_v040_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_42d_base_v041_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_42d_base_v042_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_63d_base_v043_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_63d_base_v044_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_63d_base_v045_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_126d_base_v046_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_126d_base_v047_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_126d_base_v048_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_189d_base_v049_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_189d_base_v050_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_189d_base_v051_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_252d_base_v052_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_252d_base_v053_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_252d_base_v054_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_378d_base_v055_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_378d_base_v056_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_378d_base_v057_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualsabs_504d_base_v058_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrabs_504d_base_v059_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxyabs_504d_base_v060_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualssqs_5d_base_v061_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrsqs_5d_base_v062_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxysqs_5d_base_v063_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualssqs_10d_base_v064_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrsqs_10d_base_v065_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxysqs_10d_base_v066_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualssqs_21d_base_v067_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrsqs_21d_base_v068_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxysqs_21d_base_v069_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualssqs_42d_base_v070_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrsqs_42d_base_v071_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxysqs_42d_base_v072_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_qualssqs_63d_base_v073_signal(roic, sharesbas, closeadj):
    base = _f095_quality_signal(roic, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_losgrsqs_63d_base_v074_signal(roic, sharesbas, closeadj):
    base = _f095_low_share_growth(sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f095sma_f095_skilled_manager_adds_proxy_skpxysqs_63d_base_v075_signal(roic, sharesbas, closeadj):
    base = _f095_skilled_proxy(roic, sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_5d_base_v001_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_5d_base_v002_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_5d_base_v003_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_10d_base_v004_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_10d_base_v005_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_10d_base_v006_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_21d_base_v007_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_21d_base_v008_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_21d_base_v009_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_42d_base_v010_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_42d_base_v011_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_42d_base_v012_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_63d_base_v013_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_63d_base_v014_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_63d_base_v015_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_126d_base_v016_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_126d_base_v017_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_126d_base_v018_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_189d_base_v019_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_189d_base_v020_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_189d_base_v021_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_252d_base_v022_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_252d_base_v023_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_252d_base_v024_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_378d_base_v025_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_378d_base_v026_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_378d_base_v027_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsraw_504d_base_v028_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrraw_504d_base_v029_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyraw_504d_base_v030_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_5d_base_v031_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_5d_base_v032_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_5d_base_v033_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_10d_base_v034_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_10d_base_v035_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_10d_base_v036_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_21d_base_v037_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_21d_base_v038_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_21d_base_v039_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_42d_base_v040_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_42d_base_v041_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_42d_base_v042_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_63d_base_v043_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_63d_base_v044_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_63d_base_v045_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_126d_base_v046_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_126d_base_v047_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_126d_base_v048_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_189d_base_v049_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_189d_base_v050_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_189d_base_v051_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_252d_base_v052_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_252d_base_v053_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_252d_base_v054_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_378d_base_v055_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_378d_base_v056_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_378d_base_v057_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualsabs_504d_base_v058_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrabs_504d_base_v059_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxyabs_504d_base_v060_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualssqs_5d_base_v061_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrsqs_5d_base_v062_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxysqs_5d_base_v063_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualssqs_10d_base_v064_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrsqs_10d_base_v065_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxysqs_10d_base_v066_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualssqs_21d_base_v067_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrsqs_21d_base_v068_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxysqs_21d_base_v069_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualssqs_42d_base_v070_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrsqs_42d_base_v071_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxysqs_42d_base_v072_signal,
    f095sma_f095_skilled_manager_adds_proxy_qualssqs_63d_base_v073_signal,
    f095sma_f095_skilled_manager_adds_proxy_losgrsqs_63d_base_v074_signal,
    f095sma_f095_skilled_manager_adds_proxy_skpxysqs_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F095_SKILLED_MANAGER_ADDS_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f095_quality_signal", "_f095_low_share_growth", "_f095_skilled_proxy")
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
    print(f"OK f095_skilled_manager_adds_proxy_base_001_075_claude: {n_features} features pass")
