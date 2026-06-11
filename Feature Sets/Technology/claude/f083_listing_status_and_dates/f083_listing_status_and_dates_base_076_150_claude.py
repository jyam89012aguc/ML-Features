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


# 63d z-score of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_z_63d_base_v076_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_z_126d_base_v077_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_z_252d_base_v078_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_z_504d_base_v079_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_z_63d_base_v080_signal(quarters_public, closeadj):
    base = quarters_public
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_z_126d_base_v081_signal(quarters_public, closeadj):
    base = quarters_public
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_z_252d_base_v082_signal(quarters_public, closeadj):
    base = quarters_public
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_z_504d_base_v083_signal(quarters_public, closeadj):
    base = quarters_public
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_z_63d_base_v084_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_z_126d_base_v085_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_z_252d_base_v086_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_z_504d_base_v087_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_z_63d_base_v088_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_z_126d_base_v089_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_z_252d_base_v090_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_z_504d_base_v091_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_z_63d_base_v092_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_z_126d_base_v093_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_z_252d_base_v094_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_z_504d_base_v095_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_z_63d_base_v096_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_z_126d_base_v097_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_z_252d_base_v098_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_z_504d_base_v099_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_z_63d_base_v100_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_z_126d_base_v101_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_z_252d_base_v102_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_z_504d_base_v103_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_distmax_252d_base_v104_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_distmax_504d_base_v105_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_distmax_252d_base_v106_signal(quarters_public, closeadj):
    base = quarters_public
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_distmax_504d_base_v107_signal(quarters_public, closeadj):
    base = quarters_public
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_distmax_252d_base_v108_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_distmax_504d_base_v109_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_distmax_252d_base_v110_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_distmax_504d_base_v111_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_distmax_252d_base_v112_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_distmax_504d_base_v113_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_distmax_252d_base_v114_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_distmax_504d_base_v115_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_distmax_252d_base_v116_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_distmax_504d_base_v117_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_distmed_126d_base_v118_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_distmed_252d_base_v119_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_distmed_504d_base_v120_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_distmed_126d_base_v121_signal(quarters_public, closeadj):
    base = quarters_public
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_distmed_252d_base_v122_signal(quarters_public, closeadj):
    base = quarters_public
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_distmed_504d_base_v123_signal(quarters_public, closeadj):
    base = quarters_public
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_distmed_126d_base_v124_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_distmed_252d_base_v125_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_distmed_504d_base_v126_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_distmed_126d_base_v127_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_distmed_252d_base_v128_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_distmed_504d_base_v129_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_distmed_126d_base_v130_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_distmed_252d_base_v131_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_distmed_504d_base_v132_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_distmed_126d_base_v133_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_distmed_252d_base_v134_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_distmed_504d_base_v135_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_distmed_126d_base_v136_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_distmed_252d_base_v137_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of seasoned_5y
def f083lsd_f083_listing_status_and_dates_seasoned_5y_distmed_504d_base_v138_signal(days_since_firstprice, closeadj):
    base = (days_since_firstprice > 1825).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_chg_63d_base_v139_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in delisted_flag
def f083lsd_f083_listing_status_and_dates_delisted_flag_chg_252d_base_v140_signal(isdelisted_flag, closeadj):
    base = _f083_lst(isdelisted_flag)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_chg_63d_base_v141_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in quarters_public
def f083lsd_f083_listing_status_and_dates_quarters_public_chg_252d_base_v142_signal(quarters_public, closeadj):
    base = quarters_public
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_chg_63d_base_v143_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in days_to_lastprice
def f083lsd_f083_listing_status_and_dates_days_to_lastprice_chg_252d_base_v144_signal(days_to_lastprice, closeadj):
    base = days_to_lastprice
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_chg_63d_base_v145_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in days_since_firstprice
def f083lsd_f083_listing_status_and_dates_days_since_firstprice_chg_252d_base_v146_signal(days_since_firstprice, closeadj):
    base = days_since_firstprice
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_chg_63d_base_v147_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in quarters_public_log
def f083lsd_f083_listing_status_and_dates_quarters_public_log_chg_252d_base_v148_signal(quarters_public, closeadj):
    base = np.log(quarters_public.abs().replace(0, np.nan) + 1)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_chg_63d_base_v149_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in delisting_warning
def f083lsd_f083_listing_status_and_dates_delisting_warning_chg_252d_base_v150_signal(days_to_lastprice, closeadj):
    base = (days_to_lastprice < 90).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

