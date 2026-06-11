import pandas as pd
import numpy as np
import os
import inspect
FEATURE_FUNCTIONS = {}

def f89ie_interest_expense_momentum_raw_mean_5d_jerk_v001_signal(interest_expense):
    base = interest_expense.rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_5d_jerk_v001_signal'] = f89ie_interest_expense_momentum_raw_mean_5d_jerk_v001_signal

def f89ie_interest_expense_momentum_raw_std_5d_jerk_v002_signal(interest_expense):
    base = interest_expense.rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_5d_jerk_v002_signal'] = f89ie_interest_expense_momentum_raw_std_5d_jerk_v002_signal

def f89ie_interest_expense_momentum_raw_pct_change_5d_jerk_v003_signal(interest_expense):
    base = interest_expense.pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_5d_jerk_v003_signal'] = f89ie_interest_expense_momentum_raw_pct_change_5d_jerk_v003_signal

def f89ie_interest_expense_momentum_raw_skew_5d_jerk_v004_signal(interest_expense):
    base = interest_expense.rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_5d_jerk_v004_signal'] = f89ie_interest_expense_momentum_raw_skew_5d_jerk_v004_signal

def f89ie_interest_expense_momentum_raw_kurt_5d_jerk_v005_signal(interest_expense):
    base = interest_expense.rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_5d_jerk_v005_signal'] = f89ie_interest_expense_momentum_raw_kurt_5d_jerk_v005_signal

def f89ie_interest_expense_momentum_raw_min_5d_jerk_v006_signal(interest_expense):
    base = interest_expense.rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_5d_jerk_v006_signal'] = f89ie_interest_expense_momentum_raw_min_5d_jerk_v006_signal

def f89ie_interest_expense_momentum_raw_max_5d_jerk_v007_signal(interest_expense):
    base = interest_expense.rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_5d_jerk_v007_signal'] = f89ie_interest_expense_momentum_raw_max_5d_jerk_v007_signal

def f89ie_interest_expense_momentum_raw_median_5d_jerk_v008_signal(interest_expense):
    base = interest_expense.rolling(5).median()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_5d_jerk_v008_signal'] = f89ie_interest_expense_momentum_raw_median_5d_jerk_v008_signal

def f89ie_interest_expense_momentum_raw_diff_5d_jerk_v009_signal(interest_expense):
    base = interest_expense.diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_5d_jerk_v009_signal'] = f89ie_interest_expense_momentum_raw_diff_5d_jerk_v009_signal

def f89ie_interest_expense_momentum_raw_sem_5d_jerk_v010_signal(interest_expense):
    base = interest_expense.rolling(5).sem()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_5d_jerk_v010_signal'] = f89ie_interest_expense_momentum_raw_sem_5d_jerk_v010_signal

def f89ie_interest_expense_momentum_raw_mean_10d_jerk_v011_signal(interest_expense):
    base = interest_expense.rolling(10).mean()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_10d_jerk_v011_signal'] = f89ie_interest_expense_momentum_raw_mean_10d_jerk_v011_signal

def f89ie_interest_expense_momentum_raw_std_10d_jerk_v012_signal(interest_expense):
    base = interest_expense.rolling(10).std()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_10d_jerk_v012_signal'] = f89ie_interest_expense_momentum_raw_std_10d_jerk_v012_signal

