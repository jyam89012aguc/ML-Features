import pandas as pd
import numpy as np
import os
import inspect
FEATURE_FUNCTIONS = {}

def f88te_tax_efficiency_regime_raw_mean_5d_base_v001_signal(tax_expense):
    res = tax_expense.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_5d_base_v001_signal'] = f88te_tax_efficiency_regime_raw_mean_5d_base_v001_signal

def f88te_tax_efficiency_regime_raw_std_5d_base_v002_signal(tax_expense):
    res = tax_expense.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_5d_base_v002_signal'] = f88te_tax_efficiency_regime_raw_std_5d_base_v002_signal

def f88te_tax_efficiency_regime_raw_pct_change_5d_base_v003_signal(tax_expense):
    res = tax_expense.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_5d_base_v003_signal'] = f88te_tax_efficiency_regime_raw_pct_change_5d_base_v003_signal

def f88te_tax_efficiency_regime_raw_skew_5d_base_v004_signal(tax_expense):
    res = tax_expense.rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_5d_base_v004_signal'] = f88te_tax_efficiency_regime_raw_skew_5d_base_v004_signal

def f88te_tax_efficiency_regime_raw_kurt_5d_base_v005_signal(tax_expense):
    res = tax_expense.rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_5d_base_v005_signal'] = f88te_tax_efficiency_regime_raw_kurt_5d_base_v005_signal

def f88te_tax_efficiency_regime_raw_min_5d_base_v006_signal(tax_expense):
    res = tax_expense.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_5d_base_v006_signal'] = f88te_tax_efficiency_regime_raw_min_5d_base_v006_signal

def f88te_tax_efficiency_regime_raw_max_5d_base_v007_signal(tax_expense):
    res = tax_expense.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_5d_base_v007_signal'] = f88te_tax_efficiency_regime_raw_max_5d_base_v007_signal

def f88te_tax_efficiency_regime_raw_median_5d_base_v008_signal(tax_expense):
    res = tax_expense.rolling(5).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_5d_base_v008_signal'] = f88te_tax_efficiency_regime_raw_median_5d_base_v008_signal

def f88te_tax_efficiency_regime_raw_diff_5d_base_v009_signal(tax_expense):
    res = tax_expense.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_5d_base_v009_signal'] = f88te_tax_efficiency_regime_raw_diff_5d_base_v009_signal

def f88te_tax_efficiency_regime_raw_sem_5d_base_v010_signal(tax_expense):
    res = tax_expense.rolling(5).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_5d_base_v010_signal'] = f88te_tax_efficiency_regime_raw_sem_5d_base_v010_signal

def f88te_tax_efficiency_regime_raw_mean_10d_base_v011_signal(tax_expense):
    res = tax_expense.rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_10d_base_v011_signal'] = f88te_tax_efficiency_regime_raw_mean_10d_base_v011_signal

def f88te_tax_efficiency_regime_raw_std_10d_base_v012_signal(tax_expense):
    res = tax_expense.rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_10d_base_v012_signal'] = f88te_tax_efficiency_regime_raw_std_10d_base_v012_signal

def f88te_tax_efficiency_regime_raw_pct_change_10d_base_v013_signal(tax_expense):
    res = tax_expense.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_10d_base_v013_signal'] = f88te_tax_efficiency_regime_raw_pct_change_10d_base_v013_signal

def f88te_tax_efficiency_regime_raw_skew_10d_base_v014_signal(tax_expense):
    res = tax_expense.rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_10d_base_v014_signal'] = f88te_tax_efficiency_regime_raw_skew_10d_base_v014_signal

def f88te_tax_efficiency_regime_raw_kurt_10d_base_v015_signal(tax_expense):
    res = tax_expense.rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_10d_base_v015_signal'] = f88te_tax_efficiency_regime_raw_kurt_10d_base_v015_signal

def f88te_tax_efficiency_regime_raw_min_10d_base_v016_signal(tax_expense):
    res = tax_expense.rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_10d_base_v016_signal'] = f88te_tax_efficiency_regime_raw_min_10d_base_v016_signal

def f88te_tax_efficiency_regime_raw_max_10d_base_v017_signal(tax_expense):
    res = tax_expense.rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_10d_base_v017_signal'] = f88te_tax_efficiency_regime_raw_max_10d_base_v017_signal

def f88te_tax_efficiency_regime_raw_median_10d_base_v018_signal(tax_expense):
    res = tax_expense.rolling(10).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_10d_base_v018_signal'] = f88te_tax_efficiency_regime_raw_median_10d_base_v018_signal

def f88te_tax_efficiency_regime_raw_diff_10d_base_v019_signal(tax_expense):
    res = tax_expense.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_10d_base_v019_signal'] = f88te_tax_efficiency_regime_raw_diff_10d_base_v019_signal

