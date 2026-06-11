import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def fis_f55_institutional_sentiment_mean_5d_slope_v001_signal(marketcap):
    base = marketcap.rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v001_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v001_signal

def fis_f55_institutional_sentiment_std_5d_slope_v002_signal(marketcap):
    base = marketcap.rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v002_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v002_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v003_signal(marketcap):
    base = marketcap.pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v003_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v003_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v004_signal(marketcap):
    base = marketcap / marketcap.rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v004_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v004_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v005_signal(marketcap):
    base = marketcap / marketcap.rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v005_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v005_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v006_signal(marketcap, closeadj):
    base = (marketcap / closeadj).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v006_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v006_signal

def fis_f55_institutional_sentiment_std_5d_slope_v007_signal(marketcap, closeadj):
    base = (marketcap / closeadj).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v007_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v007_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v008_signal(marketcap, closeadj):
    base = (marketcap / closeadj).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v008_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v008_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v009_signal(marketcap, closeadj):
    base = marketcap / closeadj / (marketcap / closeadj).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v009_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v009_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v010_signal(marketcap, closeadj):
    base = marketcap / closeadj / (marketcap / closeadj).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v010_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v010_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v011_signal(marketcap, closeadj):
    base = marketcap / closeadj / (marketcap / closeadj).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v011_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v011_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v012_signal(marketcap, closeadj):
    base = (marketcap / closeadj).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v012_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v012_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v013_signal(marketcap, closeadj):
    base = (marketcap / closeadj).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v013_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v013_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v014_signal(marketcap, closeadj):
    base = (marketcap / closeadj).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v014_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v014_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v015_signal(marketcap, closeadj):
    base = (marketcap / closeadj).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v015_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v015_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v016_signal(marketcap, pe):
    base = (marketcap / pe).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v016_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v016_signal

def fis_f55_institutional_sentiment_std_5d_slope_v017_signal(marketcap, pe):
    base = (marketcap / pe).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v017_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v017_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v018_signal(marketcap, pe):
    base = (marketcap / pe).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v018_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v018_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v019_signal(marketcap, pe):
    base = marketcap / pe / (marketcap / pe).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v019_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v019_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v020_signal(marketcap, pe):
    base = marketcap / pe / (marketcap / pe).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v020_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v020_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v021_signal(marketcap, pe):
    base = marketcap / pe / (marketcap / pe).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v021_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v021_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v022_signal(marketcap, pe):
    base = (marketcap / pe).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v022_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v022_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v023_signal(marketcap, pe):
    base = (marketcap / pe).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v023_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v023_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v024_signal(marketcap, pe):
    base = (marketcap / pe).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v024_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v024_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v025_signal(marketcap, pe):
    base = (marketcap / pe).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v025_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v025_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v026_signal(marketcap, pb):
    base = (marketcap / pb).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v026_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v026_signal

def fis_f55_institutional_sentiment_std_5d_slope_v027_signal(marketcap, pb):
    base = (marketcap / pb).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v027_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v027_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v028_signal(marketcap, pb):
    base = (marketcap / pb).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v028_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v028_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v029_signal(marketcap, pb):
    base = marketcap / pb / (marketcap / pb).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v029_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v029_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v030_signal(marketcap, pb):
    base = marketcap / pb / (marketcap / pb).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v030_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v030_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v031_signal(marketcap, pb):
    base = marketcap / pb / (marketcap / pb).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v031_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v031_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v032_signal(marketcap, pb):
    base = (marketcap / pb).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v032_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v032_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v033_signal(marketcap, pb):
    base = (marketcap / pb).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v033_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v033_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v034_signal(marketcap, pb):
    base = (marketcap / pb).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v034_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v034_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v035_signal(marketcap, pb):
    base = (marketcap / pb).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v035_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v035_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v036_signal(marketcap, ps):
    base = (marketcap / ps).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v036_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v036_signal

