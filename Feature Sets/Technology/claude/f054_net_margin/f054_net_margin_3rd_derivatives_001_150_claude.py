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


# 21d acceleration of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_accel_21d_3d_v001_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_accel_63d_3d_v002_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_accel_126d_3d_v003_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_accel_252d_3d_v004_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netmargin
def f054ntm_f054_net_margin_netmargin_accel_21d_3d_v005_signal(netmargin, closeadj):
    base = netmargin
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netmargin
def f054ntm_f054_net_margin_netmargin_accel_63d_3d_v006_signal(netmargin, closeadj):
    base = netmargin
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netmargin
def f054ntm_f054_net_margin_netmargin_accel_126d_3d_v007_signal(netmargin, closeadj):
    base = netmargin
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netmargin
def f054ntm_f054_net_margin_netmargin_accel_252d_3d_v008_signal(netmargin, closeadj):
    base = netmargin
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_accel_21d_3d_v009_signal(netinc, closeadj):
    base = netinc
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_accel_63d_3d_v010_signal(netinc, closeadj):
    base = netinc
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_accel_126d_3d_v011_signal(netinc, closeadj):
    base = netinc
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_accel_252d_3d_v012_signal(netinc, closeadj):
    base = netinc
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_accel_21d_3d_v013_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_accel_63d_3d_v014_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_accel_126d_3d_v015_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_accel_252d_3d_v016_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_accel_21d_3d_v017_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_accel_63d_3d_v018_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_accel_126d_3d_v019_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_accel_252d_3d_v020_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_accel_21d_3d_v021_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_accel_63d_3d_v022_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_accel_126d_3d_v023_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_accel_252d_3d_v024_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_accel_21d_3d_v025_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_accel_63d_3d_v026_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_accel_126d_3d_v027_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_accel_252d_3d_v028_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_accel_21d_3d_v029_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_accel_63d_3d_v030_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_accel_126d_3d_v031_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_accel_252d_3d_v032_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_accel_21d_3d_v033_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_accel_63d_3d_v034_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_accel_126d_3d_v035_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_accel_252d_3d_v036_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_accel_21d_3d_v037_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_accel_63d_3d_v038_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_accel_126d_3d_v039_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_accel_252d_3d_v040_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_accel_21d_3d_v041_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_accel_63d_3d_v042_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_accel_126d_3d_v043_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_accel_252d_3d_v044_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_accel_21d_3d_v045_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_accel_63d_3d_v046_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_accel_126d_3d_v047_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_accel_252d_3d_v048_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_accel_21d_3d_v049_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_accel_63d_3d_v050_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_accel_126d_3d_v051_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_accel_252d_3d_v052_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slopez_21d_z126_3d_v053_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slopez_63d_z252_3d_v054_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slopez_126d_z252_3d_v055_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_slopez_252d_z504_3d_v056_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netmargin
def f054ntm_f054_net_margin_netmargin_slopez_21d_z126_3d_v057_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netmargin
def f054ntm_f054_net_margin_netmargin_slopez_63d_z252_3d_v058_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netmargin
def f054ntm_f054_net_margin_netmargin_slopez_126d_z252_3d_v059_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netmargin
def f054ntm_f054_net_margin_netmargin_slopez_252d_z504_3d_v060_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slopez_21d_z126_3d_v061_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slopez_63d_z252_3d_v062_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slopez_126d_z252_3d_v063_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_slopez_252d_z504_3d_v064_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slopez_21d_z126_3d_v065_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slopez_63d_z252_3d_v066_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slopez_126d_z252_3d_v067_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_slopez_252d_z504_3d_v068_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slopez_21d_z126_3d_v069_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slopez_63d_z252_3d_v070_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slopez_126d_z252_3d_v071_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_slopez_252d_z504_3d_v072_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slopez_21d_z126_3d_v073_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slopez_63d_z252_3d_v074_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slopez_126d_z252_3d_v075_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_slopez_252d_z504_3d_v076_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slopez_21d_z126_3d_v077_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slopez_63d_z252_3d_v078_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slopez_126d_z252_3d_v079_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_slopez_252d_z504_3d_v080_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slopez_21d_z126_3d_v081_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slopez_63d_z252_3d_v082_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slopez_126d_z252_3d_v083_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_slopez_252d_z504_3d_v084_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slopez_21d_z126_3d_v085_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slopez_63d_z252_3d_v086_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slopez_126d_z252_3d_v087_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_slopez_252d_z504_3d_v088_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slopez_21d_z126_3d_v089_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slopez_63d_z252_3d_v090_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slopez_126d_z252_3d_v091_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_slopez_252d_z504_3d_v092_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slopez_21d_z126_3d_v093_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slopez_63d_z252_3d_v094_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slopez_126d_z252_3d_v095_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_slopez_252d_z504_3d_v096_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slopez_21d_z126_3d_v097_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slopez_63d_z252_3d_v098_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slopez_126d_z252_3d_v099_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_slopez_252d_z504_3d_v100_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slopez_21d_z126_3d_v101_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slopez_63d_z252_3d_v102_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slopez_126d_z252_3d_v103_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_slopez_252d_z504_3d_v104_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_jerk_21d_3d_v105_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_jerk_63d_3d_v106_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_jerk_126d_3d_v107_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netmargin
def f054ntm_f054_net_margin_netmargin_jerk_21d_3d_v108_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netmargin
def f054ntm_f054_net_margin_netmargin_jerk_63d_3d_v109_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netmargin
def f054ntm_f054_net_margin_netmargin_jerk_126d_3d_v110_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_jerk_21d_3d_v111_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_jerk_63d_3d_v112_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_jerk_126d_3d_v113_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_jerk_21d_3d_v114_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_jerk_63d_3d_v115_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_jerk_126d_3d_v116_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_jerk_21d_3d_v117_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_jerk_63d_3d_v118_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_jerk_126d_3d_v119_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_jerk_21d_3d_v120_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_jerk_63d_3d_v121_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_jerk_126d_3d_v122_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_jerk_21d_3d_v123_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_jerk_63d_3d_v124_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_jerk_126d_3d_v125_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_jerk_21d_3d_v126_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_jerk_63d_3d_v127_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_jerk_126d_3d_v128_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_jerk_21d_3d_v129_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_jerk_63d_3d_v130_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_jerk_126d_3d_v131_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_jerk_21d_3d_v132_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_jerk_63d_3d_v133_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_jerk_126d_3d_v134_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_jerk_21d_3d_v135_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_jerk_63d_3d_v136_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_jerk_126d_3d_v137_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_jerk_21d_3d_v138_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_jerk_63d_3d_v139_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_jerk_126d_3d_v140_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_jerk_21d_3d_v141_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_jerk_63d_3d_v142_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_jerk_126d_3d_v143_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netmargin_calc smoothed over 252d
def f054ntm_f054_net_margin_netmargin_calc_smoothaccel_63d_sm252_3d_v144_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netmargin_calc smoothed over 504d
def f054ntm_f054_net_margin_netmargin_calc_smoothaccel_252d_sm504_3d_v145_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netmargin smoothed over 252d
def f054ntm_f054_net_margin_netmargin_smoothaccel_63d_sm252_3d_v146_signal(netmargin, closeadj):
    base = netmargin
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netmargin smoothed over 504d
def f054ntm_f054_net_margin_netmargin_smoothaccel_252d_sm504_3d_v147_signal(netmargin, closeadj):
    base = netmargin
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netinc_lvl smoothed over 252d
def f054ntm_f054_net_margin_netinc_lvl_smoothaccel_63d_sm252_3d_v148_signal(netinc, closeadj):
    base = netinc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netinc_lvl smoothed over 504d
