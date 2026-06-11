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
def _f049_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w//2)).mean()
    s = revenue.rolling(w, min_periods=max(1, w//2)).std()
    return s / m.replace(0, np.nan).abs()


# 21d acceleration of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_accel_21d_3d_v001_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_accel_63d_3d_v002_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_accel_126d_3d_v003_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_accel_252d_3d_v004_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_accel_21d_3d_v005_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_accel_63d_3d_v006_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_accel_126d_3d_v007_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_accel_252d_3d_v008_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_accel_21d_3d_v009_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_accel_63d_3d_v010_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_accel_126d_3d_v011_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_accel_252d_3d_v012_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_accel_21d_3d_v013_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_accel_63d_3d_v014_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_accel_126d_3d_v015_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_accel_252d_3d_v016_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_accel_21d_3d_v017_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_accel_63d_3d_v018_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_accel_126d_3d_v019_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_accel_252d_3d_v020_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_accel_21d_3d_v021_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_accel_63d_3d_v022_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_accel_126d_3d_v023_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_accel_252d_3d_v024_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_accel_21d_3d_v025_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_accel_63d_3d_v026_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_accel_126d_3d_v027_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_accel_252d_3d_v028_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_slopez_21d_z126_3d_v029_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_slopez_63d_z252_3d_v030_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_slopez_126d_z252_3d_v031_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_slopez_252d_z504_3d_v032_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_slopez_21d_z126_3d_v033_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_slopez_63d_z252_3d_v034_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_slopez_126d_z252_3d_v035_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_slopez_252d_z504_3d_v036_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_slopez_21d_z126_3d_v037_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_slopez_63d_z252_3d_v038_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_slopez_126d_z252_3d_v039_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_slopez_252d_z504_3d_v040_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_slopez_21d_z126_3d_v041_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_slopez_63d_z252_3d_v042_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_slopez_126d_z252_3d_v043_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_slopez_252d_z504_3d_v044_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_slopez_21d_z126_3d_v045_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_slopez_63d_z252_3d_v046_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_slopez_126d_z252_3d_v047_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_slopez_252d_z504_3d_v048_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_slopez_21d_z126_3d_v049_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_slopez_63d_z252_3d_v050_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_slopez_126d_z252_3d_v051_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_slopez_252d_z504_3d_v052_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_slopez_21d_z126_3d_v053_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_slopez_63d_z252_3d_v054_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_slopez_126d_z252_3d_v055_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_slopez_252d_z504_3d_v056_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_jerk_21d_3d_v057_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_jerk_63d_3d_v058_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_jerk_126d_3d_v059_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_jerk_21d_3d_v060_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_jerk_63d_3d_v061_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_jerk_126d_3d_v062_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_jerk_21d_3d_v063_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_jerk_63d_3d_v064_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_jerk_126d_3d_v065_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_jerk_21d_3d_v066_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_jerk_63d_3d_v067_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_jerk_126d_3d_v068_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_jerk_21d_3d_v069_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_jerk_63d_3d_v070_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_jerk_126d_3d_v071_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_jerk_21d_3d_v072_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_jerk_63d_3d_v073_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_jerk_126d_3d_v074_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_jerk_21d_3d_v075_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_jerk_63d_3d_v076_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_jerk_126d_3d_v077_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_cv_252 smoothed over 252d
def f049rvd_f049_revenue_durability_rev_cv_252_smoothaccel_63d_sm252_3d_v078_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_cv_252 smoothed over 504d
def f049rvd_f049_revenue_durability_rev_cv_252_smoothaccel_252d_sm504_3d_v079_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_cv_504 smoothed over 252d
def f049rvd_f049_revenue_durability_rev_cv_504_smoothaccel_63d_sm252_3d_v080_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_cv_504 smoothed over 504d
def f049rvd_f049_revenue_durability_rev_cv_504_smoothaccel_252d_sm504_3d_v081_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_std_252 smoothed over 252d
def f049rvd_f049_revenue_durability_rev_std_252_smoothaccel_63d_sm252_3d_v082_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_std_252 smoothed over 504d
def f049rvd_f049_revenue_durability_rev_std_252_smoothaccel_252d_sm504_3d_v083_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_hit_ratio_qoq smoothed over 252d
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_smoothaccel_63d_sm252_3d_v084_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_hit_ratio_qoq smoothed over 504d
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_smoothaccel_252d_sm504_3d_v085_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_drop_count_252 smoothed over 252d
def f049rvd_f049_revenue_durability_rev_drop_count_252_smoothaccel_63d_sm252_3d_v086_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_drop_count_252 smoothed over 504d
def f049rvd_f049_revenue_durability_rev_drop_count_252_smoothaccel_252d_sm504_3d_v087_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_log_growth_vol smoothed over 252d
def f049rvd_f049_revenue_durability_rev_log_growth_vol_smoothaccel_63d_sm252_3d_v088_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_log_growth_vol smoothed over 504d
def f049rvd_f049_revenue_durability_rev_log_growth_vol_smoothaccel_252d_sm504_3d_v089_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_max_dd_252 smoothed over 252d
def f049rvd_f049_revenue_durability_rev_max_dd_252_smoothaccel_63d_sm252_3d_v090_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_max_dd_252 smoothed over 504d
def f049rvd_f049_revenue_durability_rev_max_dd_252_smoothaccel_252d_sm504_3d_v091_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_accelz_21d_z252_3d_v092_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_accelz_63d_z504_3d_v093_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_accelz_21d_z252_3d_v094_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_accelz_63d_z504_3d_v095_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_accelz_21d_z252_3d_v096_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_accelz_63d_z504_3d_v097_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_accelz_21d_z252_3d_v098_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_accelz_63d_z504_3d_v099_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_accelz_21d_z252_3d_v100_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_accelz_63d_z504_3d_v101_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_accelz_21d_z252_3d_v102_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_accelz_63d_z504_3d_v103_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_accelz_21d_z252_3d_v104_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_accelz_63d_z504_3d_v105_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_cv_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_cv_252_signflip_63d_3d_v106_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_cv_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_cv_252_signflip_252d_3d_v107_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_cv_504 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_cv_504_signflip_63d_3d_v108_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_cv_504 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_cv_504_signflip_252d_3d_v109_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_std_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_std_252_signflip_63d_3d_v110_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_std_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_std_252_signflip_252d_3d_v111_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_hit_ratio_qoq (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_signflip_63d_3d_v112_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_hit_ratio_qoq (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_signflip_252d_3d_v113_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_drop_count_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_drop_count_252_signflip_63d_3d_v114_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_drop_count_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_drop_count_252_signflip_252d_3d_v115_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_log_growth_vol (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_log_growth_vol_signflip_63d_3d_v116_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_log_growth_vol (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_log_growth_vol_signflip_252d_3d_v117_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_max_dd_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_max_dd_252_signflip_63d_3d_v118_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_max_dd_252 (raw count, no price scaling)
def f049rvd_f049_revenue_durability_rev_max_dd_252_signflip_252d_3d_v119_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_cv_252 normalized by 252d range
def f049rvd_f049_revenue_durability_rev_cv_252_rngaccel_63d_r252_3d_v120_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_cv_252 normalized by 504d range
def f049rvd_f049_revenue_durability_rev_cv_252_rngaccel_252d_r504_3d_v121_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_cv_504 normalized by 252d range
def f049rvd_f049_revenue_durability_rev_cv_504_rngaccel_63d_r252_3d_v122_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_cv_504 normalized by 504d range
def f049rvd_f049_revenue_durability_rev_cv_504_rngaccel_252d_r504_3d_v123_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_std_252 normalized by 252d range
def f049rvd_f049_revenue_durability_rev_std_252_rngaccel_63d_r252_3d_v124_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_std_252 normalized by 504d range
def f049rvd_f049_revenue_durability_rev_std_252_rngaccel_252d_r504_3d_v125_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_hit_ratio_qoq normalized by 252d range
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_rngaccel_63d_r252_3d_v126_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_hit_ratio_qoq normalized by 504d range
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_rngaccel_252d_r504_3d_v127_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_drop_count_252 normalized by 252d range
def f049rvd_f049_revenue_durability_rev_drop_count_252_rngaccel_63d_r252_3d_v128_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_drop_count_252 normalized by 504d range
def f049rvd_f049_revenue_durability_rev_drop_count_252_rngaccel_252d_r504_3d_v129_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_log_growth_vol normalized by 252d range
def f049rvd_f049_revenue_durability_rev_log_growth_vol_rngaccel_63d_r252_3d_v130_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_log_growth_vol normalized by 504d range
def f049rvd_f049_revenue_durability_rev_log_growth_vol_rngaccel_252d_r504_3d_v131_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_max_dd_252 normalized by 252d range
def f049rvd_f049_revenue_durability_rev_max_dd_252_rngaccel_63d_r252_3d_v132_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_max_dd_252 normalized by 504d range
def f049rvd_f049_revenue_durability_rev_max_dd_252_rngaccel_252d_r504_3d_v133_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_cumslope_21d_3d_v134_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_cumslope_63d_3d_v135_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_cumslope_252d_3d_v136_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_cumslope_21d_3d_v137_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_cumslope_63d_3d_v138_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_cumslope_252d_3d_v139_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_cumslope_21d_3d_v140_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_cumslope_63d_3d_v141_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_cumslope_252d_3d_v142_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_cumslope_21d_3d_v143_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_cumslope_63d_3d_v144_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_cumslope_252d_3d_v145_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_cumslope_21d_3d_v146_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_cumslope_63d_3d_v147_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_cumslope_252d_3d_v148_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_cumslope_21d_3d_v149_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_cumslope_63d_3d_v150_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

