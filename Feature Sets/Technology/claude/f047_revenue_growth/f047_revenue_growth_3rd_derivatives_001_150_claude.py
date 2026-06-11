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
def _f047_yoy(revenue):
    return revenue.pct_change(periods=252)


# 21d acceleration of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_accel_21d_3d_v001_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_accel_63d_3d_v002_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_accel_126d_3d_v003_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_accel_252d_3d_v004_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_accel_21d_3d_v005_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_accel_63d_3d_v006_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_accel_126d_3d_v007_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_accel_252d_3d_v008_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_accel_21d_3d_v009_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_accel_63d_3d_v010_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_accel_126d_3d_v011_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_accel_252d_3d_v012_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_accel_21d_3d_v013_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_accel_63d_3d_v014_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_accel_126d_3d_v015_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_accel_252d_3d_v016_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_accel_21d_3d_v017_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_accel_63d_3d_v018_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_accel_126d_3d_v019_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_accel_252d_3d_v020_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_accel_21d_3d_v021_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_accel_63d_3d_v022_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_accel_126d_3d_v023_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_accel_252d_3d_v024_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_accel_21d_3d_v025_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_accel_63d_3d_v026_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_accel_126d_3d_v027_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_accel_252d_3d_v028_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_accel_21d_3d_v029_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_accel_63d_3d_v030_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_accel_126d_3d_v031_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_accel_252d_3d_v032_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_accel_21d_3d_v033_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_accel_63d_3d_v034_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_accel_126d_3d_v035_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_accel_252d_3d_v036_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_accel_21d_3d_v037_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_accel_63d_3d_v038_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_accel_126d_3d_v039_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_accel_252d_3d_v040_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_accel_21d_3d_v045_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_accel_63d_3d_v046_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_accel_126d_3d_v047_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_accel_252d_3d_v048_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_accel_21d_3d_v049_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_accel_63d_3d_v050_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_accel_126d_3d_v051_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_accel_252d_3d_v052_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_slopez_21d_z126_3d_v053_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_slopez_63d_z252_3d_v054_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_slopez_126d_z252_3d_v055_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_slopez_252d_z504_3d_v056_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_slopez_21d_z126_3d_v057_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_slopez_63d_z252_3d_v058_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_slopez_126d_z252_3d_v059_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_slopez_252d_z504_3d_v060_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_slopez_21d_z126_3d_v061_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_slopez_63d_z252_3d_v062_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_slopez_126d_z252_3d_v063_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_slopez_252d_z504_3d_v064_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_slopez_21d_z126_3d_v065_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_slopez_63d_z252_3d_v066_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_slopez_126d_z252_3d_v067_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_slopez_252d_z504_3d_v068_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_slopez_21d_z126_3d_v069_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_slopez_63d_z252_3d_v070_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_slopez_126d_z252_3d_v071_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_slopez_252d_z504_3d_v072_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_slopez_21d_z126_3d_v073_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_slopez_63d_z252_3d_v074_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_slopez_126d_z252_3d_v075_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_slopez_252d_z504_3d_v076_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_slopez_21d_z126_3d_v077_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_slopez_63d_z252_3d_v078_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_slopez_126d_z252_3d_v079_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_slopez_252d_z504_3d_v080_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_slopez_21d_z126_3d_v081_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_slopez_63d_z252_3d_v082_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_slopez_126d_z252_3d_v083_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_slopez_252d_z504_3d_v084_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_slopez_21d_z126_3d_v085_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_slopez_63d_z252_3d_v086_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_slopez_126d_z252_3d_v087_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_slopez_252d_z504_3d_v088_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_slopez_21d_z126_3d_v089_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_slopez_63d_z252_3d_v090_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_slopez_126d_z252_3d_v091_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_slopez_252d_z504_3d_v092_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_jerk_21d_3d_v105_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_jerk_63d_3d_v106_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_jerk_126d_3d_v107_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_jerk_21d_3d_v108_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_jerk_63d_3d_v109_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_jerk_126d_3d_v110_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_jerk_21d_3d_v111_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_jerk_63d_3d_v112_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_jerk_126d_3d_v113_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_jerk_21d_3d_v114_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_jerk_63d_3d_v115_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_jerk_126d_3d_v116_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_jerk_21d_3d_v117_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_jerk_63d_3d_v118_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_jerk_126d_3d_v119_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_jerk_21d_3d_v120_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_jerk_63d_3d_v121_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_jerk_126d_3d_v122_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_jerk_21d_3d_v123_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_jerk_63d_3d_v124_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_jerk_126d_3d_v125_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_jerk_21d_3d_v126_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_jerk_63d_3d_v127_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_jerk_126d_3d_v128_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_jerk_21d_3d_v129_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_jerk_63d_3d_v130_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_jerk_126d_3d_v131_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_jerk_21d_3d_v132_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_jerk_63d_3d_v133_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_jerk_126d_3d_v134_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_jerk_21d_3d_v138_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_jerk_63d_3d_v139_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_jerk_126d_3d_v140_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_jerk_21d_3d_v141_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_jerk_63d_3d_v142_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_jerk_126d_3d_v143_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_qoq smoothed over 252d
def f047rvg_f047_revenue_growth_rev_qoq_smoothaccel_63d_sm252_3d_v144_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_qoq smoothed over 504d
def f047rvg_f047_revenue_growth_rev_qoq_smoothaccel_252d_sm504_3d_v145_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_smoothaccel_63d_sm252_3d_v146_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_smoothaccel_252d_sm504_3d_v147_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_3y smoothed over 252d
def f047rvg_f047_revenue_growth_rev_3y_smoothaccel_63d_sm252_3d_v148_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_3y smoothed over 504d
def f047rvg_f047_revenue_growth_rev_3y_smoothaccel_252d_sm504_3d_v149_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_5y_cagr smoothed over 252d
def f047rvg_f047_revenue_growth_rev_5y_cagr_smoothaccel_63d_sm252_3d_v150_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_5y_cagr smoothed over 504d
def f047rvg_f047_revenue_growth_rev_5y_cagr_smoothaccel_252d_sm504_3d_v151_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_slope_252d smoothed over 252d
def f047rvg_f047_revenue_growth_rev_slope_252d_smoothaccel_63d_sm252_3d_v152_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_slope_252d smoothed over 504d
def f047rvg_f047_revenue_growth_rev_slope_252d_smoothaccel_252d_sm504_3d_v153_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_q_streak smoothed over 252d
def f047rvg_f047_revenue_growth_rev_q_streak_smoothaccel_63d_sm252_3d_v154_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_q_streak smoothed over 504d
def f047rvg_f047_revenue_growth_rev_q_streak_smoothaccel_252d_sm504_3d_v155_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_growth_z_252 smoothed over 252d
def f047rvg_f047_revenue_growth_rev_growth_z_252_smoothaccel_63d_sm252_3d_v156_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_growth_z_252 smoothed over 504d
def f047rvg_f047_revenue_growth_rev_growth_z_252_smoothaccel_252d_sm504_3d_v157_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy_peer_sector_dist smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy_peer_sector_dist smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy_peer_sector_z smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy_peer_sector_z smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy_peer_industry_dist smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy_peer_industry_dist smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy_peer_mcap_bucket_dist smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy_peer_mcap_bucket_dist smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy_peer_sector_pctile smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy_peer_sector_pctile smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_yoy_peer_industry_pctile smoothed over 252d
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_yoy_peer_industry_pctile smoothed over 504d
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_accelz_21d_z252_3d_v170_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_qoq
def f047rvg_f047_revenue_growth_rev_qoq_accelz_63d_z504_3d_v171_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_accelz_21d_z252_3d_v172_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy
def f047rvg_f047_revenue_growth_rev_yoy_accelz_63d_z504_3d_v173_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_accelz_21d_z252_3d_v174_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_3y
def f047rvg_f047_revenue_growth_rev_3y_accelz_63d_z504_3d_v175_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_accelz_21d_z252_3d_v176_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_5y_cagr
def f047rvg_f047_revenue_growth_rev_5y_cagr_accelz_63d_z504_3d_v177_signal(revenue, closeadj):
    base = (revenue / revenue.shift(1260).abs().replace(0, np.nan))**(1/5) - 1
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_accelz_21d_z252_3d_v178_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_slope_252d
def f047rvg_f047_revenue_growth_rev_slope_252d_accelz_63d_z504_3d_v179_signal(revenue, closeadj):
    base = revenue.diff(periods=252) / revenue.shift(252).replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_accelz_21d_z252_3d_v180_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_q_streak
