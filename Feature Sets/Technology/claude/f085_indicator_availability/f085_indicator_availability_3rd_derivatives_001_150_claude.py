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
def _f085_cov(field_coverage_pct):
    return field_coverage_pct


# 21d acceleration of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_accel_21d_3d_v001_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_accel_63d_3d_v002_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_accel_126d_3d_v003_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_accel_252d_3d_v004_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_accel_21d_3d_v005_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_accel_63d_3d_v006_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_accel_126d_3d_v007_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_accel_252d_3d_v008_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_accel_21d_3d_v009_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_accel_63d_3d_v010_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_accel_126d_3d_v011_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_accel_252d_3d_v012_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of missing_share
def f085iav_f085_indicator_availability_missing_share_accel_21d_3d_v013_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of missing_share
def f085iav_f085_indicator_availability_missing_share_accel_63d_3d_v014_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of missing_share
def f085iav_f085_indicator_availability_missing_share_accel_126d_3d_v015_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of missing_share
def f085iav_f085_indicator_availability_missing_share_accel_252d_3d_v016_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_accel_21d_3d_v017_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_accel_63d_3d_v018_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_accel_126d_3d_v019_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_accel_252d_3d_v020_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_accel_21d_3d_v021_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_accel_63d_3d_v022_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_accel_126d_3d_v023_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_accel_252d_3d_v024_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_accel_21d_3d_v025_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_accel_63d_3d_v026_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_accel_126d_3d_v027_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_accel_252d_3d_v028_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slopez_21d_z126_3d_v029_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slopez_63d_z252_3d_v030_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slopez_126d_z252_3d_v031_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slopez_252d_z504_3d_v032_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slopez_21d_z126_3d_v033_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slopez_63d_z252_3d_v034_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slopez_126d_z252_3d_v035_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slopez_252d_z504_3d_v036_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slopez_21d_z126_3d_v037_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slopez_63d_z252_3d_v038_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slopez_126d_z252_3d_v039_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slopez_252d_z504_3d_v040_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of missing_share
def f085iav_f085_indicator_availability_missing_share_slopez_21d_z126_3d_v041_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of missing_share
def f085iav_f085_indicator_availability_missing_share_slopez_63d_z252_3d_v042_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of missing_share
def f085iav_f085_indicator_availability_missing_share_slopez_126d_z252_3d_v043_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of missing_share
def f085iav_f085_indicator_availability_missing_share_slopez_252d_z504_3d_v044_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slopez_21d_z126_3d_v045_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slopez_63d_z252_3d_v046_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slopez_126d_z252_3d_v047_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slopez_252d_z504_3d_v048_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slopez_21d_z126_3d_v049_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slopez_63d_z252_3d_v050_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slopez_126d_z252_3d_v051_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slopez_252d_z504_3d_v052_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slopez_21d_z126_3d_v053_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slopez_63d_z252_3d_v054_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slopez_126d_z252_3d_v055_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slopez_252d_z504_3d_v056_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_jerk_21d_3d_v057_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_jerk_63d_3d_v058_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_jerk_126d_3d_v059_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_jerk_21d_3d_v060_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_jerk_63d_3d_v061_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_jerk_126d_3d_v062_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_jerk_21d_3d_v063_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_jerk_63d_3d_v064_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_jerk_126d_3d_v065_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of missing_share
def f085iav_f085_indicator_availability_missing_share_jerk_21d_3d_v066_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of missing_share
def f085iav_f085_indicator_availability_missing_share_jerk_63d_3d_v067_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of missing_share
def f085iav_f085_indicator_availability_missing_share_jerk_126d_3d_v068_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_jerk_21d_3d_v069_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_jerk_63d_3d_v070_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_jerk_126d_3d_v071_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_jerk_21d_3d_v072_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_jerk_63d_3d_v073_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_jerk_126d_3d_v074_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_jerk_21d_3d_v075_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_jerk_63d_3d_v076_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_jerk_126d_3d_v077_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sf1_coverage smoothed over 252d
def f085iav_f085_indicator_availability_sf1_coverage_smoothaccel_63d_sm252_3d_v078_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sf1_coverage smoothed over 504d
def f085iav_f085_indicator_availability_sf1_coverage_smoothaccel_252d_sm504_3d_v079_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of daily_coverage smoothed over 252d
def f085iav_f085_indicator_availability_daily_coverage_smoothaccel_63d_sm252_3d_v080_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of daily_coverage smoothed over 504d
def f085iav_f085_indicator_availability_daily_coverage_smoothaccel_252d_sm504_3d_v081_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of missing_field_cnt smoothed over 252d
def f085iav_f085_indicator_availability_missing_field_cnt_smoothaccel_63d_sm252_3d_v082_signal(missing_field_count, closeadj):
    base = missing_field_count
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of missing_field_cnt smoothed over 504d
def f085iav_f085_indicator_availability_missing_field_cnt_smoothaccel_252d_sm504_3d_v083_signal(missing_field_count, closeadj):
    base = missing_field_count
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of missing_share smoothed over 252d
def f085iav_f085_indicator_availability_missing_share_smoothaccel_63d_sm252_3d_v084_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of missing_share smoothed over 504d
def f085iav_f085_indicator_availability_missing_share_smoothaccel_252d_sm504_3d_v085_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of coverage_pctile_y smoothed over 252d
def f085iav_f085_indicator_availability_coverage_pctile_y_smoothaccel_63d_sm252_3d_v086_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of coverage_pctile_y smoothed over 504d
def f085iav_f085_indicator_availability_coverage_pctile_y_smoothaccel_252d_sm504_3d_v087_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of low_coverage_flag smoothed over 252d
def f085iav_f085_indicator_availability_low_coverage_flag_smoothaccel_63d_sm252_3d_v088_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of low_coverage_flag smoothed over 504d
def f085iav_f085_indicator_availability_low_coverage_flag_smoothaccel_252d_sm504_3d_v089_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of coverage_yoy_chg smoothed over 252d
def f085iav_f085_indicator_availability_coverage_yoy_chg_smoothaccel_63d_sm252_3d_v090_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of coverage_yoy_chg smoothed over 504d
def f085iav_f085_indicator_availability_coverage_yoy_chg_smoothaccel_252d_sm504_3d_v091_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_accelz_21d_z252_3d_v092_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_accelz_63d_z504_3d_v093_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_accelz_21d_z252_3d_v094_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_accelz_63d_z504_3d_v095_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_accelz_21d_z252_3d_v096_signal(missing_field_count, closeadj):
    base = missing_field_count
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_accelz_63d_z504_3d_v097_signal(missing_field_count, closeadj):
    base = missing_field_count
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of missing_share
def f085iav_f085_indicator_availability_missing_share_accelz_21d_z252_3d_v098_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of missing_share
def f085iav_f085_indicator_availability_missing_share_accelz_63d_z504_3d_v099_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_accelz_21d_z252_3d_v100_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_accelz_63d_z504_3d_v101_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_accelz_21d_z252_3d_v102_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_accelz_63d_z504_3d_v103_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_accelz_21d_z252_3d_v104_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_accelz_63d_z504_3d_v105_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sf1_coverage (raw count, no price scaling)
def f085iav_f085_indicator_availability_sf1_coverage_signflip_63d_3d_v106_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in sf1_coverage (raw count, no price scaling)
def f085iav_f085_indicator_availability_sf1_coverage_signflip_252d_3d_v107_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in daily_coverage (raw count, no price scaling)
def f085iav_f085_indicator_availability_daily_coverage_signflip_63d_3d_v108_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in daily_coverage (raw count, no price scaling)
def f085iav_f085_indicator_availability_daily_coverage_signflip_252d_3d_v109_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in missing_field_cnt (raw count, no price scaling)
def f085iav_f085_indicator_availability_missing_field_cnt_signflip_63d_3d_v110_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in missing_field_cnt (raw count, no price scaling)
def f085iav_f085_indicator_availability_missing_field_cnt_signflip_252d_3d_v111_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in missing_share (raw count, no price scaling)
def f085iav_f085_indicator_availability_missing_share_signflip_63d_3d_v112_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in missing_share (raw count, no price scaling)
def f085iav_f085_indicator_availability_missing_share_signflip_252d_3d_v113_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in coverage_pctile_y (raw count, no price scaling)
def f085iav_f085_indicator_availability_coverage_pctile_y_signflip_63d_3d_v114_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in coverage_pctile_y (raw count, no price scaling)
def f085iav_f085_indicator_availability_coverage_pctile_y_signflip_252d_3d_v115_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in low_coverage_flag (raw count, no price scaling)
def f085iav_f085_indicator_availability_low_coverage_flag_signflip_63d_3d_v116_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in low_coverage_flag (raw count, no price scaling)
def f085iav_f085_indicator_availability_low_coverage_flag_signflip_252d_3d_v117_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in coverage_yoy_chg (raw count, no price scaling)
def f085iav_f085_indicator_availability_coverage_yoy_chg_signflip_63d_3d_v118_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in coverage_yoy_chg (raw count, no price scaling)
def f085iav_f085_indicator_availability_coverage_yoy_chg_signflip_252d_3d_v119_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sf1_coverage normalized by 252d range
def f085iav_f085_indicator_availability_sf1_coverage_rngaccel_63d_r252_3d_v120_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sf1_coverage normalized by 504d range
def f085iav_f085_indicator_availability_sf1_coverage_rngaccel_252d_r504_3d_v121_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of daily_coverage normalized by 252d range
def f085iav_f085_indicator_availability_daily_coverage_rngaccel_63d_r252_3d_v122_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of daily_coverage normalized by 504d range
def f085iav_f085_indicator_availability_daily_coverage_rngaccel_252d_r504_3d_v123_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of missing_field_cnt normalized by 252d range
def f085iav_f085_indicator_availability_missing_field_cnt_rngaccel_63d_r252_3d_v124_signal(missing_field_count, closeadj):
    base = missing_field_count
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of missing_field_cnt normalized by 504d range
def f085iav_f085_indicator_availability_missing_field_cnt_rngaccel_252d_r504_3d_v125_signal(missing_field_count, closeadj):
    base = missing_field_count
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of missing_share normalized by 252d range
def f085iav_f085_indicator_availability_missing_share_rngaccel_63d_r252_3d_v126_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of missing_share normalized by 504d range
def f085iav_f085_indicator_availability_missing_share_rngaccel_252d_r504_3d_v127_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of coverage_pctile_y normalized by 252d range
def f085iav_f085_indicator_availability_coverage_pctile_y_rngaccel_63d_r252_3d_v128_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of coverage_pctile_y normalized by 504d range
def f085iav_f085_indicator_availability_coverage_pctile_y_rngaccel_252d_r504_3d_v129_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of low_coverage_flag normalized by 252d range
def f085iav_f085_indicator_availability_low_coverage_flag_rngaccel_63d_r252_3d_v130_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of low_coverage_flag normalized by 504d range
def f085iav_f085_indicator_availability_low_coverage_flag_rngaccel_252d_r504_3d_v131_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of coverage_yoy_chg normalized by 252d range
def f085iav_f085_indicator_availability_coverage_yoy_chg_rngaccel_63d_r252_3d_v132_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of coverage_yoy_chg normalized by 504d range
def f085iav_f085_indicator_availability_coverage_yoy_chg_rngaccel_252d_r504_3d_v133_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_cumslope_21d_3d_v134_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_cumslope_63d_3d_v135_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_cumslope_252d_3d_v136_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_cumslope_21d_3d_v137_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_cumslope_63d_3d_v138_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_cumslope_252d_3d_v139_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_cumslope_21d_3d_v140_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_cumslope_63d_3d_v141_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_cumslope_252d_3d_v142_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of missing_share
def f085iav_f085_indicator_availability_missing_share_cumslope_21d_3d_v143_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of missing_share
def f085iav_f085_indicator_availability_missing_share_cumslope_63d_3d_v144_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of missing_share
def f085iav_f085_indicator_availability_missing_share_cumslope_252d_3d_v145_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_cumslope_21d_3d_v146_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_cumslope_63d_3d_v147_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_cumslope_252d_3d_v148_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_cumslope_21d_3d_v149_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_cumslope_63d_3d_v150_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