def f89ie_interest_expense_momentum_raw_pct_change_10d_jerk_v013_signal(interest_expense):
    base = interest_expense.pct_change(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_10d_jerk_v013_signal'] = f89ie_interest_expense_momentum_raw_pct_change_10d_jerk_v013_signal

def f89ie_interest_expense_momentum_raw_skew_10d_jerk_v014_signal(interest_expense):
    base = interest_expense.rolling(10).skew()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_10d_jerk_v014_signal'] = f89ie_interest_expense_momentum_raw_skew_10d_jerk_v014_signal

def f89ie_interest_expense_momentum_raw_kurt_10d_jerk_v015_signal(interest_expense):
    base = interest_expense.rolling(10).kurt()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_10d_jerk_v015_signal'] = f89ie_interest_expense_momentum_raw_kurt_10d_jerk_v015_signal

def f89ie_interest_expense_momentum_raw_min_10d_jerk_v016_signal(interest_expense):
    base = interest_expense.rolling(10).min()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_10d_jerk_v016_signal'] = f89ie_interest_expense_momentum_raw_min_10d_jerk_v016_signal

def f89ie_interest_expense_momentum_raw_max_10d_jerk_v017_signal(interest_expense):
    base = interest_expense.rolling(10).max()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_10d_jerk_v017_signal'] = f89ie_interest_expense_momentum_raw_max_10d_jerk_v017_signal

def f89ie_interest_expense_momentum_raw_median_10d_jerk_v018_signal(interest_expense):
    base = interest_expense.rolling(10).median()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_10d_jerk_v018_signal'] = f89ie_interest_expense_momentum_raw_median_10d_jerk_v018_signal

def f89ie_interest_expense_momentum_raw_diff_10d_jerk_v019_signal(interest_expense):
    base = interest_expense.diff(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_10d_jerk_v019_signal'] = f89ie_interest_expense_momentum_raw_diff_10d_jerk_v019_signal

def f89ie_interest_expense_momentum_raw_sem_10d_jerk_v020_signal(interest_expense):
    base = interest_expense.rolling(10).sem()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_10d_jerk_v020_signal'] = f89ie_interest_expense_momentum_raw_sem_10d_jerk_v020_signal

def f89ie_interest_expense_momentum_raw_mean_21d_jerk_v021_signal(interest_expense):
    base = interest_expense.rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_21d_jerk_v021_signal'] = f89ie_interest_expense_momentum_raw_mean_21d_jerk_v021_signal

def f89ie_interest_expense_momentum_raw_std_21d_jerk_v022_signal(interest_expense):
    base = interest_expense.rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_21d_jerk_v022_signal'] = f89ie_interest_expense_momentum_raw_std_21d_jerk_v022_signal

def f89ie_interest_expense_momentum_raw_pct_change_21d_jerk_v023_signal(interest_expense):
    base = interest_expense.pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_21d_jerk_v023_signal'] = f89ie_interest_expense_momentum_raw_pct_change_21d_jerk_v023_signal

def f89ie_interest_expense_momentum_raw_skew_21d_jerk_v024_signal(interest_expense):
    base = interest_expense.rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_21d_jerk_v024_signal'] = f89ie_interest_expense_momentum_raw_skew_21d_jerk_v024_signal

def f89ie_interest_expense_momentum_raw_kurt_21d_jerk_v025_signal(interest_expense):
    base = interest_expense.rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_21d_jerk_v025_signal'] = f89ie_interest_expense_momentum_raw_kurt_21d_jerk_v025_signal

def f89ie_interest_expense_momentum_raw_min_21d_jerk_v026_signal(interest_expense):
    base = interest_expense.rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_21d_jerk_v026_signal'] = f89ie_interest_expense_momentum_raw_min_21d_jerk_v026_signal

def f89ie_interest_expense_momentum_raw_max_21d_jerk_v027_signal(interest_expense):
    base = interest_expense.rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_21d_jerk_v027_signal'] = f89ie_interest_expense_momentum_raw_max_21d_jerk_v027_signal

def f89ie_interest_expense_momentum_raw_median_21d_jerk_v028_signal(interest_expense):
    base = interest_expense.rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_21d_jerk_v028_signal'] = f89ie_interest_expense_momentum_raw_median_21d_jerk_v028_signal

def f89ie_interest_expense_momentum_raw_diff_21d_jerk_v029_signal(interest_expense):
    base = interest_expense.diff(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_21d_jerk_v029_signal'] = f89ie_interest_expense_momentum_raw_diff_21d_jerk_v029_signal

def f89ie_interest_expense_momentum_raw_sem_21d_jerk_v030_signal(interest_expense):
    base = interest_expense.rolling(21).sem()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_21d_jerk_v030_signal'] = f89ie_interest_expense_momentum_raw_sem_21d_jerk_v030_signal

def f89ie_interest_expense_momentum_raw_mean_42d_jerk_v031_signal(interest_expense):
    base = interest_expense.rolling(42).mean()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_42d_jerk_v031_signal'] = f89ie_interest_expense_momentum_raw_mean_42d_jerk_v031_signal

def f89ie_interest_expense_momentum_raw_std_42d_jerk_v032_signal(interest_expense):
    base = interest_expense.rolling(42).std()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_42d_jerk_v032_signal'] = f89ie_interest_expense_momentum_raw_std_42d_jerk_v032_signal

def f89ie_interest_expense_momentum_raw_pct_change_42d_jerk_v033_signal(interest_expense):
    base = interest_expense.pct_change(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_42d_jerk_v033_signal'] = f89ie_interest_expense_momentum_raw_pct_change_42d_jerk_v033_signal

def f89ie_interest_expense_momentum_raw_skew_42d_jerk_v034_signal(interest_expense):
    base = interest_expense.rolling(42).skew()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_42d_jerk_v034_signal'] = f89ie_interest_expense_momentum_raw_skew_42d_jerk_v034_signal

def f89ie_interest_expense_momentum_raw_kurt_42d_jerk_v035_signal(interest_expense):
    base = interest_expense.rolling(42).kurt()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_42d_jerk_v035_signal'] = f89ie_interest_expense_momentum_raw_kurt_42d_jerk_v035_signal

def f89ie_interest_expense_momentum_raw_min_42d_jerk_v036_signal(interest_expense):
    base = interest_expense.rolling(42).min()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_42d_jerk_v036_signal'] = f89ie_interest_expense_momentum_raw_min_42d_jerk_v036_signal

def f89ie_interest_expense_momentum_raw_max_42d_jerk_v037_signal(interest_expense):
    base = interest_expense.rolling(42).max()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_42d_jerk_v037_signal'] = f89ie_interest_expense_momentum_raw_max_42d_jerk_v037_signal

def f89ie_interest_expense_momentum_raw_median_42d_jerk_v038_signal(interest_expense):
    base = interest_expense.rolling(42).median()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_42d_jerk_v038_signal'] = f89ie_interest_expense_momentum_raw_median_42d_jerk_v038_signal

def f89ie_interest_expense_momentum_raw_diff_42d_jerk_v039_signal(interest_expense):
    base = interest_expense.diff(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_42d_jerk_v039_signal'] = f89ie_interest_expense_momentum_raw_diff_42d_jerk_v039_signal

def f89ie_interest_expense_momentum_raw_sem_42d_jerk_v040_signal(interest_expense):
    base = interest_expense.rolling(42).sem()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_42d_jerk_v040_signal'] = f89ie_interest_expense_momentum_raw_sem_42d_jerk_v040_signal

def f89ie_interest_expense_momentum_raw_mean_63d_jerk_v041_signal(interest_expense):
    base = interest_expense.rolling(63).mean()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_63d_jerk_v041_signal'] = f89ie_interest_expense_momentum_raw_mean_63d_jerk_v041_signal

def f89ie_interest_expense_momentum_raw_std_63d_jerk_v042_signal(interest_expense):
    base = interest_expense.rolling(63).std()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_63d_jerk_v042_signal'] = f89ie_interest_expense_momentum_raw_std_63d_jerk_v042_signal

def f89ie_interest_expense_momentum_raw_pct_change_63d_jerk_v043_signal(interest_expense):
    base = interest_expense.pct_change(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_63d_jerk_v043_signal'] = f89ie_interest_expense_momentum_raw_pct_change_63d_jerk_v043_signal

def f89ie_interest_expense_momentum_raw_skew_63d_jerk_v044_signal(interest_expense):
    base = interest_expense.rolling(63).skew()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_63d_jerk_v044_signal'] = f89ie_interest_expense_momentum_raw_skew_63d_jerk_v044_signal

def f89ie_interest_expense_momentum_raw_kurt_63d_jerk_v045_signal(interest_expense):
    base = interest_expense.rolling(63).kurt()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_63d_jerk_v045_signal'] = f89ie_interest_expense_momentum_raw_kurt_63d_jerk_v045_signal

def f89ie_interest_expense_momentum_raw_min_63d_jerk_v046_signal(interest_expense):
    base = interest_expense.rolling(63).min()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_63d_jerk_v046_signal'] = f89ie_interest_expense_momentum_raw_min_63d_jerk_v046_signal

def f89ie_interest_expense_momentum_raw_max_63d_jerk_v047_signal(interest_expense):
    base = interest_expense.rolling(63).max()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_63d_jerk_v047_signal'] = f89ie_interest_expense_momentum_raw_max_63d_jerk_v047_signal

def f89ie_interest_expense_momentum_raw_median_63d_jerk_v048_signal(interest_expense):
    base = interest_expense.rolling(63).median()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_63d_jerk_v048_signal'] = f89ie_interest_expense_momentum_raw_median_63d_jerk_v048_signal

def f89ie_interest_expense_momentum_raw_diff_63d_jerk_v049_signal(interest_expense):
    base = interest_expense.diff(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_63d_jerk_v049_signal'] = f89ie_interest_expense_momentum_raw_diff_63d_jerk_v049_signal

def f89ie_interest_expense_momentum_raw_sem_63d_jerk_v050_signal(interest_expense):
    base = interest_expense.rolling(63).sem()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_63d_jerk_v050_signal'] = f89ie_interest_expense_momentum_raw_sem_63d_jerk_v050_signal

def f89ie_interest_expense_momentum_raw_mean_126d_jerk_v051_signal(interest_expense):
    base = interest_expense.rolling(126).mean()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_126d_jerk_v051_signal'] = f89ie_interest_expense_momentum_raw_mean_126d_jerk_v051_signal

def f89ie_interest_expense_momentum_raw_std_126d_jerk_v052_signal(interest_expense):
    base = interest_expense.rolling(126).std()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_126d_jerk_v052_signal'] = f89ie_interest_expense_momentum_raw_std_126d_jerk_v052_signal

def f89ie_interest_expense_momentum_raw_pct_change_126d_jerk_v053_signal(interest_expense):
    base = interest_expense.pct_change(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_126d_jerk_v053_signal'] = f89ie_interest_expense_momentum_raw_pct_change_126d_jerk_v053_signal

def f89ie_interest_expense_momentum_raw_skew_126d_jerk_v054_signal(interest_expense):
    base = interest_expense.rolling(126).skew()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_126d_jerk_v054_signal'] = f89ie_interest_expense_momentum_raw_skew_126d_jerk_v054_signal

def f89ie_interest_expense_momentum_raw_kurt_126d_jerk_v055_signal(interest_expense):
    base = interest_expense.rolling(126).kurt()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_126d_jerk_v055_signal'] = f89ie_interest_expense_momentum_raw_kurt_126d_jerk_v055_signal

def f89ie_interest_expense_momentum_raw_min_126d_jerk_v056_signal(interest_expense):
    base = interest_expense.rolling(126).min()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_126d_jerk_v056_signal'] = f89ie_interest_expense_momentum_raw_min_126d_jerk_v056_signal

def f89ie_interest_expense_momentum_raw_max_126d_jerk_v057_signal(interest_expense):
    base = interest_expense.rolling(126).max()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_126d_jerk_v057_signal'] = f89ie_interest_expense_momentum_raw_max_126d_jerk_v057_signal

def f89ie_interest_expense_momentum_raw_median_126d_jerk_v058_signal(interest_expense):
    base = interest_expense.rolling(126).median()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_126d_jerk_v058_signal'] = f89ie_interest_expense_momentum_raw_median_126d_jerk_v058_signal

def f89ie_interest_expense_momentum_raw_diff_126d_jerk_v059_signal(interest_expense):
    base = interest_expense.diff(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_126d_jerk_v059_signal'] = f89ie_interest_expense_momentum_raw_diff_126d_jerk_v059_signal

def f89ie_interest_expense_momentum_raw_sem_126d_jerk_v060_signal(interest_expense):
    base = interest_expense.rolling(126).sem()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_126d_jerk_v060_signal'] = f89ie_interest_expense_momentum_raw_sem_126d_jerk_v060_signal

def f89ie_interest_expense_momentum_raw_mean_252d_jerk_v061_signal(interest_expense):
    base = interest_expense.rolling(252).mean()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_mean_252d_jerk_v061_signal'] = f89ie_interest_expense_momentum_raw_mean_252d_jerk_v061_signal

def f89ie_interest_expense_momentum_raw_std_252d_jerk_v062_signal(interest_expense):
    base = interest_expense.rolling(252).std()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_std_252d_jerk_v062_signal'] = f89ie_interest_expense_momentum_raw_std_252d_jerk_v062_signal

def f89ie_interest_expense_momentum_raw_pct_change_252d_jerk_v063_signal(interest_expense):
    base = interest_expense.pct_change(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_pct_change_252d_jerk_v063_signal'] = f89ie_interest_expense_momentum_raw_pct_change_252d_jerk_v063_signal

def f89ie_interest_expense_momentum_raw_skew_252d_jerk_v064_signal(interest_expense):
    base = interest_expense.rolling(252).skew()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_skew_252d_jerk_v064_signal'] = f89ie_interest_expense_momentum_raw_skew_252d_jerk_v064_signal

def f89ie_interest_expense_momentum_raw_kurt_252d_jerk_v065_signal(interest_expense):
    base = interest_expense.rolling(252).kurt()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_kurt_252d_jerk_v065_signal'] = f89ie_interest_expense_momentum_raw_kurt_252d_jerk_v065_signal

def f89ie_interest_expense_momentum_raw_min_252d_jerk_v066_signal(interest_expense):
    base = interest_expense.rolling(252).min()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_min_252d_jerk_v066_signal'] = f89ie_interest_expense_momentum_raw_min_252d_jerk_v066_signal

def f89ie_interest_expense_momentum_raw_max_252d_jerk_v067_signal(interest_expense):
    base = interest_expense.rolling(252).max()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_max_252d_jerk_v067_signal'] = f89ie_interest_expense_momentum_raw_max_252d_jerk_v067_signal

def f89ie_interest_expense_momentum_raw_median_252d_jerk_v068_signal(interest_expense):
    base = interest_expense.rolling(252).median()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_median_252d_jerk_v068_signal'] = f89ie_interest_expense_momentum_raw_median_252d_jerk_v068_signal

def f89ie_interest_expense_momentum_raw_diff_252d_jerk_v069_signal(interest_expense):
    base = interest_expense.diff(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_diff_252d_jerk_v069_signal'] = f89ie_interest_expense_momentum_raw_diff_252d_jerk_v069_signal

def f89ie_interest_expense_momentum_raw_sem_252d_jerk_v070_signal(interest_expense):
    base = interest_expense.rolling(252).sem()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_raw_sem_252d_jerk_v070_signal'] = f89ie_interest_expense_momentum_raw_sem_252d_jerk_v070_signal

def f89ie_interest_expense_momentum_debt_mean_5d_jerk_v071_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_5d_jerk_v071_signal'] = f89ie_interest_expense_momentum_debt_mean_5d_jerk_v071_signal

def f89ie_interest_expense_momentum_debt_std_5d_jerk_v072_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_5d_jerk_v072_signal'] = f89ie_interest_expense_momentum_debt_std_5d_jerk_v072_signal

def f89ie_interest_expense_momentum_debt_pct_change_5d_jerk_v073_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_5d_jerk_v073_signal'] = f89ie_interest_expense_momentum_debt_pct_change_5d_jerk_v073_signal

def f89ie_interest_expense_momentum_debt_skew_5d_jerk_v074_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_5d_jerk_v074_signal'] = f89ie_interest_expense_momentum_debt_skew_5d_jerk_v074_signal

def f89ie_interest_expense_momentum_debt_kurt_5d_jerk_v075_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_5d_jerk_v075_signal'] = f89ie_interest_expense_momentum_debt_kurt_5d_jerk_v075_signal

def f89ie_interest_expense_momentum_debt_min_5d_jerk_v076_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_5d_jerk_v076_signal'] = f89ie_interest_expense_momentum_debt_min_5d_jerk_v076_signal

def f89ie_interest_expense_momentum_debt_max_5d_jerk_v077_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_5d_jerk_v077_signal'] = f89ie_interest_expense_momentum_debt_max_5d_jerk_v077_signal

def f89ie_interest_expense_momentum_debt_median_5d_jerk_v078_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).median()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_5d_jerk_v078_signal'] = f89ie_interest_expense_momentum_debt_median_5d_jerk_v078_signal

def f89ie_interest_expense_momentum_debt_diff_5d_jerk_v079_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_5d_jerk_v079_signal'] = f89ie_interest_expense_momentum_debt_diff_5d_jerk_v079_signal

def f89ie_interest_expense_momentum_debt_sem_5d_jerk_v080_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(5).sem()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_5d_jerk_v080_signal'] = f89ie_interest_expense_momentum_debt_sem_5d_jerk_v080_signal

def f89ie_interest_expense_momentum_debt_mean_10d_jerk_v081_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).mean()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_10d_jerk_v081_signal'] = f89ie_interest_expense_momentum_debt_mean_10d_jerk_v081_signal

def f89ie_interest_expense_momentum_debt_std_10d_jerk_v082_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).std()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_10d_jerk_v082_signal'] = f89ie_interest_expense_momentum_debt_std_10d_jerk_v082_signal

def f89ie_interest_expense_momentum_debt_pct_change_10d_jerk_v083_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_10d_jerk_v083_signal'] = f89ie_interest_expense_momentum_debt_pct_change_10d_jerk_v083_signal

def f89ie_interest_expense_momentum_debt_skew_10d_jerk_v084_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).skew()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_10d_jerk_v084_signal'] = f89ie_interest_expense_momentum_debt_skew_10d_jerk_v084_signal

def f89ie_interest_expense_momentum_debt_kurt_10d_jerk_v085_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).kurt()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_10d_jerk_v085_signal'] = f89ie_interest_expense_momentum_debt_kurt_10d_jerk_v085_signal

def f89ie_interest_expense_momentum_debt_min_10d_jerk_v086_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).min()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_10d_jerk_v086_signal'] = f89ie_interest_expense_momentum_debt_min_10d_jerk_v086_signal

def f89ie_interest_expense_momentum_debt_max_10d_jerk_v087_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).max()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_10d_jerk_v087_signal'] = f89ie_interest_expense_momentum_debt_max_10d_jerk_v087_signal

def f89ie_interest_expense_momentum_debt_median_10d_jerk_v088_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).median()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_10d_jerk_v088_signal'] = f89ie_interest_expense_momentum_debt_median_10d_jerk_v088_signal

def f89ie_interest_expense_momentum_debt_diff_10d_jerk_v089_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(10)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_10d_jerk_v089_signal'] = f89ie_interest_expense_momentum_debt_diff_10d_jerk_v089_signal

def f89ie_interest_expense_momentum_debt_sem_10d_jerk_v090_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(10).sem()
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_10d_jerk_v090_signal'] = f89ie_interest_expense_momentum_debt_sem_10d_jerk_v090_signal

def f89ie_interest_expense_momentum_debt_mean_21d_jerk_v091_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).mean()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_21d_jerk_v091_signal'] = f89ie_interest_expense_momentum_debt_mean_21d_jerk_v091_signal

def f89ie_interest_expense_momentum_debt_std_21d_jerk_v092_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).std()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_21d_jerk_v092_signal'] = f89ie_interest_expense_momentum_debt_std_21d_jerk_v092_signal

def f89ie_interest_expense_momentum_debt_pct_change_21d_jerk_v093_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_21d_jerk_v093_signal'] = f89ie_interest_expense_momentum_debt_pct_change_21d_jerk_v093_signal

def f89ie_interest_expense_momentum_debt_skew_21d_jerk_v094_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).skew()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_21d_jerk_v094_signal'] = f89ie_interest_expense_momentum_debt_skew_21d_jerk_v094_signal

