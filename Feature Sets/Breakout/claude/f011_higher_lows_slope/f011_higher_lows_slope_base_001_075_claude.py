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
def _f011_rolling_min(close, w):
    return close.rolling(w, min_periods=max(1, w // 2)).min()


def _f011_higher_lows_slope(close, w):
    rmin = close.rolling(w, min_periods=max(1, w // 2)).min()
    return rmin.diff(periods=max(1, w // 2)) / rmin.abs().replace(0, np.nan)


def _f011_support_rising(close, w):
    rmin = close.rolling(w, min_periods=max(1, w // 2)).min()
    rmean = close.rolling(w, min_periods=max(1, w // 2)).mean()
    return (rmin - rmin.shift(max(1, w // 4))) * close / rmean.replace(0, np.nan)


def f011hls_f011_higher_lows_slope_rolling_min_5d_base_v001_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_10d_base_v002_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_21d_base_v003_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_42d_base_v004_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_63d_base_v005_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_126d_base_v006_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_189d_base_v007_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_252d_base_v008_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_378d_base_v009_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_504d_base_v010_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_5d_base_v011_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_10d_base_v012_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_21d_base_v013_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_42d_base_v014_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_63d_base_v015_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_126d_base_v016_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_189d_base_v017_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_252d_base_v018_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_378d_base_v019_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_504d_base_v020_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_5d_base_v021_signal(closeadj):
    result = (_f011_support_rising(closeadj, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_10d_base_v022_signal(closeadj):
    result = (_f011_support_rising(closeadj, 10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_21d_base_v023_signal(closeadj):
    result = (_f011_support_rising(closeadj, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_42d_base_v024_signal(closeadj):
    result = (_f011_support_rising(closeadj, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_63d_base_v025_signal(closeadj):
    result = (_f011_support_rising(closeadj, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_126d_base_v026_signal(closeadj):
    result = (_f011_support_rising(closeadj, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_189d_base_v027_signal(closeadj):
    result = (_f011_support_rising(closeadj, 189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_252d_base_v028_signal(closeadj):
    result = (_f011_support_rising(closeadj, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_378d_base_v029_signal(closeadj):
    result = (_f011_support_rising(closeadj, 378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_504d_base_v030_signal(closeadj):
    result = (_f011_support_rising(closeadj, 504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_5d_base_v031_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_10d_base_v032_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 10)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_21d_base_v033_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_42d_base_v034_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 42)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_63d_base_v035_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_126d_base_v036_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_189d_base_v037_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 189)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_252d_base_v038_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 252)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_378d_base_v039_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_504d_base_v040_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 504)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_5d_base_v041_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_10d_base_v042_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 10)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_21d_base_v043_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_42d_base_v044_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 42)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_63d_base_v045_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_126d_base_v046_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_189d_base_v047_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 189)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_252d_base_v048_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 252)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_378d_base_v049_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_504d_base_v050_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 504)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_5d_base_v051_signal(closeadj):
    result = (_f011_support_rising(closeadj, 5)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_10d_base_v052_signal(closeadj):
    result = (_f011_support_rising(closeadj, 10)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_21d_base_v053_signal(closeadj):
    result = (_f011_support_rising(closeadj, 21)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_42d_base_v054_signal(closeadj):
    result = (_f011_support_rising(closeadj, 42)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_63d_base_v055_signal(closeadj):
    result = (_f011_support_rising(closeadj, 63)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_126d_base_v056_signal(closeadj):
    result = (_f011_support_rising(closeadj, 126)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_189d_base_v057_signal(closeadj):
    result = (_f011_support_rising(closeadj, 189)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_252d_base_v058_signal(closeadj):
    result = (_f011_support_rising(closeadj, 252)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_378d_base_v059_signal(closeadj):
    result = (_f011_support_rising(closeadj, 378)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_support_rising_504d_base_v060_signal(closeadj):
    result = (_f011_support_rising(closeadj, 504)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_5d_base_v061_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_10d_base_v062_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_21d_base_v063_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_42d_base_v064_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_63d_base_v065_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_126d_base_v066_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 126)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_189d_base_v067_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 189)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_252d_base_v068_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 252)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_378d_base_v069_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 378)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_rolling_min_504d_base_v070_signal(closeadj):
    result = (_f011_rolling_min(closeadj, 504)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_5d_base_v071_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 5)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_10d_base_v072_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 10)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_21d_base_v073_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 21)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_42d_base_v074_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 42)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f011hls_f011_higher_lows_slope_higher_lows_slope_63d_base_v075_signal(closeadj):
    result = (_f011_higher_lows_slope(closeadj, 63)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f011hls_f011_higher_lows_slope_rolling_min_5d_base_v001_signal,
    f011hls_f011_higher_lows_slope_rolling_min_10d_base_v002_signal,
    f011hls_f011_higher_lows_slope_rolling_min_21d_base_v003_signal,
    f011hls_f011_higher_lows_slope_rolling_min_42d_base_v004_signal,
    f011hls_f011_higher_lows_slope_rolling_min_63d_base_v005_signal,
    f011hls_f011_higher_lows_slope_rolling_min_126d_base_v006_signal,
    f011hls_f011_higher_lows_slope_rolling_min_189d_base_v007_signal,
    f011hls_f011_higher_lows_slope_rolling_min_252d_base_v008_signal,
    f011hls_f011_higher_lows_slope_rolling_min_378d_base_v009_signal,
    f011hls_f011_higher_lows_slope_rolling_min_504d_base_v010_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_5d_base_v011_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_10d_base_v012_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_21d_base_v013_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_42d_base_v014_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_63d_base_v015_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_126d_base_v016_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_189d_base_v017_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_252d_base_v018_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_378d_base_v019_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_504d_base_v020_signal,
    f011hls_f011_higher_lows_slope_support_rising_5d_base_v021_signal,
    f011hls_f011_higher_lows_slope_support_rising_10d_base_v022_signal,
    f011hls_f011_higher_lows_slope_support_rising_21d_base_v023_signal,
    f011hls_f011_higher_lows_slope_support_rising_42d_base_v024_signal,
    f011hls_f011_higher_lows_slope_support_rising_63d_base_v025_signal,
    f011hls_f011_higher_lows_slope_support_rising_126d_base_v026_signal,
    f011hls_f011_higher_lows_slope_support_rising_189d_base_v027_signal,
    f011hls_f011_higher_lows_slope_support_rising_252d_base_v028_signal,
    f011hls_f011_higher_lows_slope_support_rising_378d_base_v029_signal,
    f011hls_f011_higher_lows_slope_support_rising_504d_base_v030_signal,
    f011hls_f011_higher_lows_slope_rolling_min_5d_base_v031_signal,
    f011hls_f011_higher_lows_slope_rolling_min_10d_base_v032_signal,
    f011hls_f011_higher_lows_slope_rolling_min_21d_base_v033_signal,
    f011hls_f011_higher_lows_slope_rolling_min_42d_base_v034_signal,
    f011hls_f011_higher_lows_slope_rolling_min_63d_base_v035_signal,
    f011hls_f011_higher_lows_slope_rolling_min_126d_base_v036_signal,
    f011hls_f011_higher_lows_slope_rolling_min_189d_base_v037_signal,
    f011hls_f011_higher_lows_slope_rolling_min_252d_base_v038_signal,
    f011hls_f011_higher_lows_slope_rolling_min_378d_base_v039_signal,
    f011hls_f011_higher_lows_slope_rolling_min_504d_base_v040_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_5d_base_v041_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_10d_base_v042_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_21d_base_v043_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_42d_base_v044_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_63d_base_v045_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_126d_base_v046_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_189d_base_v047_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_252d_base_v048_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_378d_base_v049_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_504d_base_v050_signal,
    f011hls_f011_higher_lows_slope_support_rising_5d_base_v051_signal,
    f011hls_f011_higher_lows_slope_support_rising_10d_base_v052_signal,
    f011hls_f011_higher_lows_slope_support_rising_21d_base_v053_signal,
    f011hls_f011_higher_lows_slope_support_rising_42d_base_v054_signal,
    f011hls_f011_higher_lows_slope_support_rising_63d_base_v055_signal,
    f011hls_f011_higher_lows_slope_support_rising_126d_base_v056_signal,
    f011hls_f011_higher_lows_slope_support_rising_189d_base_v057_signal,
    f011hls_f011_higher_lows_slope_support_rising_252d_base_v058_signal,
    f011hls_f011_higher_lows_slope_support_rising_378d_base_v059_signal,
    f011hls_f011_higher_lows_slope_support_rising_504d_base_v060_signal,
    f011hls_f011_higher_lows_slope_rolling_min_5d_base_v061_signal,
    f011hls_f011_higher_lows_slope_rolling_min_10d_base_v062_signal,
    f011hls_f011_higher_lows_slope_rolling_min_21d_base_v063_signal,
    f011hls_f011_higher_lows_slope_rolling_min_42d_base_v064_signal,
    f011hls_f011_higher_lows_slope_rolling_min_63d_base_v065_signal,
    f011hls_f011_higher_lows_slope_rolling_min_126d_base_v066_signal,
    f011hls_f011_higher_lows_slope_rolling_min_189d_base_v067_signal,
    f011hls_f011_higher_lows_slope_rolling_min_252d_base_v068_signal,
    f011hls_f011_higher_lows_slope_rolling_min_378d_base_v069_signal,
    f011hls_f011_higher_lows_slope_rolling_min_504d_base_v070_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_5d_base_v071_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_10d_base_v072_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_21d_base_v073_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_42d_base_v074_signal,
    f011hls_f011_higher_lows_slope_higher_lows_slope_63d_base_v075_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F011_HIGHER_LOWS_SLOPE_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f011_rolling_min", "_f011_higher_lows_slope", "_f011_support_rising")
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
    print(f"OK f011_higher_lows_slope_001_075_claude: {n_features} features pass")
