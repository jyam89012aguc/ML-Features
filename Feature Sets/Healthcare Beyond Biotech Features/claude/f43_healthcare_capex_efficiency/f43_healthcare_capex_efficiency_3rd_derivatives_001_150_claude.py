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
def _f43_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f43_capex_efficiency(capex, revenue, w):
    rev_chg = revenue.diff(periods=w)
    cap_avg = _mean(capex, w)
    return rev_chg / cap_avg.replace(0, np.nan)


def _f43_capex_quality(capex, depamor, w):
    cap_avg = _mean(capex, w)
    dep_avg = _mean(depamor, w)
    return (cap_avg - dep_avg) / dep_avg.replace(0, np.nan)

# v001: jerk window 5 of capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_jerk_v001_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: jerk window 21 of capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_jerk_v002_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: jerk window 63 of capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_jerk_v003_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: jerk window 5 of capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_jerk_v004_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: jerk window 21 of capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_jerk_v005_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: jerk window 63 of capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_jerk_v006_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: jerk window 5 of capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_jerk_v007_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: jerk window 21 of capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_jerk_v008_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: jerk window 63 of capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_jerk_v009_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: jerk window 5 of capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_jerk_v010_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: jerk window 21 of capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_jerk_v011_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: jerk window 63 of capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_jerk_v012_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: jerk window 5 of capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_jerk_v013_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: jerk window 21 of capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_jerk_v014_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: jerk window 63 of capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_jerk_v015_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: jerk window 5 of capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_jerk_v016_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: jerk window 21 of capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_jerk_v017_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: jerk window 63 of capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_jerk_v018_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: jerk window 5 of capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_jerk_v019_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: jerk window 21 of capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_jerk_v020_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: jerk window 63 of capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_jerk_v021_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: jerk window 5 of capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_jerk_v022_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: jerk window 21 of capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_jerk_v023_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: jerk window 63 of capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_jerk_v024_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: jerk window 5 of capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_jerk_v025_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: jerk window 21 of capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_jerk_v026_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: jerk window 63 of capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_jerk_v027_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: jerk window 5 of capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_jerk_v028_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: jerk window 21 of capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_jerk_v029_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: jerk window 63 of capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_jerk_v030_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: jerk window 5 of capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_jerk_v031_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: jerk window 21 of capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_jerk_v032_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: jerk window 63 of capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_jerk_v033_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: jerk window 5 of capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_jerk_v034_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: jerk window 21 of capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_jerk_v035_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: jerk window 63 of capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_jerk_v036_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: jerk window 5 of capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_jerk_v037_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: jerk window 21 of capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_jerk_v038_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: jerk window 63 of capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_jerk_v039_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: jerk window 5 of capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_jerk_v040_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: jerk window 21 of capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_jerk_v041_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: jerk window 63 of capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_jerk_v042_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: jerk window 5 of capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_jerk_v043_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: jerk window 21 of capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_jerk_v044_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: jerk window 63 of capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_jerk_v045_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: jerk window 5 of intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_jerk_v046_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: jerk window 21 of intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_jerk_v047_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: jerk window 63 of intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_jerk_v048_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: jerk window 5 of intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_jerk_v049_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: jerk window 21 of intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_jerk_v050_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: jerk window 63 of intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_jerk_v051_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: jerk window 5 of intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_jerk_v052_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: jerk window 21 of intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_jerk_v053_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: jerk window 63 of intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_jerk_v054_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: jerk window 5 of intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_jerk_v055_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: jerk window 21 of intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_jerk_v056_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: jerk window 63 of intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_jerk_v057_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: jerk window 5 of intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_jerk_v058_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: jerk window 21 of intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_jerk_v059_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: jerk window 63 of intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_jerk_v060_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: jerk window 5 of intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_jerk_v061_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: jerk window 21 of intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_jerk_v062_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: jerk window 63 of intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_jerk_v063_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: jerk window 5 of effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_jerk_v064_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: jerk window 21 of effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_jerk_v065_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: jerk window 63 of effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_jerk_v066_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: jerk window 5 of effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_jerk_v067_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: jerk window 21 of effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_jerk_v068_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: jerk window 63 of effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_jerk_v069_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: jerk window 5 of effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_jerk_v070_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: jerk window 21 of effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_jerk_v071_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: jerk window 63 of effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_jerk_v072_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: jerk window 5 of capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_jerk_v073_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 5).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: jerk window 21 of capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_jerk_v074_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 5).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: jerk window 63 of capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_jerk_v075_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 5).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: jerk window 5 of capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_jerk_v076_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 15).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: jerk window 21 of capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_jerk_v077_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 15).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: jerk window 63 of capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_jerk_v078_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 15).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: jerk window 5 of capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_jerk_v079_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: jerk window 21 of capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_jerk_v080_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: jerk window 63 of capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_jerk_v081_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: jerk window 5 of capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_jerk_v082_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: jerk window 21 of capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_jerk_v083_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: jerk window 63 of capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_jerk_v084_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: jerk window 5 of capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_jerk_v085_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: jerk window 21 of capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_jerk_v086_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: jerk window 63 of capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_jerk_v087_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: jerk window 5 of capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_jerk_v088_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: jerk window 21 of capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_jerk_v089_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: jerk window 63 of capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_jerk_v090_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: jerk window 5 of capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_jerk_v091_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: jerk window 21 of capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_jerk_v092_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: jerk window 63 of capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_jerk_v093_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: jerk window 5 of capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_jerk_v094_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: jerk window 21 of capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_jerk_v095_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: jerk window 63 of capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_jerk_v096_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: jerk window 5 of capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_jerk_v097_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: jerk window 21 of capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_jerk_v098_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: jerk window 63 of capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_jerk_v099_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: jerk window 5 of capintcum_21d
def f43hce_f43_healthcare_capex_efficiency_capintcum_21d_jerk_v100_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: jerk window 21 of capintcum_21d
def f43hce_f43_healthcare_capex_efficiency_capintcum_21d_jerk_v101_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: jerk window 63 of capintcum_21d
def f43hce_f43_healthcare_capex_efficiency_capintcum_21d_jerk_v102_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: jerk window 5 of capintcum_63d
def f43hce_f43_healthcare_capex_efficiency_capintcum_63d_jerk_v103_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: jerk window 21 of capintcum_63d
def f43hce_f43_healthcare_capex_efficiency_capintcum_63d_jerk_v104_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: jerk window 63 of capintcum_63d
def f43hce_f43_healthcare_capex_efficiency_capintcum_63d_jerk_v105_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: jerk window 5 of capintcum_126d
def f43hce_f43_healthcare_capex_efficiency_capintcum_126d_jerk_v106_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: jerk window 21 of capintcum_126d
def f43hce_f43_healthcare_capex_efficiency_capintcum_126d_jerk_v107_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: jerk window 63 of capintcum_126d
def f43hce_f43_healthcare_capex_efficiency_capintcum_126d_jerk_v108_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: jerk window 5 of capeffcum_21d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_jerk_v109_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: jerk window 21 of capeffcum_21d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_jerk_v110_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: jerk window 63 of capeffcum_21d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_jerk_v111_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: jerk window 5 of capeffcum_63d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_jerk_v112_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: jerk window 21 of capeffcum_63d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_jerk_v113_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: jerk window 63 of capeffcum_63d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_jerk_v114_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: jerk window 5 of capeffcum_126d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_jerk_v115_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: jerk window 21 of capeffcum_126d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_jerk_v116_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: jerk window 63 of capeffcum_126d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_jerk_v117_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: jerk window 5 of capqualcum_21d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_jerk_v118_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: jerk window 21 of capqualcum_21d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_jerk_v119_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: jerk window 63 of capqualcum_21d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_jerk_v120_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: jerk window 5 of capqualcum_63d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_jerk_v121_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: jerk window 21 of capqualcum_63d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_jerk_v122_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: jerk window 63 of capqualcum_63d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_jerk_v123_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: jerk window 5 of capqualcum_126d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_jerk_v124_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: jerk window 21 of capqualcum_126d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_jerk_v125_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: jerk window 63 of capqualcum_126d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_jerk_v126_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: jerk window 5 of composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_jerk_v127_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: jerk window 21 of composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_jerk_v128_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: jerk window 63 of composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_jerk_v129_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: jerk window 5 of composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_jerk_v130_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: jerk window 21 of composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_jerk_v131_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: jerk window 63 of composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_jerk_v132_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: jerk window 5 of capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_jerk_v133_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _mean(revenue, 21) * closeadj / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: jerk window 21 of capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_jerk_v134_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _mean(revenue, 21) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: jerk window 63 of capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_jerk_v135_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _mean(revenue, 21) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: jerk window 5 of capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_jerk_v136_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _mean(revenue, 63) * closeadj / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: jerk window 21 of capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_jerk_v137_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _mean(revenue, 63) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: jerk window 63 of capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_jerk_v138_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _mean(revenue, 63) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: jerk window 5 of capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_jerk_v139_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _mean(revenue, 252) * closeadj / 1e9
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: jerk window 21 of capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_jerk_v140_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _mean(revenue, 252) * closeadj / 1e9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: jerk window 63 of capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_jerk_v141_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _mean(revenue, 252) * closeadj / 1e9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: jerk window 5 of capqualxcap_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_jerk_v142_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: jerk window 21 of capqualxcap_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_jerk_v143_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: jerk window 63 of capqualxcap_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_jerk_v144_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: jerk window 5 of capqualxcap_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_jerk_v145_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: jerk window 21 of capqualxcap_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_jerk_v146_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: jerk window 63 of capqualxcap_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_jerk_v147_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: jerk window 5 of capqualxcap_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_jerk_v148_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: jerk window 21 of capqualxcap_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_jerk_v149_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: jerk window 63 of capqualxcap_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_jerk_v150_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43hce_f43_healthcare_capex_efficiency_capint_21d_jerk_v001_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_21d_jerk_v002_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_21d_jerk_v003_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_jerk_v004_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_jerk_v005_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_jerk_v006_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_jerk_v007_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_jerk_v008_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_jerk_v009_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_jerk_v010_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_jerk_v011_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_jerk_v012_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_jerk_v013_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_jerk_v014_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_jerk_v015_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_jerk_v016_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_jerk_v017_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_jerk_v018_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_jerk_v019_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_jerk_v020_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_jerk_v021_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_jerk_v022_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_jerk_v023_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_jerk_v024_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_jerk_v025_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_jerk_v026_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_jerk_v027_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_jerk_v028_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_jerk_v029_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_jerk_v030_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_jerk_v031_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_jerk_v032_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_jerk_v033_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_jerk_v034_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_jerk_v035_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_jerk_v036_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_jerk_v037_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_jerk_v038_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_jerk_v039_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_jerk_v040_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_jerk_v041_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_jerk_v042_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_jerk_v043_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_jerk_v044_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_jerk_v045_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_jerk_v046_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_jerk_v047_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_jerk_v048_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_jerk_v049_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_jerk_v050_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_jerk_v051_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_jerk_v052_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_jerk_v053_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_jerk_v054_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_jerk_v055_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_jerk_v056_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_jerk_v057_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_jerk_v058_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_jerk_v059_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_jerk_v060_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_jerk_v061_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_jerk_v062_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_jerk_v063_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_jerk_v064_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_jerk_v065_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_jerk_v066_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_jerk_v067_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_jerk_v068_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_jerk_v069_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_jerk_v070_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_jerk_v071_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_jerk_v072_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_jerk_v073_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_jerk_v074_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_jerk_v075_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_jerk_v076_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_jerk_v077_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_jerk_v078_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_jerk_v079_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_jerk_v080_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_jerk_v081_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_jerk_v082_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_jerk_v083_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_jerk_v084_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_jerk_v085_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_jerk_v086_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_jerk_v087_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_jerk_v088_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_jerk_v089_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_jerk_v090_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_jerk_v091_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_jerk_v092_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_jerk_v093_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_jerk_v094_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_jerk_v095_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_jerk_v096_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_jerk_v097_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_jerk_v098_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_jerk_v099_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_21d_jerk_v100_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_21d_jerk_v101_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_21d_jerk_v102_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_63d_jerk_v103_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_63d_jerk_v104_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_63d_jerk_v105_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_126d_jerk_v106_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_126d_jerk_v107_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_126d_jerk_v108_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_jerk_v109_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_jerk_v110_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_jerk_v111_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_jerk_v112_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_jerk_v113_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_jerk_v114_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_jerk_v115_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_jerk_v116_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_jerk_v117_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_jerk_v118_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_jerk_v119_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_jerk_v120_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_jerk_v121_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_jerk_v122_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_jerk_v123_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_jerk_v124_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_jerk_v125_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_jerk_v126_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_jerk_v127_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_jerk_v128_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_jerk_v129_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_jerk_v130_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_jerk_v131_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_jerk_v132_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_jerk_v133_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_jerk_v134_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_jerk_v135_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_jerk_v136_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_jerk_v137_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_jerk_v138_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_jerk_v139_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_jerk_v140_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_jerk_v141_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_jerk_v142_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_jerk_v143_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_jerk_v144_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_jerk_v145_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_jerk_v146_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_jerk_v147_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_jerk_v148_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_jerk_v149_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_HEALTHCARE_CAPEX_EFFICIENCY_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")

    cols = {
        "capex": capex,
        "closeadj": closeadj,
        "depamor": depamor,
        "revenue": revenue,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f43_capex_intensity', '_f43_capex_efficiency', '_f43_capex_quality',)
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
    print(f"OK f43_healthcare_capex_efficiency_3rd_derivatives_001_150_claude: {n_features} features pass")