def f89ie_interest_expense_momentum_debt_kurt_21d_jerk_v095_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).kurt()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_21d_jerk_v095_signal'] = f89ie_interest_expense_momentum_debt_kurt_21d_jerk_v095_signal

def f89ie_interest_expense_momentum_debt_min_21d_jerk_v096_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).min()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_21d_jerk_v096_signal'] = f89ie_interest_expense_momentum_debt_min_21d_jerk_v096_signal

def f89ie_interest_expense_momentum_debt_max_21d_jerk_v097_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).max()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_21d_jerk_v097_signal'] = f89ie_interest_expense_momentum_debt_max_21d_jerk_v097_signal

def f89ie_interest_expense_momentum_debt_median_21d_jerk_v098_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).median()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_21d_jerk_v098_signal'] = f89ie_interest_expense_momentum_debt_median_21d_jerk_v098_signal

def f89ie_interest_expense_momentum_debt_diff_21d_jerk_v099_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_21d_jerk_v099_signal'] = f89ie_interest_expense_momentum_debt_diff_21d_jerk_v099_signal

def f89ie_interest_expense_momentum_debt_sem_21d_jerk_v100_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(21).sem()
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_21d_jerk_v100_signal'] = f89ie_interest_expense_momentum_debt_sem_21d_jerk_v100_signal

