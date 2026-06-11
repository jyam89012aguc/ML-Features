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
def _f097_specshare(specialist_value, inst_total_value):
    return specialist_value / inst_total_value.replace(0, np.nan).abs()


# 63d z-score of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_z_63d_base_v076_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_z_126d_base_v077_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_z_252d_base_v078_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_z_504d_base_v079_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_z_63d_base_v080_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_z_126d_base_v081_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_z_252d_base_v082_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_z_504d_base_v083_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_z_63d_base_v084_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_z_126d_base_v085_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_z_252d_base_v086_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_z_504d_base_v087_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_z_63d_base_v088_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_z_126d_base_v089_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_z_252d_base_v090_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_z_504d_base_v091_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_z_63d_base_v092_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_z_126d_base_v093_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_z_252d_base_v094_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_z_504d_base_v095_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_z_63d_base_v096_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_z_126d_base_v097_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_z_252d_base_v098_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_z_504d_base_v099_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_z_63d_base_v100_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_z_126d_base_v101_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_z_252d_base_v102_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_z_504d_base_v103_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_z_63d_base_v104_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_z_126d_base_v105_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_z_252d_base_v106_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_z_504d_base_v107_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_z_63d_base_v108_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_z_126d_base_v109_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_z_252d_base_v110_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_z_504d_base_v111_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_z_63d_base_v112_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_z_126d_base_v113_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_z_252d_base_v114_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_z_504d_base_v115_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_z_63d_base_v116_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_z_126d_base_v117_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_z_252d_base_v118_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of hedge_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_qoq_delta_z_504d_base_v119_signal(hedge_fund_value, closeadj):
    base = hedge_fund_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_z_63d_base_v120_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_z_126d_base_v121_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_z_252d_base_v122_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of etf_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_qoq_delta_z_504d_base_v123_signal(etf_value, closeadj):
    base = etf_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_z_63d_base_v124_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_z_126d_base_v125_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_z_252d_base_v126_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of active_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_active_share_qoq_delta_z_504d_base_v127_signal(quality_long_value, hedge_fund_value, inst_total_value, closeadj):
    base = ((quality_long_value + hedge_fund_value) / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_z_63d_base_v128_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_z_126d_base_v129_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_z_252d_base_v130_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of etf_share_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_qoq_delta_z_504d_base_v131_signal(etf_value, inst_total_value, closeadj):
    base = (etf_value / inst_total_value.replace(0, np.nan).abs()).diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_z_63d_base_v132_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_z_126d_base_v133_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_z_252d_base_v134_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of named_specialist_qoq_chg
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_qoq_chg_z_504d_base_v135_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_z_63d_base_v136_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_z_126d_base_v137_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_z_252d_base_v138_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of named_specialist_entering_flag
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_entering_flag_z_504d_base_v139_signal(named_specialist_holder_count, closeadj):
    base = (named_specialist_holder_count.diff(periods=63) > 2).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_z_63d_base_v140_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_z_126d_base_v141_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_z_252d_base_v142_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of growth_specialist_value
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_value_z_504d_base_v143_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_z_63d_base_v144_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_z_126d_base_v145_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_z_252d_base_v146_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of growth_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_growth_specialist_qoq_delta_z_504d_base_v147_signal(growth_specialist_value, closeadj):
    base = growth_specialist_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_z_63d_base_v148_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_z_126d_base_v149_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_z_252d_base_v150_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top5_specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_share_z_504d_base_v151_signal(top5_specialist_value, specialist_fund_value, closeadj):
    base = top5_specialist_value / specialist_fund_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_z_63d_base_v152_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_z_126d_base_v153_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_z_252d_base_v154_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top5_specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_top5_specialist_qoq_delta_z_504d_base_v155_signal(top5_specialist_value, closeadj):
    base = top5_specialist_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_distmax_252d_base_v156_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of specialist_share
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_share_distmax_504d_base_v157_signal(specialist_fund_value, inst_total_value, closeadj):
    base = _f097_specshare(specialist_fund_value, inst_total_value)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_distmax_252d_base_v158_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of quality_long_share
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_share_distmax_504d_base_v159_signal(quality_long_value, inst_total_value, closeadj):
    base = quality_long_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_distmax_252d_base_v160_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of hedge_share
def f097spx_f097_specialist_and_quality_fund_exposure_hedge_share_distmax_504d_base_v161_signal(hedge_fund_value, inst_total_value, closeadj):
    base = hedge_fund_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_distmax_252d_base_v162_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of etf_share
def f097spx_f097_specialist_and_quality_fund_exposure_etf_share_distmax_504d_base_v163_signal(etf_value, inst_total_value, closeadj):
    base = etf_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_distmax_252d_base_v164_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of specialist_value_yoy
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_value_yoy_distmax_504d_base_v165_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_distmax_252d_base_v166_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of named_specialist_count
def f097spx_f097_specialist_and_quality_fund_exposure_named_specialist_count_distmax_504d_base_v167_signal(named_specialist_holder_count, closeadj):
    base = named_specialist_holder_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_distmax_252d_base_v168_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of etf_minus_active
def f097spx_f097_specialist_and_quality_fund_exposure_etf_minus_active_distmax_504d_base_v169_signal(etf_value, quality_long_value, hedge_fund_value, closeadj):
    base = etf_value - (quality_long_value + hedge_fund_value)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_distmax_252d_base_v170_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of specialist_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_delta_distmax_504d_base_v171_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_distmax_252d_base_v172_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of specialist_qoq_pct
def f097spx_f097_specialist_and_quality_fund_exposure_specialist_qoq_pct_distmax_504d_base_v173_signal(specialist_fund_value, closeadj):
    base = specialist_fund_value.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_distmax_252d_base_v174_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of quality_long_qoq_delta
def f097spx_f097_specialist_and_quality_fund_exposure_quality_long_qoq_delta_distmax_504d_base_v175_signal(quality_long_value, closeadj):
    base = quality_long_value.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

