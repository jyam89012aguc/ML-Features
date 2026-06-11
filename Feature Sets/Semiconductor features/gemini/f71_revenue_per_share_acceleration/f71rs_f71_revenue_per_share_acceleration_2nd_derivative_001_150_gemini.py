import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_5d_v001_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_5d_v001_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_5d_v001_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_10d_v002_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).mean().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_10d_v002_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_10d_v002_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_21d_v003_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_21d_v003_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_21d_v003_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_42d_v004_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).mean().pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_42d_v004_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_42d_v004_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_63d_v005_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_63d_v005_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_63d_v005_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_126d_v006_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).mean().pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_126d_v006_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_126d_v006_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_252d_v007_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).mean().pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_252d_v007_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_252d_v007_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_15d_v008_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).mean().pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_15d_v008_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_15d_v008_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_30d_v009_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).mean().pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_30d_v009_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_30d_v009_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_90d_v010_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).mean().pct_change(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_90d_v010_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_90d_v010_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_150d_v011_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).mean().pct_change(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_150d_v011_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_150d_v011_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_200d_v012_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).mean().pct_change(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_200d_v012_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_200d_v012_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_300d_v013_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).mean().pct_change(300)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_300d_v013_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_300d_v013_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_5d_v014_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_5d_v014_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_5d_v014_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_10d_v015_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).std().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_10d_v015_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_10d_v015_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_21d_v016_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_21d_v016_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_21d_v016_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_42d_v017_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).std().pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_42d_v017_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_42d_v017_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_63d_v018_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).std().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_63d_v018_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_63d_v018_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_15d_v019_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).std().pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_15d_v019_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_15d_v019_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_30d_v020_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).std().pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_30d_v020_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_30d_v020_signal

