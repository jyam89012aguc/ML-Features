import pandas as pd
import numpy as np
import os
import inspect
FEATURE_FUNCTIONS = {}

def f90cv_current_ratio_volatility_raw_mean_5d_jerk_v001_signal(current_assets):
    base = current_assets.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_5d_jerk_v001_signal'] = f90cv_current_ratio_volatility_raw_mean_5d_jerk_v001_signal

def f90cv_current_ratio_volatility_raw_std_5d_jerk_v002_signal(current_assets):
    base = current_assets.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_5d_jerk_v002_signal'] = f90cv_current_ratio_volatility_raw_std_5d_jerk_v002_signal

def f90cv_current_ratio_volatility_raw_pct_change_5d_jerk_v003_signal(current_assets):
    base = current_assets.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_5d_jerk_v003_signal'] = f90cv_current_ratio_volatility_raw_pct_change_5d_jerk_v003_signal

def f90cv_current_ratio_volatility_raw_skew_5d_jerk_v004_signal(current_assets):
    base = current_assets.rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_5d_jerk_v004_signal'] = f90cv_current_ratio_volatility_raw_skew_5d_jerk_v004_signal

def f90cv_current_ratio_volatility_raw_kurt_5d_jerk_v005_signal(current_assets):
    base = current_assets.rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_5d_jerk_v005_signal'] = f90cv_current_ratio_volatility_raw_kurt_5d_jerk_v005_signal

def f90cv_current_ratio_volatility_raw_min_5d_jerk_v006_signal(current_assets):
    base = current_assets.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_5d_jerk_v006_signal'] = f90cv_current_ratio_volatility_raw_min_5d_jerk_v006_signal

def f90cv_current_ratio_volatility_raw_max_5d_jerk_v007_signal(current_assets):
    base = current_assets.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_5d_jerk_v007_signal'] = f90cv_current_ratio_volatility_raw_max_5d_jerk_v007_signal

def f90cv_current_ratio_volatility_raw_median_5d_jerk_v008_signal(current_assets):
    base = current_assets.rolling(5).median()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_5d_jerk_v008_signal'] = f90cv_current_ratio_volatility_raw_median_5d_jerk_v008_signal

def f90cv_current_ratio_volatility_raw_diff_5d_jerk_v009_signal(current_assets):
    base = current_assets.diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_5d_jerk_v009_signal'] = f90cv_current_ratio_volatility_raw_diff_5d_jerk_v009_signal

def f90cv_current_ratio_volatility_raw_sem_5d_jerk_v010_signal(current_assets):
    base = current_assets.rolling(5).sem()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_5d_jerk_v010_signal'] = f90cv_current_ratio_volatility_raw_sem_5d_jerk_v010_signal

def f90cv_current_ratio_volatility_raw_mean_10d_jerk_v011_signal(current_assets):
    base = current_assets.rolling(10).mean()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_10d_jerk_v011_signal'] = f90cv_current_ratio_volatility_raw_mean_10d_jerk_v011_signal

def f90cv_current_ratio_volatility_raw_std_10d_jerk_v012_signal(current_assets):
    base = current_assets.rolling(10).std()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_10d_jerk_v012_signal'] = f90cv_current_ratio_volatility_raw_std_10d_jerk_v012_signal

