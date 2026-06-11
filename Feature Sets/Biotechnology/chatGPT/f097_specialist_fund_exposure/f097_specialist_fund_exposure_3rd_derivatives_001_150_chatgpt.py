"""Family f097 - Healthcare specialist and activist exposure (Insiders and Ownership) | Sharadar tables: SF3,SF3A,SF3B | fields: investorname, value, units | 3rd derivatives 001-150"""
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
def _specialist_fund_exposure_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _specialist_fund_exposure_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _specialist_fund_exposure_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw value
def sfe_f097_specialist_fund_exposure_raw_21d_accel_v001_signal(value, closeadj):
    base = _mean(value, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw value
def sfe_f097_specialist_fund_exposure_raw_21d_accel_v002_signal(value, closeadj):
    base = _mean(value, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw value
def sfe_f097_specialist_fund_exposure_raw_21d_accel_v003_signal(value, closeadj):
    base = _mean(value, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw value
def sfe_f097_specialist_fund_exposure_raw_63d_accel_v004_signal(value, closeadj):
    base = _mean(value, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw value
def sfe_f097_specialist_fund_exposure_raw_63d_accel_v005_signal(value, closeadj):
    base = _mean(value, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw value
def sfe_f097_specialist_fund_exposure_raw_63d_accel_v006_signal(value, closeadj):
    base = _mean(value, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw value
def sfe_f097_specialist_fund_exposure_raw_126d_accel_v007_signal(value, closeadj):
    base = _mean(value, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw value
def sfe_f097_specialist_fund_exposure_raw_126d_accel_v008_signal(value, closeadj):
    base = _mean(value, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw value
def sfe_f097_specialist_fund_exposure_raw_126d_accel_v009_signal(value, closeadj):
    base = _mean(value, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw value
def sfe_f097_specialist_fund_exposure_raw_252d_accel_v010_signal(value, closeadj):
    base = _mean(value, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw value
def sfe_f097_specialist_fund_exposure_raw_252d_accel_v011_signal(value, closeadj):
    base = _mean(value, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw value
def sfe_f097_specialist_fund_exposure_raw_252d_accel_v012_signal(value, closeadj):
    base = _mean(value, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw value
def sfe_f097_specialist_fund_exposure_raw_504d_accel_v013_signal(value, closeadj):
    base = _mean(value, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw value
def sfe_f097_specialist_fund_exposure_raw_504d_accel_v014_signal(value, closeadj):
    base = _mean(value, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw value
def sfe_f097_specialist_fund_exposure_raw_504d_accel_v015_signal(value, closeadj):
    base = _mean(value, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log value
def sfe_f097_specialist_fund_exposure_log_21d_accel_v016_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log value
def sfe_f097_specialist_fund_exposure_log_21d_accel_v017_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log value
def sfe_f097_specialist_fund_exposure_log_21d_accel_v018_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log value
def sfe_f097_specialist_fund_exposure_log_63d_accel_v019_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log value
def sfe_f097_specialist_fund_exposure_log_63d_accel_v020_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log value
def sfe_f097_specialist_fund_exposure_log_63d_accel_v021_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log value
def sfe_f097_specialist_fund_exposure_log_126d_accel_v022_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log value
def sfe_f097_specialist_fund_exposure_log_126d_accel_v023_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log value
def sfe_f097_specialist_fund_exposure_log_126d_accel_v024_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log value
def sfe_f097_specialist_fund_exposure_log_252d_accel_v025_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log value
def sfe_f097_specialist_fund_exposure_log_252d_accel_v026_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log value
def sfe_f097_specialist_fund_exposure_log_252d_accel_v027_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log value
def sfe_f097_specialist_fund_exposure_log_504d_accel_v028_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log value
def sfe_f097_specialist_fund_exposure_log_504d_accel_v029_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log value
def sfe_f097_specialist_fund_exposure_log_504d_accel_v030_signal(value, closeadj):
    base = _mean(_specialist_fund_exposure_log(value), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare value
def sfe_f097_specialist_fund_exposure_pershare_21d_accel_v031_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare value
def sfe_f097_specialist_fund_exposure_pershare_21d_accel_v032_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare value
def sfe_f097_specialist_fund_exposure_pershare_21d_accel_v033_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare value
def sfe_f097_specialist_fund_exposure_pershare_63d_accel_v034_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare value
def sfe_f097_specialist_fund_exposure_pershare_63d_accel_v035_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare value
def sfe_f097_specialist_fund_exposure_pershare_63d_accel_v036_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare value
def sfe_f097_specialist_fund_exposure_pershare_126d_accel_v037_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare value
def sfe_f097_specialist_fund_exposure_pershare_126d_accel_v038_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare value
def sfe_f097_specialist_fund_exposure_pershare_126d_accel_v039_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare value
def sfe_f097_specialist_fund_exposure_pershare_252d_accel_v040_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare value
def sfe_f097_specialist_fund_exposure_pershare_252d_accel_v041_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare value
def sfe_f097_specialist_fund_exposure_pershare_252d_accel_v042_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare value
def sfe_f097_specialist_fund_exposure_pershare_504d_accel_v043_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare value
def sfe_f097_specialist_fund_exposure_pershare_504d_accel_v044_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare value
def sfe_f097_specialist_fund_exposure_pershare_504d_accel_v045_signal(value, sharesbas, closeadj):
    base = _mean(_specialist_fund_exposure_per_share(value, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_units value
def sfe_f097_specialist_fund_exposure_per_units_21d_accel_v046_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_units value
def sfe_f097_specialist_fund_exposure_per_units_21d_accel_v047_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_units value
def sfe_f097_specialist_fund_exposure_per_units_21d_accel_v048_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_units value
def sfe_f097_specialist_fund_exposure_per_units_63d_accel_v049_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_units value
def sfe_f097_specialist_fund_exposure_per_units_63d_accel_v050_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_units value
def sfe_f097_specialist_fund_exposure_per_units_63d_accel_v051_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_units value
def sfe_f097_specialist_fund_exposure_per_units_126d_accel_v052_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_units value
def sfe_f097_specialist_fund_exposure_per_units_126d_accel_v053_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_units value
def sfe_f097_specialist_fund_exposure_per_units_126d_accel_v054_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_units value
def sfe_f097_specialist_fund_exposure_per_units_252d_accel_v055_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_units value
def sfe_f097_specialist_fund_exposure_per_units_252d_accel_v056_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_units value
def sfe_f097_specialist_fund_exposure_per_units_252d_accel_v057_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_units value
def sfe_f097_specialist_fund_exposure_per_units_504d_accel_v058_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_units value
def sfe_f097_specialist_fund_exposure_per_units_504d_accel_v059_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_units value
def sfe_f097_specialist_fund_exposure_per_units_504d_accel_v060_signal(value, units):
    base = _mean(_specialist_fund_exposure_scaled(value, units), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_21d_accel_v061_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_21d_accel_v062_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_21d_accel_v063_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_63d_accel_v064_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_63d_accel_v065_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_63d_accel_v066_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_126d_accel_v067_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_126d_accel_v068_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_126d_accel_v069_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_252d_accel_v070_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_252d_accel_v071_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_252d_accel_v072_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_504d_accel_v073_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_504d_accel_v074_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets value
def sfe_f097_specialist_fund_exposure_per_assets_504d_accel_v075_signal(value, assets):
    base = _mean(_specialist_fund_exposure_scaled(value, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_21d_accel_v076_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_21d_accel_v077_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_21d_accel_v078_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_63d_accel_v079_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_63d_accel_v080_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_63d_accel_v081_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_126d_accel_v082_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_126d_accel_v083_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_126d_accel_v084_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_252d_accel_v085_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_252d_accel_v086_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_252d_accel_v087_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_504d_accel_v088_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_504d_accel_v089_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap value
def sfe_f097_specialist_fund_exposure_per_marketcap_504d_accel_v090_signal(value, marketcap):
    base = _mean(_specialist_fund_exposure_scaled(value, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std value
def sfe_f097_specialist_fund_exposure_std_21d_accel_v091_signal(value, closeadj):
    base = _std(value, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std value
def sfe_f097_specialist_fund_exposure_std_21d_accel_v092_signal(value, closeadj):
    base = _std(value, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std value
def sfe_f097_specialist_fund_exposure_std_21d_accel_v093_signal(value, closeadj):
    base = _std(value, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std value
def sfe_f097_specialist_fund_exposure_std_63d_accel_v094_signal(value, closeadj):
    base = _std(value, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std value
def sfe_f097_specialist_fund_exposure_std_63d_accel_v095_signal(value, closeadj):
    base = _std(value, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std value
def sfe_f097_specialist_fund_exposure_std_63d_accel_v096_signal(value, closeadj):
    base = _std(value, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std value
def sfe_f097_specialist_fund_exposure_std_126d_accel_v097_signal(value, closeadj):
    base = _std(value, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std value
def sfe_f097_specialist_fund_exposure_std_126d_accel_v098_signal(value, closeadj):
    base = _std(value, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std value
def sfe_f097_specialist_fund_exposure_std_126d_accel_v099_signal(value, closeadj):
    base = _std(value, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std value
def sfe_f097_specialist_fund_exposure_std_252d_accel_v100_signal(value, closeadj):
    base = _std(value, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std value
def sfe_f097_specialist_fund_exposure_std_252d_accel_v101_signal(value, closeadj):
    base = _std(value, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std value
def sfe_f097_specialist_fund_exposure_std_252d_accel_v102_signal(value, closeadj):
    base = _std(value, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std value
def sfe_f097_specialist_fund_exposure_std_504d_accel_v103_signal(value, closeadj):
    base = _std(value, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std value
def sfe_f097_specialist_fund_exposure_std_504d_accel_v104_signal(value, closeadj):
    base = _std(value, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std value
def sfe_f097_specialist_fund_exposure_std_504d_accel_v105_signal(value, closeadj):
    base = _std(value, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm value
def sfe_f097_specialist_fund_exposure_ewm_21d_accel_v106_signal(value, closeadj):
    base = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm value
def sfe_f097_specialist_fund_exposure_ewm_21d_accel_v107_signal(value, closeadj):
    base = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm value
def sfe_f097_specialist_fund_exposure_ewm_21d_accel_v108_signal(value, closeadj):
    base = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm value
def sfe_f097_specialist_fund_exposure_ewm_63d_accel_v109_signal(value, closeadj):
    base = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm value
def sfe_f097_specialist_fund_exposure_ewm_63d_accel_v110_signal(value, closeadj):
    base = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm value
def sfe_f097_specialist_fund_exposure_ewm_63d_accel_v111_signal(value, closeadj):
    base = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm value
def sfe_f097_specialist_fund_exposure_ewm_126d_accel_v112_signal(value, closeadj):
    base = value.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm value
def sfe_f097_specialist_fund_exposure_ewm_126d_accel_v113_signal(value, closeadj):
    base = value.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm value
def sfe_f097_specialist_fund_exposure_ewm_126d_accel_v114_signal(value, closeadj):
    base = value.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm value
def sfe_f097_specialist_fund_exposure_ewm_252d_accel_v115_signal(value, closeadj):
    base = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm value
def sfe_f097_specialist_fund_exposure_ewm_252d_accel_v116_signal(value, closeadj):
    base = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm value
def sfe_f097_specialist_fund_exposure_ewm_252d_accel_v117_signal(value, closeadj):
    base = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm value
def sfe_f097_specialist_fund_exposure_ewm_504d_accel_v118_signal(value, closeadj):
    base = value.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm value
def sfe_f097_specialist_fund_exposure_ewm_504d_accel_v119_signal(value, closeadj):
    base = value.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm value
def sfe_f097_specialist_fund_exposure_ewm_504d_accel_v120_signal(value, closeadj):
    base = value.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq value
def sfe_f097_specialist_fund_exposure_sq_21d_accel_v121_signal(value, closeadj):
    base = _mean(value * value, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq value
def sfe_f097_specialist_fund_exposure_sq_21d_accel_v122_signal(value, closeadj):
    base = _mean(value * value, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq value
def sfe_f097_specialist_fund_exposure_sq_21d_accel_v123_signal(value, closeadj):
    base = _mean(value * value, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq value
def sfe_f097_specialist_fund_exposure_sq_63d_accel_v124_signal(value, closeadj):
    base = _mean(value * value, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq value
def sfe_f097_specialist_fund_exposure_sq_63d_accel_v125_signal(value, closeadj):
    base = _mean(value * value, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq value
def sfe_f097_specialist_fund_exposure_sq_63d_accel_v126_signal(value, closeadj):
    base = _mean(value * value, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq value
def sfe_f097_specialist_fund_exposure_sq_126d_accel_v127_signal(value, closeadj):
    base = _mean(value * value, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq value
def sfe_f097_specialist_fund_exposure_sq_126d_accel_v128_signal(value, closeadj):
    base = _mean(value * value, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq value
def sfe_f097_specialist_fund_exposure_sq_126d_accel_v129_signal(value, closeadj):
    base = _mean(value * value, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq value
def sfe_f097_specialist_fund_exposure_sq_252d_accel_v130_signal(value, closeadj):
    base = _mean(value * value, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq value
def sfe_f097_specialist_fund_exposure_sq_252d_accel_v131_signal(value, closeadj):
    base = _mean(value * value, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq value
def sfe_f097_specialist_fund_exposure_sq_252d_accel_v132_signal(value, closeadj):
    base = _mean(value * value, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq value
def sfe_f097_specialist_fund_exposure_sq_504d_accel_v133_signal(value, closeadj):
    base = _mean(value * value, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq value
def sfe_f097_specialist_fund_exposure_sq_504d_accel_v134_signal(value, closeadj):
    base = _mean(value * value, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq value
def sfe_f097_specialist_fund_exposure_sq_504d_accel_v135_signal(value, closeadj):
    base = _mean(value * value, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z value
def sfe_f097_specialist_fund_exposure_z_21d_accel_v136_signal(value):
    base = _z(value, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z value
def sfe_f097_specialist_fund_exposure_z_21d_accel_v137_signal(value):
    base = _z(value, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z value
def sfe_f097_specialist_fund_exposure_z_21d_accel_v138_signal(value):
    base = _z(value, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z value
def sfe_f097_specialist_fund_exposure_z_63d_accel_v139_signal(value):
    base = _z(value, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z value
def sfe_f097_specialist_fund_exposure_z_63d_accel_v140_signal(value):
    base = _z(value, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z value
def sfe_f097_specialist_fund_exposure_z_63d_accel_v141_signal(value):
    base = _z(value, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z value
def sfe_f097_specialist_fund_exposure_z_126d_accel_v142_signal(value):
    base = _z(value, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z value
def sfe_f097_specialist_fund_exposure_z_126d_accel_v143_signal(value):
    base = _z(value, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z value
def sfe_f097_specialist_fund_exposure_z_126d_accel_v144_signal(value):
    base = _z(value, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z value
def sfe_f097_specialist_fund_exposure_z_252d_accel_v145_signal(value):
    base = _z(value, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z value
def sfe_f097_specialist_fund_exposure_z_252d_accel_v146_signal(value):
    base = _z(value, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z value
def sfe_f097_specialist_fund_exposure_z_252d_accel_v147_signal(value):
    base = _z(value, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z value
def sfe_f097_specialist_fund_exposure_z_504d_accel_v148_signal(value):
    base = _z(value, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z value
def sfe_f097_specialist_fund_exposure_z_504d_accel_v149_signal(value):
    base = _z(value, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z value
def sfe_f097_specialist_fund_exposure_z_504d_accel_v150_signal(value):
    base = _z(value, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
