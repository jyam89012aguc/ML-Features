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
def _f046_logrev(revenue):
    return np.log(revenue.abs().replace(0, np.nan))


# 21d acceleration of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_accel_21d_3d_v001_signal(revenue, closeadj):
    base = revenue
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_accel_63d_3d_v002_signal(revenue, closeadj):
    base = revenue
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_accel_126d_3d_v003_signal(revenue, closeadj):
    base = revenue
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_accel_252d_3d_v004_signal(revenue, closeadj):
    base = revenue
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of log_rev
def f046rvl_f046_revenue_level_log_rev_accel_21d_3d_v005_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of log_rev
def f046rvl_f046_revenue_level_log_rev_accel_63d_3d_v006_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of log_rev
def f046rvl_f046_revenue_level_log_rev_accel_126d_3d_v007_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of log_rev
def f046rvl_f046_revenue_level_log_rev_accel_252d_3d_v008_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_accel_21d_3d_v009_signal(sps, closeadj):
    base = sps
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_accel_63d_3d_v010_signal(sps, closeadj):
    base = sps
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_accel_126d_3d_v011_signal(sps, closeadj):
    base = sps
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_accel_252d_3d_v012_signal(sps, closeadj):
    base = sps
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_accel_21d_3d_v013_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_accel_63d_3d_v014_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_accel_126d_3d_v015_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_accel_252d_3d_v016_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_accel_21d_3d_v017_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_accel_63d_3d_v018_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_accel_126d_3d_v019_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_accel_252d_3d_v020_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_accel_21d_3d_v021_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_accel_63d_3d_v022_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_accel_126d_3d_v023_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_accel_252d_3d_v024_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_usd
def f046rvl_f046_revenue_level_rev_usd_accel_21d_3d_v025_signal(revenueusd, closeadj):
    base = revenueusd
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_usd
def f046rvl_f046_revenue_level_rev_usd_accel_63d_3d_v026_signal(revenueusd, closeadj):
    base = revenueusd
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_usd
def f046rvl_f046_revenue_level_rev_usd_accel_126d_3d_v027_signal(revenueusd, closeadj):
    base = revenueusd
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_usd
def f046rvl_f046_revenue_level_rev_usd_accel_252d_3d_v028_signal(revenueusd, closeadj):
    base = revenueusd
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_accel_21d_3d_v029_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_accel_63d_3d_v030_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_accel_126d_3d_v031_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_accel_252d_3d_v032_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_accel_21d_3d_v033_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_accel_63d_3d_v034_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_accel_126d_3d_v035_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_accel_252d_3d_v036_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_accel_21d_3d_v037_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_accel_63d_3d_v038_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_accel_126d_3d_v039_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_accel_252d_3d_v040_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_accel_21d_3d_v045_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_accel_63d_3d_v046_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_accel_126d_3d_v047_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_accel_252d_3d_v048_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_accel_21d_3d_v049_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_accel_63d_3d_v050_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_accel_126d_3d_v051_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_accel_252d_3d_v052_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slopez_21d_z126_3d_v053_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slopez_63d_z252_3d_v054_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slopez_126d_z252_3d_v055_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slopez_252d_z504_3d_v056_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of log_rev
def f046rvl_f046_revenue_level_log_rev_slopez_21d_z126_3d_v057_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of log_rev
def f046rvl_f046_revenue_level_log_rev_slopez_63d_z252_3d_v058_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of log_rev
def f046rvl_f046_revenue_level_log_rev_slopez_126d_z252_3d_v059_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of log_rev
def f046rvl_f046_revenue_level_log_rev_slopez_252d_z504_3d_v060_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slopez_21d_z126_3d_v061_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slopez_63d_z252_3d_v062_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slopez_126d_z252_3d_v063_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slopez_252d_z504_3d_v064_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slopez_21d_z126_3d_v065_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slopez_63d_z252_3d_v066_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slopez_126d_z252_3d_v067_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slopez_252d_z504_3d_v068_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slopez_21d_z126_3d_v069_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slopez_63d_z252_3d_v070_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slopez_126d_z252_3d_v071_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slopez_252d_z504_3d_v072_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slopez_21d_z126_3d_v073_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slopez_63d_z252_3d_v074_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slopez_126d_z252_3d_v075_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slopez_252d_z504_3d_v076_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slopez_21d_z126_3d_v077_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slopez_63d_z252_3d_v078_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slopez_126d_z252_3d_v079_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slopez_252d_z504_3d_v080_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slopez_21d_z126_3d_v081_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slopez_63d_z252_3d_v082_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slopez_126d_z252_3d_v083_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slopez_252d_z504_3d_v084_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slopez_21d_z126_3d_v085_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slopez_63d_z252_3d_v086_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slopez_126d_z252_3d_v087_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slopez_252d_z504_3d_v088_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slopez_21d_z126_3d_v089_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slopez_63d_z252_3d_v090_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slopez_126d_z252_3d_v091_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slopez_252d_z504_3d_v092_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_jerk_21d_3d_v105_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_jerk_63d_3d_v106_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_jerk_126d_3d_v107_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of log_rev
def f046rvl_f046_revenue_level_log_rev_jerk_21d_3d_v108_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of log_rev
def f046rvl_f046_revenue_level_log_rev_jerk_63d_3d_v109_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of log_rev
def f046rvl_f046_revenue_level_log_rev_jerk_126d_3d_v110_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_jerk_21d_3d_v111_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_jerk_63d_3d_v112_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_jerk_126d_3d_v113_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_jerk_21d_3d_v114_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_jerk_63d_3d_v115_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_jerk_126d_3d_v116_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_jerk_21d_3d_v117_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_jerk_63d_3d_v118_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_jerk_126d_3d_v119_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_jerk_21d_3d_v120_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_jerk_63d_3d_v121_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_jerk_126d_3d_v122_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_usd
def f046rvl_f046_revenue_level_rev_usd_jerk_21d_3d_v123_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_usd
def f046rvl_f046_revenue_level_rev_usd_jerk_63d_3d_v124_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_usd
def f046rvl_f046_revenue_level_rev_usd_jerk_126d_3d_v125_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_jerk_21d_3d_v126_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_jerk_63d_3d_v127_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_jerk_126d_3d_v128_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_jerk_21d_3d_v129_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_jerk_63d_3d_v130_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_jerk_126d_3d_v131_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_jerk_21d_3d_v132_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_jerk_63d_3d_v133_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_jerk_126d_3d_v134_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_jerk_21d_3d_v138_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_jerk_63d_3d_v139_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_jerk_126d_3d_v140_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_jerk_21d_3d_v141_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_jerk_63d_3d_v142_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_jerk_126d_3d_v143_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_lvl smoothed over 252d
def f046rvl_f046_revenue_level_rev_lvl_smoothaccel_63d_sm252_3d_v144_signal(revenue, closeadj):
    base = revenue
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_lvl smoothed over 504d
def f046rvl_f046_revenue_level_rev_lvl_smoothaccel_252d_sm504_3d_v145_signal(revenue, closeadj):
    base = revenue
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of log_rev smoothed over 252d
def f046rvl_f046_revenue_level_log_rev_smoothaccel_63d_sm252_3d_v146_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of log_rev smoothed over 504d
def f046rvl_f046_revenue_level_log_rev_smoothaccel_252d_sm504_3d_v147_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of sps_lvl smoothed over 252d
def f046rvl_f046_revenue_level_sps_lvl_smoothaccel_63d_sm252_3d_v148_signal(sps, closeadj):
    base = sps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of sps_lvl smoothed over 504d
