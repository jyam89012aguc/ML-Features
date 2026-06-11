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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f083_lst(isdelisted_flag):
    return isdelisted_flag.astype(float)


# 21d mean of delisted_flag scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisted_flag_mean_21d_base_v001_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of delisted_flag scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisted_flag_mean_63d_base_v002_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of delisted_flag scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisted_flag_mean_126d_base_v003_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of delisted_flag scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisted_flag_mean_252d_base_v004_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of delisted_flag scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisted_flag_mean_504d_base_v005_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of quarters_public scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_mean_21d_base_v006_signal(quarters_public, closeadj):
    base = quarters_public
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of quarters_public scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_mean_63d_base_v007_signal(quarters_public, closeadj):
    base = quarters_public
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of quarters_public scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_mean_126d_base_v008_signal(quarters_public, closeadj):
    base = quarters_public
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of quarters_public scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_mean_252d_base_v009_signal(quarters_public, closeadj):
    base = quarters_public
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of quarters_public scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_mean_504d_base_v010_signal(quarters_public, closeadj):
    base = quarters_public
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of days_to_lastprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_mean_21d_base_v011_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of days_to_lastprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_mean_63d_base_v012_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of days_to_lastprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_mean_126d_base_v013_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of days_to_lastprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_mean_252d_base_v014_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of days_to_lastprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_mean_504d_base_v015_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of days_since_firstprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_mean_21d_base_v016_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of days_since_firstprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_mean_63d_base_v017_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of days_since_firstprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_mean_126d_base_v018_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of days_since_firstprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_mean_252d_base_v019_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of days_since_firstprice scaled by closeadj
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_mean_504d_base_v020_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of quarters_public_log scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_log_mean_21d_base_v021_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of quarters_public_log scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_log_mean_63d_base_v022_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of quarters_public_log scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_log_mean_126d_base_v023_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of quarters_public_log scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_log_mean_252d_base_v024_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of quarters_public_log scaled by closeadj
def f083lsd_f083_listing_status_and_dates_quarters_public_log_mean_504d_base_v025_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of delisting_warning scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisting_warning_mean_21d_base_v026_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of delisting_warning scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisting_warning_mean_63d_base_v027_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of delisting_warning scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisting_warning_mean_126d_base_v028_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of delisting_warning scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisting_warning_mean_252d_base_v029_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of delisting_warning scaled by closeadj
def f083lsd_f083_listing_status_and_dates_delisting_warning_mean_504d_base_v030_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of seasoned_5y scaled by closeadj
def f083lsd_f083_listing_status_and_dates_seasoned_5y_mean_21d_base_v031_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of seasoned_5y scaled by closeadj
def f083lsd_f083_listing_status_and_dates_seasoned_5y_mean_63d_base_v032_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of seasoned_5y scaled by closeadj
def f083lsd_f083_listing_status_and_dates_seasoned_5y_mean_126d_base_v033_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of seasoned_5y scaled by closeadj
def f083lsd_f083_listing_status_and_dates_seasoned_5y_mean_252d_base_v034_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of seasoned_5y scaled by closeadj
def f083lsd_f083_listing_status_and_dates_seasoned_5y_mean_504d_base_v035_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_median_63d_base_v036_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_median_252d_base_v037_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_median_504d_base_v038_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_median_63d_base_v039_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_median_252d_base_v040_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_median_504d_base_v041_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_median_63d_base_v042_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_median_252d_base_v043_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_median_504d_base_v044_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_median_63d_base_v045_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_median_252d_base_v046_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_median_504d_base_v047_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_median_63d_base_v048_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_median_252d_base_v049_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_median_504d_base_v050_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_median_63d_base_v051_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_median_252d_base_v052_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_median_504d_base_v053_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_median_63d_base_v054_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_median_252d_base_v055_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_median_504d_base_v056_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_rmax_252d_base_v057_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_rmax_504d_base_v058_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_rmax_252d_base_v059_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_rmax_504d_base_v060_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_rmax_252d_base_v061_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_rmax_504d_base_v062_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_rmax_252d_base_v063_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_rmax_504d_base_v064_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_rmax_252d_base_v065_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_rmax_504d_base_v066_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_rmax_252d_base_v067_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_rmax_504d_base_v068_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_rmax_252d_base_v069_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_rmax_504d_base_v070_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_rmin_252d_base_v071_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_rmin_504d_base_v072_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_rmin_252d_base_v073_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_rmin_504d_base_v074_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_rmin_252d_base_v075_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

