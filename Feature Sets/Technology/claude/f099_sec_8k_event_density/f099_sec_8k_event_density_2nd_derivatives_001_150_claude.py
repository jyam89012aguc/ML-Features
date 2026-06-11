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
def _f099_density(event_count, w):
    return event_count.rolling(w, min_periods=max(1, w//2)).sum()


def _f099_car_window(abnormal_return_d, window_flag, w):
    return (abnormal_return_d * window_flag).rolling(w, min_periods=1).sum()


# 21d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slope_21d_2d_v001_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slope_63d_2d_v002_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slope_126d_2d_v003_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slope_252d_2d_v004_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slope_504d_2d_v005_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slope_21d_2d_v006_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slope_63d_2d_v007_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slope_126d_2d_v008_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slope_252d_2d_v009_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slope_504d_2d_v010_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slope_21d_2d_v011_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slope_63d_2d_v012_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slope_126d_2d_v013_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slope_252d_2d_v014_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slope_504d_2d_v015_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slope_21d_2d_v016_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slope_63d_2d_v017_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slope_126d_2d_v018_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slope_252d_2d_v019_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slope_504d_2d_v020_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slope_21d_2d_v021_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slope_63d_2d_v022_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slope_126d_2d_v023_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slope_252d_2d_v024_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slope_504d_2d_v025_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slope_21d_2d_v026_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slope_63d_2d_v027_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slope_126d_2d_v028_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slope_252d_2d_v029_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slope_504d_2d_v030_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slope_21d_2d_v031_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slope_63d_2d_v032_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slope_126d_2d_v033_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slope_252d_2d_v034_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slope_504d_2d_v035_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slope_21d_2d_v036_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slope_63d_2d_v037_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slope_126d_2d_v038_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slope_252d_2d_v039_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slope_504d_2d_v040_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slope_21d_2d_v041_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slope_63d_2d_v042_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slope_126d_2d_v043_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slope_252d_2d_v044_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slope_504d_2d_v045_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slope_21d_2d_v046_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slope_63d_2d_v047_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slope_126d_2d_v048_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slope_252d_2d_v049_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slope_504d_2d_v050_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slope_21d_2d_v051_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slope_63d_2d_v052_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slope_126d_2d_v053_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slope_252d_2d_v054_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slope_504d_2d_v055_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slope_21d_2d_v056_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slope_63d_2d_v057_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slope_126d_2d_v058_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slope_252d_2d_v059_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slope_504d_2d_v060_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slope_21d_2d_v061_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slope_63d_2d_v062_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slope_126d_2d_v063_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slope_252d_2d_v064_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slope_504d_2d_v065_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slope_21d_2d_v066_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slope_63d_2d_v067_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slope_126d_2d_v068_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slope_252d_2d_v069_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slope_504d_2d_v070_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slope_21d_2d_v071_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slope_63d_2d_v072_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slope_126d_2d_v073_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slope_252d_2d_v074_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slope_504d_2d_v075_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slope_21d_2d_v076_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slope_63d_2d_v077_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slope_126d_2d_v078_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slope_252d_2d_v079_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slope_504d_2d_v080_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slope_21d_2d_v081_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slope_63d_2d_v082_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slope_126d_2d_v083_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slope_252d_2d_v084_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slope_504d_2d_v085_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slope_21d_2d_v086_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slope_63d_2d_v087_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slope_126d_2d_v088_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slope_252d_2d_v089_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slope_504d_2d_v090_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slope_21d_2d_v091_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slope_63d_2d_v092_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slope_126d_2d_v093_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slope_252d_2d_v094_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slope_504d_2d_v095_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slope_21d_2d_v096_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slope_63d_2d_v097_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slope_126d_2d_v098_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slope_252d_2d_v099_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slope_504d_2d_v100_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slope_21d_2d_v101_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slope_63d_2d_v102_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slope_126d_2d_v103_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slope_252d_2d_v104_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slope_504d_2d_v105_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slope_21d_2d_v106_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slope_63d_2d_v107_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slope_126d_2d_v108_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slope_252d_2d_v109_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slope_504d_2d_v110_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_sm21_sl21_2d_v111_signal(event_count_total, closeadj):
    base = _mean(_f099_density(event_count_total, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_sm63_sl21_2d_v112_signal(event_count_total, closeadj):
    base = _mean(_f099_density(event_count_total, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_sm63_sl63_2d_v113_signal(event_count_total, closeadj):
    base = _mean(_f099_density(event_count_total, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_sm252_sl63_2d_v114_signal(event_count_total, closeadj):
    base = _mean(_f099_density(event_count_total, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_sm252_sl126_2d_v115_signal(event_count_total, closeadj):
    base = _mean(_f099_density(event_count_total, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_sm21_sl21_2d_v116_signal(event_count_code22, closeadj):
    base = _mean(_f099_density(event_count_code22, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_sm63_sl21_2d_v117_signal(event_count_code22, closeadj):
    base = _mean(_f099_density(event_count_code22, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_sm63_sl63_2d_v118_signal(event_count_code22, closeadj):
    base = _mean(_f099_density(event_count_code22, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_sm252_sl63_2d_v119_signal(event_count_code22, closeadj):
    base = _mean(_f099_density(event_count_code22, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_sm252_sl126_2d_v120_signal(event_count_code22, closeadj):
    base = _mean(_f099_density(event_count_code22, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_sm21_sl21_2d_v121_signal(event_count_code71, closeadj):
    base = _mean(_f099_density(event_count_code71, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_sm63_sl21_2d_v122_signal(event_count_code71, closeadj):
    base = _mean(_f099_density(event_count_code71, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_sm63_sl63_2d_v123_signal(event_count_code71, closeadj):
    base = _mean(_f099_density(event_count_code71, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_sm252_sl63_2d_v124_signal(event_count_code71, closeadj):
    base = _mean(_f099_density(event_count_code71, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_sm252_sl126_2d_v125_signal(event_count_code71, closeadj):
    base = _mean(_f099_density(event_count_code71, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_sm21_sl21_2d_v126_signal(event_count_code81, closeadj):
    base = _mean(_f099_density(event_count_code81, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_sm63_sl21_2d_v127_signal(event_count_code81, closeadj):
    base = _mean(_f099_density(event_count_code81, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_sm63_sl63_2d_v128_signal(event_count_code81, closeadj):
    base = _mean(_f099_density(event_count_code81, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_sm252_sl63_2d_v129_signal(event_count_code81, closeadj):
    base = _mean(_f099_density(event_count_code81, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_sm252_sl126_2d_v130_signal(event_count_code81, closeadj):
    base = _mean(_f099_density(event_count_code81, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_sm21_sl21_2d_v131_signal(event_count_code91, closeadj):
    base = _mean(_f099_density(event_count_code91, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_sm63_sl21_2d_v132_signal(event_count_code91, closeadj):
    base = _mean(_f099_density(event_count_code91, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_sm63_sl63_2d_v133_signal(event_count_code91, closeadj):
    base = _mean(_f099_density(event_count_code91, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_sm252_sl63_2d_v134_signal(event_count_code91, closeadj):
    base = _mean(_f099_density(event_count_code91, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_sm252_sl126_2d_v135_signal(event_count_code91, closeadj):
    base = _mean(_f099_density(event_count_code91, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_sm21_sl21_2d_v136_signal(event_count_total, closeadj):
    base = _mean((event_count_total > 3).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_sm63_sl21_2d_v137_signal(event_count_total, closeadj):
    base = _mean((event_count_total > 3).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_sm63_sl63_2d_v138_signal(event_count_total, closeadj):
    base = _mean((event_count_total > 3).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_sm252_sl63_2d_v139_signal(event_count_total, closeadj):
    base = _mean((event_count_total > 3).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_sm252_sl126_2d_v140_signal(event_count_total, closeadj):
    base = _mean((event_count_total > 3).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_sm21_sl21_2d_v141_signal(event_count_total, closeadj):
    base = _mean((event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_sm63_sl21_2d_v142_signal(event_count_total, closeadj):
    base = _mean((event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_sm63_sl63_2d_v143_signal(event_count_total, closeadj):
    base = _mean((event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_sm252_sl63_2d_v144_signal(event_count_total, closeadj):
    base = _mean((event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_sm252_sl126_2d_v145_signal(event_count_total, closeadj):
    base = _mean((event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_sm21_sl21_2d_v146_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_sm63_sl21_2d_v147_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_sm63_sl63_2d_v148_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_sm252_sl63_2d_v149_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_sm252_sl126_2d_v150_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_sm21_sl21_2d_v151_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_sm63_sl21_2d_v152_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_sm63_sl63_2d_v153_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_sm252_sl63_2d_v154_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_sm252_sl126_2d_v155_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_sm21_sl21_2d_v156_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_63d, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_sm63_sl21_2d_v157_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_63d, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_sm63_sl63_2d_v158_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_63d, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_sm252_sl63_2d_v159_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_63d, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_sm252_sl126_2d_v160_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code22_window_63d, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_sm21_sl21_2d_v161_signal(code22_days_since, closeadj):
    base = _mean(code22_days_since, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_sm63_sl21_2d_v162_signal(code22_days_since, closeadj):
    base = _mean(code22_days_since, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_sm63_sl63_2d_v163_signal(code22_days_since, closeadj):
    base = _mean(code22_days_since, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_sm252_sl63_2d_v164_signal(code22_days_since, closeadj):
    base = _mean(code22_days_since, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_sm252_sl126_2d_v165_signal(code22_days_since, closeadj):
    base = _mean(code22_days_since, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_sm21_sl21_2d_v166_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_sm63_sl21_2d_v167_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_sm63_sl63_2d_v168_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_sm252_sl63_2d_v169_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_sm252_sl126_2d_v170_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_sm21_sl21_2d_v171_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_sm63_sl21_2d_v172_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_sm63_sl63_2d_v173_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_sm252_sl63_2d_v174_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_sm252_sl126_2d_v175_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code71_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_sm21_sl21_2d_v176_signal(code71_days_since, closeadj):
    base = _mean(code71_days_since, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_sm63_sl21_2d_v177_signal(code71_days_since, closeadj):
    base = _mean(code71_days_since, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_sm63_sl63_2d_v178_signal(code71_days_since, closeadj):
    base = _mean(code71_days_since, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_sm252_sl63_2d_v179_signal(code71_days_since, closeadj):
    base = _mean(code71_days_since, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_sm252_sl126_2d_v180_signal(code71_days_since, closeadj):
    base = _mean(code71_days_since, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_sm21_sl21_2d_v181_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_sm63_sl21_2d_v182_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_sm63_sl63_2d_v183_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_sm252_sl63_2d_v184_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_sm252_sl126_2d_v185_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_sm21_sl21_2d_v186_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_sm63_sl21_2d_v187_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_sm63_sl63_2d_v188_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_sm252_sl63_2d_v189_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_sm252_sl126_2d_v190_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code81_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_sm21_sl21_2d_v191_signal(code81_days_since, closeadj):
    base = _mean(code81_days_since, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_sm63_sl21_2d_v192_signal(code81_days_since, closeadj):
    base = _mean(code81_days_since, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_sm63_sl63_2d_v193_signal(code81_days_since, closeadj):
    base = _mean(code81_days_since, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_sm252_sl63_2d_v194_signal(code81_days_since, closeadj):
    base = _mean(code81_days_since, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_sm252_sl126_2d_v195_signal(code81_days_since, closeadj):
    base = _mean(code81_days_since, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_sm21_sl21_2d_v196_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code91_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_sm63_sl21_2d_v197_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code91_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_sm63_sl63_2d_v198_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code91_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_sm252_sl63_2d_v199_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code91_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_sm252_sl126_2d_v200_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _mean(_f099_car_window(abnormal_return_d, code91_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

