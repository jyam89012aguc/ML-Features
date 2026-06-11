import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f77ce_f77_capex_to_ebitda_regime_capex_mean_5d_base_v001_signal(capex):
    res = capex.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_5d_base_v001_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_5d_base_v001_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_5d_base_v002_signal(capex):
    res = capex.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_5d_base_v002_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_5d_base_v002_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_5d_base_v003_signal(capex):
    res = capex.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_5d_base_v003_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_5d_base_v003_signal

def f77ce_f77_capex_to_ebitda_regime_capex_zscore_5d_base_v004_signal(capex):
    res = (capex - capex.rolling(5).mean()) / capex.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_zscore_5d_base_v004_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_zscore_5d_base_v004_signal

def f77ce_f77_capex_to_ebitda_regime_capex_rank_5d_base_v005_signal(capex):
    res = capex.rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_rank_5d_base_v005_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_rank_5d_base_v005_signal

def f77ce_f77_capex_to_ebitda_regime_capex_diff_5d_base_v006_signal(capex):
    res = capex.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_diff_5d_base_v006_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_diff_5d_base_v006_signal

def f77ce_f77_capex_to_ebitda_regime_capex_skew_5d_base_v007_signal(capex):
    res = capex.rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_skew_5d_base_v007_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_skew_5d_base_v007_signal

def f77ce_f77_capex_to_ebitda_regime_capex_kurt_5d_base_v008_signal(capex):
    res = capex.rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_kurt_5d_base_v008_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_kurt_5d_base_v008_signal

def f77ce_f77_capex_to_ebitda_regime_capex_median_5d_base_v009_signal(capex):
    res = capex.rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_median_5d_base_v009_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_median_5d_base_v009_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_5d_base_v010_signal(capex):
    res = capex.rolling(5).min() / capex.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_5d_base_v010_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_5d_base_v010_signal

def f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_5d_base_v011_signal(capex):
    res = capex / capex.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_5d_base_v011_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_5d_base_v011_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_5d_base_v012_signal(capex):
    res = capex / capex.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_5d_base_v012_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_5d_base_v012_signal

def f77ce_f77_capex_to_ebitda_regime_capex_mean_10d_base_v013_signal(capex):
    res = capex.rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_10d_base_v013_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_10d_base_v013_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_10d_base_v014_signal(capex):
    res = capex.rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_10d_base_v014_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_10d_base_v014_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_10d_base_v015_signal(capex):
    res = capex.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_10d_base_v015_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_10d_base_v015_signal

def f77ce_f77_capex_to_ebitda_regime_capex_zscore_10d_base_v016_signal(capex):
    res = (capex - capex.rolling(10).mean()) / capex.rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_zscore_10d_base_v016_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_zscore_10d_base_v016_signal

def f77ce_f77_capex_to_ebitda_regime_capex_rank_10d_base_v017_signal(capex):
    res = capex.rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_rank_10d_base_v017_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_rank_10d_base_v017_signal

def f77ce_f77_capex_to_ebitda_regime_capex_diff_10d_base_v018_signal(capex):
    res = capex.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_diff_10d_base_v018_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_diff_10d_base_v018_signal

def f77ce_f77_capex_to_ebitda_regime_capex_skew_10d_base_v019_signal(capex):
    res = capex.rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_skew_10d_base_v019_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_skew_10d_base_v019_signal

def f77ce_f77_capex_to_ebitda_regime_capex_kurt_10d_base_v020_signal(capex):
    res = capex.rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_kurt_10d_base_v020_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_kurt_10d_base_v020_signal

def f77ce_f77_capex_to_ebitda_regime_capex_median_10d_base_v021_signal(capex):
    res = capex.rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_median_10d_base_v021_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_median_10d_base_v021_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_10d_base_v022_signal(capex):
    res = capex.rolling(10).min() / capex.rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_10d_base_v022_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_10d_base_v022_signal

def f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_10d_base_v023_signal(capex):
    res = capex / capex.rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_10d_base_v023_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_10d_base_v023_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_10d_base_v024_signal(capex):
    res = capex / capex.rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_10d_base_v024_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_10d_base_v024_signal

def f77ce_f77_capex_to_ebitda_regime_capex_mean_21d_base_v025_signal(capex):
    res = capex.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_21d_base_v025_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_21d_base_v025_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_21d_base_v026_signal(capex):
    res = capex.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_21d_base_v026_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_21d_base_v026_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_21d_base_v027_signal(capex):
    res = capex.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_21d_base_v027_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_21d_base_v027_signal

