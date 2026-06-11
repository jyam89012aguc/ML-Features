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


# 63d z-score of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_z_63d_base_v076_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_z_126d_base_v077_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_z_252d_base_v078_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_z_504d_base_v079_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_z_63d_base_v080_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_z_126d_base_v081_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_z_252d_base_v082_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_z_504d_base_v083_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_z_63d_base_v084_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_z_126d_base_v085_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_z_252d_base_v086_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_z_504d_base_v087_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_z_63d_base_v088_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_z_126d_base_v089_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_z_252d_base_v090_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_z_504d_base_v091_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_z_63d_base_v092_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_z_126d_base_v093_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_z_252d_base_v094_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_z_504d_base_v095_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_z_63d_base_v096_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_z_126d_base_v097_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_z_252d_base_v098_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_z_504d_base_v099_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_z_63d_base_v100_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_z_126d_base_v101_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_z_252d_base_v102_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_cadence_z
def f099sed_f099_sec_8k_event_density_event_cadence_z_z_504d_base_v103_signal(event_count_total, closeadj):
    base = (event_count_total - event_count_total.rolling(252, min_periods=63).mean()) / event_count_total.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_z_63d_base_v104_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_z_126d_base_v105_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_z_252d_base_v106_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code22_car_5d
def f099sed_f099_sec_8k_event_density_code22_car_5d_z_504d_base_v107_signal(abnormal_return_d, code22_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_z_63d_base_v108_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_z_126d_base_v109_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_z_252d_base_v110_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code22_car_21d
def f099sed_f099_sec_8k_event_density_code22_car_21d_z_504d_base_v111_signal(abnormal_return_d, code22_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_z_63d_base_v112_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_z_126d_base_v113_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_z_252d_base_v114_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code22_car_63d
def f099sed_f099_sec_8k_event_density_code22_car_63d_z_504d_base_v115_signal(abnormal_return_d, code22_window_63d, closeadj):
    base = _f099_car_window(abnormal_return_d, code22_window_63d, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_z_63d_base_v116_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_z_126d_base_v117_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_z_252d_base_v118_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code22_days_since
def f099sed_f099_sec_8k_event_density_code22_days_since_z_504d_base_v119_signal(code22_days_since, closeadj):
    base = code22_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_z_63d_base_v120_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_z_126d_base_v121_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_z_252d_base_v122_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code71_car_5d
def f099sed_f099_sec_8k_event_density_code71_car_5d_z_504d_base_v123_signal(abnormal_return_d, code71_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_z_63d_base_v124_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_z_126d_base_v125_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_z_252d_base_v126_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code71_car_21d
def f099sed_f099_sec_8k_event_density_code71_car_21d_z_504d_base_v127_signal(abnormal_return_d, code71_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code71_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_z_63d_base_v128_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_z_126d_base_v129_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_z_252d_base_v130_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code71_days_since
def f099sed_f099_sec_8k_event_density_code71_days_since_z_504d_base_v131_signal(code71_days_since, closeadj):
    base = code71_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_z_63d_base_v132_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_z_126d_base_v133_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_z_252d_base_v134_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code81_car_5d
def f099sed_f099_sec_8k_event_density_code81_car_5d_z_504d_base_v135_signal(abnormal_return_d, code81_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_z_63d_base_v136_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_z_126d_base_v137_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_z_252d_base_v138_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code81_car_21d
def f099sed_f099_sec_8k_event_density_code81_car_21d_z_504d_base_v139_signal(abnormal_return_d, code81_window_21d, closeadj):
    base = _f099_car_window(abnormal_return_d, code81_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_z_63d_base_v140_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_z_126d_base_v141_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_z_252d_base_v142_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code81_days_since
def f099sed_f099_sec_8k_event_density_code81_days_since_z_504d_base_v143_signal(code81_days_since, closeadj):
    base = code81_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_z_63d_base_v144_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_z_126d_base_v145_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_z_252d_base_v146_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code91_car_5d
def f099sed_f099_sec_8k_event_density_code91_car_5d_z_504d_base_v147_signal(abnormal_return_d, code91_window_5d, closeadj):
    base = _f099_car_window(abnormal_return_d, code91_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_z_63d_base_v148_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_z_126d_base_v149_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_z_252d_base_v150_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of code91_days_since
def f099sed_f099_sec_8k_event_density_code91_days_since_z_504d_base_v151_signal(code91_days_since, closeadj):
    base = code91_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_z_63d_base_v152_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_z_126d_base_v153_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_z_252d_base_v154_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_cluster_252d
def f099sed_f099_sec_8k_event_density_event_cluster_252d_z_504d_base_v155_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_z_63d_base_v156_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_z_126d_base_v157_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_z_252d_base_v158_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of event_cluster_burst
def f099sed_f099_sec_8k_event_density_event_cluster_burst_z_504d_base_v159_signal(event_count_code22, event_count_code71, event_count_code81, closeadj):
    base = ((event_count_code22 + event_count_code71 + event_count_code81) > 2).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_z_63d_base_v160_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_z_126d_base_v161_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_z_252d_base_v162_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_with_financing
def f099sed_f099_sec_8k_event_density_ma_with_financing_z_504d_base_v163_signal(code22_window_5d, code71_window_5d, closeadj):
    base = ((code22_window_5d > 0) & (code71_window_5d > 0)).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_distmax_252d_base_v164_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of event_total_252
def f099sed_f099_sec_8k_event_density_event_total_252_distmax_504d_base_v165_signal(event_count_total, closeadj):
    base = _f099_density(event_count_total, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_distmax_252d_base_v166_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of event_code22_252
def f099sed_f099_sec_8k_event_density_event_code22_252_distmax_504d_base_v167_signal(event_count_code22, closeadj):
    base = _f099_density(event_count_code22, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_distmax_252d_base_v168_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of event_code71_252
def f099sed_f099_sec_8k_event_density_event_code71_252_distmax_504d_base_v169_signal(event_count_code71, closeadj):
    base = _f099_density(event_count_code71, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_distmax_252d_base_v170_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of event_code81_252
def f099sed_f099_sec_8k_event_density_event_code81_252_distmax_504d_base_v171_signal(event_count_code81, closeadj):
    base = _f099_density(event_count_code81, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_distmax_252d_base_v172_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of event_code91_252
def f099sed_f099_sec_8k_event_density_event_code91_252_distmax_504d_base_v173_signal(event_count_code91, closeadj):
    base = _f099_density(event_count_code91, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_distmax_252d_base_v174_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of event_burst
def f099sed_f099_sec_8k_event_density_event_burst_distmax_504d_base_v175_signal(event_count_total, closeadj):
    base = (event_count_total > 3).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

