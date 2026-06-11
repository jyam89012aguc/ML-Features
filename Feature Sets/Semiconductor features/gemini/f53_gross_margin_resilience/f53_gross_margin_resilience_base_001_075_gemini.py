import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fgmr_f53_gross_margin_resilience_ebitda_mean_5d_base_v001_signal(ebitda):
    res = ebitda.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_mean_5d_base_v001_signal'] = fgmr_f53_gross_margin_resilience_ebitda_mean_5d_base_v001_signal

def fgmr_f53_gross_margin_resilience_ebitda_std_5d_base_v002_signal(ebitda):
    res = ebitda.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_std_5d_base_v002_signal'] = fgmr_f53_gross_margin_resilience_ebitda_std_5d_base_v002_signal

def fgmr_f53_gross_margin_resilience_ebitda_pct_chg_5d_base_v003_signal(ebitda):
    res = ebitda.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_pct_chg_5d_base_v003_signal'] = fgmr_f53_gross_margin_resilience_ebitda_pct_chg_5d_base_v003_signal

def fgmr_f53_gross_margin_resilience_ebitda_max_ratio_5d_base_v004_signal(ebitda):
    res = ebitda / ebitda.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_max_ratio_5d_base_v004_signal'] = fgmr_f53_gross_margin_resilience_ebitda_max_ratio_5d_base_v004_signal