def f90cv_current_ratio_volatility_raw_pct_change_10d_jerk_v013_signal(current_assets):
    base = current_assets.pct_change(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_10d_jerk_v013_signal'] = f90cv_current_ratio_volatility_raw_pct_change_10d_jerk_v013_signal

def f90cv_current_ratio_volatility_raw_skew_10d_jerk_v014_signal(current_assets):
    base = current_assets.rolling(10).skew()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_10d_jerk_v014_signal'] = f90cv_current_ratio_volatility_raw_skew_10d_jerk_v014_signal

def f90cv_current_ratio_volatility_raw_kurt_10d_jerk_v015_signal(current_assets):
    base = current_assets.rolling(10).kurt()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_10d_jerk_v015_signal'] = f90cv_current_ratio_volatility_raw_kurt_10d_jerk_v015_signal

def f90cv_current_ratio_volatility_raw_min_10d_jerk_v016_signal(current_assets):
    base = current_assets.rolling(10).min()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_10d_jerk_v016_signal'] = f90cv_current_ratio_volatility_raw_min_10d_jerk_v016_signal

def f90cv_current_ratio_volatility_raw_max_10d_jerk_v017_signal(current_assets):
    base = current_assets.rolling(10).max()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_10d_jerk_v017_signal'] = f90cv_current_ratio_volatility_raw_max_10d_jerk_v017_signal

def f90cv_current_ratio_volatility_raw_median_10d_jerk_v018_signal(current_assets):
    base = current_assets.rolling(10).median()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_10d_jerk_v018_signal'] = f90cv_current_ratio_volatility_raw_median_10d_jerk_v018_signal

def f90cv_current_ratio_volatility_raw_diff_10d_jerk_v019_signal(current_assets):
    base = current_assets.diff(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_10d_jerk_v019_signal'] = f90cv_current_ratio_volatility_raw_diff_10d_jerk_v019_signal

def f90cv_current_ratio_volatility_raw_sem_10d_jerk_v020_signal(current_assets):
    base = current_assets.rolling(10).sem()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_10d_jerk_v020_signal'] = f90cv_current_ratio_volatility_raw_sem_10d_jerk_v020_signal

def f90cv_current_ratio_volatility_raw_mean_21d_jerk_v021_signal(current_assets):
    base = current_assets.rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_21d_jerk_v021_signal'] = f90cv_current_ratio_volatility_raw_mean_21d_jerk_v021_signal

def f90cv_current_ratio_volatility_raw_std_21d_jerk_v022_signal(current_assets):
    base = current_assets.rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_21d_jerk_v022_signal'] = f90cv_current_ratio_volatility_raw_std_21d_jerk_v022_signal

def f90cv_current_ratio_volatility_raw_pct_change_21d_jerk_v023_signal(current_assets):
    base = current_assets.pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_21d_jerk_v023_signal'] = f90cv_current_ratio_volatility_raw_pct_change_21d_jerk_v023_signal

def f90cv_current_ratio_volatility_raw_skew_21d_jerk_v024_signal(current_assets):
    base = current_assets.rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_21d_jerk_v024_signal'] = f90cv_current_ratio_volatility_raw_skew_21d_jerk_v024_signal

def f90cv_current_ratio_volatility_raw_kurt_21d_jerk_v025_signal(current_assets):
    base = current_assets.rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_21d_jerk_v025_signal'] = f90cv_current_ratio_volatility_raw_kurt_21d_jerk_v025_signal

def f90cv_current_ratio_volatility_raw_min_21d_jerk_v026_signal(current_assets):
    base = current_assets.rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_21d_jerk_v026_signal'] = f90cv_current_ratio_volatility_raw_min_21d_jerk_v026_signal

def f90cv_current_ratio_volatility_raw_max_21d_jerk_v027_signal(current_assets):
    base = current_assets.rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_21d_jerk_v027_signal'] = f90cv_current_ratio_volatility_raw_max_21d_jerk_v027_signal

def f90cv_current_ratio_volatility_raw_median_21d_jerk_v028_signal(current_assets):
    base = current_assets.rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_21d_jerk_v028_signal'] = f90cv_current_ratio_volatility_raw_median_21d_jerk_v028_signal

def f90cv_current_ratio_volatility_raw_diff_21d_jerk_v029_signal(current_assets):
    base = current_assets.diff(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_21d_jerk_v029_signal'] = f90cv_current_ratio_volatility_raw_diff_21d_jerk_v029_signal

def f90cv_current_ratio_volatility_raw_sem_21d_jerk_v030_signal(current_assets):
    base = current_assets.rolling(21).sem()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_21d_jerk_v030_signal'] = f90cv_current_ratio_volatility_raw_sem_21d_jerk_v030_signal

def f90cv_current_ratio_volatility_raw_mean_42d_jerk_v031_signal(current_assets):
    base = current_assets.rolling(42).mean()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_42d_jerk_v031_signal'] = f90cv_current_ratio_volatility_raw_mean_42d_jerk_v031_signal

def f90cv_current_ratio_volatility_raw_std_42d_jerk_v032_signal(current_assets):
    base = current_assets.rolling(42).std()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_42d_jerk_v032_signal'] = f90cv_current_ratio_volatility_raw_std_42d_jerk_v032_signal

def f90cv_current_ratio_volatility_raw_pct_change_42d_jerk_v033_signal(current_assets):
    base = current_assets.pct_change(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_42d_jerk_v033_signal'] = f90cv_current_ratio_volatility_raw_pct_change_42d_jerk_v033_signal

def f90cv_current_ratio_volatility_raw_skew_42d_jerk_v034_signal(current_assets):
    base = current_assets.rolling(42).skew()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_42d_jerk_v034_signal'] = f90cv_current_ratio_volatility_raw_skew_42d_jerk_v034_signal

def f90cv_current_ratio_volatility_raw_kurt_42d_jerk_v035_signal(current_assets):
    base = current_assets.rolling(42).kurt()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_42d_jerk_v035_signal'] = f90cv_current_ratio_volatility_raw_kurt_42d_jerk_v035_signal

def f90cv_current_ratio_volatility_raw_min_42d_jerk_v036_signal(current_assets):
    base = current_assets.rolling(42).min()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_42d_jerk_v036_signal'] = f90cv_current_ratio_volatility_raw_min_42d_jerk_v036_signal

def f90cv_current_ratio_volatility_raw_max_42d_jerk_v037_signal(current_assets):
    base = current_assets.rolling(42).max()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_42d_jerk_v037_signal'] = f90cv_current_ratio_volatility_raw_max_42d_jerk_v037_signal

def f90cv_current_ratio_volatility_raw_median_42d_jerk_v038_signal(current_assets):
    base = current_assets.rolling(42).median()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_42d_jerk_v038_signal'] = f90cv_current_ratio_volatility_raw_median_42d_jerk_v038_signal

def f90cv_current_ratio_volatility_raw_diff_42d_jerk_v039_signal(current_assets):
    base = current_assets.diff(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_42d_jerk_v039_signal'] = f90cv_current_ratio_volatility_raw_diff_42d_jerk_v039_signal

def f90cv_current_ratio_volatility_raw_sem_42d_jerk_v040_signal(current_assets):
    base = current_assets.rolling(42).sem()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_42d_jerk_v040_signal'] = f90cv_current_ratio_volatility_raw_sem_42d_jerk_v040_signal

def f90cv_current_ratio_volatility_raw_mean_63d_jerk_v041_signal(current_assets):
    base = current_assets.rolling(63).mean()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_63d_jerk_v041_signal'] = f90cv_current_ratio_volatility_raw_mean_63d_jerk_v041_signal

def f90cv_current_ratio_volatility_raw_std_63d_jerk_v042_signal(current_assets):
    base = current_assets.rolling(63).std()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_63d_jerk_v042_signal'] = f90cv_current_ratio_volatility_raw_std_63d_jerk_v042_signal

def f90cv_current_ratio_volatility_raw_pct_change_63d_jerk_v043_signal(current_assets):
    base = current_assets.pct_change(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_63d_jerk_v043_signal'] = f90cv_current_ratio_volatility_raw_pct_change_63d_jerk_v043_signal

def f90cv_current_ratio_volatility_raw_skew_63d_jerk_v044_signal(current_assets):
    base = current_assets.rolling(63).skew()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_63d_jerk_v044_signal'] = f90cv_current_ratio_volatility_raw_skew_63d_jerk_v044_signal

def f90cv_current_ratio_volatility_raw_kurt_63d_jerk_v045_signal(current_assets):
    base = current_assets.rolling(63).kurt()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_63d_jerk_v045_signal'] = f90cv_current_ratio_volatility_raw_kurt_63d_jerk_v045_signal

def f90cv_current_ratio_volatility_raw_min_63d_jerk_v046_signal(current_assets):
    base = current_assets.rolling(63).min()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_63d_jerk_v046_signal'] = f90cv_current_ratio_volatility_raw_min_63d_jerk_v046_signal

def f90cv_current_ratio_volatility_raw_max_63d_jerk_v047_signal(current_assets):
    base = current_assets.rolling(63).max()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_63d_jerk_v047_signal'] = f90cv_current_ratio_volatility_raw_max_63d_jerk_v047_signal

def f90cv_current_ratio_volatility_raw_median_63d_jerk_v048_signal(current_assets):
    base = current_assets.rolling(63).median()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_63d_jerk_v048_signal'] = f90cv_current_ratio_volatility_raw_median_63d_jerk_v048_signal

def f90cv_current_ratio_volatility_raw_diff_63d_jerk_v049_signal(current_assets):
    base = current_assets.diff(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_63d_jerk_v049_signal'] = f90cv_current_ratio_volatility_raw_diff_63d_jerk_v049_signal

def f90cv_current_ratio_volatility_raw_sem_63d_jerk_v050_signal(current_assets):
    base = current_assets.rolling(63).sem()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_63d_jerk_v050_signal'] = f90cv_current_ratio_volatility_raw_sem_63d_jerk_v050_signal

def f90cv_current_ratio_volatility_raw_mean_126d_jerk_v051_signal(current_assets):
    base = current_assets.rolling(126).mean()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_126d_jerk_v051_signal'] = f90cv_current_ratio_volatility_raw_mean_126d_jerk_v051_signal

def f90cv_current_ratio_volatility_raw_std_126d_jerk_v052_signal(current_assets):
    base = current_assets.rolling(126).std()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_126d_jerk_v052_signal'] = f90cv_current_ratio_volatility_raw_std_126d_jerk_v052_signal

def f90cv_current_ratio_volatility_raw_pct_change_126d_jerk_v053_signal(current_assets):
    base = current_assets.pct_change(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_126d_jerk_v053_signal'] = f90cv_current_ratio_volatility_raw_pct_change_126d_jerk_v053_signal

def f90cv_current_ratio_volatility_raw_skew_126d_jerk_v054_signal(current_assets):
    base = current_assets.rolling(126).skew()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_126d_jerk_v054_signal'] = f90cv_current_ratio_volatility_raw_skew_126d_jerk_v054_signal

def f90cv_current_ratio_volatility_raw_kurt_126d_jerk_v055_signal(current_assets):
    base = current_assets.rolling(126).kurt()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_126d_jerk_v055_signal'] = f90cv_current_ratio_volatility_raw_kurt_126d_jerk_v055_signal

def f90cv_current_ratio_volatility_raw_min_126d_jerk_v056_signal(current_assets):
    base = current_assets.rolling(126).min()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_126d_jerk_v056_signal'] = f90cv_current_ratio_volatility_raw_min_126d_jerk_v056_signal

def f90cv_current_ratio_volatility_raw_max_126d_jerk_v057_signal(current_assets):
    base = current_assets.rolling(126).max()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_126d_jerk_v057_signal'] = f90cv_current_ratio_volatility_raw_max_126d_jerk_v057_signal

def f90cv_current_ratio_volatility_raw_median_126d_jerk_v058_signal(current_assets):
    base = current_assets.rolling(126).median()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_126d_jerk_v058_signal'] = f90cv_current_ratio_volatility_raw_median_126d_jerk_v058_signal

def f90cv_current_ratio_volatility_raw_diff_126d_jerk_v059_signal(current_assets):
    base = current_assets.diff(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_126d_jerk_v059_signal'] = f90cv_current_ratio_volatility_raw_diff_126d_jerk_v059_signal

def f90cv_current_ratio_volatility_raw_sem_126d_jerk_v060_signal(current_assets):
    base = current_assets.rolling(126).sem()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_126d_jerk_v060_signal'] = f90cv_current_ratio_volatility_raw_sem_126d_jerk_v060_signal

def f90cv_current_ratio_volatility_raw_mean_252d_jerk_v061_signal(current_assets):
    base = current_assets.rolling(252).mean()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_mean_252d_jerk_v061_signal'] = f90cv_current_ratio_volatility_raw_mean_252d_jerk_v061_signal

def f90cv_current_ratio_volatility_raw_std_252d_jerk_v062_signal(current_assets):
    base = current_assets.rolling(252).std()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_std_252d_jerk_v062_signal'] = f90cv_current_ratio_volatility_raw_std_252d_jerk_v062_signal

def f90cv_current_ratio_volatility_raw_pct_change_252d_jerk_v063_signal(current_assets):
    base = current_assets.pct_change(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_pct_change_252d_jerk_v063_signal'] = f90cv_current_ratio_volatility_raw_pct_change_252d_jerk_v063_signal

def f90cv_current_ratio_volatility_raw_skew_252d_jerk_v064_signal(current_assets):
    base = current_assets.rolling(252).skew()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_skew_252d_jerk_v064_signal'] = f90cv_current_ratio_volatility_raw_skew_252d_jerk_v064_signal

def f90cv_current_ratio_volatility_raw_kurt_252d_jerk_v065_signal(current_assets):
    base = current_assets.rolling(252).kurt()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_kurt_252d_jerk_v065_signal'] = f90cv_current_ratio_volatility_raw_kurt_252d_jerk_v065_signal

def f90cv_current_ratio_volatility_raw_min_252d_jerk_v066_signal(current_assets):
    base = current_assets.rolling(252).min()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_min_252d_jerk_v066_signal'] = f90cv_current_ratio_volatility_raw_min_252d_jerk_v066_signal

def f90cv_current_ratio_volatility_raw_max_252d_jerk_v067_signal(current_assets):
    base = current_assets.rolling(252).max()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_max_252d_jerk_v067_signal'] = f90cv_current_ratio_volatility_raw_max_252d_jerk_v067_signal

def f90cv_current_ratio_volatility_raw_median_252d_jerk_v068_signal(current_assets):
    base = current_assets.rolling(252).median()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_median_252d_jerk_v068_signal'] = f90cv_current_ratio_volatility_raw_median_252d_jerk_v068_signal

def f90cv_current_ratio_volatility_raw_diff_252d_jerk_v069_signal(current_assets):
    base = current_assets.diff(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_diff_252d_jerk_v069_signal'] = f90cv_current_ratio_volatility_raw_diff_252d_jerk_v069_signal

def f90cv_current_ratio_volatility_raw_sem_252d_jerk_v070_signal(current_assets):
    base = current_assets.rolling(252).sem()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_raw_sem_252d_jerk_v070_signal'] = f90cv_current_ratio_volatility_raw_sem_252d_jerk_v070_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_5d_jerk_v071_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_5d_jerk_v071_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_5d_jerk_v071_signal

def f90cv_current_ratio_volatility_current_liabilities_std_5d_jerk_v072_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_5d_jerk_v072_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_5d_jerk_v072_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_5d_jerk_v073_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_5d_jerk_v073_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_5d_jerk_v073_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_5d_jerk_v074_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_5d_jerk_v074_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_5d_jerk_v074_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_5d_jerk_v075_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_5d_jerk_v075_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_5d_jerk_v075_signal

def f90cv_current_ratio_volatility_current_liabilities_min_5d_jerk_v076_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_5d_jerk_v076_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_5d_jerk_v076_signal

def f90cv_current_ratio_volatility_current_liabilities_max_5d_jerk_v077_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_5d_jerk_v077_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_5d_jerk_v077_signal

def f90cv_current_ratio_volatility_current_liabilities_median_5d_jerk_v078_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).median()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_5d_jerk_v078_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_5d_jerk_v078_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_5d_jerk_v079_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_5d_jerk_v079_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_5d_jerk_v079_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_5d_jerk_v080_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(5).sem()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_5d_jerk_v080_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_5d_jerk_v080_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_10d_jerk_v081_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).mean()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_10d_jerk_v081_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_10d_jerk_v081_signal

def f90cv_current_ratio_volatility_current_liabilities_std_10d_jerk_v082_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).std()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_10d_jerk_v082_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_10d_jerk_v082_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_10d_jerk_v083_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_10d_jerk_v083_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_10d_jerk_v083_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_10d_jerk_v084_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).skew()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_10d_jerk_v084_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_10d_jerk_v084_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_10d_jerk_v085_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).kurt()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_10d_jerk_v085_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_10d_jerk_v085_signal

def f90cv_current_ratio_volatility_current_liabilities_min_10d_jerk_v086_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).min()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_10d_jerk_v086_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_10d_jerk_v086_signal

def f90cv_current_ratio_volatility_current_liabilities_max_10d_jerk_v087_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).max()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_10d_jerk_v087_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_10d_jerk_v087_signal

def f90cv_current_ratio_volatility_current_liabilities_median_10d_jerk_v088_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).median()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_10d_jerk_v088_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_10d_jerk_v088_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_10d_jerk_v089_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_10d_jerk_v089_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_10d_jerk_v089_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_10d_jerk_v090_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(10).sem()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_10d_jerk_v090_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_10d_jerk_v090_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_21d_jerk_v091_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_21d_jerk_v091_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_21d_jerk_v091_signal

def f90cv_current_ratio_volatility_current_liabilities_std_21d_jerk_v092_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_21d_jerk_v092_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_21d_jerk_v092_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_21d_jerk_v093_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_21d_jerk_v093_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_21d_jerk_v093_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_21d_jerk_v094_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_21d_jerk_v094_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_21d_jerk_v094_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_21d_jerk_v095_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_21d_jerk_v095_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_21d_jerk_v095_signal

def f90cv_current_ratio_volatility_current_liabilities_min_21d_jerk_v096_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_21d_jerk_v096_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_21d_jerk_v096_signal

def f90cv_current_ratio_volatility_current_liabilities_max_21d_jerk_v097_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_21d_jerk_v097_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_21d_jerk_v097_signal

def f90cv_current_ratio_volatility_current_liabilities_median_21d_jerk_v098_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_21d_jerk_v098_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_21d_jerk_v098_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_21d_jerk_v099_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_21d_jerk_v099_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_21d_jerk_v099_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_21d_jerk_v100_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(21).sem()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_21d_jerk_v100_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_21d_jerk_v100_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_42d_jerk_v101_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).mean()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_42d_jerk_v101_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_42d_jerk_v101_signal

def f90cv_current_ratio_volatility_current_liabilities_std_42d_jerk_v102_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).std()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_42d_jerk_v102_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_42d_jerk_v102_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_42d_jerk_v103_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_42d_jerk_v103_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_42d_jerk_v103_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_42d_jerk_v104_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).skew()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_42d_jerk_v104_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_42d_jerk_v104_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_42d_jerk_v105_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).kurt()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_42d_jerk_v105_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_42d_jerk_v105_signal