def f047rvg_f047_revenue_growth_rev_q_streak_accelz_63d_z504_3d_v181_signal(revenue, closeadj):
    base = (revenue.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_accelz_21d_z252_3d_v182_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_growth_z_252
def f047rvg_f047_revenue_growth_rev_growth_z_252_accelz_63d_z504_3d_v183_signal(revenue, closeadj):
    base = (revenue.pct_change(periods=252) - revenue.pct_change(periods=252).rolling(252, min_periods=63).mean()) / revenue.pct_change(periods=252).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_accelz_21d_z252_3d_v184_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy_peer_sector_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_dist_accelz_63d_z504_3d_v185_signal(revenue, rev_yoy_sector_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_accelz_21d_z252_3d_v186_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy_peer_sector_z
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_z_accelz_63d_z504_3d_v187_signal(revenue, rev_yoy_sector_med, rev_yoy_sector_std, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_sector_med) / rev_yoy_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_accelz_21d_z252_3d_v188_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy_peer_industry_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_dist_accelz_63d_z504_3d_v189_signal(revenue, rev_yoy_industry_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_industry_med) / rev_yoy_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy_peer_mcap_bucket_dist
def f047rvg_f047_revenue_growth_rev_yoy_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(revenue, rev_yoy_mcap_med, closeadj):
    base = (_f047_yoy(revenue) - rev_yoy_mcap_med) / rev_yoy_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy_peer_sector_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(rev_yoy_sector_pctile, closeadj):
    base = rev_yoy_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_yoy_peer_industry_pctile
def f047rvg_f047_revenue_growth_rev_yoy_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(rev_yoy_industry_pctile, closeadj):
    base = rev_yoy_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_qoq (raw count, no price scaling)
def f047rvg_f047_revenue_growth_rev_qoq_signflip_63d_3d_v196_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_qoq (raw count, no price scaling)
def f047rvg_f047_revenue_growth_rev_qoq_signflip_252d_3d_v197_signal(revenue, closeadj):
    base = revenue.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_yoy (raw count, no price scaling)
def f047rvg_f047_revenue_growth_rev_yoy_signflip_63d_3d_v198_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_yoy (raw count, no price scaling)
def f047rvg_f047_revenue_growth_rev_yoy_signflip_252d_3d_v199_signal(revenue, closeadj):
    base = _f047_yoy(revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_3y (raw count, no price scaling)
def f047rvg_f047_revenue_growth_rev_3y_signflip_63d_3d_v200_signal(revenue, closeadj):
    base = revenue.pct_change(periods=756)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

