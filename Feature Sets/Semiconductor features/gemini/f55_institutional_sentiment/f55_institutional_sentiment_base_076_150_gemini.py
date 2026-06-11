import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fis_f55_institutional_sentiment_closeadj_pe_min_ratio_5d_base_v076_signal(closeadj, pe):
    res = (closeadj / pe) / (closeadj / pe).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_min_ratio_5d_base_v076_signal'] = fis_f55_institutional_sentiment_closeadj_pe_min_ratio_5d_base_v076_signal

def fis_f55_institutional_sentiment_closeadj_pe_diff_5d_base_v077_signal(closeadj, pe):
    res = (closeadj / pe).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_diff_5d_base_v077_signal'] = fis_f55_institutional_sentiment_closeadj_pe_diff_5d_base_v077_signal

def fis_f55_institutional_sentiment_closeadj_pe_skew_5d_base_v078_signal(closeadj, pe):
    res = (closeadj / pe).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_skew_5d_base_v078_signal'] = fis_f55_institutional_sentiment_closeadj_pe_skew_5d_base_v078_signal

def fis_f55_institutional_sentiment_closeadj_pe_kurt_5d_base_v079_signal(closeadj, pe):
    res = (closeadj / pe).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_kurt_5d_base_v079_signal'] = fis_f55_institutional_sentiment_closeadj_pe_kurt_5d_base_v079_signal

def fis_f55_institutional_sentiment_closeadj_pe_rank_5d_base_v080_signal(closeadj, pe):
    res = (closeadj / pe).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_rank_5d_base_v080_signal'] = fis_f55_institutional_sentiment_closeadj_pe_rank_5d_base_v080_signal

def fis_f55_institutional_sentiment_closeadj_pb_mean_5d_base_v081_signal(closeadj, pb):
    res = (closeadj / pb).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_mean_5d_base_v081_signal'] = fis_f55_institutional_sentiment_closeadj_pb_mean_5d_base_v081_signal

def fis_f55_institutional_sentiment_closeadj_pb_std_5d_base_v082_signal(closeadj, pb):
    res = (closeadj / pb).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_std_5d_base_v082_signal'] = fis_f55_institutional_sentiment_closeadj_pb_std_5d_base_v082_signal

def fis_f55_institutional_sentiment_closeadj_pb_pct_chg_5d_base_v083_signal(closeadj, pb):
    res = (closeadj / pb).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_pct_chg_5d_base_v083_signal'] = fis_f55_institutional_sentiment_closeadj_pb_pct_chg_5d_base_v083_signal

def fis_f55_institutional_sentiment_closeadj_pb_mean_ratio_5d_base_v084_signal(closeadj, pb):
    res = (closeadj / pb) / (closeadj / pb).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_mean_ratio_5d_base_v084_signal'] = fis_f55_institutional_sentiment_closeadj_pb_mean_ratio_5d_base_v084_signal

def fis_f55_institutional_sentiment_closeadj_pb_max_ratio_5d_base_v085_signal(closeadj, pb):
    res = (closeadj / pb) / (closeadj / pb).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_max_ratio_5d_base_v085_signal'] = fis_f55_institutional_sentiment_closeadj_pb_max_ratio_5d_base_v085_signal

def fis_f55_institutional_sentiment_closeadj_pb_min_ratio_5d_base_v086_signal(closeadj, pb):
    res = (closeadj / pb) / (closeadj / pb).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_min_ratio_5d_base_v086_signal'] = fis_f55_institutional_sentiment_closeadj_pb_min_ratio_5d_base_v086_signal

def fis_f55_institutional_sentiment_closeadj_pb_diff_5d_base_v087_signal(closeadj, pb):
    res = (closeadj / pb).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_diff_5d_base_v087_signal'] = fis_f55_institutional_sentiment_closeadj_pb_diff_5d_base_v087_signal

def fis_f55_institutional_sentiment_closeadj_pb_skew_5d_base_v088_signal(closeadj, pb):
    res = (closeadj / pb).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_skew_5d_base_v088_signal'] = fis_f55_institutional_sentiment_closeadj_pb_skew_5d_base_v088_signal

def fis_f55_institutional_sentiment_closeadj_pb_kurt_5d_base_v089_signal(closeadj, pb):
    res = (closeadj / pb).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_kurt_5d_base_v089_signal'] = fis_f55_institutional_sentiment_closeadj_pb_kurt_5d_base_v089_signal