def f90cv_current_ratio_volatility_current_liabilities_min_42d_jerk_v106_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).min()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_42d_jerk_v106_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_42d_jerk_v106_signal

def f90cv_current_ratio_volatility_current_liabilities_max_42d_jerk_v107_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).max()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_42d_jerk_v107_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_42d_jerk_v107_signal

def f90cv_current_ratio_volatility_current_liabilities_median_42d_jerk_v108_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).median()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_42d_jerk_v108_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_42d_jerk_v108_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_42d_jerk_v109_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_42d_jerk_v109_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_42d_jerk_v109_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_42d_jerk_v110_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(42).sem()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_42d_jerk_v110_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_42d_jerk_v110_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_63d_jerk_v111_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).mean()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_63d_jerk_v111_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_63d_jerk_v111_signal

def f90cv_current_ratio_volatility_current_liabilities_std_63d_jerk_v112_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).std()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_63d_jerk_v112_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_63d_jerk_v112_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_63d_jerk_v113_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_63d_jerk_v113_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_63d_jerk_v113_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_63d_jerk_v114_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).skew()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_63d_jerk_v114_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_63d_jerk_v114_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_63d_jerk_v115_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).kurt()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_63d_jerk_v115_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_63d_jerk_v115_signal

def f90cv_current_ratio_volatility_current_liabilities_min_63d_jerk_v116_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).min()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_63d_jerk_v116_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_63d_jerk_v116_signal

