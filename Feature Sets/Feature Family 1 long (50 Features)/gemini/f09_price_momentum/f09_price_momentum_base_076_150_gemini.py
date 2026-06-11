# f09_price_momentum_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _z(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=min(w, 5)).max()

def _mom_roc(c, w):
    return (c / c.shift(w).replace(0, np.nan) - 1)

def _mom_rsi(c, w):
    delta = c.diff()
    gain = (delta.where(delta > 0, 0)).rolling(w, min_periods=1).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(w, min_periods=1).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs.replace(np.nan, 0)))

# STD of 10d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_std_10d_base_v076_signal(arg_close):
    res = _std(_mom_roc(arg_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 10d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_z_10d_base_v077_signal(arg_close):
    res = _z(_mom_roc(arg_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 10d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_sma_10d_base_v078_signal(arg_close):
    res = _sma(_mom_rsi(arg_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 10d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_std_10d_base_v079_signal(arg_close):
    res = _std(_mom_rsi(arg_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 10d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_z_10d_base_v080_signal(arg_close):
    res = _z(_mom_rsi(arg_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 14d window of close in price_momentum domain
def f09_price_momentum_close_roc_14d_base_v081_signal(arg_close):
    res = _mom_roc(arg_close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 14d window of close in price_momentum domain
def f09_price_momentum_close_rsi_14d_base_v082_signal(arg_close):
    res = _mom_rsi(arg_close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 14d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_sma_14d_base_v083_signal(arg_close):
    res = _sma(_mom_roc(arg_close, 14), 14)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 14d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_std_14d_base_v084_signal(arg_close):
    res = _std(_mom_roc(arg_close, 14), 14)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 14d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_z_14d_base_v085_signal(arg_close):
    res = _z(_mom_roc(arg_close, 14), 14)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 14d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_sma_14d_base_v086_signal(arg_close):
    res = _sma(_mom_rsi(arg_close, 14), 14)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 14d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_std_14d_base_v087_signal(arg_close):
    res = _std(_mom_rsi(arg_close, 14), 14)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 14d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_z_14d_base_v088_signal(arg_close):
    res = _z(_mom_rsi(arg_close, 14), 14)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 21d window of close in price_momentum domain
def f09_price_momentum_close_roc_21d_base_v089_signal(arg_close):
    res = _mom_roc(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 21d window of close in price_momentum domain
def f09_price_momentum_close_rsi_21d_base_v090_signal(arg_close):
    res = _mom_rsi(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 21d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_sma_21d_base_v091_signal(arg_close):
    res = _sma(_mom_roc(arg_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 21d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_std_21d_base_v092_signal(arg_close):
    res = _std(_mom_roc(arg_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 21d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_z_21d_base_v093_signal(arg_close):
    res = _z(_mom_roc(arg_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 21d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_sma_21d_base_v094_signal(arg_close):
    res = _sma(_mom_rsi(arg_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 21d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_std_21d_base_v095_signal(arg_close):
    res = _std(_mom_rsi(arg_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 21d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_z_21d_base_v096_signal(arg_close):
    res = _z(_mom_rsi(arg_close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 42d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_42d_base_v097_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 42d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_42d_base_v098_signal(arg_closeadj):
    res = _mom_rsi(arg_closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 42d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_sma_42d_base_v099_signal(arg_closeadj):
    res = _sma(_mom_roc(arg_closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 42d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_std_42d_base_v100_signal(arg_closeadj):
    res = _std(_mom_roc(arg_closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 42d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_z_42d_base_v101_signal(arg_closeadj):
    res = _z(_mom_roc(arg_closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 42d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_sma_42d_base_v102_signal(arg_closeadj):
    res = _sma(_mom_rsi(arg_closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 42d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_std_42d_base_v103_signal(arg_closeadj):
    res = _std(_mom_rsi(arg_closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 42d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_z_42d_base_v104_signal(arg_closeadj):
    res = _z(_mom_rsi(arg_closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 63d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_63d_base_v105_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 63d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_63d_base_v106_signal(arg_closeadj):
    res = _mom_rsi(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 63d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_sma_63d_base_v107_signal(arg_closeadj):
    res = _sma(_mom_roc(arg_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 63d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_std_63d_base_v108_signal(arg_closeadj):
    res = _std(_mom_roc(arg_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 63d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_z_63d_base_v109_signal(arg_closeadj):
    res = _z(_mom_roc(arg_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 63d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_sma_63d_base_v110_signal(arg_closeadj):
    res = _sma(_mom_rsi(arg_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 63d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_std_63d_base_v111_signal(arg_closeadj):
    res = _std(_mom_rsi(arg_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 63d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_z_63d_base_v112_signal(arg_closeadj):
    res = _z(_mom_rsi(arg_closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 126d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_126d_base_v113_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 126d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_126d_base_v114_signal(arg_closeadj):
    res = _mom_rsi(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 126d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_sma_126d_base_v115_signal(arg_closeadj):
    res = _sma(_mom_roc(arg_closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 126d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_std_126d_base_v116_signal(arg_closeadj):
    res = _std(_mom_roc(arg_closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 126d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_z_126d_base_v117_signal(arg_closeadj):
    res = _z(_mom_roc(arg_closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 126d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_sma_126d_base_v118_signal(arg_closeadj):
    res = _sma(_mom_rsi(arg_closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 126d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_std_126d_base_v119_signal(arg_closeadj):
    res = _std(_mom_rsi(arg_closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 126d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_z_126d_base_v120_signal(arg_closeadj):
    res = _z(_mom_rsi(arg_closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 252d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_252d_base_v121_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 252d window of closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_252d_base_v122_signal(arg_closeadj):
    res = _mom_rsi(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 252d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_sma_252d_base_v123_signal(arg_closeadj):
    res = _sma(_mom_roc(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 252d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_std_252d_base_v124_signal(arg_closeadj):
    res = _std(_mom_roc(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 252d ROC for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_z_252d_base_v125_signal(arg_closeadj):
    res = _z(_mom_roc(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 252d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_sma_252d_base_v126_signal(arg_closeadj):
    res = _sma(_mom_rsi(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 252d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_std_252d_base_v127_signal(arg_closeadj):
    res = _std(_mom_rsi(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 252d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_z_252d_base_v128_signal(arg_closeadj):
    res = _z(_mom_rsi(arg_closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 2d ROC vs 21d ROC in price_momentum domain
def f09_price_momentum_roc_div_2d_21d_base_v129_signal(arg_open, arg_close):
    res = _mom_roc(arg_open, 2) - _mom_roc(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 3d ROC vs 21d ROC in price_momentum domain
def f09_price_momentum_roc_div_3d_21d_base_v130_signal(arg_open, arg_close):
    res = _mom_roc(arg_open, 3) - _mom_roc(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 5d ROC vs 21d ROC in price_momentum domain
def f09_price_momentum_roc_div_5d_21d_base_v131_signal(arg_open, arg_close):
    res = _mom_roc(arg_open, 5) - _mom_roc(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 10d ROC vs 21d ROC in price_momentum domain
def f09_price_momentum_roc_div_10d_21d_base_v132_signal(arg_close):
    res = _mom_roc(arg_close, 10) - _mom_roc(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 21d ROC vs 252d ROC in price_momentum domain
def f09_price_momentum_roc_div_21d_252d_base_v133_signal(arg_close, arg_closeadj):
    res = _mom_roc(arg_close, 21) - _mom_roc(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 42d ROC vs 252d ROC in price_momentum domain
def f09_price_momentum_roc_div_42d_252d_base_v134_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 42) - _mom_roc(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 63d ROC vs 252d ROC in price_momentum domain
def f09_price_momentum_roc_div_63d_252d_base_v135_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 63) - _mom_roc(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Momentum Divergence: 126d ROC vs 252d ROC in price_momentum domain
def f09_price_momentum_roc_div_126d_252d_base_v136_signal(arg_closeadj):
    res = _mom_roc(arg_closeadj, 126) - _mom_roc(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC relative to its 252d Max for closeadj in price_momentum domain
def f09_price_momentum_closeadj_roc_rel_max_252d_base_v137_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 21)
    res = roc / _max(roc, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC relative to its 252d Max for 63d ROC in price_momentum domain
def f09_price_momentum_closeadj_roc_63d_rel_max_252d_base_v138_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 63)
    res = roc / _max(roc, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Average daily return during 21d positive streaks in price_momentum domain
def f09_price_momentum_avg_pos_ret_21d_base_v139_signal(arg_close):
    ret = arg_close.pct_change()
    res = ret.where(ret > 0, 0).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Average daily return during 63d positive streaks in price_momentum domain
def f09_price_momentum_avg_pos_ret_63d_base_v140_signal(arg_closeadj):
    ret = arg_closeadj.pct_change()
    res = ret.where(ret > 0, 0).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with ROC > 0 over 21d in price_momentum domain
def f09_price_momentum_pos_roc_count_21d_base_v141_signal(arg_close):
    roc = _mom_roc(arg_close, 1)
    res = (roc > 0).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with ROC > 0 over 63d in price_momentum domain
def f09_price_momentum_pos_roc_count_63d_base_v142_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 1)
    res = (roc > 0).rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 63d ROC relative to 252d history in price_momentum domain
def f09_price_momentum_roc_63d_z_252d_base_v143_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 63)
    res = _z(roc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 21d ROC relative to 126d history in price_momentum domain
def f09_price_momentum_roc_21d_z_126d_base_v144_signal(arg_close):
    roc = _mom_roc(arg_close, 21)
    res = _z(roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d ROC relative to 63d history in price_momentum domain
def f09_price_momentum_roc_5d_z_63d_base_v145_signal(arg_close):
    roc = _mom_roc(arg_close, 5)
    res = _z(roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI Divergence: 14d RSI vs 50d RSI in price_momentum domain
def f09_price_momentum_rsi_div_14d_50d_base_v146_signal(arg_close):
    res = _mom_rsi(arg_close, 14) - _mom_rsi(arg_close, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI Divergence: 7d RSI vs 21d RSI in price_momentum domain
def f09_price_momentum_rsi_div_7d_21d_base_v147_signal(arg_close):
    res = _mom_rsi(arg_close, 7) - _mom_rsi(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 50d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_sma_50d_base_v148_signal(arg_closeadj):
    res = _sma(_mom_rsi(arg_closeadj, 50), 50)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 50d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_std_50d_base_v149_signal(arg_closeadj):
    res = _std(_mom_rsi(arg_closeadj, 50), 50)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 50d RSI for closeadj in price_momentum domain
def f09_price_momentum_closeadj_rsi_z_50d_base_v150_signal(arg_closeadj):
    res = _z(_mom_rsi(arg_closeadj, 50), 50)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f09_price_momentum_close_roc_std_10d_base_v076_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_10d_base_v076_signal},
    "f09_price_momentum_close_roc_z_10d_base_v077_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_10d_base_v077_signal},
    "f09_price_momentum_close_rsi_sma_10d_base_v078_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_sma_10d_base_v078_signal},
    "f09_price_momentum_close_rsi_std_10d_base_v079_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_std_10d_base_v079_signal},
    "f09_price_momentum_close_rsi_z_10d_base_v080_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_10d_base_v080_signal},
    "f09_price_momentum_close_roc_14d_base_v081_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_14d_base_v081_signal},
    "f09_price_momentum_close_rsi_14d_base_v082_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_14d_base_v082_signal},
    "f09_price_momentum_close_roc_sma_14d_base_v083_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_14d_base_v083_signal},
    "f09_price_momentum_close_roc_std_14d_base_v084_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_14d_base_v084_signal},
    "f09_price_momentum_close_roc_z_14d_base_v085_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_14d_base_v085_signal},
    "f09_price_momentum_close_rsi_sma_14d_base_v086_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_sma_14d_base_v086_signal},
    "f09_price_momentum_close_rsi_std_14d_base_v087_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_std_14d_base_v087_signal},
    "f09_price_momentum_close_rsi_z_14d_base_v088_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_14d_base_v088_signal},
    "f09_price_momentum_close_roc_21d_base_v089_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_21d_base_v089_signal},
    "f09_price_momentum_close_rsi_21d_base_v090_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_21d_base_v090_signal},
    "f09_price_momentum_close_roc_sma_21d_base_v091_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_21d_base_v091_signal},
    "f09_price_momentum_close_roc_std_21d_base_v092_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_21d_base_v092_signal},
    "f09_price_momentum_close_roc_z_21d_base_v093_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_21d_base_v093_signal},
    "f09_price_momentum_close_rsi_sma_21d_base_v094_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_sma_21d_base_v094_signal},
    "f09_price_momentum_close_rsi_std_21d_base_v095_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_std_21d_base_v095_signal},
    "f09_price_momentum_close_rsi_z_21d_base_v096_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_21d_base_v096_signal},
    "f09_price_momentum_closeadj_roc_42d_base_v097_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_42d_base_v097_signal},
    "f09_price_momentum_closeadj_rsi_42d_base_v098_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_42d_base_v098_signal},
    "f09_price_momentum_closeadj_roc_sma_42d_base_v099_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_42d_base_v099_signal},
    "f09_price_momentum_closeadj_roc_std_42d_base_v100_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_42d_base_v100_signal},
    "f09_price_momentum_closeadj_roc_z_42d_base_v101_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_42d_base_v101_signal},
    "f09_price_momentum_closeadj_rsi_sma_42d_base_v102_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_42d_base_v102_signal},
    "f09_price_momentum_closeadj_rsi_std_42d_base_v103_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_42d_base_v103_signal},
    "f09_price_momentum_closeadj_rsi_z_42d_base_v104_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_42d_base_v104_signal},
    "f09_price_momentum_closeadj_roc_63d_base_v105_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_63d_base_v105_signal},
    "f09_price_momentum_closeadj_rsi_63d_base_v106_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_63d_base_v106_signal},
    "f09_price_momentum_closeadj_roc_sma_63d_base_v107_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_63d_base_v107_signal},
    "f09_price_momentum_closeadj_roc_std_63d_base_v108_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_63d_base_v108_signal},
    "f09_price_momentum_closeadj_roc_z_63d_base_v109_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_63d_base_v109_signal},
    "f09_price_momentum_closeadj_rsi_sma_63d_base_v110_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_63d_base_v110_signal},
    "f09_price_momentum_closeadj_rsi_std_63d_base_v111_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_63d_base_v111_signal},
    "f09_price_momentum_closeadj_rsi_z_63d_base_v112_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_63d_base_v112_signal},
    "f09_price_momentum_closeadj_roc_126d_base_v113_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_126d_base_v113_signal},
    "f09_price_momentum_closeadj_rsi_126d_base_v114_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_126d_base_v114_signal},
    "f09_price_momentum_closeadj_roc_sma_126d_base_v115_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_126d_base_v115_signal},
    "f09_price_momentum_closeadj_roc_std_126d_base_v116_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_126d_base_v116_signal},
    "f09_price_momentum_closeadj_roc_z_126d_base_v117_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_126d_base_v117_signal},
    "f09_price_momentum_closeadj_rsi_sma_126d_base_v118_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_126d_base_v118_signal},
    "f09_price_momentum_closeadj_rsi_std_126d_base_v119_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_126d_base_v119_signal},
    "f09_price_momentum_closeadj_rsi_z_126d_base_v120_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_126d_base_v120_signal},
    "f09_price_momentum_closeadj_roc_252d_base_v121_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_252d_base_v121_signal},
    "f09_price_momentum_closeadj_rsi_252d_base_v122_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_252d_base_v122_signal},
    "f09_price_momentum_closeadj_roc_sma_252d_base_v123_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_252d_base_v123_signal},
    "f09_price_momentum_closeadj_roc_std_252d_base_v124_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_252d_base_v124_signal},
    "f09_price_momentum_closeadj_roc_z_252d_base_v125_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_252d_base_v125_signal},
    "f09_price_momentum_closeadj_rsi_sma_252d_base_v126_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_252d_base_v126_signal},
    "f09_price_momentum_closeadj_rsi_std_252d_base_v127_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_252d_base_v127_signal},
    "f09_price_momentum_closeadj_rsi_z_252d_base_v128_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_252d_base_v128_signal},
    "f09_price_momentum_roc_div_2d_21d_base_v129_signal": {"inputs": ["open", "close"], "func": f09_price_momentum_roc_div_2d_21d_base_v129_signal},
    "f09_price_momentum_roc_div_3d_21d_base_v130_signal": {"inputs": ["open", "close"], "func": f09_price_momentum_roc_div_3d_21d_base_v130_signal},
    "f09_price_momentum_roc_div_5d_21d_base_v131_signal": {"inputs": ["open", "close"], "func": f09_price_momentum_roc_div_5d_21d_base_v131_signal},
    "f09_price_momentum_roc_div_10d_21d_base_v132_signal": {"inputs": ["close"], "func": f09_price_momentum_roc_div_10d_21d_base_v132_signal},
    "f09_price_momentum_roc_div_21d_252d_base_v133_signal": {"inputs": ["close", "closeadj"], "func": f09_price_momentum_roc_div_21d_252d_base_v133_signal},
    "f09_price_momentum_roc_div_42d_252d_base_v134_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_div_42d_252d_base_v134_signal},
    "f09_price_momentum_roc_div_63d_252d_base_v135_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_div_63d_252d_base_v135_signal},
    "f09_price_momentum_roc_div_126d_252d_base_v136_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_div_126d_252d_base_v136_signal},
    "f09_price_momentum_closeadj_roc_rel_max_252d_base_v137_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_rel_max_252d_base_v137_signal},
    "f09_price_momentum_closeadj_roc_63d_rel_max_252d_base_v138_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_63d_rel_max_252d_base_v138_signal},
    "f09_price_momentum_avg_pos_ret_21d_base_v139_signal": {"inputs": ["close"], "func": f09_price_momentum_avg_pos_ret_21d_base_v139_signal},
    "f09_price_momentum_avg_pos_ret_63d_base_v140_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_avg_pos_ret_63d_base_v140_signal},
    "f09_price_momentum_pos_roc_count_21d_base_v141_signal": {"inputs": ["close"], "func": f09_price_momentum_pos_roc_count_21d_base_v141_signal},
    "f09_price_momentum_pos_roc_count_63d_base_v142_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_pos_roc_count_63d_base_v142_signal},
    "f09_price_momentum_roc_63d_z_252d_base_v143_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_63d_z_252d_base_v143_signal},
    "f09_price_momentum_roc_21d_z_126d_base_v144_signal": {"inputs": ["close"], "func": f09_price_momentum_roc_21d_z_126d_base_v144_signal},
    "f09_price_momentum_roc_5d_z_63d_base_v145_signal": {"inputs": ["close"], "func": f09_price_momentum_roc_5d_z_63d_base_v145_signal},
    "f09_price_momentum_rsi_div_14d_50d_base_v146_signal": {"inputs": ["close"], "func": f09_price_momentum_rsi_div_14d_50d_base_v146_signal},
    "f09_price_momentum_rsi_div_7d_21d_base_v147_signal": {"inputs": ["close"], "func": f09_price_momentum_rsi_div_7d_21d_base_v147_signal},
    "f09_price_momentum_closeadj_rsi_sma_50d_base_v148_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_50d_base_v148_signal},
    "f09_price_momentum_closeadj_rsi_std_50d_base_v149_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_50d_base_v149_signal},
    "f09_price_momentum_closeadj_rsi_z_50d_base_v150_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_50d_base_v150_signal},
}

F09_PRICE_MOMENTUM_REGISTRY_BASE_076_150 = REGISTRY

if __name__ == "__main__":
    import inspect
    pd.set_option('display.max_columns', None)
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "open": np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100,
        "high": np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100 + 1,
        "low": np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100 - 1,
        "close": np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100,
        "closeadj": np.exp(np.random.normal(0, 0.05, n).cumsum()) * 100
    })
    for name, info in REGISTRY.items():
        inputs = [df[col] for col in info["inputs"]]
        y1 = info["func"](*inputs)
        y2 = info["func"](*inputs)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0
        assert not q.isna().all()
        source = inspect.getsource(info["func"])
        assert "_mom_" in source or "pct_change" in source or "rolling" in source
    print("All tests passed!")
