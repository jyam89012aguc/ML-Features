"""Family f083 - Listing lifecycle and delisting context (Security Master and Universe) | Sharadar tables: TICKERS | fields: isdelisted, firstpricedate, lastpricedate, firstquarter, lastquarter | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw listingage
def lsad_f083_listing_status_and_dates_raw_21d_slope_v001_signal(listingage, closeadj):
    base = _mean(listingage, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw listingage
def lsad_f083_listing_status_and_dates_raw_21d_slope_v002_signal(listingage, closeadj):
    base = _mean(listingage, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw listingage
def lsad_f083_listing_status_and_dates_raw_21d_slope_v003_signal(listingage, closeadj):
    base = _mean(listingage, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw listingage
def lsad_f083_listing_status_and_dates_raw_63d_slope_v004_signal(listingage, closeadj):
    base = _mean(listingage, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw listingage
def lsad_f083_listing_status_and_dates_raw_63d_slope_v005_signal(listingage, closeadj):
    base = _mean(listingage, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw listingage
def lsad_f083_listing_status_and_dates_raw_63d_slope_v006_signal(listingage, closeadj):
    base = _mean(listingage, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw listingage
def lsad_f083_listing_status_and_dates_raw_126d_slope_v007_signal(listingage, closeadj):
    base = _mean(listingage, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw listingage
def lsad_f083_listing_status_and_dates_raw_126d_slope_v008_signal(listingage, closeadj):
    base = _mean(listingage, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw listingage
def lsad_f083_listing_status_and_dates_raw_126d_slope_v009_signal(listingage, closeadj):
    base = _mean(listingage, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw listingage
def lsad_f083_listing_status_and_dates_raw_252d_slope_v010_signal(listingage, closeadj):
    base = _mean(listingage, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw listingage
def lsad_f083_listing_status_and_dates_raw_252d_slope_v011_signal(listingage, closeadj):
    base = _mean(listingage, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw listingage
def lsad_f083_listing_status_and_dates_raw_252d_slope_v012_signal(listingage, closeadj):
    base = _mean(listingage, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw listingage
def lsad_f083_listing_status_and_dates_raw_504d_slope_v013_signal(listingage, closeadj):
    base = _mean(listingage, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw listingage
def lsad_f083_listing_status_and_dates_raw_504d_slope_v014_signal(listingage, closeadj):
    base = _mean(listingage, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw listingage
def lsad_f083_listing_status_and_dates_raw_504d_slope_v015_signal(listingage, closeadj):
    base = _mean(listingage, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log listingage
def lsad_f083_listing_status_and_dates_log_21d_slope_v016_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log listingage
def lsad_f083_listing_status_and_dates_log_21d_slope_v017_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log listingage
def lsad_f083_listing_status_and_dates_log_21d_slope_v018_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log listingage
def lsad_f083_listing_status_and_dates_log_63d_slope_v019_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log listingage
def lsad_f083_listing_status_and_dates_log_63d_slope_v020_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log listingage
def lsad_f083_listing_status_and_dates_log_63d_slope_v021_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log listingage
def lsad_f083_listing_status_and_dates_log_126d_slope_v022_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log listingage
def lsad_f083_listing_status_and_dates_log_126d_slope_v023_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log listingage
def lsad_f083_listing_status_and_dates_log_126d_slope_v024_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log listingage
def lsad_f083_listing_status_and_dates_log_252d_slope_v025_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log listingage
def lsad_f083_listing_status_and_dates_log_252d_slope_v026_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log listingage
def lsad_f083_listing_status_and_dates_log_252d_slope_v027_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log listingage
def lsad_f083_listing_status_and_dates_log_504d_slope_v028_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log listingage
def lsad_f083_listing_status_and_dates_log_504d_slope_v029_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log listingage
def lsad_f083_listing_status_and_dates_log_504d_slope_v030_signal(listingage, closeadj):
    base = _mean(_listing_status_and_dates_log(listingage), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_21d_slope_v031_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_21d_slope_v032_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_21d_slope_v033_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_63d_slope_v034_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_63d_slope_v035_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_63d_slope_v036_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_126d_slope_v037_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_126d_slope_v038_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_126d_slope_v039_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_252d_slope_v040_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_252d_slope_v041_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_252d_slope_v042_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_504d_slope_v043_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_504d_slope_v044_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare listingage
def lsad_f083_listing_status_and_dates_pershare_504d_slope_v045_signal(listingage, sharesbas, closeadj):
    base = _mean(_listing_status_and_dates_per_share(listingage, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_21d_slope_v046_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_21d_slope_v047_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_21d_slope_v048_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_63d_slope_v049_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_63d_slope_v050_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_63d_slope_v051_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_126d_slope_v052_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_126d_slope_v053_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_126d_slope_v054_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_252d_slope_v055_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_252d_slope_v056_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_252d_slope_v057_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_504d_slope_v058_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_504d_slope_v059_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets listingage
def lsad_f083_listing_status_and_dates_per_assets_504d_slope_v060_signal(listingage, assets):
    base = _mean(_listing_status_and_dates_scaled(listingage, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_21d_slope_v061_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_21d_slope_v062_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_21d_slope_v063_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_63d_slope_v064_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_63d_slope_v065_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_63d_slope_v066_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_126d_slope_v067_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_126d_slope_v068_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_126d_slope_v069_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_252d_slope_v070_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_252d_slope_v071_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_252d_slope_v072_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_504d_slope_v073_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_504d_slope_v074_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap listingage
def lsad_f083_listing_status_and_dates_per_marketcap_504d_slope_v075_signal(listingage, marketcap):
    base = _mean(_listing_status_and_dates_scaled(listingage, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_21d_slope_v076_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_21d_slope_v077_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_21d_slope_v078_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_63d_slope_v079_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_63d_slope_v080_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_63d_slope_v081_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_126d_slope_v082_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_126d_slope_v083_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_126d_slope_v084_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_252d_slope_v085_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_252d_slope_v086_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_252d_slope_v087_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_504d_slope_v088_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_504d_slope_v089_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity listingage
def lsad_f083_listing_status_and_dates_per_equity_504d_slope_v090_signal(listingage, equity):
    base = _mean(_listing_status_and_dates_scaled(listingage, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std listingage
def lsad_f083_listing_status_and_dates_std_21d_slope_v091_signal(listingage, closeadj):
    base = _std(listingage, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std listingage
def lsad_f083_listing_status_and_dates_std_21d_slope_v092_signal(listingage, closeadj):
    base = _std(listingage, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std listingage
def lsad_f083_listing_status_and_dates_std_21d_slope_v093_signal(listingage, closeadj):
    base = _std(listingage, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std listingage
def lsad_f083_listing_status_and_dates_std_63d_slope_v094_signal(listingage, closeadj):
    base = _std(listingage, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std listingage
def lsad_f083_listing_status_and_dates_std_63d_slope_v095_signal(listingage, closeadj):
    base = _std(listingage, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std listingage
def lsad_f083_listing_status_and_dates_std_63d_slope_v096_signal(listingage, closeadj):
    base = _std(listingage, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std listingage
def lsad_f083_listing_status_and_dates_std_126d_slope_v097_signal(listingage, closeadj):
    base = _std(listingage, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std listingage
def lsad_f083_listing_status_and_dates_std_126d_slope_v098_signal(listingage, closeadj):
    base = _std(listingage, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std listingage
def lsad_f083_listing_status_and_dates_std_126d_slope_v099_signal(listingage, closeadj):
    base = _std(listingage, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std listingage
def lsad_f083_listing_status_and_dates_std_252d_slope_v100_signal(listingage, closeadj):
    base = _std(listingage, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std listingage
def lsad_f083_listing_status_and_dates_std_252d_slope_v101_signal(listingage, closeadj):
    base = _std(listingage, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std listingage
def lsad_f083_listing_status_and_dates_std_252d_slope_v102_signal(listingage, closeadj):
    base = _std(listingage, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std listingage
def lsad_f083_listing_status_and_dates_std_504d_slope_v103_signal(listingage, closeadj):
    base = _std(listingage, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std listingage
def lsad_f083_listing_status_and_dates_std_504d_slope_v104_signal(listingage, closeadj):
    base = _std(listingage, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std listingage
def lsad_f083_listing_status_and_dates_std_504d_slope_v105_signal(listingage, closeadj):
    base = _std(listingage, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_21d_slope_v106_signal(listingage, closeadj):
    base = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_21d_slope_v107_signal(listingage, closeadj):
    base = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_21d_slope_v108_signal(listingage, closeadj):
    base = listingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_63d_slope_v109_signal(listingage, closeadj):
    base = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_63d_slope_v110_signal(listingage, closeadj):
    base = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_63d_slope_v111_signal(listingage, closeadj):
    base = listingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_126d_slope_v112_signal(listingage, closeadj):
    base = listingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_126d_slope_v113_signal(listingage, closeadj):
    base = listingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_126d_slope_v114_signal(listingage, closeadj):
    base = listingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_252d_slope_v115_signal(listingage, closeadj):
    base = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_252d_slope_v116_signal(listingage, closeadj):
    base = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_252d_slope_v117_signal(listingage, closeadj):
    base = listingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_504d_slope_v118_signal(listingage, closeadj):
    base = listingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_504d_slope_v119_signal(listingage, closeadj):
    base = listingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm listingage
def lsad_f083_listing_status_and_dates_ewm_504d_slope_v120_signal(listingage, closeadj):
    base = listingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq listingage
def lsad_f083_listing_status_and_dates_sq_21d_slope_v121_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq listingage
def lsad_f083_listing_status_and_dates_sq_21d_slope_v122_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq listingage
def lsad_f083_listing_status_and_dates_sq_21d_slope_v123_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq listingage
def lsad_f083_listing_status_and_dates_sq_63d_slope_v124_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq listingage
def lsad_f083_listing_status_and_dates_sq_63d_slope_v125_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq listingage
def lsad_f083_listing_status_and_dates_sq_63d_slope_v126_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq listingage
def lsad_f083_listing_status_and_dates_sq_126d_slope_v127_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq listingage
def lsad_f083_listing_status_and_dates_sq_126d_slope_v128_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq listingage
def lsad_f083_listing_status_and_dates_sq_126d_slope_v129_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq listingage
def lsad_f083_listing_status_and_dates_sq_252d_slope_v130_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq listingage
def lsad_f083_listing_status_and_dates_sq_252d_slope_v131_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq listingage
def lsad_f083_listing_status_and_dates_sq_252d_slope_v132_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq listingage
def lsad_f083_listing_status_and_dates_sq_504d_slope_v133_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq listingage
def lsad_f083_listing_status_and_dates_sq_504d_slope_v134_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq listingage
def lsad_f083_listing_status_and_dates_sq_504d_slope_v135_signal(listingage, closeadj):
    base = _mean(listingage * listingage, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z listingage
def lsad_f083_listing_status_and_dates_z_21d_slope_v136_signal(listingage):
    base = _z(listingage, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z listingage
def lsad_f083_listing_status_and_dates_z_21d_slope_v137_signal(listingage):
    base = _z(listingage, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z listingage
def lsad_f083_listing_status_and_dates_z_21d_slope_v138_signal(listingage):
    base = _z(listingage, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z listingage
def lsad_f083_listing_status_and_dates_z_63d_slope_v139_signal(listingage):
    base = _z(listingage, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z listingage
def lsad_f083_listing_status_and_dates_z_63d_slope_v140_signal(listingage):
    base = _z(listingage, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z listingage
def lsad_f083_listing_status_and_dates_z_63d_slope_v141_signal(listingage):
    base = _z(listingage, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z listingage
def lsad_f083_listing_status_and_dates_z_126d_slope_v142_signal(listingage):
    base = _z(listingage, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z listingage
def lsad_f083_listing_status_and_dates_z_126d_slope_v143_signal(listingage):
    base = _z(listingage, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z listingage
def lsad_f083_listing_status_and_dates_z_126d_slope_v144_signal(listingage):
    base = _z(listingage, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z listingage
def lsad_f083_listing_status_and_dates_z_252d_slope_v145_signal(listingage):
    base = _z(listingage, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z listingage
def lsad_f083_listing_status_and_dates_z_252d_slope_v146_signal(listingage):
    base = _z(listingage, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z listingage
def lsad_f083_listing_status_and_dates_z_252d_slope_v147_signal(listingage):
    base = _z(listingage, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z listingage
def lsad_f083_listing_status_and_dates_z_504d_slope_v148_signal(listingage):
    base = _z(listingage, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z listingage
def lsad_f083_listing_status_and_dates_z_504d_slope_v149_signal(listingage):
    base = _z(listingage, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z listingage
def lsad_f083_listing_status_and_dates_z_504d_slope_v150_signal(listingage):
    base = _z(listingage, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
