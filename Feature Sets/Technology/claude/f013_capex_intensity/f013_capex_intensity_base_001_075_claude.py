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
def _f013_capex_abs(capex):
    return capex.abs()


def _f013_capex_to_rev(capex, revenue):
    return capex.abs() / revenue.abs().replace(0, np.nan)


def _f013_capex_to_ocf(capex, ncfo):
    return capex.abs() / ncfo.abs().replace(0, np.nan)


# 21d mean of capex_lvl scaled by closeadj
def f013cxi_f013_capex_intensity_capex_lvl_mean_21d_base_v001_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_lvl scaled by closeadj
def f013cxi_f013_capex_intensity_capex_lvl_mean_63d_base_v002_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_lvl scaled by closeadj
def f013cxi_f013_capex_intensity_capex_lvl_mean_126d_base_v003_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_lvl scaled by closeadj
def f013cxi_f013_capex_intensity_capex_lvl_mean_252d_base_v004_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_lvl scaled by closeadj
def f013cxi_f013_capex_intensity_capex_lvl_mean_504d_base_v005_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_rev scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_rev_mean_21d_base_v006_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_rev scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_rev_mean_63d_base_v007_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_rev scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_rev_mean_126d_base_v008_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_rev scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_rev_mean_252d_base_v009_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_rev scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_rev_mean_504d_base_v010_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_asset_mean_21d_base_v011_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_asset_mean_63d_base_v012_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_asset_mean_126d_base_v013_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_asset_mean_252d_base_v014_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_asset_mean_504d_base_v015_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_ocf scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ocf_mean_21d_base_v016_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_ocf scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ocf_mean_63d_base_v017_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_ocf scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ocf_mean_126d_base_v018_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_ocf scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ocf_mean_252d_base_v019_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_ocf scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ocf_mean_504d_base_v020_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_mcap scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_mcap_mean_21d_base_v021_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_mcap scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_mcap_mean_63d_base_v022_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_mcap scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_mcap_mean_126d_base_v023_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_mcap scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_mcap_mean_252d_base_v024_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_mcap scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_mcap_mean_504d_base_v025_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_ppne scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ppne_mean_21d_base_v026_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_ppne scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ppne_mean_63d_base_v027_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_ppne scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ppne_mean_126d_base_v028_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_ppne scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ppne_mean_252d_base_v029_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_ppne scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_ppne_mean_504d_base_v030_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ppne_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_ppne_to_asset_mean_21d_base_v031_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ppne_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_ppne_to_asset_mean_63d_base_v032_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ppne_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_ppne_to_asset_mean_126d_base_v033_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ppne_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_ppne_to_asset_mean_252d_base_v034_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ppne_to_asset scaled by closeadj
def f013cxi_f013_capex_intensity_ppne_to_asset_mean_504d_base_v035_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capex_to_dep scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_dep_mean_21d_base_v036_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capex_to_dep scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_dep_mean_63d_base_v037_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capex_to_dep scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_dep_mean_126d_base_v038_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capex_to_dep scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_dep_mean_252d_base_v039_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capex_to_dep scaled by closeadj
def f013cxi_f013_capex_intensity_capex_to_dep_mean_504d_base_v040_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capint_peer_sector_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_mean_21d_base_v041_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capint_peer_sector_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_mean_63d_base_v042_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capint_peer_sector_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_mean_126d_base_v043_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capint_peer_sector_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_mean_252d_base_v044_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capint_peer_sector_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_mean_504d_base_v045_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capint_peer_sector_z scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_z_mean_21d_base_v046_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capint_peer_sector_z scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_z_mean_63d_base_v047_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capint_peer_sector_z scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_z_mean_126d_base_v048_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capint_peer_sector_z scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_z_mean_252d_base_v049_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capint_peer_sector_z scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_z_mean_504d_base_v050_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capint_peer_industry_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_mean_21d_base_v051_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capint_peer_industry_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_mean_63d_base_v052_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capint_peer_industry_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_mean_126d_base_v053_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capint_peer_industry_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_mean_252d_base_v054_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capint_peer_industry_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_dist_mean_504d_base_v055_signal(capex, revenue, capint_industry_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_industry_med) / capint_industry_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capint_peer_mcap_bucket_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_mean_21d_base_v056_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capint_peer_mcap_bucket_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_mean_63d_base_v057_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capint_peer_mcap_bucket_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_mean_126d_base_v058_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capint_peer_mcap_bucket_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_mean_252d_base_v059_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capint_peer_mcap_bucket_dist scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_mcap_bucket_dist_mean_504d_base_v060_signal(capex, revenue, capint_mcap_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_mcap_med) / capint_mcap_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capint_peer_sector_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_mean_21d_base_v061_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capint_peer_sector_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_mean_63d_base_v062_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capint_peer_sector_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_mean_126d_base_v063_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capint_peer_sector_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_mean_252d_base_v064_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capint_peer_sector_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_sector_pctile_mean_504d_base_v065_signal(capint_sector_pctile, closeadj):
    base = capint_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of capint_peer_industry_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_mean_21d_base_v066_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of capint_peer_industry_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_mean_63d_base_v067_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of capint_peer_industry_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_mean_126d_base_v068_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of capint_peer_industry_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_mean_252d_base_v069_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of capint_peer_industry_pctile scaled by closeadj