def f046rvl_f046_revenue_level_sps_lvl_smoothaccel_252d_sm504_3d_v149_signal(sps, closeadj):
    base = sps
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_per_share smoothed over 252d
def f046rvl_f046_revenue_level_rev_per_share_smoothaccel_63d_sm252_3d_v150_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_per_share smoothed over 504d
def f046rvl_f046_revenue_level_rev_per_share_smoothaccel_252d_sm504_3d_v151_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_to_mcap smoothed over 252d
def f046rvl_f046_revenue_level_rev_to_mcap_smoothaccel_63d_sm252_3d_v152_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_to_mcap smoothed over 504d
def f046rvl_f046_revenue_level_rev_to_mcap_smoothaccel_252d_sm504_3d_v153_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_to_asset smoothed over 252d
def f046rvl_f046_revenue_level_rev_to_asset_smoothaccel_63d_sm252_3d_v154_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_to_asset smoothed over 504d
def f046rvl_f046_revenue_level_rev_to_asset_smoothaccel_252d_sm504_3d_v155_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_usd smoothed over 252d
def f046rvl_f046_revenue_level_rev_usd_smoothaccel_63d_sm252_3d_v156_signal(revenueusd, closeadj):
    base = revenueusd
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_usd smoothed over 504d
def f046rvl_f046_revenue_level_rev_usd_smoothaccel_252d_sm504_3d_v157_signal(revenueusd, closeadj):
    base = revenueusd
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_peer_sector_dist smoothed over 252d
def f046rvl_f046_revenue_level_rev_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_peer_sector_dist smoothed over 504d
def f046rvl_f046_revenue_level_rev_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_peer_sector_z smoothed over 252d
def f046rvl_f046_revenue_level_rev_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_peer_sector_z smoothed over 504d
def f046rvl_f046_revenue_level_rev_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_peer_industry_dist smoothed over 252d
def f046rvl_f046_revenue_level_rev_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_peer_industry_dist smoothed over 504d
def f046rvl_f046_revenue_level_rev_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_peer_mcap_bucket_dist smoothed over 252d
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_peer_mcap_bucket_dist smoothed over 504d
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_peer_sector_pctile smoothed over 252d
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_peer_sector_pctile smoothed over 504d
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_peer_industry_pctile smoothed over 252d
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_peer_industry_pctile smoothed over 504d
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_accelz_21d_z252_3d_v170_signal(revenue, closeadj):
    base = revenue
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_accelz_63d_z504_3d_v171_signal(revenue, closeadj):
    base = revenue
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of log_rev
def f046rvl_f046_revenue_level_log_rev_accelz_21d_z252_3d_v172_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of log_rev
def f046rvl_f046_revenue_level_log_rev_accelz_63d_z504_3d_v173_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_accelz_21d_z252_3d_v174_signal(sps, closeadj):
    base = sps
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_accelz_63d_z504_3d_v175_signal(sps, closeadj):
    base = sps
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_accelz_21d_z252_3d_v176_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_accelz_63d_z504_3d_v177_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_accelz_21d_z252_3d_v178_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_accelz_63d_z504_3d_v179_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_accelz_21d_z252_3d_v180_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_accelz_63d_z504_3d_v181_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_usd
def f046rvl_f046_revenue_level_rev_usd_accelz_21d_z252_3d_v182_signal(revenueusd, closeadj):
    base = revenueusd
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_usd
def f046rvl_f046_revenue_level_rev_usd_accelz_63d_z504_3d_v183_signal(revenueusd, closeadj):
    base = revenueusd
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_accelz_21d_z252_3d_v184_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_accelz_63d_z504_3d_v185_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_accelz_21d_z252_3d_v186_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_accelz_63d_z504_3d_v187_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_accelz_21d_z252_3d_v188_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_accelz_63d_z504_3d_v189_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_lvl (raw count, no price scaling)
def f046rvl_f046_revenue_level_rev_lvl_signflip_63d_3d_v196_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_lvl (raw count, no price scaling)
def f046rvl_f046_revenue_level_rev_lvl_signflip_252d_3d_v197_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in log_rev (raw count, no price scaling)
def f046rvl_f046_revenue_level_log_rev_signflip_63d_3d_v198_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in log_rev (raw count, no price scaling)
def f046rvl_f046_revenue_level_log_rev_signflip_252d_3d_v199_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in sps_lvl (raw count, no price scaling)
def f046rvl_f046_revenue_level_sps_lvl_signflip_63d_3d_v200_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