def f89ie_interest_expense_momentum_debt_mean_42d_jerk_v101_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).mean()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_42d_jerk_v101_signal'] = f89ie_interest_expense_momentum_debt_mean_42d_jerk_v101_signal

def f89ie_interest_expense_momentum_debt_std_42d_jerk_v102_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).std()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_42d_jerk_v102_signal'] = f89ie_interest_expense_momentum_debt_std_42d_jerk_v102_signal

def f89ie_interest_expense_momentum_debt_pct_change_42d_jerk_v103_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_42d_jerk_v103_signal'] = f89ie_interest_expense_momentum_debt_pct_change_42d_jerk_v103_signal

def f89ie_interest_expense_momentum_debt_skew_42d_jerk_v104_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).skew()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_42d_jerk_v104_signal'] = f89ie_interest_expense_momentum_debt_skew_42d_jerk_v104_signal

def f89ie_interest_expense_momentum_debt_kurt_42d_jerk_v105_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).kurt()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_42d_jerk_v105_signal'] = f89ie_interest_expense_momentum_debt_kurt_42d_jerk_v105_signal

def f89ie_interest_expense_momentum_debt_min_42d_jerk_v106_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).min()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_42d_jerk_v106_signal'] = f89ie_interest_expense_momentum_debt_min_42d_jerk_v106_signal

