import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fic_f52_inventory_cycles_assets_mean_5d_base_v001_signal(assets):
    res = assets.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_mean_5d_base_v001_signal'] = fic_f52_inventory_cycles_assets_mean_5d_base_v001_signal

def fic_f52_inventory_cycles_assets_std_5d_base_v002_signal(assets):
    res = assets.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_std_5d_base_v002_signal'] = fic_f52_inventory_cycles_assets_std_5d_base_v002_signal

def fic_f52_inventory_cycles_assets_pct_chg_5d_base_v003_signal(assets):
    res = assets.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_pct_chg_5d_base_v003_signal'] = fic_f52_inventory_cycles_assets_pct_chg_5d_base_v003_signal

def fic_f52_inventory_cycles_assets_max_ratio_5d_base_v004_signal(assets):
    res = assets / assets.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_max_ratio_5d_base_v004_signal'] = fic_f52_inventory_cycles_assets_max_ratio_5d_base_v004_signal

def fic_f52_inventory_cycles_assets_min_ratio_5d_base_v005_signal(assets):
    res = assets / assets.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_min_ratio_5d_base_v005_signal'] = fic_f52_inventory_cycles_assets_min_ratio_5d_base_v005_signal

def fic_f52_inventory_cycles_assets_revenue_mean_5d_base_v006_signal(assets, revenue):
    res = (assets / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_mean_5d_base_v006_signal'] = fic_f52_inventory_cycles_assets_revenue_mean_5d_base_v006_signal

def fic_f52_inventory_cycles_assets_revenue_std_5d_base_v007_signal(assets, revenue):
    res = (assets / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_std_5d_base_v007_signal'] = fic_f52_inventory_cycles_assets_revenue_std_5d_base_v007_signal

def fic_f52_inventory_cycles_assets_revenue_pct_chg_5d_base_v008_signal(assets, revenue):
    res = (assets / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_pct_chg_5d_base_v008_signal'] = fic_f52_inventory_cycles_assets_revenue_pct_chg_5d_base_v008_signal

def fic_f52_inventory_cycles_assets_revenue_mean_ratio_5d_base_v009_signal(assets, revenue):
    res = (assets / revenue) / (assets / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_mean_ratio_5d_base_v009_signal'] = fic_f52_inventory_cycles_assets_revenue_mean_ratio_5d_base_v009_signal

def fic_f52_inventory_cycles_assets_revenue_max_ratio_5d_base_v010_signal(assets, revenue):
    res = (assets / revenue) / (assets / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_max_ratio_5d_base_v010_signal'] = fic_f52_inventory_cycles_assets_revenue_max_ratio_5d_base_v010_signal

def fic_f52_inventory_cycles_assets_revenue_min_ratio_5d_base_v011_signal(assets, revenue):
    res = (assets / revenue) / (assets / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_min_ratio_5d_base_v011_signal'] = fic_f52_inventory_cycles_assets_revenue_min_ratio_5d_base_v011_signal

def fic_f52_inventory_cycles_assets_revenue_diff_5d_base_v012_signal(assets, revenue):
    res = (assets / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_diff_5d_base_v012_signal'] = fic_f52_inventory_cycles_assets_revenue_diff_5d_base_v012_signal

def fic_f52_inventory_cycles_assets_revenue_skew_5d_base_v013_signal(assets, revenue):
    res = (assets / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_skew_5d_base_v013_signal'] = fic_f52_inventory_cycles_assets_revenue_skew_5d_base_v013_signal

def fic_f52_inventory_cycles_assets_revenue_kurt_5d_base_v014_signal(assets, revenue):
    res = (assets / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_kurt_5d_base_v014_signal'] = fic_f52_inventory_cycles_assets_revenue_kurt_5d_base_v014_signal

def fic_f52_inventory_cycles_assets_revenue_rank_5d_base_v015_signal(assets, revenue):
    res = (assets / revenue).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_revenue_rank_5d_base_v015_signal'] = fic_f52_inventory_cycles_assets_revenue_rank_5d_base_v015_signal

def fic_f52_inventory_cycles_assets_ebitda_mean_5d_base_v016_signal(assets, ebitda):
    res = (assets / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_mean_5d_base_v016_signal'] = fic_f52_inventory_cycles_assets_ebitda_mean_5d_base_v016_signal

def fic_f52_inventory_cycles_assets_ebitda_std_5d_base_v017_signal(assets, ebitda):
    res = (assets / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_std_5d_base_v017_signal'] = fic_f52_inventory_cycles_assets_ebitda_std_5d_base_v017_signal

def fic_f52_inventory_cycles_assets_ebitda_pct_chg_5d_base_v018_signal(assets, ebitda):
    res = (assets / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_pct_chg_5d_base_v018_signal'] = fic_f52_inventory_cycles_assets_ebitda_pct_chg_5d_base_v018_signal

def fic_f52_inventory_cycles_assets_ebitda_mean_ratio_5d_base_v019_signal(assets, ebitda):
    res = (assets / ebitda) / (assets / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_mean_ratio_5d_base_v019_signal'] = fic_f52_inventory_cycles_assets_ebitda_mean_ratio_5d_base_v019_signal

def fic_f52_inventory_cycles_assets_ebitda_max_ratio_5d_base_v020_signal(assets, ebitda):
    res = (assets / ebitda) / (assets / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_max_ratio_5d_base_v020_signal'] = fic_f52_inventory_cycles_assets_ebitda_max_ratio_5d_base_v020_signal

def fic_f52_inventory_cycles_assets_ebitda_min_ratio_5d_base_v021_signal(assets, ebitda):
    res = (assets / ebitda) / (assets / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_min_ratio_5d_base_v021_signal'] = fic_f52_inventory_cycles_assets_ebitda_min_ratio_5d_base_v021_signal

def fic_f52_inventory_cycles_assets_ebitda_diff_5d_base_v022_signal(assets, ebitda):
    res = (assets / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_diff_5d_base_v022_signal'] = fic_f52_inventory_cycles_assets_ebitda_diff_5d_base_v022_signal

def fic_f52_inventory_cycles_assets_ebitda_skew_5d_base_v023_signal(assets, ebitda):
    res = (assets / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_skew_5d_base_v023_signal'] = fic_f52_inventory_cycles_assets_ebitda_skew_5d_base_v023_signal

def fic_f52_inventory_cycles_assets_ebitda_kurt_5d_base_v024_signal(assets, ebitda):
    res = (assets / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_kurt_5d_base_v024_signal'] = fic_f52_inventory_cycles_assets_ebitda_kurt_5d_base_v024_signal

def fic_f52_inventory_cycles_assets_ebitda_rank_5d_base_v025_signal(assets, ebitda):
    res = (assets / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ebitda_rank_5d_base_v025_signal'] = fic_f52_inventory_cycles_assets_ebitda_rank_5d_base_v025_signal

def fic_f52_inventory_cycles_assets_ncfo_mean_5d_base_v026_signal(assets, ncfo):
    res = (assets / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_mean_5d_base_v026_signal'] = fic_f52_inventory_cycles_assets_ncfo_mean_5d_base_v026_signal

def fic_f52_inventory_cycles_assets_ncfo_std_5d_base_v027_signal(assets, ncfo):
    res = (assets / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_std_5d_base_v027_signal'] = fic_f52_inventory_cycles_assets_ncfo_std_5d_base_v027_signal

def fic_f52_inventory_cycles_assets_ncfo_pct_chg_5d_base_v028_signal(assets, ncfo):
    res = (assets / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_pct_chg_5d_base_v028_signal'] = fic_f52_inventory_cycles_assets_ncfo_pct_chg_5d_base_v028_signal

def fic_f52_inventory_cycles_assets_ncfo_mean_ratio_5d_base_v029_signal(assets, ncfo):
    res = (assets / ncfo) / (assets / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_mean_ratio_5d_base_v029_signal'] = fic_f52_inventory_cycles_assets_ncfo_mean_ratio_5d_base_v029_signal

def fic_f52_inventory_cycles_assets_ncfo_max_ratio_5d_base_v030_signal(assets, ncfo):
    res = (assets / ncfo) / (assets / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_max_ratio_5d_base_v030_signal'] = fic_f52_inventory_cycles_assets_ncfo_max_ratio_5d_base_v030_signal

def fic_f52_inventory_cycles_assets_ncfo_min_ratio_5d_base_v031_signal(assets, ncfo):
    res = (assets / ncfo) / (assets / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_min_ratio_5d_base_v031_signal'] = fic_f52_inventory_cycles_assets_ncfo_min_ratio_5d_base_v031_signal

def fic_f52_inventory_cycles_assets_ncfo_diff_5d_base_v032_signal(assets, ncfo):
    res = (assets / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_diff_5d_base_v032_signal'] = fic_f52_inventory_cycles_assets_ncfo_diff_5d_base_v032_signal

def fic_f52_inventory_cycles_assets_ncfo_skew_5d_base_v033_signal(assets, ncfo):
    res = (assets / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_skew_5d_base_v033_signal'] = fic_f52_inventory_cycles_assets_ncfo_skew_5d_base_v033_signal

def fic_f52_inventory_cycles_assets_ncfo_kurt_5d_base_v034_signal(assets, ncfo):
    res = (assets / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_kurt_5d_base_v034_signal'] = fic_f52_inventory_cycles_assets_ncfo_kurt_5d_base_v034_signal

def fic_f52_inventory_cycles_assets_ncfo_rank_5d_base_v035_signal(assets, ncfo):
    res = (assets / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_ncfo_rank_5d_base_v035_signal'] = fic_f52_inventory_cycles_assets_ncfo_rank_5d_base_v035_signal

def fic_f52_inventory_cycles_assets_fcf_mean_5d_base_v036_signal(assets, fcf):
    res = (assets / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_mean_5d_base_v036_signal'] = fic_f52_inventory_cycles_assets_fcf_mean_5d_base_v036_signal

def fic_f52_inventory_cycles_assets_fcf_std_5d_base_v037_signal(assets, fcf):
    res = (assets / fcf).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_std_5d_base_v037_signal'] = fic_f52_inventory_cycles_assets_fcf_std_5d_base_v037_signal

def fic_f52_inventory_cycles_assets_fcf_pct_chg_5d_base_v038_signal(assets, fcf):
    res = (assets / fcf).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_pct_chg_5d_base_v038_signal'] = fic_f52_inventory_cycles_assets_fcf_pct_chg_5d_base_v038_signal

def fic_f52_inventory_cycles_assets_fcf_mean_ratio_5d_base_v039_signal(assets, fcf):
    res = (assets / fcf) / (assets / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_mean_ratio_5d_base_v039_signal'] = fic_f52_inventory_cycles_assets_fcf_mean_ratio_5d_base_v039_signal

def fic_f52_inventory_cycles_assets_fcf_max_ratio_5d_base_v040_signal(assets, fcf):
    res = (assets / fcf) / (assets / fcf).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_max_ratio_5d_base_v040_signal'] = fic_f52_inventory_cycles_assets_fcf_max_ratio_5d_base_v040_signal

def fic_f52_inventory_cycles_assets_fcf_min_ratio_5d_base_v041_signal(assets, fcf):
    res = (assets / fcf) / (assets / fcf).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_min_ratio_5d_base_v041_signal'] = fic_f52_inventory_cycles_assets_fcf_min_ratio_5d_base_v041_signal

def fic_f52_inventory_cycles_assets_fcf_diff_5d_base_v042_signal(assets, fcf):
    res = (assets / fcf).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_diff_5d_base_v042_signal'] = fic_f52_inventory_cycles_assets_fcf_diff_5d_base_v042_signal

def fic_f52_inventory_cycles_assets_fcf_skew_5d_base_v043_signal(assets, fcf):
    res = (assets / fcf).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_skew_5d_base_v043_signal'] = fic_f52_inventory_cycles_assets_fcf_skew_5d_base_v043_signal

def fic_f52_inventory_cycles_assets_fcf_kurt_5d_base_v044_signal(assets, fcf):
    res = (assets / fcf).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_kurt_5d_base_v044_signal'] = fic_f52_inventory_cycles_assets_fcf_kurt_5d_base_v044_signal

def fic_f52_inventory_cycles_assets_fcf_rank_5d_base_v045_signal(assets, fcf):
    res = (assets / fcf).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_assets_fcf_rank_5d_base_v045_signal'] = fic_f52_inventory_cycles_assets_fcf_rank_5d_base_v045_signal

def fic_f52_inventory_cycles_revenue_assets_mean_5d_base_v046_signal(revenue, assets):
    res = (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_mean_5d_base_v046_signal'] = fic_f52_inventory_cycles_revenue_assets_mean_5d_base_v046_signal

def fic_f52_inventory_cycles_revenue_assets_std_5d_base_v047_signal(revenue, assets):
    res = (revenue / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_std_5d_base_v047_signal'] = fic_f52_inventory_cycles_revenue_assets_std_5d_base_v047_signal

def fic_f52_inventory_cycles_revenue_assets_pct_chg_5d_base_v048_signal(revenue, assets):
    res = (revenue / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_pct_chg_5d_base_v048_signal'] = fic_f52_inventory_cycles_revenue_assets_pct_chg_5d_base_v048_signal

def fic_f52_inventory_cycles_revenue_assets_mean_ratio_5d_base_v049_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_mean_ratio_5d_base_v049_signal'] = fic_f52_inventory_cycles_revenue_assets_mean_ratio_5d_base_v049_signal

def fic_f52_inventory_cycles_revenue_assets_max_ratio_5d_base_v050_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_max_ratio_5d_base_v050_signal'] = fic_f52_inventory_cycles_revenue_assets_max_ratio_5d_base_v050_signal

def fic_f52_inventory_cycles_revenue_assets_min_ratio_5d_base_v051_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_min_ratio_5d_base_v051_signal'] = fic_f52_inventory_cycles_revenue_assets_min_ratio_5d_base_v051_signal

def fic_f52_inventory_cycles_revenue_assets_diff_5d_base_v052_signal(revenue, assets):
    res = (revenue / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_diff_5d_base_v052_signal'] = fic_f52_inventory_cycles_revenue_assets_diff_5d_base_v052_signal

def fic_f52_inventory_cycles_revenue_assets_skew_5d_base_v053_signal(revenue, assets):
    res = (revenue / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_skew_5d_base_v053_signal'] = fic_f52_inventory_cycles_revenue_assets_skew_5d_base_v053_signal

def fic_f52_inventory_cycles_revenue_assets_kurt_5d_base_v054_signal(revenue, assets):
    res = (revenue / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_kurt_5d_base_v054_signal'] = fic_f52_inventory_cycles_revenue_assets_kurt_5d_base_v054_signal

def fic_f52_inventory_cycles_revenue_assets_rank_5d_base_v055_signal(revenue, assets):
    res = (revenue / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_assets_rank_5d_base_v055_signal'] = fic_f52_inventory_cycles_revenue_assets_rank_5d_base_v055_signal

def fic_f52_inventory_cycles_revenue_mean_5d_base_v056_signal(revenue):
    res = revenue.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_mean_5d_base_v056_signal'] = fic_f52_inventory_cycles_revenue_mean_5d_base_v056_signal

def fic_f52_inventory_cycles_revenue_std_5d_base_v057_signal(revenue):
    res = revenue.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_std_5d_base_v057_signal'] = fic_f52_inventory_cycles_revenue_std_5d_base_v057_signal

def fic_f52_inventory_cycles_revenue_pct_chg_5d_base_v058_signal(revenue):
    res = revenue.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_pct_chg_5d_base_v058_signal'] = fic_f52_inventory_cycles_revenue_pct_chg_5d_base_v058_signal

def fic_f52_inventory_cycles_revenue_max_ratio_5d_base_v059_signal(revenue):
    res = revenue / revenue.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_max_ratio_5d_base_v059_signal'] = fic_f52_inventory_cycles_revenue_max_ratio_5d_base_v059_signal

def fic_f52_inventory_cycles_revenue_min_ratio_5d_base_v060_signal(revenue):
    res = revenue / revenue.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_min_ratio_5d_base_v060_signal'] = fic_f52_inventory_cycles_revenue_min_ratio_5d_base_v060_signal

def fic_f52_inventory_cycles_revenue_ebitda_mean_5d_base_v061_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_mean_5d_base_v061_signal'] = fic_f52_inventory_cycles_revenue_ebitda_mean_5d_base_v061_signal

def fic_f52_inventory_cycles_revenue_ebitda_std_5d_base_v062_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_std_5d_base_v062_signal'] = fic_f52_inventory_cycles_revenue_ebitda_std_5d_base_v062_signal

def fic_f52_inventory_cycles_revenue_ebitda_pct_chg_5d_base_v063_signal(revenue, ebitda):
    res = (revenue / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_pct_chg_5d_base_v063_signal'] = fic_f52_inventory_cycles_revenue_ebitda_pct_chg_5d_base_v063_signal

def fic_f52_inventory_cycles_revenue_ebitda_mean_ratio_5d_base_v064_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_mean_ratio_5d_base_v064_signal'] = fic_f52_inventory_cycles_revenue_ebitda_mean_ratio_5d_base_v064_signal

def fic_f52_inventory_cycles_revenue_ebitda_max_ratio_5d_base_v065_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_max_ratio_5d_base_v065_signal'] = fic_f52_inventory_cycles_revenue_ebitda_max_ratio_5d_base_v065_signal

def fic_f52_inventory_cycles_revenue_ebitda_min_ratio_5d_base_v066_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_min_ratio_5d_base_v066_signal'] = fic_f52_inventory_cycles_revenue_ebitda_min_ratio_5d_base_v066_signal

def fic_f52_inventory_cycles_revenue_ebitda_diff_5d_base_v067_signal(revenue, ebitda):
    res = (revenue / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_diff_5d_base_v067_signal'] = fic_f52_inventory_cycles_revenue_ebitda_diff_5d_base_v067_signal

def fic_f52_inventory_cycles_revenue_ebitda_skew_5d_base_v068_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_skew_5d_base_v068_signal'] = fic_f52_inventory_cycles_revenue_ebitda_skew_5d_base_v068_signal

def fic_f52_inventory_cycles_revenue_ebitda_kurt_5d_base_v069_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_kurt_5d_base_v069_signal'] = fic_f52_inventory_cycles_revenue_ebitda_kurt_5d_base_v069_signal

def fic_f52_inventory_cycles_revenue_ebitda_rank_5d_base_v070_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ebitda_rank_5d_base_v070_signal'] = fic_f52_inventory_cycles_revenue_ebitda_rank_5d_base_v070_signal

def fic_f52_inventory_cycles_revenue_ncfo_mean_5d_base_v071_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_mean_5d_base_v071_signal'] = fic_f52_inventory_cycles_revenue_ncfo_mean_5d_base_v071_signal

def fic_f52_inventory_cycles_revenue_ncfo_std_5d_base_v072_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_std_5d_base_v072_signal'] = fic_f52_inventory_cycles_revenue_ncfo_std_5d_base_v072_signal

def fic_f52_inventory_cycles_revenue_ncfo_pct_chg_5d_base_v073_signal(revenue, ncfo):
    res = (revenue / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_pct_chg_5d_base_v073_signal'] = fic_f52_inventory_cycles_revenue_ncfo_pct_chg_5d_base_v073_signal

def fic_f52_inventory_cycles_revenue_ncfo_mean_ratio_5d_base_v074_signal(revenue, ncfo):
    res = (revenue / ncfo) / (revenue / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_mean_ratio_5d_base_v074_signal'] = fic_f52_inventory_cycles_revenue_ncfo_mean_ratio_5d_base_v074_signal

def fic_f52_inventory_cycles_revenue_ncfo_max_ratio_5d_base_v075_signal(revenue, ncfo):
    res = (revenue / ncfo) / (revenue / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_max_ratio_5d_base_v075_signal'] = fic_f52_inventory_cycles_revenue_ncfo_max_ratio_5d_base_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "capex": np.random.uniform(10, 100, n),
        "revenue": np.random.uniform(10, 100, n),
        "assets": np.random.uniform(10, 100, n),
        "ebitda": np.random.uniform(10, 100, n),
        "equity": np.random.uniform(10, 100, n),
        "debt": np.random.uniform(10, 100, n),
        "closeadj": np.random.uniform(10, 100, n),
        "marketcap": np.random.uniform(10, 100, n),
        "pe": np.random.uniform(10, 100, n),
        "pb": np.random.uniform(10, 100, n),
        "ps": np.random.uniform(10, 100, n),
        "netinc": np.random.uniform(10, 100, n),
        "fcf": np.random.uniform(10, 100, n),
        "sharesbas": np.random.uniform(10, 100, n),
        "ncfo": np.random.uniform(10, 100, n),
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
        assert not res.isna().all(), f"{name} is all NaN"
        assert res.nunique() > 1, f"{name} is constant"
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f"WARNING: High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}")
    print(f"Self-test passed for {os.path.basename(__file__)}")
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
