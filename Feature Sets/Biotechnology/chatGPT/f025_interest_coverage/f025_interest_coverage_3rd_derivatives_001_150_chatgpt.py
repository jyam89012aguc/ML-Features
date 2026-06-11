"""Family f025 - Interest coverage and stress (Capital Structure) | Sharadar tables: SF1 | fields: intexp, ebit, ebitda, ncfo | 3rd derivatives 001-150"""
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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _interest_coverage_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _interest_coverage_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _interest_coverage_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw intexp
def ic_f025_interest_coverage_raw_21d_accel_v001_signal(intexp, closeadj):
    base = _mean(intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw intexp
def ic_f025_interest_coverage_raw_21d_accel_v002_signal(intexp, closeadj):
    base = _mean(intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw intexp
def ic_f025_interest_coverage_raw_21d_accel_v003_signal(intexp, closeadj):
    base = _mean(intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw intexp
def ic_f025_interest_coverage_raw_63d_accel_v004_signal(intexp, closeadj):
    base = _mean(intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw intexp
def ic_f025_interest_coverage_raw_63d_accel_v005_signal(intexp, closeadj):
    base = _mean(intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw intexp
def ic_f025_interest_coverage_raw_63d_accel_v006_signal(intexp, closeadj):
    base = _mean(intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw intexp
def ic_f025_interest_coverage_raw_126d_accel_v007_signal(intexp, closeadj):
    base = _mean(intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw intexp
def ic_f025_interest_coverage_raw_126d_accel_v008_signal(intexp, closeadj):
    base = _mean(intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw intexp
def ic_f025_interest_coverage_raw_126d_accel_v009_signal(intexp, closeadj):
    base = _mean(intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw intexp
def ic_f025_interest_coverage_raw_252d_accel_v010_signal(intexp, closeadj):
    base = _mean(intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw intexp
def ic_f025_interest_coverage_raw_252d_accel_v011_signal(intexp, closeadj):
    base = _mean(intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw intexp
def ic_f025_interest_coverage_raw_252d_accel_v012_signal(intexp, closeadj):
    base = _mean(intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw intexp
def ic_f025_interest_coverage_raw_504d_accel_v013_signal(intexp, closeadj):
    base = _mean(intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw intexp
def ic_f025_interest_coverage_raw_504d_accel_v014_signal(intexp, closeadj):
    base = _mean(intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw intexp
def ic_f025_interest_coverage_raw_504d_accel_v015_signal(intexp, closeadj):
    base = _mean(intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log intexp
def ic_f025_interest_coverage_log_21d_accel_v016_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log intexp
def ic_f025_interest_coverage_log_21d_accel_v017_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log intexp
def ic_f025_interest_coverage_log_21d_accel_v018_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log intexp
def ic_f025_interest_coverage_log_63d_accel_v019_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log intexp
def ic_f025_interest_coverage_log_63d_accel_v020_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log intexp
def ic_f025_interest_coverage_log_63d_accel_v021_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log intexp
def ic_f025_interest_coverage_log_126d_accel_v022_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log intexp
def ic_f025_interest_coverage_log_126d_accel_v023_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log intexp
def ic_f025_interest_coverage_log_126d_accel_v024_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log intexp
def ic_f025_interest_coverage_log_252d_accel_v025_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log intexp
def ic_f025_interest_coverage_log_252d_accel_v026_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log intexp
def ic_f025_interest_coverage_log_252d_accel_v027_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log intexp
def ic_f025_interest_coverage_log_504d_accel_v028_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log intexp
def ic_f025_interest_coverage_log_504d_accel_v029_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log intexp
def ic_f025_interest_coverage_log_504d_accel_v030_signal(intexp, closeadj):
    base = _mean(_interest_coverage_log(intexp), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare intexp
def ic_f025_interest_coverage_pershare_21d_accel_v031_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare intexp
def ic_f025_interest_coverage_pershare_21d_accel_v032_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare intexp
def ic_f025_interest_coverage_pershare_21d_accel_v033_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare intexp
def ic_f025_interest_coverage_pershare_63d_accel_v034_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare intexp
def ic_f025_interest_coverage_pershare_63d_accel_v035_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare intexp
def ic_f025_interest_coverage_pershare_63d_accel_v036_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare intexp
def ic_f025_interest_coverage_pershare_126d_accel_v037_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare intexp
def ic_f025_interest_coverage_pershare_126d_accel_v038_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare intexp
def ic_f025_interest_coverage_pershare_126d_accel_v039_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare intexp
def ic_f025_interest_coverage_pershare_252d_accel_v040_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare intexp
def ic_f025_interest_coverage_pershare_252d_accel_v041_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare intexp
def ic_f025_interest_coverage_pershare_252d_accel_v042_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare intexp
def ic_f025_interest_coverage_pershare_504d_accel_v043_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare intexp
def ic_f025_interest_coverage_pershare_504d_accel_v044_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare intexp
def ic_f025_interest_coverage_pershare_504d_accel_v045_signal(intexp, sharesbas, closeadj):
    base = _mean(_interest_coverage_per_share(intexp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_21d_accel_v046_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_21d_accel_v047_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_21d_accel_v048_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_63d_accel_v049_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_63d_accel_v050_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_63d_accel_v051_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_126d_accel_v052_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_126d_accel_v053_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_126d_accel_v054_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_252d_accel_v055_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_252d_accel_v056_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_252d_accel_v057_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_504d_accel_v058_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_504d_accel_v059_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ebit intexp
def ic_f025_interest_coverage_per_ebit_504d_accel_v060_signal(intexp, ebit):
    base = _mean(_interest_coverage_scaled(intexp, ebit), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_21d_accel_v061_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_21d_accel_v062_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_21d_accel_v063_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_63d_accel_v064_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_63d_accel_v065_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_63d_accel_v066_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_126d_accel_v067_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_126d_accel_v068_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_126d_accel_v069_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_252d_accel_v070_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_252d_accel_v071_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_252d_accel_v072_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_504d_accel_v073_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_504d_accel_v074_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfo intexp
def ic_f025_interest_coverage_per_ncfo_504d_accel_v075_signal(intexp, ncfo):
    base = _mean(_interest_coverage_scaled(intexp, ncfo), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets intexp
def ic_f025_interest_coverage_per_assets_21d_accel_v076_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets intexp
def ic_f025_interest_coverage_per_assets_21d_accel_v077_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets intexp
def ic_f025_interest_coverage_per_assets_21d_accel_v078_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets intexp
def ic_f025_interest_coverage_per_assets_63d_accel_v079_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets intexp
def ic_f025_interest_coverage_per_assets_63d_accel_v080_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets intexp
def ic_f025_interest_coverage_per_assets_63d_accel_v081_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets intexp
def ic_f025_interest_coverage_per_assets_126d_accel_v082_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets intexp
def ic_f025_interest_coverage_per_assets_126d_accel_v083_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets intexp
def ic_f025_interest_coverage_per_assets_126d_accel_v084_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets intexp
def ic_f025_interest_coverage_per_assets_252d_accel_v085_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets intexp
def ic_f025_interest_coverage_per_assets_252d_accel_v086_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets intexp
def ic_f025_interest_coverage_per_assets_252d_accel_v087_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets intexp
def ic_f025_interest_coverage_per_assets_504d_accel_v088_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets intexp
def ic_f025_interest_coverage_per_assets_504d_accel_v089_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets intexp
def ic_f025_interest_coverage_per_assets_504d_accel_v090_signal(intexp, assets):
    base = _mean(_interest_coverage_scaled(intexp, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std intexp
def ic_f025_interest_coverage_std_21d_accel_v091_signal(intexp, closeadj):
    base = _std(intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std intexp
def ic_f025_interest_coverage_std_21d_accel_v092_signal(intexp, closeadj):
    base = _std(intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std intexp
def ic_f025_interest_coverage_std_21d_accel_v093_signal(intexp, closeadj):
    base = _std(intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std intexp
def ic_f025_interest_coverage_std_63d_accel_v094_signal(intexp, closeadj):
    base = _std(intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std intexp
def ic_f025_interest_coverage_std_63d_accel_v095_signal(intexp, closeadj):
    base = _std(intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std intexp
def ic_f025_interest_coverage_std_63d_accel_v096_signal(intexp, closeadj):
    base = _std(intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std intexp
def ic_f025_interest_coverage_std_126d_accel_v097_signal(intexp, closeadj):
    base = _std(intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std intexp
def ic_f025_interest_coverage_std_126d_accel_v098_signal(intexp, closeadj):
    base = _std(intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std intexp
def ic_f025_interest_coverage_std_126d_accel_v099_signal(intexp, closeadj):
    base = _std(intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std intexp
def ic_f025_interest_coverage_std_252d_accel_v100_signal(intexp, closeadj):
    base = _std(intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std intexp
def ic_f025_interest_coverage_std_252d_accel_v101_signal(intexp, closeadj):
    base = _std(intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std intexp
def ic_f025_interest_coverage_std_252d_accel_v102_signal(intexp, closeadj):
    base = _std(intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std intexp
def ic_f025_interest_coverage_std_504d_accel_v103_signal(intexp, closeadj):
    base = _std(intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std intexp
def ic_f025_interest_coverage_std_504d_accel_v104_signal(intexp, closeadj):
    base = _std(intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std intexp
def ic_f025_interest_coverage_std_504d_accel_v105_signal(intexp, closeadj):
    base = _std(intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm intexp
def ic_f025_interest_coverage_ewm_21d_accel_v106_signal(intexp, closeadj):
    base = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm intexp
def ic_f025_interest_coverage_ewm_21d_accel_v107_signal(intexp, closeadj):
    base = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm intexp
def ic_f025_interest_coverage_ewm_21d_accel_v108_signal(intexp, closeadj):
    base = intexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm intexp
def ic_f025_interest_coverage_ewm_63d_accel_v109_signal(intexp, closeadj):
    base = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm intexp
def ic_f025_interest_coverage_ewm_63d_accel_v110_signal(intexp, closeadj):
    base = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm intexp
def ic_f025_interest_coverage_ewm_63d_accel_v111_signal(intexp, closeadj):
    base = intexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm intexp
def ic_f025_interest_coverage_ewm_126d_accel_v112_signal(intexp, closeadj):
    base = intexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm intexp
def ic_f025_interest_coverage_ewm_126d_accel_v113_signal(intexp, closeadj):
    base = intexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm intexp
def ic_f025_interest_coverage_ewm_126d_accel_v114_signal(intexp, closeadj):
    base = intexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm intexp
def ic_f025_interest_coverage_ewm_252d_accel_v115_signal(intexp, closeadj):
    base = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm intexp
def ic_f025_interest_coverage_ewm_252d_accel_v116_signal(intexp, closeadj):
    base = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm intexp
def ic_f025_interest_coverage_ewm_252d_accel_v117_signal(intexp, closeadj):
    base = intexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm intexp
def ic_f025_interest_coverage_ewm_504d_accel_v118_signal(intexp, closeadj):
    base = intexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm intexp
def ic_f025_interest_coverage_ewm_504d_accel_v119_signal(intexp, closeadj):
    base = intexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm intexp
def ic_f025_interest_coverage_ewm_504d_accel_v120_signal(intexp, closeadj):
    base = intexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq intexp
def ic_f025_interest_coverage_sq_21d_accel_v121_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq intexp
def ic_f025_interest_coverage_sq_21d_accel_v122_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq intexp
def ic_f025_interest_coverage_sq_21d_accel_v123_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq intexp
def ic_f025_interest_coverage_sq_63d_accel_v124_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq intexp
def ic_f025_interest_coverage_sq_63d_accel_v125_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq intexp
def ic_f025_interest_coverage_sq_63d_accel_v126_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq intexp
def ic_f025_interest_coverage_sq_126d_accel_v127_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq intexp
def ic_f025_interest_coverage_sq_126d_accel_v128_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq intexp
def ic_f025_interest_coverage_sq_126d_accel_v129_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq intexp
def ic_f025_interest_coverage_sq_252d_accel_v130_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq intexp
def ic_f025_interest_coverage_sq_252d_accel_v131_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq intexp
def ic_f025_interest_coverage_sq_252d_accel_v132_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq intexp
def ic_f025_interest_coverage_sq_504d_accel_v133_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq intexp
def ic_f025_interest_coverage_sq_504d_accel_v134_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq intexp
def ic_f025_interest_coverage_sq_504d_accel_v135_signal(intexp, closeadj):
    base = _mean(intexp * intexp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z intexp
def ic_f025_interest_coverage_z_21d_accel_v136_signal(intexp):
    base = _z(intexp, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z intexp
def ic_f025_interest_coverage_z_21d_accel_v137_signal(intexp):
    base = _z(intexp, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z intexp
def ic_f025_interest_coverage_z_21d_accel_v138_signal(intexp):
    base = _z(intexp, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z intexp
def ic_f025_interest_coverage_z_63d_accel_v139_signal(intexp):
    base = _z(intexp, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z intexp
def ic_f025_interest_coverage_z_63d_accel_v140_signal(intexp):
    base = _z(intexp, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z intexp
def ic_f025_interest_coverage_z_63d_accel_v141_signal(intexp):
    base = _z(intexp, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z intexp
def ic_f025_interest_coverage_z_126d_accel_v142_signal(intexp):
    base = _z(intexp, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z intexp
def ic_f025_interest_coverage_z_126d_accel_v143_signal(intexp):
    base = _z(intexp, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z intexp
def ic_f025_interest_coverage_z_126d_accel_v144_signal(intexp):
    base = _z(intexp, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z intexp
def ic_f025_interest_coverage_z_252d_accel_v145_signal(intexp):
    base = _z(intexp, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z intexp
def ic_f025_interest_coverage_z_252d_accel_v146_signal(intexp):
    base = _z(intexp, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z intexp
def ic_f025_interest_coverage_z_252d_accel_v147_signal(intexp):
    base = _z(intexp, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z intexp
def ic_f025_interest_coverage_z_504d_accel_v148_signal(intexp):
    base = _z(intexp, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z intexp
def ic_f025_interest_coverage_z_504d_accel_v149_signal(intexp):
    base = _z(intexp, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z intexp
def ic_f025_interest_coverage_z_504d_accel_v150_signal(intexp):
    base = _z(intexp, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
