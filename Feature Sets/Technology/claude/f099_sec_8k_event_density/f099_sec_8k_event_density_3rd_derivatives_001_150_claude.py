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


# 21d acceleration of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_accel_21d_3d_v001_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_accel_63d_3d_v002_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_accel_126d_3d_v003_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_accel_252d_3d_v004_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_accel_21d_3d_v005_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_accel_63d_3d_v006_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_accel_126d_3d_v007_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_accel_252d_3d_v008_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_accel_21d_3d_v009_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_accel_63d_3d_v010_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_accel_126d_3d_v011_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_accel_252d_3d_v012_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_accel_21d_3d_v013_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_accel_63d_3d_v014_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_accel_126d_3d_v015_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_accel_252d_3d_v016_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_accel_21d_3d_v017_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_accel_63d_3d_v018_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_accel_126d_3d_v019_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_accel_252d_3d_v020_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_accel_21d_3d_v021_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_accel_63d_3d_v022_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_accel_126d_3d_v023_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_accel_252d_3d_v024_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_accel_21d_3d_v025_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_accel_63d_3d_v026_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_accel_126d_3d_v027_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_accel_252d_3d_v028_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_accel_21d_3d_v029_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_accel_63d_3d_v030_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_accel_126d_3d_v031_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_accel_252d_3d_v032_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_accel_21d_3d_v033_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_accel_63d_3d_v034_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_accel_126d_3d_v035_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_accel_252d_3d_v036_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_accel_21d_3d_v037_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_accel_63d_3d_v038_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_accel_126d_3d_v039_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_accel_252d_3d_v040_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_accel_21d_3d_v041_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_accel_63d_3d_v042_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_accel_126d_3d_v043_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_accel_252d_3d_v044_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_accel_21d_3d_v045_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_accel_63d_3d_v046_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_accel_126d_3d_v047_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_accel_252d_3d_v048_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_accel_21d_3d_v049_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_accel_63d_3d_v050_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_accel_126d_3d_v051_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_accel_252d_3d_v052_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_accel_21d_3d_v053_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_accel_63d_3d_v054_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_accel_126d_3d_v055_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_accel_252d_3d_v056_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_accel_21d_3d_v057_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_accel_63d_3d_v058_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_accel_126d_3d_v059_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_accel_252d_3d_v060_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_accel_21d_3d_v061_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_accel_63d_3d_v062_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_accel_126d_3d_v063_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_accel_252d_3d_v064_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_accel_21d_3d_v065_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_accel_63d_3d_v066_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_accel_126d_3d_v067_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_accel_252d_3d_v068_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_accel_21d_3d_v069_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_accel_63d_3d_v070_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_accel_126d_3d_v071_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_accel_252d_3d_v072_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_accel_21d_3d_v073_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_accel_63d_3d_v074_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_accel_126d_3d_v075_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_accel_252d_3d_v076_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_accel_21d_3d_v077_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_accel_63d_3d_v078_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_accel_126d_3d_v079_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_accel_252d_3d_v080_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_accel_21d_3d_v081_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_accel_63d_3d_v082_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_accel_126d_3d_v083_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_accel_252d_3d_v084_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_accel_21d_3d_v085_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_accel_63d_3d_v086_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_accel_126d_3d_v087_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_accel_252d_3d_v088_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slopez_21d_z126_3d_v089_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slopez_63d_z252_3d_v090_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slopez_126d_z252_3d_v091_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_slopez_252d_z504_3d_v092_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slopez_21d_z126_3d_v093_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slopez_63d_z252_3d_v094_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slopez_126d_z252_3d_v095_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_slopez_252d_z504_3d_v096_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slopez_21d_z126_3d_v097_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slopez_63d_z252_3d_v098_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slopez_126d_z252_3d_v099_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_slopez_252d_z504_3d_v100_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slopez_21d_z126_3d_v101_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slopez_63d_z252_3d_v102_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slopez_126d_z252_3d_v103_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_slopez_252d_z504_3d_v104_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slopez_21d_z126_3d_v105_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slopez_63d_z252_3d_v106_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slopez_126d_z252_3d_v107_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_slopez_252d_z504_3d_v108_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slopez_21d_z126_3d_v109_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slopez_63d_z252_3d_v110_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slopez_126d_z252_3d_v111_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_slopez_252d_z504_3d_v112_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slopez_21d_z126_3d_v113_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slopez_63d_z252_3d_v114_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slopez_126d_z252_3d_v115_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_slopez_252d_z504_3d_v116_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slopez_21d_z126_3d_v117_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slopez_63d_z252_3d_v118_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slopez_126d_z252_3d_v119_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_slopez_252d_z504_3d_v120_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slopez_21d_z126_3d_v121_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slopez_63d_z252_3d_v122_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slopez_126d_z252_3d_v123_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_slopez_252d_z504_3d_v124_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slopez_21d_z126_3d_v125_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slopez_63d_z252_3d_v126_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slopez_126d_z252_3d_v127_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_slopez_252d_z504_3d_v128_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slopez_21d_z126_3d_v129_signal(code22_days_since, closeadj):
    base = code22_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slopez_63d_z252_3d_v130_signal(code22_days_since, closeadj):
    base = code22_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slopez_126d_z252_3d_v131_signal(code22_days_since, closeadj):
    base = code22_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_slopez_252d_z504_3d_v132_signal(code22_days_since, closeadj):
    base = code22_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slopez_21d_z126_3d_v133_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slopez_63d_z252_3d_v134_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slopez_126d_z252_3d_v135_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_slopez_252d_z504_3d_v136_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slopez_21d_z126_3d_v137_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slopez_63d_z252_3d_v138_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slopez_126d_z252_3d_v139_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_slopez_252d_z504_3d_v140_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slopez_21d_z126_3d_v141_signal(code71_days_since, closeadj):
    base = code71_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slopez_63d_z252_3d_v142_signal(code71_days_since, closeadj):
    base = code71_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slopez_126d_z252_3d_v143_signal(code71_days_since, closeadj):
    base = code71_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_slopez_252d_z504_3d_v144_signal(code71_days_since, closeadj):
    base = code71_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slopez_21d_z126_3d_v145_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slopez_63d_z252_3d_v146_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slopez_126d_z252_3d_v147_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_slopez_252d_z504_3d_v148_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slopez_21d_z126_3d_v149_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slopez_63d_z252_3d_v150_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slopez_126d_z252_3d_v151_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_slopez_252d_z504_3d_v152_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slopez_21d_z126_3d_v153_signal(code81_days_since, closeadj):
    base = code81_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slopez_63d_z252_3d_v154_signal(code81_days_since, closeadj):
    base = code81_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slopez_126d_z252_3d_v155_signal(code81_days_since, closeadj):
    base = code81_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_slopez_252d_z504_3d_v156_signal(code81_days_since, closeadj):
    base = code81_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slopez_21d_z126_3d_v157_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slopez_63d_z252_3d_v158_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slopez_126d_z252_3d_v159_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_slopez_252d_z504_3d_v160_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slopez_21d_z126_3d_v161_signal(code91_days_since, closeadj):
    base = code91_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slopez_63d_z252_3d_v162_signal(code91_days_since, closeadj):
    base = code91_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slopez_126d_z252_3d_v163_signal(code91_days_since, closeadj):
    base = code91_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_slopez_252d_z504_3d_v164_signal(code91_days_since, closeadj):
    base = code91_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slopez_21d_z126_3d_v165_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slopez_63d_z252_3d_v166_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slopez_126d_z252_3d_v167_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_slopez_252d_z504_3d_v168_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slopez_21d_z126_3d_v169_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slopez_63d_z252_3d_v170_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slopez_126d_z252_3d_v171_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_slopez_252d_z504_3d_v172_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slopez_21d_z126_3d_v173_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slopez_63d_z252_3d_v174_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slopez_126d_z252_3d_v175_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_slopez_252d_z504_3d_v176_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_jerk_21d_3d_v177_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_jerk_63d_3d_v178_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_jerk_126d_3d_v179_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_jerk_21d_3d_v180_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_jerk_63d_3d_v181_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_jerk_126d_3d_v182_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_jerk_21d_3d_v183_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_jerk_63d_3d_v184_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_jerk_126d_3d_v185_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_jerk_21d_3d_v186_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_jerk_63d_3d_v187_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_jerk_126d_3d_v188_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_jerk_21d_3d_v189_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_jerk_63d_3d_v190_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_jerk_126d_3d_v191_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_jerk_21d_3d_v192_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_jerk_63d_3d_v193_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_jerk_126d_3d_v194_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_jerk_21d_3d_v195_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_jerk_63d_3d_v196_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_jerk_126d_3d_v197_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_jerk_21d_3d_v198_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_jerk_63d_3d_v199_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_jerk_126d_3d_v200_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

