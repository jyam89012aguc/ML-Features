import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_252d_base_v076_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_252d_base_v076_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_252d_base_v076_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_15d_base_v077_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_15d_base_v077_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_15d_base_v077_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_30d_base_v078_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_30d_base_v078_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_30d_base_v078_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_90d_base_v079_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_90d_base_v079_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_90d_base_v079_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_150d_base_v080_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_150d_base_v080_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_150d_base_v080_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_200d_base_v081_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_200d_base_v081_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_200d_base_v081_signal

def f71rs_f71_revenue_per_share_acceleration_rps_closeadj_300d_base_v082_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / closeadj).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_closeadj_300d_base_v082_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_closeadj_300d_base_v082_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_5d_base_v083_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_5d_base_v083_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_5d_base_v083_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_10d_base_v084_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_10d_base_v084_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_10d_base_v084_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_21d_base_v085_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_21d_base_v085_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_21d_base_v085_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_42d_base_v086_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_42d_base_v086_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_42d_base_v086_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_63d_base_v087_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_63d_base_v087_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_63d_base_v087_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_126d_base_v088_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_126d_base_v088_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_126d_base_v088_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_252d_base_v089_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_252d_base_v089_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_252d_base_v089_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_15d_base_v090_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_15d_base_v090_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_15d_base_v090_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_30d_base_v091_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_30d_base_v091_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_30d_base_v091_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_90d_base_v092_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_90d_base_v092_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_90d_base_v092_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_150d_base_v093_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_150d_base_v093_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_150d_base_v093_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_200d_base_v094_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_200d_base_v094_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_200d_base_v094_signal

def f71rs_f71_revenue_per_share_acceleration_rps_assets_300d_base_v095_signal(revenue, sharesbas, assets):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = (rps / assets).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_assets_300d_base_v095_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_assets_300d_base_v095_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_5d_base_v096_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_5d_base_v096_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_5d_base_v096_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_10d_base_v097_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_10d_base_v097_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_10d_base_v097_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_21d_base_v098_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_21d_base_v098_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_21d_base_v098_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_42d_base_v099_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_42d_base_v099_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_42d_base_v099_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_63d_base_v100_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_63d_base_v100_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_63d_base_v100_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_126d_base_v101_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_126d_base_v101_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_126d_base_v101_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_252d_base_v102_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_252d_base_v102_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_252d_base_v102_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_15d_base_v103_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_15d_base_v103_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_15d_base_v103_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_30d_base_v104_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_30d_base_v104_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_30d_base_v104_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_90d_base_v105_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(90).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_90d_base_v105_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_90d_base_v105_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_150d_base_v106_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_150d_base_v106_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_150d_base_v106_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_200d_base_v107_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_200d_base_v107_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_200d_base_v107_signal

def f71rs_f71_revenue_per_share_acceleration_log_rps_300d_base_v108_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = np.log(rps).rolling(300).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_log_rps_300d_base_v108_signal'] = f71rs_f71_revenue_per_share_acceleration_log_rps_300d_base_v108_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_5d_base_v109_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).rank(pct=True).diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_5d_base_v109_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_5d_base_v109_signal

def f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_21d_base_v110_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).rank(pct=True).diff()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_21d_base_v110_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_rank_diff_21d_base_v110_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_5d_base_v111_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_5d_base_v111_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_5d_base_v111_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_rank_10d_base_v112_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_rank_10d_base_v112_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_rank_10d_base_v112_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_5d_base_v113_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).std() / accel.rolling(5).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_5d_base_v113_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_5d_base_v113_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_10d_base_v114_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).std() / accel.rolling(10).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_10d_base_v114_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_10d_base_v114_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_21d_base_v115_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).std() / accel.rolling(21).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_21d_base_v115_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_21d_base_v115_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_42d_base_v116_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).std() / accel.rolling(42).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_42d_base_v116_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_42d_base_v116_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_63d_base_v117_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).std() / accel.rolling(63).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_63d_base_v117_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_63d_base_v117_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_126d_base_v118_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).std() / accel.rolling(126).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_126d_base_v118_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_126d_base_v118_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_252d_base_v119_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).std() / accel.rolling(252).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_252d_base_v119_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_252d_base_v119_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_15d_base_v120_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).std() / accel.rolling(15).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_15d_base_v120_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_15d_base_v120_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_30d_base_v121_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).std() / accel.rolling(30).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_30d_base_v121_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_30d_base_v121_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_90d_base_v122_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).std() / accel.rolling(90).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_90d_base_v122_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_90d_base_v122_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_150d_base_v123_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).std() / accel.rolling(150).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_150d_base_v123_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_150d_base_v123_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_200d_base_v124_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).std() / accel.rolling(200).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_200d_base_v124_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_200d_base_v124_signal

def f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_300d_base_v125_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).std() / accel.rolling(300).mean().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_300d_base_v125_signal'] = f71rs_f71_revenue_per_share_acceleration_rps_vol_accel_300d_base_v125_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_5d_base_v126_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_5d_base_v126_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_5d_base_v126_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_10d_base_v127_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_10d_base_v127_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_10d_base_v127_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_21d_base_v128_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_21d_base_v128_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_21d_base_v128_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_42d_base_v129_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_42d_base_v129_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_42d_base_v129_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_63d_base_v130_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_63d_base_v130_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_63d_base_v130_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_126d_base_v131_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_126d_base_v131_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_126d_base_v131_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_252d_base_v132_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_252d_base_v132_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_252d_base_v132_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_15d_base_v133_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(15).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_15d_base_v133_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_15d_base_v133_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_30d_base_v134_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_30d_base_v134_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_30d_base_v134_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_90d_base_v135_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_90d_base_v135_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_90d_base_v135_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_150d_base_v136_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(150).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_150d_base_v136_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_150d_base_v136_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_200d_base_v137_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(200).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_200d_base_v137_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_200d_base_v137_signal

def f71rs_f71_revenue_per_share_acceleration_accel_skew_300d_base_v138_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel.rolling(300).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel_skew_300d_base_v138_signal'] = f71rs_f71_revenue_per_share_acceleration_accel_skew_300d_base_v138_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_5d_base_v139_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(5).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_5d_base_v139_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_5d_base_v139_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_10d_base_v140_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(10).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_10d_base_v140_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_10d_base_v140_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_21d_base_v141_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_21d_base_v141_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_21d_base_v141_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_42d_base_v142_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_42d_base_v142_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_42d_base_v142_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_63d_base_v143_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_63d_base_v143_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_63d_base_v143_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_126d_base_v144_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_126d_base_v144_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_126d_base_v144_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_252d_base_v145_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_252d_base_v145_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_252d_base_v145_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_15d_base_v146_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(15).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_15d_base_v146_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_15d_base_v146_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_30d_base_v147_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_30d_base_v147_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_30d_base_v147_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_90d_base_v148_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_90d_base_v148_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_90d_base_v148_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_150d_base_v149_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(150).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_150d_base_v149_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_150d_base_v149_signal

def f71rs_f71_revenue_per_share_acceleration_accel2_skew_200d_base_v150_signal(revenue, sharesbas):
    rps = revenue / sharesbas
    accel = rps.pct_change()
    accel2 = accel.diff()
    res = accel2.rolling(200).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f71rs_f71_revenue_per_share_acceleration_accel2_skew_200d_base_v150_signal'] = f71rs_f71_revenue_per_share_acceleration_accel2_skew_200d_base_v150_signal

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