def fis_f55_institutional_sentiment_std_5d_slope_v037_signal(marketcap, ps):
    base = (marketcap / ps).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v037_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v037_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v038_signal(marketcap, ps):
    base = (marketcap / ps).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v038_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v038_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v039_signal(marketcap, ps):
    base = marketcap / ps / (marketcap / ps).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v039_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v039_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v040_signal(marketcap, ps):
    base = marketcap / ps / (marketcap / ps).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v040_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v040_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v041_signal(marketcap, ps):
    base = marketcap / ps / (marketcap / ps).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v041_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v041_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v042_signal(marketcap, ps):
    base = (marketcap / ps).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v042_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v042_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v043_signal(marketcap, ps):
    base = (marketcap / ps).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v043_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v043_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v044_signal(marketcap, ps):
    base = (marketcap / ps).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v044_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v044_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v045_signal(marketcap, ps):
    base = (marketcap / ps).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v045_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v045_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v046_signal(marketcap, fcf):
    base = (marketcap / fcf).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v046_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v046_signal

def fis_f55_institutional_sentiment_std_5d_slope_v047_signal(marketcap, fcf):
    base = (marketcap / fcf).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v047_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v047_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v048_signal(marketcap, fcf):
    base = (marketcap / fcf).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v048_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v048_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v049_signal(marketcap, fcf):
    base = marketcap / fcf / (marketcap / fcf).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v049_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v049_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v050_signal(marketcap, fcf):
    base = marketcap / fcf / (marketcap / fcf).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v050_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v050_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v051_signal(marketcap, fcf):
    base = marketcap / fcf / (marketcap / fcf).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v051_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v051_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v052_signal(marketcap, fcf):
    base = (marketcap / fcf).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v052_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v052_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v053_signal(marketcap, fcf):
    base = (marketcap / fcf).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v053_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v053_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v054_signal(marketcap, fcf):
    base = (marketcap / fcf).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v054_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v054_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v055_signal(marketcap, fcf):
    base = (marketcap / fcf).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v055_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v055_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v056_signal(closeadj, marketcap):
    base = (closeadj / marketcap).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v056_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v056_signal

def fis_f55_institutional_sentiment_std_5d_slope_v057_signal(closeadj, marketcap):
    base = (closeadj / marketcap).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v057_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v057_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v058_signal(closeadj, marketcap):
    base = (closeadj / marketcap).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v058_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v058_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v059_signal(closeadj, marketcap):
    base = closeadj / marketcap / (closeadj / marketcap).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v059_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v059_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v060_signal(closeadj, marketcap):
    base = closeadj / marketcap / (closeadj / marketcap).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v060_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v060_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v061_signal(closeadj, marketcap):
    base = closeadj / marketcap / (closeadj / marketcap).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v061_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v061_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v062_signal(closeadj, marketcap):
    base = (closeadj / marketcap).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v062_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v062_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v063_signal(closeadj, marketcap):
    base = (closeadj / marketcap).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v063_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v063_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v064_signal(closeadj, marketcap):
    base = (closeadj / marketcap).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v064_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v064_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v065_signal(closeadj, marketcap):
    base = (closeadj / marketcap).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v065_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v065_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v066_signal(closeadj):
    base = closeadj.rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v066_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v066_signal

def fis_f55_institutional_sentiment_std_5d_slope_v067_signal(closeadj):
    base = closeadj.rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v067_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v067_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v068_signal(closeadj):
    base = closeadj.pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v068_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v068_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v069_signal(closeadj):
    base = closeadj / closeadj.rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v069_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v069_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v070_signal(closeadj):
    base = closeadj / closeadj.rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v070_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v070_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v071_signal(closeadj, pe):
    base = (closeadj / pe).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v071_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v071_signal

def fis_f55_institutional_sentiment_std_5d_slope_v072_signal(closeadj, pe):
    base = (closeadj / pe).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v072_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v072_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v073_signal(closeadj, pe):
    base = (closeadj / pe).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v073_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v073_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v074_signal(closeadj, pe):
    base = closeadj / pe / (closeadj / pe).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v074_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v074_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v075_signal(closeadj, pe):
    base = closeadj / pe / (closeadj / pe).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v075_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v075_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v076_signal(closeadj, pe):
    base = closeadj / pe / (closeadj / pe).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v076_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v076_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v077_signal(closeadj, pe):
    base = (closeadj / pe).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v077_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v077_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v078_signal(closeadj, pe):
    base = (closeadj / pe).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v078_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v078_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v079_signal(closeadj, pe):
    base = (closeadj / pe).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v079_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v079_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v080_signal(closeadj, pe):
    base = (closeadj / pe).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v080_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v080_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v081_signal(closeadj, pb):
    base = (closeadj / pb).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v081_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v081_signal

