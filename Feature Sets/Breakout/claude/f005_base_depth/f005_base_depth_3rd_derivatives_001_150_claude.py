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


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f005_base_range(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / hi.replace(0, np.nan).abs()


def _f005_base_depth(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / lo.replace(0, np.nan).abs()


def _f005_base_tightness(close, w):
    m = close.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = close.rolling(w, min_periods=max(1, w // 2)).std()
    return sd / m.replace(0, np.nan).abs()


def f005bdp_f005_base_depth_base_range_21d_jerk_v001_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v002_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v003_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v004_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v005_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v006_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v007_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v008_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v009_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v010_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v011_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v012_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v013_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v014_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_slope(base, 21), max(2, 21 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v015_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v016_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v017_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v018_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v019_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, max(2, 5 // 2)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_21d_jerk_v020_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, max(2, 21 // 2)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v021_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v022_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v023_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v024_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v025_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v026_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v027_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v028_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v029_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v030_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v031_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v032_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v033_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v034_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_slope(base, 21), max(2, 21 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v035_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v036_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v037_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v038_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v039_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, max(2, 5 // 2)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_63d_jerk_v040_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, max(2, 63 // 2)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v041_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v042_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v043_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v044_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v045_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v046_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v047_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v048_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v049_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_range_126d_jerk_v050_signal(closeadj):
    base = _mean(_f005_base_range(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v051_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v052_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v053_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v054_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v055_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v056_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v057_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v058_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v059_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v060_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v061_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v062_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v063_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v064_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_slope(base, 21), max(2, 21 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v065_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v066_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v067_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v068_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v069_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, max(2, 5 // 2)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_21d_jerk_v070_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, max(2, 21 // 2)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v071_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v072_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v073_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v074_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v075_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v076_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v077_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v078_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v079_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v080_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v081_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v082_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v083_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v084_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_slope(base, 21), max(2, 21 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v085_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v086_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v087_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v088_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v089_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, max(2, 5 // 2)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_63d_jerk_v090_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, max(2, 63 // 2)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v091_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v092_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v093_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v094_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v095_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v096_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v097_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v098_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v099_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_depth_126d_jerk_v100_signal(closeadj):
    base = _mean(_f005_base_depth(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v101_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v102_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v103_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v104_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v105_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v106_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v107_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v108_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v109_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v110_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v111_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v112_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v113_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v114_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_slope(base, 21), max(2, 21 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v115_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v116_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v117_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v118_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v119_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, max(2, 5 // 2)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_21d_jerk_v120_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, max(2, 21 // 2)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v121_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v122_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v123_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v124_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v125_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v126_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v127_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v128_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v129_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v130_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v131_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v132_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v133_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v134_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_slope(base, 21), max(2, 21 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v135_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v136_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * np.sqrt(closeadj.abs())
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v137_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v138_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63).rolling(63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v139_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, max(2, 5 // 2)) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_63d_jerk_v140_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, max(2, 63 // 2)), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v141_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v142_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v143_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v144_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v145_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v146_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v147_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_slope(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v148_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v149_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f005bdp_f005_base_depth_base_tightness_126d_jerk_v150_signal(closeadj):
    base = _mean(_f005_base_tightness(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f005bdp_f005_base_depth_base_range_21d_jerk_v001_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v002_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v003_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v004_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v005_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v006_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v007_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v008_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v009_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v010_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v011_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v012_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v013_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v014_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v015_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v016_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v017_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v018_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v019_signal,
    f005bdp_f005_base_depth_base_range_21d_jerk_v020_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v021_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v022_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v023_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v024_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v025_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v026_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v027_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v028_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v029_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v030_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v031_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v032_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v033_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v034_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v035_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v036_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v037_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v038_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v039_signal,
    f005bdp_f005_base_depth_base_range_63d_jerk_v040_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v041_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v042_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v043_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v044_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v045_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v046_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v047_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v048_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v049_signal,
    f005bdp_f005_base_depth_base_range_126d_jerk_v050_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v051_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v052_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v053_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v054_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v055_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v056_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v057_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v058_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v059_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v060_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v061_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v062_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v063_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v064_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v065_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v066_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v067_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v068_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v069_signal,
    f005bdp_f005_base_depth_base_depth_21d_jerk_v070_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v071_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v072_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v073_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v074_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v075_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v076_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v077_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v078_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v079_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v080_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v081_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v082_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v083_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v084_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v085_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v086_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v087_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v088_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v089_signal,
    f005bdp_f005_base_depth_base_depth_63d_jerk_v090_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v091_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v092_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v093_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v094_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v095_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v096_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v097_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v098_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v099_signal,
    f005bdp_f005_base_depth_base_depth_126d_jerk_v100_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v101_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v102_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v103_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v104_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v105_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v106_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v107_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v108_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v109_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v110_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v111_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v112_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v113_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v114_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v115_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v116_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v117_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v118_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v119_signal,
    f005bdp_f005_base_depth_base_tightness_21d_jerk_v120_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v121_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v122_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v123_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v124_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v125_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v126_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v127_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v128_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v129_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v130_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v131_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v132_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v133_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v134_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v135_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v136_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v137_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v138_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v139_signal,
    f005bdp_f005_base_depth_base_tightness_63d_jerk_v140_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v141_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v142_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v143_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v144_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v145_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v146_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v147_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v148_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v149_signal,
    f005bdp_f005_base_depth_base_tightness_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F005_BASE_DEPTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f005_base_range", "_f005_base_depth", "_f005_base_tightness")
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
    print(f"OK f005_base_depth_3rd_derivatives_001_150_claude: {n_features} features pass")
