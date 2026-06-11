import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fis_f55_institutional_sentiment_marketcap_mean_5d_base_v001_signal(marketcap):
    res = marketcap.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_mean_5d_base_v001_signal'] = fis_f55_institutional_sentiment_marketcap_mean_5d_base_v001_signal

def fis_f55_institutional_sentiment_marketcap_std_5d_base_v002_signal(marketcap):
    res = marketcap.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_std_5d_base_v002_signal'] = fis_f55_institutional_sentiment_marketcap_std_5d_base_v002_signal

def fis_f55_institutional_sentiment_marketcap_pct_chg_5d_base_v003_signal(marketcap):
    res = marketcap.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pct_chg_5d_base_v003_signal'] = fis_f55_institutional_sentiment_marketcap_pct_chg_5d_base_v003_signal

def fis_f55_institutional_sentiment_marketcap_max_ratio_5d_base_v004_signal(marketcap):
    res = marketcap / marketcap.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_max_ratio_5d_base_v004_signal'] = fis_f55_institutional_sentiment_marketcap_max_ratio_5d_base_v004_signal

def fis_f55_institutional_sentiment_marketcap_min_ratio_5d_base_v005_signal(marketcap):
    res = marketcap / marketcap.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_min_ratio_5d_base_v005_signal'] = fis_f55_institutional_sentiment_marketcap_min_ratio_5d_base_v005_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_mean_5d_base_v006_signal(marketcap, closeadj):
    res = (marketcap / closeadj).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_mean_5d_base_v006_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_mean_5d_base_v006_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_std_5d_base_v007_signal(marketcap, closeadj):
    res = (marketcap / closeadj).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_std_5d_base_v007_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_std_5d_base_v007_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_pct_chg_5d_base_v008_signal(marketcap, closeadj):
    res = (marketcap / closeadj).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_pct_chg_5d_base_v008_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_pct_chg_5d_base_v008_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_mean_ratio_5d_base_v009_signal(marketcap, closeadj):
    res = (marketcap / closeadj) / (marketcap / closeadj).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_mean_ratio_5d_base_v009_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_mean_ratio_5d_base_v009_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_max_ratio_5d_base_v010_signal(marketcap, closeadj):
    res = (marketcap / closeadj) / (marketcap / closeadj).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_max_ratio_5d_base_v010_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_max_ratio_5d_base_v010_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_min_ratio_5d_base_v011_signal(marketcap, closeadj):
    res = (marketcap / closeadj) / (marketcap / closeadj).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_min_ratio_5d_base_v011_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_min_ratio_5d_base_v011_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_diff_5d_base_v012_signal(marketcap, closeadj):
    res = (marketcap / closeadj).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_diff_5d_base_v012_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_diff_5d_base_v012_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_skew_5d_base_v013_signal(marketcap, closeadj):
    res = (marketcap / closeadj).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_skew_5d_base_v013_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_skew_5d_base_v013_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_kurt_5d_base_v014_signal(marketcap, closeadj):
    res = (marketcap / closeadj).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_kurt_5d_base_v014_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_kurt_5d_base_v014_signal

def fis_f55_institutional_sentiment_marketcap_closeadj_rank_5d_base_v015_signal(marketcap, closeadj):
    res = (marketcap / closeadj).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_closeadj_rank_5d_base_v015_signal'] = fis_f55_institutional_sentiment_marketcap_closeadj_rank_5d_base_v015_signal

def fis_f55_institutional_sentiment_marketcap_pe_mean_5d_base_v016_signal(marketcap, pe):
    res = (marketcap / pe).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_mean_5d_base_v016_signal'] = fis_f55_institutional_sentiment_marketcap_pe_mean_5d_base_v016_signal

def fis_f55_institutional_sentiment_marketcap_pe_std_5d_base_v017_signal(marketcap, pe):
    res = (marketcap / pe).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_std_5d_base_v017_signal'] = fis_f55_institutional_sentiment_marketcap_pe_std_5d_base_v017_signal

