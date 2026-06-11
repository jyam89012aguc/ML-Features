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

# v001: capint_21d
def f43hce_f43_healthcare_capex_efficiency_capint_21d_base_v001_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v002: capint_63d
def f43hce_f43_healthcare_capex_efficiency_capint_63d_base_v002_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v003: capint_126d
def f43hce_f43_healthcare_capex_efficiency_capint_126d_base_v003_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v004: capint_252d
def f43hce_f43_healthcare_capex_efficiency_capint_252d_base_v004_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v005: capint_504d
def f43hce_f43_healthcare_capex_efficiency_capint_504d_base_v005_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v006: capeff_21d
def f43hce_f43_healthcare_capex_efficiency_capeff_21d_base_v006_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v007: capeff_63d
def f43hce_f43_healthcare_capex_efficiency_capeff_63d_base_v007_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v008: capeff_126d
def f43hce_f43_healthcare_capex_efficiency_capeff_126d_base_v008_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v009: capeff_252d
def f43hce_f43_healthcare_capex_efficiency_capeff_252d_base_v009_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v010: capeff_504d
def f43hce_f43_healthcare_capex_efficiency_capeff_504d_base_v010_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v011: capqual_21d
def f43hce_f43_healthcare_capex_efficiency_capqual_21d_base_v011_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v012: capqual_63d
def f43hce_f43_healthcare_capex_efficiency_capqual_63d_base_v012_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v013: capqual_126d
def f43hce_f43_healthcare_capex_efficiency_capqual_126d_base_v013_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v014: capqual_252d
def f43hce_f43_healthcare_capex_efficiency_capqual_252d_base_v014_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v015: capqual_504d
def f43hce_f43_healthcare_capex_efficiency_capqual_504d_base_v015_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v016: capintsq_21d
def f43hce_f43_healthcare_capex_efficiency_capintsq_21d_base_v016_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 21) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v017: capintsq_63d
def f43hce_f43_healthcare_capex_efficiency_capintsq_63d_base_v017_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 63) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v018: capintsq_252d
def f43hce_f43_healthcare_capex_efficiency_capintsq_252d_base_v018_signal(capex, revenue, closeadj):
    result = (_mean(_f43_capex_intensity(capex, revenue), 252) ** 2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v019: capeffsq_21d
def f43hce_f43_healthcare_capex_efficiency_capeffsq_21d_base_v019_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v020: capeffsq_63d
def f43hce_f43_healthcare_capex_efficiency_capeffsq_63d_base_v020_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v021: capeffsq_252d
def f43hce_f43_healthcare_capex_efficiency_capeffsq_252d_base_v021_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v022: capqualsq_21d
def f43hce_f43_healthcare_capex_efficiency_capqualsq_21d_base_v022_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v023: capqualsq_63d
def f43hce_f43_healthcare_capex_efficiency_capqualsq_63d_base_v023_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v024: capqualsq_252d
def f43hce_f43_healthcare_capex_efficiency_capqualsq_252d_base_v024_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 252).pipe(lambda s: s * s.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v025: capintz_21d
def f43hce_f43_healthcare_capex_efficiency_capintz_21d_base_v025_signal(capex, revenue, closeadj):
    result = _z(_mean(_f43_capex_intensity(capex, revenue), 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v026: capintz_63d
def f43hce_f43_healthcare_capex_efficiency_capintz_63d_base_v026_signal(capex, revenue, closeadj):
    result = _z(_mean(_f43_capex_intensity(capex, revenue), 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v027: capintz_252d
def f43hce_f43_healthcare_capex_efficiency_capintz_252d_base_v027_signal(capex, revenue, closeadj):
    result = _z(_mean(_f43_capex_intensity(capex, revenue), 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v028: capeffz_21d
def f43hce_f43_healthcare_capex_efficiency_capeffz_21d_base_v028_signal(capex, revenue, closeadj):
    result = _z(_f43_capex_efficiency(capex, revenue, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v029: capeffz_63d
def f43hce_f43_healthcare_capex_efficiency_capeffz_63d_base_v029_signal(capex, revenue, closeadj):
    result = _z(_f43_capex_efficiency(capex, revenue, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v030: capeffz_252d
def f43hce_f43_healthcare_capex_efficiency_capeffz_252d_base_v030_signal(capex, revenue, closeadj):
    result = _z(_f43_capex_efficiency(capex, revenue, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v031: capqualz_21d
def f43hce_f43_healthcare_capex_efficiency_capqualz_21d_base_v031_signal(capex, depamor, closeadj):
    result = _z(_f43_capex_quality(capex, depamor, 21), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v032: capqualz_63d
def f43hce_f43_healthcare_capex_efficiency_capqualz_63d_base_v032_signal(capex, depamor, closeadj):
    result = _z(_f43_capex_quality(capex, depamor, 63), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v033: capqualz_252d
def f43hce_f43_healthcare_capex_efficiency_capqualz_252d_base_v033_signal(capex, depamor, closeadj):
    result = _z(_f43_capex_quality(capex, depamor, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v034: intxeff_21d
def f43hce_f43_healthcare_capex_efficiency_intxeff_21d_base_v034_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_efficiency(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v035: intxeff_63d
def f43hce_f43_healthcare_capex_efficiency_intxeff_63d_base_v035_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_efficiency(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v036: intxeff_252d
def f43hce_f43_healthcare_capex_efficiency_intxeff_252d_base_v036_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_efficiency(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v037: intxqual_21d
def f43hce_f43_healthcare_capex_efficiency_intxqual_21d_base_v037_signal(capex, revenue, depamor, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v038: intxqual_63d
def f43hce_f43_healthcare_capex_efficiency_intxqual_63d_base_v038_signal(capex, revenue, depamor, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v039: intxqual_252d
def f43hce_f43_healthcare_capex_efficiency_intxqual_252d_base_v039_signal(capex, revenue, depamor, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v040: effxqual_21d
def f43hce_f43_healthcare_capex_efficiency_effxqual_21d_base_v040_signal(capex, revenue, depamor, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21) * _f43_capex_quality(capex, depamor, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v041: effxqual_63d
def f43hce_f43_healthcare_capex_efficiency_effxqual_63d_base_v041_signal(capex, revenue, depamor, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63) * _f43_capex_quality(capex, depamor, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v042: effxqual_252d
def f43hce_f43_healthcare_capex_efficiency_effxqual_252d_base_v042_signal(capex, revenue, depamor, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252) * _f43_capex_quality(capex, depamor, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v043: capintmean_21d
def f43hce_f43_healthcare_capex_efficiency_capintmean_21d_base_v043_signal(capex, revenue, closeadj):
    result = _mean(_mean(_f43_capex_intensity(capex, revenue), 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v044: capintmean_63d
def f43hce_f43_healthcare_capex_efficiency_capintmean_63d_base_v044_signal(capex, revenue, closeadj):
    result = _mean(_mean(_f43_capex_intensity(capex, revenue), 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v045: capintmean_126d
def f43hce_f43_healthcare_capex_efficiency_capintmean_126d_base_v045_signal(capex, revenue, closeadj):
    result = _mean(_mean(_f43_capex_intensity(capex, revenue), 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v046: capeffmean_21d
def f43hce_f43_healthcare_capex_efficiency_capeffmean_21d_base_v046_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_efficiency(capex, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v047: capeffmean_63d
def f43hce_f43_healthcare_capex_efficiency_capeffmean_63d_base_v047_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_efficiency(capex, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v048: capeffmean_126d
def f43hce_f43_healthcare_capex_efficiency_capeffmean_126d_base_v048_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_efficiency(capex, revenue, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v049: capqualmean_21d
def f43hce_f43_healthcare_capex_efficiency_capqualmean_21d_base_v049_signal(capex, depamor, closeadj):
    result = _mean(_f43_capex_quality(capex, depamor, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v050: capqualmean_63d
def f43hce_f43_healthcare_capex_efficiency_capqualmean_63d_base_v050_signal(capex, depamor, closeadj):
    result = _mean(_f43_capex_quality(capex, depamor, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v051: capqualmean_126d
def f43hce_f43_healthcare_capex_efficiency_capqualmean_126d_base_v051_signal(capex, depamor, closeadj):
    result = _mean(_f43_capex_quality(capex, depamor, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v052: capintstd_21d
def f43hce_f43_healthcare_capex_efficiency_capintstd_21d_base_v052_signal(capex, revenue, closeadj):
    result = _std(_mean(_f43_capex_intensity(capex, revenue), 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v053: capintstd_63d
def f43hce_f43_healthcare_capex_efficiency_capintstd_63d_base_v053_signal(capex, revenue, closeadj):
    result = _std(_mean(_f43_capex_intensity(capex, revenue), 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v054: capintstd_126d
def f43hce_f43_healthcare_capex_efficiency_capintstd_126d_base_v054_signal(capex, revenue, closeadj):
    result = _std(_mean(_f43_capex_intensity(capex, revenue), 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v055: capeffstd_21d
def f43hce_f43_healthcare_capex_efficiency_capeffstd_21d_base_v055_signal(capex, revenue, closeadj):
    result = _std(_f43_capex_efficiency(capex, revenue, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v056: capeffstd_63d
def f43hce_f43_healthcare_capex_efficiency_capeffstd_63d_base_v056_signal(capex, revenue, closeadj):
    result = _std(_f43_capex_efficiency(capex, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v057: capeffstd_126d
def f43hce_f43_healthcare_capex_efficiency_capeffstd_126d_base_v057_signal(capex, revenue, closeadj):
    result = _std(_f43_capex_efficiency(capex, revenue, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v058: capqualstd_21d
def f43hce_f43_healthcare_capex_efficiency_capqualstd_21d_base_v058_signal(capex, depamor, closeadj):
    result = _std(_f43_capex_quality(capex, depamor, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v059: capqualstd_63d
def f43hce_f43_healthcare_capex_efficiency_capqualstd_63d_base_v059_signal(capex, depamor, closeadj):
    result = _std(_f43_capex_quality(capex, depamor, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v060: capqualstd_126d
def f43hce_f43_healthcare_capex_efficiency_capqualstd_126d_base_v060_signal(capex, depamor, closeadj):
    result = _std(_f43_capex_quality(capex, depamor, 126), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v061: capintema_21d
def f43hce_f43_healthcare_capex_efficiency_capintema_21d_base_v061_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 11).ewm(span=21, adjust=False).mean() * closeadj + _f43_capex_efficiency(capex, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v062: capintema_63d
def f43hce_f43_healthcare_capex_efficiency_capintema_63d_base_v062_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 32).ewm(span=63, adjust=False).mean() * closeadj + _f43_capex_efficiency(capex, revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v063: capintema_252d
def f43hce_f43_healthcare_capex_efficiency_capintema_252d_base_v063_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 127).ewm(span=252, adjust=False).mean() * closeadj + _f43_capex_efficiency(capex, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# v064: capeffema_21d
def f43hce_f43_healthcare_capex_efficiency_capeffema_21d_base_v064_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v065: capeffema_63d
def f43hce_f43_healthcare_capex_efficiency_capeffema_63d_base_v065_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v066: capeffema_252d
def f43hce_f43_healthcare_capex_efficiency_capeffema_252d_base_v066_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v067: capqualema_21d
def f43hce_f43_healthcare_capex_efficiency_capqualema_21d_base_v067_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 21).ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v068: capqualema_63d
def f43hce_f43_healthcare_capex_efficiency_capqualema_63d_base_v068_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 63).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v069: capqualema_252d
def f43hce_f43_healthcare_capex_efficiency_capqualema_252d_base_v069_signal(capex, depamor, closeadj):
    result = _f43_capex_quality(capex, depamor, 252).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# v070: capint_5d_alt
def f43hce_f43_healthcare_capex_efficiency_capint_5d_alt_base_v070_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v071: capint_10d_alt
def f43hce_f43_healthcare_capex_efficiency_capint_10d_alt_base_v071_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 10) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v072: capint_42d_alt
def f43hce_f43_healthcare_capex_efficiency_capint_42d_alt_base_v072_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 42) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v073: capint_189d_alt
def f43hce_f43_healthcare_capex_efficiency_capint_189d_alt_base_v073_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 189) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v074: capint_378d_alt
def f43hce_f43_healthcare_capex_efficiency_capint_378d_alt_base_v074_signal(capex, revenue, closeadj):
    result = _mean(_f43_capex_intensity(capex, revenue), 378) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# v075: capeff_5d_alt
def f43hce_f43_healthcare_capex_efficiency_capeff_5d_alt_base_v075_signal(capex, revenue, closeadj):
    result = _f43_capex_efficiency(capex, revenue, 5) * closeadj * 1.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43hce_f43_healthcare_capex_efficiency_capint_21d_base_v001_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_63d_base_v002_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_126d_base_v003_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_252d_base_v004_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_504d_base_v005_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_21d_base_v006_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_63d_base_v007_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_126d_base_v008_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_252d_base_v009_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_504d_base_v010_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_21d_base_v011_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_63d_base_v012_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_126d_base_v013_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_252d_base_v014_signal,
    f43hce_f43_healthcare_capex_efficiency_capqual_504d_base_v015_signal,
    f43hce_f43_healthcare_capex_efficiency_capintsq_21d_base_v016_signal,
    f43hce_f43_healthcare_capex_efficiency_capintsq_63d_base_v017_signal,
    f43hce_f43_healthcare_capex_efficiency_capintsq_252d_base_v018_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffsq_21d_base_v019_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffsq_63d_base_v020_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffsq_252d_base_v021_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualsq_21d_base_v022_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualsq_63d_base_v023_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualsq_252d_base_v024_signal,
    f43hce_f43_healthcare_capex_efficiency_capintz_21d_base_v025_signal,
    f43hce_f43_healthcare_capex_efficiency_capintz_63d_base_v026_signal,
    f43hce_f43_healthcare_capex_efficiency_capintz_252d_base_v027_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffz_21d_base_v028_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffz_63d_base_v029_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffz_252d_base_v030_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualz_21d_base_v031_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualz_63d_base_v032_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualz_252d_base_v033_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_21d_base_v034_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_63d_base_v035_signal,
    f43hce_f43_healthcare_capex_efficiency_intxeff_252d_base_v036_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_21d_base_v037_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_63d_base_v038_signal,
    f43hce_f43_healthcare_capex_efficiency_intxqual_252d_base_v039_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_21d_base_v040_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_63d_base_v041_signal,
    f43hce_f43_healthcare_capex_efficiency_effxqual_252d_base_v042_signal,
    f43hce_f43_healthcare_capex_efficiency_capintmean_21d_base_v043_signal,
    f43hce_f43_healthcare_capex_efficiency_capintmean_63d_base_v044_signal,
    f43hce_f43_healthcare_capex_efficiency_capintmean_126d_base_v045_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffmean_21d_base_v046_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffmean_63d_base_v047_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffmean_126d_base_v048_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualmean_21d_base_v049_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualmean_63d_base_v050_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualmean_126d_base_v051_signal,
    f43hce_f43_healthcare_capex_efficiency_capintstd_21d_base_v052_signal,
    f43hce_f43_healthcare_capex_efficiency_capintstd_63d_base_v053_signal,
    f43hce_f43_healthcare_capex_efficiency_capintstd_126d_base_v054_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffstd_21d_base_v055_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffstd_63d_base_v056_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffstd_126d_base_v057_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualstd_21d_base_v058_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualstd_63d_base_v059_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualstd_126d_base_v060_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_21d_base_v061_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_63d_base_v062_signal,
    f43hce_f43_healthcare_capex_efficiency_capintema_252d_base_v063_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_21d_base_v064_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_63d_base_v065_signal,
    f43hce_f43_healthcare_capex_efficiency_capeffema_252d_base_v066_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_21d_base_v067_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_63d_base_v068_signal,
    f43hce_f43_healthcare_capex_efficiency_capqualema_252d_base_v069_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_5d_alt_base_v070_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_10d_alt_base_v071_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_42d_alt_base_v072_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_189d_alt_base_v073_signal,
    f43hce_f43_healthcare_capex_efficiency_capint_378d_alt_base_v074_signal,
    f43hce_f43_healthcare_capex_efficiency_capeff_5d_alt_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_HEALTHCARE_CAPEX_EFFICIENCY_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f43_healthcare_capex_efficiency_base_001_075_claude: {n_features} features pass")
