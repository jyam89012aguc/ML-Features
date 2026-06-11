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
def _f078_margin_diff(em, w):
    return em.diff(w)

def _f078_margin_acceleration(em, w):
    d1 = em.diff(w)
    return d1.diff(w)

def _f078_inflection_strength(em, gm, w):
    em_a = em.diff(w).diff(w)
    gm_a = gm.diff(w).diff(w)
    return em_a + gm_a


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v001_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v002_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v003_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v004_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v005_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v006_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v007_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v008_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v009_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v010_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v011_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v012_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v013_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v014_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v015_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v016_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v017_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v018_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v019_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v020_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v021_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v022_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v023_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v024_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v025_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v026_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v027_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v028_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v029_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v030_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v031_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v032_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v033_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v034_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v035_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v036_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v037_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v038_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v039_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v040_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v041_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v042_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v043_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v044_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v045_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v046_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v047_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v048_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v049_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v050_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_diff(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v051_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v052_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v053_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v054_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v055_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v056_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v057_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v058_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v059_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v060_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v061_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v062_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v063_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v064_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v065_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v066_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v067_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v068_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v069_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v070_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v071_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v072_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v073_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v074_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v075_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v076_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v077_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v078_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v079_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v080_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v081_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v082_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v083_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v084_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v085_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v086_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v087_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v088_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v089_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v090_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v091_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v092_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v093_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v094_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v095_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v096_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v097_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v098_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v099_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v100_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_margin_acceleration(ebitdamargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v101_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v102_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v103_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v104_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v105_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v106_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v107_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v108_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v109_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=21, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v110_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v111_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v112_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v113_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_z(base, 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v114_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_std(base, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v115_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 21 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v116_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v117_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v118_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v119_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 21), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v120_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v121_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v122_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v123_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v124_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v125_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v126_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v127_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v128_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v129_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=63, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v130_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v131_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base * closeadj, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v132_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v133_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_z(base, 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v134_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_std(base, 63), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v135_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.ewm(span=max(2, 63 // 2), adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v136_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.abs(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v137_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v138_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v139_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(_mean(base.abs(), 63), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v140_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base.cumsum(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v141_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v142_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v143_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v144_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base * closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v145_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v146_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_mean(base, 126), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v147_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(_std(base, 126), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v148_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v149_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.ewm(span=126, adjust=False).mean(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v150_signal(ebitdamargin, grossmargin, closeadj):
    base = _mean(_f078_inflection_strength(ebitdamargin, grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base.abs(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v001_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v002_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v003_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v004_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v005_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v006_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v007_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v008_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v009_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v010_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v011_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v012_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v013_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v014_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v015_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v016_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v017_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v018_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v019_signal,
    f078mac_f078_margin_acceleration_margin_diff_21d_jerk_v020_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v021_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v022_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v023_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v024_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v025_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v026_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v027_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v028_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v029_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v030_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v031_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v032_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v033_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v034_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v035_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v036_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v037_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v038_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v039_signal,
    f078mac_f078_margin_acceleration_margin_diff_63d_jerk_v040_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v041_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v042_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v043_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v044_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v045_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v046_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v047_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v048_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v049_signal,
    f078mac_f078_margin_acceleration_margin_diff_126d_jerk_v050_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v051_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v052_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v053_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v054_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v055_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v056_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v057_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v058_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v059_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v060_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v061_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v062_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v063_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v064_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v065_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v066_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v067_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v068_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v069_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_21d_jerk_v070_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v071_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v072_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v073_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v074_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v075_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v076_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v077_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v078_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v079_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v080_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v081_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v082_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v083_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v084_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v085_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v086_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v087_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v088_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v089_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_63d_jerk_v090_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v091_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v092_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v093_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v094_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v095_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v096_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v097_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v098_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v099_signal,
    f078mac_f078_margin_acceleration_margin_acceleration_126d_jerk_v100_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v101_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v102_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v103_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v104_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v105_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v106_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v107_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v108_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v109_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v110_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v111_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v112_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v113_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v114_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v115_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v116_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v117_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v118_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v119_signal,
    f078mac_f078_margin_acceleration_inflection_strength_21d_jerk_v120_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v121_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v122_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v123_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v124_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v125_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v126_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v127_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v128_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v129_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v130_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v131_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v132_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v133_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v134_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v135_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v136_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v137_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v138_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v139_signal,
    f078mac_f078_margin_acceleration_inflection_strength_63d_jerk_v140_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v141_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v142_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v143_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v144_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v145_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v146_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v147_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v148_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v149_signal,
    f078mac_f078_margin_acceleration_inflection_strength_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F078_MARGIN_ACCELERATION_REGISTRY_JERK_001_150 = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f078_margin_acceleration_3rd_derivatives_001_150_claude: {n_features} features pass")
