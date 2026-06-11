"""Family f095 - Institutional ownership level (Insiders and Ownership) | Sharadar tables: SF3 | fields: calendardate, investorname, value, units, price | 3rd derivatives 001-150"""
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
def _institutional_ownership_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _institutional_ownership_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _institutional_ownership_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw calendardate
def iol_f095_institutional_ownership_level_raw_21d_accel_v001_signal(calendardate, closeadj):
    base = _mean(calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw calendardate
def iol_f095_institutional_ownership_level_raw_21d_accel_v002_signal(calendardate, closeadj):
    base = _mean(calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw calendardate
def iol_f095_institutional_ownership_level_raw_21d_accel_v003_signal(calendardate, closeadj):
    base = _mean(calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw calendardate
def iol_f095_institutional_ownership_level_raw_63d_accel_v004_signal(calendardate, closeadj):
    base = _mean(calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw calendardate
def iol_f095_institutional_ownership_level_raw_63d_accel_v005_signal(calendardate, closeadj):
    base = _mean(calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw calendardate
def iol_f095_institutional_ownership_level_raw_63d_accel_v006_signal(calendardate, closeadj):
    base = _mean(calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw calendardate
def iol_f095_institutional_ownership_level_raw_126d_accel_v007_signal(calendardate, closeadj):
    base = _mean(calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw calendardate
def iol_f095_institutional_ownership_level_raw_126d_accel_v008_signal(calendardate, closeadj):
    base = _mean(calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw calendardate
def iol_f095_institutional_ownership_level_raw_126d_accel_v009_signal(calendardate, closeadj):
    base = _mean(calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw calendardate
def iol_f095_institutional_ownership_level_raw_252d_accel_v010_signal(calendardate, closeadj):
    base = _mean(calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw calendardate
def iol_f095_institutional_ownership_level_raw_252d_accel_v011_signal(calendardate, closeadj):
    base = _mean(calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw calendardate
def iol_f095_institutional_ownership_level_raw_252d_accel_v012_signal(calendardate, closeadj):
    base = _mean(calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw calendardate
def iol_f095_institutional_ownership_level_raw_504d_accel_v013_signal(calendardate, closeadj):
    base = _mean(calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw calendardate
def iol_f095_institutional_ownership_level_raw_504d_accel_v014_signal(calendardate, closeadj):
    base = _mean(calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw calendardate
def iol_f095_institutional_ownership_level_raw_504d_accel_v015_signal(calendardate, closeadj):
    base = _mean(calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log calendardate
def iol_f095_institutional_ownership_level_log_21d_accel_v016_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log calendardate
def iol_f095_institutional_ownership_level_log_21d_accel_v017_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log calendardate
def iol_f095_institutional_ownership_level_log_21d_accel_v018_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log calendardate
def iol_f095_institutional_ownership_level_log_63d_accel_v019_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log calendardate
def iol_f095_institutional_ownership_level_log_63d_accel_v020_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log calendardate
def iol_f095_institutional_ownership_level_log_63d_accel_v021_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log calendardate
def iol_f095_institutional_ownership_level_log_126d_accel_v022_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log calendardate
def iol_f095_institutional_ownership_level_log_126d_accel_v023_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log calendardate
def iol_f095_institutional_ownership_level_log_126d_accel_v024_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log calendardate
def iol_f095_institutional_ownership_level_log_252d_accel_v025_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log calendardate
def iol_f095_institutional_ownership_level_log_252d_accel_v026_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log calendardate
def iol_f095_institutional_ownership_level_log_252d_accel_v027_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log calendardate
def iol_f095_institutional_ownership_level_log_504d_accel_v028_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log calendardate
def iol_f095_institutional_ownership_level_log_504d_accel_v029_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log calendardate
def iol_f095_institutional_ownership_level_log_504d_accel_v030_signal(calendardate, closeadj):
    base = _mean(_institutional_ownership_level_log(calendardate), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_21d_accel_v031_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_21d_accel_v032_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_21d_accel_v033_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_63d_accel_v034_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_63d_accel_v035_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_63d_accel_v036_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_126d_accel_v037_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_126d_accel_v038_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_126d_accel_v039_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_252d_accel_v040_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_252d_accel_v041_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_252d_accel_v042_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_504d_accel_v043_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_504d_accel_v044_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare calendardate
def iol_f095_institutional_ownership_level_pershare_504d_accel_v045_signal(calendardate, sharesbas, closeadj):
    base = _mean(_institutional_ownership_level_per_share(calendardate, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_21d_accel_v046_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_21d_accel_v047_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_21d_accel_v048_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_63d_accel_v049_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_63d_accel_v050_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_63d_accel_v051_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_126d_accel_v052_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_126d_accel_v053_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_126d_accel_v054_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_252d_accel_v055_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_252d_accel_v056_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_252d_accel_v057_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_504d_accel_v058_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_504d_accel_v059_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_value calendardate
def iol_f095_institutional_ownership_level_per_value_504d_accel_v060_signal(calendardate, value):
    base = _mean(_institutional_ownership_level_scaled(calendardate, value), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_21d_accel_v061_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_21d_accel_v062_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_21d_accel_v063_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_63d_accel_v064_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_63d_accel_v065_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_63d_accel_v066_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_126d_accel_v067_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_126d_accel_v068_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_126d_accel_v069_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_252d_accel_v070_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_252d_accel_v071_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_252d_accel_v072_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_504d_accel_v073_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_504d_accel_v074_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_units calendardate
def iol_f095_institutional_ownership_level_per_units_504d_accel_v075_signal(calendardate, units):
    base = _mean(_institutional_ownership_level_scaled(calendardate, units), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_21d_accel_v076_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_21d_accel_v077_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_21d_accel_v078_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_63d_accel_v079_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_63d_accel_v080_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_63d_accel_v081_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_126d_accel_v082_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_126d_accel_v083_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_126d_accel_v084_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_252d_accel_v085_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_252d_accel_v086_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_252d_accel_v087_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_504d_accel_v088_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_504d_accel_v089_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_price calendardate
def iol_f095_institutional_ownership_level_per_price_504d_accel_v090_signal(calendardate, price):
    base = _mean(_institutional_ownership_level_scaled(calendardate, price), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std calendardate
def iol_f095_institutional_ownership_level_std_21d_accel_v091_signal(calendardate, closeadj):
    base = _std(calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std calendardate
def iol_f095_institutional_ownership_level_std_21d_accel_v092_signal(calendardate, closeadj):
    base = _std(calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std calendardate
def iol_f095_institutional_ownership_level_std_21d_accel_v093_signal(calendardate, closeadj):
    base = _std(calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std calendardate
def iol_f095_institutional_ownership_level_std_63d_accel_v094_signal(calendardate, closeadj):
    base = _std(calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std calendardate
def iol_f095_institutional_ownership_level_std_63d_accel_v095_signal(calendardate, closeadj):
    base = _std(calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std calendardate
def iol_f095_institutional_ownership_level_std_63d_accel_v096_signal(calendardate, closeadj):
    base = _std(calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std calendardate
def iol_f095_institutional_ownership_level_std_126d_accel_v097_signal(calendardate, closeadj):
    base = _std(calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std calendardate
def iol_f095_institutional_ownership_level_std_126d_accel_v098_signal(calendardate, closeadj):
    base = _std(calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std calendardate
def iol_f095_institutional_ownership_level_std_126d_accel_v099_signal(calendardate, closeadj):
    base = _std(calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std calendardate
def iol_f095_institutional_ownership_level_std_252d_accel_v100_signal(calendardate, closeadj):
    base = _std(calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std calendardate
def iol_f095_institutional_ownership_level_std_252d_accel_v101_signal(calendardate, closeadj):
    base = _std(calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std calendardate
def iol_f095_institutional_ownership_level_std_252d_accel_v102_signal(calendardate, closeadj):
    base = _std(calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std calendardate
def iol_f095_institutional_ownership_level_std_504d_accel_v103_signal(calendardate, closeadj):
    base = _std(calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std calendardate
def iol_f095_institutional_ownership_level_std_504d_accel_v104_signal(calendardate, closeadj):
    base = _std(calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std calendardate
def iol_f095_institutional_ownership_level_std_504d_accel_v105_signal(calendardate, closeadj):
    base = _std(calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_21d_accel_v106_signal(calendardate, closeadj):
    base = calendardate.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_21d_accel_v107_signal(calendardate, closeadj):
    base = calendardate.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_21d_accel_v108_signal(calendardate, closeadj):
    base = calendardate.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_63d_accel_v109_signal(calendardate, closeadj):
    base = calendardate.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_63d_accel_v110_signal(calendardate, closeadj):
    base = calendardate.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_63d_accel_v111_signal(calendardate, closeadj):
    base = calendardate.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_126d_accel_v112_signal(calendardate, closeadj):
    base = calendardate.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_126d_accel_v113_signal(calendardate, closeadj):
    base = calendardate.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_126d_accel_v114_signal(calendardate, closeadj):
    base = calendardate.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_252d_accel_v115_signal(calendardate, closeadj):
    base = calendardate.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_252d_accel_v116_signal(calendardate, closeadj):
    base = calendardate.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_252d_accel_v117_signal(calendardate, closeadj):
    base = calendardate.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_504d_accel_v118_signal(calendardate, closeadj):
    base = calendardate.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_504d_accel_v119_signal(calendardate, closeadj):
    base = calendardate.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm calendardate
def iol_f095_institutional_ownership_level_ewm_504d_accel_v120_signal(calendardate, closeadj):
    base = calendardate.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq calendardate
def iol_f095_institutional_ownership_level_sq_21d_accel_v121_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq calendardate
def iol_f095_institutional_ownership_level_sq_21d_accel_v122_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq calendardate
def iol_f095_institutional_ownership_level_sq_21d_accel_v123_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq calendardate
def iol_f095_institutional_ownership_level_sq_63d_accel_v124_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq calendardate
def iol_f095_institutional_ownership_level_sq_63d_accel_v125_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq calendardate
def iol_f095_institutional_ownership_level_sq_63d_accel_v126_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq calendardate
def iol_f095_institutional_ownership_level_sq_126d_accel_v127_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq calendardate
def iol_f095_institutional_ownership_level_sq_126d_accel_v128_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq calendardate
def iol_f095_institutional_ownership_level_sq_126d_accel_v129_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq calendardate
def iol_f095_institutional_ownership_level_sq_252d_accel_v130_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq calendardate
def iol_f095_institutional_ownership_level_sq_252d_accel_v131_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq calendardate
def iol_f095_institutional_ownership_level_sq_252d_accel_v132_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq calendardate
def iol_f095_institutional_ownership_level_sq_504d_accel_v133_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq calendardate
def iol_f095_institutional_ownership_level_sq_504d_accel_v134_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq calendardate
def iol_f095_institutional_ownership_level_sq_504d_accel_v135_signal(calendardate, closeadj):
    base = _mean(calendardate * calendardate, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z calendardate
def iol_f095_institutional_ownership_level_z_21d_accel_v136_signal(calendardate):
    base = _z(calendardate, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z calendardate
def iol_f095_institutional_ownership_level_z_21d_accel_v137_signal(calendardate):
    base = _z(calendardate, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z calendardate
def iol_f095_institutional_ownership_level_z_21d_accel_v138_signal(calendardate):
    base = _z(calendardate, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z calendardate
def iol_f095_institutional_ownership_level_z_63d_accel_v139_signal(calendardate):
    base = _z(calendardate, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z calendardate
def iol_f095_institutional_ownership_level_z_63d_accel_v140_signal(calendardate):
    base = _z(calendardate, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z calendardate
def iol_f095_institutional_ownership_level_z_63d_accel_v141_signal(calendardate):
    base = _z(calendardate, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z calendardate
def iol_f095_institutional_ownership_level_z_126d_accel_v142_signal(calendardate):
    base = _z(calendardate, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z calendardate
def iol_f095_institutional_ownership_level_z_126d_accel_v143_signal(calendardate):
    base = _z(calendardate, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z calendardate
def iol_f095_institutional_ownership_level_z_126d_accel_v144_signal(calendardate):
    base = _z(calendardate, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z calendardate
def iol_f095_institutional_ownership_level_z_252d_accel_v145_signal(calendardate):
    base = _z(calendardate, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z calendardate
def iol_f095_institutional_ownership_level_z_252d_accel_v146_signal(calendardate):
    base = _z(calendardate, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z calendardate
def iol_f095_institutional_ownership_level_z_252d_accel_v147_signal(calendardate):
    base = _z(calendardate, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z calendardate
def iol_f095_institutional_ownership_level_z_504d_accel_v148_signal(calendardate):
    base = _z(calendardate, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z calendardate
def iol_f095_institutional_ownership_level_z_504d_accel_v149_signal(calendardate):
    base = _z(calendardate, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z calendardate
def iol_f095_institutional_ownership_level_z_504d_accel_v150_signal(calendardate):
    base = _z(calendardate, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
