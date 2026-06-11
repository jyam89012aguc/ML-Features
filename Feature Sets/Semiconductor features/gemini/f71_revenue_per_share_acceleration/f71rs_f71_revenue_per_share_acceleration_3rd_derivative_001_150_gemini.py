import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_5d_v001_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).mean().pct_change(5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_5d_v001_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_5d_v001_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_10d_v002_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).mean().pct_change(10).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_10d_v002_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_10d_v002_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_21d_v003_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).mean().pct_change(21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_21d_v003_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_21d_v003_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_42d_v004_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).mean().pct_change(42).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_42d_v004_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_42d_v004_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_63d_v005_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).mean().pct_change(63).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_63d_v005_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_63d_v005_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_126d_v006_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).mean().pct_change(126).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_126d_v006_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_126d_v006_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_15d_v007_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).mean().pct_change(15).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_15d_v007_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_15d_v007_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_30d_v008_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).mean().pct_change(30).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_30d_v008_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_30d_v008_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_90d_v009_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).mean().pct_change(90).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_90d_v009_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_90d_v009_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_150d_v010_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).mean().pct_change(150).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_150d_v010_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_150d_v010_signal

def f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_200d_v011_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).mean().pct_change(200).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_200d_v011_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_mean_slope_std_200d_v011_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_5d_v012_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(5).skew().diff(5).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_5d_v012_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_5d_v012_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_10d_v013_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(10).skew().diff(10).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_10d_v013_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_10d_v013_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_21d_v014_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(21).skew().diff(21).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_21d_v014_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_21d_v014_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_42d_v015_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(42).skew().diff(42).rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_42d_v015_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_42d_v015_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_63d_v016_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(63).skew().diff(63).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_63d_v016_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_63d_v016_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_126d_v017_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(126).skew().diff(126).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_126d_v017_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_126d_v017_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_15d_v018_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(15).skew().diff(15).rolling(15).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_15d_v018_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_15d_v018_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_30d_v019_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(30).skew().diff(30).rolling(30).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_30d_v019_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_30d_v019_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_90d_v020_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(90).skew().diff(90).rolling(90).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_90d_v020_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_90d_v020_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_150d_v021_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(150).skew().diff(150).rolling(150).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_150d_v021_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_150d_v021_signal

