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


# 63d z-score of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_z_63d_base_v076_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_z_126d_base_v077_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_z_252d_base_v078_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_z_504d_base_v079_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_z_63d_base_v080_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_z_126d_base_v081_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_z_252d_base_v082_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_z_504d_base_v083_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_z_63d_base_v084_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_z_126d_base_v085_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_z_252d_base_v086_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_z_504d_base_v087_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of missing_share
def f085iav_f085_indicator_availability_missing_share_z_63d_base_v088_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of missing_share
def f085iav_f085_indicator_availability_missing_share_z_126d_base_v089_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of missing_share
def f085iav_f085_indicator_availability_missing_share_z_252d_base_v090_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of missing_share
def f085iav_f085_indicator_availability_missing_share_z_504d_base_v091_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_z_63d_base_v092_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_z_126d_base_v093_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_z_252d_base_v094_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_z_504d_base_v095_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_z_63d_base_v096_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_z_126d_base_v097_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_z_252d_base_v098_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_z_504d_base_v099_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_z_63d_base_v100_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_z_126d_base_v101_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_z_252d_base_v102_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_z_504d_base_v103_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_distmax_252d_base_v104_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_distmax_504d_base_v105_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_distmax_252d_base_v106_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_distmax_504d_base_v107_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_distmax_252d_base_v108_signal(missing_field_count, closeadj):
    base = missing_field_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_distmax_504d_base_v109_signal(missing_field_count, closeadj):
    base = missing_field_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of missing_share
def f085iav_f085_indicator_availability_missing_share_distmax_252d_base_v110_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of missing_share
def f085iav_f085_indicator_availability_missing_share_distmax_504d_base_v111_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_distmax_252d_base_v112_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_distmax_504d_base_v113_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_distmax_252d_base_v114_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_distmax_504d_base_v115_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_distmax_252d_base_v116_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_distmax_504d_base_v117_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_distmed_126d_base_v118_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_distmed_252d_base_v119_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_distmed_504d_base_v120_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_distmed_126d_base_v121_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_distmed_252d_base_v122_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_distmed_504d_base_v123_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_distmed_126d_base_v124_signal(missing_field_count, closeadj):
    base = missing_field_count
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_distmed_252d_base_v125_signal(missing_field_count, closeadj):
    base = missing_field_count
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_distmed_504d_base_v126_signal(missing_field_count, closeadj):
    base = missing_field_count
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of missing_share
def f085iav_f085_indicator_availability_missing_share_distmed_126d_base_v127_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of missing_share
def f085iav_f085_indicator_availability_missing_share_distmed_252d_base_v128_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of missing_share
def f085iav_f085_indicator_availability_missing_share_distmed_504d_base_v129_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_distmed_126d_base_v130_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_distmed_252d_base_v131_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_distmed_504d_base_v132_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_distmed_126d_base_v133_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_distmed_252d_base_v134_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_distmed_504d_base_v135_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_distmed_126d_base_v136_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_distmed_252d_base_v137_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of coverage_yoy_chg
def f085iav_f085_indicator_availability_coverage_yoy_chg_distmed_504d_base_v138_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_chg_63d_base_v139_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in sf1_coverage
def f085iav_f085_indicator_availability_sf1_coverage_chg_252d_base_v140_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_chg_63d_base_v141_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in daily_coverage
def f085iav_f085_indicator_availability_daily_coverage_chg_252d_base_v142_signal(daily_coverage_pct, closeadj):
    base = daily_coverage_pct
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_chg_63d_base_v143_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in missing_field_cnt
def f085iav_f085_indicator_availability_missing_field_cnt_chg_252d_base_v144_signal(missing_field_count, closeadj):
    base = missing_field_count
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in missing_share
def f085iav_f085_indicator_availability_missing_share_chg_63d_base_v145_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in missing_share
def f085iav_f085_indicator_availability_missing_share_chg_252d_base_v146_signal(missing_field_count, available_field_count, closeadj):
    base = missing_field_count / available_field_count.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_chg_63d_base_v147_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in coverage_pctile_y
def f085iav_f085_indicator_availability_coverage_pctile_y_chg_252d_base_v148_signal(sf1_coverage_pct, closeadj):
    base = sf1_coverage_pct.rolling(252, min_periods=63).rank(pct=True)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_chg_63d_base_v149_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in low_coverage_flag
def f085iav_f085_indicator_availability_low_coverage_flag_chg_252d_base_v150_signal(sf1_coverage_pct, closeadj):
    base = (sf1_coverage_pct < 0.7).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