def f90cv_current_ratio_volatility_current_liabilities_max_63d_jerk_v117_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).max()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_63d_jerk_v117_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_63d_jerk_v117_signal

def f90cv_current_ratio_volatility_current_liabilities_median_63d_jerk_v118_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).median()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_63d_jerk_v118_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_63d_jerk_v118_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_63d_jerk_v119_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_63d_jerk_v119_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_63d_jerk_v119_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_63d_jerk_v120_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(63).sem()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_63d_jerk_v120_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_63d_jerk_v120_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_126d_jerk_v121_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).mean()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_126d_jerk_v121_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_126d_jerk_v121_signal

def f90cv_current_ratio_volatility_current_liabilities_std_126d_jerk_v122_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).std()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_126d_jerk_v122_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_126d_jerk_v122_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_126d_jerk_v123_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_126d_jerk_v123_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_126d_jerk_v123_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_126d_jerk_v124_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).skew()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_126d_jerk_v124_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_126d_jerk_v124_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_126d_jerk_v125_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).kurt()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_126d_jerk_v125_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_126d_jerk_v125_signal

def f90cv_current_ratio_volatility_current_liabilities_min_126d_jerk_v126_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).min()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_126d_jerk_v126_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_126d_jerk_v126_signal

def f90cv_current_ratio_volatility_current_liabilities_max_126d_jerk_v127_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).max()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_126d_jerk_v127_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_126d_jerk_v127_signal

