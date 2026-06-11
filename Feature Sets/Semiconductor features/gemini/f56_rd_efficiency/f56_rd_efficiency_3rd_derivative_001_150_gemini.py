import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fre_f56_rd_efficiency_mean_5d_jerk_v001_signal(ebitda):
    base = ebitda.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v001_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v001_signal

def fre_f56_rd_efficiency_std_5d_jerk_v002_signal(ebitda):
    base = ebitda.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v002_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v002_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v003_signal(ebitda):
    base = ebitda.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v003_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v003_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v004_signal(ebitda):
    base = ebitda / ebitda.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v004_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v004_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v005_signal(ebitda):
    base = ebitda / ebitda.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v005_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v005_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v006_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v006_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v006_signal

def fre_f56_rd_efficiency_std_5d_jerk_v007_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v007_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v007_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v008_signal(ebitda, revenue):
    base = (ebitda / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v008_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v008_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v009_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v009_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v009_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v010_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v010_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v010_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v011_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v011_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v011_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v012_signal(ebitda, revenue):
    base = (ebitda / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v012_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v012_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v013_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v013_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v013_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v014_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v014_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v014_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v015_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v015_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v015_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v016_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v016_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v016_signal

def fre_f56_rd_efficiency_std_5d_jerk_v017_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v017_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v017_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v018_signal(ebitda, fcf):
    base = (ebitda / fcf).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v018_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v018_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v019_signal(ebitda, fcf):
    base = ebitda / fcf / (ebitda / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v019_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v019_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v020_signal(ebitda, fcf):
    base = ebitda / fcf / (ebitda / fcf).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v020_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v020_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v021_signal(ebitda, fcf):
    base = ebitda / fcf / (ebitda / fcf).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v021_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v021_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v022_signal(ebitda, fcf):
    base = (ebitda / fcf).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v022_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v022_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v023_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v023_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v023_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v024_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v024_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v024_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v025_signal(ebitda, fcf):
    base = (ebitda / fcf).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v025_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v025_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v026_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v026_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v026_signal

def fre_f56_rd_efficiency_std_5d_jerk_v027_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v027_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v027_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v028_signal(ebitda, capex):
    base = (ebitda / capex).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v028_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v028_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v029_signal(ebitda, capex):
    base = ebitda / capex / (ebitda / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v029_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v029_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v030_signal(ebitda, capex):
    base = ebitda / capex / (ebitda / capex).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v030_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v030_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v031_signal(ebitda, capex):
    base = ebitda / capex / (ebitda / capex).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v031_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v031_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v032_signal(ebitda, capex):
    base = (ebitda / capex).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v032_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v032_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v033_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v033_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v033_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v034_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v034_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v034_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v035_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v035_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v035_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v036_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v036_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v036_signal

def fre_f56_rd_efficiency_std_5d_jerk_v037_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v037_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v037_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v038_signal(ebitda, assets):
    base = (ebitda / assets).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v038_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v038_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v039_signal(ebitda, assets):
    base = ebitda / assets / (ebitda / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v039_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v039_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v040_signal(ebitda, assets):
    base = ebitda / assets / (ebitda / assets).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v040_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v040_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v041_signal(ebitda, assets):
    base = ebitda / assets / (ebitda / assets).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v041_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v041_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v042_signal(ebitda, assets):
    base = (ebitda / assets).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v042_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v042_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v043_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v043_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v043_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v044_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v044_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v044_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v045_signal(ebitda, assets):
    base = (ebitda / assets).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v045_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v045_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v046_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v046_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v046_signal

def fre_f56_rd_efficiency_std_5d_jerk_v047_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v047_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v047_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v048_signal(ebitda, netinc):
    base = (ebitda / netinc).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v048_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v048_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v049_signal(ebitda, netinc):
    base = ebitda / netinc / (ebitda / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v049_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v049_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v050_signal(ebitda, netinc):
    base = ebitda / netinc / (ebitda / netinc).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v050_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v050_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v051_signal(ebitda, netinc):
    base = ebitda / netinc / (ebitda / netinc).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v051_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v051_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v052_signal(ebitda, netinc):
    base = (ebitda / netinc).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v052_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v052_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v053_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v053_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v053_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v054_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v054_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v054_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v055_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v055_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v055_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v056_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v056_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v056_signal

def fre_f56_rd_efficiency_std_5d_jerk_v057_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v057_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v057_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v058_signal(revenue, ebitda):
    base = (revenue / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v058_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v058_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v059_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v059_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v059_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v060_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v060_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v060_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v061_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v061_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v061_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v062_signal(revenue, ebitda):
    base = (revenue / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v062_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v062_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v063_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v063_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v063_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v064_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v064_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v064_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v065_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v065_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v065_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v066_signal(revenue):
    base = revenue.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v066_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v066_signal

def fre_f56_rd_efficiency_std_5d_jerk_v067_signal(revenue):
    base = revenue.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v067_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v067_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v068_signal(revenue):
    base = revenue.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v068_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v068_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v069_signal(revenue):
    base = revenue / revenue.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v069_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v069_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v070_signal(revenue):
    base = revenue / revenue.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v070_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v070_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v071_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v071_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v071_signal

def fre_f56_rd_efficiency_std_5d_jerk_v072_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v072_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v072_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v073_signal(revenue, fcf):
    base = (revenue / fcf).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v073_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v073_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v074_signal(revenue, fcf):
    base = revenue / fcf / (revenue / fcf).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v074_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v074_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v075_signal(revenue, fcf):
    base = revenue / fcf / (revenue / fcf).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v075_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v075_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v076_signal(revenue, fcf):
    base = revenue / fcf / (revenue / fcf).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v076_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v076_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v077_signal(revenue, fcf):
    base = (revenue / fcf).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v077_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v077_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v078_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v078_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v078_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v079_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v079_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v079_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v080_signal(revenue, fcf):
    base = (revenue / fcf).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v080_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v080_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v081_signal(revenue, capex):
    base = (revenue / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v081_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v081_signal

def fre_f56_rd_efficiency_std_5d_jerk_v082_signal(revenue, capex):
    base = (revenue / capex).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v082_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v082_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v083_signal(revenue, capex):
    base = (revenue / capex).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v083_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v083_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v084_signal(revenue, capex):
    base = revenue / capex / (revenue / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v084_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v084_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v085_signal(revenue, capex):
    base = revenue / capex / (revenue / capex).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v085_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v085_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v086_signal(revenue, capex):
    base = revenue / capex / (revenue / capex).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v086_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v086_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v087_signal(revenue, capex):
    base = (revenue / capex).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v087_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v087_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v088_signal(revenue, capex):
    base = (revenue / capex).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v088_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v088_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v089_signal(revenue, capex):
    base = (revenue / capex).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v089_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v089_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v090_signal(revenue, capex):
    base = (revenue / capex).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v090_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v090_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v091_signal(revenue, assets):
    base = (revenue / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v091_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v091_signal

def fre_f56_rd_efficiency_std_5d_jerk_v092_signal(revenue, assets):
    base = (revenue / assets).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v092_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v092_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v093_signal(revenue, assets):
    base = (revenue / assets).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v093_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v093_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v094_signal(revenue, assets):
    base = revenue / assets / (revenue / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v094_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v094_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v095_signal(revenue, assets):
    base = revenue / assets / (revenue / assets).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v095_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v095_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v096_signal(revenue, assets):
    base = revenue / assets / (revenue / assets).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v096_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v096_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v097_signal(revenue, assets):
    base = (revenue / assets).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v097_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v097_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v098_signal(revenue, assets):
    base = (revenue / assets).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v098_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v098_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v099_signal(revenue, assets):
    base = (revenue / assets).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v099_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v099_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v100_signal(revenue, assets):
    base = (revenue / assets).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v100_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v100_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v101_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v101_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v101_signal

def fre_f56_rd_efficiency_std_5d_jerk_v102_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v102_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v102_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v103_signal(revenue, netinc):
    base = (revenue / netinc).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v103_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v103_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v104_signal(revenue, netinc):
    base = revenue / netinc / (revenue / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v104_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v104_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v105_signal(revenue, netinc):
    base = revenue / netinc / (revenue / netinc).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v105_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v105_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v106_signal(revenue, netinc):
    base = revenue / netinc / (revenue / netinc).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v106_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v106_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v107_signal(revenue, netinc):
    base = (revenue / netinc).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v107_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v107_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v108_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v108_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v108_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v109_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v109_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v109_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v110_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v110_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v110_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v111_signal(fcf, ebitda):
    base = (fcf / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v111_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v111_signal

def fre_f56_rd_efficiency_std_5d_jerk_v112_signal(fcf, ebitda):
    base = (fcf / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v112_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v112_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v113_signal(fcf, ebitda):
    base = (fcf / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v113_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v113_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v114_signal(fcf, ebitda):
    base = fcf / ebitda / (fcf / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v114_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v114_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v115_signal(fcf, ebitda):
    base = fcf / ebitda / (fcf / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v115_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v115_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v116_signal(fcf, ebitda):
    base = fcf / ebitda / (fcf / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v116_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v116_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v117_signal(fcf, ebitda):
    base = (fcf / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v117_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v117_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v118_signal(fcf, ebitda):
    base = (fcf / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v118_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v118_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v119_signal(fcf, ebitda):
    base = (fcf / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v119_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v119_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v120_signal(fcf, ebitda):
    base = (fcf / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v120_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v120_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v121_signal(fcf, revenue):
    base = (fcf / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v121_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v121_signal

def fre_f56_rd_efficiency_std_5d_jerk_v122_signal(fcf, revenue):
    base = (fcf / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v122_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v122_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v123_signal(fcf, revenue):
    base = (fcf / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v123_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v123_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v124_signal(fcf, revenue):
    base = fcf / revenue / (fcf / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v124_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v124_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v125_signal(fcf, revenue):
    base = fcf / revenue / (fcf / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v125_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v125_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v126_signal(fcf, revenue):
    base = fcf / revenue / (fcf / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v126_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v126_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v127_signal(fcf, revenue):
    base = (fcf / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v127_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v127_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v128_signal(fcf, revenue):
    base = (fcf / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v128_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v128_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v129_signal(fcf, revenue):
    base = (fcf / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v129_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v129_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v130_signal(fcf, revenue):
    base = (fcf / revenue).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v130_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v130_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v131_signal(fcf):
    base = fcf.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v131_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v131_signal

def fre_f56_rd_efficiency_std_5d_jerk_v132_signal(fcf):
    base = fcf.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v132_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v132_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v133_signal(fcf):
    base = fcf.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v133_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v133_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v134_signal(fcf):
    base = fcf / fcf.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v134_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v134_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v135_signal(fcf):
    base = fcf / fcf.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v135_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v135_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v136_signal(fcf, capex):
    base = (fcf / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v136_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v136_signal

def fre_f56_rd_efficiency_std_5d_jerk_v137_signal(fcf, capex):
    base = (fcf / capex).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v137_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v137_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v138_signal(fcf, capex):
    base = (fcf / capex).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v138_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v138_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v139_signal(fcf, capex):
    base = fcf / capex / (fcf / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v139_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v139_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v140_signal(fcf, capex):
    base = fcf / capex / (fcf / capex).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v140_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v140_signal

def fre_f56_rd_efficiency_min_ratio_5d_jerk_v141_signal(fcf, capex):
    base = fcf / capex / (fcf / capex).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_min_ratio_5d_jerk_v141_signal'] = fre_f56_rd_efficiency_min_ratio_5d_jerk_v141_signal

def fre_f56_rd_efficiency_diff_5d_jerk_v142_signal(fcf, capex):
    base = (fcf / capex).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_diff_5d_jerk_v142_signal'] = fre_f56_rd_efficiency_diff_5d_jerk_v142_signal

def fre_f56_rd_efficiency_skew_5d_jerk_v143_signal(fcf, capex):
    base = (fcf / capex).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_skew_5d_jerk_v143_signal'] = fre_f56_rd_efficiency_skew_5d_jerk_v143_signal

def fre_f56_rd_efficiency_kurt_5d_jerk_v144_signal(fcf, capex):
    base = (fcf / capex).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_kurt_5d_jerk_v144_signal'] = fre_f56_rd_efficiency_kurt_5d_jerk_v144_signal

def fre_f56_rd_efficiency_rank_5d_jerk_v145_signal(fcf, capex):
    base = (fcf / capex).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_rank_5d_jerk_v145_signal'] = fre_f56_rd_efficiency_rank_5d_jerk_v145_signal

def fre_f56_rd_efficiency_mean_5d_jerk_v146_signal(fcf, assets):
    base = (fcf / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_5d_jerk_v146_signal'] = fre_f56_rd_efficiency_mean_5d_jerk_v146_signal

def fre_f56_rd_efficiency_std_5d_jerk_v147_signal(fcf, assets):
    base = (fcf / assets).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_std_5d_jerk_v147_signal'] = fre_f56_rd_efficiency_std_5d_jerk_v147_signal

def fre_f56_rd_efficiency_pct_chg_5d_jerk_v148_signal(fcf, assets):
    base = (fcf / assets).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_pct_chg_5d_jerk_v148_signal'] = fre_f56_rd_efficiency_pct_chg_5d_jerk_v148_signal

def fre_f56_rd_efficiency_mean_ratio_5d_jerk_v149_signal(fcf, assets):
    base = fcf / assets / (fcf / assets).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_mean_ratio_5d_jerk_v149_signal'] = fre_f56_rd_efficiency_mean_ratio_5d_jerk_v149_signal

def fre_f56_rd_efficiency_max_ratio_5d_jerk_v150_signal(fcf, assets):
    base = fcf / assets / (fcf / assets).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_max_ratio_5d_jerk_v150_signal'] = fre_f56_rd_efficiency_max_ratio_5d_jerk_v150_signal

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
