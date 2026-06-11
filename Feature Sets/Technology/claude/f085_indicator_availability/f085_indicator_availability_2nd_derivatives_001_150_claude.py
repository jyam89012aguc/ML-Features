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


# 21d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slope_21d_2d_v001_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slope_63d_2d_v002_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slope_126d_2d_v003_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slope_252d_2d_v004_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_slope_504d_2d_v005_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slope_21d_2d_v006_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slope_63d_2d_v007_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slope_126d_2d_v008_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slope_252d_2d_v009_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_slope_504d_2d_v010_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slope_21d_2d_v011_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slope_63d_2d_v012_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slope_126d_2d_v013_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slope_252d_2d_v014_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_slope_504d_2d_v015_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_slope_21d_2d_v016_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_slope_63d_2d_v017_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_slope_126d_2d_v018_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_slope_252d_2d_v019_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_slope_504d_2d_v020_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slope_21d_2d_v021_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slope_63d_2d_v022_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slope_126d_2d_v023_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slope_252d_2d_v024_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_slope_504d_2d_v025_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slope_21d_2d_v026_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slope_63d_2d_v027_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slope_126d_2d_v028_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slope_252d_2d_v029_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_slope_504d_2d_v030_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slope_21d_2d_v031_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slope_63d_2d_v032_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slope_126d_2d_v033_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slope_252d_2d_v034_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_slope_504d_2d_v035_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sm21_sl21_2d_v036_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sm63_sl21_2d_v037_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sm63_sl63_2d_v038_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sm252_sl63_2d_v039_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sm252_sl126_2d_v040_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sm21_sl21_2d_v041_signal(daily_coverage_pct, closeadj):
    base = _mean(daily_coverage_pct, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sm63_sl21_2d_v042_signal(daily_coverage_pct, closeadj):
    base = _mean(daily_coverage_pct, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sm63_sl63_2d_v043_signal(daily_coverage_pct, closeadj):
    base = _mean(daily_coverage_pct, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sm252_sl63_2d_v044_signal(daily_coverage_pct, closeadj):
    base = _mean(daily_coverage_pct, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sm252_sl126_2d_v045_signal(daily_coverage_pct, closeadj):
    base = _mean(daily_coverage_pct, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sm21_sl21_2d_v046_signal(missing_field_count, closeadj):
    base = _mean(missing_field_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sm63_sl21_2d_v047_signal(missing_field_count, closeadj):
    base = _mean(missing_field_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sm63_sl63_2d_v048_signal(missing_field_count, closeadj):
    base = _mean(missing_field_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sm252_sl63_2d_v049_signal(missing_field_count, closeadj):
    base = _mean(missing_field_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sm252_sl126_2d_v050_signal(missing_field_count, closeadj):
    base = _mean(missing_field_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sm21_sl21_2d_v051_signal(missing_field_count, available_field_count, closeadj):
    base = _mean(missing_field_count / available_field_count.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sm63_sl21_2d_v052_signal(missing_field_count, available_field_count, closeadj):
    base = _mean(missing_field_count / available_field_count.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sm63_sl63_2d_v053_signal(missing_field_count, available_field_count, closeadj):
    base = _mean(missing_field_count / available_field_count.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sm252_sl63_2d_v054_signal(missing_field_count, available_field_count, closeadj):
    base = _mean(missing_field_count / available_field_count.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sm252_sl126_2d_v055_signal(missing_field_count, available_field_count, closeadj):
    base = _mean(missing_field_count / available_field_count.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sm21_sl21_2d_v056_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sm63_sl21_2d_v057_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sm63_sl63_2d_v058_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sm252_sl63_2d_v059_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sm252_sl126_2d_v060_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sm21_sl21_2d_v061_signal(sf1_coverage_pct, closeadj):
    base = _mean((sf1_coverage_pct < 0.7).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sm63_sl21_2d_v062_signal(sf1_coverage_pct, closeadj):
    base = _mean((sf1_coverage_pct < 0.7).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sm63_sl63_2d_v063_signal(sf1_coverage_pct, closeadj):
    base = _mean((sf1_coverage_pct < 0.7).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sm252_sl63_2d_v064_signal(sf1_coverage_pct, closeadj):
    base = _mean((sf1_coverage_pct < 0.7).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sm252_sl126_2d_v065_signal(sf1_coverage_pct, closeadj):
    base = _mean((sf1_coverage_pct < 0.7).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sm21_sl21_2d_v066_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sm63_sl21_2d_v067_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sm63_sl63_2d_v068_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sm252_sl63_2d_v069_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sm252_sl126_2d_v070_signal(sf1_coverage_pct, closeadj):
    base = _mean(sf1_coverage_pct.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_pctslope_21d_2d_v071_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_pctslope_63d_2d_v072_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_pctslope_252d_2d_v073_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_pctslope_21d_2d_v074_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_pctslope_63d_2d_v075_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_pctslope_252d_2d_v076_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_pctslope_21d_2d_v077_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_pctslope_63d_2d_v078_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_pctslope_252d_2d_v079_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of missing_share
def f085iav_f085_indicator_availability_missing_share_pctslope_21d_2d_v080_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of missing_share
def f085iav_f085_indicator_availability_missing_share_pctslope_63d_2d_v081_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of missing_share
def f085iav_f085_indicator_availability_missing_share_pctslope_252d_2d_v082_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_pctslope_21d_2d_v083_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_pctslope_63d_2d_v084_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_pctslope_252d_2d_v085_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_pctslope_21d_2d_v086_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_pctslope_63d_2d_v087_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_pctslope_252d_2d_v088_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_pctslope_21d_2d_v089_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_pctslope_63d_2d_v090_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_pctslope_252d_2d_v091_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sgnslope_21d_2d_v092_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sgnslope_63d_2d_v093_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_sgnslope_252d_2d_v094_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sgnslope_21d_2d_v095_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sgnslope_63d_2d_v096_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_sgnslope_252d_2d_v097_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sgnslope_21d_2d_v098_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sgnslope_63d_2d_v099_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_sgnslope_252d_2d_v100_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sgnslope_21d_2d_v101_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sgnslope_63d_2d_v102_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_sgnslope_252d_2d_v103_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sgnslope_21d_2d_v104_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sgnslope_63d_2d_v105_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_sgnslope_252d_2d_v106_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sgnslope_21d_2d_v107_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sgnslope_63d_2d_v108_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_sgnslope_252d_2d_v109_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sgnslope_21d_2d_v110_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sgnslope_63d_2d_v111_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_sgnslope_252d_2d_v112_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_logmagslope_21d_2d_v113_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_logmagslope_63d_2d_v114_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_logmagslope_252d_2d_v115_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_logmagslope_21d_2d_v116_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_logmagslope_63d_2d_v117_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_logmagslope_252d_2d_v118_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_logmagslope_21d_2d_v119_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_logmagslope_63d_2d_v120_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_logmagslope_252d_2d_v121_signal(missing_field_count, closeadj):
    base = missing_field_count
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_logmagslope_21d_2d_v122_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_logmagslope_63d_2d_v123_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of missing_share
def f085iav_f085_indicator_availability_missing_share_logmagslope_252d_2d_v124_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_logmagslope_21d_2d_v125_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_logmagslope_63d_2d_v126_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_logmagslope_252d_2d_v127_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_logmagslope_21d_2d_v128_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_logmagslope_63d_2d_v129_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_logmagslope_252d_2d_v130_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_logmagslope_21d_2d_v131_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_logmagslope_63d_2d_v132_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_logmagslope_252d_2d_v133_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|sf1_coverage|
def f085iav_f085_indicator_availability_sf1_coverage_logslope_63d_2d_v134_signal(sf1_coverage_pct, closeadj):
    base = np.log((sf1_coverage_pct).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|sf1_coverage|
def f085iav_f085_indicator_availability_sf1_coverage_logslope_252d_2d_v135_signal(sf1_coverage_pct, closeadj):
    base = np.log((sf1_coverage_pct).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|daily_coverage|
def f085iav_f085_indicator_availability_daily_coverage_logslope_63d_2d_v136_signal(daily_coverage_pct, closeadj):
    base = np.log((daily_coverage_pct).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|daily_coverage|
def f085iav_f085_indicator_availability_daily_coverage_logslope_252d_2d_v137_signal(daily_coverage_pct, closeadj):
    base = np.log((daily_coverage_pct).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|missing_field_cnt|
def f085iav_f085_indicator_availability_missing_field_cnt_logslope_63d_2d_v138_signal(missing_field_count, closeadj):
    base = np.log((missing_field_count).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|missing_field_cnt|
def f085iav_f085_indicator_availability_missing_field_cnt_logslope_252d_2d_v139_signal(missing_field_count, closeadj):
    base = np.log((missing_field_count).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|missing_share|
def f085iav_f085_indicator_availability_missing_share_logslope_63d_2d_v140_signal(missing_field_count, available_field_count, closeadj):
    base = np.log((missing_field_count / available_field_count.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|missing_share|
def f085iav_f085_indicator_availability_missing_share_logslope_252d_2d_v141_signal(missing_field_count, available_field_count, closeadj):
    base = np.log((missing_field_count / available_field_count.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|coverage_pctile_y|
def f085iav_f085_indicator_availability_coverage_pctile_y_logslope_63d_2d_v142_signal(sf1_coverage_pct, closeadj):
    base = np.log((sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|coverage_pctile_y|
def f085iav_f085_indicator_availability_coverage_pctile_y_logslope_252d_2d_v143_signal(sf1_coverage_pct, closeadj):
    base = np.log((sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|low_coverage_flag|
def f085iav_f085_indicator_availability_low_coverage_flag_logslope_63d_2d_v144_signal(sf1_coverage_pct, closeadj):
    base = np.log(((sf1_coverage_pct < 0.7).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|low_coverage_flag|
def f085iav_f085_indicator_availability_low_coverage_flag_logslope_252d_2d_v145_signal(sf1_coverage_pct, closeadj):
    base = np.log(((sf1_coverage_pct < 0.7).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|coverage_yoy_chg|
def f085iav_f085_indicator_availability_coverage_yoy_chg_logslope_63d_2d_v146_signal(sf1_coverage_pct, closeadj):
    base = np.log((sf1_coverage_pct.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|coverage_yoy_chg|
def f085iav_f085_indicator_availability_coverage_yoy_chg_logslope_252d_2d_v147_signal(sf1_coverage_pct, closeadj):
    base = np.log((sf1_coverage_pct.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

