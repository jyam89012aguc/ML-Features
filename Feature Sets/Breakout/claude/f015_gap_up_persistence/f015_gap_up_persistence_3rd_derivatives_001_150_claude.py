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
def _f015_gap_proxy(close, w):
    ret = close.pct_change(periods=1)
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    return ret / sd.replace(0, np.nan)


def _f015_gap_persistence(close, volume, w):
    ret = close.pct_change(periods=1)
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    gap_z = ret / sd.replace(0, np.nan)
    pos_gap = gap_z.clip(lower=0)
    vlz = volume / volume.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    return (pos_gap * vlz).rolling(w, min_periods=max(1, w // 2)).sum()


def _f015_conviction_gap(close, volume, w):
    ret = close.pct_change(periods=1)
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    gap_z = ret / sd.replace(0, np.nan)
    pos_gap = gap_z.clip(lower=0)
    vlz = volume / volume.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)
    smoothed = (pos_gap * vlz).rolling(w, min_periods=max(1, w // 2)).mean()
    return smoothed * close


def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v001_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v002_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v003_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v004_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v005_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v006_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v007_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v008_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v009_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v010_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v011_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v012_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v013_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v014_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v015_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v016_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v017_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v018_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v019_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v020_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v021_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v022_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v023_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v024_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v025_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v026_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v027_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v028_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v029_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v030_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v031_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v032_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v033_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v034_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v035_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v036_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v037_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v038_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v039_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v040_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v041_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v042_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v043_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v044_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v045_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v046_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v047_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v048_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v049_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v050_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v051_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v052_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v053_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v054_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v055_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v056_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v057_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v058_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v059_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v060_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v061_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v062_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v063_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v064_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v065_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v066_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v067_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v068_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v069_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v070_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v071_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v072_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v073_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v074_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v075_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v076_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v077_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v078_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v079_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v080_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v081_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v082_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v083_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v084_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v085_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v086_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v087_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v088_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v089_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v090_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v091_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v092_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v093_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v094_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v095_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v096_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v097_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v098_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v099_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v100_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v101_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v102_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v103_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v104_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v105_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v106_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v107_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v108_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v109_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v110_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v111_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v112_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v113_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v114_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v115_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v116_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v117_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v118_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v119_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v120_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v121_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v122_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v123_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v124_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v125_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v126_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v127_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v128_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v129_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v130_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v131_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v132_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v133_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v134_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v135_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 63)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v136_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v137_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 126)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v138_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 126)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v139_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v140_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 189)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v141_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 189)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v142_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v143_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 252)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v144_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 252)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v145_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v146_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v147_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 21)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v148_signal(closeadj):
    result = _jerk((_f015_gap_proxy(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v149_signal(closeadj, volume):
    result = _jerk((_f015_gap_persistence(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v150_signal(closeadj, volume):
    result = _jerk((_f015_conviction_gap(closeadj, volume, 42)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v001_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v002_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v003_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v004_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v005_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v006_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v007_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v008_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v009_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v010_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v011_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v012_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v013_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v014_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v015_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v016_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v017_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v018_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v019_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v020_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v021_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v022_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v023_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v024_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v025_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v026_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v027_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v028_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v029_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v030_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v031_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v032_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v033_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v034_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v035_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v036_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v037_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v038_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v039_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v040_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v041_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v042_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v043_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v044_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v045_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v046_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v047_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v048_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v049_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v050_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v051_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v052_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v053_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v054_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v055_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v056_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v057_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v058_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v059_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v060_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v061_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v062_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v063_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v064_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v065_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v066_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v067_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v068_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v069_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v070_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v071_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v072_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v073_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v074_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v075_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v076_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v077_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v078_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v079_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v080_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v081_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v082_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v083_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v084_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v085_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v086_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v087_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v088_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v089_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v090_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v091_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v092_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v093_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v094_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v095_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v096_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v097_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v098_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v099_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v100_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v101_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v102_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v103_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v104_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v105_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v106_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v107_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v108_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v109_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v110_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v111_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v112_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v113_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v114_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v115_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v116_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v117_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v118_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v119_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v120_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v121_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v122_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v123_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v124_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v125_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v126_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v127_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v128_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v129_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v130_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v131_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v132_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_63d_jerk_v133_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_63d_jerk_v134_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_63d_jerk_v135_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_126d_jerk_v136_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_126d_jerk_v137_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_126d_jerk_v138_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_189d_jerk_v139_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_189d_jerk_v140_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_189d_jerk_v141_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_252d_jerk_v142_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_252d_jerk_v143_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_252d_jerk_v144_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_21d_jerk_v145_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_21d_jerk_v146_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_21d_jerk_v147_signal,
    f015gup_f015_gap_up_persistence_gap_proxy_42d_jerk_v148_signal,
    f015gup_f015_gap_up_persistence_gap_persistence_42d_jerk_v149_signal,
    f015gup_f015_gap_up_persistence_conviction_gap_42d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F015_GAP_UP_PERSISTENCE_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    cols = {
        "closeadj": closeadj,
        "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f015_gap_proxy", "_f015_gap_persistence", "_f015_conviction_gap")
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
    print(f"OK f015_gap_up_persistence_jerk_001_150_claude: {n_features} features pass")
