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
def _f048_accel(revenue, n):
    g = revenue.pct_change(periods=n)
    return g.diff(periods=n)


# 63d z-score of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_z_63d_base_v076_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_z_126d_base_v077_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_z_252d_base_v078_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_z_504d_base_v079_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_z_63d_base_v080_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_z_126d_base_v081_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_z_252d_base_v082_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_z_504d_base_v083_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_z_63d_base_v084_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_z_126d_base_v085_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_z_252d_base_v086_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_z_504d_base_v087_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_z_63d_base_v088_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_z_126d_base_v089_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_z_252d_base_v090_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_z_504d_base_v091_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_z_63d_base_v092_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_z_126d_base_v093_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_z_252d_base_v094_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_z_504d_base_v095_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_z_63d_base_v096_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_z_126d_base_v097_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_z_252d_base_v098_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_z_504d_base_v099_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_z_63d_base_v100_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_z_126d_base_v101_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_z_252d_base_v102_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_z_504d_base_v103_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_distmax_252d_base_v104_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_distmax_504d_base_v105_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_distmax_252d_base_v106_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_distmax_504d_base_v107_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_distmax_252d_base_v108_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_distmax_504d_base_v109_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_distmax_252d_base_v110_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_distmax_504d_base_v111_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_distmax_252d_base_v112_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_distmax_504d_base_v113_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_distmax_252d_base_v114_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_distmax_504d_base_v115_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_distmax_252d_base_v116_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_distmax_504d_base_v117_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_distmed_126d_base_v118_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_distmed_252d_base_v119_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_distmed_504d_base_v120_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_distmed_126d_base_v121_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_distmed_252d_base_v122_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_distmed_504d_base_v123_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_distmed_126d_base_v124_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_distmed_252d_base_v125_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_distmed_504d_base_v126_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_distmed_126d_base_v127_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_distmed_252d_base_v128_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_distmed_504d_base_v129_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_distmed_126d_base_v130_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_distmed_252d_base_v131_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_distmed_504d_base_v132_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_distmed_126d_base_v133_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_distmed_252d_base_v134_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_distmed_504d_base_v135_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_distmed_126d_base_v136_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_distmed_252d_base_v137_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_distmed_504d_base_v138_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_chg_63d_base_v139_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_chg_252d_base_v140_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_chg_63d_base_v141_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_chg_252d_base_v142_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_chg_63d_base_v143_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_chg_252d_base_v144_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_chg_63d_base_v145_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_chg_252d_base_v146_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_chg_63d_base_v147_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_chg_252d_base_v148_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_chg_63d_base_v149_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_chg_252d_base_v150_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

