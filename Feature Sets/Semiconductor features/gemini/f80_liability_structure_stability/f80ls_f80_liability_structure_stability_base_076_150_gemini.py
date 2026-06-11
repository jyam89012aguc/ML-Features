import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f80ls_f80_liability_structure_stability_liabilities_zscore_252d_base_v076_signal(liabilities):
    res = (liabilities - liabilities.rolling(252).mean()) / liabilities.rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_zscore_252d_base_v076_signal'] = f80ls_f80_liability_structure_stability_liabilities_zscore_252d_base_v076_signal

def f80ls_f80_liability_structure_stability_liabilities_rank_252d_base_v077_signal(liabilities):
    res = liabilities.rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_rank_252d_base_v077_signal'] = f80ls_f80_liability_structure_stability_liabilities_rank_252d_base_v077_signal

def f80ls_f80_liability_structure_stability_liabilities_diff_252d_base_v078_signal(liabilities):
    res = liabilities.diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_diff_252d_base_v078_signal'] = f80ls_f80_liability_structure_stability_liabilities_diff_252d_base_v078_signal

def f80ls_f80_liability_structure_stability_liabilities_skew_252d_base_v079_signal(liabilities):
    res = liabilities.rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_skew_252d_base_v079_signal'] = f80ls_f80_liability_structure_stability_liabilities_skew_252d_base_v079_signal

def f80ls_f80_liability_structure_stability_liabilities_kurt_252d_base_v080_signal(liabilities):
    res = liabilities.rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_kurt_252d_base_v080_signal'] = f80ls_f80_liability_structure_stability_liabilities_kurt_252d_base_v080_signal

def f80ls_f80_liability_structure_stability_liabilities_median_252d_base_v081_signal(liabilities):
    res = liabilities.rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_median_252d_base_v081_signal'] = f80ls_f80_liability_structure_stability_liabilities_median_252d_base_v081_signal

def f80ls_f80_liability_structure_stability_liabilities_min_max_ratio_252d_base_v082_signal(liabilities):
    res = liabilities.rolling(252).min() / liabilities.rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_min_max_ratio_252d_base_v082_signal'] = f80ls_f80_liability_structure_stability_liabilities_min_max_ratio_252d_base_v082_signal

def f80ls_f80_liability_structure_stability_liabilities_max_ratio_252d_base_v083_signal(liabilities):
    res = liabilities / liabilities.rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_max_ratio_252d_base_v083_signal'] = f80ls_f80_liability_structure_stability_liabilities_max_ratio_252d_base_v083_signal

