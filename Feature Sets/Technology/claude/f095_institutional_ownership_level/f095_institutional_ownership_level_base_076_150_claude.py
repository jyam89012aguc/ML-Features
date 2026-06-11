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


# 63d z-score of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_z_63d_base_v076_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_z_126d_base_v077_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_z_252d_base_v078_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_z_504d_base_v079_signal(inst_total_value, closeadj):
    base = inst_total_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_z_63d_base_v080_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_z_126d_base_v081_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_z_252d_base_v082_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_z_504d_base_v083_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_z_63d_base_v084_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_z_126d_base_v085_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_z_252d_base_v086_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_z_504d_base_v087_signal(inst_total_units, closeadj):
    base = inst_total_units
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_z_63d_base_v088_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_z_126d_base_v089_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_z_252d_base_v090_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_z_504d_base_v091_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_z_63d_base_v092_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_z_126d_base_v093_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_z_252d_base_v094_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_z_504d_base_v095_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_z_63d_base_v096_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_z_126d_base_v097_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_z_252d_base_v098_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_z_504d_base_v099_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_z_63d_base_v100_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_z_126d_base_v101_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_z_252d_base_v102_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_z_504d_base_v103_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_z_63d_base_v104_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_z_126d_base_v105_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_z_252d_base_v106_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_z_504d_base_v107_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_z_63d_base_v108_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_z_126d_base_v109_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_z_252d_base_v110_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_z_504d_base_v111_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_z_63d_base_v112_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_z_126d_base_v113_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_z_252d_base_v114_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_z_504d_base_v115_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_z_63d_base_v116_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_z_126d_base_v117_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_z_252d_base_v118_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_z_504d_base_v119_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_z_63d_base_v120_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_z_126d_base_v121_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_z_252d_base_v122_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_z_504d_base_v123_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_z_63d_base_v124_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_z_126d_base_v125_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_z_252d_base_v126_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_ownership_pct_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_qoq_delta_z_504d_base_v127_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap).diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_z_63d_base_v128_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_z_126d_base_v129_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_z_252d_base_v130_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_active_value
def f095iol_f095_institutional_ownership_level_inst_active_value_z_504d_base_v131_signal(inst_total_value, etf_value, closeadj):
    base = inst_total_value - etf_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_z_63d_base_v132_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_z_126d_base_v133_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_z_252d_base_v134_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_active_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_active_qoq_delta_z_504d_base_v135_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value).diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_z_63d_base_v136_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_z_126d_base_v137_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_z_252d_base_v138_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_active_share
def f095iol_f095_institutional_ownership_level_inst_active_share_z_504d_base_v139_signal(inst_total_value, etf_value, closeadj):
    base = (inst_total_value - etf_value) / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_z_63d_base_v140_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_z_126d_base_v141_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_z_252d_base_v142_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of holder_cnt_z_252
def f095iol_f095_institutional_ownership_level_holder_cnt_z_252_z_504d_base_v143_signal(inst_holder_count, closeadj):
    base = (inst_holder_count - inst_holder_count.rolling(252, min_periods=63).mean()) / inst_holder_count.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_z_63d_base_v144_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_z_126d_base_v145_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_z_252d_base_v146_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of holder_rotation_rate
def f095iol_f095_institutional_ownership_level_holder_rotation_rate_z_504d_base_v147_signal(new_holder_count, exited_holder_count, inst_holder_count, closeadj):
    base = (new_holder_count + exited_holder_count) / inst_holder_count.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_z_63d_base_v148_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_z_126d_base_v149_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_z_252d_base_v150_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_pct_to_sector_med
def f095iol_f095_institutional_ownership_level_inst_pct_to_sector_med_z_504d_base_v151_signal(inst_total_value, marketcap, inst_ownership_sector_med, closeadj):
    base = (_f095_inst_pct(inst_total_value, marketcap) - inst_ownership_sector_med) / inst_ownership_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_distmax_252d_base_v152_signal(inst_total_value, closeadj):
    base = inst_total_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_value_lvl
def f095iol_f095_institutional_ownership_level_inst_value_lvl_distmax_504d_base_v153_signal(inst_total_value, closeadj):
    base = inst_total_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_distmax_252d_base_v154_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_ownership_pct
def f095iol_f095_institutional_ownership_level_inst_ownership_pct_distmax_504d_base_v155_signal(inst_total_value, marketcap, closeadj):
    base = _f095_inst_pct(inst_total_value, marketcap)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_distmax_252d_base_v156_signal(inst_total_units, closeadj):
    base = inst_total_units
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_units
def f095iol_f095_institutional_ownership_level_inst_units_distmax_504d_base_v157_signal(inst_total_units, closeadj):
    base = inst_total_units
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_distmax_252d_base_v158_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_holder_cnt
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_distmax_504d_base_v159_signal(inst_holder_count, closeadj):
    base = inst_holder_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_distmax_252d_base_v160_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_value_yoy
def f095iol_f095_institutional_ownership_level_inst_value_yoy_distmax_504d_base_v161_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_distmax_252d_base_v162_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_intensity
def f095iol_f095_institutional_ownership_level_inst_intensity_distmax_504d_base_v163_signal(inst_total_value, inst_holder_count, marketcap, closeadj):
    base = inst_total_value * inst_holder_count / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_distmax_252d_base_v164_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of holder_cnt_log
def f095iol_f095_institutional_ownership_level_holder_cnt_log_distmax_504d_base_v165_signal(inst_holder_count, closeadj):
    base = np.log(inst_holder_count.abs().replace(0, np.nan) + 1)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_distmax_252d_base_v166_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_value_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_value_qoq_delta_distmax_504d_base_v167_signal(inst_total_value, closeadj):
    base = inst_total_value.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_distmax_252d_base_v168_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_value_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_value_qoq_pct_distmax_504d_base_v169_signal(inst_total_value, closeadj):
    base = inst_total_value.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_distmax_252d_base_v170_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_units_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_units_qoq_delta_distmax_504d_base_v171_signal(inst_total_units, closeadj):
    base = inst_total_units.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_distmax_252d_base_v172_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_units_qoq_pct
def f095iol_f095_institutional_ownership_level_inst_units_qoq_pct_distmax_504d_base_v173_signal(inst_total_units, closeadj):
    base = inst_total_units.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_distmax_252d_base_v174_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of inst_holder_cnt_qoq_delta
def f095iol_f095_institutional_ownership_level_inst_holder_cnt_qoq_delta_distmax_504d_base_v175_signal(inst_holder_count, closeadj):
    base = inst_holder_count.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