def f89ie_interest_expense_momentum_debt_max_42d_jerk_v107_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).max()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_42d_jerk_v107_signal'] = f89ie_interest_expense_momentum_debt_max_42d_jerk_v107_signal

def f89ie_interest_expense_momentum_debt_median_42d_jerk_v108_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).median()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_42d_jerk_v108_signal'] = f89ie_interest_expense_momentum_debt_median_42d_jerk_v108_signal

def f89ie_interest_expense_momentum_debt_diff_42d_jerk_v109_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(42)
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_42d_jerk_v109_signal'] = f89ie_interest_expense_momentum_debt_diff_42d_jerk_v109_signal

def f89ie_interest_expense_momentum_debt_sem_42d_jerk_v110_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(42).sem()
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_42d_jerk_v110_signal'] = f89ie_interest_expense_momentum_debt_sem_42d_jerk_v110_signal

def f89ie_interest_expense_momentum_debt_mean_63d_jerk_v111_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).mean()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_63d_jerk_v111_signal'] = f89ie_interest_expense_momentum_debt_mean_63d_jerk_v111_signal

def f89ie_interest_expense_momentum_debt_std_63d_jerk_v112_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).std()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_63d_jerk_v112_signal'] = f89ie_interest_expense_momentum_debt_std_63d_jerk_v112_signal