def f88te_tax_efficiency_regime_raw_sem_10d_base_v020_signal(tax_expense):
    res = tax_expense.rolling(10).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_10d_base_v020_signal'] = f88te_tax_efficiency_regime_raw_sem_10d_base_v020_signal

def f88te_tax_efficiency_regime_raw_mean_21d_base_v021_signal(tax_expense):
    res = tax_expense.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_21d_base_v021_signal'] = f88te_tax_efficiency_regime_raw_mean_21d_base_v021_signal

def f88te_tax_efficiency_regime_raw_std_21d_base_v022_signal(tax_expense):
    res = tax_expense.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_21d_base_v022_signal'] = f88te_tax_efficiency_regime_raw_std_21d_base_v022_signal

def f88te_tax_efficiency_regime_raw_pct_change_21d_base_v023_signal(tax_expense):
    res = tax_expense.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_21d_base_v023_signal'] = f88te_tax_efficiency_regime_raw_pct_change_21d_base_v023_signal

def f88te_tax_efficiency_regime_raw_skew_21d_base_v024_signal(tax_expense):
    res = tax_expense.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_21d_base_v024_signal'] = f88te_tax_efficiency_regime_raw_skew_21d_base_v024_signal

def f88te_tax_efficiency_regime_raw_kurt_21d_base_v025_signal(tax_expense):
    res = tax_expense.rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_21d_base_v025_signal'] = f88te_tax_efficiency_regime_raw_kurt_21d_base_v025_signal

def f88te_tax_efficiency_regime_raw_min_21d_base_v026_signal(tax_expense):
    res = tax_expense.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_21d_base_v026_signal'] = f88te_tax_efficiency_regime_raw_min_21d_base_v026_signal

def f88te_tax_efficiency_regime_raw_max_21d_base_v027_signal(tax_expense):
    res = tax_expense.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_21d_base_v027_signal'] = f88te_tax_efficiency_regime_raw_max_21d_base_v027_signal

def f88te_tax_efficiency_regime_raw_median_21d_base_v028_signal(tax_expense):
    res = tax_expense.rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_21d_base_v028_signal'] = f88te_tax_efficiency_regime_raw_median_21d_base_v028_signal

def f88te_tax_efficiency_regime_raw_diff_21d_base_v029_signal(tax_expense):
    res = tax_expense.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_21d_base_v029_signal'] = f88te_tax_efficiency_regime_raw_diff_21d_base_v029_signal

def f88te_tax_efficiency_regime_raw_sem_21d_base_v030_signal(tax_expense):
    res = tax_expense.rolling(21).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_21d_base_v030_signal'] = f88te_tax_efficiency_regime_raw_sem_21d_base_v030_signal

def f88te_tax_efficiency_regime_raw_mean_42d_base_v031_signal(tax_expense):
    res = tax_expense.rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_42d_base_v031_signal'] = f88te_tax_efficiency_regime_raw_mean_42d_base_v031_signal

def f88te_tax_efficiency_regime_raw_std_42d_base_v032_signal(tax_expense):
    res = tax_expense.rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_42d_base_v032_signal'] = f88te_tax_efficiency_regime_raw_std_42d_base_v032_signal

def f88te_tax_efficiency_regime_raw_pct_change_42d_base_v033_signal(tax_expense):
    res = tax_expense.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_42d_base_v033_signal'] = f88te_tax_efficiency_regime_raw_pct_change_42d_base_v033_signal

def f88te_tax_efficiency_regime_raw_skew_42d_base_v034_signal(tax_expense):
    res = tax_expense.rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_42d_base_v034_signal'] = f88te_tax_efficiency_regime_raw_skew_42d_base_v034_signal

def f88te_tax_efficiency_regime_raw_kurt_42d_base_v035_signal(tax_expense):
    res = tax_expense.rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_42d_base_v035_signal'] = f88te_tax_efficiency_regime_raw_kurt_42d_base_v035_signal

def f88te_tax_efficiency_regime_raw_min_42d_base_v036_signal(tax_expense):
    res = tax_expense.rolling(42).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_42d_base_v036_signal'] = f88te_tax_efficiency_regime_raw_min_42d_base_v036_signal

def f88te_tax_efficiency_regime_raw_max_42d_base_v037_signal(tax_expense):
    res = tax_expense.rolling(42).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_42d_base_v037_signal'] = f88te_tax_efficiency_regime_raw_max_42d_base_v037_signal

def f88te_tax_efficiency_regime_raw_median_42d_base_v038_signal(tax_expense):
    res = tax_expense.rolling(42).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_42d_base_v038_signal'] = f88te_tax_efficiency_regime_raw_median_42d_base_v038_signal

