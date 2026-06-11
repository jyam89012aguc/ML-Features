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

# v001: _slope_pct window 5 of capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_slope_v001_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v002: _slope_diff_norm window 21 of capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_slope_v002_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v003: _diff window 63 of capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_slope_v003_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v004: _slope_pct window 5 of capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_slope_v004_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v005: _slope_diff_norm window 21 of capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_slope_v005_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v006: _diff window 63 of capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_slope_v006_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v007: _slope_pct window 5 of capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_slope_v007_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v008: _slope_diff_norm window 21 of capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_slope_v008_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v009: _diff window 63 of capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_slope_v009_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v010: _slope_pct window 5 of capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_slope_v010_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v011: _slope_diff_norm window 21 of capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_slope_v011_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v012: _diff window 63 of capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_slope_v012_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v013: _slope_pct window 5 of capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_slope_v013_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v014: _slope_diff_norm window 21 of capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_slope_v014_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v015: _diff window 63 of capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_slope_v015_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v016: _slope_pct window 5 of capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_slope_v016_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v017: _slope_diff_norm window 21 of capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_slope_v017_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v018: _diff window 63 of capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_slope_v018_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v019: _slope_pct window 5 of capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_slope_v019_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v020: _slope_diff_norm window 21 of capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_slope_v020_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v021: _diff window 63 of capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_slope_v021_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v022: _slope_pct window 5 of capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_slope_v022_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v023: _slope_diff_norm window 21 of capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_slope_v023_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v024: _diff window 63 of capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_slope_v024_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v025: _slope_pct window 5 of capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_slope_v025_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v026: _slope_diff_norm window 21 of capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_slope_v026_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v027: _diff window 63 of capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_slope_v027_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v028: _slope_pct window 5 of capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_slope_v028_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v029: _slope_diff_norm window 21 of capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_slope_v029_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v030: _diff window 63 of capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_slope_v030_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v031: _slope_pct window 5 of capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_slope_v031_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v032: _slope_diff_norm window 21 of capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_slope_v032_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v033: _diff window 63 of capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_slope_v033_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v034: _slope_pct window 5 of capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_slope_v034_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v035: _slope_diff_norm window 21 of capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_slope_v035_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v036: _diff window 63 of capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_slope_v036_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v037: _slope_pct window 5 of capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_slope_v037_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v038: _slope_diff_norm window 21 of capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_slope_v038_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v039: _diff window 63 of capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_slope_v039_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v040: _slope_pct window 5 of capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_slope_v040_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v041: _slope_diff_norm window 21 of capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_slope_v041_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v042: _diff window 63 of capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_slope_v042_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v043: _slope_pct window 5 of capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_slope_v043_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v044: _slope_diff_norm window 21 of capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_slope_v044_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v045: _diff window 63 of capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_slope_v045_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v046: _slope_pct window 5 of intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_slope_v046_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v047: _slope_diff_norm window 21 of intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_slope_v047_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v048: _diff window 63 of intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_slope_v048_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v049: _slope_pct window 5 of intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_slope_v049_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v050: _slope_diff_norm window 21 of intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_slope_v050_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v051: _diff window 63 of intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_slope_v051_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v052: _slope_pct window 5 of intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_slope_v052_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v053: _slope_diff_norm window 21 of intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_slope_v053_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v054: _diff window 63 of intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_slope_v054_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v055: _slope_pct window 5 of intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_slope_v055_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v056: _slope_diff_norm window 21 of intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_slope_v056_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v057: _diff window 63 of intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_slope_v057_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v058: _slope_pct window 5 of intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_slope_v058_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v059: _slope_diff_norm window 21 of intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_slope_v059_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v060: _diff window 63 of intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_slope_v060_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v061: _slope_pct window 5 of intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_slope_v061_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v062: _slope_diff_norm window 21 of intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_slope_v062_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v063: _diff window 63 of intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_slope_v063_signal(capex, revenue, depamor, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v064: _slope_pct window 5 of effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_slope_v064_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v065: _slope_diff_norm window 21 of effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_slope_v065_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v066: _diff window 63 of effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_slope_v066_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v067: _slope_pct window 5 of effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_slope_v067_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v068: _slope_diff_norm window 21 of effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_slope_v068_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v069: _diff window 63 of effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_slope_v069_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v070: _slope_pct window 5 of effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_slope_v070_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v071: _slope_diff_norm window 21 of effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_slope_v071_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v072: _diff window 63 of effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_slope_v072_signal(capex, revenue, depamor, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v073: _slope_pct window 5 of capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_slope_v073_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 5).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v074: _slope_diff_norm window 21 of capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_slope_v074_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 5).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v075: _diff window 63 of capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_slope_v075_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 5).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v076: _slope_pct window 5 of capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_slope_v076_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 15).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v077: _slope_diff_norm window 21 of capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_slope_v077_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 15).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v078: _diff window 63 of capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_slope_v078_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 15).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v079: _slope_pct window 5 of capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_slope_v079_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v080: _slope_diff_norm window 21 of capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_slope_v080_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v081: _diff window 63 of capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_slope_v081_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v082: _slope_pct window 5 of capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_slope_v082_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v083: _slope_diff_norm window 21 of capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_slope_v083_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v084: _diff window 63 of capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_slope_v084_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v085: _slope_pct window 5 of capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_slope_v085_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v086: _slope_diff_norm window 21 of capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_slope_v086_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v087: _diff window 63 of capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_slope_v087_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v088: _slope_pct window 5 of capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_slope_v088_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v089: _slope_diff_norm window 21 of capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_slope_v089_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v090: _diff window 63 of capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_slope_v090_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v091: _slope_pct window 5 of capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_slope_v091_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v092: _slope_diff_norm window 21 of capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_slope_v092_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v093: _diff window 63 of capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_slope_v093_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v094: _slope_pct window 5 of capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_slope_v094_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v095: _slope_diff_norm window 21 of capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_slope_v095_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v096: _diff window 63 of capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_slope_v096_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v097: _slope_pct window 5 of capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_slope_v097_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v098: _slope_diff_norm window 21 of capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_slope_v098_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v099: _diff window 63 of capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_slope_v099_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v100: _slope_pct window 5 of capintcum_21d
def f43hce_f43_healthcare_capex_efficiency_capintcum_21d_slope_v100_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v101: _slope_diff_norm window 21 of capintcum_21d
def f43hce_f43_healthcare_capex_efficiency_capintcum_21d_slope_v101_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v102: _diff window 63 of capintcum_21d
def f43hce_f43_healthcare_capex_efficiency_capintcum_21d_slope_v102_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v103: _slope_pct window 5 of capintcum_63d
def f43hce_f43_healthcare_capex_efficiency_capintcum_63d_slope_v103_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v104: _slope_diff_norm window 21 of capintcum_63d
def f43hce_f43_healthcare_capex_efficiency_capintcum_63d_slope_v104_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v105: _diff window 63 of capintcum_63d
def f43hce_f43_healthcare_capex_efficiency_capintcum_63d_slope_v105_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v106: _slope_pct window 5 of capintcum_126d
def f43hce_f43_healthcare_capex_efficiency_capintcum_126d_slope_v106_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v107: _slope_diff_norm window 21 of capintcum_126d
def f43hce_f43_healthcare_capex_efficiency_capintcum_126d_slope_v107_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v108: _diff window 63 of capintcum_126d
def f43hce_f43_healthcare_capex_efficiency_capintcum_126d_slope_v108_signal(capex, revenue, closeadj):
    base = _mean(_f43_capex_intensity(capex, revenue), 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v109: _slope_pct window 5 of capeffcum_21d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_slope_v109_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v110: _slope_diff_norm window 21 of capeffcum_21d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_slope_v110_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v111: _diff window 63 of capeffcum_21d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_slope_v111_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v112: _slope_pct window 5 of capeffcum_63d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_slope_v112_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v113: _slope_diff_norm window 21 of capeffcum_63d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_slope_v113_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v114: _diff window 63 of capeffcum_63d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_slope_v114_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v115: _slope_pct window 5 of capeffcum_126d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_slope_v115_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v116: _slope_diff_norm window 21 of capeffcum_126d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_slope_v116_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v117: _diff window 63 of capeffcum_126d
def f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_slope_v117_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v118: _slope_pct window 5 of capqualcum_21d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_slope_v118_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v119: _slope_diff_norm window 21 of capqualcum_21d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_slope_v119_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v120: _diff window 63 of capqualcum_21d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_slope_v120_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21).rolling(63, min_periods=21).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v121: _slope_pct window 5 of capqualcum_63d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_slope_v121_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v122: _slope_diff_norm window 21 of capqualcum_63d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_slope_v122_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v123: _diff window 63 of capqualcum_63d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_slope_v123_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v124: _slope_pct window 5 of capqualcum_126d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_slope_v124_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v125: _slope_diff_norm window 21 of capqualcum_126d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_slope_v125_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v126: _diff window 63 of capqualcum_126d
def f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_slope_v126_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 126).rolling(252, min_periods=84).sum() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v127: _slope_pct window 5 of composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_slope_v127_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v128: _slope_diff_norm window 21 of composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_slope_v128_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v129: _diff window 63 of composite_63d
def f43hce_f43_healthcare_capex_efficiency_composite_63d_slope_v129_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 63), 252) + _z(_f43_capex_efficiency(capex, revenue, 63), 252) + _z(_f43_capex_quality(capex, depamor, 63), 252)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v130: _slope_pct window 5 of composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_slope_v130_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v131: _slope_diff_norm window 21 of composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_slope_v131_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v132: _diff window 63 of composite_252d
def f43hce_f43_healthcare_capex_efficiency_composite_252d_slope_v132_signal(capex, revenue, depamor, closeadj):
    base = (_z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) + _z(_f43_capex_efficiency(capex, revenue, 252), 504) + _z(_f43_capex_quality(capex, depamor, 252), 504)) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v133: _slope_pct window 5 of capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_slope_v133_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _mean(revenue, 21) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v134: _slope_diff_norm window 21 of capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_slope_v134_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _mean(revenue, 21) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v135: _diff window 63 of capeffxrev_21d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_slope_v135_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 21) * _mean(revenue, 21) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v136: _slope_pct window 5 of capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_slope_v136_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _mean(revenue, 63) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v137: _slope_diff_norm window 21 of capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_slope_v137_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _mean(revenue, 63) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v138: _diff window 63 of capeffxrev_63d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_slope_v138_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 63) * _mean(revenue, 63) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v139: _slope_pct window 5 of capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_slope_v139_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _mean(revenue, 252) * closeadj / 1e9
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v140: _slope_diff_norm window 21 of capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_slope_v140_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _mean(revenue, 252) * closeadj / 1e9
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v141: _diff window 63 of capeffxrev_252d
def f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_slope_v141_signal(capex, revenue, closeadj):
    base = _f43_capex_efficiency(capex, revenue, 252) * _mean(revenue, 252) * closeadj / 1e9
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v142: _slope_pct window 5 of capqualxcap_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_slope_v142_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v143: _slope_diff_norm window 21 of capqualxcap_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_slope_v143_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v144: _diff window 63 of capqualxcap_21d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_slope_v144_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 21) * _mean(capex, 21) * closeadj / 1e8
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v145: _slope_pct window 5 of capqualxcap_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_slope_v145_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v146: _slope_diff_norm window 21 of capqualxcap_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_slope_v146_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v147: _diff window 63 of capqualxcap_63d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_slope_v147_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 63) * _mean(capex, 63) * closeadj / 1e8
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# v148: _slope_pct window 5 of capqualxcap_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_slope_v148_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# v149: _slope_diff_norm window 21 of capqualxcap_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_slope_v149_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# v150: _diff window 63 of capqualxcap_252d
def f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_slope_v150_signal(capex, depamor, closeadj):
    base = _f43_capex_quality(capex, depamor, 252) * _mean(capex, 252) * closeadj / 1e8
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43hce_f43_healthcare_capex_efficiency_capint_21d_slope_v001_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_21d_slope_v002_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_21d_slope_v003_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_slope_v004_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_slope_v005_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_slope_v006_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_slope_v007_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_slope_v008_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_slope_v009_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_slope_v010_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_slope_v011_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_slope_v012_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_slope_v013_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_slope_v014_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_slope_v015_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_slope_v016_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_slope_v017_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_slope_v018_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_slope_v019_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_slope_v020_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_slope_v021_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_slope_v022_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_slope_v023_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_slope_v024_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_slope_v025_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_slope_v026_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_slope_v027_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_slope_v028_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_slope_v029_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_slope_v030_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_slope_v031_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_slope_v032_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_slope_v033_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_slope_v034_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_slope_v035_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_slope_v036_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_slope_v037_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_slope_v038_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_slope_v039_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_slope_v040_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_slope_v041_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_slope_v042_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_slope_v043_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_slope_v044_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_slope_v045_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_slope_v046_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_slope_v047_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_slope_v048_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_slope_v049_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_slope_v050_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_slope_v051_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_slope_v052_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_slope_v053_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_slope_v054_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_slope_v055_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_slope_v056_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_slope_v057_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_slope_v058_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_slope_v059_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_slope_v060_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_slope_v061_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_slope_v062_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_slope_v063_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_slope_v064_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_slope_v065_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_slope_v066_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_slope_v067_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_slope_v068_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_slope_v069_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_slope_v070_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_slope_v071_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_slope_v072_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_slope_v073_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_slope_v074_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_slope_v075_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_slope_v076_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_slope_v077_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_slope_v078_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_slope_v079_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_slope_v080_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_slope_v081_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_slope_v082_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_slope_v083_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_slope_v084_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_slope_v085_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_slope_v086_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_slope_v087_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_slope_v088_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_slope_v089_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_slope_v090_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_slope_v091_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_slope_v092_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_slope_v093_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_slope_v094_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_slope_v095_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_slope_v096_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_slope_v097_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_slope_v098_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_slope_v099_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_21d_slope_v100_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_21d_slope_v101_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_21d_slope_v102_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_63d_slope_v103_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_63d_slope_v104_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_63d_slope_v105_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_126d_slope_v106_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_126d_slope_v107_signal,
    f43hce_f43_healthcare_capex_efficiency_capintcum_126d_slope_v108_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_slope_v109_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_slope_v110_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_21d_slope_v111_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_slope_v112_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_slope_v113_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_63d_slope_v114_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_slope_v115_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_slope_v116_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffcum_126d_slope_v117_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_slope_v118_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_slope_v119_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_21d_slope_v120_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_slope_v121_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_slope_v122_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_63d_slope_v123_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_slope_v124_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_slope_v125_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualcum_126d_slope_v126_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_slope_v127_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_slope_v128_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_63d_slope_v129_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_slope_v130_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_slope_v131_signal,
    f43hce_f43_healthcare_capex_efficiency_composite_252d_slope_v132_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_slope_v133_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_slope_v134_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_21d_slope_v135_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_slope_v136_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_slope_v137_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_63d_slope_v138_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_slope_v139_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_slope_v140_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffxrev_252d_slope_v141_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_slope_v142_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_slope_v143_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_21d_slope_v144_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_slope_v145_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_slope_v146_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_63d_slope_v147_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_slope_v148_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_slope_v149_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualxcap_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_HEALTHCARE_CAPEX_EFFICIENCY_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK f43_healthcare_capex_efficiency_2nd_derivatives_001_150_claude: {n_features} features pass")
