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


# 21d acceleration of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_accel_21d_3d_v001_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_accel_63d_3d_v002_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_accel_126d_3d_v003_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_accel_252d_3d_v004_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_accel_21d_3d_v005_signal(quarters_public, closeadj):
    base = quarters_public
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_accel_63d_3d_v006_signal(quarters_public, closeadj):
    base = quarters_public
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_accel_126d_3d_v007_signal(quarters_public, closeadj):
    base = quarters_public
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_accel_252d_3d_v008_signal(quarters_public, closeadj):
    base = quarters_public
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_accel_21d_3d_v009_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_accel_63d_3d_v010_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_accel_126d_3d_v011_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_accel_252d_3d_v012_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_accel_21d_3d_v013_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_accel_63d_3d_v014_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_accel_126d_3d_v015_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_accel_252d_3d_v016_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_accel_21d_3d_v017_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_accel_63d_3d_v018_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_accel_126d_3d_v019_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_accel_252d_3d_v020_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_accel_21d_3d_v021_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_accel_63d_3d_v022_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_accel_126d_3d_v023_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_accel_252d_3d_v024_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_accel_21d_3d_v025_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_accel_63d_3d_v026_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_accel_126d_3d_v027_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_accel_252d_3d_v028_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slopez_21d_z126_3d_v029_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slopez_63d_z252_3d_v030_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slopez_126d_z252_3d_v031_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_slopez_252d_z504_3d_v032_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slopez_21d_z126_3d_v033_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slopez_63d_z252_3d_v034_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slopez_126d_z252_3d_v035_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_slopez_252d_z504_3d_v036_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slopez_21d_z126_3d_v037_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slopez_63d_z252_3d_v038_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slopez_126d_z252_3d_v039_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_slopez_252d_z504_3d_v040_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slopez_21d_z126_3d_v041_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slopez_63d_z252_3d_v042_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slopez_126d_z252_3d_v043_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_slopez_252d_z504_3d_v044_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slopez_21d_z126_3d_v045_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slopez_63d_z252_3d_v046_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slopez_126d_z252_3d_v047_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_slopez_252d_z504_3d_v048_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slopez_21d_z126_3d_v049_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slopez_63d_z252_3d_v050_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slopez_126d_z252_3d_v051_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_slopez_252d_z504_3d_v052_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slopez_21d_z126_3d_v053_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slopez_63d_z252_3d_v054_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slopez_126d_z252_3d_v055_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_slopez_252d_z504_3d_v056_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_jerk_21d_3d_v057_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_jerk_63d_3d_v058_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_jerk_126d_3d_v059_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_jerk_21d_3d_v060_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_jerk_63d_3d_v061_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_jerk_126d_3d_v062_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_jerk_21d_3d_v063_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_jerk_63d_3d_v064_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_jerk_126d_3d_v065_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_jerk_21d_3d_v066_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_jerk_63d_3d_v067_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_jerk_126d_3d_v068_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_jerk_21d_3d_v069_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_jerk_63d_3d_v070_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_jerk_126d_3d_v071_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_jerk_21d_3d_v072_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_jerk_63d_3d_v073_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_jerk_126d_3d_v074_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_jerk_21d_3d_v075_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_jerk_63d_3d_v076_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_jerk_126d_3d_v077_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of delisted_flag smoothed over 252d
def f083lsd_f083_listing_status_and_dates_delisted_flag_smoothaccel_63d_sm252_3d_v078_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of delisted_flag smoothed over 504d
def f083lsd_f083_listing_status_and_dates_delisted_flag_smoothaccel_252d_sm504_3d_v079_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of quarters_public smoothed over 252d
def f083lsd_f083_listing_status_and_dates_quarters_public_smoothaccel_63d_sm252_3d_v080_signal(quarters_public, closeadj):
    base = quarters_public
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of quarters_public smoothed over 504d
def f083lsd_f083_listing_status_and_dates_quarters_public_smoothaccel_252d_sm504_3d_v081_signal(quarters_public, closeadj):
    base = quarters_public
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of days_to_lastprice smoothed over 252d
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_smoothaccel_63d_sm252_3d_v082_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of days_to_lastprice smoothed over 504d
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_smoothaccel_252d_sm504_3d_v083_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of days_since_firstprice smoothed over 252d
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_smoothaccel_63d_sm252_3d_v084_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of days_since_firstprice smoothed over 504d
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_smoothaccel_252d_sm504_3d_v085_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of quarters_public_log smoothed over 252d
def f083lsd_f083_listing_status_and_dates_quarters_public_log_smoothaccel_63d_sm252_3d_v086_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of quarters_public_log smoothed over 504d
def f083lsd_f083_listing_status_and_dates_quarters_public_log_smoothaccel_252d_sm504_3d_v087_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of delisting_warning smoothed over 252d
def f083lsd_f083_listing_status_and_dates_delisting_warning_smoothaccel_63d_sm252_3d_v088_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of delisting_warning smoothed over 504d
def f083lsd_f083_listing_status_and_dates_delisting_warning_smoothaccel_252d_sm504_3d_v089_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of seasoned_5y smoothed over 252d
def f083lsd_f083_listing_status_and_dates_seasoned_5y_smoothaccel_63d_sm252_3d_v090_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of seasoned_5y smoothed over 504d
def f083lsd_f083_listing_status_and_dates_seasoned_5y_smoothaccel_252d_sm504_3d_v091_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_accelz_21d_z252_3d_v092_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_accelz_63d_z504_3d_v093_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_accelz_21d_z252_3d_v094_signal(quarters_public, closeadj):
    base = quarters_public
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_accelz_63d_z504_3d_v095_signal(quarters_public, closeadj):
    base = quarters_public
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_accelz_21d_z252_3d_v096_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_accelz_63d_z504_3d_v097_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_accelz_21d_z252_3d_v098_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_accelz_63d_z504_3d_v099_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_accelz_21d_z252_3d_v100_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_accelz_63d_z504_3d_v101_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_accelz_21d_z252_3d_v102_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_accelz_63d_z504_3d_v103_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_accelz_21d_z252_3d_v104_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_accelz_63d_z504_3d_v105_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in delisted_flag (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_delisted_flag_signflip_63d_3d_v106_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in delisted_flag (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_delisted_flag_signflip_252d_3d_v107_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in quarters_public (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_quarters_public_signflip_63d_3d_v108_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in quarters_public (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_quarters_public_signflip_252d_3d_v109_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in days_to_lastprice (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_signflip_63d_3d_v110_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in days_to_lastprice (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_signflip_252d_3d_v111_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in days_since_firstprice (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_signflip_63d_3d_v112_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in days_since_firstprice (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_signflip_252d_3d_v113_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in quarters_public_log (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_quarters_public_log_signflip_63d_3d_v114_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in quarters_public_log (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_quarters_public_log_signflip_252d_3d_v115_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in delisting_warning (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_delisting_warning_signflip_63d_3d_v116_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in delisting_warning (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_delisting_warning_signflip_252d_3d_v117_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in seasoned_5y (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_seasoned_5y_signflip_63d_3d_v118_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in seasoned_5y (raw count, no price scaling)
def f083lsd_f083_listing_status_and_dates_seasoned_5y_signflip_252d_3d_v119_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of delisted_flag normalized by 252d range
def f083lsd_f083_listing_status_and_dates_delisted_flag_rngaccel_63d_r252_3d_v120_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of delisted_flag normalized by 504d range
def f083lsd_f083_listing_status_and_dates_delisted_flag_rngaccel_252d_r504_3d_v121_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quarters_public normalized by 252d range
def f083lsd_f083_listing_status_and_dates_quarters_public_rngaccel_63d_r252_3d_v122_signal(quarters_public, closeadj):
    base = quarters_public
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quarters_public normalized by 504d range
def f083lsd_f083_listing_status_and_dates_quarters_public_rngaccel_252d_r504_3d_v123_signal(quarters_public, closeadj):
    base = quarters_public
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of days_to_lastprice normalized by 252d range
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_rngaccel_63d_r252_3d_v124_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of days_to_lastprice normalized by 504d range
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_rngaccel_252d_r504_3d_v125_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of days_since_firstprice normalized by 252d range
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_rngaccel_63d_r252_3d_v126_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of days_since_firstprice normalized by 504d range
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_rngaccel_252d_r504_3d_v127_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of quarters_public_log normalized by 252d range
def f083lsd_f083_listing_status_and_dates_quarters_public_log_rngaccel_63d_r252_3d_v128_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of quarters_public_log normalized by 504d range
def f083lsd_f083_listing_status_and_dates_quarters_public_log_rngaccel_252d_r504_3d_v129_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of delisting_warning normalized by 252d range
def f083lsd_f083_listing_status_and_dates_delisting_warning_rngaccel_63d_r252_3d_v130_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of delisting_warning normalized by 504d range
def f083lsd_f083_listing_status_and_dates_delisting_warning_rngaccel_252d_r504_3d_v131_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of seasoned_5y normalized by 252d range
def f083lsd_f083_listing_status_and_dates_seasoned_5y_rngaccel_63d_r252_3d_v132_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of seasoned_5y normalized by 504d range
def f083lsd_f083_listing_status_and_dates_seasoned_5y_rngaccel_252d_r504_3d_v133_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_cumslope_21d_3d_v134_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_cumslope_63d_3d_v135_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_cumslope_252d_3d_v136_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_cumslope_21d_3d_v137_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_cumslope_63d_3d_v138_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_cumslope_252d_3d_v139_signal(quarters_public, closeadj):
    base = quarters_public
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_cumslope_21d_3d_v140_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_cumslope_63d_3d_v141_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_cumslope_252d_3d_v142_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_cumslope_21d_3d_v143_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_cumslope_63d_3d_v144_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_cumslope_252d_3d_v145_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_cumslope_21d_3d_v146_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_cumslope_63d_3d_v147_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_cumslope_252d_3d_v148_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_cumslope_21d_3d_v149_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_cumslope_63d_3d_v150_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