def fis_f55_institutional_sentiment_marketcap_pe_pct_chg_5d_base_v018_signal(marketcap, pe):
    res = (marketcap / pe).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_pct_chg_5d_base_v018_signal'] = fis_f55_institutional_sentiment_marketcap_pe_pct_chg_5d_base_v018_signal

def fis_f55_institutional_sentiment_marketcap_pe_mean_ratio_5d_base_v019_signal(marketcap, pe):
    res = (marketcap / pe) / (marketcap / pe).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_mean_ratio_5d_base_v019_signal'] = fis_f55_institutional_sentiment_marketcap_pe_mean_ratio_5d_base_v019_signal

def fis_f55_institutional_sentiment_marketcap_pe_max_ratio_5d_base_v020_signal(marketcap, pe):
    res = (marketcap / pe) / (marketcap / pe).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_max_ratio_5d_base_v020_signal'] = fis_f55_institutional_sentiment_marketcap_pe_max_ratio_5d_base_v020_signal

def fis_f55_institutional_sentiment_marketcap_pe_min_ratio_5d_base_v021_signal(marketcap, pe):
    res = (marketcap / pe) / (marketcap / pe).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_min_ratio_5d_base_v021_signal'] = fis_f55_institutional_sentiment_marketcap_pe_min_ratio_5d_base_v021_signal

def fis_f55_institutional_sentiment_marketcap_pe_diff_5d_base_v022_signal(marketcap, pe):
    res = (marketcap / pe).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_diff_5d_base_v022_signal'] = fis_f55_institutional_sentiment_marketcap_pe_diff_5d_base_v022_signal

def fis_f55_institutional_sentiment_marketcap_pe_skew_5d_base_v023_signal(marketcap, pe):
    res = (marketcap / pe).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_skew_5d_base_v023_signal'] = fis_f55_institutional_sentiment_marketcap_pe_skew_5d_base_v023_signal

def fis_f55_institutional_sentiment_marketcap_pe_kurt_5d_base_v024_signal(marketcap, pe):
    res = (marketcap / pe).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_kurt_5d_base_v024_signal'] = fis_f55_institutional_sentiment_marketcap_pe_kurt_5d_base_v024_signal

def fis_f55_institutional_sentiment_marketcap_pe_rank_5d_base_v025_signal(marketcap, pe):
    res = (marketcap / pe).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pe_rank_5d_base_v025_signal'] = fis_f55_institutional_sentiment_marketcap_pe_rank_5d_base_v025_signal

def fis_f55_institutional_sentiment_marketcap_pb_mean_5d_base_v026_signal(marketcap, pb):
    res = (marketcap / pb).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_mean_5d_base_v026_signal'] = fis_f55_institutional_sentiment_marketcap_pb_mean_5d_base_v026_signal

def fis_f55_institutional_sentiment_marketcap_pb_std_5d_base_v027_signal(marketcap, pb):
    res = (marketcap / pb).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_std_5d_base_v027_signal'] = fis_f55_institutional_sentiment_marketcap_pb_std_5d_base_v027_signal

def fis_f55_institutional_sentiment_marketcap_pb_pct_chg_5d_base_v028_signal(marketcap, pb):
    res = (marketcap / pb).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_pct_chg_5d_base_v028_signal'] = fis_f55_institutional_sentiment_marketcap_pb_pct_chg_5d_base_v028_signal

def fis_f55_institutional_sentiment_marketcap_pb_mean_ratio_5d_base_v029_signal(marketcap, pb):
    res = (marketcap / pb) / (marketcap / pb).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_mean_ratio_5d_base_v029_signal'] = fis_f55_institutional_sentiment_marketcap_pb_mean_ratio_5d_base_v029_signal

def fis_f55_institutional_sentiment_marketcap_pb_max_ratio_5d_base_v030_signal(marketcap, pb):
    res = (marketcap / pb) / (marketcap / pb).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_max_ratio_5d_base_v030_signal'] = fis_f55_institutional_sentiment_marketcap_pb_max_ratio_5d_base_v030_signal

