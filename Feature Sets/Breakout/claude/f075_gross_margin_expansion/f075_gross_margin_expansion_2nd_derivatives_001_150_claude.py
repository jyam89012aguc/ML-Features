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
def _f075_gm_yoy(grossmargin, w):
    return grossmargin.diff(periods=w) * grossmargin


def _f075_gm_expansion(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (grossmargin - avg) * grossmargin


def _f075_pricing_power(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (grossmargin - avg) / sd.replace(0, np.nan) * grossmargin

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v001_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v002_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v003_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 5) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v004_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v005_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v006_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v007_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v008_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v009_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v010_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v011_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v012_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v013_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 21) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v014_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v015_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v016_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v017_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v018_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v019_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v020_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v021_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v022_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v023_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 63) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v024_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v025_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v026_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v027_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v028_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v029_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v030_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v031_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v032_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v033_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 126) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v034_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v035_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v036_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v037_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v038_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v039_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v040_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v041_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v042_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v043_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 252) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v044_signal(grossmargin, closeadj):
    base = _f075_gm_yoy(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v045_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v046_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v047_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v048_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v049_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v050_signal(grossmargin, closeadj):
    base = _std(_f075_gm_yoy(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v051_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v052_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v053_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 5) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v054_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v055_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v056_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v057_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v058_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v059_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v060_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v061_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v062_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v063_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 21) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v064_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v065_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v066_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v067_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v068_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v069_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v070_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v071_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v072_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v073_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 63) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v074_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v075_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v076_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v077_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v078_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v079_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v080_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v081_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v082_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v083_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 126) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v084_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v085_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v086_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v087_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v088_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v089_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v090_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v091_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v092_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v093_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 252) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v094_signal(grossmargin, closeadj):
    base = _f075_gm_expansion(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v095_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v096_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v097_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v098_signal(grossmargin, closeadj):
    base = _mean(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v099_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v100_signal(grossmargin, closeadj):
    base = _std(_f075_gm_expansion(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v101_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v102_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v103_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 5) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v104_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 5) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v105_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v106_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v107_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v108_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v109_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v110_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 5), max(2, 5 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v111_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v112_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v113_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 21) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v114_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v115_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v116_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v117_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v118_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v119_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v120_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 21), max(2, 21 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v121_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v122_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v123_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 63) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v124_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v125_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v126_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v127_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v128_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v129_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v130_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 63), max(2, 63 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v131_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v132_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v133_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 126) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v134_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v135_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v136_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v137_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v138_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v139_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v140_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 126), max(2, 126 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v141_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v142_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v143_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 252) * closeadj
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v144_signal(grossmargin, closeadj):
    base = _f075_pricing_power(grossmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v145_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v146_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v147_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v148_signal(grossmargin, closeadj):
    base = _mean(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v149_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v150_signal(grossmargin, closeadj):
    base = _std(_f075_pricing_power(grossmargin, 252), max(2, 252 // 4)) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v001_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v002_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v003_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v004_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v005_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v006_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v007_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v008_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v009_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_slope_v010_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v011_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v012_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v013_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v014_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v015_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v016_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v017_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v018_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v019_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_slope_v020_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v021_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v022_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v023_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v024_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v025_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v026_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v027_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v028_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v029_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_slope_v030_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v031_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v032_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v033_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v034_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v035_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v036_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v037_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v038_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v039_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_slope_v040_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v041_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v042_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v043_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v044_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v045_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v046_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v047_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v048_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v049_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_slope_v050_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v051_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v052_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v053_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v054_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v055_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v056_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v057_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v058_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v059_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_slope_v060_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v061_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v062_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v063_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v064_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v065_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v066_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v067_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v068_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v069_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_slope_v070_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v071_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v072_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v073_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v074_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v075_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v076_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v077_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v078_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v079_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_slope_v080_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v081_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v082_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v083_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v084_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v085_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v086_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v087_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v088_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v089_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_slope_v090_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v091_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v092_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v093_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v094_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v095_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v096_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v097_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v098_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v099_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_slope_v100_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v101_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v102_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v103_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v104_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v105_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v106_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v107_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v108_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v109_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_slope_v110_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v111_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v112_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v113_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v114_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v115_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v116_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v117_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v118_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v119_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_slope_v120_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v121_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v122_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v123_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v124_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v125_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v126_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v127_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v128_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v129_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_slope_v130_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v131_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v132_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v133_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v134_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v135_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v136_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v137_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v138_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v139_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_slope_v140_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v141_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v142_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v143_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v144_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v145_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v146_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v147_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v148_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v149_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F075_GROSS_MARGIN_EXPANSION_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f075_gross_margin_expansion_slope_001_150_claude: {n_features} features pass")
