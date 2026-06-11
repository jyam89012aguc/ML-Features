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
def _f095_inst_pct(inst_value, marketcap):
    return inst_value / marketcap.replace(0, np.nan).abs()


# 21d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slope_21d_2d_v001_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slope_63d_2d_v002_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slope_126d_2d_v003_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slope_252d_2d_v004_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slope_504d_2d_v005_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slope_21d_2d_v006_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slope_63d_2d_v007_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slope_126d_2d_v008_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slope_252d_2d_v009_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slope_504d_2d_v010_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slope_21d_2d_v011_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slope_63d_2d_v012_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slope_126d_2d_v013_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slope_252d_2d_v014_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slope_504d_2d_v015_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slope_21d_2d_v016_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slope_63d_2d_v017_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slope_126d_2d_v018_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slope_252d_2d_v019_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slope_504d_2d_v020_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slope_21d_2d_v021_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slope_63d_2d_v022_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slope_126d_2d_v023_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slope_252d_2d_v024_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slope_504d_2d_v025_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slope_21d_2d_v026_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slope_63d_2d_v027_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slope_126d_2d_v028_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slope_252d_2d_v029_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slope_504d_2d_v030_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slope_21d_2d_v031_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slope_63d_2d_v032_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slope_126d_2d_v033_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slope_252d_2d_v034_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slope_504d_2d_v035_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slope_21d_2d_v036_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slope_63d_2d_v037_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slope_126d_2d_v038_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slope_252d_2d_v039_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slope_504d_2d_v040_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slope_21d_2d_v041_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slope_63d_2d_v042_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slope_126d_2d_v043_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slope_252d_2d_v044_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slope_504d_2d_v045_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slope_21d_2d_v046_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slope_63d_2d_v047_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slope_126d_2d_v048_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slope_252d_2d_v049_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slope_504d_2d_v050_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slope_21d_2d_v051_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slope_63d_2d_v052_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slope_126d_2d_v053_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slope_252d_2d_v054_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slope_504d_2d_v055_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slope_21d_2d_v056_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slope_63d_2d_v057_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slope_126d_2d_v058_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slope_252d_2d_v059_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slope_504d_2d_v060_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slope_21d_2d_v061_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slope_63d_2d_v062_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slope_126d_2d_v063_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slope_252d_2d_v064_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slope_504d_2d_v065_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slope_21d_2d_v066_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slope_63d_2d_v067_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slope_126d_2d_v068_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slope_252d_2d_v069_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slope_504d_2d_v070_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slope_21d_2d_v071_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slope_63d_2d_v072_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slope_126d_2d_v073_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slope_252d_2d_v074_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slope_504d_2d_v075_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slope_21d_2d_v076_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slope_63d_2d_v077_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slope_126d_2d_v078_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slope_252d_2d_v079_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slope_504d_2d_v080_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slope_21d_2d_v081_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slope_63d_2d_v082_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slope_126d_2d_v083_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slope_252d_2d_v084_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slope_504d_2d_v085_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slope_21d_2d_v086_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slope_63d_2d_v087_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slope_126d_2d_v088_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slope_252d_2d_v089_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slope_504d_2d_v090_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slope_21d_2d_v091_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slope_63d_2d_v092_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slope_126d_2d_v093_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slope_252d_2d_v094_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slope_504d_2d_v095_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_sm21_sl21_2d_v096_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_sm63_sl21_2d_v097_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_sm63_sl63_2d_v098_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_sm252_sl63_2d_v099_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_sm252_sl126_2d_v100_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_sm21_sl21_2d_v101_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_sm63_sl21_2d_v102_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_sm63_sl63_2d_v103_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_sm252_sl63_2d_v104_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_sm252_sl126_2d_v105_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_sm21_sl21_2d_v106_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_sm63_sl21_2d_v107_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_sm63_sl63_2d_v108_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_sm252_sl63_2d_v109_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_sm252_sl126_2d_v110_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_sm21_sl21_2d_v111_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_sm63_sl21_2d_v112_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_sm63_sl63_2d_v113_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_sm252_sl63_2d_v114_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_sm252_sl126_2d_v115_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_sm21_sl21_2d_v116_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_sm63_sl21_2d_v117_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_sm63_sl63_2d_v118_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_sm252_sl63_2d_v119_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_sm252_sl126_2d_v120_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_sm21_sl21_2d_v121_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = _mean(inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_sm63_sl21_2d_v122_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = _mean(inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_sm63_sl63_2d_v123_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = _mean(inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_sm252_sl63_2d_v124_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = _mean(inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_sm252_sl126_2d_v125_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = _mean(inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_sm21_sl21_2d_v126_signal(inst_holder_count, closeadj):
    base = _mean(np.log(inst_holder_count.abs().replace(0, np.nan) + 1), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_sm63_sl21_2d_v127_signal(inst_holder_count, closeadj):
    base = _mean(np.log(inst_holder_count.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_sm63_sl63_2d_v128_signal(inst_holder_count, closeadj):
    base = _mean(np.log(inst_holder_count.abs().replace(0, np.nan) + 1), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_sm252_sl63_2d_v129_signal(inst_holder_count, closeadj):
    base = _mean(np.log(inst_holder_count.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_sm252_sl126_2d_v130_signal(inst_holder_count, closeadj):
    base = _mean(np.log(inst_holder_count.abs().replace(0, np.nan) + 1), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_sm21_sl21_2d_v131_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_sm63_sl21_2d_v132_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_sm63_sl63_2d_v133_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_sm252_sl63_2d_v134_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_sm252_sl126_2d_v135_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_sm21_sl21_2d_v136_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_sm63_sl21_2d_v137_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_sm63_sl63_2d_v138_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_sm252_sl63_2d_v139_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_sm252_sl126_2d_v140_signal(inst_total_value, closeadj):
    base = _mean(inst_total_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_sm21_sl21_2d_v141_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_sm63_sl21_2d_v142_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_sm63_sl63_2d_v143_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_sm252_sl63_2d_v144_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_sm252_sl126_2d_v145_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_sm21_sl21_2d_v146_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_sm63_sl21_2d_v147_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_sm63_sl63_2d_v148_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_sm252_sl63_2d_v149_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_sm252_sl126_2d_v150_signal(inst_total_units, closeadj):
    base = _mean(inst_total_units.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_sm21_sl21_2d_v151_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_sm63_sl21_2d_v152_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_sm63_sl63_2d_v153_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_sm252_sl63_2d_v154_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_sm252_sl126_2d_v155_signal(inst_holder_count, closeadj):
    base = _mean(inst_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_sm21_sl21_2d_v156_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap).diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_sm63_sl21_2d_v157_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap).diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_sm63_sl63_2d_v158_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap).diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_sm252_sl63_2d_v159_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap).diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_sm252_sl126_2d_v160_signal(inst_total_value, marketcap, closeadj):
    base = _mean(_f095_inst_pct(inst_total_value, marketcap).diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_sm21_sl21_2d_v161_signal(inst_total_value, etf_value, closeadj):
    base = _mean(inst_total_value - etf_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_sm63_sl21_2d_v162_signal(inst_total_value, etf_value, closeadj):
    base = _mean(inst_total_value - etf_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_sm63_sl63_2d_v163_signal(inst_total_value, etf_value, closeadj):
    base = _mean(inst_total_value - etf_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_sm252_sl63_2d_v164_signal(inst_total_value, etf_value, closeadj):
    base = _mean(inst_total_value - etf_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_sm252_sl126_2d_v165_signal(inst_total_value, etf_value, closeadj):
    base = _mean(inst_total_value - etf_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_sm21_sl21_2d_v166_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value).diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_sm63_sl21_2d_v167_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value).diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_sm63_sl63_2d_v168_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value).diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_sm252_sl63_2d_v169_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value).diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_sm252_sl126_2d_v170_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value).diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_sm21_sl21_2d_v171_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_sm63_sl21_2d_v172_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_sm63_sl63_2d_v173_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_sm252_sl63_2d_v174_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_sm252_sl126_2d_v175_signal(inst_total_value, etf_value, closeadj):
    base = _mean((inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_sm21_sl21_2d_v176_signal(inst_holder_count, closeadj):
    base = _mean((inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_sm63_sl21_2d_v177_signal(inst_holder_count, closeadj):
    base = _mean((inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_sm63_sl63_2d_v178_signal(inst_holder_count, closeadj):
    base = _mean((inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_sm252_sl63_2d_v179_signal(inst_holder_count, closeadj):
    base = _mean((inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_sm252_sl126_2d_v180_signal(inst_holder_count, closeadj):
    base = _mean((inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_sm21_sl21_2d_v181_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = _mean((new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_sm63_sl21_2d_v182_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = _mean((new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_sm63_sl63_2d_v183_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = _mean((new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_sm252_sl63_2d_v184_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = _mean((new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_sm252_sl126_2d_v185_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = _mean((new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_sm21_sl21_2d_v186_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = _mean((_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_sm63_sl21_2d_v187_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = _mean((_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_sm63_sl63_2d_v188_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = _mean((_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_sm252_sl63_2d_v189_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = _mean((_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_sm252_sl126_2d_v190_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = _mean((_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_pctslope_21d_2d_v191_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_pctslope_63d_2d_v192_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_pctslope_252d_2d_v193_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_pctslope_21d_2d_v194_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_pctslope_63d_2d_v195_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_pctslope_252d_2d_v196_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_pctslope_21d_2d_v197_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_pctslope_63d_2d_v198_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_pctslope_252d_2d_v199_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_pctslope_21d_2d_v200_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