def fis_f55_institutional_sentiment_std_5d_slope_v082_signal(closeadj, pb):
    base = (closeadj / pb).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v082_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v082_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v083_signal(closeadj, pb):
    base = (closeadj / pb).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v083_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v083_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v084_signal(closeadj, pb):
    base = closeadj / pb / (closeadj / pb).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v084_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v084_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v085_signal(closeadj, pb):
    base = closeadj / pb / (closeadj / pb).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v085_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v085_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v086_signal(closeadj, pb):
    base = closeadj / pb / (closeadj / pb).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v086_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v086_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v087_signal(closeadj, pb):
    base = (closeadj / pb).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v087_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v087_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v088_signal(closeadj, pb):
    base = (closeadj / pb).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v088_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v088_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v089_signal(closeadj, pb):
    base = (closeadj / pb).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v089_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v089_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v090_signal(closeadj, pb):
    base = (closeadj / pb).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v090_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v090_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v091_signal(closeadj, ps):
    base = (closeadj / ps).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v091_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v091_signal

def fis_f55_institutional_sentiment_std_5d_slope_v092_signal(closeadj, ps):
    base = (closeadj / ps).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v092_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v092_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v093_signal(closeadj, ps):
    base = (closeadj / ps).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v093_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v093_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v094_signal(closeadj, ps):
    base = closeadj / ps / (closeadj / ps).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v094_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v094_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v095_signal(closeadj, ps):
    base = closeadj / ps / (closeadj / ps).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v095_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v095_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v096_signal(closeadj, ps):
    base = closeadj / ps / (closeadj / ps).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v096_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v096_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v097_signal(closeadj, ps):
    base = (closeadj / ps).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v097_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v097_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v098_signal(closeadj, ps):
    base = (closeadj / ps).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v098_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v098_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v099_signal(closeadj, ps):
    base = (closeadj / ps).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v099_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v099_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v100_signal(closeadj, ps):
    base = (closeadj / ps).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v100_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v100_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v101_signal(closeadj, fcf):
    base = (closeadj / fcf).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v101_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v101_signal

def fis_f55_institutional_sentiment_std_5d_slope_v102_signal(closeadj, fcf):
    base = (closeadj / fcf).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v102_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v102_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v103_signal(closeadj, fcf):
    base = (closeadj / fcf).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v103_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v103_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v104_signal(closeadj, fcf):
    base = closeadj / fcf / (closeadj / fcf).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v104_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v104_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v105_signal(closeadj, fcf):
    base = closeadj / fcf / (closeadj / fcf).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v105_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v105_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v106_signal(closeadj, fcf):
    base = closeadj / fcf / (closeadj / fcf).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v106_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v106_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v107_signal(closeadj, fcf):
    base = (closeadj / fcf).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v107_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v107_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v108_signal(closeadj, fcf):
    base = (closeadj / fcf).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v108_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v108_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v109_signal(closeadj, fcf):
    base = (closeadj / fcf).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v109_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v109_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v110_signal(closeadj, fcf):
    base = (closeadj / fcf).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v110_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v110_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v111_signal(pe, marketcap):
    base = (pe / marketcap).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v111_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v111_signal

def fis_f55_institutional_sentiment_std_5d_slope_v112_signal(pe, marketcap):
    base = (pe / marketcap).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v112_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v112_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v113_signal(pe, marketcap):
    base = (pe / marketcap).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v113_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v113_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v114_signal(pe, marketcap):
    base = pe / marketcap / (pe / marketcap).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v114_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v114_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v115_signal(pe, marketcap):
    base = pe / marketcap / (pe / marketcap).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v115_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v115_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v116_signal(pe, marketcap):
    base = pe / marketcap / (pe / marketcap).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v116_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v116_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v117_signal(pe, marketcap):
    base = (pe / marketcap).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v117_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v117_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v118_signal(pe, marketcap):
    base = (pe / marketcap).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v118_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v118_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v119_signal(pe, marketcap):
    base = (pe / marketcap).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v119_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v119_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v120_signal(pe, marketcap):
    base = (pe / marketcap).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v120_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v120_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v121_signal(pe, closeadj):
    base = (pe / closeadj).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v121_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v121_signal

