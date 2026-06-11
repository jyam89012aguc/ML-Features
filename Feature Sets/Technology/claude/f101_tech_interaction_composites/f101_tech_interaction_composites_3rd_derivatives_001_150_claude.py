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


# 21d acceleration of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_accel_21d_3d_v001_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_accel_63d_3d_v002_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_accel_126d_3d_v003_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_accel_252d_3d_v004_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_accel_21d_3d_v005_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_accel_63d_3d_v006_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_accel_126d_3d_v007_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_accel_252d_3d_v008_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_accel_21d_3d_v009_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_accel_63d_3d_v010_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_accel_126d_3d_v011_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_accel_252d_3d_v012_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_accel_21d_3d_v013_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_accel_63d_3d_v014_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_accel_126d_3d_v015_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_accel_252d_3d_v016_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_accel_21d_3d_v017_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_accel_63d_3d_v018_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_accel_126d_3d_v019_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_accel_252d_3d_v020_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_accel_21d_3d_v021_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_accel_63d_3d_v022_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_accel_126d_3d_v023_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_accel_252d_3d_v024_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_accel_21d_3d_v025_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_accel_63d_3d_v026_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_accel_126d_3d_v027_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_accel_252d_3d_v028_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_accel_21d_3d_v029_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_accel_63d_3d_v030_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_accel_126d_3d_v031_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_accel_252d_3d_v032_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_accel_21d_3d_v033_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_accel_63d_3d_v034_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_accel_126d_3d_v035_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_accel_252d_3d_v036_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_accel_21d_3d_v037_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_accel_63d_3d_v038_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_accel_126d_3d_v039_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_accel_252d_3d_v040_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_accel_21d_3d_v041_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_accel_63d_3d_v042_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_accel_126d_3d_v043_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_accel_252d_3d_v044_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_accel_21d_3d_v045_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_accel_63d_3d_v046_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_accel_126d_3d_v047_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_accel_252d_3d_v048_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_accel_21d_3d_v049_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_accel_63d_3d_v050_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_accel_126d_3d_v051_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_accel_252d_3d_v052_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_accel_21d_3d_v053_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_accel_63d_3d_v054_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_accel_126d_3d_v055_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_accel_252d_3d_v056_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_accel_21d_3d_v057_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_accel_63d_3d_v058_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_accel_126d_3d_v059_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_accel_252d_3d_v060_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_accel_21d_3d_v061_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_accel_63d_3d_v062_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_accel_126d_3d_v063_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_accel_252d_3d_v064_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_accel_21d_3d_v065_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_accel_63d_3d_v066_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_accel_126d_3d_v067_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_accel_252d_3d_v068_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_accel_21d_3d_v069_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_accel_63d_3d_v070_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_accel_126d_3d_v071_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_accel_252d_3d_v072_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_accel_21d_3d_v073_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_accel_63d_3d_v074_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_accel_126d_3d_v075_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_accel_252d_3d_v076_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_accel_21d_3d_v077_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_accel_63d_3d_v078_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_accel_126d_3d_v079_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_accel_252d_3d_v080_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_accel_21d_3d_v081_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_accel_63d_3d_v082_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_accel_126d_3d_v083_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_accel_252d_3d_v084_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_accel_21d_3d_v085_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_accel_63d_3d_v086_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_accel_126d_3d_v087_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_accel_252d_3d_v088_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slopez_21d_z126_3d_v089_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slopez_63d_z252_3d_v090_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slopez_126d_z252_3d_v091_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_slopez_252d_z504_3d_v092_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slopez_21d_z126_3d_v093_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slopez_63d_z252_3d_v094_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slopez_126d_z252_3d_v095_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_slopez_252d_z504_3d_v096_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slopez_21d_z126_3d_v097_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slopez_63d_z252_3d_v098_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slopez_126d_z252_3d_v099_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_slopez_252d_z504_3d_v100_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slopez_21d_z126_3d_v101_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slopez_63d_z252_3d_v102_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slopez_126d_z252_3d_v103_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_slopez_252d_z504_3d_v104_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slopez_21d_z126_3d_v105_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slopez_63d_z252_3d_v106_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slopez_126d_z252_3d_v107_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_slopez_252d_z504_3d_v108_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slopez_21d_z126_3d_v109_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slopez_63d_z252_3d_v110_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slopez_126d_z252_3d_v111_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_slopez_252d_z504_3d_v112_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slopez_21d_z126_3d_v113_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slopez_63d_z252_3d_v114_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slopez_126d_z252_3d_v115_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_slopez_252d_z504_3d_v116_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slopez_21d_z126_3d_v117_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slopez_63d_z252_3d_v118_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slopez_126d_z252_3d_v119_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_slopez_252d_z504_3d_v120_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slopez_21d_z126_3d_v121_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slopez_63d_z252_3d_v122_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slopez_126d_z252_3d_v123_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of inst_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_inst_qoq_x_drawdown_252_slopez_252d_z504_3d_v124_signal(inst_total_value, marketcap, closeadj):
    base = inst_total_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slopez_21d_z126_3d_v125_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slopez_63d_z252_3d_v126_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slopez_126d_z252_3d_v127_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of specialist_qoq_x_drawdown_252