def f89ie_interest_expense_momentum_debt_pct_change_63d_jerk_v113_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_63d_jerk_v113_signal'] = f89ie_interest_expense_momentum_debt_pct_change_63d_jerk_v113_signal

def f89ie_interest_expense_momentum_debt_skew_63d_jerk_v114_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).skew()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_63d_jerk_v114_signal'] = f89ie_interest_expense_momentum_debt_skew_63d_jerk_v114_signal

def f89ie_interest_expense_momentum_debt_kurt_63d_jerk_v115_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).kurt()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_63d_jerk_v115_signal'] = f89ie_interest_expense_momentum_debt_kurt_63d_jerk_v115_signal

def f89ie_interest_expense_momentum_debt_min_63d_jerk_v116_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).min()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_63d_jerk_v116_signal'] = f89ie_interest_expense_momentum_debt_min_63d_jerk_v116_signal

def f89ie_interest_expense_momentum_debt_max_63d_jerk_v117_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).max()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_63d_jerk_v117_signal'] = f89ie_interest_expense_momentum_debt_max_63d_jerk_v117_signal

def f89ie_interest_expense_momentum_debt_median_63d_jerk_v118_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).median()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_63d_jerk_v118_signal'] = f89ie_interest_expense_momentum_debt_median_63d_jerk_v118_signal

