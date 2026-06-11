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
def _f099_density(event_count, w):
    return event_count.rolling(w, min_periods=max(1, w//2)).sum()


def _f099_car_window(abnormal_return_d, window_flag, w):
    return (abnormal_return_d * window_flag).rolling(w, min_periods=1).sum()


# 21d mean of event_total_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_total_252_mean_21d_base_v001_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_total_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_total_252_mean_63d_base_v002_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_total_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_total_252_mean_126d_base_v003_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_total_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_total_252_mean_252d_base_v004_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_total_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_total_252_mean_504d_base_v005_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_code22_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code22_252_mean_21d_base_v006_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_code22_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code22_252_mean_63d_base_v007_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_code22_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code22_252_mean_126d_base_v008_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_code22_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code22_252_mean_252d_base_v009_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_code22_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code22_252_mean_504d_base_v010_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_code71_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code71_252_mean_21d_base_v011_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_code71_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code71_252_mean_63d_base_v012_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_code71_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code71_252_mean_126d_base_v013_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_code71_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code71_252_mean_252d_base_v014_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_code71_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code71_252_mean_504d_base_v015_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_code81_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code81_252_mean_21d_base_v016_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_code81_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code81_252_mean_63d_base_v017_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_code81_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code81_252_mean_126d_base_v018_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_code81_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code81_252_mean_252d_base_v019_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_code81_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code81_252_mean_504d_base_v020_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_code91_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code91_252_mean_21d_base_v021_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_code91_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code91_252_mean_63d_base_v022_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_code91_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code91_252_mean_126d_base_v023_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_code91_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code91_252_mean_252d_base_v024_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_code91_252 scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_code91_252_mean_504d_base_v025_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_burst scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_burst_mean_21d_base_v026_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_burst scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_burst_mean_63d_base_v027_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_burst scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_burst_mean_126d_base_v028_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_burst scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_burst_mean_252d_base_v029_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_burst scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_burst_mean_504d_base_v030_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_cadence_z scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cadence_z_mean_21d_base_v031_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_cadence_z scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cadence_z_mean_63d_base_v032_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_cadence_z scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cadence_z_mean_126d_base_v033_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_cadence_z scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cadence_z_mean_252d_base_v034_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_cadence_z scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cadence_z_mean_504d_base_v035_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code22_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_5d_mean_21d_base_v036_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code22_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_5d_mean_63d_base_v037_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code22_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_5d_mean_126d_base_v038_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code22_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_5d_mean_252d_base_v039_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code22_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_5d_mean_504d_base_v040_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code22_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_21d_mean_21d_base_v041_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code22_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_21d_mean_63d_base_v042_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code22_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_21d_mean_126d_base_v043_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code22_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_21d_mean_252d_base_v044_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code22_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_21d_mean_504d_base_v045_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code22_car_63d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_63d_mean_21d_base_v046_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code22_car_63d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_63d_mean_63d_base_v047_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code22_car_63d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_63d_mean_126d_base_v048_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code22_car_63d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_63d_mean_252d_base_v049_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code22_car_63d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_car_63d_mean_504d_base_v050_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code22_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_days_since_mean_21d_base_v051_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code22_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_days_since_mean_63d_base_v052_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code22_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_days_since_mean_126d_base_v053_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code22_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_days_since_mean_252d_base_v054_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code22_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code22_days_since_mean_504d_base_v055_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code71_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_5d_mean_21d_base_v056_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code71_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_5d_mean_63d_base_v057_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code71_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_5d_mean_126d_base_v058_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code71_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_5d_mean_252d_base_v059_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code71_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_5d_mean_504d_base_v060_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code71_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_21d_mean_21d_base_v061_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code71_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_21d_mean_63d_base_v062_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code71_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_21d_mean_126d_base_v063_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code71_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_21d_mean_252d_base_v064_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code71_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_car_21d_mean_504d_base_v065_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code71_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_days_since_mean_21d_base_v066_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code71_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_days_since_mean_63d_base_v067_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code71_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_days_since_mean_126d_base_v068_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code71_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_days_since_mean_252d_base_v069_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code71_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code71_days_since_mean_504d_base_v070_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code81_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_5d_mean_21d_base_v071_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code81_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_5d_mean_63d_base_v072_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code81_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_5d_mean_126d_base_v073_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code81_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_5d_mean_252d_base_v074_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code81_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_5d_mean_504d_base_v075_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code81_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_21d_mean_21d_base_v076_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code81_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_21d_mean_63d_base_v077_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code81_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_21d_mean_126d_base_v078_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code81_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_21d_mean_252d_base_v079_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code81_car_21d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_car_21d_mean_504d_base_v080_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code81_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_days_since_mean_21d_base_v081_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code81_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_days_since_mean_63d_base_v082_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code81_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_days_since_mean_126d_base_v083_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code81_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_days_since_mean_252d_base_v084_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code81_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code81_days_since_mean_504d_base_v085_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code91_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_car_5d_mean_21d_base_v086_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code91_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_car_5d_mean_63d_base_v087_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code91_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_car_5d_mean_126d_base_v088_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code91_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_car_5d_mean_252d_base_v089_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code91_car_5d scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_car_5d_mean_504d_base_v090_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of code91_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_days_since_mean_21d_base_v091_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of code91_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_days_since_mean_63d_base_v092_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of code91_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_days_since_mean_126d_base_v093_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of code91_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_days_since_mean_252d_base_v094_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of code91_days_since scaled by closeadj
def f099sed_f099_sec_8k_event_density_code91_days_since_mean_504d_base_v095_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of event_cluster_252d scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cluster_252d_mean_21d_base_v096_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of event_cluster_252d scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cluster_252d_mean_63d_base_v097_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of event_cluster_252d scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cluster_252d_mean_126d_base_v098_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of event_cluster_252d scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cluster_252d_mean_252d_base_v099_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of event_cluster_252d scaled by closeadj
def f099sed_f099_sec_8k_event_density_event_cluster_252d_mean_504d_base_v100_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

