import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f71rs_f71_revenue_per_share_acceleration_accel_mean_5d_base_v001_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_5d_base_v001_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_5d_base_v001_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_10d_base_v002_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_10d_base_v002_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_10d_base_v002_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_21d_base_v003_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_21d_base_v003_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_21d_base_v003_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_42d_base_v004_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_42d_base_v004_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_42d_base_v004_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_63d_base_v005_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_63d_base_v005_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_63d_base_v005_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_126d_base_v006_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_126d_base_v006_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_126d_base_v006_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_252d_base_v007_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_252d_base_v007_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_252d_base_v007_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_15d_base_v008_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_15d_base_v008_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_15d_base_v008_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_30d_base_v009_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_30d_base_v009_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_30d_base_v009_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_90d_base_v010_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_90d_base_v010_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_90d_base_v010_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_150d_base_v011_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_150d_base_v011_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_150d_base_v011_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_200d_base_v012_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_200d_base_v012_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_200d_base_v012_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_300d_base_v013_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_300d_base_v013_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_300d_base_v013_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_5d_base_v014_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_5d_base_v014_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_5d_base_v014_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_10d_base_v015_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_10d_base_v015_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_10d_base_v015_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_21d_base_v016_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_21d_base_v016_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_21d_base_v016_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_252d_base_v017_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_252d_base_v017_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_252d_base_v017_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_15d_base_v018_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_15d_base_v018_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_15d_base_v018_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_30d_base_v019_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_30d_base_v019_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_30d_base_v019_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_200d_base_v020_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_200d_base_v020_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_200d_base_v020_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_5d_base_v021_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_5d_base_v021_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_5d_base_v021_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_10d_base_v022_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_10d_base_v022_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_10d_base_v022_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_21d_base_v023_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_21d_base_v023_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_21d_base_v023_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_42d_base_v024_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_42d_base_v024_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_42d_base_v024_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_63d_base_v025_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_63d_base_v025_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_63d_base_v025_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_126d_base_v026_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_126d_base_v026_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_126d_base_v026_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_252d_base_v027_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_252d_base_v027_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_252d_base_v027_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_15d_base_v028_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_15d_base_v028_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_15d_base_v028_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_30d_base_v029_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_30d_base_v029_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_30d_base_v029_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_90d_base_v030_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_90d_base_v030_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_90d_base_v030_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_150d_base_v031_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_150d_base_v031_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_150d_base_v031_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_200d_base_v032_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_200d_base_v032_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_200d_base_v032_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_mean_300d_base_v033_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_mean_300d_base_v033_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_mean_300d_base_v033_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_std_5d_base_v034_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_std_5d_base_v034_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_std_5d_base_v034_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_5d_base_v035_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_5d_base_v035_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_5d_base_v035_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_10d_base_v036_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_10d_base_v036_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_10d_base_v036_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_21d_base_v037_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_21d_base_v037_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_21d_base_v037_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_42d_base_v038_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_42d_base_v038_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_42d_base_v038_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_63d_base_v039_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_63d_base_v039_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_63d_base_v039_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_126d_base_v040_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_126d_base_v040_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_126d_base_v040_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_252d_base_v041_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_252d_base_v041_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_252d_base_v041_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_15d_base_v042_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(15).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_15d_base_v042_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_15d_base_v042_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_30d_base_v043_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_30d_base_v043_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_30d_base_v043_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_90d_base_v044_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_90d_base_v044_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_90d_base_v044_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_150d_base_v045_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(150).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_150d_base_v045_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_150d_base_v045_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_200d_base_v046_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(200).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_200d_base_v046_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_200d_base_v046_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_300d_base_v047_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(300).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_300d_base_v047_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_300d_base_v047_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_5d_base_v048_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(5).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_5d_base_v048_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_5d_base_v048_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_10d_base_v049_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(10).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_10d_base_v049_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_10d_base_v049_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_21d_base_v050_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(21).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_21d_base_v050_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_21d_base_v050_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_42d_base_v051_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(42).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_42d_base_v051_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_42d_base_v051_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_252d_base_v052_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(252).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_252d_base_v052_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_252d_base_v052_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_15d_base_v053_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(15).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_15d_base_v053_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_15d_base_v053_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_30d_base_v054_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(30).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_30d_base_v054_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_30d_base_v054_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_200d_base_v055_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(200).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_200d_base_v055_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_200d_base_v055_signal

def f71rs_f71_revenue_per_share_acceleration_rps_kurt_300d_base_v056_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(300).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_kurt_300d_base_v056_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_kurt_300d_base_v056_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_5d_base_v057_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_5d_base_v057_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_5d_base_v057_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_10d_base_v058_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_10d_base_v058_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_10d_base_v058_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_max_5d_base_v059_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(5).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_max_5d_base_v059_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_max_5d_base_v059_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_max_10d_base_v060_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(10).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_max_10d_base_v060_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_max_10d_base_v060_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_max_21d_base_v061_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_max_21d_base_v061_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_max_21d_base_v061_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_max_63d_base_v062_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_max_63d_base_v062_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_max_63d_base_v062_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_min_5d_base_v063_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(5).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_min_5d_base_v063_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_min_5d_base_v063_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_min_10d_base_v064_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(10).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_min_10d_base_v064_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_min_10d_base_v064_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_min_21d_base_v065_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_min_21d_base_v065_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_min_21d_base_v065_signal

def f71rs_f71_revenue_per_share_acceleration_rps_to_min_126d_base_v066_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps / rps.rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_to_min_126d_base_v066_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_to_min_126d_base_v066_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_5d_base_v067_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel / accel.rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_5d_base_v067_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_5d_base_v067_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_10d_base_v068_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel / accel.rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_10d_base_v068_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_10d_base_v068_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_42d_base_v069_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel / accel.rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_42d_base_v069_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_42d_base_v069_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_5d_base_v070_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_5d_base_v070_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_5d_base_v070_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_10d_base_v071_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_10d_base_v071_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_10d_base_v071_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_21d_base_v072_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_21d_base_v072_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_21d_base_v072_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_42d_base_v073_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_42d_base_v073_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_42d_base_v073_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_63d_base_v074_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_63d_base_v074_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_63d_base_v074_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_126d_base_v075_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_126d_base_v075_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_126d_base_v075_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "sharesbas": np.random.uniform(100, 500, n),
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
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                assert corr_matrix.iloc[i, j] <= 0.95, f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}"
    print(f"Self-test passed for {os.path.basename(__file__)}")