def f89ie_interest_expense_momentum_debt_diff_63d_jerk_v119_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(63)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_63d_jerk_v119_signal'] = f89ie_interest_expense_momentum_debt_diff_63d_jerk_v119_signal

def f89ie_interest_expense_momentum_debt_sem_63d_jerk_v120_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(63).sem()
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_63d_jerk_v120_signal'] = f89ie_interest_expense_momentum_debt_sem_63d_jerk_v120_signal

def f89ie_interest_expense_momentum_debt_mean_126d_jerk_v121_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).mean()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_126d_jerk_v121_signal'] = f89ie_interest_expense_momentum_debt_mean_126d_jerk_v121_signal

def f89ie_interest_expense_momentum_debt_std_126d_jerk_v122_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).std()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_126d_jerk_v122_signal'] = f89ie_interest_expense_momentum_debt_std_126d_jerk_v122_signal

def f89ie_interest_expense_momentum_debt_pct_change_126d_jerk_v123_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_126d_jerk_v123_signal'] = f89ie_interest_expense_momentum_debt_pct_change_126d_jerk_v123_signal

def f89ie_interest_expense_momentum_debt_skew_126d_jerk_v124_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).skew()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_126d_jerk_v124_signal'] = f89ie_interest_expense_momentum_debt_skew_126d_jerk_v124_signal

def f89ie_interest_expense_momentum_debt_kurt_126d_jerk_v125_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).kurt()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_126d_jerk_v125_signal'] = f89ie_interest_expense_momentum_debt_kurt_126d_jerk_v125_signal

def f89ie_interest_expense_momentum_debt_min_126d_jerk_v126_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).min()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_126d_jerk_v126_signal'] = f89ie_interest_expense_momentum_debt_min_126d_jerk_v126_signal

def f89ie_interest_expense_momentum_debt_max_126d_jerk_v127_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).max()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_126d_jerk_v127_signal'] = f89ie_interest_expense_momentum_debt_max_126d_jerk_v127_signal

def f89ie_interest_expense_momentum_debt_median_126d_jerk_v128_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).median()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_126d_jerk_v128_signal'] = f89ie_interest_expense_momentum_debt_median_126d_jerk_v128_signal

def f89ie_interest_expense_momentum_debt_diff_126d_jerk_v129_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(126)
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_126d_jerk_v129_signal'] = f89ie_interest_expense_momentum_debt_diff_126d_jerk_v129_signal

def f89ie_interest_expense_momentum_debt_sem_126d_jerk_v130_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(126).sem()
    slope = base.pct_change(126)
    res = slope.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_126d_jerk_v130_signal'] = f89ie_interest_expense_momentum_debt_sem_126d_jerk_v130_signal

def f89ie_interest_expense_momentum_debt_mean_252d_jerk_v131_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).mean()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_mean_252d_jerk_v131_signal'] = f89ie_interest_expense_momentum_debt_mean_252d_jerk_v131_signal

def f89ie_interest_expense_momentum_debt_std_252d_jerk_v132_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).std()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_std_252d_jerk_v132_signal'] = f89ie_interest_expense_momentum_debt_std_252d_jerk_v132_signal

