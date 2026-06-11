"""Family f083 - Listing lifecycle and delisting context (Security Master and Universe) | Sharadar tables: TICKERS | fields: isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter | 3rd derivatives 001-150"""
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
def _listing_status_and_dates_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _listing_status_and_dates_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _listing_status_and_dates_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw listingage
def lsad_f083_listing_status_and_dates_raw_21d_accel_v001_signal(listingage, closeadj):
    base = _mean(listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw listingage
def lsad_f083_listing_status_and_dates_raw_21d_accel_v002_signal(listingage, closeadj):
    base = _mean(listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw listingage
def lsad_f083_listing_status_and_dates_raw_21d_accel_v003_signal(listingage, closeadj):
    base = _mean(listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw listingage
def lsad_f083_listing_status_and_dates_raw_63d_accel_v004_signal(listingage, closeadj):
    base = _mean(listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw listingage
def lsad_f083_listing_status_and_dates_raw_63d_accel_v005_signal(listingage, closeadj):
    base = _mean(listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw listingage
def lsad_f083_listing_status_and_dates_raw_63d_accel_v006_signal(listingage, closeadj):
    base = _mean(listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw listingage
def lsad_f083_listing_status_and_dates_raw_126d_accel_v007_signal(listingage, closeadj):
    base = _mean(listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw listingage
def lsad_f083_listing_status_and_dates_raw_126d_accel_v008_signal(listingage, closeadj):
    base = _mean(listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw listingage
def lsad_f083_listing_status_and_dates_raw_126d_accel_v009_signal(listingage, closeadj):
    base = _mean(listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw listingage
def lsad_f083_listing_status_and_dates_raw_252d_accel_v010_signal(listingage, closeadj):
    base = _mean(listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw listingage
def lsad_f083_listing_status_and_dates_raw_252d_accel_v011_signal(listingage, closeadj):
    base = _mean(listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw listingage
def lsad_f083_listing_status_and_dates_raw_252d_accel_v012_signal(listingage, closeadj):
    base = _mean(listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw listingage
def lsad_f083_listing_status_and_dates_raw_504d_accel_v013_signal(listingage, closeadj):
    base = _mean(listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw listingage
def lsad_f083_listing_status_and_dates_raw_504d_accel_v014_signal(listingage, closeadj):
    base = _mean(listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw listingage
def lsad_f083_listing_status_and_dates_raw_504d_accel_v015_signal(listingage, closeadj):
    base = _mean(listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log listingage
def lsad_f083_listing_status_and_dates_log_21d_accel_v016_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log listingage
def lsad_f083_listing_status_and_dates_log_21d_accel_v017_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log listingage
def lsad_f083_listing_status_and_dates_log_21d_accel_v018_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log listingage
def lsad_f083_listing_status_and_dates_log_63d_accel_v019_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log listingage
def lsad_f083_listing_status_and_dates_log_63d_accel_v020_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log listingage
def lsad_f083_listing_status_and_dates_log_63d_accel_v021_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log listingage
def lsad_f083_listing_status_and_dates_log_126d_accel_v022_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log listingage
def lsad_f083_listing_status_and_dates_log_126d_accel_v023_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log listingage
def lsad_f083_listing_status_and_dates_log_126d_accel_v024_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log listingage
def lsad_f083_listing_status_and_dates_log_252d_accel_v025_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log listingage
def lsad_f083_listing_status_and_dates_log_252d_accel_v026_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log listingage
def lsad_f083_listing_status_and_dates_log_252d_accel_v027_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log listingage
def lsad_f083_listing_status_and_dates_log_504d_accel_v028_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log listingage
def lsad_f083_listing_status_and_dates_log_504d_accel_v029_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log listingage
def lsad_f083_listing_status_and_dates_log_504d_accel_v030_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_21d_accel_v031_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_21d_accel_v032_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_21d_accel_v033_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_63d_accel_v034_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_63d_accel_v035_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_63d_accel_v036_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_126d_accel_v037_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_126d_accel_v038_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_126d_accel_v039_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_252d_accel_v040_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_252d_accel_v041_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_252d_accel_v042_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_504d_accel_v043_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_504d_accel_v044_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_504d_accel_v045_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_21d_accel_v046_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_21d_accel_v047_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_21d_accel_v048_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_63d_accel_v049_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_63d_accel_v050_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_63d_accel_v051_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_126d_accel_v052_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_126d_accel_v053_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_126d_accel_v054_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_252d_accel_v055_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_252d_accel_v056_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_252d_accel_v057_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_504d_accel_v058_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_504d_accel_v059_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_504d_accel_v060_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_21d_accel_v061_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_21d_accel_v062_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_21d_accel_v063_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_63d_accel_v064_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_63d_accel_v065_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_63d_accel_v066_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_126d_accel_v067_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_126d_accel_v068_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_126d_accel_v069_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_252d_accel_v070_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_252d_accel_v071_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_252d_accel_v072_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_504d_accel_v073_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_504d_accel_v074_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_504d_accel_v075_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_21d_accel_v076_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_21d_accel_v077_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_21d_accel_v078_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_63d_accel_v079_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_63d_accel_v080_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_63d_accel_v081_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_126d_accel_v082_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_126d_accel_v083_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_126d_accel_v084_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_252d_accel_v085_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_252d_accel_v086_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_252d_accel_v087_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_504d_accel_v088_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_504d_accel_v089_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_504d_accel_v090_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std listingage
def lsad_f083_listing_status_and_dates_std_21d_accel_v091_signal(listingage, closeadj):
    base = _std(listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std listingage
def lsad_f083_listing_status_and_dates_std_21d_accel_v092_signal(listingage, closeadj):
    base = _std(listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std listingage
def lsad_f083_listing_status_and_dates_std_21d_accel_v093_signal(listingage, closeadj):
    base = _std(listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std listingage
def lsad_f083_listing_status_and_dates_std_63d_accel_v094_signal(listingage, closeadj):
    base = _std(listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std listingage
def lsad_f083_listing_status_and_dates_std_63d_accel_v095_signal(listingage, closeadj):
    base = _std(listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std listingage
def lsad_f083_listing_status_and_dates_std_63d_accel_v096_signal(listingage, closeadj):
    base = _std(listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std listingage
def lsad_f083_listing_status_and_dates_std_126d_accel_v097_signal(listingage, closeadj):
    base = _std(listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std listingage
def lsad_f083_listing_status_and_dates_std_126d_accel_v098_signal(listingage, closeadj):
    base = _std(listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std listingage
def lsad_f083_listing_status_and_dates_std_126d_accel_v099_signal(listingage, closeadj):
    base = _std(listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std listingage
def lsad_f083_listing_status_and_dates_std_252d_accel_v100_signal(listingage, closeadj):
    base = _std(listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std listingage
def lsad_f083_listing_status_and_dates_std_252d_accel_v101_signal(listingage, closeadj):
    base = _std(listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std listingage
def lsad_f083_listing_status_and_dates_std_252d_accel_v102_signal(listingage, closeadj):
    base = _std(listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std listingage
def lsad_f083_listing_status_and_dates_std_504d_accel_v103_signal(listingage, closeadj):
    base = _std(listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std listingage
def lsad_f083_listing_status_and_dates_std_504d_accel_v104_signal(listingage, closeadj):
    base = _std(listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std listingage
def lsad_f083_listing_status_and_dates_std_504d_accel_v105_signal(listingage, closeadj):
    base = _std(listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_21d_accel_v106_signal(listingage, closeadj):
    base = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_21d_accel_v107_signal(listingage, closeadj):
    base = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_21d_accel_v108_signal(listingage, closeadj):
    base = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_63d_accel_v109_signal(listingage, closeadj):
    base = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_63d_accel_v110_signal(listingage, closeadj):
    base = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_63d_accel_v111_signal(listingage, closeadj):
    base = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_126d_accel_v112_signal(listingage, closeadj):
    base = listingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_126d_accel_v113_signal(listingage, closeadj):
    base = listingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_126d_accel_v114_signal(listingage, closeadj):
    base = listingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_252d_accel_v115_signal(listingage, closeadj):
    base = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_252d_accel_v116_signal(listingage, closeadj):
    base = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_252d_accel_v117_signal(listingage, closeadj):
    base = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_504d_accel_v118_signal(listingage, closeadj):
    base = listingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_504d_accel_v119_signal(listingage, closeadj):
    base = listingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_504d_accel_v120_signal(listingage, closeadj):
    base = listingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq listingage
def lsad_f083_listing_status_and_dates_sq_21d_accel_v121_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq listingage
def lsad_f083_listing_status_and_dates_sq_21d_accel_v122_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq listingage
def lsad_f083_listing_status_and_dates_sq_21d_accel_v123_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq listingage
def lsad_f083_listing_status_and_dates_sq_63d_accel_v124_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq listingage
def lsad_f083_listing_status_and_dates_sq_63d_accel_v125_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq listingage
def lsad_f083_listing_status_and_dates_sq_63d_accel_v126_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq listingage
def lsad_f083_listing_status_and_dates_sq_126d_accel_v127_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq listingage
def lsad_f083_listing_status_and_dates_sq_126d_accel_v128_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq listingage
def lsad_f083_listing_status_and_dates_sq_126d_accel_v129_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq listingage
def lsad_f083_listing_status_and_dates_sq_252d_accel_v130_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq listingage
def lsad_f083_listing_status_and_dates_sq_252d_accel_v131_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq listingage
def lsad_f083_listing_status_and_dates_sq_252d_accel_v132_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq listingage
def lsad_f083_listing_status_and_dates_sq_504d_accel_v133_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq listingage
def lsad_f083_listing_status_and_dates_sq_504d_accel_v134_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq listingage
def lsad_f083_listing_status_and_dates_sq_504d_accel_v135_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z listingage
def lsad_f083_listing_status_and_dates_z_21d_accel_v136_signal(listingage):
    base = _z(listingage, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z listingage
def lsad_f083_listing_status_and_dates_z_21d_accel_v137_signal(listingage):
    base = _z(listingage, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z listingage
def lsad_f083_listing_status_and_dates_z_21d_accel_v138_signal(listingage):
    base = _z(listingage, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z listingage
def lsad_f083_listing_status_and_dates_z_63d_accel_v139_signal(listingage):
    base = _z(listingage, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z listingage
def lsad_f083_listing_status_and_dates_z_63d_accel_v140_signal(listingage):
    base = _z(listingage, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z listingage
def lsad_f083_listing_status_and_dates_z_63d_accel_v141_signal(listingage):
    base = _z(listingage, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z listingage
def lsad_f083_listing_status_and_dates_z_126d_accel_v142_signal(listingage):
    base = _z(listingage, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z listingage
def lsad_f083_listing_status_and_dates_z_126d_accel_v143_signal(listingage):
    base = _z(listingage, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z listingage
def lsad_f083_listing_status_and_dates_z_126d_accel_v144_signal(listingage):
    base = _z(listingage, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z listingage
def lsad_f083_listing_status_and_dates_z_252d_accel_v145_signal(listingage):
    base = _z(listingage, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z listingage
def lsad_f083_listing_status_and_dates_z_252d_accel_v146_signal(listingage):
    base = _z(listingage, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z listingage
def lsad_f083_listing_status_and_dates_z_252d_accel_v147_signal(listingage):
    base = _z(listingage, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z listingage
def lsad_f083_listing_status_and_dates_z_504d_accel_v148_signal(listingage):
    base = _z(listingage, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z listingage
def lsad_f083_listing_status_and_dates_z_504d_accel_v149_signal(listingage):
    base = _z(listingage, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z listingage
def lsad_f083_listing_status_and_dates_z_504d_accel_v150_signal(listingage):
    base = _z(listingage, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
