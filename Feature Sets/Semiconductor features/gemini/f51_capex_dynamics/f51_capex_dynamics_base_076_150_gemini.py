import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f51cd_f51_capex_dynamics_ebitda_min_ratio_21d_base_v076_signal(capex, ebitda):
    res = (capex / ebitda) / (capex / ebitda).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_min_ratio_21d_base_v076_signal'] = f51cd_f51_capex_dynamics_ebitda_min_ratio_21d_base_v076_signal

def f51cd_f51_capex_dynamics_equity_min_ratio_21d_base_v077_signal(capex, equity):
    res = (capex / equity) / (capex / equity).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_min_ratio_21d_base_v077_signal'] = f51cd_f51_capex_dynamics_equity_min_ratio_21d_base_v077_signal

def f51cd_f51_capex_dynamics_debt_min_ratio_21d_base_v078_signal(capex, debt):
    res = (capex / debt) / (capex / debt).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_min_ratio_21d_base_v078_signal'] = f51cd_f51_capex_dynamics_debt_min_ratio_21d_base_v078_signal

def f51cd_f51_capex_dynamics_closeadj_min_ratio_21d_base_v079_signal(capex, closeadj):
    res = (capex / closeadj) / (capex / closeadj).rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_min_ratio_21d_base_v079_signal'] = f51cd_f51_capex_dynamics_closeadj_min_ratio_21d_base_v079_signal

def f51cd_f51_capex_dynamics_capex_min_ratio_21d_base_v080_signal(capex):
    res = capex / capex.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_min_ratio_21d_base_v080_signal'] = f51cd_f51_capex_dynamics_capex_min_ratio_21d_base_v080_signal

def f51cd_f51_capex_dynamics_revenue_cv_21d_base_v081_signal(capex, revenue):
    res = (capex / revenue).rolling(21).std() / (capex / revenue).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_cv_21d_base_v081_signal'] = f51cd_f51_capex_dynamics_revenue_cv_21d_base_v081_signal

def f51cd_f51_capex_dynamics_assets_cv_21d_base_v082_signal(capex, assets):
    res = (capex / assets).rolling(21).std() / (capex / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_cv_21d_base_v082_signal'] = f51cd_f51_capex_dynamics_assets_cv_21d_base_v082_signal

def f51cd_f51_capex_dynamics_ebitda_cv_21d_base_v083_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).std() / (capex / ebitda).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_cv_21d_base_v083_signal'] = f51cd_f51_capex_dynamics_ebitda_cv_21d_base_v083_signal

def f51cd_f51_capex_dynamics_equity_cv_21d_base_v084_signal(capex, equity):
    res = (capex / equity).rolling(21).std() / (capex / equity).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_cv_21d_base_v084_signal'] = f51cd_f51_capex_dynamics_equity_cv_21d_base_v084_signal

def f51cd_f51_capex_dynamics_debt_cv_21d_base_v085_signal(capex, debt):
    res = (capex / debt).rolling(21).std() / (capex / debt).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_cv_21d_base_v085_signal'] = f51cd_f51_capex_dynamics_debt_cv_21d_base_v085_signal

def f51cd_f51_capex_dynamics_closeadj_cv_21d_base_v086_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).std() / (capex / closeadj).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_cv_21d_base_v086_signal'] = f51cd_f51_capex_dynamics_closeadj_cv_21d_base_v086_signal

def f51cd_f51_capex_dynamics_capex_cv_21d_base_v087_signal(capex):
    res = capex.rolling(21).std() / capex.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_cv_21d_base_v087_signal'] = f51cd_f51_capex_dynamics_capex_cv_21d_base_v087_signal

def f51cd_f51_capex_dynamics_revenue_q25_21d_base_v088_signal(capex, revenue):
    res = (capex / revenue).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q25_21d_base_v088_signal'] = f51cd_f51_capex_dynamics_revenue_q25_21d_base_v088_signal

def f51cd_f51_capex_dynamics_assets_q25_21d_base_v089_signal(capex, assets):
    res = (capex / assets).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q25_21d_base_v089_signal'] = f51cd_f51_capex_dynamics_assets_q25_21d_base_v089_signal

def f51cd_f51_capex_dynamics_ebitda_q25_21d_base_v090_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q25_21d_base_v090_signal'] = f51cd_f51_capex_dynamics_ebitda_q25_21d_base_v090_signal

