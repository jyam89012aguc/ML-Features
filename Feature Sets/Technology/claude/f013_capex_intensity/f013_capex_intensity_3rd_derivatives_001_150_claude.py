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


# 21d acceleration of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_accel_21d_3d_v001_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_accel_63d_3d_v002_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_accel_126d_3d_v003_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_accel_252d_3d_v004_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_accel_21d_3d_v005_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_accel_63d_3d_v006_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_accel_126d_3d_v007_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_accel_252d_3d_v008_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_accel_21d_3d_v009_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_accel_63d_3d_v010_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_accel_126d_3d_v011_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_accel_252d_3d_v012_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_accel_21d_3d_v013_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_accel_63d_3d_v014_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_accel_126d_3d_v015_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_accel_252d_3d_v016_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_accel_21d_3d_v017_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_accel_63d_3d_v018_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_accel_126d_3d_v019_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_accel_252d_3d_v020_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_accel_21d_3d_v021_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_accel_63d_3d_v022_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_accel_126d_3d_v023_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_accel_252d_3d_v024_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_accel_21d_3d_v025_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_accel_63d_3d_v026_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_accel_126d_3d_v027_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_accel_252d_3d_v028_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_accel_21d_3d_v029_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_accel_63d_3d_v030_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_accel_126d_3d_v031_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_accel_252d_3d_v032_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_accel_21d_3d_v033_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_accel_63d_3d_v034_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_accel_126d_3d_v035_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_accel_252d_3d_v036_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_accel_21d_3d_v037_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_accel_63d_3d_v038_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_accel_126d_3d_v039_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_accel_252d_3d_v040_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_accel_21d_3d_v041_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_accel_63d_3d_v042_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_accel_126d_3d_v043_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_accel_252d_3d_v044_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_accel_21d_3d_v045_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_accel_63d_3d_v046_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_accel_126d_3d_v047_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_accel_252d_3d_v048_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_accel_21d_3d_v049_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_accel_63d_3d_v050_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_accel_126d_3d_v051_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_accel_252d_3d_v052_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_accel_21d_3d_v053_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_accel_63d_3d_v054_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_accel_126d_3d_v055_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_accel_252d_3d_v056_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slopez_21d_z126_3d_v057_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slopez_63d_z252_3d_v058_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slopez_126d_z252_3d_v059_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_slopez_252d_z504_3d_v060_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slopez_21d_z126_3d_v061_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slopez_63d_z252_3d_v062_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slopez_126d_z252_3d_v063_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_slopez_252d_z504_3d_v064_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slopez_21d_z126_3d_v065_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slopez_63d_z252_3d_v066_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slopez_126d_z252_3d_v067_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_slopez_252d_z504_3d_v068_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slopez_21d_z126_3d_v069_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slopez_63d_z252_3d_v070_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slopez_126d_z252_3d_v071_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_slopez_252d_z504_3d_v072_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slopez_21d_z126_3d_v073_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slopez_63d_z252_3d_v074_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slopez_126d_z252_3d_v075_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_slopez_252d_z504_3d_v076_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slopez_21d_z126_3d_v077_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slopez_63d_z252_3d_v078_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slopez_126d_z252_3d_v079_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_slopez_252d_z504_3d_v080_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slopez_21d_z126_3d_v081_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slopez_63d_z252_3d_v082_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slopez_126d_z252_3d_v083_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_slopez_252d_z504_3d_v084_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slopez_21d_z126_3d_v085_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slopez_63d_z252_3d_v086_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slopez_126d_z252_3d_v087_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_slopez_252d_z504_3d_v088_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slopez_21d_z126_3d_v089_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slopez_63d_z252_3d_v090_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slopez_126d_z252_3d_v091_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_slopez_252d_z504_3d_v092_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slopez_21d_z126_3d_v093_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slopez_63d_z252_3d_v094_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slopez_126d_z252_3d_v095_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_slopez_252d_z504_3d_v096_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slopez_21d_z126_3d_v097_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slopez_63d_z252_3d_v098_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slopez_126d_z252_3d_v099_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_slopez_252d_z504_3d_v100_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slopez_21d_z126_3d_v101_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slopez_63d_z252_3d_v102_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slopez_126d_z252_3d_v103_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_slopez_252d_z504_3d_v104_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slopez_21d_z126_3d_v105_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slopez_63d_z252_3d_v106_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slopez_126d_z252_3d_v107_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_slopez_252d_z504_3d_v108_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slopez_21d_z126_3d_v109_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slopez_63d_z252_3d_v110_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slopez_126d_z252_3d_v111_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_slopez_252d_z504_3d_v112_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_jerk_21d_3d_v113_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_jerk_63d_3d_v114_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_jerk_126d_3d_v115_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_jerk_21d_3d_v116_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_jerk_63d_3d_v117_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_jerk_126d_3d_v118_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_jerk_21d_3d_v119_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_jerk_63d_3d_v120_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_jerk_126d_3d_v121_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_jerk_21d_3d_v122_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_jerk_63d_3d_v123_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_jerk_126d_3d_v124_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_jerk_21d_3d_v125_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_jerk_63d_3d_v126_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_jerk_126d_3d_v127_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_jerk_21d_3d_v128_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_jerk_63d_3d_v129_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_jerk_126d_3d_v130_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_jerk_21d_3d_v131_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_jerk_63d_3d_v132_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_jerk_126d_3d_v133_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_jerk_21d_3d_v134_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_jerk_63d_3d_v135_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_jerk_126d_3d_v136_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_jerk_21d_3d_v137_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_jerk_63d_3d_v138_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_jerk_126d_3d_v139_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_jerk_21d_3d_v140_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_jerk_63d_3d_v141_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_jerk_126d_3d_v142_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_jerk_21d_3d_v143_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_jerk_63d_3d_v144_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capint_peer_industry_dist
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_jerk_126d_3d_v145_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_jerk_21d_3d_v146_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_jerk_63d_3d_v147_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capint_peer_mcap_bucket_dist
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_jerk_126d_3d_v148_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_jerk_21d_3d_v149_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_jerk_63d_3d_v150_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capint_peer_sector_pctile
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_jerk_126d_3d_v151_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_jerk_21d_3d_v152_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_jerk_63d_3d_v153_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of capint_peer_industry_pctile
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_jerk_126d_3d_v154_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_lvl smoothed over 252d
def f013cxi_f013_capex_intensity_capex_lvl_smoothaccel_63d_sm252_3d_v155_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_lvl smoothed over 504d
def f013cxi_f013_capex_intensity_capex_lvl_smoothaccel_252d_sm504_3d_v156_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_rev smoothed over 252d
def f013cxi_f013_capex_intensity_capex_to_rev_smoothaccel_63d_sm252_3d_v157_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_rev smoothed over 504d
def f013cxi_f013_capex_intensity_capex_to_rev_smoothaccel_252d_sm504_3d_v158_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_asset smoothed over 252d
def f013cxi_f013_capex_intensity_capex_to_asset_smoothaccel_63d_sm252_3d_v159_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_asset smoothed over 504d
def f013cxi_f013_capex_intensity_capex_to_asset_smoothaccel_252d_sm504_3d_v160_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_ocf smoothed over 252d
def f013cxi_f013_capex_intensity_capex_to_ocf_smoothaccel_63d_sm252_3d_v161_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_ocf smoothed over 504d
def f013cxi_f013_capex_intensity_capex_to_ocf_smoothaccel_252d_sm504_3d_v162_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_mcap smoothed over 252d
def f013cxi_f013_capex_intensity_capex_to_mcap_smoothaccel_63d_sm252_3d_v163_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_mcap smoothed over 504d
def f013cxi_f013_capex_intensity_capex_to_mcap_smoothaccel_252d_sm504_3d_v164_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_ppne smoothed over 252d
def f013cxi_f013_capex_intensity_capex_to_ppne_smoothaccel_63d_sm252_3d_v165_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_ppne smoothed over 504d
def f013cxi_f013_capex_intensity_capex_to_ppne_smoothaccel_252d_sm504_3d_v166_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ppne_to_asset smoothed over 252d
def f013cxi_f013_capex_intensity_ppne_to_asset_smoothaccel_63d_sm252_3d_v167_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ppne_to_asset smoothed over 504d
def f013cxi_f013_capex_intensity_ppne_to_asset_smoothaccel_252d_sm504_3d_v168_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capex_to_dep smoothed over 252d
def f013cxi_f013_capex_intensity_capex_to_dep_smoothaccel_63d_sm252_3d_v169_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capex_to_dep smoothed over 504d
def f013cxi_f013_capex_intensity_capex_to_dep_smoothaccel_252d_sm504_3d_v170_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capint_peer_sector_dist smoothed over 252d
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_smoothaccel_63d_sm252_3d_v171_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capint_peer_sector_dist smoothed over 504d
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_smoothaccel_252d_sm504_3d_v172_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capint_peer_sector_z smoothed over 252d
def f013cxi_f013_capex_intensity_capint_peer_sector_z_smoothaccel_63d_sm252_3d_v173_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capint_peer_sector_z smoothed over 504d
def f013cxi_f013_capex_intensity_capint_peer_sector_z_smoothaccel_252d_sm504_3d_v174_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capint_peer_industry_dist smoothed over 252d
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_smoothaccel_63d_sm252_3d_v175_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capint_peer_industry_dist smoothed over 504d
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_smoothaccel_252d_sm504_3d_v176_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capint_peer_mcap_bucket_dist smoothed over 252d
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_smoothaccel_63d_sm252_3d_v177_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capint_peer_mcap_bucket_dist smoothed over 504d
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_smoothaccel_252d_sm504_3d_v178_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capint_peer_sector_pctile smoothed over 252d
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_smoothaccel_63d_sm252_3d_v179_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capint_peer_sector_pctile smoothed over 504d
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_smoothaccel_252d_sm504_3d_v180_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of capint_peer_industry_pctile smoothed over 252d
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_smoothaccel_63d_sm252_3d_v181_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of capint_peer_industry_pctile smoothed over 504d
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_smoothaccel_252d_sm504_3d_v182_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_accelz_21d_z252_3d_v183_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_accelz_63d_z504_3d_v184_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_accelz_21d_z252_3d_v185_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_accelz_63d_z504_3d_v186_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_accelz_21d_z252_3d_v187_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_accelz_63d_z504_3d_v188_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_accelz_21d_z252_3d_v189_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_accelz_63d_z504_3d_v190_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_accelz_21d_z252_3d_v191_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_accelz_63d_z504_3d_v192_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_accelz_21d_z252_3d_v193_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_accelz_63d_z504_3d_v194_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_accelz_21d_z252_3d_v195_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_accelz_63d_z504_3d_v196_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_accelz_21d_z252_3d_v197_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_accelz_63d_z504_3d_v198_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_accelz_21d_z252_3d_v199_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_accelz_63d_z504_3d_v200_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

