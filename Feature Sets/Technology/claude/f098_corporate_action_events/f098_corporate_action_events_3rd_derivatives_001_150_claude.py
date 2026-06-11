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


# 21d acceleration of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_accel_21d_3d_v001_signal(action_count, closeadj):
    base = action_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_accel_63d_3d_v002_signal(action_count, closeadj):
    base = action_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_accel_126d_3d_v003_signal(action_count, closeadj):
    base = action_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_accel_252d_3d_v004_signal(action_count, closeadj):
    base = action_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_accel_21d_3d_v005_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_accel_63d_3d_v006_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_accel_126d_3d_v007_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_accel_252d_3d_v008_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_accel_21d_3d_v009_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_accel_63d_3d_v010_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_accel_126d_3d_v011_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_accel_252d_3d_v012_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_accel_21d_3d_v013_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_accel_63d_3d_v014_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_accel_126d_3d_v015_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_accel_252d_3d_v016_signal(split_event_flag, closeadj):
    base = split_event_flag
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_accel_21d_3d_v017_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_accel_63d_3d_v018_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_accel_126d_3d_v019_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_accel_252d_3d_v020_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_accel_21d_3d_v021_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_accel_63d_3d_v022_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_accel_126d_3d_v023_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_accel_252d_3d_v024_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_accel_21d_3d_v025_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_accel_63d_3d_v026_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_accel_126d_3d_v027_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_accel_252d_3d_v028_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_accel_21d_3d_v029_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_accel_63d_3d_v030_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_accel_126d_3d_v031_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_accel_252d_3d_v032_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_accel_21d_3d_v033_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_accel_63d_3d_v034_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_accel_126d_3d_v035_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_accel_252d_3d_v036_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_accel_21d_3d_v037_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_accel_63d_3d_v038_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_accel_126d_3d_v039_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_accel_252d_3d_v040_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_accel_21d_3d_v041_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_accel_63d_3d_v042_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_accel_126d_3d_v043_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_accel_252d_3d_v044_signal(ma_days_since, closeadj):
    base = ma_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_accel_21d_3d_v045_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_accel_63d_3d_v046_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_accel_126d_3d_v047_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_accel_252d_3d_v048_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_accel_21d_3d_v049_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_accel_63d_3d_v050_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_accel_126d_3d_v051_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_accel_252d_3d_v052_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_accel_21d_3d_v053_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_accel_63d_3d_v054_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_accel_126d_3d_v055_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_accel_252d_3d_v056_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_accel_21d_3d_v057_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_accel_63d_3d_v058_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_accel_126d_3d_v059_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_accel_252d_3d_v060_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_accel_21d_3d_v061_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_accel_63d_3d_v062_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_accel_126d_3d_v063_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_accel_252d_3d_v064_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_accel_21d_3d_v065_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_accel_63d_3d_v066_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_accel_126d_3d_v067_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_accel_252d_3d_v068_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_accel_21d_3d_v069_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_accel_63d_3d_v070_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_accel_126d_3d_v071_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_accel_252d_3d_v072_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_accel_21d_3d_v073_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_accel_63d_3d_v074_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_accel_126d_3d_v075_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_accel_252d_3d_v076_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_accel_21d_3d_v077_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_accel_63d_3d_v078_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_accel_126d_3d_v079_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_accel_252d_3d_v080_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_accel_21d_3d_v081_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_accel_63d_3d_v082_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_accel_126d_3d_v083_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_accel_252d_3d_v084_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_accel_21d_3d_v085_signal(split_days_since, closeadj):
    base = split_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_accel_63d_3d_v086_signal(split_days_since, closeadj):
    base = split_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_accel_126d_3d_v087_signal(split_days_since, closeadj):
    base = split_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_accel_252d_3d_v088_signal(split_days_since, closeadj):
    base = split_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_accel_21d_3d_v089_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_accel_63d_3d_v090_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_accel_126d_3d_v091_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of spinoff_car_21d
