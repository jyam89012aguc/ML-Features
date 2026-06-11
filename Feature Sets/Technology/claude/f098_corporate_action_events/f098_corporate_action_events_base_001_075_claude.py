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


# 21d mean of any_action_cnt scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_cnt_mean_21d_base_v001_signal(action_count, closeadj):
    base = action_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of any_action_cnt scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_cnt_mean_63d_base_v002_signal(action_count, closeadj):
    base = action_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of any_action_cnt scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_cnt_mean_126d_base_v003_signal(action_count, closeadj):
    base = action_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of any_action_cnt scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_cnt_mean_252d_base_v004_signal(action_count, closeadj):
    base = action_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of any_action_cnt scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_cnt_mean_504d_base_v005_signal(action_count, closeadj):
    base = action_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of any_action_252d scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_252d_mean_21d_base_v006_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of any_action_252d scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_252d_mean_63d_base_v007_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of any_action_252d scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_252d_mean_126d_base_v008_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of any_action_252d scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_252d_mean_252d_base_v009_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of any_action_252d scaled by closeadj
def f098cae_f098_corporate_action_events_any_action_252d_mean_504d_base_v010_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dividend_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_event_flag_mean_21d_base_v011_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dividend_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_event_flag_mean_63d_base_v012_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dividend_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_event_flag_mean_126d_base_v013_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dividend_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_event_flag_mean_252d_base_v014_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dividend_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_event_flag_mean_504d_base_v015_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of split_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_split_event_flag_mean_21d_base_v016_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of split_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_split_event_flag_mean_63d_base_v017_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of split_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_split_event_flag_mean_126d_base_v018_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of split_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_split_event_flag_mean_252d_base_v019_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of split_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_split_event_flag_mean_504d_base_v020_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of reverse_split_flag scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_flag_mean_21d_base_v021_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of reverse_split_flag scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_flag_mean_63d_base_v022_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of reverse_split_flag scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_flag_mean_126d_base_v023_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of reverse_split_flag scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_flag_mean_252d_base_v024_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of reverse_split_flag scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_flag_mean_504d_base_v025_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ma_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_ma_event_flag_mean_21d_base_v026_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ma_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_ma_event_flag_mean_63d_base_v027_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ma_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_ma_event_flag_mean_126d_base_v028_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ma_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_ma_event_flag_mean_252d_base_v029_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ma_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_ma_event_flag_mean_504d_base_v030_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of spinoff_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_spinoff_event_flag_mean_21d_base_v031_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of spinoff_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_spinoff_event_flag_mean_63d_base_v032_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of spinoff_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_spinoff_event_flag_mean_126d_base_v033_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of spinoff_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_spinoff_event_flag_mean_252d_base_v034_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of spinoff_event_flag scaled by closeadj
def f098cae_f098_corporate_action_events_spinoff_event_flag_mean_504d_base_v035_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ma_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_5d_mean_21d_base_v036_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ma_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_5d_mean_63d_base_v037_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ma_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_5d_mean_126d_base_v038_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ma_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_5d_mean_252d_base_v039_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ma_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_5d_mean_504d_base_v040_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ma_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_21d_mean_21d_base_v041_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ma_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_21d_mean_63d_base_v042_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ma_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_21d_mean_126d_base_v043_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ma_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_21d_mean_252d_base_v044_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ma_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_21d_mean_504d_base_v045_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ma_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_63d_mean_21d_base_v046_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ma_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_63d_mean_63d_base_v047_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ma_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_63d_mean_126d_base_v048_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ma_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_63d_mean_252d_base_v049_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ma_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_car_63d_mean_504d_base_v050_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ma_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_ma_days_since_mean_21d_base_v051_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ma_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_ma_days_since_mean_63d_base_v052_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ma_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_ma_days_since_mean_126d_base_v053_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ma_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_ma_days_since_mean_252d_base_v054_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ma_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_ma_days_since_mean_504d_base_v055_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ma_vol_surge_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_mean_21d_base_v056_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ma_vol_surge_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_mean_63d_base_v057_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ma_vol_surge_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_mean_126d_base_v058_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ma_vol_surge_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_mean_252d_base_v059_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ma_vol_surge_5d scaled by closeadj
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_mean_504d_base_v060_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dividend_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_5d_mean_21d_base_v061_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dividend_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_5d_mean_63d_base_v062_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dividend_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_5d_mean_126d_base_v063_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dividend_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_5d_mean_252d_base_v064_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dividend_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_5d_mean_504d_base_v065_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dividend_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_21d_mean_21d_base_v066_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dividend_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_21d_mean_63d_base_v067_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dividend_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_21d_mean_126d_base_v068_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dividend_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_21d_mean_252d_base_v069_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dividend_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_car_21d_mean_504d_base_v070_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dividend_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_days_since_mean_21d_base_v071_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dividend_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_days_since_mean_63d_base_v072_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dividend_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_days_since_mean_126d_base_v073_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dividend_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_days_since_mean_252d_base_v074_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dividend_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_days_since_mean_504d_base_v075_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dividend_init_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_init_car_63d_mean_21d_base_v076_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dividend_init_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_init_car_63d_mean_63d_base_v077_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dividend_init_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_init_car_63d_mean_126d_base_v078_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dividend_init_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_init_car_63d_mean_252d_base_v079_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dividend_init_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_dividend_init_car_63d_mean_504d_base_v080_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of reverse_split_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_21d_mean_21d_base_v081_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of reverse_split_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_21d_mean_63d_base_v082_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of reverse_split_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_21d_mean_126d_base_v083_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of reverse_split_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_21d_mean_252d_base_v084_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of reverse_split_car_21d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_21d_mean_504d_base_v085_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of reverse_split_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_63d_mean_21d_base_v086_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of reverse_split_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_63d_mean_63d_base_v087_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of reverse_split_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_63d_mean_126d_base_v088_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of reverse_split_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_63d_mean_252d_base_v089_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of reverse_split_car_63d scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_car_63d_mean_504d_base_v090_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of reverse_split_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_days_since_mean_21d_base_v091_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of reverse_split_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_days_since_mean_63d_base_v092_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of reverse_split_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_days_since_mean_126d_base_v093_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of reverse_split_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_days_since_mean_252d_base_v094_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of reverse_split_days_since scaled by closeadj
def f098cae_f098_corporate_action_events_reverse_split_days_since_mean_504d_base_v095_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of split_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_split_car_5d_mean_21d_base_v096_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of split_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_split_car_5d_mean_63d_base_v097_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of split_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_split_car_5d_mean_126d_base_v098_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of split_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_split_car_5d_mean_252d_base_v099_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of split_car_5d scaled by closeadj
def f098cae_f098_corporate_action_events_split_car_5d_mean_504d_base_v100_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