def fis_f55_institutional_sentiment_closeadj_pb_rank_5d_base_v090_signal(closeadj, pb):
    res = (closeadj / pb).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pb_rank_5d_base_v090_signal'] = fis_f55_institutional_sentiment_closeadj_pb_rank_5d_base_v090_signal

def fis_f55_institutional_sentiment_closeadj_ps_mean_5d_base_v091_signal(closeadj, ps):
    res = (closeadj / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_mean_5d_base_v091_signal'] = fis_f55_institutional_sentiment_closeadj_ps_mean_5d_base_v091_signal

def fis_f55_institutional_sentiment_closeadj_ps_std_5d_base_v092_signal(closeadj, ps):
    res = (closeadj / ps).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_std_5d_base_v092_signal'] = fis_f55_institutional_sentiment_closeadj_ps_std_5d_base_v092_signal

def fis_f55_institutional_sentiment_closeadj_ps_pct_chg_5d_base_v093_signal(closeadj, ps):
    res = (closeadj / ps).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_pct_chg_5d_base_v093_signal'] = fis_f55_institutional_sentiment_closeadj_ps_pct_chg_5d_base_v093_signal

def fis_f55_institutional_sentiment_closeadj_ps_mean_ratio_5d_base_v094_signal(closeadj, ps):
    res = (closeadj / ps) / (closeadj / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_mean_ratio_5d_base_v094_signal'] = fis_f55_institutional_sentiment_closeadj_ps_mean_ratio_5d_base_v094_signal

def fis_f55_institutional_sentiment_closeadj_ps_max_ratio_5d_base_v095_signal(closeadj, ps):
    res = (closeadj / ps) / (closeadj / ps).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_max_ratio_5d_base_v095_signal'] = fis_f55_institutional_sentiment_closeadj_ps_max_ratio_5d_base_v095_signal

def fis_f55_institutional_sentiment_closeadj_ps_min_ratio_5d_base_v096_signal(closeadj, ps):
    res = (closeadj / ps) / (closeadj / ps).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_min_ratio_5d_base_v096_signal'] = fis_f55_institutional_sentiment_closeadj_ps_min_ratio_5d_base_v096_signal

def fis_f55_institutional_sentiment_closeadj_ps_diff_5d_base_v097_signal(closeadj, ps):
    res = (closeadj / ps).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_diff_5d_base_v097_signal'] = fis_f55_institutional_sentiment_closeadj_ps_diff_5d_base_v097_signal

def fis_f55_institutional_sentiment_closeadj_ps_skew_5d_base_v098_signal(closeadj, ps):
    res = (closeadj / ps).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_skew_5d_base_v098_signal'] = fis_f55_institutional_sentiment_closeadj_ps_skew_5d_base_v098_signal

def fis_f55_institutional_sentiment_closeadj_ps_kurt_5d_base_v099_signal(closeadj, ps):
    res = (closeadj / ps).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_kurt_5d_base_v099_signal'] = fis_f55_institutional_sentiment_closeadj_ps_kurt_5d_base_v099_signal

def fis_f55_institutional_sentiment_closeadj_ps_rank_5d_base_v100_signal(closeadj, ps):
    res = (closeadj / ps).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_ps_rank_5d_base_v100_signal'] = fis_f55_institutional_sentiment_closeadj_ps_rank_5d_base_v100_signal

def fis_f55_institutional_sentiment_closeadj_fcf_mean_5d_base_v101_signal(closeadj, fcf):
    res = (closeadj / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_mean_5d_base_v101_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_mean_5d_base_v101_signal

def fis_f55_institutional_sentiment_closeadj_fcf_std_5d_base_v102_signal(closeadj, fcf):
    res = (closeadj / fcf).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_std_5d_base_v102_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_std_5d_base_v102_signal

def fis_f55_institutional_sentiment_closeadj_fcf_pct_chg_5d_base_v103_signal(closeadj, fcf):
    res = (closeadj / fcf).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_pct_chg_5d_base_v103_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_pct_chg_5d_base_v103_signal

def fis_f55_institutional_sentiment_closeadj_fcf_mean_ratio_5d_base_v104_signal(closeadj, fcf):
    res = (closeadj / fcf) / (closeadj / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_mean_ratio_5d_base_v104_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_mean_ratio_5d_base_v104_signal

def fis_f55_institutional_sentiment_closeadj_fcf_max_ratio_5d_base_v105_signal(closeadj, fcf):
    res = (closeadj / fcf) / (closeadj / fcf).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_max_ratio_5d_base_v105_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_max_ratio_5d_base_v105_signal

def fis_f55_institutional_sentiment_closeadj_fcf_min_ratio_5d_base_v106_signal(closeadj, fcf):
    res = (closeadj / fcf) / (closeadj / fcf).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_min_ratio_5d_base_v106_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_min_ratio_5d_base_v106_signal

def fis_f55_institutional_sentiment_closeadj_fcf_diff_5d_base_v107_signal(closeadj, fcf):
    res = (closeadj / fcf).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_diff_5d_base_v107_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_diff_5d_base_v107_signal

def fis_f55_institutional_sentiment_closeadj_fcf_skew_5d_base_v108_signal(closeadj, fcf):
    res = (closeadj / fcf).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_skew_5d_base_v108_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_skew_5d_base_v108_signal

def fis_f55_institutional_sentiment_closeadj_fcf_kurt_5d_base_v109_signal(closeadj, fcf):
    res = (closeadj / fcf).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_kurt_5d_base_v109_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_kurt_5d_base_v109_signal

def fis_f55_institutional_sentiment_closeadj_fcf_rank_5d_base_v110_signal(closeadj, fcf):
    res = (closeadj / fcf).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_fcf_rank_5d_base_v110_signal'] = fis_f55_institutional_sentiment_closeadj_fcf_rank_5d_base_v110_signal

def fis_f55_institutional_sentiment_pe_marketcap_mean_5d_base_v111_signal(pe, marketcap):
    res = (pe / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_mean_5d_base_v111_signal'] = fis_f55_institutional_sentiment_pe_marketcap_mean_5d_base_v111_signal

def fis_f55_institutional_sentiment_pe_marketcap_std_5d_base_v112_signal(pe, marketcap):
    res = (pe / marketcap).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_std_5d_base_v112_signal'] = fis_f55_institutional_sentiment_pe_marketcap_std_5d_base_v112_signal

def fis_f55_institutional_sentiment_pe_marketcap_pct_chg_5d_base_v113_signal(pe, marketcap):
    res = (pe / marketcap).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_pct_chg_5d_base_v113_signal'] = fis_f55_institutional_sentiment_pe_marketcap_pct_chg_5d_base_v113_signal

def fis_f55_institutional_sentiment_pe_marketcap_mean_ratio_5d_base_v114_signal(pe, marketcap):
    res = (pe / marketcap) / (pe / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_mean_ratio_5d_base_v114_signal'] = fis_f55_institutional_sentiment_pe_marketcap_mean_ratio_5d_base_v114_signal

def fis_f55_institutional_sentiment_pe_marketcap_max_ratio_5d_base_v115_signal(pe, marketcap):
    res = (pe / marketcap) / (pe / marketcap).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_max_ratio_5d_base_v115_signal'] = fis_f55_institutional_sentiment_pe_marketcap_max_ratio_5d_base_v115_signal

def fis_f55_institutional_sentiment_pe_marketcap_min_ratio_5d_base_v116_signal(pe, marketcap):
    res = (pe / marketcap) / (pe / marketcap).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_min_ratio_5d_base_v116_signal'] = fis_f55_institutional_sentiment_pe_marketcap_min_ratio_5d_base_v116_signal

def fis_f55_institutional_sentiment_pe_marketcap_diff_5d_base_v117_signal(pe, marketcap):
    res = (pe / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_diff_5d_base_v117_signal'] = fis_f55_institutional_sentiment_pe_marketcap_diff_5d_base_v117_signal

def fis_f55_institutional_sentiment_pe_marketcap_skew_5d_base_v118_signal(pe, marketcap):
    res = (pe / marketcap).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_skew_5d_base_v118_signal'] = fis_f55_institutional_sentiment_pe_marketcap_skew_5d_base_v118_signal

def fis_f55_institutional_sentiment_pe_marketcap_kurt_5d_base_v119_signal(pe, marketcap):
    res = (pe / marketcap).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_kurt_5d_base_v119_signal'] = fis_f55_institutional_sentiment_pe_marketcap_kurt_5d_base_v119_signal

def fis_f55_institutional_sentiment_pe_marketcap_rank_5d_base_v120_signal(pe, marketcap):
    res = (pe / marketcap).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_marketcap_rank_5d_base_v120_signal'] = fis_f55_institutional_sentiment_pe_marketcap_rank_5d_base_v120_signal

def fis_f55_institutional_sentiment_pe_closeadj_mean_5d_base_v121_signal(pe, closeadj):
    res = (pe / closeadj).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_mean_5d_base_v121_signal'] = fis_f55_institutional_sentiment_pe_closeadj_mean_5d_base_v121_signal

def fis_f55_institutional_sentiment_pe_closeadj_std_5d_base_v122_signal(pe, closeadj):
    res = (pe / closeadj).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_std_5d_base_v122_signal'] = fis_f55_institutional_sentiment_pe_closeadj_std_5d_base_v122_signal

def fis_f55_institutional_sentiment_pe_closeadj_pct_chg_5d_base_v123_signal(pe, closeadj):
    res = (pe / closeadj).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_pct_chg_5d_base_v123_signal'] = fis_f55_institutional_sentiment_pe_closeadj_pct_chg_5d_base_v123_signal

def fis_f55_institutional_sentiment_pe_closeadj_mean_ratio_5d_base_v124_signal(pe, closeadj):
    res = (pe / closeadj) / (pe / closeadj).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_mean_ratio_5d_base_v124_signal'] = fis_f55_institutional_sentiment_pe_closeadj_mean_ratio_5d_base_v124_signal

def fis_f55_institutional_sentiment_pe_closeadj_max_ratio_5d_base_v125_signal(pe, closeadj):
    res = (pe / closeadj) / (pe / closeadj).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_max_ratio_5d_base_v125_signal'] = fis_f55_institutional_sentiment_pe_closeadj_max_ratio_5d_base_v125_signal

def fis_f55_institutional_sentiment_pe_closeadj_min_ratio_5d_base_v126_signal(pe, closeadj):
    res = (pe / closeadj) / (pe / closeadj).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_min_ratio_5d_base_v126_signal'] = fis_f55_institutional_sentiment_pe_closeadj_min_ratio_5d_base_v126_signal

def fis_f55_institutional_sentiment_pe_closeadj_diff_5d_base_v127_signal(pe, closeadj):
    res = (pe / closeadj).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_diff_5d_base_v127_signal'] = fis_f55_institutional_sentiment_pe_closeadj_diff_5d_base_v127_signal

def fis_f55_institutional_sentiment_pe_closeadj_skew_5d_base_v128_signal(pe, closeadj):
    res = (pe / closeadj).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_skew_5d_base_v128_signal'] = fis_f55_institutional_sentiment_pe_closeadj_skew_5d_base_v128_signal

def fis_f55_institutional_sentiment_pe_closeadj_kurt_5d_base_v129_signal(pe, closeadj):
    res = (pe / closeadj).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_kurt_5d_base_v129_signal'] = fis_f55_institutional_sentiment_pe_closeadj_kurt_5d_base_v129_signal

def fis_f55_institutional_sentiment_pe_closeadj_rank_5d_base_v130_signal(pe, closeadj):
    res = (pe / closeadj).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_closeadj_rank_5d_base_v130_signal'] = fis_f55_institutional_sentiment_pe_closeadj_rank_5d_base_v130_signal

def fis_f55_institutional_sentiment_pe_mean_5d_base_v131_signal(pe):
    res = pe.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_mean_5d_base_v131_signal'] = fis_f55_institutional_sentiment_pe_mean_5d_base_v131_signal

def fis_f55_institutional_sentiment_pe_std_5d_base_v132_signal(pe):
    res = pe.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_std_5d_base_v132_signal'] = fis_f55_institutional_sentiment_pe_std_5d_base_v132_signal

def fis_f55_institutional_sentiment_pe_pct_chg_5d_base_v133_signal(pe):
    res = pe.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pct_chg_5d_base_v133_signal'] = fis_f55_institutional_sentiment_pe_pct_chg_5d_base_v133_signal

def fis_f55_institutional_sentiment_pe_max_ratio_5d_base_v134_signal(pe):
    res = pe / pe.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_max_ratio_5d_base_v134_signal'] = fis_f55_institutional_sentiment_pe_max_ratio_5d_base_v134_signal

def fis_f55_institutional_sentiment_pe_min_ratio_5d_base_v135_signal(pe):
    res = pe / pe.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_min_ratio_5d_base_v135_signal'] = fis_f55_institutional_sentiment_pe_min_ratio_5d_base_v135_signal

def fis_f55_institutional_sentiment_pe_pb_mean_5d_base_v136_signal(pe, pb):
    res = (pe / pb).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_mean_5d_base_v136_signal'] = fis_f55_institutional_sentiment_pe_pb_mean_5d_base_v136_signal

def fis_f55_institutional_sentiment_pe_pb_std_5d_base_v137_signal(pe, pb):
    res = (pe / pb).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_std_5d_base_v137_signal'] = fis_f55_institutional_sentiment_pe_pb_std_5d_base_v137_signal

def fis_f55_institutional_sentiment_pe_pb_pct_chg_5d_base_v138_signal(pe, pb):
    res = (pe / pb).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_pct_chg_5d_base_v138_signal'] = fis_f55_institutional_sentiment_pe_pb_pct_chg_5d_base_v138_signal

def fis_f55_institutional_sentiment_pe_pb_mean_ratio_5d_base_v139_signal(pe, pb):
    res = (pe / pb) / (pe / pb).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_mean_ratio_5d_base_v139_signal'] = fis_f55_institutional_sentiment_pe_pb_mean_ratio_5d_base_v139_signal

def fis_f55_institutional_sentiment_pe_pb_max_ratio_5d_base_v140_signal(pe, pb):
    res = (pe / pb) / (pe / pb).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_max_ratio_5d_base_v140_signal'] = fis_f55_institutional_sentiment_pe_pb_max_ratio_5d_base_v140_signal

def fis_f55_institutional_sentiment_pe_pb_min_ratio_5d_base_v141_signal(pe, pb):
    res = (pe / pb) / (pe / pb).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_min_ratio_5d_base_v141_signal'] = fis_f55_institutional_sentiment_pe_pb_min_ratio_5d_base_v141_signal

def fis_f55_institutional_sentiment_pe_pb_diff_5d_base_v142_signal(pe, pb):
    res = (pe / pb).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_diff_5d_base_v142_signal'] = fis_f55_institutional_sentiment_pe_pb_diff_5d_base_v142_signal

def fis_f55_institutional_sentiment_pe_pb_skew_5d_base_v143_signal(pe, pb):
    res = (pe / pb).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_skew_5d_base_v143_signal'] = fis_f55_institutional_sentiment_pe_pb_skew_5d_base_v143_signal

def fis_f55_institutional_sentiment_pe_pb_kurt_5d_base_v144_signal(pe, pb):
    res = (pe / pb).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_kurt_5d_base_v144_signal'] = fis_f55_institutional_sentiment_pe_pb_kurt_5d_base_v144_signal

def fis_f55_institutional_sentiment_pe_pb_rank_5d_base_v145_signal(pe, pb):
    res = (pe / pb).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_pb_rank_5d_base_v145_signal'] = fis_f55_institutional_sentiment_pe_pb_rank_5d_base_v145_signal

def fis_f55_institutional_sentiment_pe_ps_mean_5d_base_v146_signal(pe, ps):
    res = (pe / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_ps_mean_5d_base_v146_signal'] = fis_f55_institutional_sentiment_pe_ps_mean_5d_base_v146_signal

def fis_f55_institutional_sentiment_pe_ps_std_5d_base_v147_signal(pe, ps):
    res = (pe / ps).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_ps_std_5d_base_v147_signal'] = fis_f55_institutional_sentiment_pe_ps_std_5d_base_v147_signal

def fis_f55_institutional_sentiment_pe_ps_pct_chg_5d_base_v148_signal(pe, ps):
    res = (pe / ps).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_ps_pct_chg_5d_base_v148_signal'] = fis_f55_institutional_sentiment_pe_ps_pct_chg_5d_base_v148_signal

def fis_f55_institutional_sentiment_pe_ps_mean_ratio_5d_base_v149_signal(pe, ps):
    res = (pe / ps) / (pe / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_ps_mean_ratio_5d_base_v149_signal'] = fis_f55_institutional_sentiment_pe_ps_mean_ratio_5d_base_v149_signal

def fis_f55_institutional_sentiment_pe_ps_max_ratio_5d_base_v150_signal(pe, ps):
    res = (pe / ps) / (pe / ps).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pe_ps_max_ratio_5d_base_v150_signal'] = fis_f55_institutional_sentiment_pe_ps_max_ratio_5d_base_v150_signal

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