def f013cxi_f013_capex_intensity_capint_peer_industry_pctile_mean_504d_base_v070_signal(capint_industry_pctile, closeadj):
    base = capint_industry_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_median_63d_base_v071_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_median_252d_base_v072_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_lvl
def f013cxi_f013_capex_intensity_capex_lvl_median_504d_base_v073_signal(capex, closeadj):
    base = _f013_capex_abs(capex)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_median_63d_base_v074_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_median_252d_base_v075_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_rev
def f013cxi_f013_capex_intensity_capex_to_rev_median_504d_base_v076_signal(capex, revenue, closeadj):
    base = _f013_capex_to_rev(capex, revenue)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_median_63d_base_v077_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_median_252d_base_v078_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_asset
def f013cxi_f013_capex_intensity_capex_to_asset_median_504d_base_v079_signal(capex, assets, closeadj):
    base = _f013_capex_abs(capex) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_median_63d_base_v080_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_median_252d_base_v081_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_ocf
def f013cxi_f013_capex_intensity_capex_to_ocf_median_504d_base_v082_signal(capex, ncfo, closeadj):
    base = _f013_capex_to_ocf(capex, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_median_63d_base_v083_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_median_252d_base_v084_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_mcap
def f013cxi_f013_capex_intensity_capex_to_mcap_median_504d_base_v085_signal(capex, marketcap, closeadj):
    base = _f013_capex_abs(capex) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_median_63d_base_v086_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_median_252d_base_v087_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_ppne
def f013cxi_f013_capex_intensity_capex_to_ppne_median_504d_base_v088_signal(capex, ppnenet, closeadj):
    base = _f013_capex_abs(capex) / ppnenet.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_median_63d_base_v089_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_median_252d_base_v090_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ppne_to_asset
def f013cxi_f013_capex_intensity_ppne_to_asset_median_504d_base_v091_signal(ppnenet, assets, closeadj):
    base = ppnenet / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_median_63d_base_v092_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_median_252d_base_v093_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capex_to_dep
def f013cxi_f013_capex_intensity_capex_to_dep_median_504d_base_v094_signal(capex, depamor, closeadj):
    base = _f013_capex_abs(capex) / depamor.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_median_63d_base_v095_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_median_252d_base_v096_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capint_peer_sector_dist
def f013cxi_f013_capex_intensity_capint_peer_sector_dist_median_504d_base_v097_signal(capex, revenue, capint_sector_med, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_med.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_median_63d_base_v098_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_median_252d_base_v099_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of capint_peer_sector_z
def f013cxi_f013_capex_intensity_capint_peer_sector_z_median_504d_base_v100_signal(capex, revenue, capint_sector_med, capint_sector_std, closeadj):
    base = (_f013_capex_to_rev(capex, revenue) - capint_sector_med) / capint_sector_std.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