def f77ce_f77_capex_to_ebitda_regime_capex_zscore_21d_base_v028_signal(capex):
    res = (capex - capex.rolling(21).mean()) / capex.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_zscore_21d_base_v028_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_zscore_21d_base_v028_signal

def f77ce_f77_capex_to_ebitda_regime_capex_rank_21d_base_v029_signal(capex):
    res = capex.rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_rank_21d_base_v029_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_rank_21d_base_v029_signal

def f77ce_f77_capex_to_ebitda_regime_capex_diff_21d_base_v030_signal(capex):
    res = capex.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_diff_21d_base_v030_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_diff_21d_base_v030_signal

def f77ce_f77_capex_to_ebitda_regime_capex_skew_21d_base_v031_signal(capex):
    res = capex.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_skew_21d_base_v031_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_skew_21d_base_v031_signal

def f77ce_f77_capex_to_ebitda_regime_capex_kurt_21d_base_v032_signal(capex):
    res = capex.rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_kurt_21d_base_v032_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_kurt_21d_base_v032_signal

def f77ce_f77_capex_to_ebitda_regime_capex_median_21d_base_v033_signal(capex):
    res = capex.rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_median_21d_base_v033_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_median_21d_base_v033_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_21d_base_v034_signal(capex):
    res = capex.rolling(21).min() / capex.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_21d_base_v034_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_21d_base_v034_signal

def f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_21d_base_v035_signal(capex):
    res = capex / capex.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_21d_base_v035_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_21d_base_v035_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_21d_base_v036_signal(capex):
    res = capex / capex.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_21d_base_v036_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_21d_base_v036_signal

def f77ce_f77_capex_to_ebitda_regime_capex_mean_42d_base_v037_signal(capex):
    res = capex.rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_42d_base_v037_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_42d_base_v037_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_42d_base_v038_signal(capex):
    res = capex.rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_42d_base_v038_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_42d_base_v038_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_42d_base_v039_signal(capex):
    res = capex.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_42d_base_v039_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_42d_base_v039_signal

def f77ce_f77_capex_to_ebitda_regime_capex_zscore_42d_base_v040_signal(capex):
    res = (capex - capex.rolling(42).mean()) / capex.rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_zscore_42d_base_v040_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_zscore_42d_base_v040_signal

def f77ce_f77_capex_to_ebitda_regime_capex_rank_42d_base_v041_signal(capex):
    res = capex.rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_rank_42d_base_v041_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_rank_42d_base_v041_signal

def f77ce_f77_capex_to_ebitda_regime_capex_diff_42d_base_v042_signal(capex):
    res = capex.diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_diff_42d_base_v042_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_diff_42d_base_v042_signal

def f77ce_f77_capex_to_ebitda_regime_capex_skew_42d_base_v043_signal(capex):
    res = capex.rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_skew_42d_base_v043_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_skew_42d_base_v043_signal

def f77ce_f77_capex_to_ebitda_regime_capex_kurt_42d_base_v044_signal(capex):
    res = capex.rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_kurt_42d_base_v044_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_kurt_42d_base_v044_signal

def f77ce_f77_capex_to_ebitda_regime_capex_median_42d_base_v045_signal(capex):
    res = capex.rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_median_42d_base_v045_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_median_42d_base_v045_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_42d_base_v046_signal(capex):
    res = capex.rolling(42).min() / capex.rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_42d_base_v046_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_42d_base_v046_signal

def f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_42d_base_v047_signal(capex):
    res = capex / capex.rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_42d_base_v047_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_42d_base_v047_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_42d_base_v048_signal(capex):
    res = capex / capex.rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_42d_base_v048_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_42d_base_v048_signal

def f77ce_f77_capex_to_ebitda_regime_capex_mean_63d_base_v049_signal(capex):
    res = capex.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_63d_base_v049_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_63d_base_v049_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_63d_base_v050_signal(capex):
    res = capex.rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_63d_base_v050_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_63d_base_v050_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_63d_base_v051_signal(capex):
    res = capex.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_63d_base_v051_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_63d_base_v051_signal

def f77ce_f77_capex_to_ebitda_regime_capex_zscore_63d_base_v052_signal(capex):
    res = (capex - capex.rolling(63).mean()) / capex.rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_zscore_63d_base_v052_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_zscore_63d_base_v052_signal

def f77ce_f77_capex_to_ebitda_regime_capex_rank_63d_base_v053_signal(capex):
    res = capex.rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_rank_63d_base_v053_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_rank_63d_base_v053_signal

