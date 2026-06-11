import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fol_f54_operating_leverage_ebitda_mean_5d_base_v001_signal(ebitda):
    res = ebitda.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_mean_5d_base_v001_signal'] = fol_f54_operating_leverage_ebitda_mean_5d_base_v001_signal

def fol_f54_operating_leverage_ebitda_std_5d_base_v002_signal(ebitda):
    res = ebitda.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_std_5d_base_v002_signal'] = fol_f54_operating_leverage_ebitda_std_5d_base_v002_signal

def fol_f54_operating_leverage_ebitda_pct_chg_5d_base_v003_signal(ebitda):
    res = ebitda.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_pct_chg_5d_base_v003_signal'] = fol_f54_operating_leverage_ebitda_pct_chg_5d_base_v003_signal

def fol_f54_operating_leverage_ebitda_max_ratio_5d_base_v004_signal(ebitda):
    res = ebitda / ebitda.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_max_ratio_5d_base_v004_signal'] = fol_f54_operating_leverage_ebitda_max_ratio_5d_base_v004_signal

def fol_f54_operating_leverage_ebitda_min_ratio_5d_base_v005_signal(ebitda):
    res = ebitda / ebitda.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_min_ratio_5d_base_v005_signal'] = fol_f54_operating_leverage_ebitda_min_ratio_5d_base_v005_signal

def fol_f54_operating_leverage_ebitda_revenue_mean_5d_base_v006_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_mean_5d_base_v006_signal'] = fol_f54_operating_leverage_ebitda_revenue_mean_5d_base_v006_signal

def fol_f54_operating_leverage_ebitda_revenue_std_5d_base_v007_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_std_5d_base_v007_signal'] = fol_f54_operating_leverage_ebitda_revenue_std_5d_base_v007_signal