def f098cae_f098_corporate_action_events_spinoff_car_21d_accel_252d_3d_v092_signal(abnormal_return_d, spinoff_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_accel_21d_3d_v093_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_accel_63d_3d_v094_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_accel_126d_3d_v095_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of spinoff_car_63d
def f098cae_f098_corporate_action_events_spinoff_car_63d_accel_252d_3d_v096_signal(abnormal_return_d, spinoff_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, spinoff_window_63d, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_accel_21d_3d_v097_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_accel_63d_3d_v098_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_accel_126d_3d_v099_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of spinoff_days_since
def f098cae_f098_corporate_action_events_spinoff_days_since_accel_252d_3d_v100_signal(spinoff_days_since, closeadj):
    base = spinoff_days_since
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_accel_21d_3d_v101_signal(dividend_value, closeadj):
    base = dividend_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_accel_63d_3d_v102_signal(dividend_value, closeadj):
    base = dividend_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_accel_126d_3d_v103_signal(dividend_value, closeadj):
    base = dividend_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_value_per_share
def f098cae_f098_corporate_action_events_dividend_value_per_share_accel_252d_3d_v104_signal(dividend_value, closeadj):
    base = dividend_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_accel_21d_3d_v105_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_accel_63d_3d_v106_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_accel_126d_3d_v107_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dividend_value_yield_proxy
def f098cae_f098_corporate_action_events_dividend_value_yield_proxy_accel_252d_3d_v108_signal(dividend_value, close, closeadj):
    base = dividend_value / close.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_accel_21d_3d_v109_signal(split_value, closeadj):
    base = split_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_accel_63d_3d_v110_signal(split_value, closeadj):
    base = split_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_accel_126d_3d_v111_signal(split_value, closeadj):
    base = split_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of split_ratio_value
def f098cae_f098_corporate_action_events_split_ratio_value_accel_252d_3d_v112_signal(split_value, closeadj):
    base = split_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slopez_21d_z126_3d_v113_signal(action_count, closeadj):
    base = action_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slopez_63d_z252_3d_v114_signal(action_count, closeadj):
    base = action_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slopez_126d_z252_3d_v115_signal(action_count, closeadj):
    base = action_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of any_action_cnt
def f098cae_f098_corporate_action_events_any_action_cnt_slopez_252d_z504_3d_v116_signal(action_count, closeadj):
    base = action_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slopez_21d_z126_3d_v117_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slopez_63d_z252_3d_v118_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slopez_126d_z252_3d_v119_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of any_action_252d
def f098cae_f098_corporate_action_events_any_action_252d_slopez_252d_z504_3d_v120_signal(action_count, closeadj):
    base = _f098_action_density(action_count, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slopez_21d_z126_3d_v121_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slopez_63d_z252_3d_v122_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slopez_126d_z252_3d_v123_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dividend_event_flag
def f098cae_f098_corporate_action_events_dividend_event_flag_slopez_252d_z504_3d_v124_signal(dividend_event_flag, closeadj):
    base = dividend_event_flag
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slopez_21d_z126_3d_v125_signal(split_event_flag, closeadj):
    base = split_event_flag
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slopez_63d_z252_3d_v126_signal(split_event_flag, closeadj):
    base = split_event_flag
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slopez_126d_z252_3d_v127_signal(split_event_flag, closeadj):
    base = split_event_flag
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of split_event_flag
def f098cae_f098_corporate_action_events_split_event_flag_slopez_252d_z504_3d_v128_signal(split_event_flag, closeadj):
    base = split_event_flag
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slopez_21d_z126_3d_v129_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slopez_63d_z252_3d_v130_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slopez_126d_z252_3d_v131_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of reverse_split_flag
def f098cae_f098_corporate_action_events_reverse_split_flag_slopez_252d_z504_3d_v132_signal(reverse_split_flag, closeadj):
    base = reverse_split_flag
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slopez_21d_z126_3d_v133_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slopez_63d_z252_3d_v134_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slopez_126d_z252_3d_v135_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_event_flag
def f098cae_f098_corporate_action_events_ma_event_flag_slopez_252d_z504_3d_v136_signal(ma_event_flag, closeadj):
    base = ma_event_flag
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slopez_21d_z126_3d_v137_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slopez_63d_z252_3d_v138_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slopez_126d_z252_3d_v139_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of spinoff_event_flag
def f098cae_f098_corporate_action_events_spinoff_event_flag_slopez_252d_z504_3d_v140_signal(spinoff_event_flag, closeadj):
    base = spinoff_event_flag
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slopez_21d_z126_3d_v141_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slopez_63d_z252_3d_v142_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slopez_126d_z252_3d_v143_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_car_5d
def f098cae_f098_corporate_action_events_ma_car_5d_slopez_252d_z504_3d_v144_signal(abnormal_return_d, ma_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slopez_21d_z126_3d_v145_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slopez_63d_z252_3d_v146_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slopez_126d_z252_3d_v147_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_car_21d
def f098cae_f098_corporate_action_events_ma_car_21d_slopez_252d_z504_3d_v148_signal(abnormal_return_d, ma_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slopez_21d_z126_3d_v149_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slopez_63d_z252_3d_v150_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slopez_126d_z252_3d_v151_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_car_63d
def f098cae_f098_corporate_action_events_ma_car_63d_slopez_252d_z504_3d_v152_signal(abnormal_return_d, ma_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, ma_window_63d, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slopez_21d_z126_3d_v153_signal(ma_days_since, closeadj):
    base = ma_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slopez_63d_z252_3d_v154_signal(ma_days_since, closeadj):
    base = ma_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slopez_126d_z252_3d_v155_signal(ma_days_since, closeadj):
    base = ma_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_days_since
def f098cae_f098_corporate_action_events_ma_days_since_slopez_252d_z504_3d_v156_signal(ma_days_since, closeadj):
    base = ma_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slopez_21d_z126_3d_v157_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slopez_63d_z252_3d_v158_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slopez_126d_z252_3d_v159_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ma_vol_surge_5d
def f098cae_f098_corporate_action_events_ma_vol_surge_5d_slopez_252d_z504_3d_v160_signal(volume, ma_window_5d, closeadj):
    base = _f098_vol_surge(volume, ma_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slopez_21d_z126_3d_v161_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slopez_63d_z252_3d_v162_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slopez_126d_z252_3d_v163_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dividend_car_5d
def f098cae_f098_corporate_action_events_dividend_car_5d_slopez_252d_z504_3d_v164_signal(abnormal_return_d, dividend_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slopez_21d_z126_3d_v165_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slopez_63d_z252_3d_v166_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slopez_126d_z252_3d_v167_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dividend_car_21d
def f098cae_f098_corporate_action_events_dividend_car_21d_slopez_252d_z504_3d_v168_signal(abnormal_return_d, dividend_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slopez_21d_z126_3d_v169_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slopez_63d_z252_3d_v170_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slopez_126d_z252_3d_v171_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dividend_days_since
def f098cae_f098_corporate_action_events_dividend_days_since_slopez_252d_z504_3d_v172_signal(dividend_days_since, closeadj):
    base = dividend_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slopez_21d_z126_3d_v173_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slopez_63d_z252_3d_v174_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slopez_126d_z252_3d_v175_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dividend_init_car_63d
def f098cae_f098_corporate_action_events_dividend_init_car_63d_slopez_252d_z504_3d_v176_signal(abnormal_return_d, dividend_init_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, dividend_init_window_63d, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slopez_21d_z126_3d_v177_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slopez_63d_z252_3d_v178_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slopez_126d_z252_3d_v179_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of reverse_split_car_21d
def f098cae_f098_corporate_action_events_reverse_split_car_21d_slopez_252d_z504_3d_v180_signal(abnormal_return_d, reverse_split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slopez_21d_z126_3d_v181_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slopez_63d_z252_3d_v182_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slopez_126d_z252_3d_v183_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of reverse_split_car_63d
def f098cae_f098_corporate_action_events_reverse_split_car_63d_slopez_252d_z504_3d_v184_signal(abnormal_return_d, reverse_split_window_63d, closeadj):
    base = _f098_car_window(abnormal_return_d, reverse_split_window_63d, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slopez_21d_z126_3d_v185_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slopez_63d_z252_3d_v186_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slopez_126d_z252_3d_v187_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of reverse_split_days_since
def f098cae_f098_corporate_action_events_reverse_split_days_since_slopez_252d_z504_3d_v188_signal(reverse_split_days_since, closeadj):
    base = reverse_split_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slopez_21d_z126_3d_v189_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slopez_63d_z252_3d_v190_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slopez_126d_z252_3d_v191_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of split_car_5d
def f098cae_f098_corporate_action_events_split_car_5d_slopez_252d_z504_3d_v192_signal(abnormal_return_d, split_window_5d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slopez_21d_z126_3d_v193_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slopez_63d_z252_3d_v194_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slopez_126d_z252_3d_v195_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of split_car_21d
def f098cae_f098_corporate_action_events_split_car_21d_slopez_252d_z504_3d_v196_signal(abnormal_return_d, split_window_21d, closeadj):
    base = _f098_car_window(abnormal_return_d, split_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slopez_21d_z126_3d_v197_signal(split_days_since, closeadj):
    base = split_days_since
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slopez_63d_z252_3d_v198_signal(split_days_since, closeadj):
    base = split_days_since
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slopez_126d_z252_3d_v199_signal(split_days_since, closeadj):
    base = split_days_since
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of split_days_since
def f098cae_f098_corporate_action_events_split_days_since_slopez_252d_z504_3d_v200_signal(split_days_since, closeadj):
    base = split_days_since
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