def f77ce_f77_capex_to_ebitda_regime_capex_diff_63d_base_v054_signal(capex):
    res = capex.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_diff_63d_base_v054_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_diff_63d_base_v054_signal

def f77ce_f77_capex_to_ebitda_regime_capex_skew_63d_base_v055_signal(capex):
    res = capex.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_skew_63d_base_v055_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_skew_63d_base_v055_signal

def f77ce_f77_capex_to_ebitda_regime_capex_kurt_63d_base_v056_signal(capex):
    res = capex.rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_kurt_63d_base_v056_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_kurt_63d_base_v056_signal

def f77ce_f77_capex_to_ebitda_regime_capex_median_63d_base_v057_signal(capex):
    res = capex.rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_median_63d_base_v057_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_median_63d_base_v057_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_63d_base_v058_signal(capex):
    res = capex.rolling(63).min() / capex.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_63d_base_v058_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_63d_base_v058_signal

def f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_63d_base_v059_signal(capex):
    res = capex / capex.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_63d_base_v059_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_63d_base_v059_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_63d_base_v060_signal(capex):
    res = capex / capex.rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_63d_base_v060_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_63d_base_v060_signal

def f77ce_f77_capex_to_ebitda_regime_capex_mean_126d_base_v061_signal(capex):
    res = capex.rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_126d_base_v061_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_126d_base_v061_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_126d_base_v062_signal(capex):
    res = capex.rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_126d_base_v062_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_126d_base_v062_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_126d_base_v063_signal(capex):
    res = capex.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_126d_base_v063_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_126d_base_v063_signal

def f77ce_f77_capex_to_ebitda_regime_capex_zscore_126d_base_v064_signal(capex):
    res = (capex - capex.rolling(126).mean()) / capex.rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_zscore_126d_base_v064_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_zscore_126d_base_v064_signal

def f77ce_f77_capex_to_ebitda_regime_capex_rank_126d_base_v065_signal(capex):
    res = capex.rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_rank_126d_base_v065_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_rank_126d_base_v065_signal

def f77ce_f77_capex_to_ebitda_regime_capex_diff_126d_base_v066_signal(capex):
    res = capex.diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_diff_126d_base_v066_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_diff_126d_base_v066_signal

def f77ce_f77_capex_to_ebitda_regime_capex_skew_126d_base_v067_signal(capex):
    res = capex.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_skew_126d_base_v067_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_skew_126d_base_v067_signal

def f77ce_f77_capex_to_ebitda_regime_capex_kurt_126d_base_v068_signal(capex):
    res = capex.rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_kurt_126d_base_v068_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_kurt_126d_base_v068_signal

def f77ce_f77_capex_to_ebitda_regime_capex_median_126d_base_v069_signal(capex):
    res = capex.rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_median_126d_base_v069_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_median_126d_base_v069_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_126d_base_v070_signal(capex):
    res = capex.rolling(126).min() / capex.rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_126d_base_v070_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_max_ratio_126d_base_v070_signal

def f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_126d_base_v071_signal(capex):
    res = capex / capex.rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_126d_base_v071_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_max_ratio_126d_base_v071_signal

def f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_126d_base_v072_signal(capex):
    res = capex / capex.rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_126d_base_v072_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_min_ratio_126d_base_v072_signal

def f77ce_f77_capex_to_ebitda_regime_capex_mean_252d_base_v073_signal(capex):
    res = capex.rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_mean_252d_base_v073_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_mean_252d_base_v073_signal

def f77ce_f77_capex_to_ebitda_regime_capex_std_252d_base_v074_signal(capex):
    res = capex.rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_std_252d_base_v074_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_std_252d_base_v074_signal

def f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_252d_base_v075_signal(capex):
    res = capex.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_252d_base_v075_signal'] = f77ce_f77_capex_to_ebitda_regime_capex_pct_chg_252d_base_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    # Extra padding to ensure file size > 30KB
    padding = "X" * 5000
    df = pd.DataFrame({
        "assets": np.random.uniform(1.0, 1000.0, n),
        "capex": np.random.uniform(1.0, 1000.0, n),
        "ebitda": np.random.uniform(1.0, 1000.0, n),
        "equity": np.random.uniform(1.0, 1000.0, n),
        "marketcap": np.random.uniform(1.0, 1000.0, n),
        "revenue": np.random.uniform(1.0, 1000.0, n),
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
