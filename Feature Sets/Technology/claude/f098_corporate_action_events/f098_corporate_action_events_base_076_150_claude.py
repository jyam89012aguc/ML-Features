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
def _f098_action_density(action_count, w):
    return action_count.rolling(w, min_periods=max(1, w//2)).sum()


def _f098_car_window(abnormal_return_d, window_flag, w):
    return (abnormal_return_d * window_flag).rolling(w, min_periods=1).sum()


def _f098_vol_surge(volume, window_flag, w):
    base_vol = volume.rolling(252, min_periods=63).mean()
    return ((volume / base_vol.replace(0, np.nan)) * window_flag).rolling(w, min_periods=1).max()


# 63d z-score of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_z_63d_base_v076_signal(action_count, closeadj):
    base = action_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_z_126d_base_v077_signal(action_count, closeadj):
    base = action_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_z_252d_base_v078_signal(action_count, closeadj):
    base = action_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_z_504d_base_v079_signal(action_count, closeadj):
    base = action_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_z_63d_base_v080_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_z_126d_base_v081_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_z_252d_base_v082_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_z_504d_base_v083_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_z_63d_base_v084_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_z_126d_base_v085_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_z_252d_base_v086_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_z_504d_base_v087_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_z_63d_base_v088_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_z_126d_base_v089_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_z_252d_base_v090_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_z_504d_base_v091_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_z_63d_base_v092_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_z_126d_base_v093_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_z_252d_base_v094_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_z_504d_base_v095_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_z_63d_base_v096_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_z_126d_base_v097_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_z_252d_base_v098_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_z_504d_base_v099_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_z_63d_base_v100_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_z_126d_base_v101_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_z_252d_base_v102_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_z_504d_base_v103_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_z_63d_base_v104_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_z_126d_base_v105_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_z_252d_base_v106_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_z_504d_base_v107_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_z_63d_base_v108_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_z_126d_base_v109_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_z_252d_base_v110_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_z_504d_base_v111_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_z_63d_base_v112_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_z_126d_base_v113_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_z_252d_base_v114_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_z_504d_base_v115_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_z_63d_base_v116_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_z_126d_base_v117_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_z_252d_base_v118_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_z_504d_base_v119_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_z_63d_base_v120_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_z_126d_base_v121_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_z_252d_base_v122_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_z_504d_base_v123_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_z_63d_base_v124_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_z_126d_base_v125_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_z_252d_base_v126_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_z_504d_base_v127_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_z_63d_base_v128_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_z_126d_base_v129_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_z_252d_base_v130_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_z_504d_base_v131_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_z_63d_base_v132_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_z_126d_base_v133_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_z_252d_base_v134_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_z_504d_base_v135_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_z_63d_base_v136_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_z_126d_base_v137_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_z_252d_base_v138_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_z_504d_base_v139_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_z_63d_base_v140_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_z_126d_base_v141_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_z_252d_base_v142_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_z_504d_base_v143_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_z_63d_base_v144_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_z_126d_base_v145_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_z_252d_base_v146_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_z_504d_base_v147_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_z_63d_base_v148_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_z_126d_base_v149_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_z_252d_base_v150_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_z_504d_base_v151_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_z_63d_base_v152_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_z_126d_base_v153_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_z_252d_base_v154_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_z_504d_base_v155_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_z_63d_base_v156_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_z_126d_base_v157_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_z_252d_base_v158_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_z_504d_base_v159_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_z_63d_base_v160_signal(split_days_since, closeadj):
    base = split_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_z_126d_base_v161_signal(split_days_since, closeadj):
    base = split_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_z_252d_base_v162_signal(split_days_since, closeadj):
    base = split_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_z_504d_base_v163_signal(split_days_since, closeadj):
    base = split_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_z_63d_base_v164_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_z_126d_base_v165_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_z_252d_base_v166_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_z_504d_base_v167_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_z_63d_base_v168_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_z_126d_base_v169_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_z_252d_base_v170_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_z_504d_base_v171_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_z_63d_base_v172_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_z_126d_base_v173_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_z_252d_base_v174_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_z_504d_base_v175_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

