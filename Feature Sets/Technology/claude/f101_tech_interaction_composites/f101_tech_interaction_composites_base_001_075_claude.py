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


# 21d mean of evsales_minus_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_mean_21d_base_v001_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evsales_minus_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_mean_63d_base_v002_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evsales_minus_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_mean_126d_base_v003_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evsales_minus_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_mean_252d_base_v004_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evsales_minus_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_mean_504d_base_v005_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of evsales_per_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_mean_21d_base_v006_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of evsales_per_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_mean_63d_base_v007_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of evsales_per_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_mean_126d_base_v008_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of evsales_per_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_mean_252d_base_v009_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of evsales_per_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_mean_504d_base_v010_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revgrowth_per_evsales scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_mean_21d_base_v011_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revgrowth_per_evsales scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_mean_63d_base_v012_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revgrowth_per_evsales scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_mean_126d_base_v013_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revgrowth_per_evsales scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_mean_252d_base_v014_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revgrowth_per_evsales scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_mean_504d_base_v015_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of multiple_reset_growth_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_mean_21d_base_v016_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of multiple_reset_growth_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_mean_63d_base_v017_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of multiple_reset_growth_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_mean_126d_base_v018_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of multiple_reset_growth_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_mean_252d_base_v019_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of multiple_reset_growth_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_mean_504d_base_v020_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_buy_x_evsales_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_mean_21d_base_v021_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_buy_x_evsales_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_mean_63d_base_v022_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_buy_x_evsales_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_mean_126d_base_v023_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_buy_x_evsales_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_mean_252d_base_v024_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_buy_x_evsales_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_mean_504d_base_v025_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_buy_x_pb_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_mean_21d_base_v026_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_buy_x_pb_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_mean_63d_base_v027_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_buy_x_pb_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_mean_126d_base_v028_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_buy_x_pb_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_mean_252d_base_v029_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_buy_x_pb_compression scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_mean_504d_base_v030_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_buy_x_drawdown_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_mean_21d_base_v031_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_buy_x_drawdown_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_mean_63d_base_v032_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_buy_x_drawdown_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_mean_126d_base_v033_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_buy_x_drawdown_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_mean_252d_base_v034_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_buy_x_drawdown_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_mean_504d_base_v035_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_buy_x_drawdown_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_mean_21d_base_v036_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_buy_x_drawdown_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_mean_63d_base_v037_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_buy_x_drawdown_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_mean_126d_base_v038_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_buy_x_drawdown_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_mean_252d_base_v039_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_buy_x_drawdown_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_mean_504d_base_v040_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of inst_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_mean_21d_base_v041_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of inst_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_mean_63d_base_v042_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of inst_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_mean_126d_base_v043_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of inst_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_mean_252d_base_v044_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of inst_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_mean_504d_base_v045_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of specialist_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_mean_21d_base_v046_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of specialist_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_mean_63d_base_v047_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of specialist_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_mean_126d_base_v048_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of specialist_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_mean_252d_base_v049_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of specialist_qoq_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_mean_504d_base_v050_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of new_holder_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_mean_21d_base_v051_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of new_holder_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_mean_63d_base_v052_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of new_holder_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_mean_126d_base_v053_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of new_holder_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_mean_252d_base_v054_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of new_holder_x_drawdown_252 scaled by closeadj
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_mean_504d_base_v055_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dollar_vol_x_mom_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_mean_21d_base_v056_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dollar_vol_x_mom_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_mean_63d_base_v057_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dollar_vol_x_mom_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_mean_126d_base_v058_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dollar_vol_x_mom_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_mean_252d_base_v059_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dollar_vol_x_mom_63d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_mean_504d_base_v060_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dollar_vol_x_mom_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_mean_21d_base_v061_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dollar_vol_x_mom_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_mean_63d_base_v062_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dollar_vol_x_mom_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_mean_126d_base_v063_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dollar_vol_x_mom_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_mean_252d_base_v064_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dollar_vol_x_mom_252d scaled by closeadj
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_mean_504d_base_v065_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of vol_surge_x_p_buy scaled by closeadj
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_mean_21d_base_v066_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of vol_surge_x_p_buy scaled by closeadj
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_mean_63d_base_v067_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of vol_surge_x_p_buy scaled by closeadj
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_mean_126d_base_v068_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of vol_surge_x_p_buy scaled by closeadj
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_mean_252d_base_v069_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of vol_surge_x_p_buy scaled by closeadj
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_mean_504d_base_v070_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revgrowth_x_grossmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_mean_21d_base_v071_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revgrowth_x_grossmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_mean_63d_base_v072_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revgrowth_x_grossmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_mean_126d_base_v073_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revgrowth_x_grossmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_mean_252d_base_v074_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revgrowth_x_grossmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_mean_504d_base_v075_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revgrowth_x_fcf_margin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_mean_21d_base_v076_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revgrowth_x_fcf_margin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_mean_63d_base_v077_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revgrowth_x_fcf_margin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_mean_126d_base_v078_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revgrowth_x_fcf_margin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_mean_252d_base_v079_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revgrowth_x_fcf_margin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_mean_504d_base_v080_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revgrowth_x_opmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_mean_21d_base_v081_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revgrowth_x_opmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_mean_63d_base_v082_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revgrowth_x_opmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_mean_126d_base_v083_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revgrowth_x_opmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_mean_252d_base_v084_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revgrowth_x_opmargin scaled by closeadj
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_mean_504d_base_v085_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_2y_lag_x_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_mean_21d_base_v086_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_2y_lag_x_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_mean_63d_base_v087_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_2y_lag_x_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_mean_126d_base_v088_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_2y_lag_x_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_mean_252d_base_v089_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_2y_lag_x_revgrowth scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_mean_504d_base_v090_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_growth_x_rev_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_mean_21d_base_v091_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_growth_x_rev_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_mean_63d_base_v092_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_growth_x_rev_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_mean_126d_base_v093_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_growth_x_rev_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_mean_252d_base_v094_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_growth_x_rev_accel scaled by closeadj
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_mean_504d_base_v095_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netcash_pos_x_p_buy_x_compr scaled by closeadj
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_mean_21d_base_v096_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netcash_pos_x_p_buy_x_compr scaled by closeadj
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_mean_63d_base_v097_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netcash_pos_x_p_buy_x_compr scaled by closeadj
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_mean_126d_base_v098_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netcash_pos_x_p_buy_x_compr scaled by closeadj
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_mean_252d_base_v099_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netcash_pos_x_p_buy_x_compr scaled by closeadj
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_mean_504d_base_v100_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

