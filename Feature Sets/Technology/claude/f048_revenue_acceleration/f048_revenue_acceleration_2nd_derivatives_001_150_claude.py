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


# 21d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slope_21d_2d_v001_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slope_63d_2d_v002_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slope_126d_2d_v003_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slope_252d_2d_v004_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_slope_504d_2d_v005_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slope_21d_2d_v006_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slope_63d_2d_v007_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slope_126d_2d_v008_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slope_252d_2d_v009_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_slope_504d_2d_v010_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slope_21d_2d_v011_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slope_63d_2d_v012_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slope_126d_2d_v013_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slope_252d_2d_v014_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_slope_504d_2d_v015_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slope_21d_2d_v016_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slope_63d_2d_v017_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slope_126d_2d_v018_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slope_252d_2d_v019_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_slope_504d_2d_v020_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slope_21d_2d_v021_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slope_63d_2d_v022_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slope_126d_2d_v023_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slope_252d_2d_v024_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_slope_504d_2d_v025_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slope_21d_2d_v026_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slope_63d_2d_v027_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slope_126d_2d_v028_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slope_252d_2d_v029_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_slope_504d_2d_v030_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slope_21d_2d_v031_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slope_63d_2d_v032_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slope_126d_2d_v033_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slope_252d_2d_v034_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_slope_504d_2d_v035_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sm21_sl21_2d_v036_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sm63_sl21_2d_v037_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sm63_sl63_2d_v038_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sm252_sl63_2d_v039_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sm252_sl126_2d_v040_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sm21_sl21_2d_v041_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sm63_sl21_2d_v042_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sm63_sl63_2d_v043_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sm252_sl63_2d_v044_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sm252_sl126_2d_v045_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sm21_sl21_2d_v046_signal(revenue, closeadj):
    base = _mean(revenue.diff(periods=252).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sm63_sl21_2d_v047_signal(revenue, closeadj):
    base = _mean(revenue.diff(periods=252).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sm63_sl63_2d_v048_signal(revenue, closeadj):
    base = _mean(revenue.diff(periods=252).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sm252_sl63_2d_v049_signal(revenue, closeadj):
    base = _mean(revenue.diff(periods=252).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sm252_sl126_2d_v050_signal(revenue, closeadj):
    base = _mean(revenue.diff(periods=252).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sm21_sl21_2d_v051_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63).diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sm63_sl21_2d_v052_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63).diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sm63_sl63_2d_v053_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63).diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sm252_sl63_2d_v054_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63).diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sm252_sl126_2d_v055_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 63).diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sm21_sl21_2d_v056_signal(revenue, closeadj):
    base = _mean((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sm63_sl21_2d_v057_signal(revenue, closeadj):
    base = _mean((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sm63_sl63_2d_v058_signal(revenue, closeadj):
    base = _mean((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sm252_sl63_2d_v059_signal(revenue, closeadj):
    base = _mean((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sm252_sl126_2d_v060_signal(revenue, closeadj):
    base = _mean((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sm21_sl21_2d_v061_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sm63_sl21_2d_v062_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sm63_sl63_2d_v063_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sm252_sl63_2d_v064_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sm252_sl126_2d_v065_signal(revenue, closeadj):
    base = _mean(_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sm21_sl21_2d_v066_signal(revenue, closeadj):
    base = _mean(revenue.pct_change(periods=63).rolling(252, min_periods=63).mean(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sm63_sl21_2d_v067_signal(revenue, closeadj):
    base = _mean(revenue.pct_change(periods=63).rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sm63_sl63_2d_v068_signal(revenue, closeadj):
    base = _mean(revenue.pct_change(periods=63).rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sm252_sl63_2d_v069_signal(revenue, closeadj):
    base = _mean(revenue.pct_change(periods=63).rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sm252_sl126_2d_v070_signal(revenue, closeadj):
    base = _mean(revenue.pct_change(periods=63).rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_pctslope_21d_2d_v071_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_pctslope_63d_2d_v072_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_pctslope_252d_2d_v073_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_pctslope_21d_2d_v074_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_pctslope_63d_2d_v075_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_pctslope_252d_2d_v076_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_pctslope_21d_2d_v077_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_pctslope_63d_2d_v078_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_pctslope_252d_2d_v079_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_pctslope_21d_2d_v080_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_pctslope_63d_2d_v081_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_pctslope_252d_2d_v082_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_pctslope_21d_2d_v083_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_pctslope_63d_2d_v084_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_pctslope_252d_2d_v085_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_pctslope_21d_2d_v086_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_pctslope_63d_2d_v087_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_pctslope_252d_2d_v088_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_pctslope_21d_2d_v089_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_pctslope_63d_2d_v090_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_pctslope_252d_2d_v091_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sgnslope_21d_2d_v092_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sgnslope_63d_2d_v093_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_sgnslope_252d_2d_v094_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sgnslope_21d_2d_v095_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sgnslope_63d_2d_v096_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_sgnslope_252d_2d_v097_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sgnslope_21d_2d_v098_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sgnslope_63d_2d_v099_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_sgnslope_252d_2d_v100_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sgnslope_21d_2d_v101_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sgnslope_63d_2d_v102_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_sgnslope_252d_2d_v103_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sgnslope_21d_2d_v104_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sgnslope_63d_2d_v105_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_sgnslope_252d_2d_v106_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sgnslope_21d_2d_v107_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sgnslope_63d_2d_v108_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_sgnslope_252d_2d_v109_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sgnslope_21d_2d_v110_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sgnslope_63d_2d_v111_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_sgnslope_252d_2d_v112_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_logmagslope_21d_2d_v113_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_logmagslope_63d_2d_v114_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_accel_q
def f048rva_f048_revenue_acceleration_rev_accel_q_logmagslope_252d_2d_v115_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_logmagslope_21d_2d_v116_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_logmagslope_63d_2d_v117_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_accel_y
def f048rva_f048_revenue_acceleration_rev_accel_y_logmagslope_252d_2d_v118_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_logmagslope_21d_2d_v119_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_logmagslope_63d_2d_v120_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_2deriv_y
def f048rva_f048_revenue_acceleration_rev_2deriv_y_logmagslope_252d_2d_v121_signal(revenue, closeadj):
    base = revenue.diff(periods=252).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_logmagslope_21d_2d_v122_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_logmagslope_63d_2d_v123_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_jerk_q
def f048rva_f048_revenue_acceleration_rev_jerk_q_logmagslope_252d_2d_v124_signal(revenue, closeadj):
    base = _f048_accel(revenue, 63).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_logmagslope_21d_2d_v125_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_logmagslope_63d_2d_v126_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_growth_signflip
def f048rva_f048_revenue_acceleration_rev_growth_signflip_logmagslope_252d_2d_v127_signal(revenue, closeadj):
    base = (np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_logmagslope_21d_2d_v128_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_logmagslope_63d_2d_v129_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_accel_to_rev
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_logmagslope_252d_2d_v130_signal(revenue, closeadj):
    base = _f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_logmagslope_21d_2d_v131_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_logmagslope_63d_2d_v132_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_growth_trend_252
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_logmagslope_252d_2d_v133_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_accel_q|
def f048rva_f048_revenue_acceleration_rev_accel_q_logslope_63d_2d_v134_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_accel_q|
def f048rva_f048_revenue_acceleration_rev_accel_q_logslope_252d_2d_v135_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_accel_y|
def f048rva_f048_revenue_acceleration_rev_accel_y_logslope_63d_2d_v136_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_accel_y|
def f048rva_f048_revenue_acceleration_rev_accel_y_logslope_252d_2d_v137_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_2deriv_y|
def f048rva_f048_revenue_acceleration_rev_2deriv_y_logslope_63d_2d_v138_signal(revenue, closeadj):
    base = np.log((revenue.diff(periods=252).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_2deriv_y|
def f048rva_f048_revenue_acceleration_rev_2deriv_y_logslope_252d_2d_v139_signal(revenue, closeadj):
    base = np.log((revenue.diff(periods=252).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_jerk_q|
def f048rva_f048_revenue_acceleration_rev_jerk_q_logslope_63d_2d_v140_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 63).diff(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_jerk_q|
def f048rva_f048_revenue_acceleration_rev_jerk_q_logslope_252d_2d_v141_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 63).diff(periods=63)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_growth_signflip|
def f048rva_f048_revenue_acceleration_rev_growth_signflip_logslope_63d_2d_v142_signal(revenue, closeadj):
    base = np.log(((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_growth_signflip|
def f048rva_f048_revenue_acceleration_rev_growth_signflip_logslope_252d_2d_v143_signal(revenue, closeadj):
    base = np.log(((np.sign(revenue.pct_change(periods=252)) != np.sign(revenue.pct_change(periods=252).shift(63))).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_accel_to_rev|
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_logslope_63d_2d_v144_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_accel_to_rev|
def f048rva_f048_revenue_acceleration_rev_accel_to_rev_logslope_252d_2d_v145_signal(revenue, closeadj):
    base = np.log((_f048_accel(revenue, 252) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_growth_trend_252|
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_logslope_63d_2d_v146_signal(revenue, closeadj):
    base = np.log((revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_growth_trend_252|
def f048rva_f048_revenue_acceleration_rev_growth_trend_252_logslope_252d_2d_v147_signal(revenue, closeadj):
    base = np.log((revenue.pct_change(periods=63).rolling(252, min_periods=63).mean()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

