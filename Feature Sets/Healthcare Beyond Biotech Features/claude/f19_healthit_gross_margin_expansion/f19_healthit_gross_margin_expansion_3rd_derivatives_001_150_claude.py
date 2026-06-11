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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f19_gm_expansion(grossmargin, w):
    return grossmargin - grossmargin.shift(w)


def _f19_software_margin(grossmargin, w):
    base = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return base - 0.30


def _f19_margin_compound(grossmargin, revenue, w):
    expansion = grossmargin - grossmargin.shift(w)
    rev_growth = revenue.pct_change(periods=w)
    return expansion * rev_growth


# ===== features =====
def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v001_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v002_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v003_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v004_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v005_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v006_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v007_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v008_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v009_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v010_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v011_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v012_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v013_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v014_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v015_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v016_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v017_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v018_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v019_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v020_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v021_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v022_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v023_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v024_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * closeadj
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v025_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v026_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v027_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v028_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v029_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v030_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v031_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v032_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v033_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v034_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v035_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v036_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 21)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v037_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v038_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v039_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v040_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v041_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v042_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v043_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v044_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v045_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v046_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v047_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v048_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 63)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v049_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v050_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v051_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v052_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v053_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v054_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v055_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v056_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v057_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v058_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v059_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v060_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 21), 126)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v061_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v062_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v063_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v064_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v065_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v066_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v067_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v068_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v069_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v070_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v071_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v072_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=21, min_periods=max(1, 21 // 2)).mean()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v073_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v074_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v075_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v076_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v077_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v078_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v079_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v080_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v081_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v082_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v083_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v084_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).ewm(span=63, min_periods=max(1, 63 // 2)).mean()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v085_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v086_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v087_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v088_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v089_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v090_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v091_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v092_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v093_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v094_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v095_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v096_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v097_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v098_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v099_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v100_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v101_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v102_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v103_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v104_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v105_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v106_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v107_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v108_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21) * _f19_gm_expansion(grossmargin, 21).abs()
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v109_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v110_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v111_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v112_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v113_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v114_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v115_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v116_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v117_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v118_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v119_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v120_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 21).abs() * closeadj
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v121_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v122_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v123_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v124_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v125_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v126_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v127_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v128_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v129_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v130_signal(grossmargin):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v131_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v132_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63)
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v133_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v134_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v135_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v136_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v137_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v138_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v139_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v140_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v141_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v142_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v143_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v144_signal(grossmargin, closeadj):
    base = _f19_gm_expansion(grossmargin, 63) * closeadj
    result = _jerk(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v145_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 63), 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v146_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 63), 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v147_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 63), 21)
    result = _jerk(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v148_signal(grossmargin):
    base = _mean(_f19_gm_expansion(grossmargin, 63), 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v149_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 63), 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v150_signal(grossmargin, closeadj):
    base = _mean(_f19_gm_expansion(grossmargin, 63), 21)
    result = _jerk(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v001_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v002_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v003_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v004_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v005_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v006_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v007_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v008_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v009_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v010_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v011_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v012_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v013_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v014_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v015_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v016_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v017_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v018_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v019_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v020_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v021_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v022_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v023_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v024_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v025_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v026_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v027_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v028_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v029_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v030_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v031_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v032_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v033_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v034_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v035_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v036_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v037_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v038_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v039_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v040_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v041_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v042_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v043_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v044_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v045_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v046_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v047_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v048_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v049_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v050_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v051_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v052_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v053_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v054_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v055_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v056_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v057_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v058_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v059_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v060_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v061_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v062_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v063_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v064_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v065_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v066_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v067_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v068_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v069_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v070_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v071_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v072_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v073_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v074_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v075_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v076_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v077_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v078_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v079_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v080_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v081_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v082_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v083_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v084_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v085_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v086_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v087_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v088_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v089_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v090_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v091_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v092_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v093_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v094_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v095_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v096_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v097_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v098_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v099_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v100_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v101_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v102_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v103_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v104_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v105_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v106_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v107_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v108_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v109_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v110_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v111_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v112_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v113_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v114_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v115_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v116_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v117_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v118_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v119_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_21d_jerk_v120_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v121_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v122_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v123_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v124_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v125_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v126_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v127_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v128_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v129_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v130_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v131_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v132_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v133_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v134_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v135_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v136_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v137_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v138_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v139_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v140_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v141_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v142_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v143_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v144_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v145_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v146_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v147_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v148_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v149_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_63d_jerk_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_HEALTHIT_GROSS_MARGIN_EXPANSION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "sgna": sgna,
        "opex": opex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f19_gm_expansion', '_f19_software_margin', '_f19_margin_compound')
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
    print(f"OK f19_healthit_gross_margin_expansion_3rd_derivatives_001_150_claude: {n_features} features pass")
