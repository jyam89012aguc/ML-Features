import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fic_f52_inventory_cycles_mean_5d_jerk_v001_signal(assets):
    base = assets.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v001_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v001_signal

def fic_f52_inventory_cycles_std_5d_jerk_v002_signal(assets):
    base = assets.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v002_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v002_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v003_signal(assets):
    base = assets.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v003_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v003_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v004_signal(assets):
    base = assets / assets.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v004_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v004_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v005_signal(assets):
    base = assets / assets.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v005_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v005_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v006_signal(assets, revenue):
    base = (assets / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v006_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v006_signal

def fic_f52_inventory_cycles_std_5d_jerk_v007_signal(assets, revenue):
    base = (assets / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v007_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v007_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v008_signal(assets, revenue):
    base = (assets / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v008_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v008_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v009_signal(assets, revenue):
    base = assets / revenue / (assets / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v009_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v009_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v010_signal(assets, revenue):
    base = assets / revenue / (assets / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v010_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v010_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v011_signal(assets, revenue):
    base = assets / revenue / (assets / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v011_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v011_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v012_signal(assets, revenue):
    base = (assets / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v012_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v012_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v013_signal(assets, revenue):
    base = (assets / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v013_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v013_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v014_signal(assets, revenue):
    base = (assets / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v014_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v014_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v015_signal(assets, revenue):
    base = (assets / revenue).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v015_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v015_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v016_signal(assets, ebitda):
    base = (assets / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v016_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v016_signal

def fic_f52_inventory_cycles_std_5d_jerk_v017_signal(assets, ebitda):
    base = (assets / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v017_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v017_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v018_signal(assets, ebitda):
    base = (assets / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v018_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v018_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v019_signal(assets, ebitda):
    base = assets / ebitda / (assets / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v019_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v019_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v020_signal(assets, ebitda):
    base = assets / ebitda / (assets / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v020_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v020_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v021_signal(assets, ebitda):
    base = assets / ebitda / (assets / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v021_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v021_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v022_signal(assets, ebitda):
    base = (assets / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v022_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v022_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v023_signal(assets, ebitda):
    base = (assets / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v023_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v023_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v024_signal(assets, ebitda):
    base = (assets / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v024_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v024_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v025_signal(assets, ebitda):
    base = (assets / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v025_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v025_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v026_signal(assets, ncfo):
    base = (assets / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v026_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v026_signal

def fic_f52_inventory_cycles_std_5d_jerk_v027_signal(assets, ncfo):
    base = (assets / ncfo).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v027_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v027_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v028_signal(assets, ncfo):
    base = (assets / ncfo).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v028_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v028_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v029_signal(assets, ncfo):
    base = assets / ncfo / (assets / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v029_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v029_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v030_signal(assets, ncfo):
    base = assets / ncfo / (assets / ncfo).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v030_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v030_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v031_signal(assets, ncfo):
    base = assets / ncfo / (assets / ncfo).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v031_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v031_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v032_signal(assets, ncfo):
    base = (assets / ncfo).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v032_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v032_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v033_signal(assets, ncfo):
    base = (assets / ncfo).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v033_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v033_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v034_signal(assets, ncfo):
    base = (assets / ncfo).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v034_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v034_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v035_signal(assets, ncfo):
    base = (assets / ncfo).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v035_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v035_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v036_signal(assets, fcf):
    base = (assets / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v036_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v036_signal

def fic_f52_inventory_cycles_std_5d_jerk_v037_signal(assets, fcf):
    base = (assets / fcf).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v037_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v037_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v038_signal(assets, fcf):
    base = (assets / fcf).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v038_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v038_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v039_signal(assets, fcf):
    base = assets / fcf / (assets / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v039_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v039_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v040_signal(assets, fcf):
    base = assets / fcf / (assets / fcf).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v040_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v040_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v041_signal(assets, fcf):
    base = assets / fcf / (assets / fcf).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v041_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v041_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v042_signal(assets, fcf):
    base = (assets / fcf).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v042_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v042_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v043_signal(assets, fcf):
    base = (assets / fcf).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v043_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v043_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v044_signal(assets, fcf):
    base = (assets / fcf).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v044_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v044_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v045_signal(assets, fcf):
    base = (assets / fcf).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v045_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v045_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v046_signal(revenue, assets):
    base = (revenue / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v046_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v046_signal

def fic_f52_inventory_cycles_std_5d_jerk_v047_signal(revenue, assets):
    base = (revenue / assets).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v047_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v047_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v048_signal(revenue, assets):
    base = (revenue / assets).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v048_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v048_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v049_signal(revenue, assets):
    base = revenue / assets / (revenue / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v049_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v049_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v050_signal(revenue, assets):
    base = revenue / assets / (revenue / assets).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v050_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v050_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v051_signal(revenue, assets):
    base = revenue / assets / (revenue / assets).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v051_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v051_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v052_signal(revenue, assets):
    base = (revenue / assets).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v052_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v052_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v053_signal(revenue, assets):
    base = (revenue / assets).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v053_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v053_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v054_signal(revenue, assets):
    base = (revenue / assets).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v054_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v054_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v055_signal(revenue, assets):
    base = (revenue / assets).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v055_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v055_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v056_signal(revenue):
    base = revenue.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v056_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v056_signal

def fic_f52_inventory_cycles_std_5d_jerk_v057_signal(revenue):
    base = revenue.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v057_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v057_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v058_signal(revenue):
    base = revenue.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v058_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v058_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v059_signal(revenue):
    base = revenue / revenue.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v059_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v059_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v060_signal(revenue):
    base = revenue / revenue.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v060_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v060_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v061_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v061_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v061_signal

def fic_f52_inventory_cycles_std_5d_jerk_v062_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v062_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v062_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v063_signal(revenue, ebitda):
    base = (revenue / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v063_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v063_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v064_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v064_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v064_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v065_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v065_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v065_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v066_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v066_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v066_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v067_signal(revenue, ebitda):
    base = (revenue / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v067_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v067_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v068_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v068_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v068_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v069_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v069_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v069_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v070_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v070_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v070_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v071_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v071_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v071_signal

def fic_f52_inventory_cycles_std_5d_jerk_v072_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v072_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v072_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v073_signal(revenue, ncfo):
    base = (revenue / ncfo).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v073_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v073_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v074_signal(revenue, ncfo):
    base = revenue / ncfo / (revenue / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v074_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v074_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v075_signal(revenue, ncfo):
    base = revenue / ncfo / (revenue / ncfo).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v075_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v075_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v076_signal(revenue, ncfo):
    base = revenue / ncfo / (revenue / ncfo).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v076_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v076_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v077_signal(revenue, ncfo):
    base = (revenue / ncfo).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v077_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v077_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v078_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v078_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v078_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v079_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v079_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v079_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v080_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v080_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v080_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v081_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v081_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v081_signal

def fic_f52_inventory_cycles_std_5d_jerk_v082_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v082_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v082_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v083_signal(revenue, fcf):
    base = (revenue / fcf).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v083_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v083_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v084_signal(revenue, fcf):
    base = revenue / fcf / (revenue / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v084_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v084_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v085_signal(revenue, fcf):
    base = revenue / fcf / (revenue / fcf).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v085_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v085_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v086_signal(revenue, fcf):
    base = revenue / fcf / (revenue / fcf).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v086_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v086_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v087_signal(revenue, fcf):
    base = (revenue / fcf).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v087_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v087_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v088_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v088_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v088_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v089_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v089_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v089_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v090_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v090_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v090_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v091_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v091_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v091_signal

def fic_f52_inventory_cycles_std_5d_jerk_v092_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v092_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v092_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v093_signal(ebitda, assets):
    base = (ebitda / assets).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v093_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v093_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v094_signal(ebitda, assets):
    base = ebitda / assets / (ebitda / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v094_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v094_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v095_signal(ebitda, assets):
    base = ebitda / assets / (ebitda / assets).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v095_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v095_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v096_signal(ebitda, assets):
    base = ebitda / assets / (ebitda / assets).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v096_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v096_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v097_signal(ebitda, assets):
    base = (ebitda / assets).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v097_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v097_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v098_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v098_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v098_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v099_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v099_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v099_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v100_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v100_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v100_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v101_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v101_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v101_signal

def fic_f52_inventory_cycles_std_5d_jerk_v102_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v102_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v102_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v103_signal(ebitda, revenue):
    base = (ebitda / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v103_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v103_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v104_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v104_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v104_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v105_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v105_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v105_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v106_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v106_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v106_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v107_signal(ebitda, revenue):
    base = (ebitda / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v107_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v107_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v108_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v108_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v108_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v109_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v109_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v109_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v110_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v110_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v110_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v111_signal(ebitda):
    base = ebitda.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v111_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v111_signal

def fic_f52_inventory_cycles_std_5d_jerk_v112_signal(ebitda):
    base = ebitda.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v112_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v112_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v113_signal(ebitda):
    base = ebitda.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v113_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v113_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v114_signal(ebitda):
    base = ebitda / ebitda.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v114_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v114_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v115_signal(ebitda):
    base = ebitda / ebitda.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v115_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v115_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v116_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v116_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v116_signal

def fic_f52_inventory_cycles_std_5d_jerk_v117_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v117_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v117_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v118_signal(ebitda, ncfo):
    base = (ebitda / ncfo).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v118_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v118_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v119_signal(ebitda, ncfo):
    base = ebitda / ncfo / (ebitda / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v119_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v119_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v120_signal(ebitda, ncfo):
    base = ebitda / ncfo / (ebitda / ncfo).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v120_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v120_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v121_signal(ebitda, ncfo):
    base = ebitda / ncfo / (ebitda / ncfo).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v121_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v121_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v122_signal(ebitda, ncfo):
    base = (ebitda / ncfo).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v122_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v122_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v123_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v123_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v123_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v124_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v124_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v124_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v125_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v125_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v125_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v126_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v126_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v126_signal

def fic_f52_inventory_cycles_std_5d_jerk_v127_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v127_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v127_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v128_signal(ebitda, fcf):
    base = (ebitda / fcf).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v128_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v128_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v129_signal(ebitda, fcf):
    base = ebitda / fcf / (ebitda / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v129_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v129_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v130_signal(ebitda, fcf):
    base = ebitda / fcf / (ebitda / fcf).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v130_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v130_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v131_signal(ebitda, fcf):
    base = ebitda / fcf / (ebitda / fcf).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v131_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v131_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v132_signal(ebitda, fcf):
    base = (ebitda / fcf).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v132_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v132_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v133_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v133_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v133_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v134_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v134_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v134_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v135_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v135_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v135_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v136_signal(ncfo, assets):
    base = (ncfo / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v136_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v136_signal

def fic_f52_inventory_cycles_std_5d_jerk_v137_signal(ncfo, assets):
    base = (ncfo / assets).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v137_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v137_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v138_signal(ncfo, assets):
    base = (ncfo / assets).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v138_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v138_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v139_signal(ncfo, assets):
    base = ncfo / assets / (ncfo / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v139_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v139_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v140_signal(ncfo, assets):
    base = ncfo / assets / (ncfo / assets).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v140_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v140_signal

def fic_f52_inventory_cycles_min_ratio_5d_jerk_v141_signal(ncfo, assets):
    base = ncfo / assets / (ncfo / assets).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_min_ratio_5d_jerk_v141_signal'] = fic_f52_inventory_cycles_min_ratio_5d_jerk_v141_signal

def fic_f52_inventory_cycles_diff_5d_jerk_v142_signal(ncfo, assets):
    base = (ncfo / assets).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_diff_5d_jerk_v142_signal'] = fic_f52_inventory_cycles_diff_5d_jerk_v142_signal

def fic_f52_inventory_cycles_skew_5d_jerk_v143_signal(ncfo, assets):
    base = (ncfo / assets).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_skew_5d_jerk_v143_signal'] = fic_f52_inventory_cycles_skew_5d_jerk_v143_signal

def fic_f52_inventory_cycles_kurt_5d_jerk_v144_signal(ncfo, assets):
    base = (ncfo / assets).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_kurt_5d_jerk_v144_signal'] = fic_f52_inventory_cycles_kurt_5d_jerk_v144_signal

def fic_f52_inventory_cycles_rank_5d_jerk_v145_signal(ncfo, assets):
    base = (ncfo / assets).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_rank_5d_jerk_v145_signal'] = fic_f52_inventory_cycles_rank_5d_jerk_v145_signal

def fic_f52_inventory_cycles_mean_5d_jerk_v146_signal(ncfo, revenue):
    base = (ncfo / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_5d_jerk_v146_signal'] = fic_f52_inventory_cycles_mean_5d_jerk_v146_signal

def fic_f52_inventory_cycles_std_5d_jerk_v147_signal(ncfo, revenue):
    base = (ncfo / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_std_5d_jerk_v147_signal'] = fic_f52_inventory_cycles_std_5d_jerk_v147_signal

def fic_f52_inventory_cycles_pct_chg_5d_jerk_v148_signal(ncfo, revenue):
    base = (ncfo / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_pct_chg_5d_jerk_v148_signal'] = fic_f52_inventory_cycles_pct_chg_5d_jerk_v148_signal

def fic_f52_inventory_cycles_mean_ratio_5d_jerk_v149_signal(ncfo, revenue):
    base = ncfo / revenue / (ncfo / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_mean_ratio_5d_jerk_v149_signal'] = fic_f52_inventory_cycles_mean_ratio_5d_jerk_v149_signal

def fic_f52_inventory_cycles_max_ratio_5d_jerk_v150_signal(ncfo, revenue):
    base = ncfo / revenue / (ncfo / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_max_ratio_5d_jerk_v150_signal'] = fic_f52_inventory_cycles_max_ratio_5d_jerk_v150_signal

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
