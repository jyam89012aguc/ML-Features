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
def _f101_evsales(ev, revenue):
    return ev / revenue.abs().replace(0, np.nan)


def _f101_revgrowth(revenue):
    return revenue.pct_change(periods=252)


def _f101_fcf_margin(fcf, revenue):
    return fcf / revenue.abs().replace(0, np.nan)


def _f101_drawdown(closeadj, w):
    peak = closeadj.rolling(w, min_periods=max(1, w//2)).max()
    return (closeadj - peak) / peak.replace(0, np.nan).abs()


# 63d z-score of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_z_63d_base_v076_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_z_126d_base_v077_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_z_252d_base_v078_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_z_504d_base_v079_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_z_63d_base_v080_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_z_126d_base_v081_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_z_252d_base_v082_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_z_504d_base_v083_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_z_63d_base_v084_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_z_126d_base_v085_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_z_252d_base_v086_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_z_504d_base_v087_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_z_63d_base_v088_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_z_126d_base_v089_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_z_252d_base_v090_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_z_504d_base_v091_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_z_63d_base_v092_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_z_126d_base_v093_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_z_252d_base_v094_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_z_504d_base_v095_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_z_63d_base_v096_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_z_126d_base_v097_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_z_252d_base_v098_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_z_504d_base_v099_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_z_63d_base_v100_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_z_126d_base_v101_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_z_252d_base_v102_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_z_504d_base_v103_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_z_63d_base_v104_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_z_126d_base_v105_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_z_252d_base_v106_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_z_504d_base_v107_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_z_63d_base_v108_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_z_126d_base_v109_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_z_252d_base_v110_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_z_504d_base_v111_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_z_63d_base_v112_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_z_126d_base_v113_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_z_252d_base_v114_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_z_504d_base_v115_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_z_63d_base_v116_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_z_126d_base_v117_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_z_252d_base_v118_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_z_504d_base_v119_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_z_63d_base_v120_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_z_126d_base_v121_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_z_252d_base_v122_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_z_504d_base_v123_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_z_63d_base_v124_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_z_126d_base_v125_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_z_252d_base_v126_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_z_504d_base_v127_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_z_63d_base_v128_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_z_126d_base_v129_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_z_252d_base_v130_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_z_504d_base_v131_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_z_63d_base_v132_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_z_126d_base_v133_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_z_252d_base_v134_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_z_504d_base_v135_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_z_63d_base_v136_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_z_126d_base_v137_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_z_252d_base_v138_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_z_504d_base_v139_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_z_63d_base_v140_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_z_126d_base_v141_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_z_252d_base_v142_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_z_504d_base_v143_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_z_63d_base_v144_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_z_126d_base_v145_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_z_252d_base_v146_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_z_504d_base_v147_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_z_63d_base_v148_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_z_126d_base_v149_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_z_252d_base_v150_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_z_504d_base_v151_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_z_63d_base_v152_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_z_126d_base_v153_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_z_252d_base_v154_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_z_504d_base_v155_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_z_63d_base_v156_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_z_126d_base_v157_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_z_252d_base_v158_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_z_504d_base_v159_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_z_63d_base_v160_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_z_126d_base_v161_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_z_252d_base_v162_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_z_504d_base_v163_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_distmax_252d_base_v164_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_distmax_504d_base_v165_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_distmax_252d_base_v166_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_distmax_504d_base_v167_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_distmax_252d_base_v168_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_distmax_504d_base_v169_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_distmax_252d_base_v170_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_distmax_504d_base_v171_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_distmax_252d_base_v172_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_distmax_504d_base_v173_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_distmax_252d_base_v174_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_distmax_504d_base_v175_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

