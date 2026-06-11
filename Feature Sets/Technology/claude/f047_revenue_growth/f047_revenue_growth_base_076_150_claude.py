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
def _f047_yoy(revenue):
    return revenue.pct_change(periods=252)


# 63d z-score of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_z_63d_base_v076_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_z_126d_base_v077_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_z_252d_base_v078_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_z_504d_base_v079_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_z_63d_base_v080_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_z_126d_base_v081_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_z_252d_base_v082_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_z_504d_base_v083_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_z_63d_base_v084_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_z_126d_base_v085_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_z_252d_base_v086_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_z_504d_base_v087_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_z_63d_base_v088_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_z_126d_base_v089_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_z_252d_base_v090_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_z_504d_base_v091_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_z_63d_base_v092_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_z_126d_base_v093_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_z_252d_base_v094_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_z_504d_base_v095_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_z_63d_base_v096_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_z_126d_base_v097_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_z_252d_base_v098_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_z_504d_base_v099_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_z_63d_base_v100_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_z_126d_base_v101_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_z_252d_base_v102_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_z_504d_base_v103_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_z_63d_base_v104_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_z_126d_base_v105_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_z_252d_base_v106_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_z_504d_base_v107_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_z_63d_base_v108_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_z_126d_base_v109_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_z_252d_base_v110_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_z_504d_base_v111_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_z_63d_base_v112_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_z_126d_base_v113_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_z_252d_base_v114_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_z_504d_base_v115_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_z_63d_base_v116_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_z_126d_base_v117_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_z_252d_base_v118_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_z_504d_base_v119_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_z_63d_base_v120_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_z_126d_base_v121_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_z_252d_base_v122_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_z_504d_base_v123_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_z_63d_base_v124_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_z_126d_base_v125_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_z_252d_base_v126_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_z_504d_base_v127_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_distmax_252d_base_v128_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_distmax_504d_base_v129_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_distmax_252d_base_v130_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_distmax_504d_base_v131_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_distmax_252d_base_v132_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_distmax_504d_base_v133_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_distmax_252d_base_v134_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_distmax_504d_base_v135_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_distmax_252d_base_v136_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_distmax_504d_base_v137_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_distmax_252d_base_v138_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_distmax_504d_base_v139_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_distmax_252d_base_v140_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_distmax_504d_base_v141_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_distmax_252d_base_v142_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_distmax_504d_base_v143_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_distmax_252d_base_v144_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_distmax_504d_base_v145_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_distmax_252d_base_v146_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_distmax_504d_base_v147_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_distmax_252d_base_v150_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_distmax_504d_base_v151_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_distmax_252d_base_v152_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_distmax_504d_base_v153_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_distmed_126d_base_v154_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_distmed_252d_base_v155_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_distmed_504d_base_v156_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_distmed_126d_base_v157_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_distmed_252d_base_v158_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_distmed_504d_base_v159_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_distmed_126d_base_v160_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_distmed_252d_base_v161_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_distmed_504d_base_v162_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_distmed_126d_base_v163_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_distmed_252d_base_v164_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_distmed_504d_base_v165_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_distmed_126d_base_v166_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_distmed_252d_base_v167_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_distmed_504d_base_v168_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_distmed_126d_base_v169_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_distmed_252d_base_v170_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_distmed_504d_base_v171_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_distmed_126d_base_v172_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_distmed_252d_base_v173_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_distmed_504d_base_v174_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_distmed_126d_base_v175_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