def f054ntm_f054_net_margin_netinc_lvl_smoothaccel_252d_sm504_3d_v149_signal(netinc, closeadj):
    base = netinc
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of netinc_yoy smoothed over 252d
def f054ntm_f054_net_margin_netinc_yoy_smoothaccel_63d_sm252_3d_v150_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of netinc_yoy smoothed over 504d
def f054ntm_f054_net_margin_netinc_yoy_smoothaccel_252d_sm504_3d_v151_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_yoy_chg smoothed over 252d
def f054ntm_f054_net_margin_nm_yoy_chg_smoothaccel_63d_sm252_3d_v152_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_yoy_chg smoothed over 504d
def f054ntm_f054_net_margin_nm_yoy_chg_smoothaccel_252d_sm504_3d_v153_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_vol_252 smoothed over 252d
def f054ntm_f054_net_margin_nm_vol_252_smoothaccel_63d_sm252_3d_v154_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_vol_252 smoothed over 504d
def f054ntm_f054_net_margin_nm_vol_252_smoothaccel_252d_sm504_3d_v155_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ni_to_asset smoothed over 252d
def f054ntm_f054_net_margin_ni_to_asset_smoothaccel_63d_sm252_3d_v156_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ni_to_asset smoothed over 504d
def f054ntm_f054_net_margin_ni_to_asset_smoothaccel_252d_sm504_3d_v157_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_peer_sector_dist smoothed over 252d
def f054ntm_f054_net_margin_nm_peer_sector_dist_smoothaccel_63d_sm252_3d_v158_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_peer_sector_dist smoothed over 504d
def f054ntm_f054_net_margin_nm_peer_sector_dist_smoothaccel_252d_sm504_3d_v159_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_peer_sector_z smoothed over 252d
def f054ntm_f054_net_margin_nm_peer_sector_z_smoothaccel_63d_sm252_3d_v160_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_peer_sector_z smoothed over 504d
def f054ntm_f054_net_margin_nm_peer_sector_z_smoothaccel_252d_sm504_3d_v161_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_peer_industry_dist smoothed over 252d
def f054ntm_f054_net_margin_nm_peer_industry_dist_smoothaccel_63d_sm252_3d_v162_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_peer_industry_dist smoothed over 504d
def f054ntm_f054_net_margin_nm_peer_industry_dist_smoothaccel_252d_sm504_3d_v163_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_peer_mcap_bucket_dist smoothed over 252d
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v164_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_peer_mcap_bucket_dist smoothed over 504d
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v165_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_peer_sector_pctile smoothed over 252d
def f054ntm_f054_net_margin_nm_peer_sector_pctile_smoothaccel_63d_sm252_3d_v166_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_peer_sector_pctile smoothed over 504d
def f054ntm_f054_net_margin_nm_peer_sector_pctile_smoothaccel_252d_sm504_3d_v167_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_peer_industry_pctile smoothed over 252d
def f054ntm_f054_net_margin_nm_peer_industry_pctile_smoothaccel_63d_sm252_3d_v168_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_peer_industry_pctile smoothed over 504d
def f054ntm_f054_net_margin_nm_peer_industry_pctile_smoothaccel_252d_sm504_3d_v169_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_accelz_21d_z252_3d_v170_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_accelz_63d_z504_3d_v171_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netmargin
def f054ntm_f054_net_margin_netmargin_accelz_21d_z252_3d_v172_signal(netmargin, closeadj):
    base = netmargin
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netmargin
def f054ntm_f054_net_margin_netmargin_accelz_63d_z504_3d_v173_signal(netmargin, closeadj):
    base = netmargin
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_accelz_21d_z252_3d_v174_signal(netinc, closeadj):
    base = netinc
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_accelz_63d_z504_3d_v175_signal(netinc, closeadj):
    base = netinc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_accelz_21d_z252_3d_v176_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_accelz_63d_z504_3d_v177_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_accelz_21d_z252_3d_v178_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_accelz_63d_z504_3d_v179_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_accelz_21d_z252_3d_v180_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_accelz_63d_z504_3d_v181_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_accelz_21d_z252_3d_v182_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_accelz_63d_z504_3d_v183_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_accelz_21d_z252_3d_v184_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_accelz_63d_z504_3d_v185_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_accelz_21d_z252_3d_v186_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_accelz_63d_z504_3d_v187_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_accelz_21d_z252_3d_v188_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_accelz_63d_z504_3d_v189_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_accelz_21d_z252_3d_v190_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_accelz_63d_z504_3d_v191_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_accelz_21d_z252_3d_v192_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_accelz_63d_z504_3d_v193_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_accelz_21d_z252_3d_v194_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_accelz_63d_z504_3d_v195_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netmargin_calc (raw count, no price scaling)
def f054ntm_f054_net_margin_netmargin_calc_signflip_63d_3d_v196_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netmargin_calc (raw count, no price scaling)
def f054ntm_f054_net_margin_netmargin_calc_signflip_252d_3d_v197_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netmargin (raw count, no price scaling)
def f054ntm_f054_net_margin_netmargin_signflip_63d_3d_v198_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in netmargin (raw count, no price scaling)
def f054ntm_f054_net_margin_netmargin_signflip_252d_3d_v199_signal(netmargin, closeadj):
    base = netmargin
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in netinc_lvl (raw count, no price scaling)
def f054ntm_f054_net_margin_netinc_lvl_signflip_63d_3d_v200_signal(netinc, closeadj):
    base = netinc
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

