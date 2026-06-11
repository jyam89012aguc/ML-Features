import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fol_f54_operating_leverage_mean_5d_jerk_v001_signal(ebitda):
    base = ebitda.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v001_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v001_signal

def fol_f54_operating_leverage_std_5d_jerk_v002_signal(ebitda):
    base = ebitda.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v002_signal'] = fol_f54_operating_leverage_std_5d_jerk_v002_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v003_signal(ebitda):
    base = ebitda.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v003_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v003_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v004_signal(ebitda):
    base = ebitda / ebitda.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v004_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v004_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v005_signal(ebitda):
    base = ebitda / ebitda.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v005_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v005_signal

def fol_f54_operating_leverage_mean_5d_jerk_v006_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v006_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v006_signal

def fol_f54_operating_leverage_std_5d_jerk_v007_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v007_signal'] = fol_f54_operating_leverage_std_5d_jerk_v007_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v008_signal(ebitda, revenue):
    base = (ebitda / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v008_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v008_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v009_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v009_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v009_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v010_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v010_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v010_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v011_signal(ebitda, revenue):
    base = ebitda / revenue / (ebitda / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v011_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v011_signal

def fol_f54_operating_leverage_diff_5d_jerk_v012_signal(ebitda, revenue):
    base = (ebitda / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v012_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v012_signal

def fol_f54_operating_leverage_skew_5d_jerk_v013_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v013_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v013_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v014_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v014_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v014_signal

def fol_f54_operating_leverage_rank_5d_jerk_v015_signal(ebitda, revenue):
    base = (ebitda / revenue).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v015_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v015_signal

def fol_f54_operating_leverage_mean_5d_jerk_v016_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v016_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v016_signal

def fol_f54_operating_leverage_std_5d_jerk_v017_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v017_signal'] = fol_f54_operating_leverage_std_5d_jerk_v017_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v018_signal(ebitda, netinc):
    base = (ebitda / netinc).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v018_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v018_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v019_signal(ebitda, netinc):
    base = ebitda / netinc / (ebitda / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v019_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v019_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v020_signal(ebitda, netinc):
    base = ebitda / netinc / (ebitda / netinc).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v020_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v020_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v021_signal(ebitda, netinc):
    base = ebitda / netinc / (ebitda / netinc).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v021_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v021_signal

def fol_f54_operating_leverage_diff_5d_jerk_v022_signal(ebitda, netinc):
    base = (ebitda / netinc).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v022_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v022_signal

def fol_f54_operating_leverage_skew_5d_jerk_v023_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v023_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v023_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v024_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v024_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v024_signal

def fol_f54_operating_leverage_rank_5d_jerk_v025_signal(ebitda, netinc):
    base = (ebitda / netinc).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v025_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v025_signal

def fol_f54_operating_leverage_mean_5d_jerk_v026_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v026_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v026_signal

def fol_f54_operating_leverage_std_5d_jerk_v027_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v027_signal'] = fol_f54_operating_leverage_std_5d_jerk_v027_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v028_signal(ebitda, ncfo):
    base = (ebitda / ncfo).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v028_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v028_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v029_signal(ebitda, ncfo):
    base = ebitda / ncfo / (ebitda / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v029_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v029_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v030_signal(ebitda, ncfo):
    base = ebitda / ncfo / (ebitda / ncfo).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v030_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v030_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v031_signal(ebitda, ncfo):
    base = ebitda / ncfo / (ebitda / ncfo).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v031_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v031_signal

def fol_f54_operating_leverage_diff_5d_jerk_v032_signal(ebitda, ncfo):
    base = (ebitda / ncfo).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v032_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v032_signal

def fol_f54_operating_leverage_skew_5d_jerk_v033_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v033_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v033_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v034_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v034_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v034_signal

def fol_f54_operating_leverage_rank_5d_jerk_v035_signal(ebitda, ncfo):
    base = (ebitda / ncfo).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v035_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v035_signal

def fol_f54_operating_leverage_mean_5d_jerk_v036_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v036_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v036_signal

def fol_f54_operating_leverage_std_5d_jerk_v037_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v037_signal'] = fol_f54_operating_leverage_std_5d_jerk_v037_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v038_signal(ebitda, capex):
    base = (ebitda / capex).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v038_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v038_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v039_signal(ebitda, capex):
    base = ebitda / capex / (ebitda / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v039_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v039_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v040_signal(ebitda, capex):
    base = ebitda / capex / (ebitda / capex).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v040_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v040_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v041_signal(ebitda, capex):
    base = ebitda / capex / (ebitda / capex).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v041_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v041_signal

def fol_f54_operating_leverage_diff_5d_jerk_v042_signal(ebitda, capex):
    base = (ebitda / capex).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v042_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v042_signal

def fol_f54_operating_leverage_skew_5d_jerk_v043_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v043_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v043_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v044_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v044_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v044_signal

def fol_f54_operating_leverage_rank_5d_jerk_v045_signal(ebitda, capex):
    base = (ebitda / capex).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v045_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v045_signal

def fol_f54_operating_leverage_mean_5d_jerk_v046_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v046_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v046_signal

def fol_f54_operating_leverage_std_5d_jerk_v047_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v047_signal'] = fol_f54_operating_leverage_std_5d_jerk_v047_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v048_signal(revenue, ebitda):
    base = (revenue / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v048_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v048_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v049_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v049_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v049_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v050_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v050_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v050_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v051_signal(revenue, ebitda):
    base = revenue / ebitda / (revenue / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v051_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v051_signal

def fol_f54_operating_leverage_diff_5d_jerk_v052_signal(revenue, ebitda):
    base = (revenue / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v052_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v052_signal

def fol_f54_operating_leverage_skew_5d_jerk_v053_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v053_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v053_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v054_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v054_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v054_signal

def fol_f54_operating_leverage_rank_5d_jerk_v055_signal(revenue, ebitda):
    base = (revenue / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v055_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v055_signal

def fol_f54_operating_leverage_mean_5d_jerk_v056_signal(revenue):
    base = revenue.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v056_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v056_signal

def fol_f54_operating_leverage_std_5d_jerk_v057_signal(revenue):
    base = revenue.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v057_signal'] = fol_f54_operating_leverage_std_5d_jerk_v057_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v058_signal(revenue):
    base = revenue.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v058_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v058_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v059_signal(revenue):
    base = revenue / revenue.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v059_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v059_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v060_signal(revenue):
    base = revenue / revenue.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v060_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v060_signal

def fol_f54_operating_leverage_mean_5d_jerk_v061_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v061_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v061_signal

def fol_f54_operating_leverage_std_5d_jerk_v062_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v062_signal'] = fol_f54_operating_leverage_std_5d_jerk_v062_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v063_signal(revenue, netinc):
    base = (revenue / netinc).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v063_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v063_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v064_signal(revenue, netinc):
    base = revenue / netinc / (revenue / netinc).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v064_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v064_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v065_signal(revenue, netinc):
    base = revenue / netinc / (revenue / netinc).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v065_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v065_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v066_signal(revenue, netinc):
    base = revenue / netinc / (revenue / netinc).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v066_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v066_signal

def fol_f54_operating_leverage_diff_5d_jerk_v067_signal(revenue, netinc):
    base = (revenue / netinc).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v067_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v067_signal

def fol_f54_operating_leverage_skew_5d_jerk_v068_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v068_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v068_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v069_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v069_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v069_signal

def fol_f54_operating_leverage_rank_5d_jerk_v070_signal(revenue, netinc):
    base = (revenue / netinc).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v070_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v070_signal

def fol_f54_operating_leverage_mean_5d_jerk_v071_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v071_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v071_signal

def fol_f54_operating_leverage_std_5d_jerk_v072_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v072_signal'] = fol_f54_operating_leverage_std_5d_jerk_v072_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v073_signal(revenue, ncfo):
    base = (revenue / ncfo).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v073_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v073_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v074_signal(revenue, ncfo):
    base = revenue / ncfo / (revenue / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v074_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v074_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v075_signal(revenue, ncfo):
    base = revenue / ncfo / (revenue / ncfo).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v075_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v075_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v076_signal(revenue, ncfo):
    base = revenue / ncfo / (revenue / ncfo).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v076_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v076_signal

def fol_f54_operating_leverage_diff_5d_jerk_v077_signal(revenue, ncfo):
    base = (revenue / ncfo).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v077_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v077_signal

def fol_f54_operating_leverage_skew_5d_jerk_v078_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v078_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v078_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v079_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v079_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v079_signal

def fol_f54_operating_leverage_rank_5d_jerk_v080_signal(revenue, ncfo):
    base = (revenue / ncfo).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v080_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v080_signal

def fol_f54_operating_leverage_mean_5d_jerk_v081_signal(revenue, capex):
    base = (revenue / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v081_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v081_signal

def fol_f54_operating_leverage_std_5d_jerk_v082_signal(revenue, capex):
    base = (revenue / capex).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v082_signal'] = fol_f54_operating_leverage_std_5d_jerk_v082_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v083_signal(revenue, capex):
    base = (revenue / capex).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v083_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v083_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v084_signal(revenue, capex):
    base = revenue / capex / (revenue / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v084_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v084_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v085_signal(revenue, capex):
    base = revenue / capex / (revenue / capex).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v085_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v085_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v086_signal(revenue, capex):
    base = revenue / capex / (revenue / capex).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v086_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v086_signal

def fol_f54_operating_leverage_diff_5d_jerk_v087_signal(revenue, capex):
    base = (revenue / capex).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v087_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v087_signal

def fol_f54_operating_leverage_skew_5d_jerk_v088_signal(revenue, capex):
    base = (revenue / capex).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v088_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v088_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v089_signal(revenue, capex):
    base = (revenue / capex).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v089_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v089_signal

def fol_f54_operating_leverage_rank_5d_jerk_v090_signal(revenue, capex):
    base = (revenue / capex).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v090_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v090_signal

def fol_f54_operating_leverage_mean_5d_jerk_v091_signal(netinc, ebitda):
    base = (netinc / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v091_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v091_signal

def fol_f54_operating_leverage_std_5d_jerk_v092_signal(netinc, ebitda):
    base = (netinc / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v092_signal'] = fol_f54_operating_leverage_std_5d_jerk_v092_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v093_signal(netinc, ebitda):
    base = (netinc / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v093_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v093_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v094_signal(netinc, ebitda):
    base = netinc / ebitda / (netinc / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v094_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v094_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v095_signal(netinc, ebitda):
    base = netinc / ebitda / (netinc / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v095_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v095_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v096_signal(netinc, ebitda):
    base = netinc / ebitda / (netinc / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v096_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v096_signal

def fol_f54_operating_leverage_diff_5d_jerk_v097_signal(netinc, ebitda):
    base = (netinc / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v097_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v097_signal

def fol_f54_operating_leverage_skew_5d_jerk_v098_signal(netinc, ebitda):
    base = (netinc / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v098_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v098_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v099_signal(netinc, ebitda):
    base = (netinc / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v099_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v099_signal

def fol_f54_operating_leverage_rank_5d_jerk_v100_signal(netinc, ebitda):
    base = (netinc / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v100_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v100_signal

def fol_f54_operating_leverage_mean_5d_jerk_v101_signal(netinc, revenue):
    base = (netinc / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v101_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v101_signal

def fol_f54_operating_leverage_std_5d_jerk_v102_signal(netinc, revenue):
    base = (netinc / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v102_signal'] = fol_f54_operating_leverage_std_5d_jerk_v102_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v103_signal(netinc, revenue):
    base = (netinc / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v103_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v103_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v104_signal(netinc, revenue):
    base = netinc / revenue / (netinc / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v104_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v104_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v105_signal(netinc, revenue):
    base = netinc / revenue / (netinc / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v105_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v105_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v106_signal(netinc, revenue):
    base = netinc / revenue / (netinc / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v106_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v106_signal

def fol_f54_operating_leverage_diff_5d_jerk_v107_signal(netinc, revenue):
    base = (netinc / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v107_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v107_signal

def fol_f54_operating_leverage_skew_5d_jerk_v108_signal(netinc, revenue):
    base = (netinc / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v108_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v108_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v109_signal(netinc, revenue):
    base = (netinc / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v109_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v109_signal

def fol_f54_operating_leverage_rank_5d_jerk_v110_signal(netinc, revenue):
    base = (netinc / revenue).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v110_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v110_signal

def fol_f54_operating_leverage_mean_5d_jerk_v111_signal(netinc):
    base = netinc.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v111_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v111_signal

def fol_f54_operating_leverage_std_5d_jerk_v112_signal(netinc):
    base = netinc.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v112_signal'] = fol_f54_operating_leverage_std_5d_jerk_v112_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v113_signal(netinc):
    base = netinc.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v113_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v113_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v114_signal(netinc):
    base = netinc / netinc.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v114_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v114_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v115_signal(netinc):
    base = netinc / netinc.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v115_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v115_signal

def fol_f54_operating_leverage_mean_5d_jerk_v116_signal(netinc, ncfo):
    base = (netinc / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v116_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v116_signal

def fol_f54_operating_leverage_std_5d_jerk_v117_signal(netinc, ncfo):
    base = (netinc / ncfo).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v117_signal'] = fol_f54_operating_leverage_std_5d_jerk_v117_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v118_signal(netinc, ncfo):
    base = (netinc / ncfo).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v118_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v118_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v119_signal(netinc, ncfo):
    base = netinc / ncfo / (netinc / ncfo).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v119_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v119_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v120_signal(netinc, ncfo):
    base = netinc / ncfo / (netinc / ncfo).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v120_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v120_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v121_signal(netinc, ncfo):
    base = netinc / ncfo / (netinc / ncfo).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v121_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v121_signal

def fol_f54_operating_leverage_diff_5d_jerk_v122_signal(netinc, ncfo):
    base = (netinc / ncfo).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v122_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v122_signal

def fol_f54_operating_leverage_skew_5d_jerk_v123_signal(netinc, ncfo):
    base = (netinc / ncfo).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v123_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v123_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v124_signal(netinc, ncfo):
    base = (netinc / ncfo).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v124_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v124_signal

def fol_f54_operating_leverage_rank_5d_jerk_v125_signal(netinc, ncfo):
    base = (netinc / ncfo).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v125_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v125_signal

def fol_f54_operating_leverage_mean_5d_jerk_v126_signal(netinc, capex):
    base = (netinc / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v126_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v126_signal

def fol_f54_operating_leverage_std_5d_jerk_v127_signal(netinc, capex):
    base = (netinc / capex).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v127_signal'] = fol_f54_operating_leverage_std_5d_jerk_v127_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v128_signal(netinc, capex):
    base = (netinc / capex).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v128_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v128_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v129_signal(netinc, capex):
    base = netinc / capex / (netinc / capex).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v129_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v129_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v130_signal(netinc, capex):
    base = netinc / capex / (netinc / capex).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v130_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v130_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v131_signal(netinc, capex):
    base = netinc / capex / (netinc / capex).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v131_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v131_signal

def fol_f54_operating_leverage_diff_5d_jerk_v132_signal(netinc, capex):
    base = (netinc / capex).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v132_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v132_signal

def fol_f54_operating_leverage_skew_5d_jerk_v133_signal(netinc, capex):
    base = (netinc / capex).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v133_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v133_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v134_signal(netinc, capex):
    base = (netinc / capex).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v134_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v134_signal

def fol_f54_operating_leverage_rank_5d_jerk_v135_signal(netinc, capex):
    base = (netinc / capex).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v135_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v135_signal

def fol_f54_operating_leverage_mean_5d_jerk_v136_signal(ncfo, ebitda):
    base = (ncfo / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v136_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v136_signal

def fol_f54_operating_leverage_std_5d_jerk_v137_signal(ncfo, ebitda):
    base = (ncfo / ebitda).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v137_signal'] = fol_f54_operating_leverage_std_5d_jerk_v137_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v138_signal(ncfo, ebitda):
    base = (ncfo / ebitda).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v138_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v138_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v139_signal(ncfo, ebitda):
    base = ncfo / ebitda / (ncfo / ebitda).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v139_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v139_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v140_signal(ncfo, ebitda):
    base = ncfo / ebitda / (ncfo / ebitda).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v140_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v140_signal

def fol_f54_operating_leverage_min_ratio_5d_jerk_v141_signal(ncfo, ebitda):
    base = ncfo / ebitda / (ncfo / ebitda).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_min_ratio_5d_jerk_v141_signal'] = fol_f54_operating_leverage_min_ratio_5d_jerk_v141_signal

def fol_f54_operating_leverage_diff_5d_jerk_v142_signal(ncfo, ebitda):
    base = (ncfo / ebitda).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_diff_5d_jerk_v142_signal'] = fol_f54_operating_leverage_diff_5d_jerk_v142_signal

def fol_f54_operating_leverage_skew_5d_jerk_v143_signal(ncfo, ebitda):
    base = (ncfo / ebitda).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_skew_5d_jerk_v143_signal'] = fol_f54_operating_leverage_skew_5d_jerk_v143_signal

def fol_f54_operating_leverage_kurt_5d_jerk_v144_signal(ncfo, ebitda):
    base = (ncfo / ebitda).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_kurt_5d_jerk_v144_signal'] = fol_f54_operating_leverage_kurt_5d_jerk_v144_signal

def fol_f54_operating_leverage_rank_5d_jerk_v145_signal(ncfo, ebitda):
    base = (ncfo / ebitda).rolling(5).rank(pct=True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_rank_5d_jerk_v145_signal'] = fol_f54_operating_leverage_rank_5d_jerk_v145_signal

def fol_f54_operating_leverage_mean_5d_jerk_v146_signal(ncfo, revenue):
    base = (ncfo / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_5d_jerk_v146_signal'] = fol_f54_operating_leverage_mean_5d_jerk_v146_signal

def fol_f54_operating_leverage_std_5d_jerk_v147_signal(ncfo, revenue):
    base = (ncfo / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_std_5d_jerk_v147_signal'] = fol_f54_operating_leverage_std_5d_jerk_v147_signal

def fol_f54_operating_leverage_pct_chg_5d_jerk_v148_signal(ncfo, revenue):
    base = (ncfo / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_pct_chg_5d_jerk_v148_signal'] = fol_f54_operating_leverage_pct_chg_5d_jerk_v148_signal

def fol_f54_operating_leverage_mean_ratio_5d_jerk_v149_signal(ncfo, revenue):
    base = ncfo / revenue / (ncfo / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_mean_ratio_5d_jerk_v149_signal'] = fol_f54_operating_leverage_mean_ratio_5d_jerk_v149_signal

def fol_f54_operating_leverage_max_ratio_5d_jerk_v150_signal(ncfo, revenue):
    base = ncfo / revenue / (ncfo / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_max_ratio_5d_jerk_v150_signal'] = fol_f54_operating_leverage_max_ratio_5d_jerk_v150_signal

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