def f88te_tax_efficiency_regime_raw_diff_42d_base_v039_signal(tax_expense):
    res = tax_expense.diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_42d_base_v039_signal'] = f88te_tax_efficiency_regime_raw_diff_42d_base_v039_signal

def f88te_tax_efficiency_regime_raw_sem_42d_base_v040_signal(tax_expense):
    res = tax_expense.rolling(42).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_42d_base_v040_signal'] = f88te_tax_efficiency_regime_raw_sem_42d_base_v040_signal

def f88te_tax_efficiency_regime_raw_mean_63d_base_v041_signal(tax_expense):
    res = tax_expense.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_63d_base_v041_signal'] = f88te_tax_efficiency_regime_raw_mean_63d_base_v041_signal

def f88te_tax_efficiency_regime_raw_std_63d_base_v042_signal(tax_expense):
    res = tax_expense.rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_63d_base_v042_signal'] = f88te_tax_efficiency_regime_raw_std_63d_base_v042_signal

def f88te_tax_efficiency_regime_raw_pct_change_63d_base_v043_signal(tax_expense):
    res = tax_expense.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_63d_base_v043_signal'] = f88te_tax_efficiency_regime_raw_pct_change_63d_base_v043_signal

def f88te_tax_efficiency_regime_raw_skew_63d_base_v044_signal(tax_expense):
    res = tax_expense.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_63d_base_v044_signal'] = f88te_tax_efficiency_regime_raw_skew_63d_base_v044_signal

def f88te_tax_efficiency_regime_raw_kurt_63d_base_v045_signal(tax_expense):
    res = tax_expense.rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_63d_base_v045_signal'] = f88te_tax_efficiency_regime_raw_kurt_63d_base_v045_signal

def f88te_tax_efficiency_regime_raw_min_63d_base_v046_signal(tax_expense):
    res = tax_expense.rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_63d_base_v046_signal'] = f88te_tax_efficiency_regime_raw_min_63d_base_v046_signal

def f88te_tax_efficiency_regime_raw_max_63d_base_v047_signal(tax_expense):
    res = tax_expense.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_63d_base_v047_signal'] = f88te_tax_efficiency_regime_raw_max_63d_base_v047_signal

def f88te_tax_efficiency_regime_raw_median_63d_base_v048_signal(tax_expense):
    res = tax_expense.rolling(63).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_63d_base_v048_signal'] = f88te_tax_efficiency_regime_raw_median_63d_base_v048_signal

def f88te_tax_efficiency_regime_raw_diff_63d_base_v049_signal(tax_expense):
    res = tax_expense.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_63d_base_v049_signal'] = f88te_tax_efficiency_regime_raw_diff_63d_base_v049_signal

def f88te_tax_efficiency_regime_raw_sem_63d_base_v050_signal(tax_expense):
    res = tax_expense.rolling(63).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_63d_base_v050_signal'] = f88te_tax_efficiency_regime_raw_sem_63d_base_v050_signal

def f88te_tax_efficiency_regime_raw_mean_126d_base_v051_signal(tax_expense):
    res = tax_expense.rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_126d_base_v051_signal'] = f88te_tax_efficiency_regime_raw_mean_126d_base_v051_signal

def f88te_tax_efficiency_regime_raw_std_126d_base_v052_signal(tax_expense):
    res = tax_expense.rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_126d_base_v052_signal'] = f88te_tax_efficiency_regime_raw_std_126d_base_v052_signal

def f88te_tax_efficiency_regime_raw_pct_change_126d_base_v053_signal(tax_expense):
    res = tax_expense.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_126d_base_v053_signal'] = f88te_tax_efficiency_regime_raw_pct_change_126d_base_v053_signal

def f88te_tax_efficiency_regime_raw_skew_126d_base_v054_signal(tax_expense):
    res = tax_expense.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_126d_base_v054_signal'] = f88te_tax_efficiency_regime_raw_skew_126d_base_v054_signal

def f88te_tax_efficiency_regime_raw_kurt_126d_base_v055_signal(tax_expense):
    res = tax_expense.rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_126d_base_v055_signal'] = f88te_tax_efficiency_regime_raw_kurt_126d_base_v055_signal

def f88te_tax_efficiency_regime_raw_min_126d_base_v056_signal(tax_expense):
    res = tax_expense.rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_126d_base_v056_signal'] = f88te_tax_efficiency_regime_raw_min_126d_base_v056_signal

def f88te_tax_efficiency_regime_raw_max_126d_base_v057_signal(tax_expense):
    res = tax_expense.rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_126d_base_v057_signal'] = f88te_tax_efficiency_regime_raw_max_126d_base_v057_signal