def fgmr_f53_gross_margin_resilience_ebitda_min_ratio_5d_base_v005_signal(ebitda):
    res = ebitda / ebitda.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_min_ratio_5d_base_v005_signal'] = fgmr_f53_gross_margin_resilience_ebitda_min_ratio_5d_base_v005_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_mean_5d_base_v006_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_mean_5d_base_v006_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_mean_5d_base_v006_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_std_5d_base_v007_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_std_5d_base_v007_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_std_5d_base_v007_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_pct_chg_5d_base_v008_signal(ebitda, revenue):
    res = (ebitda / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_pct_chg_5d_base_v008_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_pct_chg_5d_base_v008_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_mean_ratio_5d_base_v009_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_mean_ratio_5d_base_v009_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_mean_ratio_5d_base_v009_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_max_ratio_5d_base_v010_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_max_ratio_5d_base_v010_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_max_ratio_5d_base_v010_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_min_ratio_5d_base_v011_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_min_ratio_5d_base_v011_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_min_ratio_5d_base_v011_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_diff_5d_base_v012_signal(ebitda, revenue):
    res = (ebitda / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_diff_5d_base_v012_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_diff_5d_base_v012_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_skew_5d_base_v013_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_skew_5d_base_v013_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_skew_5d_base_v013_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_kurt_5d_base_v014_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_kurt_5d_base_v014_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_kurt_5d_base_v014_signal

def fgmr_f53_gross_margin_resilience_ebitda_revenue_rank_5d_base_v015_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_revenue_rank_5d_base_v015_signal'] = fgmr_f53_gross_margin_resilience_ebitda_revenue_rank_5d_base_v015_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_mean_5d_base_v016_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_mean_5d_base_v016_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_mean_5d_base_v016_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_std_5d_base_v017_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_std_5d_base_v017_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_std_5d_base_v017_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_pct_chg_5d_base_v018_signal(ebitda, netinc):
    res = (ebitda / netinc).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_pct_chg_5d_base_v018_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_pct_chg_5d_base_v018_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_mean_ratio_5d_base_v019_signal(ebitda, netinc):
    res = (ebitda / netinc) / (ebitda / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_mean_ratio_5d_base_v019_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_mean_ratio_5d_base_v019_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_max_ratio_5d_base_v020_signal(ebitda, netinc):
    res = (ebitda / netinc) / (ebitda / netinc).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_max_ratio_5d_base_v020_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_max_ratio_5d_base_v020_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_min_ratio_5d_base_v021_signal(ebitda, netinc):
    res = (ebitda / netinc) / (ebitda / netinc).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_min_ratio_5d_base_v021_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_min_ratio_5d_base_v021_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_diff_5d_base_v022_signal(ebitda, netinc):
    res = (ebitda / netinc).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_diff_5d_base_v022_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_diff_5d_base_v022_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_skew_5d_base_v023_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_skew_5d_base_v023_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_skew_5d_base_v023_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_kurt_5d_base_v024_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_kurt_5d_base_v024_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_kurt_5d_base_v024_signal

def fgmr_f53_gross_margin_resilience_ebitda_netinc_rank_5d_base_v025_signal(ebitda, netinc):
    res = (ebitda / netinc).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_netinc_rank_5d_base_v025_signal'] = fgmr_f53_gross_margin_resilience_ebitda_netinc_rank_5d_base_v025_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_mean_5d_base_v026_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_mean_5d_base_v026_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_mean_5d_base_v026_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_std_5d_base_v027_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_std_5d_base_v027_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_std_5d_base_v027_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_pct_chg_5d_base_v028_signal(ebitda, assets):
    res = (ebitda / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_pct_chg_5d_base_v028_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_pct_chg_5d_base_v028_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_mean_ratio_5d_base_v029_signal(ebitda, assets):
    res = (ebitda / assets) / (ebitda / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_mean_ratio_5d_base_v029_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_mean_ratio_5d_base_v029_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_max_ratio_5d_base_v030_signal(ebitda, assets):
    res = (ebitda / assets) / (ebitda / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_max_ratio_5d_base_v030_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_max_ratio_5d_base_v030_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_min_ratio_5d_base_v031_signal(ebitda, assets):
    res = (ebitda / assets) / (ebitda / assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_min_ratio_5d_base_v031_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_min_ratio_5d_base_v031_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_diff_5d_base_v032_signal(ebitda, assets):
    res = (ebitda / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_diff_5d_base_v032_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_diff_5d_base_v032_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_skew_5d_base_v033_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_skew_5d_base_v033_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_skew_5d_base_v033_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_kurt_5d_base_v034_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_kurt_5d_base_v034_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_kurt_5d_base_v034_signal

def fgmr_f53_gross_margin_resilience_ebitda_assets_rank_5d_base_v035_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_assets_rank_5d_base_v035_signal'] = fgmr_f53_gross_margin_resilience_ebitda_assets_rank_5d_base_v035_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_mean_5d_base_v036_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_mean_5d_base_v036_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_mean_5d_base_v036_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_std_5d_base_v037_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_std_5d_base_v037_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_std_5d_base_v037_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_pct_chg_5d_base_v038_signal(ebitda, ncfo):
    res = (ebitda / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_pct_chg_5d_base_v038_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_pct_chg_5d_base_v038_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_mean_ratio_5d_base_v039_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_mean_ratio_5d_base_v039_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_mean_ratio_5d_base_v039_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_max_ratio_5d_base_v040_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_max_ratio_5d_base_v040_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_max_ratio_5d_base_v040_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_min_ratio_5d_base_v041_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_min_ratio_5d_base_v041_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_min_ratio_5d_base_v041_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_diff_5d_base_v042_signal(ebitda, ncfo):
    res = (ebitda / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_diff_5d_base_v042_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_diff_5d_base_v042_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_skew_5d_base_v043_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_skew_5d_base_v043_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_skew_5d_base_v043_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_kurt_5d_base_v044_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_kurt_5d_base_v044_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_kurt_5d_base_v044_signal

def fgmr_f53_gross_margin_resilience_ebitda_ncfo_rank_5d_base_v045_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_ebitda_ncfo_rank_5d_base_v045_signal'] = fgmr_f53_gross_margin_resilience_ebitda_ncfo_rank_5d_base_v045_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_mean_5d_base_v046_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_mean_5d_base_v046_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_mean_5d_base_v046_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_std_5d_base_v047_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_std_5d_base_v047_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_std_5d_base_v047_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_pct_chg_5d_base_v048_signal(revenue, ebitda):
    res = (revenue / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_pct_chg_5d_base_v048_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_pct_chg_5d_base_v048_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_mean_ratio_5d_base_v049_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_mean_ratio_5d_base_v049_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_mean_ratio_5d_base_v049_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_max_ratio_5d_base_v050_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_max_ratio_5d_base_v050_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_max_ratio_5d_base_v050_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_min_ratio_5d_base_v051_signal(revenue, ebitda):
    res = (revenue / ebitda) / (revenue / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_min_ratio_5d_base_v051_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_min_ratio_5d_base_v051_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_diff_5d_base_v052_signal(revenue, ebitda):
    res = (revenue / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_diff_5d_base_v052_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_diff_5d_base_v052_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_skew_5d_base_v053_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_skew_5d_base_v053_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_skew_5d_base_v053_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_kurt_5d_base_v054_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_kurt_5d_base_v054_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_kurt_5d_base_v054_signal

def fgmr_f53_gross_margin_resilience_revenue_ebitda_rank_5d_base_v055_signal(revenue, ebitda):
    res = (revenue / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_ebitda_rank_5d_base_v055_signal'] = fgmr_f53_gross_margin_resilience_revenue_ebitda_rank_5d_base_v055_signal

def fgmr_f53_gross_margin_resilience_revenue_mean_5d_base_v056_signal(revenue):
    res = revenue.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_mean_5d_base_v056_signal'] = fgmr_f53_gross_margin_resilience_revenue_mean_5d_base_v056_signal

def fgmr_f53_gross_margin_resilience_revenue_std_5d_base_v057_signal(revenue):
    res = revenue.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_std_5d_base_v057_signal'] = fgmr_f53_gross_margin_resilience_revenue_std_5d_base_v057_signal

def fgmr_f53_gross_margin_resilience_revenue_pct_chg_5d_base_v058_signal(revenue):
    res = revenue.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_pct_chg_5d_base_v058_signal'] = fgmr_f53_gross_margin_resilience_revenue_pct_chg_5d_base_v058_signal

def fgmr_f53_gross_margin_resilience_revenue_max_ratio_5d_base_v059_signal(revenue):
    res = revenue / revenue.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_max_ratio_5d_base_v059_signal'] = fgmr_f53_gross_margin_resilience_revenue_max_ratio_5d_base_v059_signal

def fgmr_f53_gross_margin_resilience_revenue_min_ratio_5d_base_v060_signal(revenue):
    res = revenue / revenue.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_min_ratio_5d_base_v060_signal'] = fgmr_f53_gross_margin_resilience_revenue_min_ratio_5d_base_v060_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_mean_5d_base_v061_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_mean_5d_base_v061_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_mean_5d_base_v061_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_std_5d_base_v062_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_std_5d_base_v062_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_std_5d_base_v062_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_pct_chg_5d_base_v063_signal(revenue, netinc):
    res = (revenue / netinc).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_pct_chg_5d_base_v063_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_pct_chg_5d_base_v063_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_mean_ratio_5d_base_v064_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_mean_ratio_5d_base_v064_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_mean_ratio_5d_base_v064_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_max_ratio_5d_base_v065_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_max_ratio_5d_base_v065_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_max_ratio_5d_base_v065_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_min_ratio_5d_base_v066_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_min_ratio_5d_base_v066_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_min_ratio_5d_base_v066_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_diff_5d_base_v067_signal(revenue, netinc):
    res = (revenue / netinc).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_diff_5d_base_v067_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_diff_5d_base_v067_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_skew_5d_base_v068_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_skew_5d_base_v068_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_skew_5d_base_v068_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_kurt_5d_base_v069_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_kurt_5d_base_v069_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_kurt_5d_base_v069_signal

def fgmr_f53_gross_margin_resilience_revenue_netinc_rank_5d_base_v070_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_netinc_rank_5d_base_v070_signal'] = fgmr_f53_gross_margin_resilience_revenue_netinc_rank_5d_base_v070_signal

def fgmr_f53_gross_margin_resilience_revenue_assets_mean_5d_base_v071_signal(revenue, assets):
    res = (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_assets_mean_5d_base_v071_signal'] = fgmr_f53_gross_margin_resilience_revenue_assets_mean_5d_base_v071_signal

def fgmr_f53_gross_margin_resilience_revenue_assets_std_5d_base_v072_signal(revenue, assets):
    res = (revenue / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_assets_std_5d_base_v072_signal'] = fgmr_f53_gross_margin_resilience_revenue_assets_std_5d_base_v072_signal

def fgmr_f53_gross_margin_resilience_revenue_assets_pct_chg_5d_base_v073_signal(revenue, assets):
    res = (revenue / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_assets_pct_chg_5d_base_v073_signal'] = fgmr_f53_gross_margin_resilience_revenue_assets_pct_chg_5d_base_v073_signal

def fgmr_f53_gross_margin_resilience_revenue_assets_mean_ratio_5d_base_v074_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_assets_mean_ratio_5d_base_v074_signal'] = fgmr_f53_gross_margin_resilience_revenue_assets_mean_ratio_5d_base_v074_signal

def fgmr_f53_gross_margin_resilience_revenue_assets_max_ratio_5d_base_v075_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fgmr_f53_gross_margin_resilience_revenue_assets_max_ratio_5d_base_v075_signal'] = fgmr_f53_gross_margin_resilience_revenue_assets_max_ratio_5d_base_v075_signal

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
