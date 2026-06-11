# f01_peak_and_crash_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _z(s, w):
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _min(s, w):
    return s.rolling(w, min_periods=min(w, 5)).min()

def _max(s, w):
    return s.rolling(w, min_periods=min(w, 5)).max()

def _atr(h, l, c, w):
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=min(w, 5)).mean()

def _peak_crash_drawdown(c, w):
    return (c / _max(c, w).replace(0, np.nan)) - 1

def _peak_crash_recovery(c, w):
    return (c / _min(c, w).replace(0, np.nan)) - 1

# 5d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_5d_base_v076_signal(close):
    res = _ema(_peak_crash_drawdown(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# 5d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_5d_base_v077_signal(close):
    res = _ema(_peak_crash_recovery(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_5d_base_v078_signal(high, low, close):
    res = _peak_crash_drawdown(close, 5) * close / _atr(high, low, close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 5d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_5d_base_v079_signal(high, low, close):
    res = _peak_crash_recovery(close, 5) * close / _atr(high, low, close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -2% over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_count_5d_base_v080_signal(close):
    res = (_peak_crash_drawdown(close, 5) < -0.02).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 2% over 5d in peak_and_crash domain
def f01_peak_and_crash_rec_count_5d_base_v081_signal(close):
    res = (_peak_crash_recovery(close, 5) > 0.02).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_5d_base_v082_signal(close):
    res = _z(_peak_crash_drawdown(close, 5).diff(1), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 5d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_5d_base_v083_signal(close):
    res = _z(_peak_crash_recovery(close, 5).diff(1), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 5d in peak_and_crash domain
def f01_peak_and_crash_dd_range_5d_base_v084_signal(close):
    dd = _peak_crash_drawdown(close, 5)
    res = _max(dd, 5) - _min(dd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of recovery values over rolling 5d in peak_and_crash domain
def f01_peak_and_crash_rec_range_5d_base_v085_signal(close):
    rec = _peak_crash_recovery(close, 5)
    res = _max(rec, 5) - _min(rec, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Acceleration of drawdown over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_5d_base_v086_signal(close):
    res = _peak_crash_drawdown(close, 5).diff(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

# 10d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_10d_base_v087_signal(close):
    res = _ema(_peak_crash_drawdown(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# 10d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_10d_base_v088_signal(close):
    res = _ema(_peak_crash_recovery(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_10d_base_v089_signal(high, low, close):
    res = _peak_crash_drawdown(close, 10) * close / _atr(high, low, close, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 10d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_10d_base_v090_signal(high, low, close):
    res = _peak_crash_recovery(close, 10) * close / _atr(high, low, close, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -5% over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_count_10d_base_v091_signal(close):
    res = (_peak_crash_drawdown(close, 10) < -0.05).rolling(10).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 5% over 10d in peak_and_crash domain
def f01_peak_and_crash_rec_count_10d_base_v092_signal(close):
    res = (_peak_crash_recovery(close, 10) > 0.05).rolling(10).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_10d_base_v093_signal(close):
    res = _z(_peak_crash_drawdown(close, 10).diff(2), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 10d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_10d_base_v094_signal(close):
    res = _z(_peak_crash_recovery(close, 10).diff(2), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 10d in peak_and_crash domain
def f01_peak_and_crash_dd_range_10d_base_v095_signal(close):
    dd = _peak_crash_drawdown(close, 10)
    res = _max(dd, 10) - _min(dd, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of recovery values over rolling 10d in peak_and_crash domain
def f01_peak_and_crash_rec_range_10d_base_v096_signal(close):
    rec = _peak_crash_recovery(close, 10)
    res = _max(rec, 10) - _min(rec, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Acceleration of drawdown over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_10d_base_v097_signal(close):
    res = _peak_crash_drawdown(close, 10).diff(2).diff(2)
    return res.replace([np.inf, -np.inf], np.nan)

# 21d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_21d_base_v098_signal(close):
    res = _ema(_peak_crash_drawdown(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# 21d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_21d_base_v099_signal(close):
    res = _ema(_peak_crash_recovery(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_21d_base_v100_signal(high, low, close):
    res = _peak_crash_drawdown(close, 21) * close / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 21d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_21d_base_v101_signal(high, low, close):
    res = _peak_crash_recovery(close, 21) * close / _atr(high, low, close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -10% over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_count_21d_base_v102_signal(close):
    res = (_peak_crash_drawdown(close, 21) < -0.10).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 10% over 21d in peak_and_crash domain
def f01_peak_and_crash_rec_count_21d_base_v103_signal(close):
    res = (_peak_crash_recovery(close, 21) > 0.10).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_21d_base_v104_signal(close):
    res = _z(_peak_crash_drawdown(close, 21).diff(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 21d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_21d_base_v105_signal(close):
    res = _z(_peak_crash_recovery(close, 21).diff(5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 21d in peak_and_crash domain
def f01_peak_and_crash_dd_range_21d_base_v106_signal(close):
    dd = _peak_crash_drawdown(close, 21)
    res = _max(dd, 21) - _min(dd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of recovery values over rolling 21d in peak_and_crash domain
def f01_peak_and_crash_rec_range_21d_base_v107_signal(close):
    rec = _peak_crash_recovery(close, 21)
    res = _max(rec, 21) - _min(rec, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Acceleration of drawdown over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_21d_base_v108_signal(close):
    res = _peak_crash_drawdown(close, 21).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_63d_base_v109_signal(closeadj):
    res = _ema(_peak_crash_drawdown(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# 63d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_63d_base_v110_signal(closeadj):
    res = _ema(_peak_crash_recovery(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_63d_base_v111_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_drawdown(closeadj, 63) * closeadj / _atr(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 63d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_63d_base_v112_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_recovery(closeadj, 63) * closeadj / _atr(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -15% over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_count_63d_base_v113_signal(closeadj):
    res = (_peak_crash_drawdown(closeadj, 63) < -0.15).rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 15% over 63d in peak_and_crash domain
def f01_peak_and_crash_rec_count_63d_base_v114_signal(closeadj):
    res = (_peak_crash_recovery(closeadj, 63) > 0.15).rolling(63).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_63d_base_v115_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 63).diff(21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 63d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_63d_base_v116_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 63).diff(21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 63d in peak_and_crash domain
def f01_peak_and_crash_dd_range_63d_base_v117_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 63)
    res = _max(dd, 63) - _min(dd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of recovery values over rolling 63d in peak_and_crash domain
def f01_peak_and_crash_rec_range_63d_base_v118_signal(closeadj):
    rec = _peak_crash_recovery(closeadj, 63)
    res = _max(rec, 63) - _min(rec, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Acceleration of drawdown over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_63d_base_v119_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 63).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_126d_base_v120_signal(closeadj):
    res = _ema(_peak_crash_drawdown(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# 126d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_126d_base_v121_signal(closeadj):
    res = _ema(_peak_crash_recovery(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_126d_base_v122_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_drawdown(closeadj, 126) * closeadj / _atr(high * adj, low * adj, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 126d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_126d_base_v123_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_recovery(closeadj, 126) * closeadj / _atr(high * adj, low * adj, closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -20% over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_count_126d_base_v124_signal(closeadj):
    res = (_peak_crash_drawdown(closeadj, 126) < -0.20).rolling(126).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 20% over 126d in peak_and_crash domain
def f01_peak_and_crash_rec_count_126d_base_v125_signal(closeadj):
    res = (_peak_crash_recovery(closeadj, 126) > 0.20).rolling(126).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_126d_base_v126_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 126).diff(21), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 126d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_126d_base_v127_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 126).diff(21), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 126d in peak_and_crash domain
def f01_peak_and_crash_dd_range_126d_base_v128_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 126)
    res = _max(dd, 126) - _min(dd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of recovery values over rolling 126d in peak_and_crash domain
def f01_peak_and_crash_rec_range_126d_base_v129_signal(closeadj):
    rec = _peak_crash_recovery(closeadj, 126)
    res = _max(rec, 126) - _min(rec, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Acceleration of drawdown over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_126d_base_v130_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 126).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_252d_base_v131_signal(closeadj):
    res = _ema(_peak_crash_drawdown(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# 252d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_252d_base_v132_signal(closeadj):
    res = _ema(_peak_crash_recovery(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_252d_base_v133_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_drawdown(closeadj, 252) * closeadj / _atr(high * adj, low * adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 252d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_252d_base_v134_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_recovery(closeadj, 252) * closeadj / _atr(high * adj, low * adj, closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -25% over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_count_252d_base_v135_signal(closeadj):
    res = (_peak_crash_drawdown(closeadj, 252) < -0.25).rolling(252).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 25% over 252d in peak_and_crash domain
def f01_peak_and_crash_rec_count_252d_base_v136_signal(closeadj):
    res = (_peak_crash_recovery(closeadj, 252) > 0.25).rolling(252).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_252d_base_v137_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 252).diff(63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 252d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_252d_base_v138_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 252).diff(63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 252d in peak_and_crash domain
def f01_peak_and_crash_dd_range_252d_base_v139_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 252)
    res = _max(dd, 252) - _min(dd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of recovery values over rolling 252d in peak_and_crash domain
def f01_peak_and_crash_rec_range_252d_base_v140_signal(closeadj):
    rec = _peak_crash_recovery(closeadj, 252)
    res = _max(rec, 252) - _min(rec, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Acceleration of drawdown over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_252d_base_v141_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 252).diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_504d_base_v142_signal(closeadj):
    res = _ema(_peak_crash_drawdown(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# 504d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_504d_base_v143_signal(closeadj):
    res = _ema(_peak_crash_recovery(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown in ATR units over 504d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_504d_base_v144_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_drawdown(closeadj, 504) * closeadj / _atr(high * adj, low * adj, closeadj, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery in ATR units over 504d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_504d_base_v145_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    res = _peak_crash_recovery(closeadj, 504) * closeadj / _atr(high * adj, low * adj, closeadj, 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with drawdown < -30% over 504d in peak_and_crash domain
def f01_peak_and_crash_dd_count_504d_base_v146_signal(closeadj):
    res = (_peak_crash_drawdown(closeadj, 504) < -0.30).rolling(504).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Count of days with recovery > 30% over 504d in peak_and_crash domain
def f01_peak_and_crash_rec_count_504d_base_v147_signal(closeadj):
    res = (_peak_crash_recovery(closeadj, 504) > 0.30).rolling(504).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown velocity over 504d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_504d_base_v148_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 504).diff(63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery velocity over 504d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_504d_base_v149_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 504).diff(63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Range of drawdown values over rolling 504d in peak_and_crash domain
def f01_peak_and_crash_dd_range_504d_base_v150_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 504)
    res = _max(dd, 504) - _min(dd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f01_peak_and_crash_dd_ema_5d_base_v076_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_ema_5d_base_v076_signal},
    "f01_peak_and_crash_rec_ema_5d_base_v077_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_ema_5d_base_v077_signal},
    "f01_peak_and_crash_dd_atr_5d_base_v078_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_dd_atr_5d_base_v078_signal},
    "f01_peak_and_crash_rec_atr_5d_base_v079_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_rec_atr_5d_base_v079_signal},
    "f01_peak_and_crash_dd_count_5d_base_v080_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_count_5d_base_v080_signal},
    "f01_peak_and_crash_rec_count_5d_base_v081_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_count_5d_base_v081_signal},
    "f01_peak_and_crash_dd_vel_z_5d_base_v082_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_vel_z_5d_base_v082_signal},
    "f01_peak_and_crash_rec_vel_z_5d_base_v083_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_vel_z_5d_base_v083_signal},
    "f01_peak_and_crash_dd_range_5d_base_v084_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_range_5d_base_v084_signal},
    "f01_peak_and_crash_rec_range_5d_base_v085_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_range_5d_base_v085_signal},
    "f01_peak_and_crash_dd_accel_5d_base_v086_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_accel_5d_base_v086_signal},
    "f01_peak_and_crash_dd_ema_10d_base_v087_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_ema_10d_base_v087_signal},
    "f01_peak_and_crash_rec_ema_10d_base_v088_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_ema_10d_base_v088_signal},
    "f01_peak_and_crash_dd_atr_10d_base_v089_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_dd_atr_10d_base_v089_signal},
    "f01_peak_and_crash_rec_atr_10d_base_v090_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_rec_atr_10d_base_v090_signal},
    "f01_peak_and_crash_dd_count_10d_base_v091_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_count_10d_base_v091_signal},
    "f01_peak_and_crash_rec_count_10d_base_v092_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_count_10d_base_v092_signal},
    "f01_peak_and_crash_dd_vel_z_10d_base_v093_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_vel_z_10d_base_v093_signal},
    "f01_peak_and_crash_rec_vel_z_10d_base_v094_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_vel_z_10d_base_v094_signal},
    "f01_peak_and_crash_dd_range_10d_base_v095_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_range_10d_base_v095_signal},
    "f01_peak_and_crash_rec_range_10d_base_v096_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_range_10d_base_v096_signal},
    "f01_peak_and_crash_dd_accel_10d_base_v097_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_accel_10d_base_v097_signal},
    "f01_peak_and_crash_dd_ema_21d_base_v098_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_ema_21d_base_v098_signal},
    "f01_peak_and_crash_rec_ema_21d_base_v099_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_ema_21d_base_v099_signal},
    "f01_peak_and_crash_dd_atr_21d_base_v100_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_dd_atr_21d_base_v100_signal},
    "f01_peak_and_crash_rec_atr_21d_base_v101_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_rec_atr_21d_base_v101_signal},
    "f01_peak_and_crash_dd_count_21d_base_v102_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_count_21d_base_v102_signal},
    "f01_peak_and_crash_rec_count_21d_base_v103_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_count_21d_base_v103_signal},
    "f01_peak_and_crash_dd_vel_z_21d_base_v104_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_vel_z_21d_base_v104_signal},
    "f01_peak_and_crash_rec_vel_z_21d_base_v105_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_vel_z_21d_base_v105_signal},
    "f01_peak_and_crash_dd_range_21d_base_v106_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_range_21d_base_v106_signal},
    "f01_peak_and_crash_rec_range_21d_base_v107_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_range_21d_base_v107_signal},
    "f01_peak_and_crash_dd_accel_21d_base_v108_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_accel_21d_base_v108_signal},
    "f01_peak_and_crash_dd_ema_63d_base_v109_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_63d_base_v109_signal},
    "f01_peak_and_crash_rec_ema_63d_base_v110_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_63d_base_v110_signal},
    "f01_peak_and_crash_dd_atr_63d_base_v111_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_63d_base_v111_signal},
    "f01_peak_and_crash_rec_atr_63d_base_v112_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_63d_base_v112_signal},
    "f01_peak_and_crash_dd_count_63d_base_v113_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_63d_base_v113_signal},
    "f01_peak_and_crash_rec_count_63d_base_v114_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_63d_base_v114_signal},
    "f01_peak_and_crash_dd_vel_z_63d_base_v115_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_63d_base_v115_signal},
    "f01_peak_and_crash_rec_vel_z_63d_base_v116_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_63d_base_v116_signal},
    "f01_peak_and_crash_dd_range_63d_base_v117_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_63d_base_v117_signal},
    "f01_peak_and_crash_rec_range_63d_base_v118_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_range_63d_base_v118_signal},
    "f01_peak_and_crash_dd_accel_63d_base_v119_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_accel_63d_base_v119_signal},
    "f01_peak_and_crash_dd_ema_126d_base_v120_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_126d_base_v120_signal},
    "f01_peak_and_crash_rec_ema_126d_base_v121_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_126d_base_v121_signal},
    "f01_peak_and_crash_dd_atr_126d_base_v122_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_126d_base_v122_signal},
    "f01_peak_and_crash_rec_atr_126d_base_v123_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_126d_base_v123_signal},
    "f01_peak_and_crash_dd_count_126d_base_v124_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_126d_base_v124_signal},
    "f01_peak_and_crash_rec_count_126d_base_v125_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_126d_base_v125_signal},
    "f01_peak_and_crash_dd_vel_z_126d_base_v126_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_126d_base_v126_signal},
    "f01_peak_and_crash_rec_vel_z_126d_base_v127_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_126d_base_v127_signal},
    "f01_peak_and_crash_dd_range_126d_base_v128_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_126d_base_v128_signal},
    "f01_peak_and_crash_rec_range_126d_base_v129_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_range_126d_base_v129_signal},
    "f01_peak_and_crash_dd_accel_126d_base_v130_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_accel_126d_base_v130_signal},
    "f01_peak_and_crash_dd_ema_252d_base_v131_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_252d_base_v131_signal},
    "f01_peak_and_crash_rec_ema_252d_base_v132_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_252d_base_v132_signal},
    "f01_peak_and_crash_dd_atr_252d_base_v133_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_252d_base_v133_signal},
    "f01_peak_and_crash_rec_atr_252d_base_v134_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_252d_base_v134_signal},
    "f01_peak_and_crash_dd_count_252d_base_v135_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_252d_base_v135_signal},
    "f01_peak_and_crash_rec_count_252d_base_v136_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_252d_base_v136_signal},
    "f01_peak_and_crash_dd_vel_z_252d_base_v137_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_252d_base_v137_signal},
    "f01_peak_and_crash_rec_vel_z_252d_base_v138_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_252d_base_v138_signal},
    "f01_peak_and_crash_dd_range_252d_base_v139_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_252d_base_v139_signal},
    "f01_peak_and_crash_rec_range_252d_base_v140_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_range_252d_base_v140_signal},
    "f01_peak_and_crash_dd_accel_252d_base_v141_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_accel_252d_base_v141_signal},
    "f01_peak_and_crash_dd_ema_504d_base_v142_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_504d_base_v142_signal},
    "f01_peak_and_crash_rec_ema_504d_base_v143_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_504d_base_v143_signal},
    "f01_peak_and_crash_dd_atr_504d_base_v144_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_504d_base_v144_signal},
    "f01_peak_and_crash_rec_atr_504d_base_v145_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_504d_base_v145_signal},
    "f01_peak_and_crash_dd_count_504d_base_v146_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_504d_base_v146_signal},
    "f01_peak_and_crash_rec_count_504d_base_v147_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_504d_base_v147_signal},
    "f01_peak_and_crash_dd_vel_z_504d_base_v148_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_504d_base_v148_signal},
    "f01_peak_and_crash_rec_vel_z_504d_base_v149_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_504d_base_v149_signal},
    "f01_peak_and_crash_dd_range_504d_base_v150_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_504d_base_v150_signal},
}

F01_PEAK_AND_CRASH_REGISTRY_076_150 = REGISTRY

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
        assert q.nunique() > 50 or "count" in name or "range" in name
        assert q.std() > 0
        assert not q.isna().all()
        source = inspect.getsource(info["func"])
        assert "_peak_crash_" in source
    print("All tests passed!")
