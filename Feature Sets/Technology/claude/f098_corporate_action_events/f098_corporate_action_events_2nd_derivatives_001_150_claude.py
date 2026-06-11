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
def _f098_action_density(action_count, w):
    return action_count.rolling(w, min_periods=max(1, w//2)).sum()


def _f098_car_window(abnormal_return_d, window_flag, w):
    return (abnormal_return_d * window_flag).rolling(w, min_periods=1).sum()


def _f098_vol_surge(volume, window_flag, w):
    base_vol = volume.rolling(252, min_periods=63).mean()
    return ((volume / base_vol.replace(0, np.nan)) * window_flag).rolling(w, min_periods=1).max()


# 21d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slope_21d_2d_v001_signal(action_count, closeadj):
    base = action_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slope_63d_2d_v002_signal(action_count, closeadj):
    base = action_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slope_126d_2d_v003_signal(action_count, closeadj):
    base = action_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slope_252d_2d_v004_signal(action_count, closeadj):
    base = action_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slope_504d_2d_v005_signal(action_count, closeadj):
    base = action_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slope_21d_2d_v006_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slope_63d_2d_v007_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slope_126d_2d_v008_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slope_252d_2d_v009_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slope_504d_2d_v010_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slope_21d_2d_v011_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slope_63d_2d_v012_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slope_126d_2d_v013_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slope_252d_2d_v014_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slope_504d_2d_v015_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slope_21d_2d_v016_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slope_63d_2d_v017_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slope_126d_2d_v018_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slope_252d_2d_v019_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slope_504d_2d_v020_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slope_21d_2d_v021_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slope_63d_2d_v022_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slope_126d_2d_v023_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slope_252d_2d_v024_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slope_504d_2d_v025_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slope_21d_2d_v026_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slope_63d_2d_v027_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slope_126d_2d_v028_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slope_252d_2d_v029_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slope_504d_2d_v030_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slope_21d_2d_v031_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slope_63d_2d_v032_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slope_126d_2d_v033_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slope_252d_2d_v034_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slope_504d_2d_v035_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slope_21d_2d_v036_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slope_63d_2d_v037_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slope_126d_2d_v038_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slope_252d_2d_v039_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slope_504d_2d_v040_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slope_21d_2d_v041_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slope_63d_2d_v042_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slope_126d_2d_v043_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slope_252d_2d_v044_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slope_504d_2d_v045_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slope_21d_2d_v046_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slope_63d_2d_v047_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slope_126d_2d_v048_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slope_252d_2d_v049_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slope_504d_2d_v050_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slope_21d_2d_v051_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slope_63d_2d_v052_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slope_126d_2d_v053_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slope_252d_2d_v054_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slope_504d_2d_v055_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slope_21d_2d_v056_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slope_63d_2d_v057_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slope_126d_2d_v058_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slope_252d_2d_v059_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slope_504d_2d_v060_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slope_21d_2d_v061_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slope_63d_2d_v062_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slope_126d_2d_v063_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slope_252d_2d_v064_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slope_504d_2d_v065_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slope_21d_2d_v066_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slope_63d_2d_v067_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slope_126d_2d_v068_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slope_252d_2d_v069_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slope_504d_2d_v070_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slope_21d_2d_v071_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slope_63d_2d_v072_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slope_126d_2d_v073_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slope_252d_2d_v074_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slope_504d_2d_v075_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slope_21d_2d_v076_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slope_63d_2d_v077_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slope_126d_2d_v078_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slope_252d_2d_v079_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slope_504d_2d_v080_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slope_21d_2d_v081_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slope_63d_2d_v082_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slope_126d_2d_v083_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slope_252d_2d_v084_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slope_504d_2d_v085_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slope_21d_2d_v086_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slope_63d_2d_v087_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slope_126d_2d_v088_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slope_252d_2d_v089_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slope_504d_2d_v090_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slope_21d_2d_v091_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slope_63d_2d_v092_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slope_126d_2d_v093_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slope_252d_2d_v094_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slope_504d_2d_v095_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slope_21d_2d_v096_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slope_63d_2d_v097_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slope_126d_2d_v098_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slope_252d_2d_v099_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slope_504d_2d_v100_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slope_21d_2d_v101_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slope_63d_2d_v102_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slope_126d_2d_v103_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slope_252d_2d_v104_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slope_504d_2d_v105_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slope_21d_2d_v106_signal(split_days_since, closeadj):
    base = split_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slope_63d_2d_v107_signal(split_days_since, closeadj):
    base = split_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slope_126d_2d_v108_signal(split_days_since, closeadj):
    base = split_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slope_252d_2d_v109_signal(split_days_since, closeadj):
    base = split_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slope_504d_2d_v110_signal(split_days_since, closeadj):
    base = split_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_slope_21d_2d_v111_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_slope_63d_2d_v112_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_slope_126d_2d_v113_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_slope_252d_2d_v114_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_slope_504d_2d_v115_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_slope_21d_2d_v116_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_slope_63d_2d_v117_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_slope_126d_2d_v118_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_slope_252d_2d_v119_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_slope_504d_2d_v120_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_slope_21d_2d_v121_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_slope_63d_2d_v122_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_slope_126d_2d_v123_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_slope_252d_2d_v124_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_slope_504d_2d_v125_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_slope_21d_2d_v126_signal(dividend_value, closeadj):
    base = dividend_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_slope_63d_2d_v127_signal(dividend_value, closeadj):
    base = dividend_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_slope_126d_2d_v128_signal(dividend_value, closeadj):
    base = dividend_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_slope_252d_2d_v129_signal(dividend_value, closeadj):
    base = dividend_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_slope_504d_2d_v130_signal(dividend_value, closeadj):
    base = dividend_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_slope_21d_2d_v131_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_slope_63d_2d_v132_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_slope_126d_2d_v133_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_slope_252d_2d_v134_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_slope_504d_2d_v135_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_slope_21d_2d_v136_signal(split_value, closeadj):
    base = split_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_slope_63d_2d_v137_signal(split_value, closeadj):
    base = split_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_slope_126d_2d_v138_signal(split_value, closeadj):
    base = split_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_slope_252d_2d_v139_signal(split_value, closeadj):
    base = split_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_slope_504d_2d_v140_signal(split_value, closeadj):
    base = split_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_sm21_sl21_2d_v141_signal(action_count, closeadj):
    base = _mean(action_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_sm63_sl21_2d_v142_signal(action_count, closeadj):
    base = _mean(action_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_sm63_sl63_2d_v143_signal(action_count, closeadj):
    base = _mean(action_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_sm252_sl63_2d_v144_signal(action_count, closeadj):
    base = _mean(action_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_sm252_sl126_2d_v145_signal(action_count, closeadj):
    base = _mean(action_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_sm21_sl21_2d_v146_signal(action_count, closeadj):
    base = _mean(_f098_action_density(action_count, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_sm63_sl21_2d_v147_signal(action_count, closeadj):
    base = _mean(_f098_action_density(action_count, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_sm63_sl63_2d_v148_signal(action_count, closeadj):
    base = _mean(_f098_action_density(action_count, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_sm252_sl63_2d_v149_signal(action_count, closeadj):
    base = _mean(_f098_action_density(action_count, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_sm252_sl126_2d_v150_signal(action_count, closeadj):
    base = _mean(_f098_action_density(action_count, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_sm21_sl21_2d_v151_signal(dividend_event_flag, closeadj):
    base = _mean(dividend_event_flag, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_sm63_sl21_2d_v152_signal(dividend_event_flag, closeadj):
    base = _mean(dividend_event_flag, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_sm63_sl63_2d_v153_signal(dividend_event_flag, closeadj):
    base = _mean(dividend_event_flag, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_sm252_sl63_2d_v154_signal(dividend_event_flag, closeadj):
    base = _mean(dividend_event_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_sm252_sl126_2d_v155_signal(dividend_event_flag, closeadj):
    base = _mean(dividend_event_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_sm21_sl21_2d_v156_signal(split_event_flag, closeadj):
    base = _mean(split_event_flag, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_sm63_sl21_2d_v157_signal(split_event_flag, closeadj):
    base = _mean(split_event_flag, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_sm63_sl63_2d_v158_signal(split_event_flag, closeadj):
    base = _mean(split_event_flag, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_sm252_sl63_2d_v159_signal(split_event_flag, closeadj):
    base = _mean(split_event_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_sm252_sl126_2d_v160_signal(split_event_flag, closeadj):
    base = _mean(split_event_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_sm21_sl21_2d_v161_signal(reverse_split_flag, closeadj):
    base = _mean(reverse_split_flag, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_sm63_sl21_2d_v162_signal(reverse_split_flag, closeadj):
    base = _mean(reverse_split_flag, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_sm63_sl63_2d_v163_signal(reverse_split_flag, closeadj):
    base = _mean(reverse_split_flag, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_sm252_sl63_2d_v164_signal(reverse_split_flag, closeadj):
    base = _mean(reverse_split_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_sm252_sl126_2d_v165_signal(reverse_split_flag, closeadj):
    base = _mean(reverse_split_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_sm21_sl21_2d_v166_signal(ma_event_flag, closeadj):
    base = _mean(ma_event_flag, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_sm63_sl21_2d_v167_signal(ma_event_flag, closeadj):
    base = _mean(ma_event_flag, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_sm63_sl63_2d_v168_signal(ma_event_flag, closeadj):
    base = _mean(ma_event_flag, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_sm252_sl63_2d_v169_signal(ma_event_flag, closeadj):
    base = _mean(ma_event_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_sm252_sl126_2d_v170_signal(ma_event_flag, closeadj):
    base = _mean(ma_event_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_sm21_sl21_2d_v171_signal(spinoff_event_flag, closeadj):
    base = _mean(spinoff_event_flag, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_sm63_sl21_2d_v172_signal(spinoff_event_flag, closeadj):
    base = _mean(spinoff_event_flag, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_sm63_sl63_2d_v173_signal(spinoff_event_flag, closeadj):
    base = _mean(spinoff_event_flag, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_sm252_sl63_2d_v174_signal(spinoff_event_flag, closeadj):
    base = _mean(spinoff_event_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_sm252_sl126_2d_v175_signal(spinoff_event_flag, closeadj):
    base = _mean(spinoff_event_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_sm21_sl21_2d_v176_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_sm63_sl21_2d_v177_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_sm63_sl63_2d_v178_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_sm252_sl63_2d_v179_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_sm252_sl126_2d_v180_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_sm21_sl21_2d_v181_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_sm63_sl21_2d_v182_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_sm63_sl63_2d_v183_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_sm252_sl63_2d_v184_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_sm252_sl126_2d_v185_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_sm21_sl21_2d_v186_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_63d, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_sm63_sl21_2d_v187_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_63d, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_sm63_sl63_2d_v188_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_63d, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_sm252_sl63_2d_v189_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_63d, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_sm252_sl126_2d_v190_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _mean(_f098_car_window(abnormal_return_d, ma_window_63d, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_sm21_sl21_2d_v191_signal(ma_days_since, closeadj):
    base = _mean(ma_days_since, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_sm63_sl21_2d_v192_signal(ma_days_since, closeadj):
    base = _mean(ma_days_since, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_sm63_sl63_2d_v193_signal(ma_days_since, closeadj):
    base = _mean(ma_days_since, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_sm252_sl63_2d_v194_signal(ma_days_since, closeadj):
    base = _mean(ma_days_since, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_sm252_sl126_2d_v195_signal(ma_days_since, closeadj):
    base = _mean(ma_days_since, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_sm21_sl21_2d_v196_signal(volume, ma_window_5d, closeadj):
    base = _mean(_f098_vol_surge(volume, ma_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_sm63_sl21_2d_v197_signal(volume, ma_window_5d, closeadj):
    base = _mean(_f098_vol_surge(volume, ma_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_sm63_sl63_2d_v198_signal(volume, ma_window_5d, closeadj):
    base = _mean(_f098_vol_surge(volume, ma_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_sm252_sl63_2d_v199_signal(volume, ma_window_5d, closeadj):
    base = _mean(_f098_vol_surge(volume, ma_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_sm252_sl126_2d_v200_signal(volume, ma_window_5d, closeadj):
    base = _mean(_f098_vol_surge(volume, ma_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

