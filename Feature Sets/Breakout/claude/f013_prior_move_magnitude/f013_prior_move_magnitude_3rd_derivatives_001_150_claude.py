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
def _f013_recent_range(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / lo.replace(0, np.nan).abs()


def _f013_prior_move(close, w):
    return close.pct_change(periods=w)


def _f013_move_magnitude(close, w):
    pm = close.pct_change(periods=w)
    return pm.abs() * close


def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v001_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v002_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v003_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v004_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v005_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v006_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v007_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v008_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v009_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v010_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v011_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v012_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v013_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v014_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v015_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v016_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v017_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v018_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v019_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v020_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v021_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v022_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v023_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v024_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v025_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v026_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v027_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v028_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v029_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v030_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v031_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v032_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v033_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v034_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v035_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v036_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v037_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v038_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v039_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v040_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v041_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v042_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v043_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v044_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v045_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v046_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v047_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v048_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v049_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v050_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v051_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v052_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v053_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v054_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v055_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v056_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v057_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v058_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v059_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v060_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v061_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v062_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v063_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v064_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v065_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v066_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v067_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v068_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v069_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v070_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v071_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v072_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v073_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v074_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v075_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v076_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v077_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v078_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v079_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v080_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v081_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v082_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v083_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v084_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v085_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v086_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v087_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v088_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v089_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v090_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v091_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v092_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v093_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v094_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v095_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v096_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v097_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v098_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v099_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v100_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v101_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v102_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v103_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v104_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v105_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v106_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v107_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v108_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v109_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v110_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v111_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v112_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v113_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v114_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v115_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v116_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v117_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v118_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v119_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v120_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v121_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v122_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v123_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v124_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v125_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v126_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v127_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v128_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v129_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v130_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v131_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v132_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v133_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v134_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v135_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 63)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v136_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v137_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v138_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 126)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v139_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v140_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v141_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 189)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v142_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v143_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v144_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 252)) * np.log(closeadj.replace(0, np.nan)), 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v145_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v146_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v147_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 21)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v148_signal(closeadj):
    result = _jerk((_f013_recent_range(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v149_signal(closeadj):
    result = _jerk((_f013_prior_move(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v150_signal(closeadj):
    result = _jerk((_f013_move_magnitude(closeadj, 42)) * np.log(closeadj.replace(0, np.nan)), 42)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v001_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v002_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v003_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v004_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v005_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v006_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v007_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v008_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v009_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v010_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v011_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v012_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v013_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v014_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v015_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v016_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v017_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v018_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v019_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v020_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v021_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v022_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v023_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v024_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v025_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v026_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v027_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v028_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v029_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v030_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v031_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v032_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v033_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v034_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v035_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v036_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v037_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v038_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v039_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v040_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v041_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v042_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v043_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v044_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v045_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v046_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v047_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v048_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v049_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v050_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v051_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v052_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v053_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v054_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v055_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v056_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v057_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v058_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v059_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v060_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v061_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v062_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v063_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v064_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v065_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v066_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v067_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v068_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v069_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v070_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v071_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v072_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v073_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v074_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v075_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v076_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v077_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v078_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v079_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v080_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v081_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v082_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v083_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v084_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v085_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v086_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v087_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v088_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v089_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v090_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v091_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v092_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v093_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v094_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v095_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v096_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v097_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v098_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v099_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v100_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v101_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v102_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v103_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v104_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v105_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v106_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v107_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v108_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v109_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v110_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v111_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v112_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v113_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v114_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v115_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v116_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v117_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v118_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v119_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v120_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v121_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v122_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v123_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v124_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v125_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v126_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v127_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v128_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v129_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v130_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v131_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v132_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_63d_jerk_v133_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_63d_jerk_v134_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_63d_jerk_v135_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_126d_jerk_v136_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_126d_jerk_v137_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_126d_jerk_v138_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_189d_jerk_v139_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_189d_jerk_v140_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_189d_jerk_v141_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_252d_jerk_v142_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_252d_jerk_v143_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_252d_jerk_v144_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_21d_jerk_v145_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_21d_jerk_v146_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_21d_jerk_v147_signal,
    f013pmm_f013_prior_move_magnitude_recent_range_42d_jerk_v148_signal,
    f013pmm_f013_prior_move_magnitude_prior_move_42d_jerk_v149_signal,
    f013pmm_f013_prior_move_magnitude_move_magnitude_42d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F013_PRIOR_MOVE_MAGNITUDE_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f013_recent_range", "_f013_prior_move", "_f013_move_magnitude")
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
    print(f"OK f013_prior_move_magnitude_jerk_001_150_claude: {n_features} features pass")
