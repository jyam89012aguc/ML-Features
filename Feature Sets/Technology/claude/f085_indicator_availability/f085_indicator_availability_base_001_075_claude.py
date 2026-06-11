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
def _f085_cov(field_coverage_pct):
    return field_coverage_pct


# 21d mean of sf1_coverage scaled by closeadj
def f085iav_f085_indicator_availability_sf1_coverage_mean_21d_base_v001_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sf1_coverage scaled by closeadj
def f085iav_f085_indicator_availability_sf1_coverage_mean_63d_base_v002_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sf1_coverage scaled by closeadj
def f085iav_f085_indicator_availability_sf1_coverage_mean_126d_base_v003_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sf1_coverage scaled by closeadj
def f085iav_f085_indicator_availability_sf1_coverage_mean_252d_base_v004_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sf1_coverage scaled by closeadj
def f085iav_f085_indicator_availability_sf1_coverage_mean_504d_base_v005_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of daily_coverage scaled by closeadj
def f085iav_f085_indicator_availability_daily_coverage_mean_21d_base_v006_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of daily_coverage scaled by closeadj
def f085iav_f085_indicator_availability_daily_coverage_mean_63d_base_v007_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of daily_coverage scaled by closeadj
def f085iav_f085_indicator_availability_daily_coverage_mean_126d_base_v008_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of daily_coverage scaled by closeadj
def f085iav_f085_indicator_availability_daily_coverage_mean_252d_base_v009_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of daily_coverage scaled by closeadj
def f085iav_f085_indicator_availability_daily_coverage_mean_504d_base_v010_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of missing_field_cnt scaled by closeadj
def f085iav_f085_indicator_availability_missing_field_cnt_mean_21d_base_v011_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of missing_field_cnt scaled by closeadj
def f085iav_f085_indicator_availability_missing_field_cnt_mean_63d_base_v012_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of missing_field_cnt scaled by closeadj
def f085iav_f085_indicator_availability_missing_field_cnt_mean_126d_base_v013_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of missing_field_cnt scaled by closeadj
def f085iav_f085_indicator_availability_missing_field_cnt_mean_252d_base_v014_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of missing_field_cnt scaled by closeadj
def f085iav_f085_indicator_availability_missing_field_cnt_mean_504d_base_v015_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of missing_share scaled by closeadj
def f085iav_f085_indicator_availability_missing_share_mean_21d_base_v016_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of missing_share scaled by closeadj
def f085iav_f085_indicator_availability_missing_share_mean_63d_base_v017_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of missing_share scaled by closeadj
def f085iav_f085_indicator_availability_missing_share_mean_126d_base_v018_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of missing_share scaled by closeadj
def f085iav_f085_indicator_availability_missing_share_mean_252d_base_v019_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of missing_share scaled by closeadj
def f085iav_f085_indicator_availability_missing_share_mean_504d_base_v020_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of coverage_pctile_y scaled by closeadj
def f085iav_f085_indicator_availability_coverage_pctile_y_mean_21d_base_v021_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of coverage_pctile_y scaled by closeadj
def f085iav_f085_indicator_availability_coverage_pctile_y_mean_63d_base_v022_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of coverage_pctile_y scaled by closeadj
def f085iav_f085_indicator_availability_coverage_pctile_y_mean_126d_base_v023_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of coverage_pctile_y scaled by closeadj
def f085iav_f085_indicator_availability_coverage_pctile_y_mean_252d_base_v024_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of coverage_pctile_y scaled by closeadj
def f085iav_f085_indicator_availability_coverage_pctile_y_mean_504d_base_v025_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of low_coverage_flag scaled by closeadj
def f085iav_f085_indicator_availability_low_coverage_flag_mean_21d_base_v026_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of low_coverage_flag scaled by closeadj
def f085iav_f085_indicator_availability_low_coverage_flag_mean_63d_base_v027_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of low_coverage_flag scaled by closeadj
def f085iav_f085_indicator_availability_low_coverage_flag_mean_126d_base_v028_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of low_coverage_flag scaled by closeadj
def f085iav_f085_indicator_availability_low_coverage_flag_mean_252d_base_v029_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of low_coverage_flag scaled by closeadj
def f085iav_f085_indicator_availability_low_coverage_flag_mean_504d_base_v030_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of coverage_yoy_chg scaled by closeadj
def f085iav_f085_indicator_availability_coverage_yoy_chg_mean_21d_base_v031_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of coverage_yoy_chg scaled by closeadj
def f085iav_f085_indicator_availability_coverage_yoy_chg_mean_63d_base_v032_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of coverage_yoy_chg scaled by closeadj
def f085iav_f085_indicator_availability_coverage_yoy_chg_mean_126d_base_v033_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of coverage_yoy_chg scaled by closeadj
def f085iav_f085_indicator_availability_coverage_yoy_chg_mean_252d_base_v034_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of coverage_yoy_chg scaled by closeadj
def f085iav_f085_indicator_availability_coverage_yoy_chg_mean_504d_base_v035_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_median_63d_base_v036_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_median_252d_base_v037_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_median_504d_base_v038_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_median_63d_base_v039_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_median_252d_base_v040_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_median_504d_base_v041_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_median_63d_base_v042_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_median_252d_base_v043_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_median_504d_base_v044_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of missing_share
def f085iav_f085_indicator_availability_missing_share_median_63d_base_v045_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of missing_share
def f085iav_f085_indicator_availability_missing_share_median_252d_base_v046_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of missing_share
def f085iav_f085_indicator_availability_missing_share_median_504d_base_v047_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_median_63d_base_v048_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_median_252d_base_v049_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_median_504d_base_v050_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_median_63d_base_v051_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_median_252d_base_v052_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_median_504d_base_v053_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_median_63d_base_v054_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_median_252d_base_v055_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_median_504d_base_v056_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_rmax_252d_base_v057_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_rmax_504d_base_v058_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_rmax_252d_base_v059_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_rmax_504d_base_v060_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_rmax_252d_base_v061_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_rmax_504d_base_v062_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of missing_share
def f085iav_f085_indicator_availability_missing_share_rmax_252d_base_v063_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of missing_share
def f085iav_f085_indicator_availability_missing_share_rmax_504d_base_v064_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_rmax_252d_base_v065_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_rmax_504d_base_v066_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_rmax_252d_base_v067_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_rmax_504d_base_v068_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_rmax_252d_base_v069_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_rmax_504d_base_v070_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_rmin_252d_base_v071_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_rmin_504d_base_v072_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_rmin_252d_base_v073_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_rmin_504d_base_v074_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_rmin_252d_base_v075_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