def f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_200d_v022_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.rolling(200).skew().diff(200).rolling(200).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_200d_v022_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_skew_diff_rank_200d_v022_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_5d_v023_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(5).std()).rolling(5).rank(pct=True).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_5d_v023_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_5d_v023_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_10d_v024_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(10).std()).rolling(10).rank(pct=True).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_10d_v024_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_10d_v024_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_21d_v025_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(21).std()).rolling(21).rank(pct=True).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_21d_v025_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_21d_v025_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_42d_v026_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(42).std()).rolling(42).rank(pct=True).pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_42d_v026_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_42d_v026_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_63d_v027_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(63).std()).rolling(63).rank(pct=True).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_63d_v027_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_63d_v027_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_126d_v028_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(126).std()).rolling(126).rank(pct=True).pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_126d_v028_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_126d_v028_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_15d_v029_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(15).std()).rolling(15).rank(pct=True).pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_15d_v029_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_15d_v029_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_30d_v030_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(30).std()).rolling(30).rank(pct=True).pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_30d_v030_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_30d_v030_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_90d_v031_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(90).std()).rolling(90).rank(pct=True).pct_change(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_90d_v031_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_90d_v031_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_150d_v032_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(150).std()).rolling(150).rank(pct=True).pct_change(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_150d_v032_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_150d_v032_signal

def f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_200d_v033_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (accel / accel.rolling(200).std()).rolling(200).rank(pct=True).pct_change(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_200d_v033_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_to_std_rank_slope_200d_v033_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_5d_v034_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_5d_v034_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_5d_v034_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_10d_v035_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(10).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_10d_v035_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_10d_v035_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_21d_v036_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_21d_v036_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_21d_v036_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_42d_v037_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(42).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_42d_v037_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_42d_v037_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_63d_v038_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(63).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_63d_v038_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_63d_v038_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_126d_v039_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(126).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_126d_v039_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_126d_v039_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_252d_v040_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(252).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_252d_v040_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_252d_v040_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_15d_v041_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(15).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_15d_v041_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_15d_v041_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_30d_v042_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(30).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_30d_v042_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_30d_v042_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_90d_v043_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(90).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_90d_v043_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_90d_v043_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_150d_v044_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(150).rolling(150).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_150d_v044_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_150d_v044_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_200d_v045_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(200).rolling(200).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_200d_v045_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_200d_v045_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_300d_v046_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).pct_change(300).rolling(300).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_300d_v046_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_accel_std_300d_v046_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_5d_v047_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(5).std() / np.log(rps).rolling(5).mean()).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_5d_v047_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_5d_v047_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_10d_v048_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(10).std() / np.log(rps).rolling(10).mean()).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_10d_v048_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_10d_v048_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_21d_v049_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(21).std() / np.log(rps).rolling(21).mean()).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_21d_v049_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_21d_v049_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_42d_v050_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(42).std() / np.log(rps).rolling(42).mean()).rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_42d_v050_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_42d_v050_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_63d_v051_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(63).std() / np.log(rps).rolling(63).mean()).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_63d_v051_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_63d_v051_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_126d_v052_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(126).std() / np.log(rps).rolling(126).mean()).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_126d_v052_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_126d_v052_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_252d_v053_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(252).std() / np.log(rps).rolling(252).mean()).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_252d_v053_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_252d_v053_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_15d_v054_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(15).std() / np.log(rps).rolling(15).mean()).rolling(15).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_15d_v054_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_15d_v054_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_30d_v055_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(30).std() / np.log(rps).rolling(30).mean()).rolling(30).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_30d_v055_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_30d_v055_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_90d_v056_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(90).std() / np.log(rps).rolling(90).mean()).rolling(90).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_90d_v056_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_90d_v056_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_150d_v057_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(150).std() / np.log(rps).rolling(150).mean()).rolling(150).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_150d_v057_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_150d_v057_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_200d_v058_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(200).std() / np.log(rps).rolling(200).mean()).rolling(200).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_200d_v058_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_200d_v058_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_300d_v059_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (np.log(rps).rolling(300).std() / np.log(rps).rolling(300).mean()).rolling(300).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_300d_v059_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_vol_rank_300d_v059_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_5d_v060_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(5).rank(pct=True).rolling(5).mean().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_5d_v060_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_5d_v060_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_10d_v061_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(10).rank(pct=True).rolling(10).mean().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_10d_v061_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_10d_v061_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_21d_v062_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(21).rank(pct=True).rolling(21).mean().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_21d_v062_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_21d_v062_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_42d_v063_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(42).rank(pct=True).rolling(42).mean().pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_42d_v063_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_42d_v063_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_63d_v064_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(63).rank(pct=True).rolling(63).mean().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_63d_v064_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_63d_v064_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_126d_v065_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(126).rank(pct=True).rolling(126).mean().pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_126d_v065_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_126d_v065_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_15d_v066_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(15).rank(pct=True).rolling(15).mean().pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_15d_v066_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_15d_v066_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_30d_v067_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(30).rank(pct=True).rolling(30).mean().pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_30d_v067_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_30d_v067_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_90d_v068_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(90).rank(pct=True).rolling(90).mean().pct_change(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_90d_v068_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_90d_v068_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_150d_v069_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(150).rank(pct=True).rolling(150).mean().pct_change(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_150d_v069_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_150d_v069_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_200d_v070_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(200).rank(pct=True).rolling(200).mean().pct_change(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_200d_v070_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_mean_slope_200d_v070_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_5d_v071_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).skew().rolling(5).rank(pct=True).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_5d_v071_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_5d_v071_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_10d_v072_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).skew().rolling(10).rank(pct=True).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_10d_v072_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_10d_v072_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_21d_v073_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).skew().rolling(21).rank(pct=True).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_21d_v073_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_21d_v073_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_42d_v074_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).skew().rolling(42).rank(pct=True).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_42d_v074_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_42d_v074_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_63d_v075_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).skew().rolling(63).rank(pct=True).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_63d_v075_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_63d_v075_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_126d_v076_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).skew().rolling(126).rank(pct=True).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_126d_v076_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_126d_v076_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_15d_v077_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).skew().rolling(15).rank(pct=True).diff(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_15d_v077_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_15d_v077_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_30d_v078_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).skew().rolling(30).rank(pct=True).diff(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_30d_v078_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_30d_v078_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_90d_v079_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).skew().rolling(90).rank(pct=True).diff(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_90d_v079_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_90d_v079_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_150d_v080_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).skew().rolling(150).rank(pct=True).diff(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_150d_v080_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_150d_v080_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_200d_v081_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).skew().rolling(200).rank(pct=True).diff(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_200d_v081_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_rank_diff_200d_v081_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_5d_v082_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_5d_v082_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_5d_v082_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_10d_v083_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_10d_v083_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_10d_v083_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_21d_v084_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(21).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_21d_v084_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_21d_v084_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_42d_v085_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(42).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_42d_v085_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_42d_v085_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_63d_v086_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(63).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_63d_v086_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_63d_v086_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_126d_v087_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(126).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_126d_v087_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_126d_v087_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_252d_v088_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(252).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_252d_v088_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_252d_v088_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_15d_v089_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(15).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_15d_v089_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_15d_v089_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_30d_v090_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(30).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_30d_v090_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_30d_v090_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_90d_v091_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(90).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_90d_v091_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_90d_v091_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_150d_v092_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(150).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_150d_v092_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_150d_v092_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_200d_v093_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(200).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_200d_v093_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_200d_v093_signal

def f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_300d_v094_signal(revenue, sharesbas, ebitda):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / ebitda).pct_change(300).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_300d_v094_signal'] = f71rs_f71_revenue_per_share_acceleration_ebitda_rps_ratio_accel_300d_v094_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_5d_v095_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(5).diff(5).rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_5d_v095_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_5d_v095_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_10d_v096_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(10).diff(10).rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_10d_v096_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_10d_v096_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_21d_v097_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(21).diff(21).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_21d_v097_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_21d_v097_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_42d_v098_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(42).diff(42).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_42d_v098_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_42d_v098_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_63d_v099_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(63).diff(63).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_63d_v099_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_63d_v099_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_126d_v100_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(126).diff(126).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_126d_v100_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_126d_v100_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_15d_v101_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(15).diff(15).rolling(15).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_15d_v101_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_15d_v101_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_30d_v102_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(30).diff(30).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_30d_v102_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_30d_v102_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_90d_v103_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(90).diff(90).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_90d_v103_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_90d_v103_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_150d_v104_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(150).diff(150).rolling(150).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_150d_v104_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_150d_v104_signal