def f101tic_f101_tech_interaction_composites_specialist_qoq_x_drawdown_252_slopez_252d_z504_3d_v128_signal(specialist_fund_value, marketcap, closeadj):
    base = specialist_fund_value.diff(periods=63) / marketcap.replace(0, np.nan).abs() * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slopez_21d_z126_3d_v129_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slopez_63d_z252_3d_v130_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slopez_126d_z252_3d_v131_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of new_holder_x_drawdown_252
def f101tic_f101_tech_interaction_composites_new_holder_x_drawdown_252_slopez_252d_z504_3d_v132_signal(new_holder_count, closeadj):
    base = new_holder_count * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slopez_21d_z126_3d_v133_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slopez_63d_z252_3d_v134_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slopez_126d_z252_3d_v135_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dollar_vol_x_mom_63d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_63d_slopez_252d_z504_3d_v136_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slopez_21d_z126_3d_v137_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slopez_63d_z252_3d_v138_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slopez_126d_z252_3d_v139_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of dollar_vol_x_mom_252d
def f101tic_f101_tech_interaction_composites_dollar_vol_x_mom_252d_slopez_252d_z504_3d_v140_signal(volume, closeadj):
    base = (volume * closeadj) * closeadj.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slopez_21d_z126_3d_v141_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slopez_63d_z252_3d_v142_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slopez_126d_z252_3d_v143_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of vol_surge_x_p_buy