def fol_f54_operating_leverage_ebitda_revenue_pct_chg_5d_base_v008_signal(ebitda, revenue):
    res = (ebitda / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_pct_chg_5d_base_v008_signal'] = fol_f54_operating_leverage_ebitda_revenue_pct_chg_5d_base_v008_signal

def fol_f54_operating_leverage_ebitda_revenue_mean_ratio_5d_base_v009_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_mean_ratio_5d_base_v009_signal'] = fol_f54_operating_leverage_ebitda_revenue_mean_ratio_5d_base_v009_signal

def fol_f54_operating_leverage_ebitda_revenue_max_ratio_5d_base_v010_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_max_ratio_5d_base_v010_signal'] = fol_f54_operating_leverage_ebitda_revenue_max_ratio_5d_base_v010_signal

def fol_f54_operating_leverage_ebitda_revenue_min_ratio_5d_base_v011_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_min_ratio_5d_base_v011_signal'] = fol_f54_operating_leverage_ebitda_revenue_min_ratio_5d_base_v011_signal

def fol_f54_operating_leverage_ebitda_revenue_diff_5d_base_v012_signal(ebitda, revenue):
    res = (ebitda / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_diff_5d_base_v012_signal'] = fol_f54_operating_leverage_ebitda_revenue_diff_5d_base_v012_signal

def fol_f54_operating_leverage_ebitda_revenue_skew_5d_base_v013_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_skew_5d_base_v013_signal'] = fol_f54_operating_leverage_ebitda_revenue_skew_5d_base_v013_signal

def fol_f54_operating_leverage_ebitda_revenue_kurt_5d_base_v014_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_kurt_5d_base_v014_signal'] = fol_f54_operating_leverage_ebitda_revenue_kurt_5d_base_v014_signal

def fol_f54_operating_leverage_ebitda_revenue_rank_5d_base_v015_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_revenue_rank_5d_base_v015_signal'] = fol_f54_operating_leverage_ebitda_revenue_rank_5d_base_v015_signal

def fol_f54_operating_leverage_ebitda_netinc_mean_5d_base_v016_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_mean_5d_base_v016_signal'] = fol_f54_operating_leverage_ebitda_netinc_mean_5d_base_v016_signal

def fol_f54_operating_leverage_ebitda_netinc_std_5d_base_v017_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_std_5d_base_v017_signal'] = fol_f54_operating_leverage_ebitda_netinc_std_5d_base_v017_signal

def fol_f54_operating_leverage_ebitda_netinc_pct_chg_5d_base_v018_signal(ebitda, netinc):
    res = (ebitda / netinc).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_pct_chg_5d_base_v018_signal'] = fol_f54_operating_leverage_ebitda_netinc_pct_chg_5d_base_v018_signal

def fol_f54_operating_leverage_ebitda_netinc_mean_ratio_5d_base_v019_signal(ebitda, netinc):
    res = (ebitda / netinc) / (ebitda / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_mean_ratio_5d_base_v019_signal'] = fol_f54_operating_leverage_ebitda_netinc_mean_ratio_5d_base_v019_signal

def fol_f54_operating_leverage_ebitda_netinc_max_ratio_5d_base_v020_signal(ebitda, netinc):
    res = (ebitda / netinc) / (ebitda / netinc).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_max_ratio_5d_base_v020_signal'] = fol_f54_operating_leverage_ebitda_netinc_max_ratio_5d_base_v020_signal

def fol_f54_operating_leverage_ebitda_netinc_min_ratio_5d_base_v021_signal(ebitda, netinc):
    res = (ebitda / netinc) / (ebitda / netinc).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_min_ratio_5d_base_v021_signal'] = fol_f54_operating_leverage_ebitda_netinc_min_ratio_5d_base_v021_signal

def fol_f54_operating_leverage_ebitda_netinc_diff_5d_base_v022_signal(ebitda, netinc):
    res = (ebitda / netinc).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_diff_5d_base_v022_signal'] = fol_f54_operating_leverage_ebitda_netinc_diff_5d_base_v022_signal

def fol_f54_operating_leverage_ebitda_netinc_skew_5d_base_v023_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_skew_5d_base_v023_signal'] = fol_f54_operating_leverage_ebitda_netinc_skew_5d_base_v023_signal

def fol_f54_operating_leverage_ebitda_netinc_kurt_5d_base_v024_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_kurt_5d_base_v024_signal'] = fol_f54_operating_leverage_ebitda_netinc_kurt_5d_base_v024_signal

def fol_f54_operating_leverage_ebitda_netinc_rank_5d_base_v025_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_netinc_rank_5d_base_v025_signal'] = fol_f54_operating_leverage_ebitda_netinc_rank_5d_base_v025_signal

def fol_f54_operating_leverage_ebitda_ncfo_mean_5d_base_v026_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_mean_5d_base_v026_signal'] = fol_f54_operating_leverage_ebitda_ncfo_mean_5d_base_v026_signal

def fol_f54_operating_leverage_ebitda_ncfo_std_5d_base_v027_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_std_5d_base_v027_signal'] = fol_f54_operating_leverage_ebitda_ncfo_std_5d_base_v027_signal

def fol_f54_operating_leverage_ebitda_ncfo_pct_chg_5d_base_v028_signal(ebitda, ncfo):
    res = (ebitda / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_pct_chg_5d_base_v028_signal'] = fol_f54_operating_leverage_ebitda_ncfo_pct_chg_5d_base_v028_signal

def fol_f54_operating_leverage_ebitda_ncfo_mean_ratio_5d_base_v029_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_mean_ratio_5d_base_v029_signal'] = fol_f54_operating_leverage_ebitda_ncfo_mean_ratio_5d_base_v029_signal

def fol_f54_operating_leverage_ebitda_ncfo_max_ratio_5d_base_v030_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_max_ratio_5d_base_v030_signal'] = fol_f54_operating_leverage_ebitda_ncfo_max_ratio_5d_base_v030_signal

def fol_f54_operating_leverage_ebitda_ncfo_min_ratio_5d_base_v031_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_min_ratio_5d_base_v031_signal'] = fol_f54_operating_leverage_ebitda_ncfo_min_ratio_5d_base_v031_signal

def fol_f54_operating_leverage_ebitda_ncfo_diff_5d_base_v032_signal(ebitda, ncfo):
    res = (ebitda / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_diff_5d_base_v032_signal'] = fol_f54_operating_leverage_ebitda_ncfo_diff_5d_base_v032_signal

def fol_f54_operating_leverage_ebitda_ncfo_skew_5d_base_v033_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_skew_5d_base_v033_signal'] = fol_f54_operating_leverage_ebitda_ncfo_skew_5d_base_v033_signal

def fol_f54_operating_leverage_ebitda_ncfo_kurt_5d_base_v034_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_kurt_5d_base_v034_signal'] = fol_f54_operating_leverage_ebitda_ncfo_kurt_5d_base_v034_signal

def fol_f54_operating_leverage_ebitda_ncfo_rank_5d_base_v035_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_ncfo_rank_5d_base_v035_signal'] = fol_f54_operating_leverage_ebitda_ncfo_rank_5d_base_v035_signal

def fol_f54_operating_leverage_ebitda_capex_mean_5d_base_v036_signal(ebitda, capex):
    res = (ebitda / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_mean_5d_base_v036_signal'] = fol_f54_operating_leverage_ebitda_capex_mean_5d_base_v036_signal

def fol_f54_operating_leverage_ebitda_capex_std_5d_base_v037_signal(ebitda, capex):
    res = (ebitda / capex).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_std_5d_base_v037_signal'] = fol_f54_operating_leverage_ebitda_capex_std_5d_base_v037_signal

def fol_f54_operating_leverage_ebitda_capex_pct_chg_5d_base_v038_signal(ebitda, capex):
    res = (ebitda / capex).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_pct_chg_5d_base_v038_signal'] = fol_f54_operating_leverage_ebitda_capex_pct_chg_5d_base_v038_signal

def fol_f54_operating_leverage_ebitda_capex_mean_ratio_5d_base_v039_signal(ebitda, capex):
    res = (ebitda / capex) / (ebitda / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_mean_ratio_5d_base_v039_signal'] = fol_f54_operating_leverage_ebitda_capex_mean_ratio_5d_base_v039_signal

def fol_f54_operating_leverage_ebitda_capex_max_ratio_5d_base_v040_signal(ebitda, capex):
    res = (ebitda / capex) / (ebitda / capex).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_max_ratio_5d_base_v040_signal'] = fol_f54_operating_leverage_ebitda_capex_max_ratio_5d_base_v040_signal

def fol_f54_operating_leverage_ebitda_capex_min_ratio_5d_base_v041_signal(ebitda, capex):
    res = (ebitda / capex) / (ebitda / capex).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_min_ratio_5d_base_v041_signal'] = fol_f54_operating_leverage_ebitda_capex_min_ratio_5d_base_v041_signal

def fol_f54_operating_leverage_ebitda_capex_diff_5d_base_v042_signal(ebitda, capex):
    res = (ebitda / capex).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_diff_5d_base_v042_signal'] = fol_f54_operating_leverage_ebitda_capex_diff_5d_base_v042_signal

def fol_f54_operating_leverage_ebitda_capex_skew_5d_base_v043_signal(ebitda, capex):
    res = (ebitda / capex).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_skew_5d_base_v043_signal'] = fol_f54_operating_leverage_ebitda_capex_skew_5d_base_v043_signal

def fol_f54_operating_leverage_ebitda_capex_kurt_5d_base_v044_signal(ebitda, capex):
    res = (ebitda / capex).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_kurt_5d_base_v044_signal'] = fol_f54_operating_leverage_ebitda_capex_kurt_5d_base_v044_signal

def fol_f54_operating_leverage_ebitda_capex_rank_5d_base_v045_signal(ebitda, capex):
    res = (ebitda / capex).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ebitda_capex_rank_5d_base_v045_signal'] = fol_f54_operating_leverage_ebitda_capex_rank_5d_base_v045_signal

def fol_f54_operating_leverage_revenue_ebitda_mean_5d_base_v046_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_mean_5d_base_v046_signal'] = fol_f54_operating_leverage_revenue_ebitda_mean_5d_base_v046_signal

def fol_f54_operating_leverage_revenue_ebitda_std_5d_base_v047_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_std_5d_base_v047_signal'] = fol_f54_operating_leverage_revenue_ebitda_std_5d_base_v047_signal

def fol_f54_operating_leverage_revenue_ebitda_pct_chg_5d_base_v048_signal(revenue, ebitda):
    res = (revenue / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_pct_chg_5d_base_v048_signal'] = fol_f54_operating_leverage_revenue_ebitda_pct_chg_5d_base_v048_signal

def fol_f54_operating_leverage_revenue_ebitda_mean_ratio_5d_base_v049_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_mean_ratio_5d_base_v049_signal'] = fol_f54_operating_leverage_revenue_ebitda_mean_ratio_5d_base_v049_signal

def fol_f54_operating_leverage_revenue_ebitda_max_ratio_5d_base_v050_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_max_ratio_5d_base_v050_signal'] = fol_f54_operating_leverage_revenue_ebitda_max_ratio_5d_base_v050_signal

def fol_f54_operating_leverage_revenue_ebitda_min_ratio_5d_base_v051_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_min_ratio_5d_base_v051_signal'] = fol_f54_operating_leverage_revenue_ebitda_min_ratio_5d_base_v051_signal

def fol_f54_operating_leverage_revenue_ebitda_diff_5d_base_v052_signal(revenue, ebitda):
    res = (revenue / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_diff_5d_base_v052_signal'] = fol_f54_operating_leverage_revenue_ebitda_diff_5d_base_v052_signal

def fol_f54_operating_leverage_revenue_ebitda_skew_5d_base_v053_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_skew_5d_base_v053_signal'] = fol_f54_operating_leverage_revenue_ebitda_skew_5d_base_v053_signal

def fol_f54_operating_leverage_revenue_ebitda_kurt_5d_base_v054_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_kurt_5d_base_v054_signal'] = fol_f54_operating_leverage_revenue_ebitda_kurt_5d_base_v054_signal

def fol_f54_operating_leverage_revenue_ebitda_rank_5d_base_v055_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ebitda_rank_5d_base_v055_signal'] = fol_f54_operating_leverage_revenue_ebitda_rank_5d_base_v055_signal

def fol_f54_operating_leverage_revenue_mean_5d_base_v056_signal(revenue):
    res = revenue.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_mean_5d_base_v056_signal'] = fol_f54_operating_leverage_revenue_mean_5d_base_v056_signal

def fol_f54_operating_leverage_revenue_std_5d_base_v057_signal(revenue):
    res = revenue.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_std_5d_base_v057_signal'] = fol_f54_operating_leverage_revenue_std_5d_base_v057_signal

def fol_f54_operating_leverage_revenue_pct_chg_5d_base_v058_signal(revenue):
    res = revenue.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_pct_chg_5d_base_v058_signal'] = fol_f54_operating_leverage_revenue_pct_chg_5d_base_v058_signal

def fol_f54_operating_leverage_revenue_max_ratio_5d_base_v059_signal(revenue):
    res = revenue / revenue.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_max_ratio_5d_base_v059_signal'] = fol_f54_operating_leverage_revenue_max_ratio_5d_base_v059_signal

def fol_f54_operating_leverage_revenue_min_ratio_5d_base_v060_signal(revenue):
    res = revenue / revenue.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_min_ratio_5d_base_v060_signal'] = fol_f54_operating_leverage_revenue_min_ratio_5d_base_v060_signal

def fol_f54_operating_leverage_revenue_netinc_mean_5d_base_v061_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_mean_5d_base_v061_signal'] = fol_f54_operating_leverage_revenue_netinc_mean_5d_base_v061_signal

def fol_f54_operating_leverage_revenue_netinc_std_5d_base_v062_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_std_5d_base_v062_signal'] = fol_f54_operating_leverage_revenue_netinc_std_5d_base_v062_signal

def fol_f54_operating_leverage_revenue_netinc_pct_chg_5d_base_v063_signal(revenue, netinc):
    res = (revenue / netinc).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_pct_chg_5d_base_v063_signal'] = fol_f54_operating_leverage_revenue_netinc_pct_chg_5d_base_v063_signal

def fol_f54_operating_leverage_revenue_netinc_mean_ratio_5d_base_v064_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_mean_ratio_5d_base_v064_signal'] = fol_f54_operating_leverage_revenue_netinc_mean_ratio_5d_base_v064_signal

def fol_f54_operating_leverage_revenue_netinc_max_ratio_5d_base_v065_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_max_ratio_5d_base_v065_signal'] = fol_f54_operating_leverage_revenue_netinc_max_ratio_5d_base_v065_signal

def fol_f54_operating_leverage_revenue_netinc_min_ratio_5d_base_v066_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_min_ratio_5d_base_v066_signal'] = fol_f54_operating_leverage_revenue_netinc_min_ratio_5d_base_v066_signal

def fol_f54_operating_leverage_revenue_netinc_diff_5d_base_v067_signal(revenue, netinc):
    res = (revenue / netinc).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_diff_5d_base_v067_signal'] = fol_f54_operating_leverage_revenue_netinc_diff_5d_base_v067_signal

def fol_f54_operating_leverage_revenue_netinc_skew_5d_base_v068_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_skew_5d_base_v068_signal'] = fol_f54_operating_leverage_revenue_netinc_skew_5d_base_v068_signal

def fol_f54_operating_leverage_revenue_netinc_kurt_5d_base_v069_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_kurt_5d_base_v069_signal'] = fol_f54_operating_leverage_revenue_netinc_kurt_5d_base_v069_signal

def fol_f54_operating_leverage_revenue_netinc_rank_5d_base_v070_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_netinc_rank_5d_base_v070_signal'] = fol_f54_operating_leverage_revenue_netinc_rank_5d_base_v070_signal

def fol_f54_operating_leverage_revenue_ncfo_mean_5d_base_v071_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_mean_5d_base_v071_signal'] = fol_f54_operating_leverage_revenue_ncfo_mean_5d_base_v071_signal

def fol_f54_operating_leverage_revenue_ncfo_std_5d_base_v072_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_std_5d_base_v072_signal'] = fol_f54_operating_leverage_revenue_ncfo_std_5d_base_v072_signal

def fol_f54_operating_leverage_revenue_ncfo_pct_chg_5d_base_v073_signal(revenue, ncfo):
    res = (revenue / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_pct_chg_5d_base_v073_signal'] = fol_f54_operating_leverage_revenue_ncfo_pct_chg_5d_base_v073_signal

def fol_f54_operating_leverage_revenue_ncfo_mean_ratio_5d_base_v074_signal(revenue, ncfo):
    res = (revenue / ncfo) / (revenue / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_mean_ratio_5d_base_v074_signal'] = fol_f54_operating_leverage_revenue_ncfo_mean_ratio_5d_base_v074_signal

def fol_f54_operating_leverage_revenue_ncfo_max_ratio_5d_base_v075_signal(revenue, ncfo):
    res = (revenue / ncfo) / (revenue / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_max_ratio_5d_base_v075_signal'] = fol_f54_operating_leverage_revenue_ncfo_max_ratio_5d_base_v075_signal

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
