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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

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


def f079rct_f079_roic_trend_roic_slope_21d_slope_v001_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v002_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v003_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v004_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v005_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v006_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v007_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v008_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v009_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v010_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v011_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v012_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v013_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v014_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v015_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v016_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v017_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v018_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v019_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_21d_slope_v020_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v021_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v022_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v023_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v024_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v025_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v026_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v027_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v028_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v029_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v030_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v031_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v032_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v033_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v034_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v035_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v036_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v037_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v038_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v039_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_63d_slope_v040_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v041_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v042_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v043_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v044_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v045_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v046_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v047_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v048_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v049_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_slope_126d_slope_v050_signal(roic, closeadj):
    base = _mean(_f079_roic_slope(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v051_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v052_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v053_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v054_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v055_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v056_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v057_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v058_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v059_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v060_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v061_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v062_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v063_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v064_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v065_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v066_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v067_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v068_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v069_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_21d_slope_v070_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v071_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v072_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v073_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v074_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v075_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v076_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v077_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v078_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v079_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v080_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v081_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v082_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v083_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v084_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v085_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v086_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v087_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v088_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v089_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_63d_slope_v090_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v091_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v092_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v093_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v094_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v095_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v096_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v097_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v098_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v099_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_roic_improvement_126d_slope_v100_signal(roic, closeadj):
    base = _mean(_f079_roic_improvement(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v101_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v102_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v103_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v104_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v105_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v106_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v107_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v108_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v109_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v110_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v111_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v112_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v113_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v114_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v115_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v116_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v117_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v118_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v119_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_21d_slope_v120_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v121_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v122_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v123_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v124_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v125_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v126_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v127_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v128_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v129_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v130_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v131_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v132_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v133_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v134_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v135_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v136_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v137_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v138_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v139_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_63d_slope_v140_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v141_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v142_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v143_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v144_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v145_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v146_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v147_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v148_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v149_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f079rct_f079_roic_trend_value_creation_126d_slope_v150_signal(roic, closeadj):
    base = _mean(_f079_value_creation(roic, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f079rct_f079_roic_trend_roic_slope_21d_slope_v001_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v002_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v003_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v004_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v005_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v006_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v007_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v008_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v009_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v010_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v011_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v012_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v013_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v014_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v015_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v016_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v017_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v018_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v019_signal,
    f079rct_f079_roic_trend_roic_slope_21d_slope_v020_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v021_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v022_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v023_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v024_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v025_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v026_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v027_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v028_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v029_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v030_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v031_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v032_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v033_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v034_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v035_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v036_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v037_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v038_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v039_signal,
    f079rct_f079_roic_trend_roic_slope_63d_slope_v040_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v041_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v042_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v043_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v044_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v045_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v046_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v047_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v048_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v049_signal,
    f079rct_f079_roic_trend_roic_slope_126d_slope_v050_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v051_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v052_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v053_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v054_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v055_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v056_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v057_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v058_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v059_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v060_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v061_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v062_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v063_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v064_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v065_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v066_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v067_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v068_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v069_signal,
    f079rct_f079_roic_trend_roic_improvement_21d_slope_v070_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v071_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v072_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v073_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v074_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v075_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v076_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v077_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v078_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v079_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v080_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v081_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v082_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v083_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v084_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v085_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v086_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v087_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v088_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v089_signal,
    f079rct_f079_roic_trend_roic_improvement_63d_slope_v090_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v091_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v092_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v093_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v094_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v095_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v096_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v097_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v098_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v099_signal,
    f079rct_f079_roic_trend_roic_improvement_126d_slope_v100_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v101_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v102_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v103_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v104_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v105_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v106_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v107_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v108_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v109_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v110_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v111_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v112_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v113_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v114_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v115_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v116_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v117_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v118_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v119_signal,
    f079rct_f079_roic_trend_value_creation_21d_slope_v120_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v121_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v122_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v123_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v124_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v125_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v126_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v127_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v128_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v129_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v130_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v131_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v132_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v133_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v134_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v135_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v136_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v137_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v138_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v139_signal,
    f079rct_f079_roic_trend_value_creation_63d_slope_v140_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v141_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v142_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v143_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v144_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v145_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v146_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v147_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v148_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v149_signal,
    f079rct_f079_roic_trend_value_creation_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F079_ROIC_TREND_REGISTRY_SLOPE_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f079_roic_trend_2nd_derivatives_001_150_claude: {n_features} features pass")
