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
def _f075_gm_yoy(grossmargin, w):
    return grossmargin.diff(periods=w) * grossmargin


def _f075_gm_expansion(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (grossmargin - avg) * grossmargin


def _f075_pricing_power(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (grossmargin - avg) / sd.replace(0, np.nan) * grossmargin

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v001_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v002_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v003_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v004_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v005_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v006_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v007_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v008_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v009_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v010_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v011_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v012_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v013_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v014_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v015_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v016_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v017_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v018_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v019_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v020_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v021_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v022_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v023_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v024_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v025_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v026_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v027_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v028_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v029_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v030_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v031_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v032_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v033_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v034_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v035_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v036_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v037_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v038_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v039_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v040_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v041_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v042_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v043_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v044_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v045_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v046_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v047_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v048_signal(grossmargin, closeadj):
    base = (_f075_gm_yoy(grossmargin, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v049_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v050_signal(grossmargin, closeadj):
    base = _z(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v051_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v052_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v053_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v054_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v055_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v056_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v057_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v058_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v059_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v060_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v061_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v062_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v063_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v064_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v065_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v066_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v067_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v068_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v069_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v070_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v071_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v072_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v073_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v074_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v075_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v076_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v077_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v078_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v079_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v080_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v081_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v082_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v083_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v084_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v085_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v086_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v087_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v088_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v089_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v090_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v091_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v092_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v093_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v094_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v095_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v096_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v097_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v098_signal(grossmargin, closeadj):
    base = (_f075_gm_expansion(grossmargin, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v099_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v100_signal(grossmargin, closeadj):
    base = _z(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v101_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v102_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 5) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v103_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v104_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v105_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v106_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v107_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v108_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 5)).ewm(span=max(2, 5 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v109_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v110_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v111_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v112_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v113_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v114_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v115_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v116_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v117_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v118_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v119_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v120_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v121_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v122_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v123_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v124_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v125_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v126_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v127_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v128_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 63)).ewm(span=max(2, 63 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v129_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v130_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v131_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v132_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 126) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v133_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v134_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v135_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v136_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v137_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v138_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 126)).ewm(span=max(2, 126 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v139_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v140_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v141_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v142_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 252) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v143_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v144_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v145_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v146_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v147_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v148_signal(grossmargin, closeadj):
    base = (_f075_pricing_power(grossmargin, 252)).ewm(span=max(2, 252 // 2), adjust=False).mean() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v149_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v150_signal(grossmargin, closeadj):
    base = _z(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v001_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v002_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v003_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v004_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v005_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v006_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v007_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v008_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v009_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_jerk_v010_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v011_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v012_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v013_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v014_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v015_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v016_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v017_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v018_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v019_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_jerk_v020_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v021_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v022_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v023_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v024_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v025_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v026_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v027_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v028_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v029_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_jerk_v030_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v031_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v032_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v033_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v034_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v035_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v036_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v037_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v038_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v039_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_jerk_v040_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v041_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v042_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v043_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v044_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v045_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v046_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v047_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v048_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v049_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_jerk_v050_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v051_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v052_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v053_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v054_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v055_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v056_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v057_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v058_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v059_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_jerk_v060_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v061_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v062_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v063_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v064_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v065_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v066_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v067_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v068_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v069_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_jerk_v070_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v071_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v072_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v073_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v074_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v075_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v076_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v077_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v078_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v079_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_jerk_v080_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v081_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v082_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v083_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v084_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v085_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v086_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v087_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v088_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v089_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_jerk_v090_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v091_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v092_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v093_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v094_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v095_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v096_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v097_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v098_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v099_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_jerk_v100_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v101_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v102_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v103_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v104_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v105_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v106_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v107_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v108_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v109_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_jerk_v110_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v111_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v112_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v113_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v114_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v115_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v116_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v117_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v118_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v119_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_jerk_v120_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v121_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v122_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v123_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v124_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v125_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v126_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v127_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v128_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v129_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_jerk_v130_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v131_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v132_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v133_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v134_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v135_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v136_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v137_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v138_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v139_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_jerk_v140_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v141_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v142_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v143_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v144_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v145_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v146_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v147_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v148_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v149_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F075_GROSS_MARGIN_EXPANSION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    cols = {"grossmargin": grossmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f075_gm_yoy", "_f075_gm_expansion", "_f075_pricing_power")
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
    print(f"OK f075_gross_margin_expansion_jerk_001_150_claude: {n_features} features pass")
