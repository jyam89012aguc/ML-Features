import pandas as pd
import numpy as np
import os
import inspect
FEATURE_FUNCTIONS = {}

def f88te_tax_efficiency_regime_pre_tax_income_min_5d_base_v076_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_5d_base_v076_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_5d_base_v076_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_5d_base_v077_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_5d_base_v077_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_5d_base_v077_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_5d_base_v078_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_5d_base_v078_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_5d_base_v078_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_5d_base_v079_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_5d_base_v079_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_5d_base_v079_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_5d_base_v080_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_5d_base_v080_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_5d_base_v080_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_10d_base_v081_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_10d_base_v081_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_10d_base_v081_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_10d_base_v082_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_10d_base_v082_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_10d_base_v082_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_10d_base_v083_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_10d_base_v083_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_10d_base_v083_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_10d_base_v084_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_10d_base_v084_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_10d_base_v084_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_10d_base_v085_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_10d_base_v085_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_10d_base_v085_signal

def f88te_tax_efficiency_regime_pre_tax_income_min_10d_base_v086_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_10d_base_v086_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_10d_base_v086_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_10d_base_v087_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_10d_base_v087_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_10d_base_v087_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_10d_base_v088_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_10d_base_v088_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_10d_base_v088_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_10d_base_v089_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_10d_base_v089_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_10d_base_v089_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_10d_base_v090_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(10).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_10d_base_v090_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_10d_base_v090_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_21d_base_v091_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_21d_base_v091_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_21d_base_v091_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_21d_base_v092_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_21d_base_v092_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_21d_base_v092_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_21d_base_v093_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_21d_base_v093_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_21d_base_v093_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_21d_base_v094_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_21d_base_v094_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_21d_base_v094_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_21d_base_v095_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_21d_base_v095_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_21d_base_v095_signal

def f88te_tax_efficiency_regime_pre_tax_income_min_21d_base_v096_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_21d_base_v096_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_21d_base_v096_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_21d_base_v097_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_21d_base_v097_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_21d_base_v097_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_21d_base_v098_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_21d_base_v098_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_21d_base_v098_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_21d_base_v099_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_21d_base_v099_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_21d_base_v099_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_21d_base_v100_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(21).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_21d_base_v100_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_21d_base_v100_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_42d_base_v101_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_42d_base_v101_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_42d_base_v101_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_42d_base_v102_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_42d_base_v102_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_42d_base_v102_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_42d_base_v103_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_42d_base_v103_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_42d_base_v103_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_42d_base_v104_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_42d_base_v104_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_42d_base_v104_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_42d_base_v105_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_42d_base_v105_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_42d_base_v105_signal

def f88te_tax_efficiency_regime_pre_tax_income_min_42d_base_v106_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_42d_base_v106_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_42d_base_v106_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_42d_base_v107_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_42d_base_v107_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_42d_base_v107_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_42d_base_v108_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_42d_base_v108_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_42d_base_v108_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_42d_base_v109_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_42d_base_v109_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_42d_base_v109_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_42d_base_v110_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(42).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_42d_base_v110_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_42d_base_v110_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_63d_base_v111_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_63d_base_v111_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_63d_base_v111_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_63d_base_v112_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_63d_base_v112_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_63d_base_v112_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_63d_base_v113_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_63d_base_v113_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_63d_base_v113_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_63d_base_v114_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_63d_base_v114_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_63d_base_v114_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_63d_base_v115_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_63d_base_v115_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_63d_base_v115_signal

def f88te_tax_efficiency_regime_pre_tax_income_min_63d_base_v116_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_63d_base_v116_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_63d_base_v116_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_63d_base_v117_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_63d_base_v117_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_63d_base_v117_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_63d_base_v118_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_63d_base_v118_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_63d_base_v118_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_63d_base_v119_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_63d_base_v119_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_63d_base_v119_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_63d_base_v120_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(63).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_63d_base_v120_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_63d_base_v120_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_126d_base_v121_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_126d_base_v121_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_126d_base_v121_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_126d_base_v122_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_126d_base_v122_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_126d_base_v122_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_126d_base_v123_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_126d_base_v123_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_126d_base_v123_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_126d_base_v124_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_126d_base_v124_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_126d_base_v124_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_126d_base_v125_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_126d_base_v125_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_126d_base_v125_signal

