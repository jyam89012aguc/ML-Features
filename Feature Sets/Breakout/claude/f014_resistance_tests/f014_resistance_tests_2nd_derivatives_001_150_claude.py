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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f014_near_max_proxy(close, w):
    mx = close.rolling(w, min_periods=max(1, w // 2)).max()
    # Continuous proximity score: 1 at max, decays as price falls.
    return (close / mx.replace(0, np.nan)).clip(lower=0)


def _f014_resistance_tests(close, w):
    mx = close.rolling(w, min_periods=max(1, w // 2)).max()
    prox = (close / mx.replace(0, np.nan)).clip(lower=0)
    # Soft test density: how often near the max during window.
    near = (prox > 0.97).astype(float)
    return near.rolling(w, min_periods=max(1, w // 2)).sum() + prox


def _f014_test_intensity(close, w):
    mx = close.rolling(w, min_periods=max(1, w // 2)).max()
    prox = (close / mx.replace(0, np.nan)).clip(lower=0)
    near = (prox > 0.97).astype(float)
    cnt = near.rolling(w, min_periods=max(1, w // 2)).sum()
    return (cnt + prox * w) * close / float(w)


def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v001_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v002_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v003_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v004_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v005_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v006_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v007_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v008_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v009_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v010_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v011_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v012_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v013_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v014_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v015_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v016_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v017_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v018_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v019_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v020_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v021_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v022_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v023_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v024_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v025_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v026_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v027_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v028_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v029_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v030_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v031_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v032_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v033_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v034_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v035_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v036_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v037_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v038_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v039_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v040_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v041_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v042_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v043_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v044_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v045_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v046_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v047_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v048_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v049_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v050_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v051_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v052_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v053_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v054_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v055_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v056_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v057_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v058_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v059_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v060_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v061_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v062_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v063_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v064_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v065_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v066_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v067_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v068_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v069_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v070_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v071_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v072_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v073_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v074_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v075_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v076_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v077_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v078_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v079_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v080_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v081_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v082_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v083_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v084_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v085_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v086_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v087_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v088_signal(closeadj):
    result = _slope_pct((_f014_near_max_proxy(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v089_signal(closeadj):
    result = _slope_pct((_f014_resistance_tests(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v090_signal(closeadj):
    result = _slope_pct((_f014_test_intensity(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v091_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v092_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v093_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v094_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v095_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v096_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v097_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v098_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v099_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v100_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v101_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v102_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v103_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v104_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v105_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v106_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v107_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v108_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v109_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v110_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v111_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v112_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v113_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v114_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v115_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v116_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v117_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v118_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v119_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v120_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v121_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v122_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v123_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v124_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v125_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v126_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v127_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v128_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v129_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v130_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v131_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v132_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v133_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_63d_slope_v134_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_63d_slope_v135_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v136_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_126d_slope_v137_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_126d_slope_v138_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v139_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_189d_slope_v140_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_189d_slope_v141_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v142_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_252d_slope_v143_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_252d_slope_v144_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v145_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_21d_slope_v146_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_21d_slope_v147_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v148_signal(closeadj):
    result = _slope_diff_norm((_f014_near_max_proxy(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_resistance_tests_42d_slope_v149_signal(closeadj):
    result = _slope_diff_norm((_f014_resistance_tests(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f014rts_f014_resistance_tests_test_intensity_42d_slope_v150_signal(closeadj):
    result = _slope_diff_norm((_f014_test_intensity(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v001_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v002_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v003_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v004_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v005_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v006_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v007_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v008_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v009_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v010_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v011_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v012_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v013_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v014_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v015_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v016_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v017_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v018_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v019_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v020_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v021_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v022_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v023_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v024_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v025_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v026_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v027_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v028_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v029_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v030_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v031_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v032_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v033_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v034_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v035_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v036_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v037_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v038_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v039_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v040_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v041_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v042_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v043_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v044_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v045_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v046_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v047_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v048_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v049_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v050_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v051_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v052_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v053_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v054_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v055_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v056_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v057_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v058_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v059_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v060_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v061_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v062_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v063_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v064_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v065_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v066_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v067_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v068_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v069_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v070_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v071_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v072_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v073_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v074_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v075_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v076_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v077_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v078_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v079_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v080_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v081_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v082_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v083_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v084_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v085_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v086_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v087_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v088_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v089_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v090_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v091_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v092_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v093_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v094_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v095_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v096_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v097_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v098_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v099_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v100_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v101_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v102_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v103_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v104_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v105_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v106_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v107_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v108_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v109_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v110_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v111_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v112_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v113_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v114_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v115_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v116_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v117_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v118_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v119_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v120_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v121_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v122_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v123_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v124_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v125_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v126_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v127_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v128_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v129_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v130_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v131_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v132_signal,
    f014rts_f014_resistance_tests_near_max_proxy_63d_slope_v133_signal,
    f014rts_f014_resistance_tests_resistance_tests_63d_slope_v134_signal,
    f014rts_f014_resistance_tests_test_intensity_63d_slope_v135_signal,
    f014rts_f014_resistance_tests_near_max_proxy_126d_slope_v136_signal,
    f014rts_f014_resistance_tests_resistance_tests_126d_slope_v137_signal,
    f014rts_f014_resistance_tests_test_intensity_126d_slope_v138_signal,
    f014rts_f014_resistance_tests_near_max_proxy_189d_slope_v139_signal,
    f014rts_f014_resistance_tests_resistance_tests_189d_slope_v140_signal,
    f014rts_f014_resistance_tests_test_intensity_189d_slope_v141_signal,
    f014rts_f014_resistance_tests_near_max_proxy_252d_slope_v142_signal,
    f014rts_f014_resistance_tests_resistance_tests_252d_slope_v143_signal,
    f014rts_f014_resistance_tests_test_intensity_252d_slope_v144_signal,
    f014rts_f014_resistance_tests_near_max_proxy_21d_slope_v145_signal,
    f014rts_f014_resistance_tests_resistance_tests_21d_slope_v146_signal,
    f014rts_f014_resistance_tests_test_intensity_21d_slope_v147_signal,
    f014rts_f014_resistance_tests_near_max_proxy_42d_slope_v148_signal,
    f014rts_f014_resistance_tests_resistance_tests_42d_slope_v149_signal,
    f014rts_f014_resistance_tests_test_intensity_42d_slope_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F014_RESISTANCE_TESTS_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {
        "closeadj": closeadj,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f014_near_max_proxy", "_f014_resistance_tests", "_f014_test_intensity")
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
    print(f"OK f014_resistance_tests_slope_001_150_claude: {n_features} features pass")
