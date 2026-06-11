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
def _f053_ma_fast(closeadj, w):
    return closeadj.rolling(w, min_periods=max(1, w // 2)).mean()


def _f053_ma_alignment(closeadj, w):
    w_fast = max(2, w // 4)
    w_mid = max(3, w // 2)
    w_slow = w
    fast = closeadj.rolling(w_fast, min_periods=max(1, w_fast // 2)).mean()
    mid = closeadj.rolling(w_mid, min_periods=max(1, w_mid // 2)).mean()
    slow = closeadj.rolling(w_slow, min_periods=max(1, w_slow // 2)).mean()
    return (fast - mid) / slow.replace(0, np.nan).abs() + (mid - slow) / slow.replace(0, np.nan).abs()


def _f053_stacking_score(closeadj, w):
    w_fast = max(2, w // 4)
    w_mid = max(3, w // 2)
    w_slow = w
    fast = closeadj.rolling(w_fast, min_periods=max(1, w_fast // 2)).mean()
    mid = closeadj.rolling(w_mid, min_periods=max(1, w_mid // 2)).mean()
    slow = closeadj.rolling(w_slow, min_periods=max(1, w_slow // 2)).mean()
    align = (fast - mid) / slow.replace(0, np.nan).abs() + (mid - slow) / slow.replace(0, np.nan).abs()
    return align * closeadj


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v001_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v002_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v003_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v004_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v005_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v006_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v007_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v008_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v009_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v010_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v011_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v012_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v013_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v014_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v015_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v016_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v017_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v018_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v019_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v020_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v021_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v022_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v023_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v024_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v025_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v026_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v027_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v028_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v029_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v030_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v031_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v032_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v033_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).median(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v034_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(63, min_periods=15).median(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v035_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_mean(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v036_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_std(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v037_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_z(base, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v038_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v039_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v040_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v041_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.cumsum(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v042_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v043_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v044_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v045_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).std(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v046_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_z(base, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v047_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v048_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v049_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).max(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v050_signal(closeadj):
    base = _mean(_f053_ma_fast(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).min(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v051_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v052_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v053_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v054_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v055_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v056_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v057_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v058_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v059_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v060_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v061_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v062_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v063_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v064_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v065_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v066_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v067_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v068_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v069_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v070_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v071_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v072_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v073_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v074_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v075_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v076_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v077_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v078_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v079_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v080_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v081_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v082_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v083_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).median(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v084_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(63, min_periods=15).median(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v085_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_mean(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v086_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_std(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v087_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_z(base, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v088_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v089_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v090_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v091_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.cumsum(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v092_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v093_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v094_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v095_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).std(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v096_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_z(base, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v097_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v098_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v099_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).max(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v100_signal(closeadj):
    base = _mean(_f053_ma_alignment(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).min(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v101_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v102_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v103_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v104_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v105_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v106_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v107_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v108_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v109_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v110_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v111_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v112_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v113_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v114_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v115_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v116_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v117_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v118_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v119_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v120_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v121_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v122_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v123_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v124_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v125_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v126_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v127_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v128_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v129_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v130_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v131_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v132_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v133_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).median(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v134_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(63, min_periods=15).median(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v135_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_mean(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v136_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_std(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v137_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_z(base, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v138_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v139_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v140_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v141_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.cumsum(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v142_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v143_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v144_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v145_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).std(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v146_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_z(base, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v147_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v148_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v149_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).max(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v150_signal(closeadj):
    base = _mean(_f053_stacking_score(closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).min(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v001_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v002_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v003_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v004_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v005_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v006_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v007_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v008_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v009_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_21d_jerk_v010_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v011_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v012_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v013_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v014_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v015_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v016_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v017_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v018_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v019_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_63d_jerk_v020_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v021_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v022_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v023_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v024_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v025_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v026_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v027_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v028_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v029_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_126d_jerk_v030_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v031_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v032_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v033_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v034_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v035_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v036_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v037_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v038_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v039_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_252d_jerk_v040_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v041_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v042_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v043_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v044_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v045_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v046_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v047_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v048_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v049_signal,
    f053mas_f053_ma_alignment_stacking_ma_fast_42d_jerk_v050_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v051_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v052_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v053_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v054_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v055_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v056_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v057_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v058_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v059_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_21d_jerk_v060_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v061_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v062_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v063_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v064_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v065_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v066_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v067_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v068_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v069_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_63d_jerk_v070_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v071_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v072_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v073_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v074_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v075_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v076_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v077_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v078_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v079_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_126d_jerk_v080_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v081_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v082_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v083_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v084_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v085_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v086_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v087_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v088_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v089_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_252d_jerk_v090_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v091_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v092_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v093_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v094_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v095_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v096_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v097_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v098_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v099_signal,
    f053mas_f053_ma_alignment_stacking_ma_alignment_42d_jerk_v100_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v101_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v102_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v103_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v104_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v105_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v106_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v107_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v108_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v109_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_21d_jerk_v110_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v111_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v112_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v113_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v114_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v115_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v116_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v117_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v118_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v119_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_63d_jerk_v120_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v121_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v122_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v123_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v124_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v125_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v126_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v127_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v128_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v129_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_126d_jerk_v130_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v131_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v132_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v133_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v134_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v135_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v136_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v137_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v138_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v139_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_252d_jerk_v140_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v141_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v142_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v143_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v144_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v145_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v146_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v147_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v148_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v149_signal,
    f053mas_f053_ma_alignment_stacking_stacking_score_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F053_MA_ALIGNMENT_STACKING_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f053_ma_fast', '_f053_ma_alignment', '_f053_stacking_score')
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
    print(f"OK f053_ma_alignment_stacking_3rd_derivatives_001_150_claude: {n_features} features pass")
