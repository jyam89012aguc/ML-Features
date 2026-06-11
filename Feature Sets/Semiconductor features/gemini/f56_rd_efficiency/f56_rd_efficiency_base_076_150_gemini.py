import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fre_f56_rd_efficiency_revenue_fcf_min_ratio_5d_base_v076_signal(revenue, fcf):
    res = (revenue / fcf) / (revenue / fcf).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_fcf_min_ratio_5d_base_v076_signal'] = fre_f56_rd_efficiency_revenue_fcf_min_ratio_5d_base_v076_signal

def fre_f56_rd_efficiency_revenue_fcf_diff_5d_base_v077_signal(revenue, fcf):
    res = (revenue / fcf).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_fcf_diff_5d_base_v077_signal'] = fre_f56_rd_efficiency_revenue_fcf_diff_5d_base_v077_signal

def fre_f56_rd_efficiency_revenue_fcf_skew_5d_base_v078_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_fcf_skew_5d_base_v078_signal'] = fre_f56_rd_efficiency_revenue_fcf_skew_5d_base_v078_signal

def fre_f56_rd_efficiency_revenue_fcf_kurt_5d_base_v079_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_fcf_kurt_5d_base_v079_signal'] = fre_f56_rd_efficiency_revenue_fcf_kurt_5d_base_v079_signal

def fre_f56_rd_efficiency_revenue_fcf_rank_5d_base_v080_signal(revenue, fcf):
    res = (revenue / fcf).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_fcf_rank_5d_base_v080_signal'] = fre_f56_rd_efficiency_revenue_fcf_rank_5d_base_v080_signal

