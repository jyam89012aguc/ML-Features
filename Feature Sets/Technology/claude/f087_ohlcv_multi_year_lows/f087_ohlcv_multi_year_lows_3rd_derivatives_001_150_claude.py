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
def _f087_distlow(close, w):
    lo = close.rolling(w, min_periods=max(1, w//2)).min()
    return (close - lo) / lo.replace(0, np.nan).abs()


# 21d acceleration of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_accel_21d_3d_v001_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_accel_63d_3d_v002_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_accel_126d_3d_v003_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_accel_252d_3d_v004_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_accel_21d_3d_v005_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_accel_63d_3d_v006_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_accel_126d_3d_v007_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_accel_252d_3d_v008_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_accel_21d_3d_v009_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_accel_63d_3d_v010_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_accel_126d_3d_v011_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_accel_252d_3d_v012_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_accel_21d_3d_v013_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_accel_63d_3d_v014_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_accel_126d_3d_v015_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_accel_252d_3d_v016_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_accel_21d_3d_v017_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_accel_63d_3d_v018_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_accel_126d_3d_v019_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_accel_252d_3d_v020_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_accel_21d_3d_v021_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_accel_63d_3d_v022_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_accel_126d_3d_v023_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_accel_252d_3d_v024_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_accel_21d_3d_v025_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_accel_63d_3d_v026_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_accel_126d_3d_v027_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_accel_252d_3d_v028_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_slopez_21d_z126_3d_v029_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_slopez_63d_z252_3d_v030_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_slopez_126d_z252_3d_v031_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_slopez_252d_z504_3d_v032_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_slopez_21d_z126_3d_v033_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_slopez_63d_z252_3d_v034_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_slopez_126d_z252_3d_v035_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_slopez_252d_z504_3d_v036_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_slopez_21d_z126_3d_v037_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_slopez_63d_z252_3d_v038_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_slopez_126d_z252_3d_v039_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_slopez_252d_z504_3d_v040_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_slopez_21d_z126_3d_v041_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_slopez_63d_z252_3d_v042_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_slopez_126d_z252_3d_v043_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_slopez_252d_z504_3d_v044_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_slopez_21d_z126_3d_v045_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_slopez_63d_z252_3d_v046_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_slopez_126d_z252_3d_v047_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_slopez_252d_z504_3d_v048_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_slopez_21d_z126_3d_v049_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_slopez_63d_z252_3d_v050_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_slopez_126d_z252_3d_v051_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_slopez_252d_z504_3d_v052_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_slopez_21d_z126_3d_v053_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_slopez_63d_z252_3d_v054_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_slopez_126d_z252_3d_v055_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_slopez_252d_z504_3d_v056_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_jerk_21d_3d_v057_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_jerk_63d_3d_v058_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_jerk_126d_3d_v059_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_jerk_21d_3d_v060_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_jerk_63d_3d_v061_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_jerk_126d_3d_v062_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_jerk_21d_3d_v063_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_jerk_63d_3d_v064_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_jerk_126d_3d_v065_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_jerk_21d_3d_v066_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_jerk_63d_3d_v067_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_jerk_126d_3d_v068_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_jerk_21d_3d_v069_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_jerk_63d_3d_v070_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_jerk_126d_3d_v071_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_jerk_21d_3d_v072_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_jerk_63d_3d_v073_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_jerk_126d_3d_v074_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_jerk_21d_3d_v075_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_jerk_63d_3d_v076_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_jerk_126d_3d_v077_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of distlow_252d smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_smoothaccel_63d_sm252_3d_v078_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of distlow_252d smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_smoothaccel_252d_sm504_3d_v079_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of distlow_504d smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_smoothaccel_63d_sm252_3d_v080_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of distlow_504d smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_smoothaccel_252d_sm504_3d_v081_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of distlow_756d smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_smoothaccel_63d_sm252_3d_v082_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of distlow_756d smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_smoothaccel_252d_sm504_3d_v083_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of distlow_1260d smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_smoothaccel_63d_sm252_3d_v084_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of distlow_1260d smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_smoothaccel_252d_sm504_3d_v085_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of new_low_252_flag smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_smoothaccel_63d_sm252_3d_v086_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of new_low_252_flag smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_smoothaccel_252d_sm504_3d_v087_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of low_pctile_504 smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_smoothaccel_63d_sm252_3d_v088_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of low_pctile_504 smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_smoothaccel_252d_sm504_3d_v089_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of days_since_252low smoothed over 252d
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_smoothaccel_63d_sm252_3d_v090_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of days_since_252low smoothed over 504d
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_smoothaccel_252d_sm504_3d_v091_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_accelz_21d_z252_3d_v092_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_accelz_63d_z504_3d_v093_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_accelz_21d_z252_3d_v094_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_accelz_63d_z504_3d_v095_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_accelz_21d_z252_3d_v096_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_accelz_63d_z504_3d_v097_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_accelz_21d_z252_3d_v098_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_accelz_63d_z504_3d_v099_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_accelz_21d_z252_3d_v100_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_accelz_63d_z504_3d_v101_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_accelz_21d_z252_3d_v102_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_accelz_63d_z504_3d_v103_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_accelz_21d_z252_3d_v104_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of days_since_252low
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_accelz_63d_z504_3d_v105_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in distlow_252d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_signflip_63d_3d_v106_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in distlow_252d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_signflip_252d_3d_v107_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in distlow_504d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_signflip_63d_3d_v108_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in distlow_504d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_signflip_252d_3d_v109_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in distlow_756d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_signflip_63d_3d_v110_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in distlow_756d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_signflip_252d_3d_v111_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in distlow_1260d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_signflip_63d_3d_v112_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in distlow_1260d (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_signflip_252d_3d_v113_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in new_low_252_flag (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_signflip_63d_3d_v114_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in new_low_252_flag (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_signflip_252d_3d_v115_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in low_pctile_504 (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_signflip_63d_3d_v116_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in low_pctile_504 (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_signflip_252d_3d_v117_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in days_since_252low (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_signflip_63d_3d_v118_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in days_since_252low (raw count, no price scaling)
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_signflip_252d_3d_v119_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_252d normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_rngaccel_63d_r252_3d_v120_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_252d normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_rngaccel_252d_r504_3d_v121_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_504d normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_rngaccel_63d_r252_3d_v122_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_504d normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_rngaccel_252d_r504_3d_v123_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_756d normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_rngaccel_63d_r252_3d_v124_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_756d normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_rngaccel_252d_r504_3d_v125_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of distlow_1260d normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_rngaccel_63d_r252_3d_v126_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of distlow_1260d normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_rngaccel_252d_r504_3d_v127_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of new_low_252_flag normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_rngaccel_63d_r252_3d_v128_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of new_low_252_flag normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_rngaccel_252d_r504_3d_v129_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of low_pctile_504 normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_rngaccel_63d_r252_3d_v130_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of low_pctile_504 normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_rngaccel_252d_r504_3d_v131_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of days_since_252low normalized by 252d range
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_rngaccel_63d_r252_3d_v132_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of days_since_252low normalized by 504d range
def f087lo_f087_ohlcv_multi_year_lows_days_since_252low_rngaccel_252d_r504_3d_v133_signal(closeadj):
    base = (closeadj.rolling(252, min_periods=63).apply(lambda x: len(x) - 1 - x.values.argmin(), raw=False))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_cumslope_21d_3d_v134_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_cumslope_63d_3d_v135_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of distlow_252d
def f087lo_f087_ohlcv_multi_year_lows_distlow_252d_cumslope_252d_3d_v136_signal(closeadj):
    base = _f087_distlow(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_cumslope_21d_3d_v137_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_cumslope_63d_3d_v138_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of distlow_504d
def f087lo_f087_ohlcv_multi_year_lows_distlow_504d_cumslope_252d_3d_v139_signal(closeadj):
    base = _f087_distlow(closeadj, 504)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_cumslope_21d_3d_v140_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_cumslope_63d_3d_v141_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of distlow_756d
def f087lo_f087_ohlcv_multi_year_lows_distlow_756d_cumslope_252d_3d_v142_signal(closeadj):
    base = _f087_distlow(closeadj, 756)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_cumslope_21d_3d_v143_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_cumslope_63d_3d_v144_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of distlow_1260d
def f087lo_f087_ohlcv_multi_year_lows_distlow_1260d_cumslope_252d_3d_v145_signal(closeadj):
    base = _f087_distlow(closeadj, 1260)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_cumslope_21d_3d_v146_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_cumslope_63d_3d_v147_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of new_low_252_flag
def f087lo_f087_ohlcv_multi_year_lows_new_low_252_flag_cumslope_252d_3d_v148_signal(closeadj):
    base = (closeadj <= closeadj.rolling(252, min_periods=63).min()).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_cumslope_21d_3d_v149_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of low_pctile_504
def f087lo_f087_ohlcv_multi_year_lows_low_pctile_504_cumslope_63d_3d_v150_signal(closeadj):
    base = closeadj.rolling(504, min_periods=126).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

