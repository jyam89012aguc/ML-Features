# f07_price_moving_averages_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _ma_sma(c, w):
    return c.rolling(w, min_periods=1).mean()

def _ma_ema(c, w):
    return c.ewm(span=w, adjust=False).mean()

# f07_price_moving_averages_high_ema_rel_5d
def f07_price_moving_averages_high_ema_rel_5d_base_v076_signal(arg_high, arg_close):
    res = _ma_ema(arg_high, 5) / _ma_ema(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_bb_pct_5d
def f07_price_moving_averages_high_bb_pct_5d_base_v077_signal(arg_high):
    res = (arg_high - (_ma_sma(arg_high, 5) - 2 * arg_high.rolling(5).std())) / (4 * arg_high.rolling(5).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_zscore_5d
def f07_price_moving_averages_high_zscore_5d_base_v078_signal(arg_high):
    res = (arg_high - _ma_sma(arg_high, 5)) / arg_high.rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_dist_max_5d
def f07_price_moving_averages_high_sma_dist_max_5d_base_v079_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 5).rolling(25).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_high_sma_dist_min_5d
def f07_price_moving_averages_high_sma_dist_min_5d_base_v080_signal(arg_high):
    res = arg_high / _ma_sma(arg_high, 5).rolling(25).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_5d
def f07_price_moving_averages_low_sma_5d_base_v081_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_ema_5d
def f07_price_moving_averages_low_ema_5d_base_v082_signal(arg_low):
    res = arg_low / _ma_ema(arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_rel_5d
def f07_price_moving_averages_low_sma_rel_5d_base_v083_signal(arg_low, arg_close):
    res = _ma_sma(arg_low, 5) / _ma_sma(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_ema_rel_5d
def f07_price_moving_averages_low_ema_rel_5d_base_v084_signal(arg_low, arg_close):
    res = _ma_ema(arg_low, 5) / _ma_ema(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_bb_pct_5d
def f07_price_moving_averages_low_bb_pct_5d_base_v085_signal(arg_low):
    res = (arg_low - (_ma_sma(arg_low, 5) - 2 * arg_low.rolling(5).std())) / (4 * arg_low.rolling(5).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_zscore_5d
def f07_price_moving_averages_low_zscore_5d_base_v086_signal(arg_low):
    res = (arg_low - _ma_sma(arg_low, 5)) / arg_low.rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_dist_max_5d
def f07_price_moving_averages_low_sma_dist_max_5d_base_v087_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 5).rolling(25).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_low_sma_dist_min_5d
def f07_price_moving_averages_low_sma_dist_min_5d_base_v088_signal(arg_low):
    res = arg_low / _ma_sma(arg_low, 5).rolling(25).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_5d
def f07_price_moving_averages_close_sma_5d_base_v089_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_5d
def f07_price_moving_averages_close_ema_5d_base_v090_signal(arg_close):
    res = arg_close / _ma_ema(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_rel_5d
def f07_price_moving_averages_close_sma_rel_5d_base_v091_signal(arg_close):
    res = _ma_sma(arg_close, 5) / _ma_sma(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_rel_5d
def f07_price_moving_averages_close_ema_rel_5d_base_v092_signal(arg_close):
    res = _ma_ema(arg_close, 5) / _ma_ema(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_bb_pct_5d
def f07_price_moving_averages_close_bb_pct_5d_base_v093_signal(arg_close):
    res = (arg_close - (_ma_sma(arg_close, 5) - 2 * arg_close.rolling(5).std())) / (4 * arg_close.rolling(5).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_zscore_5d
def f07_price_moving_averages_close_zscore_5d_base_v094_signal(arg_close):
    res = (arg_close - _ma_sma(arg_close, 5)) / arg_close.rolling(5).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_max_5d
def f07_price_moving_averages_close_sma_dist_max_5d_base_v095_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 5).rolling(25).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_min_5d
def f07_price_moving_averages_close_sma_dist_min_5d_base_v096_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 5).rolling(25).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_10d
def f07_price_moving_averages_close_sma_10d_base_v097_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_10d
def f07_price_moving_averages_close_ema_10d_base_v098_signal(arg_close):
    res = arg_close / _ma_ema(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_rel_10d
def f07_price_moving_averages_close_sma_rel_10d_base_v099_signal(arg_close, arg_closeadj):
    res = _ma_sma(arg_close, 10) / _ma_sma(arg_closeadj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_rel_10d
def f07_price_moving_averages_close_ema_rel_10d_base_v100_signal(arg_close, arg_closeadj):
    res = _ma_ema(arg_close, 10) / _ma_ema(arg_closeadj, 30)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_bb_pct_10d
def f07_price_moving_averages_close_bb_pct_10d_base_v101_signal(arg_close):
    res = (arg_close - (_ma_sma(arg_close, 10) - 2 * arg_close.rolling(10).std())) / (4 * arg_close.rolling(10).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_zscore_10d
def f07_price_moving_averages_close_zscore_10d_base_v102_signal(arg_close):
    res = (arg_close - _ma_sma(arg_close, 10)) / arg_close.rolling(10).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_max_10d
def f07_price_moving_averages_close_sma_dist_max_10d_base_v103_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 10).rolling(50).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_min_10d
def f07_price_moving_averages_close_sma_dist_min_10d_base_v104_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 10).rolling(50).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_15d
def f07_price_moving_averages_close_sma_15d_base_v105_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_15d
def f07_price_moving_averages_close_ema_15d_base_v106_signal(arg_close):
    res = arg_close / _ma_ema(arg_close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_rel_15d
def f07_price_moving_averages_close_sma_rel_15d_base_v107_signal(arg_close, arg_closeadj):
    res = _ma_sma(arg_close, 15) / _ma_sma(arg_closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_rel_15d
def f07_price_moving_averages_close_ema_rel_15d_base_v108_signal(arg_close, arg_closeadj):
    res = _ma_ema(arg_close, 15) / _ma_ema(arg_closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_bb_pct_15d
def f07_price_moving_averages_close_bb_pct_15d_base_v109_signal(arg_close):
    res = (arg_close - (_ma_sma(arg_close, 15) - 2 * arg_close.rolling(15).std())) / (4 * arg_close.rolling(15).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_zscore_15d
def f07_price_moving_averages_close_zscore_15d_base_v110_signal(arg_close):
    res = (arg_close - _ma_sma(arg_close, 15)) / arg_close.rolling(15).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_max_15d
def f07_price_moving_averages_close_sma_dist_max_15d_base_v111_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 15).rolling(75).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_min_15d
def f07_price_moving_averages_close_sma_dist_min_15d_base_v112_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 15).rolling(75).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_21d
def f07_price_moving_averages_close_sma_21d_base_v113_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_21d
def f07_price_moving_averages_close_ema_21d_base_v114_signal(arg_close):
    res = arg_close / _ma_ema(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_rel_21d
def f07_price_moving_averages_close_sma_rel_21d_base_v115_signal(arg_close, arg_closeadj):
    res = _ma_sma(arg_close, 21) / _ma_sma(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_ema_rel_21d
def f07_price_moving_averages_close_ema_rel_21d_base_v116_signal(arg_close, arg_closeadj):
    res = _ma_ema(arg_close, 21) / _ma_ema(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_bb_pct_21d
def f07_price_moving_averages_close_bb_pct_21d_base_v117_signal(arg_close):
    res = (arg_close - (_ma_sma(arg_close, 21) - 2 * arg_close.rolling(21).std())) / (4 * arg_close.rolling(21).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_zscore_21d
def f07_price_moving_averages_close_zscore_21d_base_v118_signal(arg_close):
    res = (arg_close - _ma_sma(arg_close, 21)) / arg_close.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_max_21d
def f07_price_moving_averages_close_sma_dist_max_21d_base_v119_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 21).rolling(105).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_close_sma_dist_min_21d
def f07_price_moving_averages_close_sma_dist_min_21d_base_v120_signal(arg_close):
    res = arg_close / _ma_sma(arg_close, 21).rolling(105).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_42d
def f07_price_moving_averages_closeadj_sma_42d_base_v121_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_42d
def f07_price_moving_averages_closeadj_ema_42d_base_v122_signal(arg_closeadj):
    res = arg_closeadj / _ma_ema(arg_closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_rel_42d
def f07_price_moving_averages_closeadj_sma_rel_42d_base_v123_signal(arg_closeadj):
    res = _ma_sma(arg_closeadj, 42) / _ma_sma(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_rel_42d
def f07_price_moving_averages_closeadj_ema_rel_42d_base_v124_signal(arg_closeadj):
    res = _ma_ema(arg_closeadj, 42) / _ma_ema(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_bb_pct_42d
def f07_price_moving_averages_closeadj_bb_pct_42d_base_v125_signal(arg_closeadj):
    res = (arg_closeadj - (_ma_sma(arg_closeadj, 42) - 2 * arg_closeadj.rolling(42).std())) / (4 * arg_closeadj.rolling(42).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_zscore_42d
def f07_price_moving_averages_closeadj_zscore_42d_base_v126_signal(arg_closeadj):
    res = (arg_closeadj - _ma_sma(arg_closeadj, 42)) / arg_closeadj.rolling(42).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_dist_max_42d
def f07_price_moving_averages_closeadj_sma_dist_max_42d_base_v127_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 42).rolling(210).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_dist_min_42d
def f07_price_moving_averages_closeadj_sma_dist_min_42d_base_v128_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 42).rolling(210).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_63d
def f07_price_moving_averages_closeadj_sma_63d_base_v129_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_63d
def f07_price_moving_averages_closeadj_ema_63d_base_v130_signal(arg_closeadj):
    res = arg_closeadj / _ma_ema(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_rel_63d
def f07_price_moving_averages_closeadj_sma_rel_63d_base_v131_signal(arg_closeadj):
    res = _ma_sma(arg_closeadj, 63) / _ma_sma(arg_closeadj, 189)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_rel_63d
def f07_price_moving_averages_closeadj_ema_rel_63d_base_v132_signal(arg_closeadj):
    res = _ma_ema(arg_closeadj, 63) / _ma_ema(arg_closeadj, 189)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_bb_pct_63d
def f07_price_moving_averages_closeadj_bb_pct_63d_base_v133_signal(arg_closeadj):
    res = (arg_closeadj - (_ma_sma(arg_closeadj, 63) - 2 * arg_closeadj.rolling(63).std())) / (4 * arg_closeadj.rolling(63).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_zscore_63d
def f07_price_moving_averages_closeadj_zscore_63d_base_v134_signal(arg_closeadj):
    res = (arg_closeadj - _ma_sma(arg_closeadj, 63)) / arg_closeadj.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_dist_max_63d
def f07_price_moving_averages_closeadj_sma_dist_max_63d_base_v135_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 63).rolling(315).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_dist_min_63d
def f07_price_moving_averages_closeadj_sma_dist_min_63d_base_v136_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 63).rolling(315).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_126d
def f07_price_moving_averages_closeadj_sma_126d_base_v137_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_126d
def f07_price_moving_averages_closeadj_ema_126d_base_v138_signal(arg_closeadj):
    res = arg_closeadj / _ma_ema(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_rel_126d
def f07_price_moving_averages_closeadj_sma_rel_126d_base_v139_signal(arg_closeadj):
    res = _ma_sma(arg_closeadj, 126) / _ma_sma(arg_closeadj, 378)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_rel_126d
def f07_price_moving_averages_closeadj_ema_rel_126d_base_v140_signal(arg_closeadj):
    res = _ma_ema(arg_closeadj, 126) / _ma_ema(arg_closeadj, 378)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_bb_pct_126d
def f07_price_moving_averages_closeadj_bb_pct_126d_base_v141_signal(arg_closeadj):
    res = (arg_closeadj - (_ma_sma(arg_closeadj, 126) - 2 * arg_closeadj.rolling(126).std())) / (4 * arg_closeadj.rolling(126).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_zscore_126d
def f07_price_moving_averages_closeadj_zscore_126d_base_v142_signal(arg_closeadj):
    res = (arg_closeadj - _ma_sma(arg_closeadj, 126)) / arg_closeadj.rolling(126).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_dist_max_126d
def f07_price_moving_averages_closeadj_sma_dist_max_126d_base_v143_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 126).rolling(630).max().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_dist_min_126d
def f07_price_moving_averages_closeadj_sma_dist_min_126d_base_v144_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 126).rolling(630).min().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_252d
def f07_price_moving_averages_closeadj_sma_252d_base_v145_signal(arg_closeadj):
    res = arg_closeadj / _ma_sma(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_252d
def f07_price_moving_averages_closeadj_ema_252d_base_v146_signal(arg_closeadj):
    res = arg_closeadj / _ma_ema(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_sma_rel_252d
def f07_price_moving_averages_closeadj_sma_rel_252d_base_v147_signal(arg_closeadj):
    res = _ma_sma(arg_closeadj, 252) / _ma_sma(arg_closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_ema_rel_252d
def f07_price_moving_averages_closeadj_ema_rel_252d_base_v148_signal(arg_closeadj):
    res = _ma_ema(arg_closeadj, 252) / _ma_ema(arg_closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_bb_pct_252d
def f07_price_moving_averages_closeadj_bb_pct_252d_base_v149_signal(arg_closeadj):
    res = (arg_closeadj - (_ma_sma(arg_closeadj, 252) - 2 * arg_closeadj.rolling(252).std())) / (4 * arg_closeadj.rolling(252).std().replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

# f07_price_moving_averages_closeadj_zscore_252d
def f07_price_moving_averages_closeadj_zscore_252d_base_v150_signal(arg_closeadj):
    res = (arg_closeadj - _ma_sma(arg_closeadj, 252)) / arg_closeadj.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    'f07_price_moving_averages_high_ema_rel_5d_base_v076_signal': {'inputs': ['high', 'close'], 'func': f07_price_moving_averages_high_ema_rel_5d_base_v076_signal},
    'f07_price_moving_averages_high_bb_pct_5d_base_v077_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_bb_pct_5d_base_v077_signal},
    'f07_price_moving_averages_high_zscore_5d_base_v078_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_zscore_5d_base_v078_signal},
    'f07_price_moving_averages_high_sma_dist_max_5d_base_v079_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_max_5d_base_v079_signal},
    'f07_price_moving_averages_high_sma_dist_min_5d_base_v080_signal': {'inputs': ['high'], 'func': f07_price_moving_averages_high_sma_dist_min_5d_base_v080_signal},
    'f07_price_moving_averages_low_sma_5d_base_v081_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_5d_base_v081_signal},
    'f07_price_moving_averages_low_ema_5d_base_v082_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_ema_5d_base_v082_signal},
    'f07_price_moving_averages_low_sma_rel_5d_base_v083_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_sma_rel_5d_base_v083_signal},
    'f07_price_moving_averages_low_ema_rel_5d_base_v084_signal': {'inputs': ['low', 'close'], 'func': f07_price_moving_averages_low_ema_rel_5d_base_v084_signal},
    'f07_price_moving_averages_low_bb_pct_5d_base_v085_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_bb_pct_5d_base_v085_signal},
    'f07_price_moving_averages_low_zscore_5d_base_v086_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_zscore_5d_base_v086_signal},
    'f07_price_moving_averages_low_sma_dist_max_5d_base_v087_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_max_5d_base_v087_signal},
    'f07_price_moving_averages_low_sma_dist_min_5d_base_v088_signal': {'inputs': ['low'], 'func': f07_price_moving_averages_low_sma_dist_min_5d_base_v088_signal},
    'f07_price_moving_averages_close_sma_5d_base_v089_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_5d_base_v089_signal},
    'f07_price_moving_averages_close_ema_5d_base_v090_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_5d_base_v090_signal},
    'f07_price_moving_averages_close_sma_rel_5d_base_v091_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_rel_5d_base_v091_signal},
    'f07_price_moving_averages_close_ema_rel_5d_base_v092_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_rel_5d_base_v092_signal},
    'f07_price_moving_averages_close_bb_pct_5d_base_v093_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_5d_base_v093_signal},
    'f07_price_moving_averages_close_zscore_5d_base_v094_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_5d_base_v094_signal},
    'f07_price_moving_averages_close_sma_dist_max_5d_base_v095_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_5d_base_v095_signal},
    'f07_price_moving_averages_close_sma_dist_min_5d_base_v096_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_5d_base_v096_signal},
    'f07_price_moving_averages_close_sma_10d_base_v097_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_10d_base_v097_signal},
    'f07_price_moving_averages_close_ema_10d_base_v098_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_10d_base_v098_signal},
    'f07_price_moving_averages_close_sma_rel_10d_base_v099_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_sma_rel_10d_base_v099_signal},
    'f07_price_moving_averages_close_ema_rel_10d_base_v100_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_ema_rel_10d_base_v100_signal},
    'f07_price_moving_averages_close_bb_pct_10d_base_v101_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_10d_base_v101_signal},
    'f07_price_moving_averages_close_zscore_10d_base_v102_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_10d_base_v102_signal},
    'f07_price_moving_averages_close_sma_dist_max_10d_base_v103_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_10d_base_v103_signal},
    'f07_price_moving_averages_close_sma_dist_min_10d_base_v104_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_10d_base_v104_signal},
    'f07_price_moving_averages_close_sma_15d_base_v105_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_15d_base_v105_signal},
    'f07_price_moving_averages_close_ema_15d_base_v106_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_15d_base_v106_signal},
    'f07_price_moving_averages_close_sma_rel_15d_base_v107_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_sma_rel_15d_base_v107_signal},
    'f07_price_moving_averages_close_ema_rel_15d_base_v108_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_ema_rel_15d_base_v108_signal},
    'f07_price_moving_averages_close_bb_pct_15d_base_v109_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_15d_base_v109_signal},
    'f07_price_moving_averages_close_zscore_15d_base_v110_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_15d_base_v110_signal},
    'f07_price_moving_averages_close_sma_dist_max_15d_base_v111_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_15d_base_v111_signal},
    'f07_price_moving_averages_close_sma_dist_min_15d_base_v112_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_15d_base_v112_signal},
    'f07_price_moving_averages_close_sma_21d_base_v113_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_21d_base_v113_signal},
    'f07_price_moving_averages_close_ema_21d_base_v114_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_ema_21d_base_v114_signal},
    'f07_price_moving_averages_close_sma_rel_21d_base_v115_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_sma_rel_21d_base_v115_signal},
    'f07_price_moving_averages_close_ema_rel_21d_base_v116_signal': {'inputs': ['close', 'closeadj'], 'func': f07_price_moving_averages_close_ema_rel_21d_base_v116_signal},
    'f07_price_moving_averages_close_bb_pct_21d_base_v117_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_bb_pct_21d_base_v117_signal},
    'f07_price_moving_averages_close_zscore_21d_base_v118_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_zscore_21d_base_v118_signal},
    'f07_price_moving_averages_close_sma_dist_max_21d_base_v119_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_max_21d_base_v119_signal},
    'f07_price_moving_averages_close_sma_dist_min_21d_base_v120_signal': {'inputs': ['close'], 'func': f07_price_moving_averages_close_sma_dist_min_21d_base_v120_signal},
    'f07_price_moving_averages_closeadj_sma_42d_base_v121_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_42d_base_v121_signal},
    'f07_price_moving_averages_closeadj_ema_42d_base_v122_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_42d_base_v122_signal},
    'f07_price_moving_averages_closeadj_sma_rel_42d_base_v123_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_42d_base_v123_signal},
    'f07_price_moving_averages_closeadj_ema_rel_42d_base_v124_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_42d_base_v124_signal},
    'f07_price_moving_averages_closeadj_bb_pct_42d_base_v125_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_42d_base_v125_signal},
    'f07_price_moving_averages_closeadj_zscore_42d_base_v126_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_42d_base_v126_signal},
    'f07_price_moving_averages_closeadj_sma_dist_max_42d_base_v127_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_max_42d_base_v127_signal},
    'f07_price_moving_averages_closeadj_sma_dist_min_42d_base_v128_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_min_42d_base_v128_signal},
    'f07_price_moving_averages_closeadj_sma_63d_base_v129_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_63d_base_v129_signal},
    'f07_price_moving_averages_closeadj_ema_63d_base_v130_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_63d_base_v130_signal},
    'f07_price_moving_averages_closeadj_sma_rel_63d_base_v131_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_63d_base_v131_signal},
    'f07_price_moving_averages_closeadj_ema_rel_63d_base_v132_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_63d_base_v132_signal},
    'f07_price_moving_averages_closeadj_bb_pct_63d_base_v133_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_63d_base_v133_signal},
    'f07_price_moving_averages_closeadj_zscore_63d_base_v134_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_63d_base_v134_signal},
    'f07_price_moving_averages_closeadj_sma_dist_max_63d_base_v135_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_max_63d_base_v135_signal},
    'f07_price_moving_averages_closeadj_sma_dist_min_63d_base_v136_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_min_63d_base_v136_signal},
    'f07_price_moving_averages_closeadj_sma_126d_base_v137_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_126d_base_v137_signal},
    'f07_price_moving_averages_closeadj_ema_126d_base_v138_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_126d_base_v138_signal},
    'f07_price_moving_averages_closeadj_sma_rel_126d_base_v139_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_126d_base_v139_signal},
    'f07_price_moving_averages_closeadj_ema_rel_126d_base_v140_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_126d_base_v140_signal},
    'f07_price_moving_averages_closeadj_bb_pct_126d_base_v141_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_126d_base_v141_signal},
    'f07_price_moving_averages_closeadj_zscore_126d_base_v142_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_126d_base_v142_signal},
    'f07_price_moving_averages_closeadj_sma_dist_max_126d_base_v143_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_max_126d_base_v143_signal},
    'f07_price_moving_averages_closeadj_sma_dist_min_126d_base_v144_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_dist_min_126d_base_v144_signal},
    'f07_price_moving_averages_closeadj_sma_252d_base_v145_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_252d_base_v145_signal},
    'f07_price_moving_averages_closeadj_ema_252d_base_v146_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_252d_base_v146_signal},
    'f07_price_moving_averages_closeadj_sma_rel_252d_base_v147_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_sma_rel_252d_base_v147_signal},
    'f07_price_moving_averages_closeadj_ema_rel_252d_base_v148_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_ema_rel_252d_base_v148_signal},
    'f07_price_moving_averages_closeadj_bb_pct_252d_base_v149_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_bb_pct_252d_base_v149_signal},
    'f07_price_moving_averages_closeadj_zscore_252d_base_v150_signal': {'inputs': ['closeadj'], 'func': f07_price_moving_averages_closeadj_zscore_252d_base_v150_signal},
}

F07_PRICE_MOVING_AVERAGES_REGISTRY_076_150 = REGISTRY

if __name__ == '__main__':
    n = 1000
    df = pd.DataFrame({k: np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100 for k in ['open', 'high', 'low', 'close', 'closeadj']})
    for name, info in REGISTRY.items():
        inputs = [df[col] for col in info['inputs']]
        y = info['func'](*inputs)
        assert len(y) > 0
        assert y.nunique() > 2
        assert y.std() > 0
    print('Tests passed!')
