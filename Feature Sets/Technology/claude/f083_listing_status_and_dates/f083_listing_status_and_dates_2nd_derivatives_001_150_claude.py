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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f083_lst(isdelisted_flag):
    return isdelisted_flag.astype(float)


# 21d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slope_21d_2d_v001_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slope_63d_2d_v002_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slope_126d_2d_v003_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slope_252d_2d_v004_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slope_504d_2d_v005_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slope_21d_2d_v006_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slope_63d_2d_v007_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slope_126d_2d_v008_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slope_252d_2d_v009_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slope_504d_2d_v010_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slope_21d_2d_v011_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slope_63d_2d_v012_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slope_126d_2d_v013_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slope_252d_2d_v014_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slope_504d_2d_v015_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slope_21d_2d_v016_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slope_63d_2d_v017_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slope_126d_2d_v018_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slope_252d_2d_v019_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slope_504d_2d_v020_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slope_21d_2d_v021_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slope_63d_2d_v022_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slope_126d_2d_v023_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slope_252d_2d_v024_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slope_504d_2d_v025_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slope_21d_2d_v026_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slope_63d_2d_v027_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slope_126d_2d_v028_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slope_252d_2d_v029_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slope_504d_2d_v030_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slope_21d_2d_v031_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slope_63d_2d_v032_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slope_126d_2d_v033_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slope_252d_2d_v034_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slope_504d_2d_v035_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sm21_sl21_2d_v036_signal(isdelisted_flag, closeadj):
    base = _mean(_f083_lst(isdelisted_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sm63_sl21_2d_v037_signal(isdelisted_flag, closeadj):
    base = _mean(_f083_lst(isdelisted_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sm63_sl63_2d_v038_signal(isdelisted_flag, closeadj):
    base = _mean(_f083_lst(isdelisted_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sm252_sl63_2d_v039_signal(isdelisted_flag, closeadj):
    base = _mean(_f083_lst(isdelisted_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sm252_sl126_2d_v040_signal(isdelisted_flag, closeadj):
    base = _mean(_f083_lst(isdelisted_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sm21_sl21_2d_v041_signal(quarters_public, closeadj):
    base = _mean(quarters_public, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sm63_sl21_2d_v042_signal(quarters_public, closeadj):
    base = _mean(quarters_public, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sm63_sl63_2d_v043_signal(quarters_public, closeadj):
    base = _mean(quarters_public, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sm252_sl63_2d_v044_signal(quarters_public, closeadj):
    base = _mean(quarters_public, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sm252_sl126_2d_v045_signal(quarters_public, closeadj):
    base = _mean(quarters_public, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sm21_sl21_2d_v046_signal(days_to_lastprice, closeadj):
    base = _mean(days_to_lastprice, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sm63_sl21_2d_v047_signal(days_to_lastprice, closeadj):
    base = _mean(days_to_lastprice, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sm63_sl63_2d_v048_signal(days_to_lastprice, closeadj):
    base = _mean(days_to_lastprice, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sm252_sl63_2d_v049_signal(days_to_lastprice, closeadj):
    base = _mean(days_to_lastprice, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sm252_sl126_2d_v050_signal(days_to_lastprice, closeadj):
    base = _mean(days_to_lastprice, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sm21_sl21_2d_v051_signal(days_since_firstprice, closeadj):
    base = _mean(days_since_firstprice, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sm63_sl21_2d_v052_signal(days_since_firstprice, closeadj):
    base = _mean(days_since_firstprice, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sm63_sl63_2d_v053_signal(days_since_firstprice, closeadj):
    base = _mean(days_since_firstprice, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sm252_sl63_2d_v054_signal(days_since_firstprice, closeadj):
    base = _mean(days_since_firstprice, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sm252_sl126_2d_v055_signal(days_since_firstprice, closeadj):
    base = _mean(days_since_firstprice, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sm21_sl21_2d_v056_signal(quarters_public, closeadj):
    base = _mean(np.log(quarters_public.abs().replace(0, np.nan) + 1), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sm63_sl21_2d_v057_signal(quarters_public, closeadj):
    base = _mean(np.log(quarters_public.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sm63_sl63_2d_v058_signal(quarters_public, closeadj):
    base = _mean(np.log(quarters_public.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sm252_sl63_2d_v059_signal(quarters_public, closeadj):
    base = _mean(np.log(quarters_public.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sm252_sl126_2d_v060_signal(quarters_public, closeadj):
    base = _mean(np.log(quarters_public.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sm21_sl21_2d_v061_signal(days_to_lastprice, closeadj):
    base = _mean((days_to_lastprice < 90).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sm63_sl21_2d_v062_signal(days_to_lastprice, closeadj):
    base = _mean((days_to_lastprice < 90).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sm63_sl63_2d_v063_signal(days_to_lastprice, closeadj):
    base = _mean((days_to_lastprice < 90).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sm252_sl63_2d_v064_signal(days_to_lastprice, closeadj):
    base = _mean((days_to_lastprice < 90).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sm252_sl126_2d_v065_signal(days_to_lastprice, closeadj):
    base = _mean((days_to_lastprice < 90).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sm21_sl21_2d_v066_signal(days_since_firstprice, closeadj):
    base = _mean((days_since_firstprice > 1825).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sm63_sl21_2d_v067_signal(days_since_firstprice, closeadj):
    base = _mean((days_since_firstprice > 1825).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sm63_sl63_2d_v068_signal(days_since_firstprice, closeadj):
    base = _mean((days_since_firstprice > 1825).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sm252_sl63_2d_v069_signal(days_since_firstprice, closeadj):
    base = _mean((days_since_firstprice > 1825).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sm252_sl126_2d_v070_signal(days_since_firstprice, closeadj):
    base = _mean((days_since_firstprice > 1825).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_pctslope_21d_2d_v071_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_pctslope_63d_2d_v072_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_pctslope_252d_2d_v073_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_pctslope_21d_2d_v074_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_pctslope_63d_2d_v075_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_pctslope_252d_2d_v076_signal(quarters_public, closeadj):
    base = quarters_public
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_pctslope_21d_2d_v077_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_pctslope_63d_2d_v078_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_pctslope_252d_2d_v079_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_pctslope_21d_2d_v080_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_pctslope_63d_2d_v081_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_pctslope_252d_2d_v082_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_pctslope_21d_2d_v083_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_pctslope_63d_2d_v084_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_pctslope_252d_2d_v085_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_pctslope_21d_2d_v086_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_pctslope_63d_2d_v087_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_pctslope_252d_2d_v088_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_pctslope_21d_2d_v089_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_pctslope_63d_2d_v090_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_pctslope_252d_2d_v091_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sgnslope_21d_2d_v092_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sgnslope_63d_2d_v093_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_sgnslope_252d_2d_v094_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sgnslope_21d_2d_v095_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sgnslope_63d_2d_v096_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_sgnslope_252d_2d_v097_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sgnslope_21d_2d_v098_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sgnslope_63d_2d_v099_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_sgnslope_252d_2d_v100_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sgnslope_21d_2d_v101_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sgnslope_63d_2d_v102_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_sgnslope_252d_2d_v103_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sgnslope_21d_2d_v104_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sgnslope_63d_2d_v105_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_sgnslope_252d_2d_v106_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sgnslope_21d_2d_v107_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sgnslope_63d_2d_v108_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_sgnslope_252d_2d_v109_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sgnslope_21d_2d_v110_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sgnslope_63d_2d_v111_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_sgnslope_252d_2d_v112_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_logmagslope_21d_2d_v113_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_logmagslope_63d_2d_v114_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_logmagslope_252d_2d_v115_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_logmagslope_21d_2d_v116_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_logmagslope_63d_2d_v117_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_logmagslope_252d_2d_v118_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_logmagslope_21d_2d_v119_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_logmagslope_63d_2d_v120_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_logmagslope_252d_2d_v121_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_logmagslope_21d_2d_v122_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_logmagslope_63d_2d_v123_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_logmagslope_252d_2d_v124_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_logmagslope_21d_2d_v125_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_logmagslope_63d_2d_v126_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_logmagslope_252d_2d_v127_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_logmagslope_21d_2d_v128_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_logmagslope_63d_2d_v129_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_logmagslope_252d_2d_v130_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_logmagslope_21d_2d_v131_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_logmagslope_63d_2d_v132_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_logmagslope_252d_2d_v133_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|delisted_flag|
def f083lsd_f083_listing_status_and_dates_delisted_flag_logslope_63d_2d_v134_signal(isdelisted_flag, closeadj):
    base = np.log((_f083_lst(isdelisted_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|delisted_flag|
def f083lsd_f083_listing_status_and_dates_delisted_flag_logslope_252d_2d_v135_signal(isdelisted_flag, closeadj):
    base = np.log((_f083_lst(isdelisted_flag)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|quarters_public|
def f083lsd_f083_listing_status_and_dates_quarters_public_logslope_63d_2d_v136_signal(quarters_public, closeadj):
    base = np.log((quarters_public).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|quarters_public|
def f083lsd_f083_listing_status_and_dates_quarters_public_logslope_252d_2d_v137_signal(quarters_public, closeadj):
    base = np.log((quarters_public).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|days_to_lastprice|
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_logslope_63d_2d_v138_signal(days_to_lastprice, closeadj):
    base = np.log((days_to_lastprice).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|days_to_lastprice|
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_logslope_252d_2d_v139_signal(days_to_lastprice, closeadj):
    base = np.log((days_to_lastprice).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|days_since_firstprice|
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_logslope_63d_2d_v140_signal(days_since_firstprice, closeadj):
    base = np.log((days_since_firstprice).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|days_since_firstprice|
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_logslope_252d_2d_v141_signal(days_since_firstprice, closeadj):
    base = np.log((days_since_firstprice).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|quarters_public_log|
def f083lsd_f083_listing_status_and_dates_quarters_public_log_logslope_63d_2d_v142_signal(quarters_public, closeadj):
    base = np.log((np.log(quarters_public.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|quarters_public_log|
def f083lsd_f083_listing_status_and_dates_quarters_public_log_logslope_252d_2d_v143_signal(quarters_public, closeadj):
    base = np.log((np.log(quarters_public.abs().replace(0, np.nan) + 1)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|delisting_warning|
def f083lsd_f083_listing_status_and_dates_delisting_warning_logslope_63d_2d_v144_signal(days_to_lastprice, closeadj):
    base = np.log(((days_to_lastprice < 90).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|delisting_warning|
def f083lsd_f083_listing_status_and_dates_delisting_warning_logslope_252d_2d_v145_signal(days_to_lastprice, closeadj):
    base = np.log(((days_to_lastprice < 90).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|seasoned_5y|
def f083lsd_f083_listing_status_and_dates_seasoned_5y_logslope_63d_2d_v146_signal(days_since_firstprice, closeadj):
    base = np.log(((days_since_firstprice > 1825).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|seasoned_5y|
def f083lsd_f083_listing_status_and_dates_seasoned_5y_logslope_252d_2d_v147_signal(days_since_firstprice, closeadj):
    base = np.log(((days_since_firstprice > 1825).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

