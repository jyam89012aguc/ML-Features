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
def _f046_logrev(revenue):
    return np.log(revenue.abs().replace(0, np.nan))


# 21d mean of rev_lvl scaled by closeadj
def f046rvl_f046_revenue_level_rev_lvl_mean_21d_base_v001_signal(revenue, closeadj):
    base = revenue
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_lvl scaled by closeadj
def f046rvl_f046_revenue_level_rev_lvl_mean_63d_base_v002_signal(revenue, closeadj):
    base = revenue
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_lvl scaled by closeadj
def f046rvl_f046_revenue_level_rev_lvl_mean_126d_base_v003_signal(revenue, closeadj):
    base = revenue
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_lvl scaled by closeadj
def f046rvl_f046_revenue_level_rev_lvl_mean_252d_base_v004_signal(revenue, closeadj):
    base = revenue
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_lvl scaled by closeadj
def f046rvl_f046_revenue_level_rev_lvl_mean_504d_base_v005_signal(revenue, closeadj):
    base = revenue
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of log_rev scaled by closeadj
def f046rvl_f046_revenue_level_log_rev_mean_21d_base_v006_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of log_rev scaled by closeadj
def f046rvl_f046_revenue_level_log_rev_mean_63d_base_v007_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of log_rev scaled by closeadj
def f046rvl_f046_revenue_level_log_rev_mean_126d_base_v008_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of log_rev scaled by closeadj
def f046rvl_f046_revenue_level_log_rev_mean_252d_base_v009_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of log_rev scaled by closeadj
def f046rvl_f046_revenue_level_log_rev_mean_504d_base_v010_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sps_lvl scaled by closeadj
def f046rvl_f046_revenue_level_sps_lvl_mean_21d_base_v011_signal(sps, closeadj):
    base = sps
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sps_lvl scaled by closeadj
def f046rvl_f046_revenue_level_sps_lvl_mean_63d_base_v012_signal(sps, closeadj):
    base = sps
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sps_lvl scaled by closeadj
def f046rvl_f046_revenue_level_sps_lvl_mean_126d_base_v013_signal(sps, closeadj):
    base = sps
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sps_lvl scaled by closeadj
def f046rvl_f046_revenue_level_sps_lvl_mean_252d_base_v014_signal(sps, closeadj):
    base = sps
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sps_lvl scaled by closeadj
def f046rvl_f046_revenue_level_sps_lvl_mean_504d_base_v015_signal(sps, closeadj):
    base = sps
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_per_share scaled by closeadj
def f046rvl_f046_revenue_level_rev_per_share_mean_21d_base_v016_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_per_share scaled by closeadj
def f046rvl_f046_revenue_level_rev_per_share_mean_63d_base_v017_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_per_share scaled by closeadj
def f046rvl_f046_revenue_level_rev_per_share_mean_126d_base_v018_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_per_share scaled by closeadj
def f046rvl_f046_revenue_level_rev_per_share_mean_252d_base_v019_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_per_share scaled by closeadj
def f046rvl_f046_revenue_level_rev_per_share_mean_504d_base_v020_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_to_mcap scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_mcap_mean_21d_base_v021_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_to_mcap scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_mcap_mean_63d_base_v022_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_to_mcap scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_mcap_mean_126d_base_v023_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_to_mcap scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_mcap_mean_252d_base_v024_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_to_mcap scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_mcap_mean_504d_base_v025_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_to_asset scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_asset_mean_21d_base_v026_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_to_asset scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_asset_mean_63d_base_v027_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_to_asset scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_asset_mean_126d_base_v028_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_to_asset scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_asset_mean_252d_base_v029_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_to_asset scaled by closeadj
def f046rvl_f046_revenue_level_rev_to_asset_mean_504d_base_v030_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_usd scaled by closeadj
def f046rvl_f046_revenue_level_rev_usd_mean_21d_base_v031_signal(revenueusd, closeadj):
    base = revenueusd
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_usd scaled by closeadj
def f046rvl_f046_revenue_level_rev_usd_mean_63d_base_v032_signal(revenueusd, closeadj):
    base = revenueusd
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_usd scaled by closeadj
def f046rvl_f046_revenue_level_rev_usd_mean_126d_base_v033_signal(revenueusd, closeadj):
    base = revenueusd
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_usd scaled by closeadj
def f046rvl_f046_revenue_level_rev_usd_mean_252d_base_v034_signal(revenueusd, closeadj):
    base = revenueusd
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_usd scaled by closeadj
def f046rvl_f046_revenue_level_rev_usd_mean_504d_base_v035_signal(revenueusd, closeadj):
    base = revenueusd
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_peer_sector_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_dist_mean_21d_base_v036_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_peer_sector_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_dist_mean_63d_base_v037_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_peer_sector_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_dist_mean_126d_base_v038_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_peer_sector_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_dist_mean_252d_base_v039_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_peer_sector_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_dist_mean_504d_base_v040_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_peer_sector_z scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_z_mean_21d_base_v041_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_peer_sector_z scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_z_mean_63d_base_v042_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_peer_sector_z scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_z_mean_126d_base_v043_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_peer_sector_z scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_z_mean_252d_base_v044_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_peer_sector_z scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_z_mean_504d_base_v045_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_peer_industry_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_dist_mean_21d_base_v046_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_peer_industry_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_dist_mean_63d_base_v047_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_peer_industry_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_dist_mean_126d_base_v048_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_peer_industry_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_dist_mean_252d_base_v049_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_peer_industry_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_dist_mean_504d_base_v050_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_peer_mcap_bucket_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_mean_21d_base_v051_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_peer_mcap_bucket_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_mean_63d_base_v052_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_peer_mcap_bucket_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_mean_126d_base_v053_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_peer_mcap_bucket_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_mean_252d_base_v054_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_peer_mcap_bucket_dist scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_mean_504d_base_v055_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_peer_sector_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_mean_21d_base_v056_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_peer_sector_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_mean_63d_base_v057_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_peer_sector_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_mean_126d_base_v058_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_peer_sector_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_mean_252d_base_v059_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_peer_sector_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_mean_504d_base_v060_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_peer_industry_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_mean_21d_base_v061_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_peer_industry_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_mean_63d_base_v062_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_peer_industry_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_mean_126d_base_v063_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_peer_industry_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_mean_252d_base_v064_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_peer_industry_pctile scaled by closeadj
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_mean_504d_base_v065_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_median_63d_base_v066_signal(revenue, closeadj):
    base = revenue
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_median_252d_base_v067_signal(revenue, closeadj):
    base = revenue
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_median_504d_base_v068_signal(revenue, closeadj):
    base = revenue
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of log_rev
def f046rvl_f046_revenue_level_log_rev_median_63d_base_v069_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of log_rev
def f046rvl_f046_revenue_level_log_rev_median_252d_base_v070_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of log_rev
def f046rvl_f046_revenue_level_log_rev_median_504d_base_v071_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_median_63d_base_v072_signal(sps, closeadj):
    base = sps
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_median_252d_base_v073_signal(sps, closeadj):
    base = sps
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_median_504d_base_v074_signal(sps, closeadj):
    base = sps
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_median_63d_base_v075_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_median_252d_base_v076_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_median_504d_base_v077_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_median_63d_base_v078_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_median_252d_base_v079_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_median_504d_base_v080_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_median_63d_base_v081_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_median_252d_base_v082_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_median_504d_base_v083_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_usd
def f046rvl_f046_revenue_level_rev_usd_median_63d_base_v084_signal(revenueusd, closeadj):
    base = revenueusd
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_usd
def f046rvl_f046_revenue_level_rev_usd_median_252d_base_v085_signal(revenueusd, closeadj):
    base = revenueusd
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_usd
def f046rvl_f046_revenue_level_rev_usd_median_504d_base_v086_signal(revenueusd, closeadj):
    base = revenueusd
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_median_63d_base_v087_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_median_252d_base_v088_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_median_504d_base_v089_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_median_63d_base_v090_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_median_252d_base_v091_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_median_504d_base_v092_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_median_63d_base_v093_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_median_252d_base_v094_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_median_504d_base_v095_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_median_63d_base_v096_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_median_252d_base_v097_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_median_504d_base_v098_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_median_63d_base_v099_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_median_252d_base_v100_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