def f51cd_f51_capex_dynamics_equity_q25_21d_base_v091_signal(capex, equity):
    res = (capex / equity).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q25_21d_base_v091_signal'] = f51cd_f51_capex_dynamics_equity_q25_21d_base_v091_signal

def f51cd_f51_capex_dynamics_debt_q25_21d_base_v092_signal(capex, debt):
    res = (capex / debt).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q25_21d_base_v092_signal'] = f51cd_f51_capex_dynamics_debt_q25_21d_base_v092_signal

def f51cd_f51_capex_dynamics_closeadj_q25_21d_base_v093_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q25_21d_base_v093_signal'] = f51cd_f51_capex_dynamics_closeadj_q25_21d_base_v093_signal

def f51cd_f51_capex_dynamics_capex_q25_21d_base_v094_signal(capex):
    res = capex.rolling(21).quantile(0.25)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q25_21d_base_v094_signal'] = f51cd_f51_capex_dynamics_capex_q25_21d_base_v094_signal

def f51cd_f51_capex_dynamics_revenue_q75_21d_base_v095_signal(capex, revenue):
    res = (capex / revenue).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q75_21d_base_v095_signal'] = f51cd_f51_capex_dynamics_revenue_q75_21d_base_v095_signal

def f51cd_f51_capex_dynamics_assets_q75_21d_base_v096_signal(capex, assets):
    res = (capex / assets).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q75_21d_base_v096_signal'] = f51cd_f51_capex_dynamics_assets_q75_21d_base_v096_signal

def f51cd_f51_capex_dynamics_ebitda_q75_21d_base_v097_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q75_21d_base_v097_signal'] = f51cd_f51_capex_dynamics_ebitda_q75_21d_base_v097_signal

def f51cd_f51_capex_dynamics_equity_q75_21d_base_v098_signal(capex, equity):
    res = (capex / equity).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q75_21d_base_v098_signal'] = f51cd_f51_capex_dynamics_equity_q75_21d_base_v098_signal

def f51cd_f51_capex_dynamics_debt_q75_21d_base_v099_signal(capex, debt):
    res = (capex / debt).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q75_21d_base_v099_signal'] = f51cd_f51_capex_dynamics_debt_q75_21d_base_v099_signal

def f51cd_f51_capex_dynamics_closeadj_q75_21d_base_v100_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q75_21d_base_v100_signal'] = f51cd_f51_capex_dynamics_closeadj_q75_21d_base_v100_signal

def f51cd_f51_capex_dynamics_capex_q75_21d_base_v101_signal(capex):
    res = capex.rolling(21).quantile(0.75)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q75_21d_base_v101_signal'] = f51cd_f51_capex_dynamics_capex_q75_21d_base_v101_signal

def f51cd_f51_capex_dynamics_revenue_q10_21d_base_v102_signal(capex, revenue):
    res = (capex / revenue).rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q10_21d_base_v102_signal'] = f51cd_f51_capex_dynamics_revenue_q10_21d_base_v102_signal

def f51cd_f51_capex_dynamics_assets_q10_21d_base_v103_signal(capex, assets):
    res = (capex / assets).rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q10_21d_base_v103_signal'] = f51cd_f51_capex_dynamics_assets_q10_21d_base_v103_signal

def f51cd_f51_capex_dynamics_ebitda_q10_21d_base_v104_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q10_21d_base_v104_signal'] = f51cd_f51_capex_dynamics_ebitda_q10_21d_base_v104_signal

def f51cd_f51_capex_dynamics_equity_q10_21d_base_v105_signal(capex, equity):
    res = (capex / equity).rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q10_21d_base_v105_signal'] = f51cd_f51_capex_dynamics_equity_q10_21d_base_v105_signal

def f51cd_f51_capex_dynamics_debt_q10_21d_base_v106_signal(capex, debt):
    res = (capex / debt).rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q10_21d_base_v106_signal'] = f51cd_f51_capex_dynamics_debt_q10_21d_base_v106_signal

def f51cd_f51_capex_dynamics_closeadj_q10_21d_base_v107_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q10_21d_base_v107_signal'] = f51cd_f51_capex_dynamics_closeadj_q10_21d_base_v107_signal