def f101tic_f101_tech_interaction_composites_vol_surge_x_p_buy_slopez_252d_z504_3d_v144_signal(volume, insider_p_buy_value, marketcap, closeadj):
    base = (volume / volume.rolling(252, min_periods=63).mean().replace(0, np.nan)) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slopez_21d_z126_3d_v145_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slopez_63d_z252_3d_v146_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slopez_126d_z252_3d_v147_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revgrowth_x_grossmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_grossmargin_slopez_252d_z504_3d_v148_signal(revenue, gp, closeadj):
    base = _f101_revgrowth(revenue) * (gp / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slopez_21d_z126_3d_v149_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slopez_63d_z252_3d_v150_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slopez_126d_z252_3d_v151_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revgrowth_x_fcf_margin
def f101tic_f101_tech_interaction_composites_revgrowth_x_fcf_margin_slopez_252d_z504_3d_v152_signal(revenue, fcf, closeadj):
    base = _f101_revgrowth(revenue) * _f101_fcf_margin(fcf, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slopez_21d_z126_3d_v153_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slopez_63d_z252_3d_v154_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slopez_126d_z252_3d_v155_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revgrowth_x_opmargin
def f101tic_f101_tech_interaction_composites_revgrowth_x_opmargin_slopez_252d_z504_3d_v156_signal(revenue, opinc, closeadj):
    base = _f101_revgrowth(revenue) * (opinc / revenue.replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slopez_21d_z126_3d_v157_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slopez_63d_z252_3d_v158_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slopez_126d_z252_3d_v159_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_2y_lag_x_revgrowth
def f101tic_f101_tech_interaction_composites_rnd_2y_lag_x_revgrowth_slopez_252d_z504_3d_v160_signal(rnd, revenue, closeadj):
    base = rnd.shift(504) * _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slopez_21d_z126_3d_v161_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slopez_63d_z252_3d_v162_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slopez_126d_z252_3d_v163_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_growth_x_rev_accel
def f101tic_f101_tech_interaction_composites_rnd_growth_x_rev_accel_slopez_252d_z504_3d_v164_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(252))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slopez_21d_z126_3d_v165_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slopez_63d_z252_3d_v166_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slopez_126d_z252_3d_v167_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netcash_pos_x_p_buy_x_compr
def f101tic_f101_tech_interaction_composites_netcash_pos_x_p_buy_x_compr_slopez_252d_z504_3d_v168_signal(cashneq, investmentsc, debt, insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = ((cashneq + investmentsc - debt) > 0).astype(float) * (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slopez_21d_z126_3d_v169_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slopez_63d_z252_3d_v170_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slopez_126d_z252_3d_v171_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of roic_x_drawdown_252
def f101tic_f101_tech_interaction_composites_roic_x_drawdown_252_slopez_252d_z504_3d_v172_signal(roic, closeadj):
    base = roic * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slopez_21d_z126_3d_v173_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slopez_63d_z252_3d_v174_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slopez_126d_z252_3d_v175_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcfm_x_drawdown_252
def f101tic_f101_tech_interaction_composites_fcfm_x_drawdown_252_slopez_252d_z504_3d_v176_signal(fcf, revenue, closeadj):
    base = _f101_fcf_margin(fcf, revenue) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_jerk_21d_3d_v177_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_jerk_63d_3d_v178_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evsales_minus_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_minus_revgrowth_jerk_126d_3d_v179_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) - _f101_revgrowth(revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_jerk_21d_3d_v180_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_jerk_63d_3d_v181_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of evsales_per_revgrowth
def f101tic_f101_tech_interaction_composites_evsales_per_revgrowth_jerk_126d_3d_v182_signal(ev, revenue, closeadj):
    base = _f101_evsales(ev, revenue) / _f101_revgrowth(revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_jerk_21d_3d_v183_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_jerk_63d_3d_v184_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revgrowth_per_evsales
def f101tic_f101_tech_interaction_composites_revgrowth_per_evsales_jerk_126d_3d_v185_signal(ev, revenue, closeadj):
    base = _f101_revgrowth(revenue) / _f101_evsales(ev, revenue).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_jerk_21d_3d_v186_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_jerk_63d_3d_v187_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of multiple_reset_growth_accel
def f101tic_f101_tech_interaction_composites_multiple_reset_growth_accel_jerk_126d_3d_v188_signal(ev, revenue, closeadj):
    base = ((_f101_evsales(ev, revenue) < _f101_evsales(ev, revenue).rolling(252, min_periods=63).quantile(0.25)).astype(float)) * (_f101_revgrowth(revenue) - _f101_revgrowth(revenue).shift(63))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_jerk_21d_3d_v189_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_jerk_63d_3d_v190_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_buy_x_evsales_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_evsales_compression_jerk_126d_3d_v191_signal(insider_p_buy_value, marketcap, ev, revenue, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - _f101_evsales(ev, revenue) / _f101_evsales(ev, revenue).rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_jerk_21d_3d_v192_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_jerk_63d_3d_v193_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_buy_x_pb_compression
def f101tic_f101_tech_interaction_composites_p_buy_x_pb_compression_jerk_126d_3d_v194_signal(insider_p_buy_value, marketcap, pb, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * (1 - pb / pb.rolling(252, min_periods=63).max().replace(0, np.nan).abs())
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_jerk_21d_3d_v195_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_jerk_63d_3d_v196_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_buy_x_drawdown_252d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_252d_jerk_126d_3d_v197_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_jerk_21d_3d_v198_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_jerk_63d_3d_v199_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_buy_x_drawdown_63d
def f101tic_f101_tech_interaction_composites_p_buy_x_drawdown_63d_jerk_126d_3d_v200_signal(insider_p_buy_value, marketcap, closeadj):
    base = (insider_p_buy_value / marketcap.replace(0, np.nan).abs()) * _f101_drawdown(closeadj, 63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

