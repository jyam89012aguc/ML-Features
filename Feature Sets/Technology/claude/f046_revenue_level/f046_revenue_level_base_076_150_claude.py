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


# 63d z-score of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_z_63d_base_v076_signal(revenue, closeadj):
    base = revenue
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_z_126d_base_v077_signal(revenue, closeadj):
    base = revenue
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_z_252d_base_v078_signal(revenue, closeadj):
    base = revenue
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_z_504d_base_v079_signal(revenue, closeadj):
    base = revenue
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of log_rev
def f046rvl_f046_revenue_level_log_rev_z_63d_base_v080_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of log_rev
def f046rvl_f046_revenue_level_log_rev_z_126d_base_v081_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of log_rev
def f046rvl_f046_revenue_level_log_rev_z_252d_base_v082_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of log_rev
def f046rvl_f046_revenue_level_log_rev_z_504d_base_v083_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_z_63d_base_v084_signal(sps, closeadj):
    base = sps
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_z_126d_base_v085_signal(sps, closeadj):
    base = sps
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_z_252d_base_v086_signal(sps, closeadj):
    base = sps
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_z_504d_base_v087_signal(sps, closeadj):
    base = sps
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_z_63d_base_v088_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_z_126d_base_v089_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_z_252d_base_v090_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_z_504d_base_v091_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_z_63d_base_v092_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_z_126d_base_v093_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_z_252d_base_v094_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_z_504d_base_v095_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_z_63d_base_v096_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_z_126d_base_v097_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_z_252d_base_v098_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_z_504d_base_v099_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_usd
def f046rvl_f046_revenue_level_rev_usd_z_63d_base_v100_signal(revenueusd, closeadj):
    base = revenueusd
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_usd
def f046rvl_f046_revenue_level_rev_usd_z_126d_base_v101_signal(revenueusd, closeadj):
    base = revenueusd
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_usd
def f046rvl_f046_revenue_level_rev_usd_z_252d_base_v102_signal(revenueusd, closeadj):
    base = revenueusd
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_usd
def f046rvl_f046_revenue_level_rev_usd_z_504d_base_v103_signal(revenueusd, closeadj):
    base = revenueusd
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_z_63d_base_v104_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_z_126d_base_v105_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_z_252d_base_v106_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_z_504d_base_v107_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_z_63d_base_v108_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_z_126d_base_v109_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_z_252d_base_v110_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_z_504d_base_v111_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_z_63d_base_v112_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_z_126d_base_v113_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_z_252d_base_v114_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_z_504d_base_v115_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_z_63d_base_v116_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_z_126d_base_v117_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_z_252d_base_v118_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_z_504d_base_v119_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_z_63d_base_v120_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_z_126d_base_v121_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_z_252d_base_v122_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_z_504d_base_v123_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_z_63d_base_v124_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_z_126d_base_v125_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_z_252d_base_v126_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_z_504d_base_v127_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_distmax_252d_base_v128_signal(revenue, closeadj):
    base = revenue
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_distmax_504d_base_v129_signal(revenue, closeadj):
    base = revenue
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of log_rev
def f046rvl_f046_revenue_level_log_rev_distmax_252d_base_v130_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of log_rev
def f046rvl_f046_revenue_level_log_rev_distmax_504d_base_v131_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_distmax_252d_base_v132_signal(sps, closeadj):
    base = sps
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_distmax_504d_base_v133_signal(sps, closeadj):
    base = sps
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_distmax_252d_base_v134_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_distmax_504d_base_v135_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_distmax_252d_base_v136_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_distmax_504d_base_v137_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_distmax_252d_base_v138_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_distmax_504d_base_v139_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_usd
def f046rvl_f046_revenue_level_rev_usd_distmax_252d_base_v140_signal(revenueusd, closeadj):
    base = revenueusd
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_usd
def f046rvl_f046_revenue_level_rev_usd_distmax_504d_base_v141_signal(revenueusd, closeadj):
    base = revenueusd
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_distmax_252d_base_v142_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_distmax_504d_base_v143_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_distmax_252d_base_v144_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_peer_sector_z
def f046rvl_f046_revenue_level_rev_peer_sector_z_distmax_504d_base_v145_signal(revenue, rev_sector_med, rev_sector_std, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_distmax_252d_base_v146_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_peer_industry_dist
def f046rvl_f046_revenue_level_rev_peer_industry_dist_distmax_504d_base_v147_signal(revenue, rev_industry_med, closeadj):
    base = (revenue - rev_industry_med) / rev_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_peer_mcap_bucket_dist
def f046rvl_f046_revenue_level_rev_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(revenue, rev_mcap_med, closeadj):
    base = (revenue - rev_mcap_med) / rev_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_distmax_252d_base_v150_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_peer_sector_pctile
def f046rvl_f046_revenue_level_rev_peer_sector_pctile_distmax_504d_base_v151_signal(rev_sector_pctile, closeadj):
    base = rev_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_distmax_252d_base_v152_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_peer_industry_pctile
def f046rvl_f046_revenue_level_rev_peer_industry_pctile_distmax_504d_base_v153_signal(rev_industry_pctile, closeadj):
    base = rev_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_distmed_126d_base_v154_signal(revenue, closeadj):
    base = revenue
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_distmed_252d_base_v155_signal(revenue, closeadj):
    base = revenue
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_lvl
def f046rvl_f046_revenue_level_rev_lvl_distmed_504d_base_v156_signal(revenue, closeadj):
    base = revenue
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of log_rev
def f046rvl_f046_revenue_level_log_rev_distmed_126d_base_v157_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of log_rev
def f046rvl_f046_revenue_level_log_rev_distmed_252d_base_v158_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of log_rev
def f046rvl_f046_revenue_level_log_rev_distmed_504d_base_v159_signal(revenue, closeadj):
    base = _f046_logrev(revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_distmed_126d_base_v160_signal(sps, closeadj):
    base = sps
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_distmed_252d_base_v161_signal(sps, closeadj):
    base = sps
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of sps_lvl
def f046rvl_f046_revenue_level_sps_lvl_distmed_504d_base_v162_signal(sps, closeadj):
    base = sps
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_distmed_126d_base_v163_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_distmed_252d_base_v164_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_per_share
def f046rvl_f046_revenue_level_rev_per_share_distmed_504d_base_v165_signal(revenue, sharesbas, closeadj):
    base = revenue / sharesbas.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_distmed_126d_base_v166_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_distmed_252d_base_v167_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_to_mcap
def f046rvl_f046_revenue_level_rev_to_mcap_distmed_504d_base_v168_signal(revenue, marketcap, closeadj):
    base = revenue / marketcap.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_distmed_126d_base_v169_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_distmed_252d_base_v170_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_to_asset
def f046rvl_f046_revenue_level_rev_to_asset_distmed_504d_base_v171_signal(revenue, assets, closeadj):
    base = revenue / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_usd
def f046rvl_f046_revenue_level_rev_usd_distmed_126d_base_v172_signal(revenueusd, closeadj):
    base = revenueusd
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_usd
def f046rvl_f046_revenue_level_rev_usd_distmed_252d_base_v173_signal(revenueusd, closeadj):
    base = revenueusd
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_usd
def f046rvl_f046_revenue_level_rev_usd_distmed_504d_base_v174_signal(revenueusd, closeadj):
    base = revenueusd
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_peer_sector_dist
def f046rvl_f046_revenue_level_rev_peer_sector_dist_distmed_126d_base_v175_signal(revenue, rev_sector_med, closeadj):
    base = (revenue - rev_sector_med) / rev_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

