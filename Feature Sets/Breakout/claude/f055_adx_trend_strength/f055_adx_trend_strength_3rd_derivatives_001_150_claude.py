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
def _f055_dm_plus(high, low, w):
    up = high.diff()
    dn = -low.diff()
    dmp = ((up > dn) & (up > 0)).astype(float) * up
    return dmp.rolling(w, min_periods=max(1, w // 2)).mean()


def _f055_dm_minus(high, low, w):
    up = high.diff()
    dn = -low.diff()
    dmn = ((dn > up) & (dn > 0)).astype(float) * dn
    return dmn.rolling(w, min_periods=max(1, w // 2)).mean()


def _f055_adx(high, low, closeadj, w):
    up = high.diff()
    dn = -low.diff()
    dmp = ((up > dn) & (up > 0)).astype(float) * up
    dmn = ((dn > up) & (dn > 0)).astype(float) * dn
    tr = (high - low).abs()
    atr = tr.rolling(w, min_periods=max(1, w // 2)).mean()
    dip = dmp.rolling(w, min_periods=max(1, w // 2)).mean() / atr.replace(0, np.nan)
    din = dmn.rolling(w, min_periods=max(1, w // 2)).mean() / atr.replace(0, np.nan)
    dx = (dip - din).abs() / (dip + din).replace(0, np.nan)
    return dx.rolling(w, min_periods=max(1, w // 2)).mean() * closeadj


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v001_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v002_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v003_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v004_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v005_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v006_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v007_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v008_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v009_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v010_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v011_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v012_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v013_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v014_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v015_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v016_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v017_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v018_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v019_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v020_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v021_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v022_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v023_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v024_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v025_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v026_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v027_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v028_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v029_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v030_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v031_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v032_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v033_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).median(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v034_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(63, min_periods=15).median(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v035_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_mean(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v036_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_std(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v037_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_z(base, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v038_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v039_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v040_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v041_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.cumsum(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v042_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v043_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v044_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v045_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).std(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v046_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_z(base, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v047_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v048_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v049_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).max(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v050_signal(high, low, closeadj):
    base = _mean(_f055_dm_plus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).min(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v051_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v052_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v053_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v054_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v055_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v056_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v057_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v058_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v059_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v060_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v061_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v062_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v063_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v064_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v065_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v066_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v067_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v068_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v069_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v070_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v071_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v072_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v073_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v074_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v075_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v076_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v077_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v078_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v079_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v080_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v081_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v082_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v083_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).median(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v084_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(63, min_periods=15).median(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v085_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_mean(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v086_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_std(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v087_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_z(base, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v088_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v089_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v090_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v091_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.cumsum(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v092_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v093_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v094_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v095_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).std(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v096_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_z(base, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v097_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v098_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v099_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).max(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v100_signal(high, low, closeadj):
    base = _mean(_f055_dm_minus(high, low, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).min(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v101_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v102_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v103_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v104_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v105_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v106_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v107_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v108_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v109_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_21d_jerk_v110_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v111_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v112_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v113_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v114_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v115_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v116_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v117_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v118_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v119_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_63d_jerk_v120_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(np.log1p(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v121_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v122_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(np.sqrt(base.abs()), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v123_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v124_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v125_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v126_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v127_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v128_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v129_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_126d_jerk_v130_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 10), 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v131_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v132_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v133_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).median(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v134_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.rolling(63, min_periods=15).median(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v135_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_mean(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v136_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_std(base, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v137_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(_z(base, 42), 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v138_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v139_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base.diff(63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_252d_jerk_v140_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base * closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v141_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.cumsum(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v142_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v143_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base, 126), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v144_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v145_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).std(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v146_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_z(base, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v147_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v148_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(_std(base.abs(), 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v149_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).max(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f055ats_f055_adx_trend_strength_adx_42d_jerk_v150_signal(high, low, closeadj):
    base = _mean(_f055_adx(high, low, closeadj, 42), max(2, 42 // 4)) * closeadj
    result = _jerk(base.rolling(21, min_periods=5).min(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v001_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v002_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v003_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v004_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v005_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v006_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v007_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v008_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v009_signal,
    f055ats_f055_adx_trend_strength_dm_plus_21d_jerk_v010_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v011_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v012_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v013_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v014_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v015_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v016_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v017_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v018_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v019_signal,
    f055ats_f055_adx_trend_strength_dm_plus_63d_jerk_v020_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v021_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v022_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v023_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v024_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v025_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v026_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v027_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v028_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v029_signal,
    f055ats_f055_adx_trend_strength_dm_plus_126d_jerk_v030_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v031_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v032_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v033_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v034_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v035_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v036_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v037_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v038_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v039_signal,
    f055ats_f055_adx_trend_strength_dm_plus_252d_jerk_v040_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v041_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v042_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v043_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v044_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v045_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v046_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v047_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v048_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v049_signal,
    f055ats_f055_adx_trend_strength_dm_plus_42d_jerk_v050_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v051_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v052_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v053_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v054_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v055_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v056_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v057_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v058_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v059_signal,
    f055ats_f055_adx_trend_strength_dm_minus_21d_jerk_v060_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v061_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v062_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v063_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v064_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v065_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v066_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v067_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v068_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v069_signal,
    f055ats_f055_adx_trend_strength_dm_minus_63d_jerk_v070_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v071_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v072_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v073_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v074_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v075_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v076_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v077_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v078_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v079_signal,
    f055ats_f055_adx_trend_strength_dm_minus_126d_jerk_v080_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v081_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v082_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v083_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v084_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v085_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v086_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v087_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v088_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v089_signal,
    f055ats_f055_adx_trend_strength_dm_minus_252d_jerk_v090_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v091_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v092_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v093_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v094_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v095_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v096_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v097_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v098_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v099_signal,
    f055ats_f055_adx_trend_strength_dm_minus_42d_jerk_v100_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v101_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v102_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v103_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v104_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v105_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v106_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v107_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v108_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v109_signal,
    f055ats_f055_adx_trend_strength_adx_21d_jerk_v110_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v111_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v112_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v113_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v114_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v115_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v116_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v117_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v118_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v119_signal,
    f055ats_f055_adx_trend_strength_adx_63d_jerk_v120_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v121_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v122_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v123_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v124_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v125_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v126_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v127_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v128_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v129_signal,
    f055ats_f055_adx_trend_strength_adx_126d_jerk_v130_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v131_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v132_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v133_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v134_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v135_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v136_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v137_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v138_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v139_signal,
    f055ats_f055_adx_trend_strength_adx_252d_jerk_v140_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v141_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v142_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v143_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v144_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v145_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v146_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v147_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v148_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v149_signal,
    f055ats_f055_adx_trend_strength_adx_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F055_ADX_TREND_STRENGTH_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = pd.Series(closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    cols = {"closeadj": closeadj, "high": high, "low": low}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f055_dm_plus', '_f055_dm_minus', '_f055_adx')
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
    print(f"OK f055_adx_trend_strength_3rd_derivatives_001_150_claude: {n_features} features pass")