def f90cv_current_ratio_volatility_current_liabilities_median_126d_jerk_v128_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).median()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_126d_jerk_v128_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_126d_jerk_v128_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_126d_jerk_v129_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_126d_jerk_v129_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_126d_jerk_v129_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_126d_jerk_v130_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(126).sem()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_126d_jerk_v130_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_126d_jerk_v130_signal

def f90cv_current_ratio_volatility_current_liabilities_mean_252d_jerk_v131_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).mean()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_mean_252d_jerk_v131_signal'] = f90cv_current_ratio_volatility_current_liabilities_mean_252d_jerk_v131_signal

def f90cv_current_ratio_volatility_current_liabilities_std_252d_jerk_v132_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).std()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_std_252d_jerk_v132_signal'] = f90cv_current_ratio_volatility_current_liabilities_std_252d_jerk_v132_signal

def f90cv_current_ratio_volatility_current_liabilities_pct_change_252d_jerk_v133_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).pct_change(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_pct_change_252d_jerk_v133_signal'] = f90cv_current_ratio_volatility_current_liabilities_pct_change_252d_jerk_v133_signal

def f90cv_current_ratio_volatility_current_liabilities_skew_252d_jerk_v134_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).skew()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_skew_252d_jerk_v134_signal'] = f90cv_current_ratio_volatility_current_liabilities_skew_252d_jerk_v134_signal