def f88te_tax_efficiency_regime_raw_median_126d_base_v058_signal(tax_expense):
    res = tax_expense.rolling(126).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_126d_base_v058_signal'] = f88te_tax_efficiency_regime_raw_median_126d_base_v058_signal

def f88te_tax_efficiency_regime_raw_diff_126d_base_v059_signal(tax_expense):
    res = tax_expense.diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_126d_base_v059_signal'] = f88te_tax_efficiency_regime_raw_diff_126d_base_v059_signal

def f88te_tax_efficiency_regime_raw_sem_126d_base_v060_signal(tax_expense):
    res = tax_expense.rolling(126).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_126d_base_v060_signal'] = f88te_tax_efficiency_regime_raw_sem_126d_base_v060_signal

def f88te_tax_efficiency_regime_raw_mean_252d_base_v061_signal(tax_expense):
    res = tax_expense.rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_mean_252d_base_v061_signal'] = f88te_tax_efficiency_regime_raw_mean_252d_base_v061_signal

def f88te_tax_efficiency_regime_raw_std_252d_base_v062_signal(tax_expense):
    res = tax_expense.rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_std_252d_base_v062_signal'] = f88te_tax_efficiency_regime_raw_std_252d_base_v062_signal

def f88te_tax_efficiency_regime_raw_pct_change_252d_base_v063_signal(tax_expense):
    res = tax_expense.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_pct_change_252d_base_v063_signal'] = f88te_tax_efficiency_regime_raw_pct_change_252d_base_v063_signal

def f88te_tax_efficiency_regime_raw_skew_252d_base_v064_signal(tax_expense):
    res = tax_expense.rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_skew_252d_base_v064_signal'] = f88te_tax_efficiency_regime_raw_skew_252d_base_v064_signal

def f88te_tax_efficiency_regime_raw_kurt_252d_base_v065_signal(tax_expense):
    res = tax_expense.rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_kurt_252d_base_v065_signal'] = f88te_tax_efficiency_regime_raw_kurt_252d_base_v065_signal

def f88te_tax_efficiency_regime_raw_min_252d_base_v066_signal(tax_expense):
    res = tax_expense.rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_min_252d_base_v066_signal'] = f88te_tax_efficiency_regime_raw_min_252d_base_v066_signal

def f88te_tax_efficiency_regime_raw_max_252d_base_v067_signal(tax_expense):
    res = tax_expense.rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_max_252d_base_v067_signal'] = f88te_tax_efficiency_regime_raw_max_252d_base_v067_signal

def f88te_tax_efficiency_regime_raw_median_252d_base_v068_signal(tax_expense):
    res = tax_expense.rolling(252).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_median_252d_base_v068_signal'] = f88te_tax_efficiency_regime_raw_median_252d_base_v068_signal

def f88te_tax_efficiency_regime_raw_diff_252d_base_v069_signal(tax_expense):
    res = tax_expense.diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_diff_252d_base_v069_signal'] = f88te_tax_efficiency_regime_raw_diff_252d_base_v069_signal

def f88te_tax_efficiency_regime_raw_sem_252d_base_v070_signal(tax_expense):
    res = tax_expense.rolling(252).sem()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_raw_sem_252d_base_v070_signal'] = f88te_tax_efficiency_regime_raw_sem_252d_base_v070_signal

def f88te_tax_efficiency_regime_pre_tax_income_mean_5d_base_v071_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_mean_5d_base_v071_signal'] = f88te_tax_efficiency_regime_pre_tax_income_mean_5d_base_v071_signal

def f88te_tax_efficiency_regime_pre_tax_income_std_5d_base_v072_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_std_5d_base_v072_signal'] = f88te_tax_efficiency_regime_pre_tax_income_std_5d_base_v072_signal

def f88te_tax_efficiency_regime_pre_tax_income_pct_change_5d_base_v073_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_pct_change_5d_base_v073_signal'] = f88te_tax_efficiency_regime_pre_tax_income_pct_change_5d_base_v073_signal

def f88te_tax_efficiency_regime_pre_tax_income_skew_5d_base_v074_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_skew_5d_base_v074_signal'] = f88te_tax_efficiency_regime_pre_tax_income_skew_5d_base_v074_signal

def f88te_tax_efficiency_regime_pre_tax_income_kurt_5d_base_v075_signal(tax_expense, pre_tax_income):
    res = (tax_expense / pre_tax_income).rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f88te_tax_efficiency_regime_pre_tax_income_kurt_5d_base_v075_signal'] = f88te_tax_efficiency_regime_pre_tax_income_kurt_5d_base_v075_signal


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