def f51cd_f51_capex_dynamics_capex_q10_21d_base_v108_signal(capex):
    res = capex.rolling(21).quantile(0.10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q10_21d_base_v108_signal'] = f51cd_f51_capex_dynamics_capex_q10_21d_base_v108_signal

def f51cd_f51_capex_dynamics_revenue_q90_21d_base_v109_signal(capex, revenue):
    res = (capex / revenue).rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_q90_21d_base_v109_signal'] = f51cd_f51_capex_dynamics_revenue_q90_21d_base_v109_signal

def f51cd_f51_capex_dynamics_assets_q90_21d_base_v110_signal(capex, assets):
    res = (capex / assets).rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_q90_21d_base_v110_signal'] = f51cd_f51_capex_dynamics_assets_q90_21d_base_v110_signal

def f51cd_f51_capex_dynamics_ebitda_q90_21d_base_v111_signal(capex, ebitda):
    res = (capex / ebitda).rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_q90_21d_base_v111_signal'] = f51cd_f51_capex_dynamics_ebitda_q90_21d_base_v111_signal

def f51cd_f51_capex_dynamics_equity_q90_21d_base_v112_signal(capex, equity):
    res = (capex / equity).rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_q90_21d_base_v112_signal'] = f51cd_f51_capex_dynamics_equity_q90_21d_base_v112_signal

def f51cd_f51_capex_dynamics_debt_q90_21d_base_v113_signal(capex, debt):
    res = (capex / debt).rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_q90_21d_base_v113_signal'] = f51cd_f51_capex_dynamics_debt_q90_21d_base_v113_signal

def f51cd_f51_capex_dynamics_closeadj_q90_21d_base_v114_signal(capex, closeadj):
    res = (capex / closeadj).rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_q90_21d_base_v114_signal'] = f51cd_f51_capex_dynamics_closeadj_q90_21d_base_v114_signal

def f51cd_f51_capex_dynamics_capex_q90_21d_base_v115_signal(capex):
    res = capex.rolling(21).quantile(0.90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_q90_21d_base_v115_signal'] = f51cd_f51_capex_dynamics_capex_q90_21d_base_v115_signal

def f51cd_f51_capex_dynamics_revenue_range_21d_base_v116_signal(capex, revenue):
    res = ((capex / revenue).rolling(21).max() - (capex / revenue).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_range_21d_base_v116_signal'] = f51cd_f51_capex_dynamics_revenue_range_21d_base_v116_signal

def f51cd_f51_capex_dynamics_assets_range_21d_base_v117_signal(capex, assets):
    res = ((capex / assets).rolling(21).max() - (capex / assets).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_range_21d_base_v117_signal'] = f51cd_f51_capex_dynamics_assets_range_21d_base_v117_signal

def f51cd_f51_capex_dynamics_ebitda_range_21d_base_v118_signal(capex, ebitda):
    res = ((capex / ebitda).rolling(21).max() - (capex / ebitda).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_range_21d_base_v118_signal'] = f51cd_f51_capex_dynamics_ebitda_range_21d_base_v118_signal

def f51cd_f51_capex_dynamics_equity_range_21d_base_v119_signal(capex, equity):
    res = ((capex / equity).rolling(21).max() - (capex / equity).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_range_21d_base_v119_signal'] = f51cd_f51_capex_dynamics_equity_range_21d_base_v119_signal

def f51cd_f51_capex_dynamics_debt_range_21d_base_v120_signal(capex, debt):
    res = ((capex / debt).rolling(21).max() - (capex / debt).rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_range_21d_base_v120_signal'] = f51cd_f51_capex_dynamics_debt_range_21d_base_v120_signal

def f51cd_f51_capex_dynamics_closeadj_range_63d_base_v121_signal(capex, closeadj):
    res = ((capex / closeadj).rolling(63).max() - (capex / closeadj).rolling(63).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_range_63d_base_v121_signal'] = f51cd_f51_capex_dynamics_closeadj_range_63d_base_v121_signal

def f51cd_f51_capex_dynamics_capex_range_21d_base_v122_signal(capex):
    res = (capex.rolling(21).max() - capex.rolling(21).min())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_range_21d_base_v122_signal'] = f51cd_f51_capex_dynamics_capex_range_21d_base_v122_signal

def f51cd_f51_capex_dynamics_revenue_abs_diff_mean_21d_base_v123_signal(capex, revenue):
    res = ((capex / revenue) - (capex / revenue).rolling(21).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_abs_diff_mean_21d_base_v123_signal'] = f51cd_f51_capex_dynamics_revenue_abs_diff_mean_21d_base_v123_signal

def f51cd_f51_capex_dynamics_assets_abs_diff_mean_21d_base_v124_signal(capex, assets):
    res = ((capex / assets) - (capex / assets).rolling(21).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_abs_diff_mean_21d_base_v124_signal'] = f51cd_f51_capex_dynamics_assets_abs_diff_mean_21d_base_v124_signal

def f51cd_f51_capex_dynamics_ebitda_abs_diff_mean_21d_base_v125_signal(capex, ebitda):
    res = ((capex / ebitda) - (capex / ebitda).rolling(21).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_abs_diff_mean_21d_base_v125_signal'] = f51cd_f51_capex_dynamics_ebitda_abs_diff_mean_21d_base_v125_signal

def f51cd_f51_capex_dynamics_equity_abs_diff_mean_21d_base_v126_signal(capex, equity):
    res = ((capex / equity) - (capex / equity).rolling(21).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_abs_diff_mean_21d_base_v126_signal'] = f51cd_f51_capex_dynamics_equity_abs_diff_mean_21d_base_v126_signal

def f51cd_f51_capex_dynamics_debt_abs_diff_mean_21d_base_v127_signal(capex, debt):
    res = ((capex / debt) - (capex / debt).rolling(21).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_abs_diff_mean_21d_base_v127_signal'] = f51cd_f51_capex_dynamics_debt_abs_diff_mean_21d_base_v127_signal

def f51cd_f51_capex_dynamics_closeadj_abs_diff_mean_63d_base_v128_signal(capex, closeadj):
    res = ((capex / closeadj) - (capex / closeadj).rolling(63).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_abs_diff_mean_63d_base_v128_signal'] = f51cd_f51_capex_dynamics_closeadj_abs_diff_mean_63d_base_v128_signal

def f51cd_f51_capex_dynamics_capex_abs_diff_mean_21d_base_v129_signal(capex):
    res = (capex - capex.rolling(21).mean()).abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_abs_diff_mean_21d_base_v129_signal'] = f51cd_f51_capex_dynamics_capex_abs_diff_mean_21d_base_v129_signal

def f51cd_f51_capex_dynamics_revenue_sq_mean_63d_base_v130_signal(capex, revenue):
    res = ((capex / revenue)**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_sq_mean_63d_base_v130_signal'] = f51cd_f51_capex_dynamics_revenue_sq_mean_63d_base_v130_signal

def f51cd_f51_capex_dynamics_assets_sq_mean_63d_base_v131_signal(capex, assets):
    res = ((capex / assets)**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_sq_mean_63d_base_v131_signal'] = f51cd_f51_capex_dynamics_assets_sq_mean_63d_base_v131_signal

def f51cd_f51_capex_dynamics_ebitda_sq_mean_63d_base_v132_signal(capex, ebitda):
    res = ((capex / ebitda)**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_sq_mean_63d_base_v132_signal'] = f51cd_f51_capex_dynamics_ebitda_sq_mean_63d_base_v132_signal

def f51cd_f51_capex_dynamics_equity_sq_mean_63d_base_v133_signal(capex, equity):
    res = ((capex / equity)**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_sq_mean_63d_base_v133_signal'] = f51cd_f51_capex_dynamics_equity_sq_mean_63d_base_v133_signal

def f51cd_f51_capex_dynamics_debt_sq_mean_63d_base_v134_signal(capex, debt):
    res = ((capex / debt)**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_sq_mean_63d_base_v134_signal'] = f51cd_f51_capex_dynamics_debt_sq_mean_63d_base_v134_signal

def f51cd_f51_capex_dynamics_closeadj_sq_mean_63d_base_v135_signal(capex, closeadj):
    res = ((capex / closeadj)**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_sq_mean_63d_base_v135_signal'] = f51cd_f51_capex_dynamics_closeadj_sq_mean_63d_base_v135_signal

def f51cd_f51_capex_dynamics_capex_sq_mean_63d_base_v136_signal(capex):
    res = (capex**2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_sq_mean_63d_base_v136_signal'] = f51cd_f51_capex_dynamics_capex_sq_mean_63d_base_v136_signal

def f51cd_f51_capex_dynamics_closeadj_zscore_med_126d_base_v137_signal(capex, closeadj):
    res = ((capex / closeadj) - (capex / closeadj).rolling(126).median()) / (capex / closeadj).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_zscore_med_126d_base_v137_signal'] = f51cd_f51_capex_dynamics_closeadj_zscore_med_126d_base_v137_signal

def f51cd_f51_capex_dynamics_revenue_log_std_21d_base_v138_signal(capex, revenue):
    res = np.log((capex / revenue)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_log_std_21d_base_v138_signal'] = f51cd_f51_capex_dynamics_revenue_log_std_21d_base_v138_signal

def f51cd_f51_capex_dynamics_assets_log_std_21d_base_v139_signal(capex, assets):
    res = np.log((capex / assets)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_log_std_21d_base_v139_signal'] = f51cd_f51_capex_dynamics_assets_log_std_21d_base_v139_signal

def f51cd_f51_capex_dynamics_ebitda_log_std_21d_base_v140_signal(capex, ebitda):
    res = np.log((capex / ebitda)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_log_std_21d_base_v140_signal'] = f51cd_f51_capex_dynamics_ebitda_log_std_21d_base_v140_signal

def f51cd_f51_capex_dynamics_equity_log_std_21d_base_v141_signal(capex, equity):
    res = np.log((capex / equity)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_log_std_21d_base_v141_signal'] = f51cd_f51_capex_dynamics_equity_log_std_21d_base_v141_signal

def f51cd_f51_capex_dynamics_debt_log_std_21d_base_v142_signal(capex, debt):
    res = np.log((capex / debt)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_log_std_21d_base_v142_signal'] = f51cd_f51_capex_dynamics_debt_log_std_21d_base_v142_signal

def f51cd_f51_capex_dynamics_closeadj_log_std_21d_base_v143_signal(capex, closeadj):
    res = np.log((capex / closeadj)).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_log_std_21d_base_v143_signal'] = f51cd_f51_capex_dynamics_closeadj_log_std_21d_base_v143_signal

def f51cd_f51_capex_dynamics_capex_log_std_21d_base_v144_signal(capex):
    res = np.log(capex).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_capex_log_std_21d_base_v144_signal'] = f51cd_f51_capex_dynamics_capex_log_std_21d_base_v144_signal

def f51cd_f51_capex_dynamics_revenue_log_mean_63d_base_v145_signal(capex, revenue):
    res = np.log((capex / revenue)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_revenue_log_mean_63d_base_v145_signal'] = f51cd_f51_capex_dynamics_revenue_log_mean_63d_base_v145_signal

def f51cd_f51_capex_dynamics_assets_log_mean_21d_base_v146_signal(capex, assets):
    res = np.log((capex / assets)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_assets_log_mean_21d_base_v146_signal'] = f51cd_f51_capex_dynamics_assets_log_mean_21d_base_v146_signal

def f51cd_f51_capex_dynamics_ebitda_log_mean_21d_base_v147_signal(capex, ebitda):
    res = np.log((capex / ebitda)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_ebitda_log_mean_21d_base_v147_signal'] = f51cd_f51_capex_dynamics_ebitda_log_mean_21d_base_v147_signal

def f51cd_f51_capex_dynamics_equity_log_mean_63d_base_v148_signal(capex, equity):
    res = np.log((capex / equity)).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_equity_log_mean_63d_base_v148_signal'] = f51cd_f51_capex_dynamics_equity_log_mean_63d_base_v148_signal

def f51cd_f51_capex_dynamics_debt_log_mean_21d_base_v149_signal(capex, debt):
    res = np.log((capex / debt)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_debt_log_mean_21d_base_v149_signal'] = f51cd_f51_capex_dynamics_debt_log_mean_21d_base_v149_signal

def f51cd_f51_capex_dynamics_closeadj_log_mean_21d_base_v150_signal(capex, closeadj):
    res = np.log((capex / closeadj)).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f51cd_f51_capex_dynamics_closeadj_log_mean_21d_base_v150_signal'] = f51cd_f51_capex_dynamics_closeadj_log_mean_21d_base_v150_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "capex": np.random.uniform(10, 100, n),
        "revenue": np.random.uniform(500, 2000, n),
        "assets": np.random.uniform(2000, 5000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "equity": np.random.uniform(1000, 3000, n),
        "debt": np.random.uniform(500, 1500, n),
        "closeadj": np.random.uniform(10, 100, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
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
