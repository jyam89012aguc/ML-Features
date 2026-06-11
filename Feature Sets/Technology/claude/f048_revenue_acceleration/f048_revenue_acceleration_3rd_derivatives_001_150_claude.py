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
def _f048_accel(revenue, n):
    g = revenue.pct_change(periods=n)
    return g.diff(periods=n)


# 21d acceleration of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_accel_21d_3d_v001_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_accel_63d_3d_v002_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_accel_126d_3d_v003_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_accel_252d_3d_v004_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_accel_21d_3d_v005_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_accel_63d_3d_v006_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_accel_126d_3d_v007_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_accel_252d_3d_v008_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_accel_21d_3d_v009_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_accel_63d_3d_v010_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_accel_126d_3d_v011_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_accel_252d_3d_v012_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_accel_21d_3d_v013_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_accel_63d_3d_v014_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_accel_126d_3d_v015_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_accel_252d_3d_v016_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_accel_21d_3d_v017_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_accel_63d_3d_v018_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_accel_126d_3d_v019_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_accel_252d_3d_v020_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_accel_21d_3d_v021_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_accel_63d_3d_v022_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_accel_126d_3d_v023_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_accel_252d_3d_v024_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_accel_21d_3d_v025_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_accel_63d_3d_v026_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_accel_126d_3d_v027_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_accel_252d_3d_v028_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slopez_21d_z126_3d_v029_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slopez_63d_z252_3d_v030_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slopez_126d_z252_3d_v031_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slopez_252d_z504_3d_v032_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slopez_21d_z126_3d_v033_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slopez_63d_z252_3d_v034_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slopez_126d_z252_3d_v035_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slopez_252d_z504_3d_v036_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slopez_21d_z126_3d_v037_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slopez_63d_z252_3d_v038_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slopez_126d_z252_3d_v039_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slopez_252d_z504_3d_v040_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slopez_21d_z126_3d_v041_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slopez_63d_z252_3d_v042_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slopez_126d_z252_3d_v043_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slopez_252d_z504_3d_v044_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slopez_21d_z126_3d_v045_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slopez_63d_z252_3d_v046_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slopez_126d_z252_3d_v047_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slopez_252d_z504_3d_v048_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slopez_21d_z126_3d_v049_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slopez_63d_z252_3d_v050_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slopez_126d_z252_3d_v051_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slopez_252d_z504_3d_v052_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slopez_21d_z126_3d_v053_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slopez_63d_z252_3d_v054_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slopez_126d_z252_3d_v055_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slopez_252d_z504_3d_v056_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_jerk_21d_3d_v057_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_jerk_63d_3d_v058_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_jerk_126d_3d_v059_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_jerk_21d_3d_v060_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_jerk_63d_3d_v061_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_jerk_126d_3d_v062_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_jerk_21d_3d_v063_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_jerk_63d_3d_v064_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_jerk_126d_3d_v065_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_jerk_21d_3d_v066_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_jerk_63d_3d_v067_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_jerk_126d_3d_v068_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_jerk_21d_3d_v069_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_jerk_63d_3d_v070_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_jerk_126d_3d_v071_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_jerk_21d_3d_v072_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_jerk_63d_3d_v073_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_jerk_126d_3d_v074_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_jerk_21d_3d_v075_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_jerk_63d_3d_v076_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_jerk_126d_3d_v077_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_accel_q smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_accel_q_smoothaccel_63d_sm252_3d_v078_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_accel_q smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_accel_q_smoothaccel_252d_sm504_3d_v079_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_accel_y smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_accel_y_smoothaccel_63d_sm252_3d_v080_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_accel_y smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_accel_y_smoothaccel_252d_sm504_3d_v081_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_2deriv_y smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_2deriv_y_smoothaccel_63d_sm252_3d_v082_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_2deriv_y smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_2deriv_y_smoothaccel_252d_sm504_3d_v083_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_jerk_q smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_jerk_q_smoothaccel_63d_sm252_3d_v084_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_jerk_q smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_jerk_q_smoothaccel_252d_sm504_3d_v085_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_growth_signflip smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_growth_signflip_smoothaccel_63d_sm252_3d_v086_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_growth_signflip smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_growth_signflip_smoothaccel_252d_sm504_3d_v087_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_accel_to_rev smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_smoothaccel_63d_sm252_3d_v088_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_accel_to_rev smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_smoothaccel_252d_sm504_3d_v089_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_growth_trend_252 smoothed over 252d
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_smoothaccel_63d_sm252_3d_v090_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_growth_trend_252 smoothed over 504d
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_smoothaccel_252d_sm504_3d_v091_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_accelz_21d_z252_3d_v092_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_accelz_63d_z504_3d_v093_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_accelz_21d_z252_3d_v094_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_accelz_63d_z504_3d_v095_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_accelz_21d_z252_3d_v096_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_accelz_63d_z504_3d_v097_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_accelz_21d_z252_3d_v098_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_accelz_63d_z504_3d_v099_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_accelz_21d_z252_3d_v100_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_accelz_63d_z504_3d_v101_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_accelz_21d_z252_3d_v102_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_accelz_63d_z504_3d_v103_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_accelz_21d_z252_3d_v104_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_accelz_63d_z504_3d_v105_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_accel_q (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_accel_q_signflip_63d_3d_v106_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_accel_q (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_accel_q_signflip_252d_3d_v107_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_accel_y (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_accel_y_signflip_63d_3d_v108_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_accel_y (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_accel_y_signflip_252d_3d_v109_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_2deriv_y (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_2deriv_y_signflip_63d_3d_v110_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_2deriv_y (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_2deriv_y_signflip_252d_3d_v111_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_jerk_q (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_jerk_q_signflip_63d_3d_v112_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_jerk_q (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_jerk_q_signflip_252d_3d_v113_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_growth_signflip (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_growth_signflip_signflip_63d_3d_v114_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_growth_signflip (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_growth_signflip_signflip_252d_3d_v115_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_accel_to_rev (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_signflip_63d_3d_v116_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_accel_to_rev (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_signflip_252d_3d_v117_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_growth_trend_252 (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_signflip_63d_3d_v118_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_growth_trend_252 (raw count, no price scaling)
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_signflip_252d_3d_v119_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_accel_q normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_accel_q_rngaccel_63d_r252_3d_v120_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_accel_q normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_accel_q_rngaccel_252d_r504_3d_v121_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_accel_y normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_accel_y_rngaccel_63d_r252_3d_v122_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_accel_y normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_accel_y_rngaccel_252d_r504_3d_v123_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_2deriv_y normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_2deriv_y_rngaccel_63d_r252_3d_v124_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_2deriv_y normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_2deriv_y_rngaccel_252d_r504_3d_v125_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_jerk_q normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_jerk_q_rngaccel_63d_r252_3d_v126_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_jerk_q normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_jerk_q_rngaccel_252d_r504_3d_v127_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_signflip normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_growth_signflip_rngaccel_63d_r252_3d_v128_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_signflip normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_growth_signflip_rngaccel_252d_r504_3d_v129_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_accel_to_rev normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_rngaccel_63d_r252_3d_v130_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_accel_to_rev normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_rngaccel_252d_r504_3d_v131_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_trend_252 normalized by 252d range
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_rngaccel_63d_r252_3d_v132_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_trend_252 normalized by 504d range
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_rngaccel_252d_r504_3d_v133_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_cumslope_21d_3d_v134_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_cumslope_63d_3d_v135_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_cumslope_252d_3d_v136_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_cumslope_21d_3d_v137_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_cumslope_63d_3d_v138_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_cumslope_252d_3d_v139_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_cumslope_21d_3d_v140_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_cumslope_63d_3d_v141_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_cumslope_252d_3d_v142_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_cumslope_21d_3d_v143_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_cumslope_63d_3d_v144_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_cumslope_252d_3d_v145_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_cumslope_21d_3d_v146_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_cumslope_63d_3d_v147_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_cumslope_252d_3d_v148_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_cumslope_21d_3d_v149_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_cumslope_63d_3d_v150_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

