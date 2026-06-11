"""Family f085 - Field availability and schema coverage (Security Master and Universe) | Sharadar tables: INDICATORS | fields: table, indicator, title, description | 3rd derivatives 001-150"""
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
def _indicator_availability_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _indicator_availability_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _indicator_availability_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw field_coverage
def ia_f085_indicator_availability_raw_21d_accel_v001_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw field_coverage
def ia_f085_indicator_availability_raw_21d_accel_v002_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw field_coverage
def ia_f085_indicator_availability_raw_21d_accel_v003_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw field_coverage
def ia_f085_indicator_availability_raw_63d_accel_v004_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw field_coverage
def ia_f085_indicator_availability_raw_63d_accel_v005_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw field_coverage
def ia_f085_indicator_availability_raw_63d_accel_v006_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw field_coverage
def ia_f085_indicator_availability_raw_126d_accel_v007_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw field_coverage
def ia_f085_indicator_availability_raw_126d_accel_v008_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw field_coverage
def ia_f085_indicator_availability_raw_126d_accel_v009_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw field_coverage
def ia_f085_indicator_availability_raw_252d_accel_v010_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw field_coverage
def ia_f085_indicator_availability_raw_252d_accel_v011_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw field_coverage
def ia_f085_indicator_availability_raw_252d_accel_v012_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw field_coverage
def ia_f085_indicator_availability_raw_504d_accel_v013_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw field_coverage
def ia_f085_indicator_availability_raw_504d_accel_v014_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw field_coverage
def ia_f085_indicator_availability_raw_504d_accel_v015_signal(field_coverage, closeadj):
    base = _mean(field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log field_coverage
def ia_f085_indicator_availability_log_21d_accel_v016_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log field_coverage
def ia_f085_indicator_availability_log_21d_accel_v017_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log field_coverage
def ia_f085_indicator_availability_log_21d_accel_v018_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log field_coverage
def ia_f085_indicator_availability_log_63d_accel_v019_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log field_coverage
def ia_f085_indicator_availability_log_63d_accel_v020_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log field_coverage
def ia_f085_indicator_availability_log_63d_accel_v021_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log field_coverage
def ia_f085_indicator_availability_log_126d_accel_v022_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log field_coverage
def ia_f085_indicator_availability_log_126d_accel_v023_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log field_coverage
def ia_f085_indicator_availability_log_126d_accel_v024_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log field_coverage
def ia_f085_indicator_availability_log_252d_accel_v025_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log field_coverage
def ia_f085_indicator_availability_log_252d_accel_v026_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log field_coverage
def ia_f085_indicator_availability_log_252d_accel_v027_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log field_coverage
def ia_f085_indicator_availability_log_504d_accel_v028_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log field_coverage
def ia_f085_indicator_availability_log_504d_accel_v029_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log field_coverage
def ia_f085_indicator_availability_log_504d_accel_v030_signal(field_coverage, closeadj):
    base = _mean(_indicator_availability_log(field_coverage), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare field_coverage
def ia_f085_indicator_availability_pershare_21d_accel_v031_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare field_coverage
def ia_f085_indicator_availability_pershare_21d_accel_v032_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare field_coverage
def ia_f085_indicator_availability_pershare_21d_accel_v033_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare field_coverage
def ia_f085_indicator_availability_pershare_63d_accel_v034_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare field_coverage
def ia_f085_indicator_availability_pershare_63d_accel_v035_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare field_coverage
def ia_f085_indicator_availability_pershare_63d_accel_v036_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare field_coverage
def ia_f085_indicator_availability_pershare_126d_accel_v037_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare field_coverage
def ia_f085_indicator_availability_pershare_126d_accel_v038_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare field_coverage
def ia_f085_indicator_availability_pershare_126d_accel_v039_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare field_coverage
def ia_f085_indicator_availability_pershare_252d_accel_v040_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare field_coverage
def ia_f085_indicator_availability_pershare_252d_accel_v041_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare field_coverage
def ia_f085_indicator_availability_pershare_252d_accel_v042_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare field_coverage
def ia_f085_indicator_availability_pershare_504d_accel_v043_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare field_coverage
def ia_f085_indicator_availability_pershare_504d_accel_v044_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare field_coverage
def ia_f085_indicator_availability_pershare_504d_accel_v045_signal(field_coverage, sharesbas, closeadj):
    base = _mean(_indicator_availability_per_share(field_coverage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_21d_accel_v046_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_21d_accel_v047_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_21d_accel_v048_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_63d_accel_v049_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_63d_accel_v050_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_63d_accel_v051_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_126d_accel_v052_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_126d_accel_v053_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_126d_accel_v054_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_252d_accel_v055_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_252d_accel_v056_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_252d_accel_v057_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_504d_accel_v058_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_504d_accel_v059_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_indicator field_coverage
def ia_f085_indicator_availability_per_indicator_504d_accel_v060_signal(field_coverage, indicator):
    base = _mean(_indicator_availability_scaled(field_coverage, indicator), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_21d_accel_v061_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_21d_accel_v062_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_21d_accel_v063_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_63d_accel_v064_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_63d_accel_v065_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_63d_accel_v066_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_126d_accel_v067_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_126d_accel_v068_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_126d_accel_v069_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_252d_accel_v070_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_252d_accel_v071_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_252d_accel_v072_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_504d_accel_v073_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_504d_accel_v074_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets field_coverage
def ia_f085_indicator_availability_per_assets_504d_accel_v075_signal(field_coverage, assets):
    base = _mean(_indicator_availability_scaled(field_coverage, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_21d_accel_v076_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_21d_accel_v077_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_21d_accel_v078_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_63d_accel_v079_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_63d_accel_v080_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_63d_accel_v081_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_126d_accel_v082_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_126d_accel_v083_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_126d_accel_v084_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_252d_accel_v085_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_252d_accel_v086_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_252d_accel_v087_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_504d_accel_v088_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_504d_accel_v089_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap field_coverage
def ia_f085_indicator_availability_per_marketcap_504d_accel_v090_signal(field_coverage, marketcap):
    base = _mean(_indicator_availability_scaled(field_coverage, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std field_coverage
def ia_f085_indicator_availability_std_21d_accel_v091_signal(field_coverage, closeadj):
    base = _std(field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std field_coverage
def ia_f085_indicator_availability_std_21d_accel_v092_signal(field_coverage, closeadj):
    base = _std(field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std field_coverage
def ia_f085_indicator_availability_std_21d_accel_v093_signal(field_coverage, closeadj):
    base = _std(field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std field_coverage
def ia_f085_indicator_availability_std_63d_accel_v094_signal(field_coverage, closeadj):
    base = _std(field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std field_coverage
def ia_f085_indicator_availability_std_63d_accel_v095_signal(field_coverage, closeadj):
    base = _std(field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std field_coverage
def ia_f085_indicator_availability_std_63d_accel_v096_signal(field_coverage, closeadj):
    base = _std(field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std field_coverage
def ia_f085_indicator_availability_std_126d_accel_v097_signal(field_coverage, closeadj):
    base = _std(field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std field_coverage
def ia_f085_indicator_availability_std_126d_accel_v098_signal(field_coverage, closeadj):
    base = _std(field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std field_coverage
def ia_f085_indicator_availability_std_126d_accel_v099_signal(field_coverage, closeadj):
    base = _std(field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std field_coverage
def ia_f085_indicator_availability_std_252d_accel_v100_signal(field_coverage, closeadj):
    base = _std(field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std field_coverage
def ia_f085_indicator_availability_std_252d_accel_v101_signal(field_coverage, closeadj):
    base = _std(field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std field_coverage
def ia_f085_indicator_availability_std_252d_accel_v102_signal(field_coverage, closeadj):
    base = _std(field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std field_coverage
def ia_f085_indicator_availability_std_504d_accel_v103_signal(field_coverage, closeadj):
    base = _std(field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std field_coverage
def ia_f085_indicator_availability_std_504d_accel_v104_signal(field_coverage, closeadj):
    base = _std(field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std field_coverage
def ia_f085_indicator_availability_std_504d_accel_v105_signal(field_coverage, closeadj):
    base = _std(field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm field_coverage
def ia_f085_indicator_availability_ewm_21d_accel_v106_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm field_coverage
def ia_f085_indicator_availability_ewm_21d_accel_v107_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm field_coverage
def ia_f085_indicator_availability_ewm_21d_accel_v108_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm field_coverage
def ia_f085_indicator_availability_ewm_63d_accel_v109_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm field_coverage
def ia_f085_indicator_availability_ewm_63d_accel_v110_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm field_coverage
def ia_f085_indicator_availability_ewm_63d_accel_v111_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm field_coverage
def ia_f085_indicator_availability_ewm_126d_accel_v112_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm field_coverage
def ia_f085_indicator_availability_ewm_126d_accel_v113_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm field_coverage
def ia_f085_indicator_availability_ewm_126d_accel_v114_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm field_coverage
def ia_f085_indicator_availability_ewm_252d_accel_v115_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm field_coverage
def ia_f085_indicator_availability_ewm_252d_accel_v116_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm field_coverage
def ia_f085_indicator_availability_ewm_252d_accel_v117_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm field_coverage
def ia_f085_indicator_availability_ewm_504d_accel_v118_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm field_coverage
def ia_f085_indicator_availability_ewm_504d_accel_v119_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm field_coverage
def ia_f085_indicator_availability_ewm_504d_accel_v120_signal(field_coverage, closeadj):
    base = field_coverage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq field_coverage
def ia_f085_indicator_availability_sq_21d_accel_v121_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq field_coverage
def ia_f085_indicator_availability_sq_21d_accel_v122_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq field_coverage
def ia_f085_indicator_availability_sq_21d_accel_v123_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq field_coverage
def ia_f085_indicator_availability_sq_63d_accel_v124_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq field_coverage
def ia_f085_indicator_availability_sq_63d_accel_v125_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq field_coverage
def ia_f085_indicator_availability_sq_63d_accel_v126_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq field_coverage
def ia_f085_indicator_availability_sq_126d_accel_v127_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq field_coverage
def ia_f085_indicator_availability_sq_126d_accel_v128_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq field_coverage
def ia_f085_indicator_availability_sq_126d_accel_v129_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq field_coverage
def ia_f085_indicator_availability_sq_252d_accel_v130_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq field_coverage
def ia_f085_indicator_availability_sq_252d_accel_v131_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq field_coverage
def ia_f085_indicator_availability_sq_252d_accel_v132_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq field_coverage
def ia_f085_indicator_availability_sq_504d_accel_v133_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq field_coverage
def ia_f085_indicator_availability_sq_504d_accel_v134_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq field_coverage
def ia_f085_indicator_availability_sq_504d_accel_v135_signal(field_coverage, closeadj):
    base = _mean(field_coverage * field_coverage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z field_coverage
def ia_f085_indicator_availability_z_21d_accel_v136_signal(field_coverage):
    base = _z(field_coverage, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z field_coverage
def ia_f085_indicator_availability_z_21d_accel_v137_signal(field_coverage):
    base = _z(field_coverage, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z field_coverage
def ia_f085_indicator_availability_z_21d_accel_v138_signal(field_coverage):
    base = _z(field_coverage, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z field_coverage
def ia_f085_indicator_availability_z_63d_accel_v139_signal(field_coverage):
    base = _z(field_coverage, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z field_coverage
def ia_f085_indicator_availability_z_63d_accel_v140_signal(field_coverage):
    base = _z(field_coverage, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z field_coverage
def ia_f085_indicator_availability_z_63d_accel_v141_signal(field_coverage):
    base = _z(field_coverage, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z field_coverage
def ia_f085_indicator_availability_z_126d_accel_v142_signal(field_coverage):
    base = _z(field_coverage, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z field_coverage
def ia_f085_indicator_availability_z_126d_accel_v143_signal(field_coverage):
    base = _z(field_coverage, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z field_coverage
def ia_f085_indicator_availability_z_126d_accel_v144_signal(field_coverage):
    base = _z(field_coverage, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z field_coverage
def ia_f085_indicator_availability_z_252d_accel_v145_signal(field_coverage):
    base = _z(field_coverage, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z field_coverage
def ia_f085_indicator_availability_z_252d_accel_v146_signal(field_coverage):
    base = _z(field_coverage, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z field_coverage
def ia_f085_indicator_availability_z_252d_accel_v147_signal(field_coverage):
    base = _z(field_coverage, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z field_coverage
def ia_f085_indicator_availability_z_504d_accel_v148_signal(field_coverage):
    base = _z(field_coverage, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z field_coverage
def ia_f085_indicator_availability_z_504d_accel_v149_signal(field_coverage):
    base = _z(field_coverage, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z field_coverage
def ia_f085_indicator_availability_z_504d_accel_v150_signal(field_coverage):
    base = _z(field_coverage, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
