import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fol_f54_operating_leverage_revenue_ncfo_min_ratio_5d_base_v076_signal(revenue, ncfo):
    res = (revenue / ncfo) / (revenue / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_min_ratio_5d_base_v076_signal'] = fol_f54_operating_leverage_revenue_ncfo_min_ratio_5d_base_v076_signal

def fol_f54_operating_leverage_revenue_ncfo_diff_5d_base_v077_signal(revenue, ncfo):
    res = (revenue / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_diff_5d_base_v077_signal'] = fol_f54_operating_leverage_revenue_ncfo_diff_5d_base_v077_signal

def fol_f54_operating_leverage_revenue_ncfo_skew_5d_base_v078_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_skew_5d_base_v078_signal'] = fol_f54_operating_leverage_revenue_ncfo_skew_5d_base_v078_signal

def fol_f54_operating_leverage_revenue_ncfo_kurt_5d_base_v079_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_kurt_5d_base_v079_signal'] = fol_f54_operating_leverage_revenue_ncfo_kurt_5d_base_v079_signal

def fol_f54_operating_leverage_revenue_ncfo_rank_5d_base_v080_signal(revenue, ncfo):
    res = (revenue / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_ncfo_rank_5d_base_v080_signal'] = fol_f54_operating_leverage_revenue_ncfo_rank_5d_base_v080_signal

def fol_f54_operating_leverage_revenue_capex_mean_5d_base_v081_signal(revenue, capex):
    res = (revenue / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_mean_5d_base_v081_signal'] = fol_f54_operating_leverage_revenue_capex_mean_5d_base_v081_signal

def fol_f54_operating_leverage_revenue_capex_std_5d_base_v082_signal(revenue, capex):
    res = (revenue / capex).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_std_5d_base_v082_signal'] = fol_f54_operating_leverage_revenue_capex_std_5d_base_v082_signal

def fol_f54_operating_leverage_revenue_capex_pct_chg_5d_base_v083_signal(revenue, capex):
    res = (revenue / capex).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_pct_chg_5d_base_v083_signal'] = fol_f54_operating_leverage_revenue_capex_pct_chg_5d_base_v083_signal

def fol_f54_operating_leverage_revenue_capex_mean_ratio_5d_base_v084_signal(revenue, capex):
    res = (revenue / capex) / (revenue / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_mean_ratio_5d_base_v084_signal'] = fol_f54_operating_leverage_revenue_capex_mean_ratio_5d_base_v084_signal

def fol_f54_operating_leverage_revenue_capex_max_ratio_5d_base_v085_signal(revenue, capex):
    res = (revenue / capex) / (revenue / capex).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_max_ratio_5d_base_v085_signal'] = fol_f54_operating_leverage_revenue_capex_max_ratio_5d_base_v085_signal

def fol_f54_operating_leverage_revenue_capex_min_ratio_5d_base_v086_signal(revenue, capex):
    res = (revenue / capex) / (revenue / capex).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_min_ratio_5d_base_v086_signal'] = fol_f54_operating_leverage_revenue_capex_min_ratio_5d_base_v086_signal

def fol_f54_operating_leverage_revenue_capex_diff_5d_base_v087_signal(revenue, capex):
    res = (revenue / capex).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_diff_5d_base_v087_signal'] = fol_f54_operating_leverage_revenue_capex_diff_5d_base_v087_signal

def fol_f54_operating_leverage_revenue_capex_skew_5d_base_v088_signal(revenue, capex):
    res = (revenue / capex).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_skew_5d_base_v088_signal'] = fol_f54_operating_leverage_revenue_capex_skew_5d_base_v088_signal

def fol_f54_operating_leverage_revenue_capex_kurt_5d_base_v089_signal(revenue, capex):
    res = (revenue / capex).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_kurt_5d_base_v089_signal'] = fol_f54_operating_leverage_revenue_capex_kurt_5d_base_v089_signal

def fol_f54_operating_leverage_revenue_capex_rank_5d_base_v090_signal(revenue, capex):
    res = (revenue / capex).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_revenue_capex_rank_5d_base_v090_signal'] = fol_f54_operating_leverage_revenue_capex_rank_5d_base_v090_signal

def fol_f54_operating_leverage_netinc_ebitda_mean_5d_base_v091_signal(netinc, ebitda):
    res = (netinc / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_mean_5d_base_v091_signal'] = fol_f54_operating_leverage_netinc_ebitda_mean_5d_base_v091_signal

def fol_f54_operating_leverage_netinc_ebitda_std_5d_base_v092_signal(netinc, ebitda):
    res = (netinc / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_std_5d_base_v092_signal'] = fol_f54_operating_leverage_netinc_ebitda_std_5d_base_v092_signal

def fol_f54_operating_leverage_netinc_ebitda_pct_chg_5d_base_v093_signal(netinc, ebitda):
    res = (netinc / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_pct_chg_5d_base_v093_signal'] = fol_f54_operating_leverage_netinc_ebitda_pct_chg_5d_base_v093_signal

def fol_f54_operating_leverage_netinc_ebitda_mean_ratio_5d_base_v094_signal(netinc, ebitda):
    res = (netinc / ebitda) / (netinc / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_mean_ratio_5d_base_v094_signal'] = fol_f54_operating_leverage_netinc_ebitda_mean_ratio_5d_base_v094_signal

def fol_f54_operating_leverage_netinc_ebitda_max_ratio_5d_base_v095_signal(netinc, ebitda):
    res = (netinc / ebitda) / (netinc / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_max_ratio_5d_base_v095_signal'] = fol_f54_operating_leverage_netinc_ebitda_max_ratio_5d_base_v095_signal

def fol_f54_operating_leverage_netinc_ebitda_min_ratio_5d_base_v096_signal(netinc, ebitda):
    res = (netinc / ebitda) / (netinc / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_min_ratio_5d_base_v096_signal'] = fol_f54_operating_leverage_netinc_ebitda_min_ratio_5d_base_v096_signal

def fol_f54_operating_leverage_netinc_ebitda_diff_5d_base_v097_signal(netinc, ebitda):
    res = (netinc / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_diff_5d_base_v097_signal'] = fol_f54_operating_leverage_netinc_ebitda_diff_5d_base_v097_signal

def fol_f54_operating_leverage_netinc_ebitda_skew_5d_base_v098_signal(netinc, ebitda):
    res = (netinc / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_skew_5d_base_v098_signal'] = fol_f54_operating_leverage_netinc_ebitda_skew_5d_base_v098_signal

def fol_f54_operating_leverage_netinc_ebitda_kurt_5d_base_v099_signal(netinc, ebitda):
    res = (netinc / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_kurt_5d_base_v099_signal'] = fol_f54_operating_leverage_netinc_ebitda_kurt_5d_base_v099_signal

def fol_f54_operating_leverage_netinc_ebitda_rank_5d_base_v100_signal(netinc, ebitda):
    res = (netinc / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ebitda_rank_5d_base_v100_signal'] = fol_f54_operating_leverage_netinc_ebitda_rank_5d_base_v100_signal

def fol_f54_operating_leverage_netinc_revenue_mean_5d_base_v101_signal(netinc, revenue):
    res = (netinc / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_mean_5d_base_v101_signal'] = fol_f54_operating_leverage_netinc_revenue_mean_5d_base_v101_signal

def fol_f54_operating_leverage_netinc_revenue_std_5d_base_v102_signal(netinc, revenue):
    res = (netinc / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_std_5d_base_v102_signal'] = fol_f54_operating_leverage_netinc_revenue_std_5d_base_v102_signal

def fol_f54_operating_leverage_netinc_revenue_pct_chg_5d_base_v103_signal(netinc, revenue):
    res = (netinc / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_pct_chg_5d_base_v103_signal'] = fol_f54_operating_leverage_netinc_revenue_pct_chg_5d_base_v103_signal

def fol_f54_operating_leverage_netinc_revenue_mean_ratio_5d_base_v104_signal(netinc, revenue):
    res = (netinc / revenue) / (netinc / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_mean_ratio_5d_base_v104_signal'] = fol_f54_operating_leverage_netinc_revenue_mean_ratio_5d_base_v104_signal

def fol_f54_operating_leverage_netinc_revenue_max_ratio_5d_base_v105_signal(netinc, revenue):
    res = (netinc / revenue) / (netinc / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_max_ratio_5d_base_v105_signal'] = fol_f54_operating_leverage_netinc_revenue_max_ratio_5d_base_v105_signal

def fol_f54_operating_leverage_netinc_revenue_min_ratio_5d_base_v106_signal(netinc, revenue):
    res = (netinc / revenue) / (netinc / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_min_ratio_5d_base_v106_signal'] = fol_f54_operating_leverage_netinc_revenue_min_ratio_5d_base_v106_signal

def fol_f54_operating_leverage_netinc_revenue_diff_5d_base_v107_signal(netinc, revenue):
    res = (netinc / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_diff_5d_base_v107_signal'] = fol_f54_operating_leverage_netinc_revenue_diff_5d_base_v107_signal

def fol_f54_operating_leverage_netinc_revenue_skew_5d_base_v108_signal(netinc, revenue):
    res = (netinc / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_skew_5d_base_v108_signal'] = fol_f54_operating_leverage_netinc_revenue_skew_5d_base_v108_signal

def fol_f54_operating_leverage_netinc_revenue_kurt_5d_base_v109_signal(netinc, revenue):
    res = (netinc / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_kurt_5d_base_v109_signal'] = fol_f54_operating_leverage_netinc_revenue_kurt_5d_base_v109_signal

def fol_f54_operating_leverage_netinc_revenue_rank_5d_base_v110_signal(netinc, revenue):
    res = (netinc / revenue).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_revenue_rank_5d_base_v110_signal'] = fol_f54_operating_leverage_netinc_revenue_rank_5d_base_v110_signal

def fol_f54_operating_leverage_netinc_mean_5d_base_v111_signal(netinc):
    res = netinc.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_mean_5d_base_v111_signal'] = fol_f54_operating_leverage_netinc_mean_5d_base_v111_signal

def fol_f54_operating_leverage_netinc_std_5d_base_v112_signal(netinc):
    res = netinc.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_std_5d_base_v112_signal'] = fol_f54_operating_leverage_netinc_std_5d_base_v112_signal

def fol_f54_operating_leverage_netinc_pct_chg_5d_base_v113_signal(netinc):
    res = netinc.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_pct_chg_5d_base_v113_signal'] = fol_f54_operating_leverage_netinc_pct_chg_5d_base_v113_signal

def fol_f54_operating_leverage_netinc_max_ratio_5d_base_v114_signal(netinc):
    res = netinc / netinc.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_max_ratio_5d_base_v114_signal'] = fol_f54_operating_leverage_netinc_max_ratio_5d_base_v114_signal

def fol_f54_operating_leverage_netinc_min_ratio_5d_base_v115_signal(netinc):
    res = netinc / netinc.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_min_ratio_5d_base_v115_signal'] = fol_f54_operating_leverage_netinc_min_ratio_5d_base_v115_signal

def fol_f54_operating_leverage_netinc_ncfo_mean_5d_base_v116_signal(netinc, ncfo):
    res = (netinc / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_mean_5d_base_v116_signal'] = fol_f54_operating_leverage_netinc_ncfo_mean_5d_base_v116_signal

def fol_f54_operating_leverage_netinc_ncfo_std_5d_base_v117_signal(netinc, ncfo):
    res = (netinc / ncfo).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_std_5d_base_v117_signal'] = fol_f54_operating_leverage_netinc_ncfo_std_5d_base_v117_signal

def fol_f54_operating_leverage_netinc_ncfo_pct_chg_5d_base_v118_signal(netinc, ncfo):
    res = (netinc / ncfo).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_pct_chg_5d_base_v118_signal'] = fol_f54_operating_leverage_netinc_ncfo_pct_chg_5d_base_v118_signal

def fol_f54_operating_leverage_netinc_ncfo_mean_ratio_5d_base_v119_signal(netinc, ncfo):
    res = (netinc / ncfo) / (netinc / ncfo).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_mean_ratio_5d_base_v119_signal'] = fol_f54_operating_leverage_netinc_ncfo_mean_ratio_5d_base_v119_signal

def fol_f54_operating_leverage_netinc_ncfo_max_ratio_5d_base_v120_signal(netinc, ncfo):
    res = (netinc / ncfo) / (netinc / ncfo).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_max_ratio_5d_base_v120_signal'] = fol_f54_operating_leverage_netinc_ncfo_max_ratio_5d_base_v120_signal

def fol_f54_operating_leverage_netinc_ncfo_min_ratio_5d_base_v121_signal(netinc, ncfo):
    res = (netinc / ncfo) / (netinc / ncfo).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_min_ratio_5d_base_v121_signal'] = fol_f54_operating_leverage_netinc_ncfo_min_ratio_5d_base_v121_signal

def fol_f54_operating_leverage_netinc_ncfo_diff_5d_base_v122_signal(netinc, ncfo):
    res = (netinc / ncfo).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_diff_5d_base_v122_signal'] = fol_f54_operating_leverage_netinc_ncfo_diff_5d_base_v122_signal

def fol_f54_operating_leverage_netinc_ncfo_skew_5d_base_v123_signal(netinc, ncfo):
    res = (netinc / ncfo).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_skew_5d_base_v123_signal'] = fol_f54_operating_leverage_netinc_ncfo_skew_5d_base_v123_signal

def fol_f54_operating_leverage_netinc_ncfo_kurt_5d_base_v124_signal(netinc, ncfo):
    res = (netinc / ncfo).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_kurt_5d_base_v124_signal'] = fol_f54_operating_leverage_netinc_ncfo_kurt_5d_base_v124_signal

def fol_f54_operating_leverage_netinc_ncfo_rank_5d_base_v125_signal(netinc, ncfo):
    res = (netinc / ncfo).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_ncfo_rank_5d_base_v125_signal'] = fol_f54_operating_leverage_netinc_ncfo_rank_5d_base_v125_signal

def fol_f54_operating_leverage_netinc_capex_mean_5d_base_v126_signal(netinc, capex):
    res = (netinc / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_mean_5d_base_v126_signal'] = fol_f54_operating_leverage_netinc_capex_mean_5d_base_v126_signal

def fol_f54_operating_leverage_netinc_capex_std_5d_base_v127_signal(netinc, capex):
    res = (netinc / capex).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_std_5d_base_v127_signal'] = fol_f54_operating_leverage_netinc_capex_std_5d_base_v127_signal

def fol_f54_operating_leverage_netinc_capex_pct_chg_5d_base_v128_signal(netinc, capex):
    res = (netinc / capex).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_pct_chg_5d_base_v128_signal'] = fol_f54_operating_leverage_netinc_capex_pct_chg_5d_base_v128_signal

def fol_f54_operating_leverage_netinc_capex_mean_ratio_5d_base_v129_signal(netinc, capex):
    res = (netinc / capex) / (netinc / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_mean_ratio_5d_base_v129_signal'] = fol_f54_operating_leverage_netinc_capex_mean_ratio_5d_base_v129_signal

def fol_f54_operating_leverage_netinc_capex_max_ratio_5d_base_v130_signal(netinc, capex):
    res = (netinc / capex) / (netinc / capex).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_max_ratio_5d_base_v130_signal'] = fol_f54_operating_leverage_netinc_capex_max_ratio_5d_base_v130_signal

def fol_f54_operating_leverage_netinc_capex_min_ratio_5d_base_v131_signal(netinc, capex):
    res = (netinc / capex) / (netinc / capex).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_min_ratio_5d_base_v131_signal'] = fol_f54_operating_leverage_netinc_capex_min_ratio_5d_base_v131_signal

def fol_f54_operating_leverage_netinc_capex_diff_5d_base_v132_signal(netinc, capex):
    res = (netinc / capex).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_diff_5d_base_v132_signal'] = fol_f54_operating_leverage_netinc_capex_diff_5d_base_v132_signal

def fol_f54_operating_leverage_netinc_capex_skew_5d_base_v133_signal(netinc, capex):
    res = (netinc / capex).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_skew_5d_base_v133_signal'] = fol_f54_operating_leverage_netinc_capex_skew_5d_base_v133_signal

def fol_f54_operating_leverage_netinc_capex_kurt_5d_base_v134_signal(netinc, capex):
    res = (netinc / capex).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_kurt_5d_base_v134_signal'] = fol_f54_operating_leverage_netinc_capex_kurt_5d_base_v134_signal

def fol_f54_operating_leverage_netinc_capex_rank_5d_base_v135_signal(netinc, capex):
    res = (netinc / capex).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_netinc_capex_rank_5d_base_v135_signal'] = fol_f54_operating_leverage_netinc_capex_rank_5d_base_v135_signal

def fol_f54_operating_leverage_ncfo_ebitda_mean_5d_base_v136_signal(ncfo, ebitda):
    res = (ncfo / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_mean_5d_base_v136_signal'] = fol_f54_operating_leverage_ncfo_ebitda_mean_5d_base_v136_signal

def fol_f54_operating_leverage_ncfo_ebitda_std_5d_base_v137_signal(ncfo, ebitda):
    res = (ncfo / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_std_5d_base_v137_signal'] = fol_f54_operating_leverage_ncfo_ebitda_std_5d_base_v137_signal

def fol_f54_operating_leverage_ncfo_ebitda_pct_chg_5d_base_v138_signal(ncfo, ebitda):
    res = (ncfo / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_pct_chg_5d_base_v138_signal'] = fol_f54_operating_leverage_ncfo_ebitda_pct_chg_5d_base_v138_signal

def fol_f54_operating_leverage_ncfo_ebitda_mean_ratio_5d_base_v139_signal(ncfo, ebitda):
    res = (ncfo / ebitda) / (ncfo / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_mean_ratio_5d_base_v139_signal'] = fol_f54_operating_leverage_ncfo_ebitda_mean_ratio_5d_base_v139_signal

def fol_f54_operating_leverage_ncfo_ebitda_max_ratio_5d_base_v140_signal(ncfo, ebitda):
    res = (ncfo / ebitda) / (ncfo / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_max_ratio_5d_base_v140_signal'] = fol_f54_operating_leverage_ncfo_ebitda_max_ratio_5d_base_v140_signal

def fol_f54_operating_leverage_ncfo_ebitda_min_ratio_5d_base_v141_signal(ncfo, ebitda):
    res = (ncfo / ebitda) / (ncfo / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_min_ratio_5d_base_v141_signal'] = fol_f54_operating_leverage_ncfo_ebitda_min_ratio_5d_base_v141_signal

def fol_f54_operating_leverage_ncfo_ebitda_diff_5d_base_v142_signal(ncfo, ebitda):
    res = (ncfo / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_diff_5d_base_v142_signal'] = fol_f54_operating_leverage_ncfo_ebitda_diff_5d_base_v142_signal

def fol_f54_operating_leverage_ncfo_ebitda_skew_5d_base_v143_signal(ncfo, ebitda):
    res = (ncfo / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_skew_5d_base_v143_signal'] = fol_f54_operating_leverage_ncfo_ebitda_skew_5d_base_v143_signal

def fol_f54_operating_leverage_ncfo_ebitda_kurt_5d_base_v144_signal(ncfo, ebitda):
    res = (ncfo / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_kurt_5d_base_v144_signal'] = fol_f54_operating_leverage_ncfo_ebitda_kurt_5d_base_v144_signal

def fol_f54_operating_leverage_ncfo_ebitda_rank_5d_base_v145_signal(ncfo, ebitda):
    res = (ncfo / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_ebitda_rank_5d_base_v145_signal'] = fol_f54_operating_leverage_ncfo_ebitda_rank_5d_base_v145_signal

def fol_f54_operating_leverage_ncfo_revenue_mean_5d_base_v146_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_revenue_mean_5d_base_v146_signal'] = fol_f54_operating_leverage_ncfo_revenue_mean_5d_base_v146_signal

def fol_f54_operating_leverage_ncfo_revenue_std_5d_base_v147_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_revenue_std_5d_base_v147_signal'] = fol_f54_operating_leverage_ncfo_revenue_std_5d_base_v147_signal

def fol_f54_operating_leverage_ncfo_revenue_pct_chg_5d_base_v148_signal(ncfo, revenue):
    res = (ncfo / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_revenue_pct_chg_5d_base_v148_signal'] = fol_f54_operating_leverage_ncfo_revenue_pct_chg_5d_base_v148_signal

def fol_f54_operating_leverage_ncfo_revenue_mean_ratio_5d_base_v149_signal(ncfo, revenue):
    res = (ncfo / revenue) / (ncfo / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_revenue_mean_ratio_5d_base_v149_signal'] = fol_f54_operating_leverage_ncfo_revenue_mean_ratio_5d_base_v149_signal

def fol_f54_operating_leverage_ncfo_revenue_max_ratio_5d_base_v150_signal(ncfo, revenue):
    res = (ncfo / revenue) / (ncfo / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fol_f54_operating_leverage_ncfo_revenue_max_ratio_5d_base_v150_signal'] = fol_f54_operating_leverage_ncfo_revenue_max_ratio_5d_base_v150_signal

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
