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
def _f095_inst_pct(inst_value, marketcap):
    return inst_value / marketcap.replace(0, np.nan).abs()


# 21d mean of inst_value_lvl scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_lvl_mean_21d_base_v001_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_value_lvl scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_lvl_mean_63d_base_v002_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_value_lvl scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_lvl_mean_126d_base_v003_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_value_lvl scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_lvl_mean_252d_base_v004_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_value_lvl scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_lvl_mean_504d_base_v005_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_ownership_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_mean_21d_base_v006_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_ownership_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_mean_63d_base_v007_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_ownership_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_mean_126d_base_v008_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_ownership_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_mean_252d_base_v009_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_ownership_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_mean_504d_base_v010_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_units scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_mean_21d_base_v011_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_units scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_mean_63d_base_v012_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_units scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_mean_126d_base_v013_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_units scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_mean_252d_base_v014_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_units scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_mean_504d_base_v015_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_holder_cnt scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_mean_21d_base_v016_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_holder_cnt scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_mean_63d_base_v017_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_holder_cnt scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_mean_126d_base_v018_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_holder_cnt scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_mean_252d_base_v019_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_holder_cnt scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_mean_504d_base_v020_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_value_yoy scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_yoy_mean_21d_base_v021_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_value_yoy scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_yoy_mean_63d_base_v022_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_value_yoy scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_yoy_mean_126d_base_v023_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_value_yoy scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_yoy_mean_252d_base_v024_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_value_yoy scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_yoy_mean_504d_base_v025_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_intensity scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_intensity_mean_21d_base_v026_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_intensity scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_intensity_mean_63d_base_v027_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_intensity scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_intensity_mean_126d_base_v028_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_intensity scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_intensity_mean_252d_base_v029_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_intensity scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_intensity_mean_504d_base_v030_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of holder_cnt_log scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_log_mean_21d_base_v031_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of holder_cnt_log scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_log_mean_63d_base_v032_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of holder_cnt_log scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_log_mean_126d_base_v033_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of holder_cnt_log scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_log_mean_252d_base_v034_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of holder_cnt_log scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_log_mean_504d_base_v035_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_value_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_mean_21d_base_v036_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_value_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_mean_63d_base_v037_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_value_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_mean_126d_base_v038_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_value_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_mean_252d_base_v039_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_value_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_mean_504d_base_v040_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_value_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_mean_21d_base_v041_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_value_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_mean_63d_base_v042_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_value_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_mean_126d_base_v043_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_value_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_mean_252d_base_v044_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_value_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_mean_504d_base_v045_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_units_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_mean_21d_base_v046_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_units_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_mean_63d_base_v047_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_units_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_mean_126d_base_v048_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_units_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_mean_252d_base_v049_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_units_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_mean_504d_base_v050_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_units_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_mean_21d_base_v051_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_units_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_mean_63d_base_v052_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_units_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_mean_126d_base_v053_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_units_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_mean_252d_base_v054_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_units_qoq_pct scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_mean_504d_base_v055_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_holder_cnt_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_mean_21d_base_v056_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_holder_cnt_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_mean_63d_base_v057_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_holder_cnt_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_mean_126d_base_v058_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_holder_cnt_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_mean_252d_base_v059_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_holder_cnt_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_mean_504d_base_v060_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_ownership_pct_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_mean_21d_base_v061_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_ownership_pct_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_mean_63d_base_v062_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_ownership_pct_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_mean_126d_base_v063_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_ownership_pct_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_mean_252d_base_v064_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_ownership_pct_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_mean_504d_base_v065_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_active_value scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_value_mean_21d_base_v066_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_active_value scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_value_mean_63d_base_v067_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_active_value scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_value_mean_126d_base_v068_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_active_value scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_value_mean_252d_base_v069_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_active_value scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_value_mean_504d_base_v070_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_active_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_mean_21d_base_v071_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_active_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_mean_63d_base_v072_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_active_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_mean_126d_base_v073_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_active_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_mean_252d_base_v074_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_active_qoq_delta scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_mean_504d_base_v075_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_active_share scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_share_mean_21d_base_v076_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_active_share scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_share_mean_63d_base_v077_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_active_share scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_share_mean_126d_base_v078_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_active_share scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_share_mean_252d_base_v079_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_active_share scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_active_share_mean_504d_base_v080_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of holder_cnt_z_252 scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_mean_21d_base_v081_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of holder_cnt_z_252 scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_mean_63d_base_v082_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of holder_cnt_z_252 scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_mean_126d_base_v083_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of holder_cnt_z_252 scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_mean_252d_base_v084_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of holder_cnt_z_252 scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_mean_504d_base_v085_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of holder_rotation_rate scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_mean_21d_base_v086_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of holder_rotation_rate scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_mean_63d_base_v087_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of holder_rotation_rate scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_mean_126d_base_v088_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of holder_rotation_rate scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_mean_252d_base_v089_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of holder_rotation_rate scaled by closeadj
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_mean_504d_base_v090_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_pct_to_sector_med scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_mean_21d_base_v091_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_pct_to_sector_med scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_mean_63d_base_v092_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_pct_to_sector_med scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_mean_126d_base_v093_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_pct_to_sector_med scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_mean_252d_base_v094_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_pct_to_sector_med scaled by closeadj
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_mean_504d_base_v095_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_median_63d_base_v096_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_median_252d_base_v097_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_median_504d_base_v098_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_median_63d_base_v099_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_median_252d_base_v100_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

