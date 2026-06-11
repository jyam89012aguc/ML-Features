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
def _f013_capex_abs(capex):
    return capex.abs()


def _f013_capex_to_rev(capex, revenue):
    return capex.abs() / revenue.abs().replace(0, np.nan)


def _f013_capex_to_ocf(capex, ncfo):
    return capex.abs() / ncfo.abs().replace(0, np.nan)


# 21d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slope_21d_2d_v001_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slope_63d_2d_v002_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slope_126d_2d_v003_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slope_252d_2d_v004_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slope_504d_2d_v005_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slope_21d_2d_v006_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slope_63d_2d_v007_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slope_126d_2d_v008_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slope_252d_2d_v009_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slope_504d_2d_v010_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slope_21d_2d_v011_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slope_63d_2d_v012_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slope_126d_2d_v013_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slope_252d_2d_v014_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slope_504d_2d_v015_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slope_21d_2d_v016_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slope_63d_2d_v017_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slope_126d_2d_v018_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slope_252d_2d_v019_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slope_504d_2d_v020_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slope_21d_2d_v021_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slope_63d_2d_v022_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slope_126d_2d_v023_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slope_252d_2d_v024_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slope_504d_2d_v025_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slope_21d_2d_v026_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slope_63d_2d_v027_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slope_126d_2d_v028_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slope_252d_2d_v029_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slope_504d_2d_v030_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slope_21d_2d_v031_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slope_63d_2d_v032_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slope_126d_2d_v033_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slope_252d_2d_v034_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slope_504d_2d_v035_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slope_21d_2d_v036_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slope_63d_2d_v037_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slope_126d_2d_v038_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slope_252d_2d_v039_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slope_504d_2d_v040_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slope_21d_2d_v041_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slope_63d_2d_v042_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slope_126d_2d_v043_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slope_252d_2d_v044_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slope_504d_2d_v045_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slope_21d_2d_v046_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slope_63d_2d_v047_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slope_126d_2d_v048_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slope_252d_2d_v049_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slope_504d_2d_v050_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slope_21d_2d_v051_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slope_63d_2d_v052_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slope_126d_2d_v053_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slope_252d_2d_v054_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slope_504d_2d_v055_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slope_21d_2d_v056_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slope_63d_2d_v057_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slope_126d_2d_v058_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slope_252d_2d_v059_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slope_504d_2d_v060_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slope_21d_2d_v061_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slope_63d_2d_v062_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slope_126d_2d_v063_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slope_252d_2d_v064_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slope_504d_2d_v065_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slope_21d_2d_v066_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slope_63d_2d_v067_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slope_126d_2d_v068_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slope_252d_2d_v069_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slope_504d_2d_v070_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sm21_sl21_2d_v071_signal(capex, closeadj):
    base = _mean(_f013_capex_abs(capex), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sm63_sl21_2d_v072_signal(capex, closeadj):
    base = _mean(_f013_capex_abs(capex), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sm63_sl63_2d_v073_signal(capex, closeadj):
    base = _mean(_f013_capex_abs(capex), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sm252_sl63_2d_v074_signal(capex, closeadj):
    base = _mean(_f013_capex_abs(capex), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sm252_sl126_2d_v075_signal(capex, closeadj):
    base = _mean(_f013_capex_abs(capex), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sm21_sl21_2d_v076_signal(capex, revenue, closeadj):
    base = _mean(_f013_capex_to_rev(capex, revenue), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sm63_sl21_2d_v077_signal(capex, revenue, closeadj):
    base = _mean(_f013_capex_to_rev(capex, revenue), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sm63_sl63_2d_v078_signal(capex, revenue, closeadj):
    base = _mean(_f013_capex_to_rev(capex, revenue), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sm252_sl63_2d_v079_signal(capex, revenue, closeadj):
    base = _mean(_f013_capex_to_rev(capex, revenue), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sm252_sl126_2d_v080_signal(capex, revenue, closeadj):
    base = _mean(_f013_capex_to_rev(capex, revenue), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sm21_sl21_2d_v081_signal(capex, assets, closeadj):
    base = _mean(_f013_capex_abs(capex) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sm63_sl21_2d_v082_signal(capex, assets, closeadj):
    base = _mean(_f013_capex_abs(capex) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sm63_sl63_2d_v083_signal(capex, assets, closeadj):
    base = _mean(_f013_capex_abs(capex) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sm252_sl63_2d_v084_signal(capex, assets, closeadj):
    base = _mean(_f013_capex_abs(capex) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sm252_sl126_2d_v085_signal(capex, assets, closeadj):
    base = _mean(_f013_capex_abs(capex) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sm21_sl21_2d_v086_signal(capex, ncfo, closeadj):
    base = _mean(_f013_capex_to_ocf(capex, ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sm63_sl21_2d_v087_signal(capex, ncfo, closeadj):
    base = _mean(_f013_capex_to_ocf(capex, ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sm63_sl63_2d_v088_signal(capex, ncfo, closeadj):
    base = _mean(_f013_capex_to_ocf(capex, ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sm252_sl63_2d_v089_signal(capex, ncfo, closeadj):
    base = _mean(_f013_capex_to_ocf(capex, ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sm252_sl126_2d_v090_signal(capex, ncfo, closeadj):
    base = _mean(_f013_capex_to_ocf(capex, ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sm21_sl21_2d_v091_signal(capex, marketcap, closeadj):
    base = _mean(_f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sm63_sl21_2d_v092_signal(capex, marketcap, closeadj):
    base = _mean(_f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sm63_sl63_2d_v093_signal(capex, marketcap, closeadj):
    base = _mean(_f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sm252_sl63_2d_v094_signal(capex, marketcap, closeadj):
    base = _mean(_f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sm252_sl126_2d_v095_signal(capex, marketcap, closeadj):
    base = _mean(_f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sm21_sl21_2d_v096_signal(capex, ppnenet, closeadj):
    base = _mean(_f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sm63_sl21_2d_v097_signal(capex, ppnenet, closeadj):
    base = _mean(_f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sm63_sl63_2d_v098_signal(capex, ppnenet, closeadj):
    base = _mean(_f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sm252_sl63_2d_v099_signal(capex, ppnenet, closeadj):
    base = _mean(_f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sm252_sl126_2d_v100_signal(capex, ppnenet, closeadj):
    base = _mean(_f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_sm21_sl21_2d_v101_signal(ppnenet, assets, closeadj):
    base = _mean(ppnenet / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_sm63_sl21_2d_v102_signal(ppnenet, assets, closeadj):
    base = _mean(ppnenet / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_sm63_sl63_2d_v103_signal(ppnenet, assets, closeadj):
    base = _mean(ppnenet / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_sm252_sl63_2d_v104_signal(ppnenet, assets, closeadj):
    base = _mean(ppnenet / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_sm252_sl126_2d_v105_signal(ppnenet, assets, closeadj):
    base = _mean(ppnenet / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_sm21_sl21_2d_v106_signal(capex, depamor, closeadj):
    base = _mean(_f013_capex_abs(capex) / depamor.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_sm63_sl21_2d_v107_signal(capex, depamor, closeadj):
    base = _mean(_f013_capex_abs(capex) / depamor.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_sm63_sl63_2d_v108_signal(capex, depamor, closeadj):
    base = _mean(_f013_capex_abs(capex) / depamor.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_sm252_sl63_2d_v109_signal(capex, depamor, closeadj):
    base = _mean(_f013_capex_abs(capex) / depamor.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_sm252_sl126_2d_v110_signal(capex, depamor, closeadj):
    base = _mean(_f013_capex_abs(capex) / depamor.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_sm21_sl21_2d_v111_signal(capex, revenue, capint_sector_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_sm63_sl21_2d_v112_signal(capex, revenue, capint_sector_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_sm63_sl63_2d_v113_signal(capex, revenue, capint_sector_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_sm252_sl63_2d_v114_signal(capex, revenue, capint_sector_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_sm252_sl126_2d_v115_signal(capex, revenue, capint_sector_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_sm21_sl21_2d_v116_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_sm63_sl21_2d_v117_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_sm63_sl63_2d_v118_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_sm252_sl63_2d_v119_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_sm252_sl126_2d_v120_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_sm21_sl21_2d_v121_signal(capex, revenue, capint_industry_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_sm63_sl21_2d_v122_signal(capex, revenue, capint_industry_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_sm63_sl63_2d_v123_signal(capex, revenue, capint_industry_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_sm252_sl63_2d_v124_signal(capex, revenue, capint_industry_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_sm252_sl126_2d_v125_signal(capex, revenue, capint_industry_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_sm21_sl21_2d_v126_signal(capex, revenue, capint_mcap_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_sm63_sl21_2d_v127_signal(capex, revenue, capint_mcap_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_sm63_sl63_2d_v128_signal(capex, revenue, capint_mcap_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_sm252_sl63_2d_v129_signal(capex, revenue, capint_mcap_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_sm252_sl126_2d_v130_signal(capex, revenue, capint_mcap_med, closeadj):
    base = _mean((_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_sm21_sl21_2d_v131_signal(capint_sector_pctile, closeadj):
    base = _mean(capint_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_sm63_sl21_2d_v132_signal(capint_sector_pctile, closeadj):
    base = _mean(capint_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_sm63_sl63_2d_v133_signal(capint_sector_pctile, closeadj):
    base = _mean(capint_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_sm252_sl63_2d_v134_signal(capint_sector_pctile, closeadj):
    base = _mean(capint_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_sm252_sl126_2d_v135_signal(capint_sector_pctile, closeadj):
    base = _mean(capint_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_sm21_sl21_2d_v136_signal(capint_industry_pctile, closeadj):
    base = _mean(capint_industry_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_sm63_sl21_2d_v137_signal(capint_industry_pctile, closeadj):
    base = _mean(capint_industry_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_sm63_sl63_2d_v138_signal(capint_industry_pctile, closeadj):
    base = _mean(capint_industry_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_sm252_sl63_2d_v139_signal(capint_industry_pctile, closeadj):
    base = _mean(capint_industry_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_sm252_sl126_2d_v140_signal(capint_industry_pctile, closeadj):
    base = _mean(capint_industry_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_pctslope_21d_2d_v141_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_pctslope_63d_2d_v142_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_pctslope_252d_2d_v143_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_pctslope_21d_2d_v144_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_pctslope_63d_2d_v145_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_pctslope_252d_2d_v146_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_pctslope_21d_2d_v147_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_pctslope_63d_2d_v148_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_pctslope_252d_2d_v149_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_pctslope_21d_2d_v150_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_pctslope_63d_2d_v151_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_pctslope_252d_2d_v152_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_pctslope_21d_2d_v153_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_pctslope_63d_2d_v154_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_pctslope_252d_2d_v155_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_pctslope_21d_2d_v156_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_pctslope_63d_2d_v157_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_pctslope_252d_2d_v158_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_pctslope_21d_2d_v159_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_pctslope_63d_2d_v160_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_pctslope_252d_2d_v161_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_pctslope_21d_2d_v162_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_pctslope_63d_2d_v163_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_pctslope_252d_2d_v164_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_pctslope_21d_2d_v165_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_pctslope_63d_2d_v166_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_pctslope_252d_2d_v167_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_pctslope_21d_2d_v168_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_pctslope_63d_2d_v169_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_pctslope_252d_2d_v170_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_pctslope_21d_2d_v171_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_pctslope_63d_2d_v172_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_pctslope_252d_2d_v173_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_pctslope_21d_2d_v174_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_pctslope_63d_2d_v175_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_pctslope_252d_2d_v176_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_pctslope_21d_2d_v177_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_pctslope_63d_2d_v178_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_pctslope_252d_2d_v179_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_pctslope_21d_2d_v180_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_pctslope_63d_2d_v181_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_pctslope_252d_2d_v182_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sgnslope_21d_2d_v183_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sgnslope_63d_2d_v184_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_sgnslope_252d_2d_v185_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sgnslope_21d_2d_v186_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sgnslope_63d_2d_v187_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_sgnslope_252d_2d_v188_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sgnslope_21d_2d_v189_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sgnslope_63d_2d_v190_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_sgnslope_252d_2d_v191_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sgnslope_21d_2d_v192_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sgnslope_63d_2d_v193_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_sgnslope_252d_2d_v194_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sgnslope_21d_2d_v195_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sgnslope_63d_2d_v196_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_sgnslope_252d_2d_v197_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sgnslope_21d_2d_v198_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sgnslope_63d_2d_v199_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_sgnslope_252d_2d_v200_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