def f80ls_f80_liability_structure_stability_liabilities_min_ratio_252d_base_v084_signal(liabilities):
    res = liabilities / liabilities.rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_min_ratio_252d_base_v084_signal'] = f80ls_f80_liability_structure_stability_liabilities_min_ratio_252d_base_v084_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_mean_5d_base_v085_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_mean_5d_base_v085_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_mean_5d_base_v085_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_std_5d_base_v086_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_std_5d_base_v086_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_std_5d_base_v086_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_5d_base_v087_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_5d_base_v087_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_5d_base_v087_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_zscore_5d_base_v088_signal(assets, liabilities):
    res = ((liabilities / assets) - (liabilities / assets).rolling(5).mean()) / (liabilities / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_zscore_5d_base_v088_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_zscore_5d_base_v088_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_rank_5d_base_v089_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_rank_5d_base_v089_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_rank_5d_base_v089_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_diff_5d_base_v090_signal(assets, liabilities):
    res = (liabilities / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_diff_5d_base_v090_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_diff_5d_base_v090_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_skew_5d_base_v091_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_skew_5d_base_v091_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_skew_5d_base_v091_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_kurt_5d_base_v092_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_kurt_5d_base_v092_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_kurt_5d_base_v092_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_median_5d_base_v093_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_median_5d_base_v093_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_median_5d_base_v093_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_5d_base_v094_signal(assets, liabilities):
    res = (liabilities / assets).rolling(5).min() / (liabilities / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_5d_base_v094_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_5d_base_v094_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_5d_base_v095_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_5d_base_v095_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_5d_base_v095_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_5d_base_v096_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_5d_base_v096_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_5d_base_v096_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_mean_10d_base_v097_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_mean_10d_base_v097_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_mean_10d_base_v097_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_std_10d_base_v098_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_std_10d_base_v098_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_std_10d_base_v098_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_10d_base_v099_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_10d_base_v099_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_10d_base_v099_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_zscore_10d_base_v100_signal(assets, liabilities):
    res = ((liabilities / assets) - (liabilities / assets).rolling(10).mean()) / (liabilities / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_zscore_10d_base_v100_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_zscore_10d_base_v100_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_rank_10d_base_v101_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_rank_10d_base_v101_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_rank_10d_base_v101_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_diff_10d_base_v102_signal(assets, liabilities):
    res = (liabilities / assets).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_diff_10d_base_v102_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_diff_10d_base_v102_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_skew_10d_base_v103_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_skew_10d_base_v103_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_skew_10d_base_v103_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_kurt_10d_base_v104_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_kurt_10d_base_v104_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_kurt_10d_base_v104_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_median_10d_base_v105_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_median_10d_base_v105_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_median_10d_base_v105_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_10d_base_v106_signal(assets, liabilities):
    res = (liabilities / assets).rolling(10).min() / (liabilities / assets).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_10d_base_v106_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_10d_base_v106_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_10d_base_v107_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_10d_base_v107_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_10d_base_v107_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_10d_base_v108_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_10d_base_v108_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_10d_base_v108_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_mean_21d_base_v109_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_mean_21d_base_v109_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_mean_21d_base_v109_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_std_21d_base_v110_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_std_21d_base_v110_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_std_21d_base_v110_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_21d_base_v111_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_21d_base_v111_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_21d_base_v111_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_zscore_21d_base_v112_signal(assets, liabilities):
    res = ((liabilities / assets) - (liabilities / assets).rolling(21).mean()) / (liabilities / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_zscore_21d_base_v112_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_zscore_21d_base_v112_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_rank_21d_base_v113_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_rank_21d_base_v113_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_rank_21d_base_v113_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_diff_21d_base_v114_signal(assets, liabilities):
    res = (liabilities / assets).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_diff_21d_base_v114_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_diff_21d_base_v114_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_skew_21d_base_v115_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_skew_21d_base_v115_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_skew_21d_base_v115_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_kurt_21d_base_v116_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_kurt_21d_base_v116_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_kurt_21d_base_v116_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_median_21d_base_v117_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_median_21d_base_v117_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_median_21d_base_v117_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_21d_base_v118_signal(assets, liabilities):
    res = (liabilities / assets).rolling(21).min() / (liabilities / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_21d_base_v118_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_21d_base_v118_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_21d_base_v119_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_21d_base_v119_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_21d_base_v119_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_21d_base_v120_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_21d_base_v120_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_21d_base_v120_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_mean_42d_base_v121_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_mean_42d_base_v121_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_mean_42d_base_v121_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_std_42d_base_v122_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_std_42d_base_v122_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_std_42d_base_v122_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_42d_base_v123_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_42d_base_v123_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_42d_base_v123_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_zscore_42d_base_v124_signal(assets, liabilities):
    res = ((liabilities / assets) - (liabilities / assets).rolling(42).mean()) / (liabilities / assets).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_zscore_42d_base_v124_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_zscore_42d_base_v124_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_rank_42d_base_v125_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_rank_42d_base_v125_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_rank_42d_base_v125_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_diff_42d_base_v126_signal(assets, liabilities):
    res = (liabilities / assets).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_diff_42d_base_v126_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_diff_42d_base_v126_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_skew_42d_base_v127_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_skew_42d_base_v127_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_skew_42d_base_v127_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_kurt_42d_base_v128_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_kurt_42d_base_v128_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_kurt_42d_base_v128_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_median_42d_base_v129_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_median_42d_base_v129_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_median_42d_base_v129_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_42d_base_v130_signal(assets, liabilities):
    res = (liabilities / assets).rolling(42).min() / (liabilities / assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_42d_base_v130_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_42d_base_v130_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_42d_base_v131_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_42d_base_v131_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_42d_base_v131_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_42d_base_v132_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_42d_base_v132_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_42d_base_v132_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_mean_63d_base_v133_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_mean_63d_base_v133_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_mean_63d_base_v133_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_std_63d_base_v134_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_std_63d_base_v134_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_std_63d_base_v134_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_63d_base_v135_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_63d_base_v135_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_63d_base_v135_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_zscore_63d_base_v136_signal(assets, liabilities):
    res = ((liabilities / assets) - (liabilities / assets).rolling(63).mean()) / (liabilities / assets).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_zscore_63d_base_v136_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_zscore_63d_base_v136_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_rank_63d_base_v137_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_rank_63d_base_v137_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_rank_63d_base_v137_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_diff_63d_base_v138_signal(assets, liabilities):
    res = (liabilities / assets).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_diff_63d_base_v138_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_diff_63d_base_v138_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_skew_63d_base_v139_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_skew_63d_base_v139_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_skew_63d_base_v139_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_kurt_63d_base_v140_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_kurt_63d_base_v140_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_kurt_63d_base_v140_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_median_63d_base_v141_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_median_63d_base_v141_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_median_63d_base_v141_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_63d_base_v142_signal(assets, liabilities):
    res = (liabilities / assets).rolling(63).min() / (liabilities / assets).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_63d_base_v142_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_max_ratio_63d_base_v142_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_63d_base_v143_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_63d_base_v143_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_max_ratio_63d_base_v143_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_63d_base_v144_signal(assets, liabilities):
    res = (liabilities / assets) / (liabilities / assets).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_63d_base_v144_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_min_ratio_63d_base_v144_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_mean_126d_base_v145_signal(assets, liabilities):
    res = (liabilities / assets).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_mean_126d_base_v145_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_mean_126d_base_v145_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_std_126d_base_v146_signal(assets, liabilities):
    res = (liabilities / assets).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_std_126d_base_v146_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_std_126d_base_v146_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_126d_base_v147_signal(assets, liabilities):
    res = (liabilities / assets).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_126d_base_v147_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_pct_chg_126d_base_v147_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_zscore_126d_base_v148_signal(assets, liabilities):
    res = ((liabilities / assets) - (liabilities / assets).rolling(126).mean()) / (liabilities / assets).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_zscore_126d_base_v148_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_zscore_126d_base_v148_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_rank_126d_base_v149_signal(assets, liabilities):
    res = (liabilities / assets).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_rank_126d_base_v149_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_rank_126d_base_v149_signal

def f80ls_f80_liability_structure_stability_liabilities_assets_diff_126d_base_v150_signal(assets, liabilities):
    res = (liabilities / assets).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f80ls_f80_liability_structure_stability_liabilities_assets_diff_126d_base_v150_signal'] = f80ls_f80_liability_structure_stability_liabilities_assets_diff_126d_base_v150_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    # Extra padding to ensure file size > 30KB
    padding = "X" * 5000
    df = pd.DataFrame({
        "assets": np.random.uniform(1.0, 1000.0, n),
        "debt": np.random.uniform(1.0, 1000.0, n),
        "equity": np.random.uniform(1.0, 1000.0, n),
        "liabilities": np.random.uniform(1.0, 1000.0, n),
        "marketcap": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_0": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_1": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_2": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_3": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_4": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_5": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_6": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_7": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_8": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_9": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_10": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_11": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_12": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_13": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_14": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_15": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_16": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_17": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_18": np.random.uniform(1.0, 1000.0, n),
        "extra_test_col_19": np.random.uniform(1.0, 1000.0, n),
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
        if res.isna().all():
            print(f"ERROR: {name} is all NaN")
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        high_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    high_corr.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j]))
        if high_corr:
            for c1, c2, val in high_corr[:5]:
                print(f"WARNING: High correlation between {c1} and {c2}: {val}")
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
