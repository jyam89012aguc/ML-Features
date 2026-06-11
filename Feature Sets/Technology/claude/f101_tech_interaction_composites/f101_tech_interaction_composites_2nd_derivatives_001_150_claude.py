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
def _f101_evsales(ev, revenue):
    return ev / revenue.abs().replace(0, np.nan)


def _f101_revgrowth(revenue):
    return revenue.pct_change(periods=252)


def _f101_fcf_margin(fcf, revenue):
    return fcf / revenue.abs().replace(0, np.nan)


def _f101_drawdown(closeadj, w):
    peak = closeadj.rolling(w, min_periods=max(1, w//2)).max()
    return (closeadj - peak) / peak.replace(0, np.nan).abs()


# 21d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slope_21d_2d_v001_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slope_63d_2d_v002_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slope_126d_2d_v003_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slope_252d_2d_v004_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slope_504d_2d_v005_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slope_21d_2d_v006_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slope_63d_2d_v007_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slope_126d_2d_v008_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slope_252d_2d_v009_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slope_504d_2d_v010_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slope_21d_2d_v011_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slope_63d_2d_v012_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slope_126d_2d_v013_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slope_252d_2d_v014_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slope_504d_2d_v015_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slope_21d_2d_v016_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slope_63d_2d_v017_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slope_126d_2d_v018_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slope_252d_2d_v019_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slope_504d_2d_v020_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slope_21d_2d_v021_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slope_63d_2d_v022_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slope_126d_2d_v023_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slope_252d_2d_v024_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slope_504d_2d_v025_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slope_21d_2d_v026_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slope_63d_2d_v027_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slope_126d_2d_v028_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slope_252d_2d_v029_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slope_504d_2d_v030_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slope_21d_2d_v031_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slope_63d_2d_v032_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slope_126d_2d_v033_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slope_252d_2d_v034_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slope_504d_2d_v035_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slope_21d_2d_v036_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slope_63d_2d_v037_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slope_126d_2d_v038_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slope_252d_2d_v039_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slope_504d_2d_v040_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slope_21d_2d_v041_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slope_63d_2d_v042_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slope_126d_2d_v043_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slope_252d_2d_v044_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slope_504d_2d_v045_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slope_21d_2d_v046_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slope_63d_2d_v047_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slope_126d_2d_v048_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slope_252d_2d_v049_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slope_504d_2d_v050_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slope_21d_2d_v051_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slope_63d_2d_v052_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slope_126d_2d_v053_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slope_252d_2d_v054_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slope_504d_2d_v055_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slope_21d_2d_v056_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slope_63d_2d_v057_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slope_126d_2d_v058_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slope_252d_2d_v059_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slope_504d_2d_v060_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slope_21d_2d_v061_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slope_63d_2d_v062_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slope_126d_2d_v063_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slope_252d_2d_v064_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slope_504d_2d_v065_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slope_21d_2d_v066_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slope_63d_2d_v067_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slope_126d_2d_v068_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slope_252d_2d_v069_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slope_504d_2d_v070_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slope_21d_2d_v071_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slope_63d_2d_v072_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slope_126d_2d_v073_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slope_252d_2d_v074_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slope_504d_2d_v075_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slope_21d_2d_v076_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slope_63d_2d_v077_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slope_126d_2d_v078_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slope_252d_2d_v079_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slope_504d_2d_v080_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slope_21d_2d_v081_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slope_63d_2d_v082_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slope_126d_2d_v083_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slope_252d_2d_v084_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slope_504d_2d_v085_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slope_21d_2d_v086_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slope_63d_2d_v087_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slope_126d_2d_v088_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slope_252d_2d_v089_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slope_504d_2d_v090_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slope_21d_2d_v091_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slope_63d_2d_v092_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slope_126d_2d_v093_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slope_252d_2d_v094_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slope_504d_2d_v095_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slope_21d_2d_v096_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slope_63d_2d_v097_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slope_126d_2d_v098_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slope_252d_2d_v099_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slope_504d_2d_v100_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slope_21d_2d_v101_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slope_63d_2d_v102_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slope_126d_2d_v103_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slope_252d_2d_v104_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slope_504d_2d_v105_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slope_21d_2d_v106_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slope_63d_2d_v107_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slope_126d_2d_v108_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slope_252d_2d_v109_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slope_504d_2d_v110_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_sm21_sl21_2d_v111_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) - _f101_revgrowth(revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_sm63_sl21_2d_v112_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) - _f101_revgrowth(revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_sm63_sl63_2d_v113_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) - _f101_revgrowth(revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_sm252_sl63_2d_v114_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) - _f101_revgrowth(revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_sm252_sl126_2d_v115_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) - _f101_revgrowth(revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_sm21_sl21_2d_v116_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_sm63_sl21_2d_v117_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_sm63_sl63_2d_v118_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_sm252_sl63_2d_v119_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_sm252_sl126_2d_v120_signal(ev, revenue, closeadj):
    base = _mean(_f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_sm21_sl21_2d_v121_signal(ev, revenue, closeadj):
    base = _mean(_f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_sm63_sl21_2d_v122_signal(ev, revenue, closeadj):
    base = _mean(_f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_sm63_sl63_2d_v123_signal(ev, revenue, closeadj):
    base = _mean(_f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_sm252_sl63_2d_v124_signal(ev, revenue, closeadj):
    base = _mean(_f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_sm252_sl126_2d_v125_signal(ev, revenue, closeadj):
    base = _mean(_f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_sm21_sl21_2d_v126_signal(ev, revenue, closeadj):
    base = _mean(((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_sm63_sl21_2d_v127_signal(ev, revenue, closeadj):
    base = _mean(((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_sm63_sl63_2d_v128_signal(ev, revenue, closeadj):
    base = _mean(((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_sm252_sl63_2d_v129_signal(ev, revenue, closeadj):
    base = _mean(((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_sm252_sl126_2d_v130_signal(ev, revenue, closeadj):
    base = _mean(((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_sm21_sl21_2d_v131_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_sm63_sl21_2d_v132_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_sm63_sl63_2d_v133_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_sm252_sl63_2d_v134_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_sm252_sl126_2d_v135_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_sm21_sl21_2d_v136_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_sm63_sl21_2d_v137_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_sm63_sl63_2d_v138_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_sm252_sl63_2d_v139_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_sm252_sl126_2d_v140_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_sm21_sl21_2d_v141_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_sm63_sl21_2d_v142_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_sm63_sl63_2d_v143_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_sm252_sl63_2d_v144_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_sm252_sl126_2d_v145_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_sm21_sl21_2d_v146_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_sm63_sl21_2d_v147_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_sm63_sl63_2d_v148_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_sm252_sl63_2d_v149_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_sm252_sl126_2d_v150_signal(insider_p_buy_value, marketcap, closeadj):
    base = _mean((insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_sm21_sl21_2d_v151_signal(inst_total_value, marketcap, closeadj):
    base = _mean(inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_sm63_sl21_2d_v152_signal(inst_total_value, marketcap, closeadj):
    base = _mean(inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_sm63_sl63_2d_v153_signal(inst_total_value, marketcap, closeadj):
    base = _mean(inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_sm252_sl63_2d_v154_signal(inst_total_value, marketcap, closeadj):
    base = _mean(inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_sm252_sl126_2d_v155_signal(inst_total_value, marketcap, closeadj):
    base = _mean(inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_sm21_sl21_2d_v156_signal(specialist_fund_value, marketcap, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_sm63_sl21_2d_v157_signal(specialist_fund_value, marketcap, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_sm63_sl63_2d_v158_signal(specialist_fund_value, marketcap, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_sm252_sl63_2d_v159_signal(specialist_fund_value, marketcap, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_sm252_sl126_2d_v160_signal(specialist_fund_value, marketcap, closeadj):
    base = _mean(specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_sm21_sl21_2d_v161_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count * _f101_drawdown(closeadj, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_sm63_sl21_2d_v162_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_sm63_sl63_2d_v163_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count * _f101_drawdown(closeadj, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_sm252_sl63_2d_v164_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_sm252_sl126_2d_v165_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count * _f101_drawdown(closeadj, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_sm21_sl21_2d_v166_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_sm63_sl21_2d_v167_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_sm63_sl63_2d_v168_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_sm252_sl63_2d_v169_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_sm252_sl126_2d_v170_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_sm21_sl21_2d_v171_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_sm63_sl21_2d_v172_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_sm63_sl63_2d_v173_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_sm252_sl63_2d_v174_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_sm252_sl126_2d_v175_signal(volume, closeadj):
    base = _mean((volume * closeadj) * closeadj.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_sm21_sl21_2d_v176_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = _mean((volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_sm63_sl21_2d_v177_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = _mean((volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_sm63_sl63_2d_v178_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = _mean((volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_sm252_sl63_2d_v179_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = _mean((volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_sm252_sl126_2d_v180_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = _mean((volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_sm21_sl21_2d_v181_signal(revenue, gp, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_sm63_sl21_2d_v182_signal(revenue, gp, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_sm63_sl63_2d_v183_signal(revenue, gp, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_sm252_sl63_2d_v184_signal(revenue, gp, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_sm252_sl126_2d_v185_signal(revenue, gp, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_sm21_sl21_2d_v186_signal(revenue, fcf, closeadj):
    base = _mean(_f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_sm63_sl21_2d_v187_signal(revenue, fcf, closeadj):
    base = _mean(_f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_sm63_sl63_2d_v188_signal(revenue, fcf, closeadj):
    base = _mean(_f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_sm252_sl63_2d_v189_signal(revenue, fcf, closeadj):
    base = _mean(_f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_sm252_sl126_2d_v190_signal(revenue, fcf, closeadj):
    base = _mean(_f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_sm21_sl21_2d_v191_signal(revenue, opinc, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs()), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_sm63_sl21_2d_v192_signal(revenue, opinc, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_sm63_sl63_2d_v193_signal(revenue, opinc, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs()), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_sm252_sl63_2d_v194_signal(revenue, opinc, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_sm252_sl126_2d_v195_signal(revenue, opinc, closeadj):
    base = _mean(_f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs()), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_sm21_sl21_2d_v196_signal(rnd, revenue, closeadj):
    base = _mean(rnd.shift(504) * _f101_revgrowth(revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_sm63_sl21_2d_v197_signal(rnd, revenue, closeadj):
    base = _mean(rnd.shift(504) * _f101_revgrowth(revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_sm63_sl63_2d_v198_signal(rnd, revenue, closeadj):
    base = _mean(rnd.shift(504) * _f101_revgrowth(revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_sm252_sl63_2d_v199_signal(rnd, revenue, closeadj):
    base = _mean(rnd.shift(504) * _f101_revgrowth(revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_sm252_sl126_2d_v200_signal(rnd, revenue, closeadj):
    base = _mean(rnd.shift(504) * _f101_revgrowth(revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

