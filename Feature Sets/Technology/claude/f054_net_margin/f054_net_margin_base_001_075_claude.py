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
def _f054_nm(netinc, revenue):
    return netinc / revenue.abs().replace(0, np.nan)


# 21d mean of netmargin_calc scaled by closeadj
def f054ntm_f054_net_margin_netmargin_calc_mean_21d_base_v001_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netmargin_calc scaled by closeadj
def f054ntm_f054_net_margin_netmargin_calc_mean_63d_base_v002_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netmargin_calc scaled by closeadj
def f054ntm_f054_net_margin_netmargin_calc_mean_126d_base_v003_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netmargin_calc scaled by closeadj
def f054ntm_f054_net_margin_netmargin_calc_mean_252d_base_v004_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netmargin_calc scaled by closeadj
def f054ntm_f054_net_margin_netmargin_calc_mean_504d_base_v005_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netmargin scaled by closeadj
def f054ntm_f054_net_margin_netmargin_mean_21d_base_v006_signal(netmargin, closeadj):
    base = netmargin
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netmargin scaled by closeadj
def f054ntm_f054_net_margin_netmargin_mean_63d_base_v007_signal(netmargin, closeadj):
    base = netmargin
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netmargin scaled by closeadj
def f054ntm_f054_net_margin_netmargin_mean_126d_base_v008_signal(netmargin, closeadj):
    base = netmargin
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netmargin scaled by closeadj
def f054ntm_f054_net_margin_netmargin_mean_252d_base_v009_signal(netmargin, closeadj):
    base = netmargin
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netmargin scaled by closeadj
def f054ntm_f054_net_margin_netmargin_mean_504d_base_v010_signal(netmargin, closeadj):
    base = netmargin
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netinc_lvl scaled by closeadj
def f054ntm_f054_net_margin_netinc_lvl_mean_21d_base_v011_signal(netinc, closeadj):
    base = netinc
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netinc_lvl scaled by closeadj
def f054ntm_f054_net_margin_netinc_lvl_mean_63d_base_v012_signal(netinc, closeadj):
    base = netinc
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netinc_lvl scaled by closeadj
def f054ntm_f054_net_margin_netinc_lvl_mean_126d_base_v013_signal(netinc, closeadj):
    base = netinc
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netinc_lvl scaled by closeadj
def f054ntm_f054_net_margin_netinc_lvl_mean_252d_base_v014_signal(netinc, closeadj):
    base = netinc
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netinc_lvl scaled by closeadj
def f054ntm_f054_net_margin_netinc_lvl_mean_504d_base_v015_signal(netinc, closeadj):
    base = netinc
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of netinc_yoy scaled by closeadj
def f054ntm_f054_net_margin_netinc_yoy_mean_21d_base_v016_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of netinc_yoy scaled by closeadj
def f054ntm_f054_net_margin_netinc_yoy_mean_63d_base_v017_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of netinc_yoy scaled by closeadj
def f054ntm_f054_net_margin_netinc_yoy_mean_126d_base_v018_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of netinc_yoy scaled by closeadj
def f054ntm_f054_net_margin_netinc_yoy_mean_252d_base_v019_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of netinc_yoy scaled by closeadj
def f054ntm_f054_net_margin_netinc_yoy_mean_504d_base_v020_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_yoy_chg scaled by closeadj
def f054ntm_f054_net_margin_nm_yoy_chg_mean_21d_base_v021_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_yoy_chg scaled by closeadj
def f054ntm_f054_net_margin_nm_yoy_chg_mean_63d_base_v022_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_yoy_chg scaled by closeadj
def f054ntm_f054_net_margin_nm_yoy_chg_mean_126d_base_v023_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_yoy_chg scaled by closeadj
def f054ntm_f054_net_margin_nm_yoy_chg_mean_252d_base_v024_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_yoy_chg scaled by closeadj
def f054ntm_f054_net_margin_nm_yoy_chg_mean_504d_base_v025_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_vol_252 scaled by closeadj
def f054ntm_f054_net_margin_nm_vol_252_mean_21d_base_v026_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_vol_252 scaled by closeadj
def f054ntm_f054_net_margin_nm_vol_252_mean_63d_base_v027_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_vol_252 scaled by closeadj
def f054ntm_f054_net_margin_nm_vol_252_mean_126d_base_v028_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_vol_252 scaled by closeadj
def f054ntm_f054_net_margin_nm_vol_252_mean_252d_base_v029_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_vol_252 scaled by closeadj
def f054ntm_f054_net_margin_nm_vol_252_mean_504d_base_v030_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ni_to_asset scaled by closeadj
def f054ntm_f054_net_margin_ni_to_asset_mean_21d_base_v031_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ni_to_asset scaled by closeadj
def f054ntm_f054_net_margin_ni_to_asset_mean_63d_base_v032_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ni_to_asset scaled by closeadj
def f054ntm_f054_net_margin_ni_to_asset_mean_126d_base_v033_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ni_to_asset scaled by closeadj
def f054ntm_f054_net_margin_ni_to_asset_mean_252d_base_v034_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ni_to_asset scaled by closeadj
def f054ntm_f054_net_margin_ni_to_asset_mean_504d_base_v035_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_peer_sector_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_dist_mean_21d_base_v036_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_peer_sector_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_dist_mean_63d_base_v037_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_peer_sector_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_dist_mean_126d_base_v038_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_peer_sector_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_dist_mean_252d_base_v039_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_peer_sector_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_dist_mean_504d_base_v040_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_peer_sector_z scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_z_mean_21d_base_v041_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_peer_sector_z scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_z_mean_63d_base_v042_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_peer_sector_z scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_z_mean_126d_base_v043_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_peer_sector_z scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_z_mean_252d_base_v044_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_peer_sector_z scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_z_mean_504d_base_v045_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_peer_industry_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_dist_mean_21d_base_v046_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_peer_industry_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_dist_mean_63d_base_v047_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_peer_industry_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_dist_mean_126d_base_v048_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_peer_industry_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_dist_mean_252d_base_v049_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_peer_industry_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_dist_mean_504d_base_v050_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_peer_mcap_bucket_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_mean_21d_base_v051_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_peer_mcap_bucket_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_mean_63d_base_v052_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_peer_mcap_bucket_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_mean_126d_base_v053_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_peer_mcap_bucket_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_mean_252d_base_v054_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_peer_mcap_bucket_dist scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_mean_504d_base_v055_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_peer_sector_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_pctile_mean_21d_base_v056_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_peer_sector_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_pctile_mean_63d_base_v057_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_peer_sector_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_pctile_mean_126d_base_v058_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_peer_sector_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_pctile_mean_252d_base_v059_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_peer_sector_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_sector_pctile_mean_504d_base_v060_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_peer_industry_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_pctile_mean_21d_base_v061_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_peer_industry_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_pctile_mean_63d_base_v062_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_peer_industry_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_pctile_mean_126d_base_v063_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_peer_industry_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_pctile_mean_252d_base_v064_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_peer_industry_pctile scaled by closeadj
def f054ntm_f054_net_margin_nm_peer_industry_pctile_mean_504d_base_v065_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_median_63d_base_v066_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_median_252d_base_v067_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_median_504d_base_v068_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netmargin
def f054ntm_f054_net_margin_netmargin_median_63d_base_v069_signal(netmargin, closeadj):
    base = netmargin
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netmargin
def f054ntm_f054_net_margin_netmargin_median_252d_base_v070_signal(netmargin, closeadj):
    base = netmargin
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netmargin
def f054ntm_f054_net_margin_netmargin_median_504d_base_v071_signal(netmargin, closeadj):
    base = netmargin
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_median_63d_base_v072_signal(netinc, closeadj):
    base = netinc
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_median_252d_base_v073_signal(netinc, closeadj):
    base = netinc
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_median_504d_base_v074_signal(netinc, closeadj):
    base = netinc
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_median_63d_base_v075_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_median_252d_base_v076_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_median_504d_base_v077_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_median_63d_base_v078_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_median_252d_base_v079_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_median_504d_base_v080_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_median_63d_base_v081_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_median_252d_base_v082_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_median_504d_base_v083_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_median_63d_base_v084_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_median_252d_base_v085_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_median_504d_base_v086_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_median_63d_base_v087_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_median_252d_base_v088_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_median_504d_base_v089_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_median_63d_base_v090_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_median_252d_base_v091_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_median_504d_base_v092_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_median_63d_base_v093_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_median_252d_base_v094_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_median_504d_base_v095_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_median_63d_base_v096_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_median_252d_base_v097_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_median_504d_base_v098_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_median_63d_base_v099_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_median_252d_base_v100_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

