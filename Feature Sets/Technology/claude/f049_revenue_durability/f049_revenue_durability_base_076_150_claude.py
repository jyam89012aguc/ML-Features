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


# 63d z-score of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_z_63d_base_v076_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_z_126d_base_v077_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_z_252d_base_v078_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_z_504d_base_v079_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_z_63d_base_v080_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_z_126d_base_v081_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_z_252d_base_v082_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_z_504d_base_v083_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_z_63d_base_v084_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_z_126d_base_v085_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_z_252d_base_v086_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_z_504d_base_v087_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_z_63d_base_v088_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_z_126d_base_v089_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_z_252d_base_v090_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_z_504d_base_v091_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_z_63d_base_v092_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_z_126d_base_v093_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_z_252d_base_v094_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_z_504d_base_v095_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_z_63d_base_v096_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_z_126d_base_v097_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_z_252d_base_v098_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_z_504d_base_v099_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_z_63d_base_v100_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_z_126d_base_v101_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_z_252d_base_v102_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_z_504d_base_v103_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_distmax_252d_base_v104_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_distmax_504d_base_v105_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_distmax_252d_base_v106_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_distmax_504d_base_v107_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_distmax_252d_base_v108_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_distmax_504d_base_v109_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_distmax_252d_base_v110_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_distmax_504d_base_v111_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_distmax_252d_base_v112_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_distmax_504d_base_v113_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_distmax_252d_base_v114_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_distmax_504d_base_v115_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_distmax_252d_base_v116_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_distmax_504d_base_v117_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_distmed_126d_base_v118_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_distmed_252d_base_v119_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_distmed_504d_base_v120_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_distmed_126d_base_v121_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_distmed_252d_base_v122_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_distmed_504d_base_v123_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_distmed_126d_base_v124_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_distmed_252d_base_v125_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_distmed_504d_base_v126_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_distmed_126d_base_v127_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_distmed_252d_base_v128_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_distmed_504d_base_v129_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_distmed_126d_base_v130_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_distmed_252d_base_v131_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_distmed_504d_base_v132_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_distmed_126d_base_v133_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_distmed_252d_base_v134_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_distmed_504d_base_v135_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_distmed_126d_base_v136_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_distmed_252d_base_v137_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_max_dd_252
def f049rvd_f049_revenue_durability_rev_max_dd_252_distmed_504d_base_v138_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).max()) / revenue.rolling(252, min_periods=63).max().replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_chg_63d_base_v139_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_cv_252
def f049rvd_f049_revenue_durability_rev_cv_252_chg_252d_base_v140_signal(revenue, closeadj):
    base = _f049_cv(revenue, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_chg_63d_base_v141_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_cv_504
def f049rvd_f049_revenue_durability_rev_cv_504_chg_252d_base_v142_signal(revenue, closeadj):
    base = _f049_cv(revenue, 504)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_chg_63d_base_v143_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_std_252
def f049rvd_f049_revenue_durability_rev_std_252_chg_252d_base_v144_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).std()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_chg_63d_base_v145_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_hit_ratio_qoq
def f049rvd_f049_revenue_durability_rev_hit_ratio_qoq_chg_252d_base_v146_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(504, min_periods=126).mean()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_chg_63d_base_v147_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_drop_count_252
def f049rvd_f049_revenue_durability_rev_drop_count_252_chg_252d_base_v148_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) < 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_chg_63d_base_v149_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_log_growth_vol
def f049rvd_f049_revenue_durability_rev_log_growth_vol_chg_252d_base_v150_signal(revenue, closeadj):
    base = (np.log(revenue.abs().replace(0, np.nan))).diff(periods=252).rolling(504, min_periods=126).std()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