def fis_f55_institutional_sentiment_marketcap_pb_min_ratio_5d_base_v031_signal(marketcap, pb):
    res = (marketcap / pb) / (marketcap / pb).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_min_ratio_5d_base_v031_signal'] = fis_f55_institutional_sentiment_marketcap_pb_min_ratio_5d_base_v031_signal

def fis_f55_institutional_sentiment_marketcap_pb_diff_5d_base_v032_signal(marketcap, pb):
    res = (marketcap / pb).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_diff_5d_base_v032_signal'] = fis_f55_institutional_sentiment_marketcap_pb_diff_5d_base_v032_signal

def fis_f55_institutional_sentiment_marketcap_pb_skew_5d_base_v033_signal(marketcap, pb):
    res = (marketcap / pb).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_skew_5d_base_v033_signal'] = fis_f55_institutional_sentiment_marketcap_pb_skew_5d_base_v033_signal

def fis_f55_institutional_sentiment_marketcap_pb_kurt_5d_base_v034_signal(marketcap, pb):
    res = (marketcap / pb).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_kurt_5d_base_v034_signal'] = fis_f55_institutional_sentiment_marketcap_pb_kurt_5d_base_v034_signal

def fis_f55_institutional_sentiment_marketcap_pb_rank_5d_base_v035_signal(marketcap, pb):
    res = (marketcap / pb).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_pb_rank_5d_base_v035_signal'] = fis_f55_institutional_sentiment_marketcap_pb_rank_5d_base_v035_signal