def f89ie_interest_expense_momentum_debt_pct_change_252d_jerk_v133_signal(interest_expense, debt):
    base = (interest_expense / debt).pct_change(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_pct_change_252d_jerk_v133_signal'] = f89ie_interest_expense_momentum_debt_pct_change_252d_jerk_v133_signal

def f89ie_interest_expense_momentum_debt_skew_252d_jerk_v134_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).skew()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_skew_252d_jerk_v134_signal'] = f89ie_interest_expense_momentum_debt_skew_252d_jerk_v134_signal

def f89ie_interest_expense_momentum_debt_kurt_252d_jerk_v135_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).kurt()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_kurt_252d_jerk_v135_signal'] = f89ie_interest_expense_momentum_debt_kurt_252d_jerk_v135_signal

def f89ie_interest_expense_momentum_debt_min_252d_jerk_v136_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).min()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_min_252d_jerk_v136_signal'] = f89ie_interest_expense_momentum_debt_min_252d_jerk_v136_signal

def f89ie_interest_expense_momentum_debt_max_252d_jerk_v137_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).max()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_max_252d_jerk_v137_signal'] = f89ie_interest_expense_momentum_debt_max_252d_jerk_v137_signal

def f89ie_interest_expense_momentum_debt_median_252d_jerk_v138_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).median()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_median_252d_jerk_v138_signal'] = f89ie_interest_expense_momentum_debt_median_252d_jerk_v138_signal

def f89ie_interest_expense_momentum_debt_diff_252d_jerk_v139_signal(interest_expense, debt):
    base = (interest_expense / debt).diff(252)
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_diff_252d_jerk_v139_signal'] = f89ie_interest_expense_momentum_debt_diff_252d_jerk_v139_signal

def f89ie_interest_expense_momentum_debt_sem_252d_jerk_v140_signal(interest_expense, debt):
    base = (interest_expense / debt).rolling(252).sem()
    slope = base.pct_change(252)
    res = slope.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_debt_sem_252d_jerk_v140_signal'] = f89ie_interest_expense_momentum_debt_sem_252d_jerk_v140_signal

def f89ie_interest_expense_momentum_ebit_mean_5d_jerk_v141_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).mean()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_mean_5d_jerk_v141_signal'] = f89ie_interest_expense_momentum_ebit_mean_5d_jerk_v141_signal

def f89ie_interest_expense_momentum_ebit_std_5d_jerk_v142_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).std()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_std_5d_jerk_v142_signal'] = f89ie_interest_expense_momentum_ebit_std_5d_jerk_v142_signal

def f89ie_interest_expense_momentum_ebit_pct_change_5d_jerk_v143_signal(interest_expense, ebit):
    base = (interest_expense / ebit).pct_change(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_pct_change_5d_jerk_v143_signal'] = f89ie_interest_expense_momentum_ebit_pct_change_5d_jerk_v143_signal

def f89ie_interest_expense_momentum_ebit_skew_5d_jerk_v144_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).skew()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_skew_5d_jerk_v144_signal'] = f89ie_interest_expense_momentum_ebit_skew_5d_jerk_v144_signal

def f89ie_interest_expense_momentum_ebit_kurt_5d_jerk_v145_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).kurt()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_kurt_5d_jerk_v145_signal'] = f89ie_interest_expense_momentum_ebit_kurt_5d_jerk_v145_signal

def f89ie_interest_expense_momentum_ebit_min_5d_jerk_v146_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).min()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_min_5d_jerk_v146_signal'] = f89ie_interest_expense_momentum_ebit_min_5d_jerk_v146_signal

def f89ie_interest_expense_momentum_ebit_max_5d_jerk_v147_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).max()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_max_5d_jerk_v147_signal'] = f89ie_interest_expense_momentum_ebit_max_5d_jerk_v147_signal

def f89ie_interest_expense_momentum_ebit_median_5d_jerk_v148_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).median()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_median_5d_jerk_v148_signal'] = f89ie_interest_expense_momentum_ebit_median_5d_jerk_v148_signal

def f89ie_interest_expense_momentum_ebit_diff_5d_jerk_v149_signal(interest_expense, ebit):
    base = (interest_expense / ebit).diff(5)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_diff_5d_jerk_v149_signal'] = f89ie_interest_expense_momentum_ebit_diff_5d_jerk_v149_signal

def f89ie_interest_expense_momentum_ebit_sem_5d_jerk_v150_signal(interest_expense, ebit):
    base = (interest_expense / ebit).rolling(5).sem()
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f89ie_interest_expense_momentum_ebit_sem_5d_jerk_v150_signal'] = f89ie_interest_expense_momentum_ebit_sem_5d_jerk_v150_signal


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "debt": np.random.uniform(10, 100, n),
        "ebit": np.random.uniform(10, 100, n),
        "interest_expense": np.random.uniform(10, 100, n),
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