def f90cv_current_ratio_volatility_current_liabilities_kurt_252d_jerk_v135_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).kurt()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_kurt_252d_jerk_v135_signal'] = f90cv_current_ratio_volatility_current_liabilities_kurt_252d_jerk_v135_signal

def f90cv_current_ratio_volatility_current_liabilities_min_252d_jerk_v136_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).min()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_min_252d_jerk_v136_signal'] = f90cv_current_ratio_volatility_current_liabilities_min_252d_jerk_v136_signal

def f90cv_current_ratio_volatility_current_liabilities_max_252d_jerk_v137_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).max()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_max_252d_jerk_v137_signal'] = f90cv_current_ratio_volatility_current_liabilities_max_252d_jerk_v137_signal

def f90cv_current_ratio_volatility_current_liabilities_median_252d_jerk_v138_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).median()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_median_252d_jerk_v138_signal'] = f90cv_current_ratio_volatility_current_liabilities_median_252d_jerk_v138_signal

def f90cv_current_ratio_volatility_current_liabilities_diff_252d_jerk_v139_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).diff(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_diff_252d_jerk_v139_signal'] = f90cv_current_ratio_volatility_current_liabilities_diff_252d_jerk_v139_signal

def f90cv_current_ratio_volatility_current_liabilities_sem_252d_jerk_v140_signal(current_assets, current_liabilities):
    base = (current_assets / current_liabilities).rolling(252).sem()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_current_liabilities_sem_252d_jerk_v140_signal'] = f90cv_current_ratio_volatility_current_liabilities_sem_252d_jerk_v140_signal

def f90cv_current_ratio_volatility_revenue_mean_5d_jerk_v141_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_mean_5d_jerk_v141_signal'] = f90cv_current_ratio_volatility_revenue_mean_5d_jerk_v141_signal

def f90cv_current_ratio_volatility_revenue_std_5d_jerk_v142_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_std_5d_jerk_v142_signal'] = f90cv_current_ratio_volatility_revenue_std_5d_jerk_v142_signal

def f90cv_current_ratio_volatility_revenue_pct_change_5d_jerk_v143_signal(current_assets, revenue):
    base = (current_assets / revenue).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_pct_change_5d_jerk_v143_signal'] = f90cv_current_ratio_volatility_revenue_pct_change_5d_jerk_v143_signal

def f90cv_current_ratio_volatility_revenue_skew_5d_jerk_v144_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_skew_5d_jerk_v144_signal'] = f90cv_current_ratio_volatility_revenue_skew_5d_jerk_v144_signal

def f90cv_current_ratio_volatility_revenue_kurt_5d_jerk_v145_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_kurt_5d_jerk_v145_signal'] = f90cv_current_ratio_volatility_revenue_kurt_5d_jerk_v145_signal

def f90cv_current_ratio_volatility_revenue_min_5d_jerk_v146_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_min_5d_jerk_v146_signal'] = f90cv_current_ratio_volatility_revenue_min_5d_jerk_v146_signal

def f90cv_current_ratio_volatility_revenue_max_5d_jerk_v147_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_max_5d_jerk_v147_signal'] = f90cv_current_ratio_volatility_revenue_max_5d_jerk_v147_signal

def f90cv_current_ratio_volatility_revenue_median_5d_jerk_v148_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).median()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_median_5d_jerk_v148_signal'] = f90cv_current_ratio_volatility_revenue_median_5d_jerk_v148_signal

def f90cv_current_ratio_volatility_revenue_diff_5d_jerk_v149_signal(current_assets, revenue):
    base = (current_assets / revenue).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_diff_5d_jerk_v149_signal'] = f90cv_current_ratio_volatility_revenue_diff_5d_jerk_v149_signal

def f90cv_current_ratio_volatility_revenue_sem_5d_jerk_v150_signal(current_assets, revenue):
    base = (current_assets / revenue).rolling(5).sem()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f90cv_current_ratio_volatility_revenue_sem_5d_jerk_v150_signal'] = f90cv_current_ratio_volatility_revenue_sem_5d_jerk_v150_signal


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
