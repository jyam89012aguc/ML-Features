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
def _f049_cv(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w//2)).mean()
    s = revenue.rolling(w, min_periods=max(1, w//2)).std()
    return s / m.replace(0, np.nan).abs()


# 21d mean of rev_cv_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_252_mean_21d_base_v001_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_cv_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_252_mean_63d_base_v002_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_cv_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_252_mean_126d_base_v003_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_cv_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_252_mean_252d_base_v004_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_cv_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_252_mean_504d_base_v005_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_cv_504 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_504_mean_21d_base_v006_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_cv_504 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_504_mean_63d_base_v007_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_cv_504 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_504_mean_126d_base_v008_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_cv_504 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_504_mean_252d_base_v009_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_cv_504 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_cv_504_mean_504d_base_v010_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_std_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_std_252_mean_21d_base_v011_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_std_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_std_252_mean_63d_base_v012_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_std_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_std_252_mean_126d_base_v013_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_std_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_std_252_mean_252d_base_v014_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_std_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_std_252_mean_504d_base_v015_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_hit_ratio_qoq scaled by closeadj
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_mean_21d_base_v016_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_hit_ratio_qoq scaled by closeadj
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_mean_63d_base_v017_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_hit_ratio_qoq scaled by closeadj
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_mean_126d_base_v018_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_hit_ratio_qoq scaled by closeadj
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_mean_252d_base_v019_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_hit_ratio_qoq scaled by closeadj
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_mean_504d_base_v020_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_drop_count_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_drop_count_252_mean_21d_base_v021_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_drop_count_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_drop_count_252_mean_63d_base_v022_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_drop_count_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_drop_count_252_mean_126d_base_v023_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_drop_count_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_drop_count_252_mean_252d_base_v024_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_drop_count_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_drop_count_252_mean_504d_base_v025_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_log_growth_vol scaled by closeadj
def f049rvd_f049_revenue_durability_rev_log_growth_vol_mean_21d_base_v026_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_log_growth_vol scaled by closeadj
def f049rvd_f049_revenue_durability_rev_log_growth_vol_mean_63d_base_v027_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_log_growth_vol scaled by closeadj
def f049rvd_f049_revenue_durability_rev_log_growth_vol_mean_126d_base_v028_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_log_growth_vol scaled by closeadj
def f049rvd_f049_revenue_durability_rev_log_growth_vol_mean_252d_base_v029_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_log_growth_vol scaled by closeadj
def f049rvd_f049_revenue_durability_rev_log_growth_vol_mean_504d_base_v030_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_max_dd_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_max_dd_252_mean_21d_base_v031_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_max_dd_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_max_dd_252_mean_63d_base_v032_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_max_dd_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_max_dd_252_mean_126d_base_v033_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_max_dd_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_max_dd_252_mean_252d_base_v034_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_max_dd_252 scaled by closeadj
def f049rvd_f049_revenue_durability_rev_max_dd_252_mean_504d_base_v035_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_median_63d_base_v036_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_median_252d_base_v037_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_median_504d_base_v038_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_median_63d_base_v039_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_median_252d_base_v040_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_median_504d_base_v041_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_median_63d_base_v042_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_median_252d_base_v043_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_median_504d_base_v044_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_median_63d_base_v045_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_median_252d_base_v046_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_median_504d_base_v047_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_median_63d_base_v048_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_median_252d_base_v049_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_median_504d_base_v050_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_median_63d_base_v051_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_median_252d_base_v052_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_median_504d_base_v053_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_median_63d_base_v054_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_median_252d_base_v055_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_median_504d_base_v056_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_rmax_252d_base_v057_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_rmax_504d_base_v058_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_rmax_252d_base_v059_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_rmax_504d_base_v060_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_rmax_252d_base_v061_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_rmax_504d_base_v062_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_rmax_252d_base_v063_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_rmax_504d_base_v064_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_rmax_252d_base_v065_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_rmax_504d_base_v066_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_rmax_252d_base_v067_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_rmax_504d_base_v068_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_rmax_252d_base_v069_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_rmax_504d_base_v070_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_rmin_252d_base_v071_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_rmin_504d_base_v072_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_rmin_252d_base_v073_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_rmin_504d_base_v074_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_rmin_252d_base_v075_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

