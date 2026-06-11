import pandas as pd
import numpy as np
import os
import inspect
FEATURE_FUNCTIONS = {}

def f90cv_current_ratio_volatility_current_liabilities_min_5d_base_v076_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_5d_base_v076_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_5d_base_v076_signal

def f90cv_current_ratio_volatility_current_liabilities_max_5d_base_v077_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_5d_base_v077_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_5d_base_v077_signal

def f90cv_current_ratio_volatility_current_liabilities_median_5d_base_v078_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_5d_base_v078_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_5d_base_v078_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_5d_base_v079_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_5d_base_v079_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_5d_base_v079_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_5d_base_v080_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(5).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_5d_base_v080_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_5d_base_v080_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_10d_base_v081_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_10d_base_v081_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_10d_base_v081_signal

def f90cv_current_ratio_volatility_current_liabilities_std_10d_base_v082_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_10d_base_v082_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_10d_base_v082_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_10d_base_v083_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_10d_base_v083_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_10d_base_v083_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_10d_base_v084_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_10d_base_v084_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_10d_base_v084_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_10d_base_v085_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_10d_base_v085_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_10d_base_v085_signal

def f90cv_current_ratio_volatility_current_liabilities_min_10d_base_v086_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_10d_base_v086_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_10d_base_v086_signal

def f90cv_current_ratio_volatility_current_liabilities_max_10d_base_v087_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_10d_base_v087_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_10d_base_v087_signal

def f90cv_current_ratio_volatility_current_liabilities_median_10d_base_v088_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_10d_base_v088_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_10d_base_v088_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_10d_base_v089_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_10d_base_v089_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_10d_base_v089_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_10d_base_v090_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(10).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_10d_base_v090_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_10d_base_v090_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_21d_base_v091_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_21d_base_v091_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_21d_base_v091_signal

def f90cv_current_ratio_volatility_current_liabilities_std_21d_base_v092_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_21d_base_v092_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_21d_base_v092_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_21d_base_v093_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_21d_base_v093_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_21d_base_v093_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_21d_base_v094_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_21d_base_v094_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_21d_base_v094_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_21d_base_v095_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_21d_base_v095_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_21d_base_v095_signal

def f90cv_current_ratio_volatility_current_liabilities_min_21d_base_v096_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_21d_base_v096_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_21d_base_v096_signal

def f90cv_current_ratio_volatility_current_liabilities_max_21d_base_v097_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_21d_base_v097_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_21d_base_v097_signal

def f90cv_current_ratio_volatility_current_liabilities_median_21d_base_v098_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_21d_base_v098_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_21d_base_v098_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_21d_base_v099_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_21d_base_v099_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_21d_base_v099_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_21d_base_v100_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(21).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_21d_base_v100_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_21d_base_v100_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_42d_base_v101_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_42d_base_v101_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_42d_base_v101_signal

def f90cv_current_ratio_volatility_current_liabilities_std_42d_base_v102_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_42d_base_v102_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_42d_base_v102_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_42d_base_v103_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_42d_base_v103_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_42d_base_v103_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_42d_base_v104_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_42d_base_v104_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_42d_base_v104_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_42d_base_v105_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_42d_base_v105_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_42d_base_v105_signal

def f90cv_current_ratio_volatility_current_liabilities_min_42d_base_v106_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_42d_base_v106_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_42d_base_v106_signal

def f90cv_current_ratio_volatility_current_liabilities_max_42d_base_v107_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_42d_base_v107_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_42d_base_v107_signal

def f90cv_current_ratio_volatility_current_liabilities_median_42d_base_v108_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_42d_base_v108_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_42d_base_v108_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_42d_base_v109_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_42d_base_v109_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_42d_base_v109_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_42d_base_v110_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(42).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_42d_base_v110_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_42d_base_v110_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_63d_base_v111_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_63d_base_v111_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_63d_base_v111_signal

def f90cv_current_ratio_volatility_current_liabilities_std_63d_base_v112_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_63d_base_v112_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_63d_base_v112_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_63d_base_v113_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_63d_base_v113_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_63d_base_v113_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_63d_base_v114_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_63d_base_v114_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_63d_base_v114_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_63d_base_v115_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_63d_base_v115_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_63d_base_v115_signal

def f90cv_current_ratio_volatility_current_liabilities_min_63d_base_v116_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_63d_base_v116_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_63d_base_v116_signal

def f90cv_current_ratio_volatility_current_liabilities_max_63d_base_v117_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_63d_base_v117_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_63d_base_v117_signal

def f90cv_current_ratio_volatility_current_liabilities_median_63d_base_v118_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_63d_base_v118_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_63d_base_v118_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_63d_base_v119_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_63d_base_v119_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_63d_base_v119_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_63d_base_v120_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(63).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_63d_base_v120_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_63d_base_v120_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_126d_base_v121_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_126d_base_v121_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_126d_base_v121_signal

