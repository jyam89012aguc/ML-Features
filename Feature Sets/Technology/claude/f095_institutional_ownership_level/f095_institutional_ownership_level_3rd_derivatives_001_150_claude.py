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


# 21d acceleration of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_accel_21d_3d_v001_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_accel_63d_3d_v002_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_accel_126d_3d_v003_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_accel_252d_3d_v004_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_accel_21d_3d_v005_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_accel_63d_3d_v006_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_accel_126d_3d_v007_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_accel_252d_3d_v008_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_accel_21d_3d_v009_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_accel_63d_3d_v010_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_accel_126d_3d_v011_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_accel_252d_3d_v012_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_accel_21d_3d_v013_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_accel_63d_3d_v014_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_accel_126d_3d_v015_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_accel_252d_3d_v016_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_accel_21d_3d_v017_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_accel_63d_3d_v018_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_accel_126d_3d_v019_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_accel_252d_3d_v020_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_accel_21d_3d_v021_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_accel_63d_3d_v022_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_accel_126d_3d_v023_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_accel_252d_3d_v024_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_accel_21d_3d_v025_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_accel_63d_3d_v026_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_accel_126d_3d_v027_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_accel_252d_3d_v028_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_accel_21d_3d_v029_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_accel_63d_3d_v030_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_accel_126d_3d_v031_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_accel_252d_3d_v032_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_accel_21d_3d_v033_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_accel_63d_3d_v034_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_accel_126d_3d_v035_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_accel_252d_3d_v036_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_accel_21d_3d_v037_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_accel_63d_3d_v038_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_accel_126d_3d_v039_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_accel_252d_3d_v040_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_accel_21d_3d_v041_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_accel_63d_3d_v042_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_accel_126d_3d_v043_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_accel_252d_3d_v044_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_accel_21d_3d_v045_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_accel_63d_3d_v046_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_accel_126d_3d_v047_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_accel_252d_3d_v048_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_accel_21d_3d_v049_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_accel_63d_3d_v050_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_accel_126d_3d_v051_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_accel_252d_3d_v052_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_accel_21d_3d_v053_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_accel_63d_3d_v054_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_accel_126d_3d_v055_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_accel_252d_3d_v056_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_accel_21d_3d_v057_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_accel_63d_3d_v058_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_accel_126d_3d_v059_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_accel_252d_3d_v060_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_accel_21d_3d_v061_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_accel_63d_3d_v062_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_accel_126d_3d_v063_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_accel_252d_3d_v064_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_accel_21d_3d_v065_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_accel_63d_3d_v066_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_accel_126d_3d_v067_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_accel_252d_3d_v068_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_accel_21d_3d_v069_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_accel_63d_3d_v070_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_accel_126d_3d_v071_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_accel_252d_3d_v072_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_accel_21d_3d_v073_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_accel_63d_3d_v074_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_accel_126d_3d_v075_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_accel_252d_3d_v076_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slopez_21d_z126_3d_v077_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slopez_63d_z252_3d_v078_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slopez_126d_z252_3d_v079_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_slopez_252d_z504_3d_v080_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slopez_21d_z126_3d_v081_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slopez_63d_z252_3d_v082_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slopez_126d_z252_3d_v083_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_slopez_252d_z504_3d_v084_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slopez_21d_z126_3d_v085_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slopez_63d_z252_3d_v086_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slopez_126d_z252_3d_v087_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_slopez_252d_z504_3d_v088_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slopez_21d_z126_3d_v089_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slopez_63d_z252_3d_v090_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slopez_126d_z252_3d_v091_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_slopez_252d_z504_3d_v092_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slopez_21d_z126_3d_v093_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slopez_63d_z252_3d_v094_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slopez_126d_z252_3d_v095_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_slopez_252d_z504_3d_v096_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slopez_21d_z126_3d_v097_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slopez_63d_z252_3d_v098_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slopez_126d_z252_3d_v099_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_slopez_252d_z504_3d_v100_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slopez_21d_z126_3d_v101_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slopez_63d_z252_3d_v102_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slopez_126d_z252_3d_v103_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_slopez_252d_z504_3d_v104_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slopez_21d_z126_3d_v105_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slopez_63d_z252_3d_v106_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slopez_126d_z252_3d_v107_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_slopez_252d_z504_3d_v108_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slopez_21d_z126_3d_v109_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slopez_63d_z252_3d_v110_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slopez_126d_z252_3d_v111_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_slopez_252d_z504_3d_v112_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slopez_21d_z126_3d_v113_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slopez_63d_z252_3d_v114_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slopez_126d_z252_3d_v115_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_slopez_252d_z504_3d_v116_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slopez_21d_z126_3d_v117_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slopez_63d_z252_3d_v118_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slopez_126d_z252_3d_v119_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_slopez_252d_z504_3d_v120_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slopez_21d_z126_3d_v121_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slopez_63d_z252_3d_v122_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slopez_126d_z252_3d_v123_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_slopez_252d_z504_3d_v124_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slopez_21d_z126_3d_v125_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slopez_63d_z252_3d_v126_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slopez_126d_z252_3d_v127_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_slopez_252d_z504_3d_v128_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slopez_21d_z126_3d_v129_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slopez_63d_z252_3d_v130_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slopez_126d_z252_3d_v131_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_slopez_252d_z504_3d_v132_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slopez_21d_z126_3d_v133_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slopez_63d_z252_3d_v134_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slopez_126d_z252_3d_v135_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_slopez_252d_z504_3d_v136_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slopez_21d_z126_3d_v137_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slopez_63d_z252_3d_v138_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slopez_126d_z252_3d_v139_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_slopez_252d_z504_3d_v140_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slopez_21d_z126_3d_v141_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slopez_63d_z252_3d_v142_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slopez_126d_z252_3d_v143_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_slopez_252d_z504_3d_v144_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slopez_21d_z126_3d_v145_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slopez_63d_z252_3d_v146_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slopez_126d_z252_3d_v147_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_slopez_252d_z504_3d_v148_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slopez_21d_z126_3d_v149_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slopez_63d_z252_3d_v150_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slopez_126d_z252_3d_v151_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_slopez_252d_z504_3d_v152_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_jerk_21d_3d_v153_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_jerk_63d_3d_v154_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_jerk_126d_3d_v155_signal(inst_total_value, closeadj):
    base = inst_total_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_jerk_21d_3d_v156_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_jerk_63d_3d_v157_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_jerk_126d_3d_v158_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_jerk_21d_3d_v159_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_jerk_63d_3d_v160_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_jerk_126d_3d_v161_signal(inst_total_units, closeadj):
    base = inst_total_units
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_jerk_21d_3d_v162_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_jerk_63d_3d_v163_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_jerk_126d_3d_v164_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_jerk_21d_3d_v165_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_jerk_63d_3d_v166_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_jerk_126d_3d_v167_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_jerk_21d_3d_v168_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_jerk_63d_3d_v169_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_jerk_126d_3d_v170_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_jerk_21d_3d_v171_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_jerk_63d_3d_v172_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_jerk_126d_3d_v173_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_jerk_21d_3d_v174_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_jerk_63d_3d_v175_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_jerk_126d_3d_v176_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_jerk_21d_3d_v177_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_jerk_63d_3d_v178_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_jerk_126d_3d_v179_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_jerk_21d_3d_v180_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_jerk_63d_3d_v181_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_jerk_126d_3d_v182_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_jerk_21d_3d_v183_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_jerk_63d_3d_v184_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_jerk_126d_3d_v185_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_jerk_21d_3d_v186_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_jerk_63d_3d_v187_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_jerk_126d_3d_v188_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_jerk_21d_3d_v189_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_jerk_63d_3d_v190_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_jerk_126d_3d_v191_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_jerk_21d_3d_v192_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_jerk_63d_3d_v193_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_jerk_126d_3d_v194_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_jerk_21d_3d_v195_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_jerk_63d_3d_v196_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_jerk_126d_3d_v197_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_jerk_21d_3d_v198_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_jerk_63d_3d_v199_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_jerk_126d_3d_v200_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