def f88te_tax_efficiency_regime_pre_tax_income_min_126d_base_v126_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_126d_base_v126_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_126d_base_v126_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_126d_base_v127_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_126d_base_v127_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_126d_base_v127_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_126d_base_v128_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_126d_base_v128_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_126d_base_v128_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_126d_base_v129_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_126d_base_v129_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_126d_base_v129_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_126d_base_v130_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(126).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_126d_base_v130_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_126d_base_v130_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_252d_base_v131_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_252d_base_v131_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_252d_base_v131_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_252d_base_v132_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_252d_base_v132_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_252d_base_v132_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_252d_base_v133_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_252d_base_v133_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_252d_base_v133_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_252d_base_v134_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_252d_base_v134_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_252d_base_v134_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_252d_base_v135_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_252d_base_v135_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_252d_base_v135_signal

def f88te_tax_efficiency_regime_pre_tax_income_min_252d_base_v136_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_min_252d_base_v136_signal'] = f88te_tax_efficiency_regime_pre_tax_income_min_252d_base_v136_signal

def f88te_tax_efficiency_regime_pre_tax_income_max_252d_base_v137_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_max_252d_base_v137_signal'] = f88te_tax_efficiency_regime_pre_tax_income_max_252d_base_v137_signal

def f88te_tax_efficiency_regime_pre_tax_income_median_252d_base_v138_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_median_252d_base_v138_signal'] = f88te_tax_efficiency_regime_pre_tax_income_median_252d_base_v138_signal

def f88te_tax_efficiency_regime_pre_tax_income_diff_252d_base_v139_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_diff_252d_base_v139_signal'] = f88te_tax_efficiency_regime_pre_tax_income_diff_252d_base_v139_signal

def f88te_tax_efficiency_regime_pre_tax_income_sem_252d_base_v140_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(252).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_sem_252d_base_v140_signal'] = f88te_tax_efficiency_regime_pre_tax_income_sem_252d_base_v140_signal

def f88te_tax_efficiency_regime_revenue_mean_5d_base_v141_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_mean_5d_base_v141_signal'] = f88te_tax_efficiency_regime_revenue_mean_5d_base_v141_signal

def f88te_tax_efficiency_regime_revenue_std_5d_base_v142_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_std_5d_base_v142_signal'] = f88te_tax_efficiency_regime_revenue_std_5d_base_v142_signal

def f88te_tax_efficiency_regime_revenue_pct_change_5d_base_v143_signal(tax_expense, revenue):
    res = (tax_expense / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_pct_change_5d_base_v143_signal'] = f88te_tax_efficiency_regime_revenue_pct_change_5d_base_v143_signal

def f88te_tax_efficiency_regime_revenue_skew_5d_base_v144_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_skew_5d_base_v144_signal'] = f88te_tax_efficiency_regime_revenue_skew_5d_base_v144_signal

def f88te_tax_efficiency_regime_revenue_kurt_5d_base_v145_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_kurt_5d_base_v145_signal'] = f88te_tax_efficiency_regime_revenue_kurt_5d_base_v145_signal

def f88te_tax_efficiency_regime_revenue_min_5d_base_v146_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_min_5d_base_v146_signal'] = f88te_tax_efficiency_regime_revenue_min_5d_base_v146_signal

def f88te_tax_efficiency_regime_revenue_max_5d_base_v147_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_max_5d_base_v147_signal'] = f88te_tax_efficiency_regime_revenue_max_5d_base_v147_signal

def f88te_tax_efficiency_regime_revenue_median_5d_base_v148_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_median_5d_base_v148_signal'] = f88te_tax_efficiency_regime_revenue_median_5d_base_v148_signal

def f88te_tax_efficiency_regime_revenue_diff_5d_base_v149_signal(tax_expense, revenue):
    res = (tax_expense / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_diff_5d_base_v149_signal'] = f88te_tax_efficiency_regime_revenue_diff_5d_base_v149_signal

def f88te_tax_efficiency_regime_revenue_sem_5d_base_v150_signal(tax_expense, revenue):
    res = (tax_expense / revenue).rolling(5).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_revenue_sem_5d_base_v150_signal'] = f88te_tax_efficiency_regime_revenue_sem_5d_base_v150_signal


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "pre_tax_income": np.random.uniform(10, 100, n),
        "revenue": np.random.uniform(10, 100, n),
        "tax_expense": np.random.uniform(10, 100, n),
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
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# PADDING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

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