def f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_200d_v105_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = rps.pct_change(200).diff(200).rolling(200).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_200d_v105_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_complex_triple_200d_v105_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_5d_v106_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(5).rolling(5).std().pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_5d_v106_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_5d_v106_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_10d_v107_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(10).rolling(10).std().pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_10d_v107_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_10d_v107_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_21d_v108_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(21).rolling(21).std().pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_21d_v108_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_21d_v108_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_42d_v109_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(42).rolling(42).std().pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_42d_v109_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_42d_v109_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_63d_v110_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(63).rolling(63).std().pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_63d_v110_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_63d_v110_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_126d_v111_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(126).rolling(126).std().pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_126d_v111_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_126d_v111_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_15d_v112_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(15).rolling(15).std().pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_15d_v112_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_15d_v112_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_30d_v113_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(30).rolling(30).std().pct_change(30)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_30d_v113_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_30d_v113_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_90d_v114_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(90).rolling(90).std().pct_change(90)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_90d_v114_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_90d_v114_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_150d_v115_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(150).rolling(150).std().pct_change(150)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_150d_v115_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_150d_v115_signal

def f71rs_f71_revenue_per_share_acceleration_accel_triple_std_200d_v116_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.diff(200).rolling(200).std().pct_change(200)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_triple_std_200d_v116_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_triple_std_200d_v116_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_5d_v117_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(5).rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_5d_v117_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_5d_v117_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_10d_v118_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(10).rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_10d_v118_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_10d_v118_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_21d_v119_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(21).rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_21d_v119_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_21d_v119_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_42d_v120_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(42).rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_42d_v120_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_42d_v120_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_63d_v121_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(63).rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_63d_v121_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_63d_v121_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_126d_v122_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(126).rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_126d_v122_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_126d_v122_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_252d_v123_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(252).rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_252d_v123_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_252d_v123_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_15d_v124_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(15).rolling(15).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_15d_v124_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_15d_v124_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_30d_v125_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(30).rolling(30).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_30d_v125_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_30d_v125_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_90d_v126_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(90).rolling(90).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_90d_v126_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_90d_v126_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_150d_v127_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(150).rolling(150).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_150d_v127_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_150d_v127_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_200d_v128_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(200).rolling(200).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_200d_v128_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_200d_v128_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_300d_v129_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).pct_change(300).rolling(300).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_300d_v129_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_accel_rank_300d_v129_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_5d_v130_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(5).mean()) / accel2.rolling(5).std()).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_5d_v130_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_5d_v130_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_10d_v131_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(10).mean()) / accel2.rolling(10).std()).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_10d_v131_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_10d_v131_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_21d_v132_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(21).mean()) / accel2.rolling(21).std()).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_21d_v132_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_21d_v132_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_42d_v133_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(42).mean()) / accel2.rolling(42).std()).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_42d_v133_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_42d_v133_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_63d_v134_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(63).mean()) / accel2.rolling(63).std()).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_63d_v134_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_63d_v134_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_126d_v135_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(126).mean()) / accel2.rolling(126).std()).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_126d_v135_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_126d_v135_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_252d_v136_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(252).mean()) / accel2.rolling(252).std()).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_252d_v136_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_252d_v136_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_15d_v137_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(15).mean()) / accel2.rolling(15).std()).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_15d_v137_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_15d_v137_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_30d_v138_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(30).mean()) / accel2.rolling(30).std()).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_30d_v138_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_30d_v138_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_90d_v139_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(90).mean()) / accel2.rolling(90).std()).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_90d_v139_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_90d_v139_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_150d_v140_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(150).mean()) / accel2.rolling(150).std()).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_150d_v140_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_150d_v140_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_200d_v141_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(200).mean()) / accel2.rolling(200).std()).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_200d_v141_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_200d_v141_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_300d_v142_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = ((accel2 - accel2.rolling(300).mean()) / accel2.rolling(300).std()).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_300d_v142_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_zscore_mean_300d_v142_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_5d_v143_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_5d_v143_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_5d_v143_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_10d_v144_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(10).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_10d_v144_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_10d_v144_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_21d_v145_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_21d_v145_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_21d_v145_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_42d_v146_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(42).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_42d_v146_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_42d_v146_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_63d_v147_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(63).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_63d_v147_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_63d_v147_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_126d_v148_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(126).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_126d_v148_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_126d_v148_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_252d_v149_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(252).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_252d_v149_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_252d_v149_signal

def f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_15d_v150_signal(revenue, sharesbas, debt):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / debt).pct_change(15).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_15d_v150_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_debt_accel_std_15d_v150_signal

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