def f71rs_f71_revenue_per_share_acceleration_accel_std_slope_90d_v021_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).std().pct_change(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_std_slope_90d_v021_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_std_slope_90d_v021_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_5d_v022_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(5).skew().diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_5d_v022_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_5d_v022_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_10d_v023_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(10).skew().diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_10d_v023_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_10d_v023_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_21d_v024_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(21).skew().diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_21d_v024_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_21d_v024_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_42d_v025_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(42).skew().diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_42d_v025_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_42d_v025_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_63d_v026_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(63).skew().diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_63d_v026_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_63d_v026_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_126d_v027_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(126).skew().diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_126d_v027_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_126d_v027_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_252d_v028_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(252).skew().diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_252d_v028_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_252d_v028_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_15d_v029_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(15).skew().diff(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_15d_v029_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_15d_v029_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_30d_v030_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(30).skew().diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_30d_v030_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_30d_v030_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_90d_v031_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(90).skew().diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_90d_v031_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_90d_v031_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_150d_v032_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(150).skew().diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_150d_v032_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_150d_v032_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_200d_v033_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(200).skew().diff(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_200d_v033_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_200d_v033_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_300d_v034_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(300).skew().diff(300)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_300d_v034_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_slope_300d_v034_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_5d_v035_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).rank(pct=True).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_5d_v035_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_5d_v035_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_10d_v036_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).rank(pct=True).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_10d_v036_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_10d_v036_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_21d_v037_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).rank(pct=True).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_21d_v037_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_21d_v037_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_42d_v038_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).rank(pct=True).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_42d_v038_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_42d_v038_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_63d_v039_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).rank(pct=True).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_63d_v039_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_63d_v039_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_126d_v040_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).rank(pct=True).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_126d_v040_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_126d_v040_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_252d_v041_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).rank(pct=True).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_252d_v041_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_252d_v041_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_15d_v042_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).rank(pct=True).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_15d_v042_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_15d_v042_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_30d_v043_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).rank(pct=True).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_30d_v043_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_30d_v043_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_90d_v044_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).rank(pct=True).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_90d_v044_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_90d_v044_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_150d_v045_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).rank(pct=True).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_150d_v045_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_150d_v045_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_200d_v046_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).rank(pct=True).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_200d_v046_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_200d_v046_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_std_300d_v047_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).rank(pct=True).rolling(300).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_std_300d_v047_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_std_300d_v047_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_5d_v048_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(5).std()).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_5d_v048_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_5d_v048_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_10d_v049_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(10).std()).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_10d_v049_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_10d_v049_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_21d_v050_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(21).std()).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_21d_v050_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_21d_v050_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_5d_v051_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_5d_v051_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_5d_v051_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_10d_v052_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_10d_v052_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_10d_v052_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_21d_v053_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(21).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_21d_v053_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_21d_v053_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_42d_v054_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(42).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_42d_v054_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_42d_v054_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_63d_v055_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(63).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_63d_v055_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_63d_v055_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_126d_v056_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(126).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_126d_v056_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_126d_v056_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_252d_v057_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(252).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_252d_v057_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_252d_v057_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_15d_v058_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(15).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_15d_v058_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_15d_v058_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_30d_v059_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(30).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_30d_v059_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_30d_v059_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_90d_v060_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(90).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_90d_v060_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_90d_v060_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_150d_v061_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(150).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_150d_v061_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_150d_v061_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_200d_v062_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(200).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_200d_v062_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_200d_v062_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_300d_v063_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(300).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_300d_v063_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_300d_v063_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_5d_v064_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(5).std() / np.log(rps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_5d_v064_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_5d_v064_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_10d_v065_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(10).std() / np.log(rps).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_10d_v065_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_10d_v065_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_21d_v066_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(21).std() / np.log(rps).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_21d_v066_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_21d_v066_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_42d_v067_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(42).std() / np.log(rps).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_42d_v067_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_42d_v067_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_63d_v068_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(63).std() / np.log(rps).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_63d_v068_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_63d_v068_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_126d_v069_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(126).std() / np.log(rps).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_126d_v069_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_126d_v069_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_252d_v070_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(252).std() / np.log(rps).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_252d_v070_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_252d_v070_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_15d_v071_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(15).std() / np.log(rps).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_15d_v071_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_15d_v071_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_30d_v072_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(30).std() / np.log(rps).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_30d_v072_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_30d_v072_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_90d_v073_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(90).std() / np.log(rps).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_90d_v073_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_90d_v073_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_150d_v074_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(150).std() / np.log(rps).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_150d_v074_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_150d_v074_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_200d_v075_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(200).std() / np.log(rps).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_200d_v075_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_200d_v075_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_300d_v076_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(300).std() / np.log(rps).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_300d_v076_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_300d_v076_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_5d_v077_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).rank(pct=True).diff().rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_5d_v077_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_5d_v077_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_10d_v078_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).rank(pct=True).diff().rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_10d_v078_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_10d_v078_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_21d_v079_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).rank(pct=True).diff().rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_21d_v079_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_21d_v079_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_42d_v080_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).rank(pct=True).diff().rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_42d_v080_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_42d_v080_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_63d_v081_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).rank(pct=True).diff().rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_63d_v081_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_63d_v081_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_15d_v082_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).rank(pct=True).diff().rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_15d_v082_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_15d_v082_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_30d_v083_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).rank(pct=True).diff().rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_30d_v083_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_30d_v083_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_300d_v084_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).rank(pct=True).diff().rolling(300).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_300d_v084_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_std_300d_v084_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_5d_v085_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(5).rank(pct=True).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_5d_v085_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_5d_v085_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_10d_v086_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(10).rank(pct=True).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_10d_v086_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_10d_v086_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_21d_v087_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(21).rank(pct=True).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_21d_v087_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_21d_v087_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_42d_v088_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(42).rank(pct=True).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_42d_v088_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_42d_v088_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_63d_v089_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(63).rank(pct=True).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_63d_v089_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_63d_v089_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_126d_v090_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(126).rank(pct=True).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_126d_v090_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_126d_v090_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_252d_v091_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(252).rank(pct=True).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_252d_v091_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_252d_v091_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_15d_v092_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(15).rank(pct=True).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_15d_v092_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_15d_v092_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_30d_v093_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(30).rank(pct=True).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_30d_v093_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_30d_v093_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_90d_v094_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(90).rank(pct=True).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_90d_v094_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_90d_v094_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_150d_v095_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(150).rank(pct=True).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_150d_v095_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_150d_v095_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_200d_v096_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(200).rank(pct=True).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_200d_v096_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_200d_v096_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_300d_v097_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(300).rank(pct=True).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_300d_v097_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_300d_v097_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_5d_v098_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(5).std() / accel.rolling(5).mean().abs()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_5d_v098_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_5d_v098_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_10d_v099_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(10).std() / accel.rolling(10).mean().abs()).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_10d_v099_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_10d_v099_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_21d_v100_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(21).std() / accel.rolling(21).mean().abs()).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_21d_v100_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_21d_v100_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_42d_v101_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(42).std() / accel.rolling(42).mean().abs()).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_42d_v101_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_42d_v101_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_63d_v102_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(63).std() / accel.rolling(63).mean().abs()).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_63d_v102_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_63d_v102_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_126d_v103_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(126).std() / accel.rolling(126).mean().abs()).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_126d_v103_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_126d_v103_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_252d_v104_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(252).std() / accel.rolling(252).mean().abs()).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_252d_v104_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_252d_v104_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_15d_v105_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(15).std() / accel.rolling(15).mean().abs()).diff(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_15d_v105_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_15d_v105_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_30d_v106_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(30).std() / accel.rolling(30).mean().abs()).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_30d_v106_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_30d_v106_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_90d_v107_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(90).std() / accel.rolling(90).mean().abs()).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_90d_v107_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_90d_v107_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_150d_v108_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(150).std() / accel.rolling(150).mean().abs()).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_150d_v108_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_150d_v108_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_200d_v109_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(200).std() / accel.rolling(200).mean().abs()).diff(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_200d_v109_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_200d_v109_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_300d_v110_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(300).std() / accel.rolling(300).mean().abs()).diff(300)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_300d_v110_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_diff_300d_v110_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_5d_v111_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).skew().rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_5d_v111_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_5d_v111_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_10d_v112_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).skew().rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_10d_v112_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_10d_v112_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_21d_v113_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).skew().rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_21d_v113_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_21d_v113_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_42d_v114_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).skew().rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_42d_v114_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_42d_v114_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_63d_v115_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).skew().rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_63d_v115_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_63d_v115_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_126d_v116_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).skew().rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_126d_v116_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_126d_v116_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_252d_v117_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).skew().rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_252d_v117_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_252d_v117_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_15d_v118_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).skew().rolling(15).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_15d_v118_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_15d_v118_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_30d_v119_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).skew().rolling(30).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_30d_v119_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_30d_v119_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_90d_v120_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).skew().rolling(90).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_90d_v120_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_90d_v120_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_150d_v121_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).skew().rolling(150).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_150d_v121_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_150d_v121_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_200d_v122_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).skew().rolling(200).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_200d_v122_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_200d_v122_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_300d_v123_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).skew().rolling(300).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_300d_v123_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_300d_v123_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_5d_v124_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_5d_v124_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_5d_v124_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_10d_v125_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_10d_v125_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_10d_v125_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_21d_v126_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_21d_v126_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_21d_v126_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_42d_v127_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(42).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_42d_v127_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_42d_v127_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_63d_v128_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_63d_v128_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_63d_v128_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_126d_v129_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(126).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_126d_v129_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_126d_v129_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_252d_v130_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(252).pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_252d_v130_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_252d_v130_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_15d_v131_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(15).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_15d_v131_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_15d_v131_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_30d_v132_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(30).pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_30d_v132_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_30d_v132_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_90d_v133_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(90).pct_change(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_90d_v133_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_90d_v133_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_150d_v134_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(150).pct_change(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_150d_v134_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_150d_v134_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_200d_v135_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(200).pct_change(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_200d_v135_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_200d_v135_signal

def f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_300d_v136_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.diff(300).pct_change(300)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_300d_v136_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_diff_accel_300d_v136_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_5d_v137_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_5d_v137_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_5d_v137_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_10d_v138_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_10d_v138_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_10d_v138_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_21d_v139_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_21d_v139_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_21d_v139_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_42d_v140_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_42d_v140_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_42d_v140_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_63d_v141_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_63d_v141_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_63d_v141_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_126d_v142_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_126d_v142_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_126d_v142_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_252d_v143_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_252d_v143_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_252d_v143_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_15d_v144_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_15d_v144_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_15d_v144_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_30d_v145_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_30d_v145_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_30d_v145_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_90d_v146_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_90d_v146_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_90d_v146_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_150d_v147_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_150d_v147_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_150d_v147_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_200d_v148_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_200d_v148_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_200d_v148_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_300d_v149_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_300d_v149_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_300d_v149_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_zscore_5d_v150_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel.rolling(5).mean() - accel.rolling(252 if 5*2 > 252 else 5*2).mean()) / accel.rolling(252 if 5*2 > 252 else 5*2).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_zscore_5d_v150_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_zscore_5d_v150_signal

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
