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


# 21d mean of rev_qoq scaled by closeadj
def f047rvg_f047_revenue_growth_rev_qoq_mean_21d_base_v001_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_qoq scaled by closeadj
def f047rvg_f047_revenue_growth_rev_qoq_mean_63d_base_v002_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_qoq scaled by closeadj
def f047rvg_f047_revenue_growth_rev_qoq_mean_126d_base_v003_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_qoq scaled by closeadj
def f047rvg_f047_revenue_growth_rev_qoq_mean_252d_base_v004_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_qoq scaled by closeadj
def f047rvg_f047_revenue_growth_rev_qoq_mean_504d_base_v005_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_mean_21d_base_v006_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_mean_63d_base_v007_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_mean_126d_base_v008_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_mean_252d_base_v009_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_mean_504d_base_v010_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_3y scaled by closeadj
def f047rvg_f047_revenue_growth_rev_3y_mean_21d_base_v011_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_3y scaled by closeadj
def f047rvg_f047_revenue_growth_rev_3y_mean_63d_base_v012_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_3y scaled by closeadj
def f047rvg_f047_revenue_growth_rev_3y_mean_126d_base_v013_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_3y scaled by closeadj
def f047rvg_f047_revenue_growth_rev_3y_mean_252d_base_v014_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_3y scaled by closeadj
def f047rvg_f047_revenue_growth_rev_3y_mean_504d_base_v015_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_5y_cagr scaled by closeadj
def f047rvg_f047_revenue_growth_rev_5y_cagr_mean_21d_base_v016_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_5y_cagr scaled by closeadj
def f047rvg_f047_revenue_growth_rev_5y_cagr_mean_63d_base_v017_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_5y_cagr scaled by closeadj
def f047rvg_f047_revenue_growth_rev_5y_cagr_mean_126d_base_v018_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_5y_cagr scaled by closeadj
def f047rvg_f047_revenue_growth_rev_5y_cagr_mean_252d_base_v019_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_5y_cagr scaled by closeadj
def f047rvg_f047_revenue_growth_rev_5y_cagr_mean_504d_base_v020_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_slope_252d scaled by closeadj
def f047rvg_f047_revenue_growth_rev_slope_252d_mean_21d_base_v021_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_slope_252d scaled by closeadj
def f047rvg_f047_revenue_growth_rev_slope_252d_mean_63d_base_v022_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_slope_252d scaled by closeadj
def f047rvg_f047_revenue_growth_rev_slope_252d_mean_126d_base_v023_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_slope_252d scaled by closeadj
def f047rvg_f047_revenue_growth_rev_slope_252d_mean_252d_base_v024_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_slope_252d scaled by closeadj
def f047rvg_f047_revenue_growth_rev_slope_252d_mean_504d_base_v025_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_q_streak scaled by closeadj
def f047rvg_f047_revenue_growth_rev_q_streak_mean_21d_base_v026_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_q_streak scaled by closeadj
def f047rvg_f047_revenue_growth_rev_q_streak_mean_63d_base_v027_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_q_streak scaled by closeadj
def f047rvg_f047_revenue_growth_rev_q_streak_mean_126d_base_v028_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_q_streak scaled by closeadj
def f047rvg_f047_revenue_growth_rev_q_streak_mean_252d_base_v029_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_q_streak scaled by closeadj
def f047rvg_f047_revenue_growth_rev_q_streak_mean_504d_base_v030_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_growth_z_252 scaled by closeadj
def f047rvg_f047_revenue_growth_rev_growth_z_252_mean_21d_base_v031_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_growth_z_252 scaled by closeadj
def f047rvg_f047_revenue_growth_rev_growth_z_252_mean_63d_base_v032_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_growth_z_252 scaled by closeadj
def f047rvg_f047_revenue_growth_rev_growth_z_252_mean_126d_base_v033_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_growth_z_252 scaled by closeadj
def f047rvg_f047_revenue_growth_rev_growth_z_252_mean_252d_base_v034_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_growth_z_252 scaled by closeadj
def f047rvg_f047_revenue_growth_rev_growth_z_252_mean_504d_base_v035_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy_peer_sector_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_mean_21d_base_v036_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy_peer_sector_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_mean_63d_base_v037_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy_peer_sector_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_mean_126d_base_v038_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy_peer_sector_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_mean_252d_base_v039_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy_peer_sector_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_mean_504d_base_v040_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy_peer_sector_z scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_mean_21d_base_v041_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy_peer_sector_z scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_mean_63d_base_v042_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy_peer_sector_z scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_mean_126d_base_v043_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy_peer_sector_z scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_mean_252d_base_v044_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy_peer_sector_z scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_mean_504d_base_v045_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy_peer_industry_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_mean_21d_base_v046_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy_peer_industry_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_mean_63d_base_v047_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy_peer_industry_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_mean_126d_base_v048_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy_peer_industry_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_mean_252d_base_v049_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy_peer_industry_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_mean_504d_base_v050_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy_peer_mcap_bucket_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_mean_21d_base_v051_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy_peer_mcap_bucket_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_mean_63d_base_v052_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy_peer_mcap_bucket_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_mean_126d_base_v053_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy_peer_mcap_bucket_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_mean_252d_base_v054_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy_peer_mcap_bucket_dist scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_mean_504d_base_v055_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy_peer_sector_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_mean_21d_base_v056_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy_peer_sector_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_mean_63d_base_v057_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy_peer_sector_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_mean_126d_base_v058_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy_peer_sector_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_mean_252d_base_v059_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy_peer_sector_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_mean_504d_base_v060_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_yoy_peer_industry_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_mean_21d_base_v061_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_yoy_peer_industry_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_mean_63d_base_v062_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_yoy_peer_industry_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_mean_126d_base_v063_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_yoy_peer_industry_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_mean_252d_base_v064_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_yoy_peer_industry_pctile scaled by closeadj
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_mean_504d_base_v065_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_median_63d_base_v066_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_median_252d_base_v067_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_median_504d_base_v068_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_median_63d_base_v069_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_median_252d_base_v070_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_median_504d_base_v071_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_median_63d_base_v072_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_median_252d_base_v073_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_median_504d_base_v074_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_median_63d_base_v075_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_median_252d_base_v076_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_median_504d_base_v077_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_median_63d_base_v078_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_median_252d_base_v079_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_median_504d_base_v080_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_median_63d_base_v081_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_median_252d_base_v082_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_median_504d_base_v083_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_median_63d_base_v084_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_median_252d_base_v085_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_median_504d_base_v086_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_median_63d_base_v087_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_median_252d_base_v088_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_median_504d_base_v089_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_median_63d_base_v090_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_median_252d_base_v091_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_median_504d_base_v092_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_median_63d_base_v093_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_median_252d_base_v094_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_median_504d_base_v095_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_median_63d_base_v096_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_median_252d_base_v097_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_median_504d_base_v098_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_median_63d_base_v099_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_median_252d_base_v100_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