def fis_f55_institutional_sentiment_marketcap_ps_mean_5d_base_v036_signal(marketcap, ps):
    res = (marketcap / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_mean_5d_base_v036_signal'] = fis_f55_institutional_sentiment_marketcap_ps_mean_5d_base_v036_signal

def fis_f55_institutional_sentiment_marketcap_ps_std_5d_base_v037_signal(marketcap, ps):
    res = (marketcap / ps).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_std_5d_base_v037_signal'] = fis_f55_institutional_sentiment_marketcap_ps_std_5d_base_v037_signal

def fis_f55_institutional_sentiment_marketcap_ps_pct_chg_5d_base_v038_signal(marketcap, ps):
    res = (marketcap / ps).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_pct_chg_5d_base_v038_signal'] = fis_f55_institutional_sentiment_marketcap_ps_pct_chg_5d_base_v038_signal

def fis_f55_institutional_sentiment_marketcap_ps_mean_ratio_5d_base_v039_signal(marketcap, ps):
    res = (marketcap / ps) / (marketcap / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_mean_ratio_5d_base_v039_signal'] = fis_f55_institutional_sentiment_marketcap_ps_mean_ratio_5d_base_v039_signal

def fis_f55_institutional_sentiment_marketcap_ps_max_ratio_5d_base_v040_signal(marketcap, ps):
    res = (marketcap / ps) / (marketcap / ps).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_max_ratio_5d_base_v040_signal'] = fis_f55_institutional_sentiment_marketcap_ps_max_ratio_5d_base_v040_signal

def fis_f55_institutional_sentiment_marketcap_ps_min_ratio_5d_base_v041_signal(marketcap, ps):
    res = (marketcap / ps) / (marketcap / ps).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_min_ratio_5d_base_v041_signal'] = fis_f55_institutional_sentiment_marketcap_ps_min_ratio_5d_base_v041_signal

def fis_f55_institutional_sentiment_marketcap_ps_diff_5d_base_v042_signal(marketcap, ps):
    res = (marketcap / ps).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_diff_5d_base_v042_signal'] = fis_f55_institutional_sentiment_marketcap_ps_diff_5d_base_v042_signal

def fis_f55_institutional_sentiment_marketcap_ps_skew_5d_base_v043_signal(marketcap, ps):
    res = (marketcap / ps).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_skew_5d_base_v043_signal'] = fis_f55_institutional_sentiment_marketcap_ps_skew_5d_base_v043_signal

def fis_f55_institutional_sentiment_marketcap_ps_kurt_5d_base_v044_signal(marketcap, ps):
    res = (marketcap / ps).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_kurt_5d_base_v044_signal'] = fis_f55_institutional_sentiment_marketcap_ps_kurt_5d_base_v044_signal

def fis_f55_institutional_sentiment_marketcap_ps_rank_5d_base_v045_signal(marketcap, ps):
    res = (marketcap / ps).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_ps_rank_5d_base_v045_signal'] = fis_f55_institutional_sentiment_marketcap_ps_rank_5d_base_v045_signal

def fis_f55_institutional_sentiment_marketcap_fcf_mean_5d_base_v046_signal(marketcap, fcf):
    res = (marketcap / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_mean_5d_base_v046_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_mean_5d_base_v046_signal

def fis_f55_institutional_sentiment_marketcap_fcf_std_5d_base_v047_signal(marketcap, fcf):
    res = (marketcap / fcf).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_std_5d_base_v047_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_std_5d_base_v047_signal

def fis_f55_institutional_sentiment_marketcap_fcf_pct_chg_5d_base_v048_signal(marketcap, fcf):
    res = (marketcap / fcf).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_pct_chg_5d_base_v048_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_pct_chg_5d_base_v048_signal

def fis_f55_institutional_sentiment_marketcap_fcf_mean_ratio_5d_base_v049_signal(marketcap, fcf):
    res = (marketcap / fcf) / (marketcap / fcf).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_mean_ratio_5d_base_v049_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_mean_ratio_5d_base_v049_signal

def fis_f55_institutional_sentiment_marketcap_fcf_max_ratio_5d_base_v050_signal(marketcap, fcf):
    res = (marketcap / fcf) / (marketcap / fcf).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_max_ratio_5d_base_v050_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_max_ratio_5d_base_v050_signal

def fis_f55_institutional_sentiment_marketcap_fcf_min_ratio_5d_base_v051_signal(marketcap, fcf):
    res = (marketcap / fcf) / (marketcap / fcf).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_min_ratio_5d_base_v051_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_min_ratio_5d_base_v051_signal

def fis_f55_institutional_sentiment_marketcap_fcf_diff_5d_base_v052_signal(marketcap, fcf):
    res = (marketcap / fcf).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_diff_5d_base_v052_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_diff_5d_base_v052_signal

def fis_f55_institutional_sentiment_marketcap_fcf_skew_5d_base_v053_signal(marketcap, fcf):
    res = (marketcap / fcf).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_skew_5d_base_v053_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_skew_5d_base_v053_signal

def fis_f55_institutional_sentiment_marketcap_fcf_kurt_5d_base_v054_signal(marketcap, fcf):
    res = (marketcap / fcf).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_kurt_5d_base_v054_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_kurt_5d_base_v054_signal

def fis_f55_institutional_sentiment_marketcap_fcf_rank_5d_base_v055_signal(marketcap, fcf):
    res = (marketcap / fcf).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_marketcap_fcf_rank_5d_base_v055_signal'] = fis_f55_institutional_sentiment_marketcap_fcf_rank_5d_base_v055_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_mean_5d_base_v056_signal(closeadj, marketcap):
    res = (closeadj / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_mean_5d_base_v056_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_mean_5d_base_v056_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_std_5d_base_v057_signal(closeadj, marketcap):
    res = (closeadj / marketcap).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_std_5d_base_v057_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_std_5d_base_v057_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_pct_chg_5d_base_v058_signal(closeadj, marketcap):
    res = (closeadj / marketcap).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_pct_chg_5d_base_v058_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_pct_chg_5d_base_v058_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_mean_ratio_5d_base_v059_signal(closeadj, marketcap):
    res = (closeadj / marketcap) / (closeadj / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_mean_ratio_5d_base_v059_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_mean_ratio_5d_base_v059_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_max_ratio_5d_base_v060_signal(closeadj, marketcap):
    res = (closeadj / marketcap) / (closeadj / marketcap).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_max_ratio_5d_base_v060_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_max_ratio_5d_base_v060_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_min_ratio_5d_base_v061_signal(closeadj, marketcap):
    res = (closeadj / marketcap) / (closeadj / marketcap).rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_min_ratio_5d_base_v061_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_min_ratio_5d_base_v061_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_diff_5d_base_v062_signal(closeadj, marketcap):
    res = (closeadj / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_diff_5d_base_v062_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_diff_5d_base_v062_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_skew_5d_base_v063_signal(closeadj, marketcap):
    res = (closeadj / marketcap).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_skew_5d_base_v063_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_skew_5d_base_v063_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_kurt_5d_base_v064_signal(closeadj, marketcap):
    res = (closeadj / marketcap).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_kurt_5d_base_v064_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_kurt_5d_base_v064_signal

def fis_f55_institutional_sentiment_closeadj_marketcap_rank_5d_base_v065_signal(closeadj, marketcap):
    res = (closeadj / marketcap).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_marketcap_rank_5d_base_v065_signal'] = fis_f55_institutional_sentiment_closeadj_marketcap_rank_5d_base_v065_signal

def fis_f55_institutional_sentiment_closeadj_mean_5d_base_v066_signal(closeadj):
    res = closeadj.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_mean_5d_base_v066_signal'] = fis_f55_institutional_sentiment_closeadj_mean_5d_base_v066_signal

def fis_f55_institutional_sentiment_closeadj_std_5d_base_v067_signal(closeadj):
    res = closeadj.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_std_5d_base_v067_signal'] = fis_f55_institutional_sentiment_closeadj_std_5d_base_v067_signal

def fis_f55_institutional_sentiment_closeadj_pct_chg_5d_base_v068_signal(closeadj):
    res = closeadj.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pct_chg_5d_base_v068_signal'] = fis_f55_institutional_sentiment_closeadj_pct_chg_5d_base_v068_signal

def fis_f55_institutional_sentiment_closeadj_max_ratio_5d_base_v069_signal(closeadj):
    res = closeadj / closeadj.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_max_ratio_5d_base_v069_signal'] = fis_f55_institutional_sentiment_closeadj_max_ratio_5d_base_v069_signal

def fis_f55_institutional_sentiment_closeadj_min_ratio_5d_base_v070_signal(closeadj):
    res = closeadj / closeadj.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_min_ratio_5d_base_v070_signal'] = fis_f55_institutional_sentiment_closeadj_min_ratio_5d_base_v070_signal

def fis_f55_institutional_sentiment_closeadj_pe_mean_5d_base_v071_signal(closeadj, pe):
    res = (closeadj / pe).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_mean_5d_base_v071_signal'] = fis_f55_institutional_sentiment_closeadj_pe_mean_5d_base_v071_signal

def fis_f55_institutional_sentiment_closeadj_pe_std_5d_base_v072_signal(closeadj, pe):
    res = (closeadj / pe).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_std_5d_base_v072_signal'] = fis_f55_institutional_sentiment_closeadj_pe_std_5d_base_v072_signal

def fis_f55_institutional_sentiment_closeadj_pe_pct_chg_5d_base_v073_signal(closeadj, pe):
    res = (closeadj / pe).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_pct_chg_5d_base_v073_signal'] = fis_f55_institutional_sentiment_closeadj_pe_pct_chg_5d_base_v073_signal

def fis_f55_institutional_sentiment_closeadj_pe_mean_ratio_5d_base_v074_signal(closeadj, pe):
    res = (closeadj / pe) / (closeadj / pe).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_mean_ratio_5d_base_v074_signal'] = fis_f55_institutional_sentiment_closeadj_pe_mean_ratio_5d_base_v074_signal

def fis_f55_institutional_sentiment_closeadj_pe_max_ratio_5d_base_v075_signal(closeadj, pe):
    res = (closeadj / pe) / (closeadj / pe).rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_closeadj_pe_max_ratio_5d_base_v075_signal'] = fis_f55_institutional_sentiment_closeadj_pe_max_ratio_5d_base_v075_signal

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