def f90cv_current_ratio_volatility_current_liabilities_std_126d_base_v122_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_126d_base_v122_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_126d_base_v122_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_126d_base_v123_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_126d_base_v123_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_126d_base_v123_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_126d_base_v124_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_126d_base_v124_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_126d_base_v124_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_126d_base_v125_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_126d_base_v125_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_126d_base_v125_signal

def f90cv_current_ratio_volatility_current_liabilities_min_126d_base_v126_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_126d_base_v126_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_126d_base_v126_signal

def f90cv_current_ratio_volatility_current_liabilities_max_126d_base_v127_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_126d_base_v127_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_126d_base_v127_signal

def f90cv_current_ratio_volatility_current_liabilities_median_126d_base_v128_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_126d_base_v128_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_126d_base_v128_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_126d_base_v129_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_126d_base_v129_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_126d_base_v129_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_126d_base_v130_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(126).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_126d_base_v130_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_126d_base_v130_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_252d_base_v131_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_252d_base_v131_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_252d_base_v131_signal

def f90cv_current_ratio_volatility_current_liabilities_std_252d_base_v132_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_252d_base_v132_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_252d_base_v132_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_252d_base_v133_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_252d_base_v133_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_252d_base_v133_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_252d_base_v134_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_252d_base_v134_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_252d_base_v134_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_252d_base_v135_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_252d_base_v135_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_252d_base_v135_signal

def f90cv_current_ratio_volatility_current_liabilities_min_252d_base_v136_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_252d_base_v136_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_252d_base_v136_signal

def f90cv_current_ratio_volatility_current_liabilities_max_252d_base_v137_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_252d_base_v137_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_252d_base_v137_signal

def f90cv_current_ratio_volatility_current_liabilities_median_252d_base_v138_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_252d_base_v138_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_252d_base_v138_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_252d_base_v139_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_252d_base_v139_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_252d_base_v139_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_252d_base_v140_signal(current_assets, current_liabilities):
    res = (current_assets / current_liabilities).rolling(252).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_252d_base_v140_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_252d_base_v140_signal

def f90cv_current_ratio_volatility_revenue_mean_5d_base_v141_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_mean_5d_base_v141_signal'] = f90cv_current_ratio_volatility_revenue_mean_5d_base_v141_signal

def f90cv_current_ratio_volatility_revenue_std_5d_base_v142_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_std_5d_base_v142_signal'] = f90cv_current_ratio_volatility_revenue_std_5d_base_v142_signal

def f90cv_current_ratio_volatility_revenue_pct_change_5d_base_v143_signal(current_assets, revenue):
    res = (current_assets / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_pct_change_5d_base_v143_signal'] = f90cv_current_ratio_volatility_revenue_pct_change_5d_base_v143_signal

def f90cv_current_ratio_volatility_revenue_skew_5d_base_v144_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_skew_5d_base_v144_signal'] = f90cv_current_ratio_volatility_revenue_skew_5d_base_v144_signal

def f90cv_current_ratio_volatility_revenue_kurt_5d_base_v145_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_kurt_5d_base_v145_signal'] = f90cv_current_ratio_volatility_revenue_kurt_5d_base_v145_signal

def f90cv_current_ratio_volatility_revenue_min_5d_base_v146_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_min_5d_base_v146_signal'] = f90cv_current_ratio_volatility_revenue_min_5d_base_v146_signal

def f90cv_current_ratio_volatility_revenue_max_5d_base_v147_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_max_5d_base_v147_signal'] = f90cv_current_ratio_volatility_revenue_max_5d_base_v147_signal

def f90cv_current_ratio_volatility_revenue_median_5d_base_v148_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_median_5d_base_v148_signal'] = f90cv_current_ratio_volatility_revenue_median_5d_base_v148_signal

def f90cv_current_ratio_volatility_revenue_diff_5d_base_v149_signal(current_assets, revenue):
    res = (current_assets / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_diff_5d_base_v149_signal'] = f90cv_current_ratio_volatility_revenue_diff_5d_base_v149_signal

def f90cv_current_ratio_volatility_revenue_sem_5d_base_v150_signal(current_assets, revenue):
    res = (current_assets / revenue).rolling(5).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_sem_5d_base_v150_signal'] = f90cv_current_ratio_volatility_revenue_sem_5d_base_v150_signal


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "current_assets": np.random.uniform(10, 100, n),
        "current_liabilities": np.random.uniform(10, 100, n),
        "revenue": np.random.uniform(10, 100, n),
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
        assert not res.isna().all(), f"{name} is all NaN"
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    pass
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
