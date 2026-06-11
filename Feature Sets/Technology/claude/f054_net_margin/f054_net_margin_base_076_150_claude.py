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


# 63d z-score of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_z_63d_base_v076_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_z_126d_base_v077_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_z_252d_base_v078_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_z_504d_base_v079_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netmargin
def f054ntm_f054_net_margin_netmargin_z_63d_base_v080_signal(netmargin, closeadj):
    base = netmargin
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netmargin
def f054ntm_f054_net_margin_netmargin_z_126d_base_v081_signal(netmargin, closeadj):
    base = netmargin
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netmargin
def f054ntm_f054_net_margin_netmargin_z_252d_base_v082_signal(netmargin, closeadj):
    base = netmargin
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netmargin
def f054ntm_f054_net_margin_netmargin_z_504d_base_v083_signal(netmargin, closeadj):
    base = netmargin
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_z_63d_base_v084_signal(netinc, closeadj):
    base = netinc
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_z_126d_base_v085_signal(netinc, closeadj):
    base = netinc
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_z_252d_base_v086_signal(netinc, closeadj):
    base = netinc
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_z_504d_base_v087_signal(netinc, closeadj):
    base = netinc
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_z_63d_base_v088_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_z_126d_base_v089_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_z_252d_base_v090_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_z_504d_base_v091_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_z_63d_base_v092_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_z_126d_base_v093_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_z_252d_base_v094_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_z_504d_base_v095_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_z_63d_base_v096_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_z_126d_base_v097_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_z_252d_base_v098_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_z_504d_base_v099_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_z_63d_base_v100_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_z_126d_base_v101_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_z_252d_base_v102_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_z_504d_base_v103_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_z_63d_base_v104_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_z_126d_base_v105_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_z_252d_base_v106_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_z_504d_base_v107_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_z_63d_base_v108_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_z_126d_base_v109_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_z_252d_base_v110_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_z_504d_base_v111_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_z_63d_base_v112_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_z_126d_base_v113_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_z_252d_base_v114_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_z_504d_base_v115_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_z_63d_base_v116_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_z_126d_base_v117_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_z_252d_base_v118_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_z_504d_base_v119_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_z_63d_base_v120_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_z_126d_base_v121_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_z_252d_base_v122_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_z_504d_base_v123_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_z_63d_base_v124_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_z_126d_base_v125_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_z_252d_base_v126_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_z_504d_base_v127_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_distmax_252d_base_v128_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_distmax_504d_base_v129_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netmargin
def f054ntm_f054_net_margin_netmargin_distmax_252d_base_v130_signal(netmargin, closeadj):
    base = netmargin
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netmargin
def f054ntm_f054_net_margin_netmargin_distmax_504d_base_v131_signal(netmargin, closeadj):
    base = netmargin
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_distmax_252d_base_v132_signal(netinc, closeadj):
    base = netinc
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_distmax_504d_base_v133_signal(netinc, closeadj):
    base = netinc
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_distmax_252d_base_v134_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_distmax_504d_base_v135_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_distmax_252d_base_v136_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_distmax_504d_base_v137_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_distmax_252d_base_v138_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_distmax_504d_base_v139_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_distmax_252d_base_v140_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_distmax_504d_base_v141_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_distmax_252d_base_v142_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_distmax_504d_base_v143_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_distmax_252d_base_v144_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_peer_sector_z
def f054ntm_f054_net_margin_nm_peer_sector_z_distmax_504d_base_v145_signal(netinc, revenue, nm_sector_med, nm_sector_std, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_std.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_distmax_252d_base_v146_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_peer_industry_dist
def f054ntm_f054_net_margin_nm_peer_industry_dist_distmax_504d_base_v147_signal(netinc, revenue, nm_industry_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_industry_med) / nm_industry_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_distmax_252d_base_v148_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_peer_mcap_bucket_dist
def f054ntm_f054_net_margin_nm_peer_mcap_bucket_dist_distmax_504d_base_v149_signal(netinc, revenue, nm_mcap_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_mcap_med) / nm_mcap_med.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_distmax_252d_base_v150_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_peer_sector_pctile
def f054ntm_f054_net_margin_nm_peer_sector_pctile_distmax_504d_base_v151_signal(nm_sector_pctile, closeadj):
    base = nm_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_distmax_252d_base_v152_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_peer_industry_pctile
def f054ntm_f054_net_margin_nm_peer_industry_pctile_distmax_504d_base_v153_signal(nm_industry_pctile, closeadj):
    base = nm_industry_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_distmed_126d_base_v154_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_distmed_252d_base_v155_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netmargin_calc
def f054ntm_f054_net_margin_netmargin_calc_distmed_504d_base_v156_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netmargin
def f054ntm_f054_net_margin_netmargin_distmed_126d_base_v157_signal(netmargin, closeadj):
    base = netmargin
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netmargin
def f054ntm_f054_net_margin_netmargin_distmed_252d_base_v158_signal(netmargin, closeadj):
    base = netmargin
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netmargin
def f054ntm_f054_net_margin_netmargin_distmed_504d_base_v159_signal(netmargin, closeadj):
    base = netmargin
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_distmed_126d_base_v160_signal(netinc, closeadj):
    base = netinc
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_distmed_252d_base_v161_signal(netinc, closeadj):
    base = netinc
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netinc_lvl
def f054ntm_f054_net_margin_netinc_lvl_distmed_504d_base_v162_signal(netinc, closeadj):
    base = netinc
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_distmed_126d_base_v163_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_distmed_252d_base_v164_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of netinc_yoy
def f054ntm_f054_net_margin_netinc_yoy_distmed_504d_base_v165_signal(netinc, closeadj):
    base = netinc.pct_change(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_distmed_126d_base_v166_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_distmed_252d_base_v167_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of nm_yoy_chg
def f054ntm_f054_net_margin_nm_yoy_chg_distmed_504d_base_v168_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_distmed_126d_base_v169_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_distmed_252d_base_v170_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of nm_vol_252
def f054ntm_f054_net_margin_nm_vol_252_distmed_504d_base_v171_signal(netinc, revenue, closeadj):
    base = _f054_nm(netinc, revenue).rolling(252, min_periods=63).std()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_distmed_126d_base_v172_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_distmed_252d_base_v173_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ni_to_asset
def f054ntm_f054_net_margin_ni_to_asset_distmed_504d_base_v174_signal(netinc, assets, closeadj):
    base = netinc / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of nm_peer_sector_dist
def f054ntm_f054_net_margin_nm_peer_sector_dist_distmed_126d_base_v175_signal(netinc, revenue, nm_sector_med, closeadj):
    base = (_f054_nm(netinc, revenue) - nm_sector_med) / nm_sector_med.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

