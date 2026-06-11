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
def _f084_chg(ticker_change_count):
    return ticker_change_count


# 21d acceleration of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_accel_21d_3d_v001_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_accel_63d_3d_v002_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_accel_126d_3d_v003_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_accel_252d_3d_v004_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_accel_21d_3d_v005_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_accel_63d_3d_v006_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_accel_126d_3d_v007_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_accel_252d_3d_v008_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_accel_21d_3d_v009_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_accel_63d_3d_v010_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_accel_126d_3d_v011_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_accel_252d_3d_v012_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_accel_21d_3d_v013_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_accel_63d_3d_v014_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_accel_126d_3d_v015_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_accel_252d_3d_v016_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_accel_21d_3d_v017_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_accel_63d_3d_v018_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_accel_126d_3d_v019_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_accel_252d_3d_v020_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_accel_21d_3d_v021_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_accel_63d_3d_v022_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_accel_126d_3d_v023_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_accel_252d_3d_v024_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_accel_21d_3d_v025_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_accel_63d_3d_v026_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_accel_126d_3d_v027_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_accel_252d_3d_v028_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slopez_21d_z126_3d_v029_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slopez_63d_z252_3d_v030_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slopez_126d_z252_3d_v031_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_slopez_252d_z504_3d_v032_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slopez_21d_z126_3d_v033_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slopez_63d_z252_3d_v034_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slopez_126d_z252_3d_v035_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_slopez_252d_z504_3d_v036_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slopez_21d_z126_3d_v037_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slopez_63d_z252_3d_v038_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slopez_126d_z252_3d_v039_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_slopez_252d_z504_3d_v040_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slopez_21d_z126_3d_v041_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slopez_63d_z252_3d_v042_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slopez_126d_z252_3d_v043_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_slopez_252d_z504_3d_v044_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slopez_21d_z126_3d_v045_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slopez_63d_z252_3d_v046_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slopez_126d_z252_3d_v047_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_slopez_252d_z504_3d_v048_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slopez_21d_z126_3d_v049_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slopez_63d_z252_3d_v050_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slopez_126d_z252_3d_v051_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_slopez_252d_z504_3d_v052_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slopez_21d_z126_3d_v053_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slopez_63d_z252_3d_v054_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slopez_126d_z252_3d_v055_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_slopez_252d_z504_3d_v056_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_jerk_21d_3d_v057_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_jerk_63d_3d_v058_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_jerk_126d_3d_v059_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_jerk_21d_3d_v060_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_jerk_63d_3d_v061_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_jerk_126d_3d_v062_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_jerk_21d_3d_v063_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_jerk_63d_3d_v064_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_jerk_126d_3d_v065_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_jerk_21d_3d_v066_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_jerk_63d_3d_v067_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_jerk_126d_3d_v068_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_jerk_21d_3d_v069_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_jerk_63d_3d_v070_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_jerk_126d_3d_v071_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_jerk_21d_3d_v072_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_jerk_63d_3d_v073_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_jerk_126d_3d_v074_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_jerk_21d_3d_v075_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_jerk_63d_3d_v076_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_jerk_126d_3d_v077_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ticker_change_cnt smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_smoothaccel_63d_sm252_3d_v078_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ticker_change_cnt smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_smoothaccel_252d_sm504_3d_v079_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of related_ticker_cnt smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_smoothaccel_63d_sm252_3d_v080_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of related_ticker_cnt smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_smoothaccel_252d_sm504_3d_v081_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nonusd_flag smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_smoothaccel_63d_sm252_3d_v082_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nonusd_flag smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_smoothaccel_252d_sm504_3d_v083_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of change_rate_504d smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_smoothaccel_63d_sm252_3d_v084_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of change_rate_504d smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_smoothaccel_252d_sm504_3d_v085_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of related_log smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_related_log_smoothaccel_63d_sm252_3d_v086_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of related_log smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_related_log_smoothaccel_252d_sm504_3d_v087_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of permaticker_age smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_smoothaccel_63d_sm252_3d_v088_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of permaticker_age smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_smoothaccel_252d_sm504_3d_v089_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of change_recent_252 smoothed over 252d
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_smoothaccel_63d_sm252_3d_v090_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of change_recent_252 smoothed over 504d
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_smoothaccel_252d_sm504_3d_v091_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_accelz_21d_z252_3d_v092_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_accelz_63d_z504_3d_v093_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_accelz_21d_z252_3d_v094_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_accelz_63d_z504_3d_v095_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_accelz_21d_z252_3d_v096_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_accelz_63d_z504_3d_v097_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_accelz_21d_z252_3d_v098_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_accelz_63d_z504_3d_v099_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_accelz_21d_z252_3d_v100_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_accelz_63d_z504_3d_v101_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_accelz_21d_z252_3d_v102_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_accelz_63d_z504_3d_v103_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_accelz_21d_z252_3d_v104_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of change_recent_252
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_accelz_63d_z504_3d_v105_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ticker_change_cnt (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_signflip_63d_3d_v106_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ticker_change_cnt (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_signflip_252d_3d_v107_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in related_ticker_cnt (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_signflip_63d_3d_v108_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in related_ticker_cnt (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_signflip_252d_3d_v109_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in nonusd_flag (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_signflip_63d_3d_v110_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in nonusd_flag (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_signflip_252d_3d_v111_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in change_rate_504d (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_signflip_63d_3d_v112_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in change_rate_504d (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_signflip_252d_3d_v113_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in related_log (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_related_log_signflip_63d_3d_v114_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in related_log (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_related_log_signflip_252d_3d_v115_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in permaticker_age (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_signflip_63d_3d_v116_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in permaticker_age (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_signflip_252d_3d_v117_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in change_recent_252 (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_signflip_63d_3d_v118_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in change_recent_252 (raw count, no price scaling)
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_signflip_252d_3d_v119_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ticker_change_cnt normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_rngaccel_63d_r252_3d_v120_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ticker_change_cnt normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_rngaccel_252d_r504_3d_v121_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of related_ticker_cnt normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_rngaccel_63d_r252_3d_v122_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of related_ticker_cnt normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_rngaccel_252d_r504_3d_v123_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nonusd_flag normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_rngaccel_63d_r252_3d_v124_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nonusd_flag normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_rngaccel_252d_r504_3d_v125_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of change_rate_504d normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_rngaccel_63d_r252_3d_v126_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of change_rate_504d normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_rngaccel_252d_r504_3d_v127_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of related_log normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_related_log_rngaccel_63d_r252_3d_v128_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of related_log normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_related_log_rngaccel_252d_r504_3d_v129_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of permaticker_age normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_rngaccel_63d_r252_3d_v130_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of permaticker_age normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_rngaccel_252d_r504_3d_v131_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of change_recent_252 normalized by 252d range
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_rngaccel_63d_r252_3d_v132_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of change_recent_252 normalized by 504d range
def f084tcp_f084_ticker_changes_and_permaticker_change_recent_252_rngaccel_252d_r504_3d_v133_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_cumslope_21d_3d_v134_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_cumslope_63d_3d_v135_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ticker_change_cnt
def f084tcp_f084_ticker_changes_and_permaticker_ticker_change_cnt_cumslope_252d_3d_v136_signal(ticker_change_count, closeadj):
    base = ticker_change_count
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_cumslope_21d_3d_v137_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_cumslope_63d_3d_v138_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of related_ticker_cnt
def f084tcp_f084_ticker_changes_and_permaticker_related_ticker_cnt_cumslope_252d_3d_v139_signal(related_ticker_count, closeadj):
    base = related_ticker_count
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_cumslope_21d_3d_v140_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_cumslope_63d_3d_v141_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of nonusd_flag
def f084tcp_f084_ticker_changes_and_permaticker_nonusd_flag_cumslope_252d_3d_v142_signal(currency_code, closeadj):
    base = (currency_code != 'USD').astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_cumslope_21d_3d_v143_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_cumslope_63d_3d_v144_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of change_rate_504d
def f084tcp_f084_ticker_changes_and_permaticker_change_rate_504d_cumslope_252d_3d_v145_signal(ticker_change_count, closeadj):
    base = ticker_change_count.diff(periods=504)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_cumslope_21d_3d_v146_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_cumslope_63d_3d_v147_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of related_log
def f084tcp_f084_ticker_changes_and_permaticker_related_log_cumslope_252d_3d_v148_signal(related_ticker_count, closeadj):
    base = np.log(related_ticker_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_cumslope_21d_3d_v149_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of permaticker_age
def f084tcp_f084_ticker_changes_and_permaticker_permaticker_age_cumslope_63d_3d_v150_signal(permaticker_age_days, closeadj):
    base = permaticker_age_days
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

