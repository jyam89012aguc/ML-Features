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


# 21d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slope_21d_2d_v001_signal(revenue, closeadj):
    base = revenue
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slope_63d_2d_v002_signal(revenue, closeadj):
    base = revenue
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slope_126d_2d_v003_signal(revenue, closeadj):
    base = revenue
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slope_252d_2d_v004_signal(revenue, closeadj):
    base = revenue
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_slope_504d_2d_v005_signal(revenue, closeadj):
    base = revenue
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_slope_21d_2d_v006_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_slope_63d_2d_v007_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_slope_126d_2d_v008_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_slope_252d_2d_v009_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_slope_504d_2d_v010_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slope_21d_2d_v011_signal(sps, closeadj):
    base = sps
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slope_63d_2d_v012_signal(sps, closeadj):
    base = sps
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slope_126d_2d_v013_signal(sps, closeadj):
    base = sps
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slope_252d_2d_v014_signal(sps, closeadj):
    base = sps
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_slope_504d_2d_v015_signal(sps, closeadj):
    base = sps
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slope_21d_2d_v016_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slope_63d_2d_v017_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slope_126d_2d_v018_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slope_252d_2d_v019_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_slope_504d_2d_v020_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slope_21d_2d_v021_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slope_63d_2d_v022_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slope_126d_2d_v023_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slope_252d_2d_v024_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_slope_504d_2d_v025_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slope_21d_2d_v026_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slope_63d_2d_v027_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slope_126d_2d_v028_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slope_252d_2d_v029_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_slope_504d_2d_v030_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slope_21d_2d_v031_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slope_63d_2d_v032_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slope_126d_2d_v033_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slope_252d_2d_v034_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_slope_504d_2d_v035_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slope_21d_2d_v036_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slope_63d_2d_v037_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slope_126d_2d_v038_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slope_252d_2d_v039_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_slope_504d_2d_v040_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slope_21d_2d_v041_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slope_63d_2d_v042_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slope_126d_2d_v043_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slope_252d_2d_v044_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_slope_504d_2d_v045_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slope_21d_2d_v046_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slope_63d_2d_v047_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slope_126d_2d_v048_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slope_252d_2d_v049_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_slope_504d_2d_v050_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slope_21d_2d_v056_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slope_63d_2d_v057_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slope_126d_2d_v058_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slope_252d_2d_v059_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_slope_504d_2d_v060_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slope_21d_2d_v061_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slope_63d_2d_v062_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slope_126d_2d_v063_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slope_252d_2d_v064_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_slope_504d_2d_v065_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sm21_sl21_2d_v066_signal(revenue, closeadj):
    base = _mean(revenue, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sm63_sl21_2d_v067_signal(revenue, closeadj):
    base = _mean(revenue, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sm63_sl63_2d_v068_signal(revenue, closeadj):
    base = _mean(revenue, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sm252_sl63_2d_v069_signal(revenue, closeadj):
    base = _mean(revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sm252_sl126_2d_v070_signal(revenue, closeadj):
    base = _mean(revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sm21_sl21_2d_v071_signal(revenue, closeadj):
    base = _mean(_f046_logrev(revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sm63_sl21_2d_v072_signal(revenue, closeadj):
    base = _mean(_f046_logrev(revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sm63_sl63_2d_v073_signal(revenue, closeadj):
    base = _mean(_f046_logrev(revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sm252_sl63_2d_v074_signal(revenue, closeadj):
    base = _mean(_f046_logrev(revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sm252_sl126_2d_v075_signal(revenue, closeadj):
    base = _mean(_f046_logrev(revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sm21_sl21_2d_v076_signal(sps, closeadj):
    base = _mean(sps, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sm63_sl21_2d_v077_signal(sps, closeadj):
    base = _mean(sps, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sm63_sl63_2d_v078_signal(sps, closeadj):
    base = _mean(sps, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sm252_sl63_2d_v079_signal(sps, closeadj):
    base = _mean(sps, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sm252_sl126_2d_v080_signal(sps, closeadj):
    base = _mean(sps, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sm21_sl21_2d_v081_signal(revenue, sharesbas, closeadj):
    base = _mean(revenue / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sm63_sl21_2d_v082_signal(revenue, sharesbas, closeadj):
    base = _mean(revenue / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sm63_sl63_2d_v083_signal(revenue, sharesbas, closeadj):
    base = _mean(revenue / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sm252_sl63_2d_v084_signal(revenue, sharesbas, closeadj):
    base = _mean(revenue / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sm252_sl126_2d_v085_signal(revenue, sharesbas, closeadj):
    base = _mean(revenue / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sm21_sl21_2d_v086_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sm63_sl21_2d_v087_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sm63_sl63_2d_v088_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sm252_sl63_2d_v089_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sm252_sl126_2d_v090_signal(revenue, marketcap, closeadj):
    base = _mean(revenue / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sm21_sl21_2d_v091_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sm63_sl21_2d_v092_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sm63_sl63_2d_v093_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sm252_sl63_2d_v094_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sm252_sl126_2d_v095_signal(revenue, assets, closeadj):
    base = _mean(revenue / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sm21_sl21_2d_v096_signal(revenueusd, closeadj):
    base = _mean(revenueusd, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sm63_sl21_2d_v097_signal(revenueusd, closeadj):
    base = _mean(revenueusd, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sm63_sl63_2d_v098_signal(revenueusd, closeadj):
    base = _mean(revenueusd, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sm252_sl63_2d_v099_signal(revenueusd, closeadj):
    base = _mean(revenueusd, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sm252_sl126_2d_v100_signal(revenueusd, closeadj):
    base = _mean(revenueusd, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sm21_sl21_2d_v101_signal(revenue, rev_sector_med, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sm63_sl21_2d_v102_signal(revenue, rev_sector_med, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sm63_sl63_2d_v103_signal(revenue, rev_sector_med, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sm252_sl63_2d_v104_signal(revenue, rev_sector_med, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sm252_sl126_2d_v105_signal(revenue, rev_sector_med, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sm21_sl21_2d_v106_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sm63_sl21_2d_v107_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sm63_sl63_2d_v108_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sm252_sl63_2d_v109_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sm252_sl126_2d_v110_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = _mean((revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sm21_sl21_2d_v111_signal(revenue, rev_industry_med, closeadj):
    base = _mean((revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sm63_sl21_2d_v112_signal(revenue, rev_industry_med, closeadj):
    base = _mean((revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sm63_sl63_2d_v113_signal(revenue, rev_industry_med, closeadj):
    base = _mean((revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sm252_sl63_2d_v114_signal(revenue, rev_industry_med, closeadj):
    base = _mean((revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sm252_sl126_2d_v115_signal(revenue, rev_industry_med, closeadj):
    base = _mean((revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(revenue, rev_mcap_med, closeadj):
    base = _mean((revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(revenue, rev_mcap_med, closeadj):
    base = _mean((revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(revenue, rev_mcap_med, closeadj):
    base = _mean((revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(revenue, rev_mcap_med, closeadj):
    base = _mean((revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(revenue, rev_mcap_med, closeadj):
    base = _mean((revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_sm21_sl21_2d_v121_signal(rev_sector_pctile, closeadj):
    base = _mean(rev_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_sm63_sl21_2d_v122_signal(rev_sector_pctile, closeadj):
    base = _mean(rev_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_sm63_sl63_2d_v123_signal(rev_sector_pctile, closeadj):
    base = _mean(rev_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_sm252_sl63_2d_v124_signal(rev_sector_pctile, closeadj):
    base = _mean(rev_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_sm252_sl126_2d_v125_signal(rev_sector_pctile, closeadj):
    base = _mean(rev_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_sm21_sl21_2d_v126_signal(rev_industry_pctile, closeadj):
    base = _mean(rev_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_sm63_sl21_2d_v127_signal(rev_industry_pctile, closeadj):
    base = _mean(rev_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_sm63_sl63_2d_v128_signal(rev_industry_pctile, closeadj):
    base = _mean(rev_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_sm252_sl63_2d_v129_signal(rev_industry_pctile, closeadj):
    base = _mean(rev_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_sm252_sl126_2d_v130_signal(rev_industry_pctile, closeadj):
    base = _mean(rev_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_pctslope_21d_2d_v131_signal(revenue, closeadj):
    base = revenue
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_pctslope_63d_2d_v132_signal(revenue, closeadj):
    base = revenue
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_pctslope_252d_2d_v133_signal(revenue, closeadj):
    base = revenue
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of log_rev
def f046rvl_f046_revenue_level_log_rev_pctslope_21d_2d_v134_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of log_rev
def f046rvl_f046_revenue_level_log_rev_pctslope_63d_2d_v135_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of log_rev
def f046rvl_f046_revenue_level_log_rev_pctslope_252d_2d_v136_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_pctslope_21d_2d_v137_signal(sps, closeadj):
    base = sps
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_pctslope_63d_2d_v138_signal(sps, closeadj):
    base = sps
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_pctslope_252d_2d_v139_signal(sps, closeadj):
    base = sps
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_pctslope_21d_2d_v140_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_pctslope_63d_2d_v141_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_pctslope_252d_2d_v142_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_pctslope_21d_2d_v143_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_pctslope_63d_2d_v144_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_pctslope_252d_2d_v145_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_pctslope_21d_2d_v146_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_pctslope_63d_2d_v147_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_pctslope_252d_2d_v148_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_pctslope_21d_2d_v149_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_pctslope_63d_2d_v150_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_pctslope_252d_2d_v151_signal(revenueusd, closeadj):
    base = revenueusd
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_pctslope_21d_2d_v152_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_pctslope_63d_2d_v153_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_pctslope_252d_2d_v154_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_pctslope_21d_2d_v155_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_pctslope_63d_2d_v156_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_pctslope_252d_2d_v157_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_pctslope_21d_2d_v158_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_pctslope_63d_2d_v159_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_pctslope_252d_2d_v160_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_pctslope_21d_2d_v164_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_pctslope_63d_2d_v165_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_pctslope_252d_2d_v166_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_pctslope_21d_2d_v167_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_pctslope_63d_2d_v168_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_pctslope_252d_2d_v169_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sgnslope_21d_2d_v170_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sgnslope_63d_2d_v171_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_sgnslope_252d_2d_v172_signal(revenue, closeadj):
    base = revenue
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sgnslope_21d_2d_v173_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sgnslope_63d_2d_v174_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of log_rev
def f046rvl_f046_revenue_level_log_rev_sgnslope_252d_2d_v175_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sgnslope_21d_2d_v176_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sgnslope_63d_2d_v177_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_sgnslope_252d_2d_v178_signal(sps, closeadj):
    base = sps
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sgnslope_21d_2d_v179_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sgnslope_63d_2d_v180_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_sgnslope_252d_2d_v181_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sgnslope_21d_2d_v182_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sgnslope_63d_2d_v183_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_sgnslope_252d_2d_v184_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sgnslope_21d_2d_v185_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sgnslope_63d_2d_v186_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_sgnslope_252d_2d_v187_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sgnslope_21d_2d_v188_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sgnslope_63d_2d_v189_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_usd
def f046rvl_f046_revenue_level_rev_usd_sgnslope_252d_2d_v190_signal(revenueusd, closeadj):
    base = revenueusd
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sgnslope_21d_2d_v191_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sgnslope_63d_2d_v192_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_sgnslope_252d_2d_v193_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sgnslope_21d_2d_v194_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sgnslope_63d_2d_v195_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_sgnslope_252d_2d_v196_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sgnslope_21d_2d_v197_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sgnslope_63d_2d_v198_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_sgnslope_252d_2d_v199_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