def fre_f56_rd_efficiency_revenue_capex_mean_5d_base_v081_signal(revenue, capex):
    res = (revenue / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_mean_5d_base_v081_signal'] = fre_f56_rd_efficiency_revenue_capex_mean_5d_base_v081_signal

def fre_f56_rd_efficiency_revenue_capex_std_5d_base_v082_signal(revenue, capex):
    res = (revenue / capex).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_std_5d_base_v082_signal'] = fre_f56_rd_efficiency_revenue_capex_std_5d_base_v082_signal

def fre_f56_rd_efficiency_revenue_capex_pct_chg_5d_base_v083_signal(revenue, capex):
    res = (revenue / capex).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_pct_chg_5d_base_v083_signal'] = fre_f56_rd_efficiency_revenue_capex_pct_chg_5d_base_v083_signal

def fre_f56_rd_efficiency_revenue_capex_mean_ratio_5d_base_v084_signal(revenue, capex):
    res = (revenue / capex) / (revenue / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_mean_ratio_5d_base_v084_signal'] = fre_f56_rd_efficiency_revenue_capex_mean_ratio_5d_base_v084_signal

def fre_f56_rd_efficiency_revenue_capex_max_ratio_5d_base_v085_signal(revenue, capex):
    res = (revenue / capex) / (revenue / capex).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_max_ratio_5d_base_v085_signal'] = fre_f56_rd_efficiency_revenue_capex_max_ratio_5d_base_v085_signal

def fre_f56_rd_efficiency_revenue_capex_min_ratio_5d_base_v086_signal(revenue, capex):
    res = (revenue / capex) / (revenue / capex).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_min_ratio_5d_base_v086_signal'] = fre_f56_rd_efficiency_revenue_capex_min_ratio_5d_base_v086_signal

def fre_f56_rd_efficiency_revenue_capex_diff_5d_base_v087_signal(revenue, capex):
    res = (revenue / capex).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_diff_5d_base_v087_signal'] = fre_f56_rd_efficiency_revenue_capex_diff_5d_base_v087_signal

def fre_f56_rd_efficiency_revenue_capex_skew_5d_base_v088_signal(revenue, capex):
    res = (revenue / capex).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_skew_5d_base_v088_signal'] = fre_f56_rd_efficiency_revenue_capex_skew_5d_base_v088_signal

def fre_f56_rd_efficiency_revenue_capex_kurt_5d_base_v089_signal(revenue, capex):
    res = (revenue / capex).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_kurt_5d_base_v089_signal'] = fre_f56_rd_efficiency_revenue_capex_kurt_5d_base_v089_signal

def fre_f56_rd_efficiency_revenue_capex_rank_5d_base_v090_signal(revenue, capex):
    res = (revenue / capex).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_capex_rank_5d_base_v090_signal'] = fre_f56_rd_efficiency_revenue_capex_rank_5d_base_v090_signal

def fre_f56_rd_efficiency_revenue_assets_mean_5d_base_v091_signal(revenue, assets):
    res = (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_mean_5d_base_v091_signal'] = fre_f56_rd_efficiency_revenue_assets_mean_5d_base_v091_signal

def fre_f56_rd_efficiency_revenue_assets_std_5d_base_v092_signal(revenue, assets):
    res = (revenue / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_std_5d_base_v092_signal'] = fre_f56_rd_efficiency_revenue_assets_std_5d_base_v092_signal

def fre_f56_rd_efficiency_revenue_assets_pct_chg_5d_base_v093_signal(revenue, assets):
    res = (revenue / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_pct_chg_5d_base_v093_signal'] = fre_f56_rd_efficiency_revenue_assets_pct_chg_5d_base_v093_signal

def fre_f56_rd_efficiency_revenue_assets_mean_ratio_5d_base_v094_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_mean_ratio_5d_base_v094_signal'] = fre_f56_rd_efficiency_revenue_assets_mean_ratio_5d_base_v094_signal

def fre_f56_rd_efficiency_revenue_assets_max_ratio_5d_base_v095_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_max_ratio_5d_base_v095_signal'] = fre_f56_rd_efficiency_revenue_assets_max_ratio_5d_base_v095_signal

def fre_f56_rd_efficiency_revenue_assets_min_ratio_5d_base_v096_signal(revenue, assets):
    res = (revenue / assets) / (revenue / assets).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_min_ratio_5d_base_v096_signal'] = fre_f56_rd_efficiency_revenue_assets_min_ratio_5d_base_v096_signal

def fre_f56_rd_efficiency_revenue_assets_diff_5d_base_v097_signal(revenue, assets):
    res = (revenue / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_diff_5d_base_v097_signal'] = fre_f56_rd_efficiency_revenue_assets_diff_5d_base_v097_signal

def fre_f56_rd_efficiency_revenue_assets_skew_5d_base_v098_signal(revenue, assets):
    res = (revenue / assets).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_skew_5d_base_v098_signal'] = fre_f56_rd_efficiency_revenue_assets_skew_5d_base_v098_signal

def fre_f56_rd_efficiency_revenue_assets_kurt_5d_base_v099_signal(revenue, assets):
    res = (revenue / assets).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_kurt_5d_base_v099_signal'] = fre_f56_rd_efficiency_revenue_assets_kurt_5d_base_v099_signal

def fre_f56_rd_efficiency_revenue_assets_rank_5d_base_v100_signal(revenue, assets):
    res = (revenue / assets).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_assets_rank_5d_base_v100_signal'] = fre_f56_rd_efficiency_revenue_assets_rank_5d_base_v100_signal

def fre_f56_rd_efficiency_revenue_netinc_mean_5d_base_v101_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_mean_5d_base_v101_signal'] = fre_f56_rd_efficiency_revenue_netinc_mean_5d_base_v101_signal

def fre_f56_rd_efficiency_revenue_netinc_std_5d_base_v102_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_std_5d_base_v102_signal'] = fre_f56_rd_efficiency_revenue_netinc_std_5d_base_v102_signal

def fre_f56_rd_efficiency_revenue_netinc_pct_chg_5d_base_v103_signal(revenue, netinc):
    res = (revenue / netinc).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_pct_chg_5d_base_v103_signal'] = fre_f56_rd_efficiency_revenue_netinc_pct_chg_5d_base_v103_signal

def fre_f56_rd_efficiency_revenue_netinc_mean_ratio_5d_base_v104_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_mean_ratio_5d_base_v104_signal'] = fre_f56_rd_efficiency_revenue_netinc_mean_ratio_5d_base_v104_signal

def fre_f56_rd_efficiency_revenue_netinc_max_ratio_5d_base_v105_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_max_ratio_5d_base_v105_signal'] = fre_f56_rd_efficiency_revenue_netinc_max_ratio_5d_base_v105_signal

def fre_f56_rd_efficiency_revenue_netinc_min_ratio_5d_base_v106_signal(revenue, netinc):
    res = (revenue / netinc) / (revenue / netinc).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_min_ratio_5d_base_v106_signal'] = fre_f56_rd_efficiency_revenue_netinc_min_ratio_5d_base_v106_signal

def fre_f56_rd_efficiency_revenue_netinc_diff_5d_base_v107_signal(revenue, netinc):
    res = (revenue / netinc).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_diff_5d_base_v107_signal'] = fre_f56_rd_efficiency_revenue_netinc_diff_5d_base_v107_signal

def fre_f56_rd_efficiency_revenue_netinc_skew_5d_base_v108_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_skew_5d_base_v108_signal'] = fre_f56_rd_efficiency_revenue_netinc_skew_5d_base_v108_signal

def fre_f56_rd_efficiency_revenue_netinc_kurt_5d_base_v109_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_kurt_5d_base_v109_signal'] = fre_f56_rd_efficiency_revenue_netinc_kurt_5d_base_v109_signal

def fre_f56_rd_efficiency_revenue_netinc_rank_5d_base_v110_signal(revenue, netinc):
    res = (revenue / netinc).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_revenue_netinc_rank_5d_base_v110_signal'] = fre_f56_rd_efficiency_revenue_netinc_rank_5d_base_v110_signal

def fre_f56_rd_efficiency_fcf_ebitda_mean_5d_base_v111_signal(fcf, ebitda):
    res = (fcf / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_mean_5d_base_v111_signal'] = fre_f56_rd_efficiency_fcf_ebitda_mean_5d_base_v111_signal

def fre_f56_rd_efficiency_fcf_ebitda_std_5d_base_v112_signal(fcf, ebitda):
    res = (fcf / ebitda).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_std_5d_base_v112_signal'] = fre_f56_rd_efficiency_fcf_ebitda_std_5d_base_v112_signal

def fre_f56_rd_efficiency_fcf_ebitda_pct_chg_5d_base_v113_signal(fcf, ebitda):
    res = (fcf / ebitda).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_pct_chg_5d_base_v113_signal'] = fre_f56_rd_efficiency_fcf_ebitda_pct_chg_5d_base_v113_signal

def fre_f56_rd_efficiency_fcf_ebitda_mean_ratio_5d_base_v114_signal(fcf, ebitda):
    res = (fcf / ebitda) / (fcf / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_mean_ratio_5d_base_v114_signal'] = fre_f56_rd_efficiency_fcf_ebitda_mean_ratio_5d_base_v114_signal

def fre_f56_rd_efficiency_fcf_ebitda_max_ratio_5d_base_v115_signal(fcf, ebitda):
    res = (fcf / ebitda) / (fcf / ebitda).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_max_ratio_5d_base_v115_signal'] = fre_f56_rd_efficiency_fcf_ebitda_max_ratio_5d_base_v115_signal

def fre_f56_rd_efficiency_fcf_ebitda_min_ratio_5d_base_v116_signal(fcf, ebitda):
    res = (fcf / ebitda) / (fcf / ebitda).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_min_ratio_5d_base_v116_signal'] = fre_f56_rd_efficiency_fcf_ebitda_min_ratio_5d_base_v116_signal

def fre_f56_rd_efficiency_fcf_ebitda_diff_5d_base_v117_signal(fcf, ebitda):
    res = (fcf / ebitda).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_diff_5d_base_v117_signal'] = fre_f56_rd_efficiency_fcf_ebitda_diff_5d_base_v117_signal

def fre_f56_rd_efficiency_fcf_ebitda_skew_5d_base_v118_signal(fcf, ebitda):
    res = (fcf / ebitda).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_skew_5d_base_v118_signal'] = fre_f56_rd_efficiency_fcf_ebitda_skew_5d_base_v118_signal

def fre_f56_rd_efficiency_fcf_ebitda_kurt_5d_base_v119_signal(fcf, ebitda):
    res = (fcf / ebitda).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_kurt_5d_base_v119_signal'] = fre_f56_rd_efficiency_fcf_ebitda_kurt_5d_base_v119_signal

def fre_f56_rd_efficiency_fcf_ebitda_rank_5d_base_v120_signal(fcf, ebitda):
    res = (fcf / ebitda).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_ebitda_rank_5d_base_v120_signal'] = fre_f56_rd_efficiency_fcf_ebitda_rank_5d_base_v120_signal

def fre_f56_rd_efficiency_fcf_revenue_mean_5d_base_v121_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_mean_5d_base_v121_signal'] = fre_f56_rd_efficiency_fcf_revenue_mean_5d_base_v121_signal

def fre_f56_rd_efficiency_fcf_revenue_std_5d_base_v122_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_std_5d_base_v122_signal'] = fre_f56_rd_efficiency_fcf_revenue_std_5d_base_v122_signal

def fre_f56_rd_efficiency_fcf_revenue_pct_chg_5d_base_v123_signal(fcf, revenue):
    res = (fcf / revenue).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_pct_chg_5d_base_v123_signal'] = fre_f56_rd_efficiency_fcf_revenue_pct_chg_5d_base_v123_signal

def fre_f56_rd_efficiency_fcf_revenue_mean_ratio_5d_base_v124_signal(fcf, revenue):
    res = (fcf / revenue) / (fcf / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_mean_ratio_5d_base_v124_signal'] = fre_f56_rd_efficiency_fcf_revenue_mean_ratio_5d_base_v124_signal

def fre_f56_rd_efficiency_fcf_revenue_max_ratio_5d_base_v125_signal(fcf, revenue):
    res = (fcf / revenue) / (fcf / revenue).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_max_ratio_5d_base_v125_signal'] = fre_f56_rd_efficiency_fcf_revenue_max_ratio_5d_base_v125_signal

def fre_f56_rd_efficiency_fcf_revenue_min_ratio_5d_base_v126_signal(fcf, revenue):
    res = (fcf / revenue) / (fcf / revenue).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_min_ratio_5d_base_v126_signal'] = fre_f56_rd_efficiency_fcf_revenue_min_ratio_5d_base_v126_signal

def fre_f56_rd_efficiency_fcf_revenue_diff_5d_base_v127_signal(fcf, revenue):
    res = (fcf / revenue).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_diff_5d_base_v127_signal'] = fre_f56_rd_efficiency_fcf_revenue_diff_5d_base_v127_signal

def fre_f56_rd_efficiency_fcf_revenue_skew_5d_base_v128_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_skew_5d_base_v128_signal'] = fre_f56_rd_efficiency_fcf_revenue_skew_5d_base_v128_signal

def fre_f56_rd_efficiency_fcf_revenue_kurt_5d_base_v129_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_kurt_5d_base_v129_signal'] = fre_f56_rd_efficiency_fcf_revenue_kurt_5d_base_v129_signal

def fre_f56_rd_efficiency_fcf_revenue_rank_5d_base_v130_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_revenue_rank_5d_base_v130_signal'] = fre_f56_rd_efficiency_fcf_revenue_rank_5d_base_v130_signal

def fre_f56_rd_efficiency_fcf_mean_5d_base_v131_signal(fcf):
    res = fcf.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_mean_5d_base_v131_signal'] = fre_f56_rd_efficiency_fcf_mean_5d_base_v131_signal

def fre_f56_rd_efficiency_fcf_std_5d_base_v132_signal(fcf):
    res = fcf.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_std_5d_base_v132_signal'] = fre_f56_rd_efficiency_fcf_std_5d_base_v132_signal

def fre_f56_rd_efficiency_fcf_pct_chg_5d_base_v133_signal(fcf):
    res = fcf.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_pct_chg_5d_base_v133_signal'] = fre_f56_rd_efficiency_fcf_pct_chg_5d_base_v133_signal

def fre_f56_rd_efficiency_fcf_max_ratio_5d_base_v134_signal(fcf):
    res = fcf / fcf.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_max_ratio_5d_base_v134_signal'] = fre_f56_rd_efficiency_fcf_max_ratio_5d_base_v134_signal

def fre_f56_rd_efficiency_fcf_min_ratio_5d_base_v135_signal(fcf):
    res = fcf / fcf.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_min_ratio_5d_base_v135_signal'] = fre_f56_rd_efficiency_fcf_min_ratio_5d_base_v135_signal

def fre_f56_rd_efficiency_fcf_capex_mean_5d_base_v136_signal(fcf, capex):
    res = (fcf / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_mean_5d_base_v136_signal'] = fre_f56_rd_efficiency_fcf_capex_mean_5d_base_v136_signal

def fre_f56_rd_efficiency_fcf_capex_std_5d_base_v137_signal(fcf, capex):
    res = (fcf / capex).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_std_5d_base_v137_signal'] = fre_f56_rd_efficiency_fcf_capex_std_5d_base_v137_signal

def fre_f56_rd_efficiency_fcf_capex_pct_chg_5d_base_v138_signal(fcf, capex):
    res = (fcf / capex).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_pct_chg_5d_base_v138_signal'] = fre_f56_rd_efficiency_fcf_capex_pct_chg_5d_base_v138_signal

def fre_f56_rd_efficiency_fcf_capex_mean_ratio_5d_base_v139_signal(fcf, capex):
    res = (fcf / capex) / (fcf / capex).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_mean_ratio_5d_base_v139_signal'] = fre_f56_rd_efficiency_fcf_capex_mean_ratio_5d_base_v139_signal

def fre_f56_rd_efficiency_fcf_capex_max_ratio_5d_base_v140_signal(fcf, capex):
    res = (fcf / capex) / (fcf / capex).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_max_ratio_5d_base_v140_signal'] = fre_f56_rd_efficiency_fcf_capex_max_ratio_5d_base_v140_signal

def fre_f56_rd_efficiency_fcf_capex_min_ratio_5d_base_v141_signal(fcf, capex):
    res = (fcf / capex) / (fcf / capex).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_min_ratio_5d_base_v141_signal'] = fre_f56_rd_efficiency_fcf_capex_min_ratio_5d_base_v141_signal

def fre_f56_rd_efficiency_fcf_capex_diff_5d_base_v142_signal(fcf, capex):
    res = (fcf / capex).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_diff_5d_base_v142_signal'] = fre_f56_rd_efficiency_fcf_capex_diff_5d_base_v142_signal

def fre_f56_rd_efficiency_fcf_capex_skew_5d_base_v143_signal(fcf, capex):
    res = (fcf / capex).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_skew_5d_base_v143_signal'] = fre_f56_rd_efficiency_fcf_capex_skew_5d_base_v143_signal

def fre_f56_rd_efficiency_fcf_capex_kurt_5d_base_v144_signal(fcf, capex):
    res = (fcf / capex).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_kurt_5d_base_v144_signal'] = fre_f56_rd_efficiency_fcf_capex_kurt_5d_base_v144_signal

def fre_f56_rd_efficiency_fcf_capex_rank_5d_base_v145_signal(fcf, capex):
    res = (fcf / capex).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_capex_rank_5d_base_v145_signal'] = fre_f56_rd_efficiency_fcf_capex_rank_5d_base_v145_signal

def fre_f56_rd_efficiency_fcf_assets_mean_5d_base_v146_signal(fcf, assets):
    res = (fcf / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_assets_mean_5d_base_v146_signal'] = fre_f56_rd_efficiency_fcf_assets_mean_5d_base_v146_signal

def fre_f56_rd_efficiency_fcf_assets_std_5d_base_v147_signal(fcf, assets):
    res = (fcf / assets).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_assets_std_5d_base_v147_signal'] = fre_f56_rd_efficiency_fcf_assets_std_5d_base_v147_signal

def fre_f56_rd_efficiency_fcf_assets_pct_chg_5d_base_v148_signal(fcf, assets):
    res = (fcf / assets).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_assets_pct_chg_5d_base_v148_signal'] = fre_f56_rd_efficiency_fcf_assets_pct_chg_5d_base_v148_signal

def fre_f56_rd_efficiency_fcf_assets_mean_ratio_5d_base_v149_signal(fcf, assets):
    res = (fcf / assets) / (fcf / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_assets_mean_ratio_5d_base_v149_signal'] = fre_f56_rd_efficiency_fcf_assets_mean_ratio_5d_base_v149_signal

def fre_f56_rd_efficiency_fcf_assets_max_ratio_5d_base_v150_signal(fcf, assets):
    res = (fcf / assets) / (fcf / assets).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fre_f56_rd_efficiency_fcf_assets_max_ratio_5d_base_v150_signal'] = fre_f56_rd_efficiency_fcf_assets_max_ratio_5d_base_v150_signal

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