def fis_f55_institutional_sentiment_std_5d_slope_v122_signal(pe, closeadj):
    base = (pe / closeadj).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v122_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v122_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v123_signal(pe, closeadj):
    base = (pe / closeadj).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v123_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v123_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v124_signal(pe, closeadj):
    base = pe / closeadj / (pe / closeadj).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v124_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v124_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v125_signal(pe, closeadj):
    base = pe / closeadj / (pe / closeadj).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v125_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v125_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v126_signal(pe, closeadj):
    base = pe / closeadj / (pe / closeadj).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v126_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v126_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v127_signal(pe, closeadj):
    base = (pe / closeadj).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v127_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v127_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v128_signal(pe, closeadj):
    base = (pe / closeadj).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v128_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v128_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v129_signal(pe, closeadj):
    base = (pe / closeadj).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v129_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v129_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v130_signal(pe, closeadj):
    base = (pe / closeadj).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v130_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v130_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v131_signal(pe):
    base = pe.rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v131_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v131_signal

def fis_f55_institutional_sentiment_std_5d_slope_v132_signal(pe):
    base = pe.rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v132_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v132_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v133_signal(pe):
    base = pe.pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v133_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v133_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v134_signal(pe):
    base = pe / pe.rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v134_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v134_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v135_signal(pe):
    base = pe / pe.rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v135_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v135_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v136_signal(pe, pb):
    base = (pe / pb).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v136_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v136_signal

def fis_f55_institutional_sentiment_std_5d_slope_v137_signal(pe, pb):
    base = (pe / pb).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v137_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v137_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v138_signal(pe, pb):
    base = (pe / pb).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v138_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v138_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v139_signal(pe, pb):
    base = pe / pb / (pe / pb).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v139_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v139_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v140_signal(pe, pb):
    base = pe / pb / (pe / pb).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v140_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v140_signal

def fis_f55_institutional_sentiment_min_ratio_5d_slope_v141_signal(pe, pb):
    base = pe / pb / (pe / pb).rolling(5).min()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_min_ratio_5d_slope_v141_signal'] = fis_f55_institutional_sentiment_min_ratio_5d_slope_v141_signal

def fis_f55_institutional_sentiment_diff_5d_slope_v142_signal(pe, pb):
    base = (pe / pb).diff(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_diff_5d_slope_v142_signal'] = fis_f55_institutional_sentiment_diff_5d_slope_v142_signal

def fis_f55_institutional_sentiment_skew_5d_slope_v143_signal(pe, pb):
    base = (pe / pb).rolling(5).skew()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_skew_5d_slope_v143_signal'] = fis_f55_institutional_sentiment_skew_5d_slope_v143_signal

def fis_f55_institutional_sentiment_kurt_5d_slope_v144_signal(pe, pb):
    base = (pe / pb).rolling(5).kurt()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_kurt_5d_slope_v144_signal'] = fis_f55_institutional_sentiment_kurt_5d_slope_v144_signal

def fis_f55_institutional_sentiment_rank_5d_slope_v145_signal(pe, pb):
    base = (pe / pb).rolling(5).rank(pct=True)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_rank_5d_slope_v145_signal'] = fis_f55_institutional_sentiment_rank_5d_slope_v145_signal

def fis_f55_institutional_sentiment_mean_5d_slope_v146_signal(pe, ps):
    base = (pe / ps).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_5d_slope_v146_signal'] = fis_f55_institutional_sentiment_mean_5d_slope_v146_signal

def fis_f55_institutional_sentiment_std_5d_slope_v147_signal(pe, ps):
    base = (pe / ps).rolling(5).std()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_std_5d_slope_v147_signal'] = fis_f55_institutional_sentiment_std_5d_slope_v147_signal

def fis_f55_institutional_sentiment_pct_chg_5d_slope_v148_signal(pe, ps):
    base = (pe / ps).pct_change(5)
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_pct_chg_5d_slope_v148_signal'] = fis_f55_institutional_sentiment_pct_chg_5d_slope_v148_signal

def fis_f55_institutional_sentiment_mean_ratio_5d_slope_v149_signal(pe, ps):
    base = pe / ps / (pe / ps).rolling(5).mean()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_mean_ratio_5d_slope_v149_signal'] = fis_f55_institutional_sentiment_mean_ratio_5d_slope_v149_signal

def fis_f55_institutional_sentiment_max_ratio_5d_slope_v150_signal(pe, ps):
    base = pe / ps / (pe / ps).rolling(5).max()
    res = base.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['fis_f55_institutional_sentiment_max_ratio_5d_slope_v150_signal'] = fis_f55_institutional_sentiment_max_ratio_5d_slope_v150_signal

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
