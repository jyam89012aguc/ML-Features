import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fic_f52_inventory_cycles_revenue_ncfo_min_ratio_5d_base_v076_signal(revenue, ncfo):
    res = (revenue / ncfo) / (revenue / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_min_ratio_5d_base_v076_signal'] = fic_f52_inventory_cycles_revenue_ncfo_min_ratio_5d_base_v076_signal

def fic_f52_inventory_cycles_revenue_ncfo_diff_5d_base_v077_signal(revenue, ncfo):
    res = (revenue / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_diff_5d_base_v077_signal'] = fic_f52_inventory_cycles_revenue_ncfo_diff_5d_base_v077_signal

def fic_f52_inventory_cycles_revenue_ncfo_skew_5d_base_v078_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_skew_5d_base_v078_signal'] = fic_f52_inventory_cycles_revenue_ncfo_skew_5d_base_v078_signal

def fic_f52_inventory_cycles_revenue_ncfo_kurt_5d_base_v079_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_kurt_5d_base_v079_signal'] = fic_f52_inventory_cycles_revenue_ncfo_kurt_5d_base_v079_signal

def fic_f52_inventory_cycles_revenue_ncfo_rank_5d_base_v080_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_ncfo_rank_5d_base_v080_signal'] = fic_f52_inventory_cycles_revenue_ncfo_rank_5d_base_v080_signal

def fic_f52_inventory_cycles_revenue_fcf_mean_5d_base_v081_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_mean_5d_base_v081_signal'] = fic_f52_inventory_cycles_revenue_fcf_mean_5d_base_v081_signal

def fic_f52_inventory_cycles_revenue_fcf_std_5d_base_v082_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_std_5d_base_v082_signal'] = fic_f52_inventory_cycles_revenue_fcf_std_5d_base_v082_signal

def fic_f52_inventory_cycles_revenue_fcf_pct_chg_5d_base_v083_signal(revenue, fcf):
    res = (revenue / fcf).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_pct_chg_5d_base_v083_signal'] = fic_f52_inventory_cycles_revenue_fcf_pct_chg_5d_base_v083_signal

def fic_f52_inventory_cycles_revenue_fcf_mean_ratio_5d_base_v084_signal(revenue, fcf):
    res = (revenue / fcf) / (revenue / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_mean_ratio_5d_base_v084_signal'] = fic_f52_inventory_cycles_revenue_fcf_mean_ratio_5d_base_v084_signal

def fic_f52_inventory_cycles_revenue_fcf_max_ratio_5d_base_v085_signal(revenue, fcf):
    res = (revenue / fcf) / (revenue / fcf).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_max_ratio_5d_base_v085_signal'] = fic_f52_inventory_cycles_revenue_fcf_max_ratio_5d_base_v085_signal

def fic_f52_inventory_cycles_revenue_fcf_min_ratio_5d_base_v086_signal(revenue, fcf):
    res = (revenue / fcf) / (revenue / fcf).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_min_ratio_5d_base_v086_signal'] = fic_f52_inventory_cycles_revenue_fcf_min_ratio_5d_base_v086_signal

def fic_f52_inventory_cycles_revenue_fcf_diff_5d_base_v087_signal(revenue, fcf):
    res = (revenue / fcf).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_diff_5d_base_v087_signal'] = fic_f52_inventory_cycles_revenue_fcf_diff_5d_base_v087_signal

def fic_f52_inventory_cycles_revenue_fcf_skew_5d_base_v088_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_skew_5d_base_v088_signal'] = fic_f52_inventory_cycles_revenue_fcf_skew_5d_base_v088_signal

def fic_f52_inventory_cycles_revenue_fcf_kurt_5d_base_v089_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_kurt_5d_base_v089_signal'] = fic_f52_inventory_cycles_revenue_fcf_kurt_5d_base_v089_signal

def fic_f52_inventory_cycles_revenue_fcf_rank_5d_base_v090_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_revenue_fcf_rank_5d_base_v090_signal'] = fic_f52_inventory_cycles_revenue_fcf_rank_5d_base_v090_signal

def fic_f52_inventory_cycles_ebitda_assets_mean_5d_base_v091_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_mean_5d_base_v091_signal'] = fic_f52_inventory_cycles_ebitda_assets_mean_5d_base_v091_signal

def fic_f52_inventory_cycles_ebitda_assets_std_5d_base_v092_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_std_5d_base_v092_signal'] = fic_f52_inventory_cycles_ebitda_assets_std_5d_base_v092_signal

def fic_f52_inventory_cycles_ebitda_assets_pct_chg_5d_base_v093_signal(ebitda, assets):
    res = (ebitda / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_pct_chg_5d_base_v093_signal'] = fic_f52_inventory_cycles_ebitda_assets_pct_chg_5d_base_v093_signal

def fic_f52_inventory_cycles_ebitda_assets_mean_ratio_5d_base_v094_signal(ebitda, assets):
    res = (ebitda / assets) / (ebitda / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_mean_ratio_5d_base_v094_signal'] = fic_f52_inventory_cycles_ebitda_assets_mean_ratio_5d_base_v094_signal

def fic_f52_inventory_cycles_ebitda_assets_max_ratio_5d_base_v095_signal(ebitda, assets):
    res = (ebitda / assets) / (ebitda / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_max_ratio_5d_base_v095_signal'] = fic_f52_inventory_cycles_ebitda_assets_max_ratio_5d_base_v095_signal

def fic_f52_inventory_cycles_ebitda_assets_min_ratio_5d_base_v096_signal(ebitda, assets):
    res = (ebitda / assets) / (ebitda / assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_min_ratio_5d_base_v096_signal'] = fic_f52_inventory_cycles_ebitda_assets_min_ratio_5d_base_v096_signal

def fic_f52_inventory_cycles_ebitda_assets_diff_5d_base_v097_signal(ebitda, assets):
    res = (ebitda / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_diff_5d_base_v097_signal'] = fic_f52_inventory_cycles_ebitda_assets_diff_5d_base_v097_signal

def fic_f52_inventory_cycles_ebitda_assets_skew_5d_base_v098_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_skew_5d_base_v098_signal'] = fic_f52_inventory_cycles_ebitda_assets_skew_5d_base_v098_signal

def fic_f52_inventory_cycles_ebitda_assets_kurt_5d_base_v099_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_kurt_5d_base_v099_signal'] = fic_f52_inventory_cycles_ebitda_assets_kurt_5d_base_v099_signal

def fic_f52_inventory_cycles_ebitda_assets_rank_5d_base_v100_signal(ebitda, assets):
    res = (ebitda / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_assets_rank_5d_base_v100_signal'] = fic_f52_inventory_cycles_ebitda_assets_rank_5d_base_v100_signal

def fic_f52_inventory_cycles_ebitda_revenue_mean_5d_base_v101_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_mean_5d_base_v101_signal'] = fic_f52_inventory_cycles_ebitda_revenue_mean_5d_base_v101_signal

def fic_f52_inventory_cycles_ebitda_revenue_std_5d_base_v102_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_std_5d_base_v102_signal'] = fic_f52_inventory_cycles_ebitda_revenue_std_5d_base_v102_signal

def fic_f52_inventory_cycles_ebitda_revenue_pct_chg_5d_base_v103_signal(ebitda, revenue):
    res = (ebitda / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_pct_chg_5d_base_v103_signal'] = fic_f52_inventory_cycles_ebitda_revenue_pct_chg_5d_base_v103_signal

def fic_f52_inventory_cycles_ebitda_revenue_mean_ratio_5d_base_v104_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_mean_ratio_5d_base_v104_signal'] = fic_f52_inventory_cycles_ebitda_revenue_mean_ratio_5d_base_v104_signal

def fic_f52_inventory_cycles_ebitda_revenue_max_ratio_5d_base_v105_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_max_ratio_5d_base_v105_signal'] = fic_f52_inventory_cycles_ebitda_revenue_max_ratio_5d_base_v105_signal

def fic_f52_inventory_cycles_ebitda_revenue_min_ratio_5d_base_v106_signal(ebitda, revenue):
    res = (ebitda / revenue) / (ebitda / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_min_ratio_5d_base_v106_signal'] = fic_f52_inventory_cycles_ebitda_revenue_min_ratio_5d_base_v106_signal

def fic_f52_inventory_cycles_ebitda_revenue_diff_5d_base_v107_signal(ebitda, revenue):
    res = (ebitda / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_diff_5d_base_v107_signal'] = fic_f52_inventory_cycles_ebitda_revenue_diff_5d_base_v107_signal

def fic_f52_inventory_cycles_ebitda_revenue_skew_5d_base_v108_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_skew_5d_base_v108_signal'] = fic_f52_inventory_cycles_ebitda_revenue_skew_5d_base_v108_signal

def fic_f52_inventory_cycles_ebitda_revenue_kurt_5d_base_v109_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_kurt_5d_base_v109_signal'] = fic_f52_inventory_cycles_ebitda_revenue_kurt_5d_base_v109_signal

def fic_f52_inventory_cycles_ebitda_revenue_rank_5d_base_v110_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_revenue_rank_5d_base_v110_signal'] = fic_f52_inventory_cycles_ebitda_revenue_rank_5d_base_v110_signal

def fic_f52_inventory_cycles_ebitda_mean_5d_base_v111_signal(ebitda):
    res = ebitda.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_mean_5d_base_v111_signal'] = fic_f52_inventory_cycles_ebitda_mean_5d_base_v111_signal

def fic_f52_inventory_cycles_ebitda_std_5d_base_v112_signal(ebitda):
    res = ebitda.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_std_5d_base_v112_signal'] = fic_f52_inventory_cycles_ebitda_std_5d_base_v112_signal

def fic_f52_inventory_cycles_ebitda_pct_chg_5d_base_v113_signal(ebitda):
    res = ebitda.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_pct_chg_5d_base_v113_signal'] = fic_f52_inventory_cycles_ebitda_pct_chg_5d_base_v113_signal

def fic_f52_inventory_cycles_ebitda_max_ratio_5d_base_v114_signal(ebitda):
    res = ebitda / ebitda.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_max_ratio_5d_base_v114_signal'] = fic_f52_inventory_cycles_ebitda_max_ratio_5d_base_v114_signal

def fic_f52_inventory_cycles_ebitda_min_ratio_5d_base_v115_signal(ebitda):
    res = ebitda / ebitda.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_min_ratio_5d_base_v115_signal'] = fic_f52_inventory_cycles_ebitda_min_ratio_5d_base_v115_signal

def fic_f52_inventory_cycles_ebitda_ncfo_mean_5d_base_v116_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_mean_5d_base_v116_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_mean_5d_base_v116_signal

def fic_f52_inventory_cycles_ebitda_ncfo_std_5d_base_v117_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_std_5d_base_v117_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_std_5d_base_v117_signal

def fic_f52_inventory_cycles_ebitda_ncfo_pct_chg_5d_base_v118_signal(ebitda, ncfo):
    res = (ebitda / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_pct_chg_5d_base_v118_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_pct_chg_5d_base_v118_signal

def fic_f52_inventory_cycles_ebitda_ncfo_mean_ratio_5d_base_v119_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_mean_ratio_5d_base_v119_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_mean_ratio_5d_base_v119_signal

def fic_f52_inventory_cycles_ebitda_ncfo_max_ratio_5d_base_v120_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_max_ratio_5d_base_v120_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_max_ratio_5d_base_v120_signal

def fic_f52_inventory_cycles_ebitda_ncfo_min_ratio_5d_base_v121_signal(ebitda, ncfo):
    res = (ebitda / ncfo) / (ebitda / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_min_ratio_5d_base_v121_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_min_ratio_5d_base_v121_signal

def fic_f52_inventory_cycles_ebitda_ncfo_diff_5d_base_v122_signal(ebitda, ncfo):
    res = (ebitda / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_diff_5d_base_v122_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_diff_5d_base_v122_signal

def fic_f52_inventory_cycles_ebitda_ncfo_skew_5d_base_v123_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_skew_5d_base_v123_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_skew_5d_base_v123_signal

def fic_f52_inventory_cycles_ebitda_ncfo_kurt_5d_base_v124_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_kurt_5d_base_v124_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_kurt_5d_base_v124_signal

def fic_f52_inventory_cycles_ebitda_ncfo_rank_5d_base_v125_signal(ebitda, ncfo):
    res = (ebitda / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_ncfo_rank_5d_base_v125_signal'] = fic_f52_inventory_cycles_ebitda_ncfo_rank_5d_base_v125_signal

def fic_f52_inventory_cycles_ebitda_fcf_mean_5d_base_v126_signal(ebitda, fcf):
    res = (ebitda / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_mean_5d_base_v126_signal'] = fic_f52_inventory_cycles_ebitda_fcf_mean_5d_base_v126_signal

def fic_f52_inventory_cycles_ebitda_fcf_std_5d_base_v127_signal(ebitda, fcf):
    res = (ebitda / fcf).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_std_5d_base_v127_signal'] = fic_f52_inventory_cycles_ebitda_fcf_std_5d_base_v127_signal

def fic_f52_inventory_cycles_ebitda_fcf_pct_chg_5d_base_v128_signal(ebitda, fcf):
    res = (ebitda / fcf).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_pct_chg_5d_base_v128_signal'] = fic_f52_inventory_cycles_ebitda_fcf_pct_chg_5d_base_v128_signal

def fic_f52_inventory_cycles_ebitda_fcf_mean_ratio_5d_base_v129_signal(ebitda, fcf):
    res = (ebitda / fcf) / (ebitda / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_mean_ratio_5d_base_v129_signal'] = fic_f52_inventory_cycles_ebitda_fcf_mean_ratio_5d_base_v129_signal

def fic_f52_inventory_cycles_ebitda_fcf_max_ratio_5d_base_v130_signal(ebitda, fcf):
    res = (ebitda / fcf) / (ebitda / fcf).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_max_ratio_5d_base_v130_signal'] = fic_f52_inventory_cycles_ebitda_fcf_max_ratio_5d_base_v130_signal

def fic_f52_inventory_cycles_ebitda_fcf_min_ratio_5d_base_v131_signal(ebitda, fcf):
    res = (ebitda / fcf) / (ebitda / fcf).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_min_ratio_5d_base_v131_signal'] = fic_f52_inventory_cycles_ebitda_fcf_min_ratio_5d_base_v131_signal

def fic_f52_inventory_cycles_ebitda_fcf_diff_5d_base_v132_signal(ebitda, fcf):
    res = (ebitda / fcf).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_diff_5d_base_v132_signal'] = fic_f52_inventory_cycles_ebitda_fcf_diff_5d_base_v132_signal

def fic_f52_inventory_cycles_ebitda_fcf_skew_5d_base_v133_signal(ebitda, fcf):
    res = (ebitda / fcf).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_skew_5d_base_v133_signal'] = fic_f52_inventory_cycles_ebitda_fcf_skew_5d_base_v133_signal

def fic_f52_inventory_cycles_ebitda_fcf_kurt_5d_base_v134_signal(ebitda, fcf):
    res = (ebitda / fcf).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_kurt_5d_base_v134_signal'] = fic_f52_inventory_cycles_ebitda_fcf_kurt_5d_base_v134_signal

def fic_f52_inventory_cycles_ebitda_fcf_rank_5d_base_v135_signal(ebitda, fcf):
    res = (ebitda / fcf).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ebitda_fcf_rank_5d_base_v135_signal'] = fic_f52_inventory_cycles_ebitda_fcf_rank_5d_base_v135_signal

def fic_f52_inventory_cycles_ncfo_assets_mean_5d_base_v136_signal(ncfo, assets):
    res = (ncfo / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_mean_5d_base_v136_signal'] = fic_f52_inventory_cycles_ncfo_assets_mean_5d_base_v136_signal

def fic_f52_inventory_cycles_ncfo_assets_std_5d_base_v137_signal(ncfo, assets):
    res = (ncfo / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_std_5d_base_v137_signal'] = fic_f52_inventory_cycles_ncfo_assets_std_5d_base_v137_signal

def fic_f52_inventory_cycles_ncfo_assets_pct_chg_5d_base_v138_signal(ncfo, assets):
    res = (ncfo / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_pct_chg_5d_base_v138_signal'] = fic_f52_inventory_cycles_ncfo_assets_pct_chg_5d_base_v138_signal

def fic_f52_inventory_cycles_ncfo_assets_mean_ratio_5d_base_v139_signal(ncfo, assets):
    res = (ncfo / assets) / (ncfo / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_mean_ratio_5d_base_v139_signal'] = fic_f52_inventory_cycles_ncfo_assets_mean_ratio_5d_base_v139_signal

def fic_f52_inventory_cycles_ncfo_assets_max_ratio_5d_base_v140_signal(ncfo, assets):
    res = (ncfo / assets) / (ncfo / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_max_ratio_5d_base_v140_signal'] = fic_f52_inventory_cycles_ncfo_assets_max_ratio_5d_base_v140_signal

def fic_f52_inventory_cycles_ncfo_assets_min_ratio_5d_base_v141_signal(ncfo, assets):
    res = (ncfo / assets) / (ncfo / assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_min_ratio_5d_base_v141_signal'] = fic_f52_inventory_cycles_ncfo_assets_min_ratio_5d_base_v141_signal

def fic_f52_inventory_cycles_ncfo_assets_diff_5d_base_v142_signal(ncfo, assets):
    res = (ncfo / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_diff_5d_base_v142_signal'] = fic_f52_inventory_cycles_ncfo_assets_diff_5d_base_v142_signal

def fic_f52_inventory_cycles_ncfo_assets_skew_5d_base_v143_signal(ncfo, assets):
    res = (ncfo / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_skew_5d_base_v143_signal'] = fic_f52_inventory_cycles_ncfo_assets_skew_5d_base_v143_signal

def fic_f52_inventory_cycles_ncfo_assets_kurt_5d_base_v144_signal(ncfo, assets):
    res = (ncfo / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_kurt_5d_base_v144_signal'] = fic_f52_inventory_cycles_ncfo_assets_kurt_5d_base_v144_signal

def fic_f52_inventory_cycles_ncfo_assets_rank_5d_base_v145_signal(ncfo, assets):
    res = (ncfo / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_assets_rank_5d_base_v145_signal'] = fic_f52_inventory_cycles_ncfo_assets_rank_5d_base_v145_signal

def fic_f52_inventory_cycles_ncfo_revenue_mean_5d_base_v146_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_revenue_mean_5d_base_v146_signal'] = fic_f52_inventory_cycles_ncfo_revenue_mean_5d_base_v146_signal

def fic_f52_inventory_cycles_ncfo_revenue_std_5d_base_v147_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_revenue_std_5d_base_v147_signal'] = fic_f52_inventory_cycles_ncfo_revenue_std_5d_base_v147_signal

def fic_f52_inventory_cycles_ncfo_revenue_pct_chg_5d_base_v148_signal(ncfo, revenue):
    res = (ncfo / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_revenue_pct_chg_5d_base_v148_signal'] = fic_f52_inventory_cycles_ncfo_revenue_pct_chg_5d_base_v148_signal

def fic_f52_inventory_cycles_ncfo_revenue_mean_ratio_5d_base_v149_signal(ncfo, revenue):
    res = (ncfo / revenue) / (ncfo / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_revenue_mean_ratio_5d_base_v149_signal'] = fic_f52_inventory_cycles_ncfo_revenue_mean_ratio_5d_base_v149_signal

def fic_f52_inventory_cycles_ncfo_revenue_max_ratio_5d_base_v150_signal(ncfo, revenue):
    res = (ncfo / revenue) / (ncfo / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fic_f52_inventory_cycles_ncfo_revenue_max_ratio_5d_base_v150_signal'] = fic_f52_inventory_cycles_ncfo_revenue_max_ratio_5d_base_v150_signal

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
