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
def _f054_nm(netinc, revenue):
    return netinc / revenue.abs().replace(0, np.nan)


# 21d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slope_21d_2d_v001_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slope_63d_2d_v002_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slope_126d_2d_v003_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slope_252d_2d_v004_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slope_504d_2d_v005_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netmargin
def f054ntm_f054_net_margin_netmargin_slope_21d_2d_v006_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netmargin
def f054ntm_f054_net_margin_netmargin_slope_63d_2d_v007_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netmargin
def f054ntm_f054_net_margin_netmargin_slope_126d_2d_v008_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netmargin
def f054ntm_f054_net_margin_netmargin_slope_252d_2d_v009_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netmargin
def f054ntm_f054_net_margin_netmargin_slope_504d_2d_v010_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slope_21d_2d_v011_signal(netinc, closeadj):
    base = netinc
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slope_63d_2d_v012_signal(netinc, closeadj):
    base = netinc
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slope_126d_2d_v013_signal(netinc, closeadj):
    base = netinc
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slope_252d_2d_v014_signal(netinc, closeadj):
    base = netinc
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slope_504d_2d_v015_signal(netinc, closeadj):
    base = netinc
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slope_21d_2d_v016_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slope_63d_2d_v017_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slope_126d_2d_v018_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slope_252d_2d_v019_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slope_504d_2d_v020_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slope_21d_2d_v021_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slope_63d_2d_v022_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slope_126d_2d_v023_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slope_252d_2d_v024_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slope_504d_2d_v025_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slope_21d_2d_v026_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slope_63d_2d_v027_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slope_126d_2d_v028_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slope_252d_2d_v029_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slope_504d_2d_v030_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slope_21d_2d_v031_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slope_63d_2d_v032_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slope_126d_2d_v033_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slope_252d_2d_v034_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slope_504d_2d_v035_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slope_21d_2d_v036_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slope_63d_2d_v037_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slope_126d_2d_v038_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slope_252d_2d_v039_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slope_504d_2d_v040_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slope_21d_2d_v041_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slope_63d_2d_v042_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slope_126d_2d_v043_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slope_252d_2d_v044_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slope_504d_2d_v045_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slope_21d_2d_v046_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slope_63d_2d_v047_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slope_126d_2d_v048_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slope_252d_2d_v049_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slope_504d_2d_v050_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slope_21d_2d_v051_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slope_63d_2d_v052_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slope_126d_2d_v053_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slope_252d_2d_v054_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slope_504d_2d_v055_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slope_21d_2d_v056_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slope_63d_2d_v057_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slope_126d_2d_v058_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slope_252d_2d_v059_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slope_504d_2d_v060_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slope_21d_2d_v061_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slope_63d_2d_v062_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slope_126d_2d_v063_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slope_252d_2d_v064_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slope_504d_2d_v065_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sm21_sl21_2d_v066_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sm63_sl21_2d_v067_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sm63_sl63_2d_v068_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sm252_sl63_2d_v069_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sm252_sl126_2d_v070_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sm21_sl21_2d_v071_signal(netmargin, closeadj):
    base = _mean(netmargin, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sm63_sl21_2d_v072_signal(netmargin, closeadj):
    base = _mean(netmargin, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sm63_sl63_2d_v073_signal(netmargin, closeadj):
    base = _mean(netmargin, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sm252_sl63_2d_v074_signal(netmargin, closeadj):
    base = _mean(netmargin, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sm252_sl126_2d_v075_signal(netmargin, closeadj):
    base = _mean(netmargin, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sm21_sl21_2d_v076_signal(netinc, closeadj):
    base = _mean(netinc, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sm63_sl21_2d_v077_signal(netinc, closeadj):
    base = _mean(netinc, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sm63_sl63_2d_v078_signal(netinc, closeadj):
    base = _mean(netinc, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sm252_sl63_2d_v079_signal(netinc, closeadj):
    base = _mean(netinc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sm252_sl126_2d_v080_signal(netinc, closeadj):
    base = _mean(netinc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sm21_sl21_2d_v081_signal(netinc, closeadj):
    base = _mean(netinc.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sm63_sl21_2d_v082_signal(netinc, closeadj):
    base = _mean(netinc.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sm63_sl63_2d_v083_signal(netinc, closeadj):
    base = _mean(netinc.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sm252_sl63_2d_v084_signal(netinc, closeadj):
    base = _mean(netinc.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sm252_sl126_2d_v085_signal(netinc, closeadj):
    base = _mean(netinc.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sm21_sl21_2d_v086_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sm63_sl21_2d_v087_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sm63_sl63_2d_v088_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sm252_sl63_2d_v089_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sm252_sl126_2d_v090_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sm21_sl21_2d_v091_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).rolling(252, min_periods=63).std(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sm63_sl21_2d_v092_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sm63_sl63_2d_v093_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).rolling(252, min_periods=63).std(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sm252_sl63_2d_v094_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sm252_sl126_2d_v095_signal(netinc, revenue, closeadj):
    base = _mean(_f054_nm(netinc, revenue).rolling(252, min_periods=63).std(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sm21_sl21_2d_v096_signal(netinc, assets, closeadj):
    base = _mean(netinc / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sm63_sl21_2d_v097_signal(netinc, assets, closeadj):
    base = _mean(netinc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sm63_sl63_2d_v098_signal(netinc, assets, closeadj):
    base = _mean(netinc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sm252_sl63_2d_v099_signal(netinc, assets, closeadj):
    base = _mean(netinc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sm252_sl126_2d_v100_signal(netinc, assets, closeadj):
    base = _mean(netinc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sm21_sl21_2d_v101_signal(netinc, revenue, nm_sector_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sm63_sl21_2d_v102_signal(netinc, revenue, nm_sector_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sm63_sl63_2d_v103_signal(netinc, revenue, nm_sector_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sm252_sl63_2d_v104_signal(netinc, revenue, nm_sector_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sm252_sl126_2d_v105_signal(netinc, revenue, nm_sector_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sm21_sl21_2d_v106_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sm63_sl21_2d_v107_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sm63_sl63_2d_v108_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sm252_sl63_2d_v109_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sm252_sl126_2d_v110_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sm21_sl21_2d_v111_signal(netinc, revenue, nm_industry_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sm63_sl21_2d_v112_signal(netinc, revenue, nm_industry_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sm63_sl63_2d_v113_signal(netinc, revenue, nm_industry_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sm252_sl63_2d_v114_signal(netinc, revenue, nm_industry_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sm252_sl126_2d_v115_signal(netinc, revenue, nm_industry_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_sm21_sl21_2d_v116_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_sm63_sl21_2d_v117_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_sm63_sl63_2d_v118_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_sm252_sl63_2d_v119_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_sm252_sl126_2d_v120_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = _mean((_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_sm21_sl21_2d_v121_signal(nm_sector_pctile, closeadj):
    base = _mean(nm_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_sm63_sl21_2d_v122_signal(nm_sector_pctile, closeadj):
    base = _mean(nm_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_sm63_sl63_2d_v123_signal(nm_sector_pctile, closeadj):
    base = _mean(nm_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_sm252_sl63_2d_v124_signal(nm_sector_pctile, closeadj):
    base = _mean(nm_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_sm252_sl126_2d_v125_signal(nm_sector_pctile, closeadj):
    base = _mean(nm_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_sm21_sl21_2d_v126_signal(nm_industry_pctile, closeadj):
    base = _mean(nm_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_sm63_sl21_2d_v127_signal(nm_industry_pctile, closeadj):
    base = _mean(nm_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_sm63_sl63_2d_v128_signal(nm_industry_pctile, closeadj):
    base = _mean(nm_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_sm252_sl63_2d_v129_signal(nm_industry_pctile, closeadj):
    base = _mean(nm_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_sm252_sl126_2d_v130_signal(nm_industry_pctile, closeadj):
    base = _mean(nm_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_pctslope_21d_2d_v131_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_pctslope_63d_2d_v132_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_pctslope_252d_2d_v133_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netmargin
def f054ntm_f054_net_margin_netmargin_pctslope_21d_2d_v134_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netmargin
def f054ntm_f054_net_margin_netmargin_pctslope_63d_2d_v135_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netmargin
def f054ntm_f054_net_margin_netmargin_pctslope_252d_2d_v136_signal(netmargin, closeadj):
    base = netmargin
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_pctslope_21d_2d_v137_signal(netinc, closeadj):
    base = netinc
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_pctslope_63d_2d_v138_signal(netinc, closeadj):
    base = netinc
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_pctslope_252d_2d_v139_signal(netinc, closeadj):
    base = netinc
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_pctslope_21d_2d_v140_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_pctslope_63d_2d_v141_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_pctslope_252d_2d_v142_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_pctslope_21d_2d_v143_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_pctslope_63d_2d_v144_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_pctslope_252d_2d_v145_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_pctslope_21d_2d_v146_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_pctslope_63d_2d_v147_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_pctslope_252d_2d_v148_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_pctslope_21d_2d_v149_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_pctslope_63d_2d_v150_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_pctslope_252d_2d_v151_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_pctslope_21d_2d_v152_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_pctslope_63d_2d_v153_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_pctslope_252d_2d_v154_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_pctslope_21d_2d_v155_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_pctslope_63d_2d_v156_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_pctslope_252d_2d_v157_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_pctslope_21d_2d_v158_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_pctslope_63d_2d_v159_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_pctslope_252d_2d_v160_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_pctslope_21d_2d_v161_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_pctslope_63d_2d_v162_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_pctslope_252d_2d_v163_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_pctslope_21d_2d_v164_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_pctslope_63d_2d_v165_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_pctslope_252d_2d_v166_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_pctslope_21d_2d_v167_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_pctslope_63d_2d_v168_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_pctslope_252d_2d_v169_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sgnslope_21d_2d_v170_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sgnslope_63d_2d_v171_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_sgnslope_252d_2d_v172_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sgnslope_21d_2d_v173_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sgnslope_63d_2d_v174_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netmargin
def f054ntm_f054_net_margin_netmargin_sgnslope_252d_2d_v175_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sgnslope_21d_2d_v176_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sgnslope_63d_2d_v177_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_sgnslope_252d_2d_v178_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sgnslope_21d_2d_v179_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sgnslope_63d_2d_v180_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_sgnslope_252d_2d_v181_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sgnslope_21d_2d_v182_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sgnslope_63d_2d_v183_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_sgnslope_252d_2d_v184_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sgnslope_21d_2d_v185_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sgnslope_63d_2d_v186_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_sgnslope_252d_2d_v187_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sgnslope_21d_2d_v188_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sgnslope_63d_2d_v189_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_sgnslope_252d_2d_v190_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sgnslope_21d_2d_v191_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sgnslope_63d_2d_v192_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_sgnslope_252d_2d_v193_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sgnslope_21d_2d_v194_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sgnslope_63d_2d_v195_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_sgnslope_252d_2d_v196_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sgnslope_21d_2d_v197_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sgnslope_63d_2d_v198_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_sgnslope_252d_2d_v199_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_sgnslope_21d_2d_v200_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

