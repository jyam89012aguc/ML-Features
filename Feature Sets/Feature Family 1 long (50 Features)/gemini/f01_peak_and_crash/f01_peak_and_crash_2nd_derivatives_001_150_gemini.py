# f01_peak_and_crash_slope_001_150_gemini.py
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

# Slope of drawdown from peak over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_5d_slope_v001_signal(close):
    base = _peak_crash_drawdown(close, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 5d window in peak_and_crash domain
def f01_peak_and_crash_recovery_5d_slope_v002_signal(close):
    base = _peak_crash_recovery(close, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_5d_slope_v003_signal(close):
    base = _z(_peak_crash_drawdown(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 5d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_5d_slope_v004_signal(close):
    base = _z(_peak_crash_recovery(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 5d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_5d_slope_v005_signal(close):
    base = close / _max(close, 5).replace(0, np.nan)
    base = base + _peak_crash_drawdown(close, 5) * 0
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 5d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_5d_slope_v006_signal(close):
    base = close / _min(close, 5).replace(0, np.nan)
    base = base + _peak_crash_recovery(close, 5) * 0
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_5d_slope_v007_signal(close):
    base = _peak_crash_drawdown(close, 5).rolling(5).std()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 5d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_5d_slope_v008_signal(close):
    base = _peak_crash_recovery(close, 5).rolling(5).std()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_5d_slope_v009_signal(close):
    base = _sma(_peak_crash_drawdown(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 5d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_5d_slope_v010_signal(close):
    base = _min(_peak_crash_drawdown(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum recovery observed over rolling 5d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_5d_slope_v011_signal(close):
    base = _max(_peak_crash_recovery(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown from peak over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_10d_slope_v012_signal(close):
    base = _peak_crash_drawdown(close, 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 10d window in peak_and_crash domain
def f01_peak_and_crash_recovery_10d_slope_v013_signal(close):
    base = _peak_crash_recovery(close, 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_10d_slope_v014_signal(close):
    base = _z(_peak_crash_drawdown(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 10d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_10d_slope_v015_signal(close):
    base = _z(_peak_crash_recovery(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 10d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_10d_slope_v016_signal(close):
    base = close / _max(close, 10).replace(0, np.nan)
    base = base + _peak_crash_drawdown(close, 10) * 0
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 10d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_10d_slope_v017_signal(close):
    base = close / _min(close, 10).replace(0, np.nan)
    base = base + _peak_crash_recovery(close, 10) * 0
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_10d_slope_v018_signal(close):
    base = _peak_crash_drawdown(close, 10).rolling(10).std()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 10d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_10d_slope_v019_signal(close):
    base = _peak_crash_recovery(close, 10).rolling(10).std()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_10d_slope_v020_signal(close):
    base = _sma(_peak_crash_drawdown(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 10d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_10d_slope_v021_signal(close):
    base = _min(_peak_crash_drawdown(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum recovery observed over rolling 10d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_10d_slope_v022_signal(close):
    base = _max(_peak_crash_recovery(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown from peak over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_21d_slope_v023_signal(close):
    base = _peak_crash_drawdown(close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 21d window in peak_and_crash domain
def f01_peak_and_crash_recovery_21d_slope_v024_signal(close):
    base = _peak_crash_recovery(close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_21d_slope_v025_signal(close):
    base = _z(_peak_crash_drawdown(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 21d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_21d_slope_v026_signal(close):
    base = _z(_peak_crash_recovery(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 21d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_21d_slope_v027_signal(close):
    base = close / _max(close, 21).replace(0, np.nan)
    base = base + _peak_crash_drawdown(close, 21) * 0
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 21d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_21d_slope_v028_signal(close):
    base = close / _min(close, 21).replace(0, np.nan)
    base = base + _peak_crash_recovery(close, 21) * 0
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_21d_slope_v029_signal(close):
    base = _peak_crash_drawdown(close, 21).rolling(21).std()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 21d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_21d_slope_v030_signal(close):
    base = _peak_crash_recovery(close, 21).rolling(21).std()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_21d_slope_v031_signal(close):
    base = _sma(_peak_crash_drawdown(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 21d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_21d_slope_v032_signal(close):
    base = _min(_peak_crash_drawdown(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum recovery observed over rolling 21d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_21d_slope_v033_signal(close):
    base = _max(_peak_crash_recovery(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown from peak over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_63d_slope_v034_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 63d window in peak_and_crash domain
def f01_peak_and_crash_recovery_63d_slope_v035_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_63d_slope_v036_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 63d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_63d_slope_v037_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 63d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_63d_slope_v038_signal(closeadj):
    base = closeadj / _max(closeadj, 63).replace(0, np.nan)
    base = base + _peak_crash_drawdown(closeadj, 63) * 0
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 63d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_63d_slope_v039_signal(closeadj):
    base = closeadj / _min(closeadj, 63).replace(0, np.nan)
    base = base + _peak_crash_recovery(closeadj, 63) * 0
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_63d_slope_v040_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 63).rolling(63).std()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 63d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_63d_slope_v041_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 63).rolling(63).std()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_63d_slope_v042_signal(closeadj):
    base = _sma(_peak_crash_drawdown(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 63d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_63d_slope_v043_signal(closeadj):
    base = _min(_peak_crash_drawdown(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum recovery observed over rolling 63d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_63d_slope_v044_signal(closeadj):
    base = _max(_peak_crash_recovery(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown from peak over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_126d_slope_v045_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 126d window in peak_and_crash domain
def f01_peak_and_crash_recovery_126d_slope_v046_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_126d_slope_v047_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 126d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_126d_slope_v048_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 126d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_126d_slope_v049_signal(closeadj):
    base = closeadj / _max(closeadj, 126).replace(0, np.nan)
    base = base + _peak_crash_drawdown(closeadj, 126) * 0
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 126d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_126d_slope_v050_signal(closeadj):
    base = closeadj / _min(closeadj, 126).replace(0, np.nan)
    base = base + _peak_crash_recovery(closeadj, 126) * 0
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_126d_slope_v051_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 126).rolling(126).std()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 126d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_126d_slope_v052_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 126).rolling(126).std()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_126d_slope_v053_signal(closeadj):
    base = _sma(_peak_crash_drawdown(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 126d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_126d_slope_v054_signal(closeadj):
    base = _min(_peak_crash_drawdown(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum recovery observed over rolling 126d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_126d_slope_v055_signal(closeadj):
    base = _max(_peak_crash_recovery(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown from peak over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_252d_slope_v056_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 252d window in peak_and_crash domain
def f01_peak_and_crash_recovery_252d_slope_v057_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_252d_slope_v058_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 252d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_252d_slope_v059_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 252d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_252d_slope_v060_signal(closeadj):
    base = closeadj / _max(closeadj, 252).replace(0, np.nan)
    base = base + _peak_crash_drawdown(closeadj, 252) * 0
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 252d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_252d_slope_v061_signal(closeadj):
    base = closeadj / _min(closeadj, 252).replace(0, np.nan)
    base = base + _peak_crash_recovery(closeadj, 252) * 0
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_252d_slope_v062_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 252).rolling(252).std()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 252d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_252d_slope_v063_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 252).rolling(252).std()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_252d_slope_v064_signal(closeadj):
    base = _sma(_peak_crash_drawdown(closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 252d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_252d_slope_v065_signal(closeadj):
    base = _min(_peak_crash_drawdown(closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown from peak over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_504d_slope_v066_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery from trough over 504d window in peak_and_crash domain
def f01_peak_and_crash_recovery_504d_slope_v067_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown from peak over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_504d_slope_v068_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 504), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery from trough over 504d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_504d_slope_v069_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 504), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 504d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_504d_slope_v070_signal(closeadj):
    base = closeadj / _max(closeadj, 504).replace(0, np.nan)
    base = base + _peak_crash_drawdown(closeadj, 504) * 0
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of ratio of current price to 504d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_504d_slope_v071_signal(closeadj):
    base = closeadj / _min(closeadj, 504).replace(0, np.nan)
    base = base + _peak_crash_recovery(closeadj, 504) * 0
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of drawdown over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_504d_slope_v072_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 504).rolling(504).std()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling volatility of recovery over 504d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_504d_slope_v073_signal(closeadj):
    base = _peak_crash_recovery(closeadj, 504).rolling(504).std()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of rolling mean of drawdown over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_504d_slope_v074_signal(closeadj):
    base = _sma(_peak_crash_drawdown(closeadj, 504), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of maximum drawdown observed over rolling 504d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_504d_slope_v075_signal(closeadj):
    base = _min(_peak_crash_drawdown(closeadj, 504), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 5d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_5d_slope_v076_signal(close):
    base = _ema(_peak_crash_drawdown(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 5d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_5d_slope_v077_signal(close):
    base = _ema(_peak_crash_recovery(close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_5d_slope_v078_signal(high, low, close):
    base = _peak_crash_drawdown(close, 5) * close / _atr(high, low, close, 5).replace(0, np.nan)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 5d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_5d_slope_v079_signal(high, low, close):
    base = _peak_crash_recovery(close, 5) * close / _atr(high, low, close, 5).replace(0, np.nan)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -2% over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_count_5d_slope_v080_signal(close):
    base = (_peak_crash_drawdown(close, 5) < -0.02).rolling(5).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 2% over 5d in peak_and_crash domain
def f01_peak_and_crash_rec_count_5d_slope_v081_signal(close):
    base = (_peak_crash_recovery(close, 5) > 0.02).rolling(5).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_5d_slope_v082_signal(close):
    base = _z(_peak_crash_drawdown(close, 5).diff(1), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 5d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_5d_slope_v083_signal(close):
    base = _z(_peak_crash_recovery(close, 5).diff(1), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 5d in peak_and_crash domain
def f01_peak_and_crash_dd_range_5d_slope_v084_signal(close):
    dd = _peak_crash_drawdown(close, 5)
    base = _max(dd, 5) - _min(dd, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of recovery values over rolling 5d in peak_and_crash domain
def f01_peak_and_crash_rec_range_5d_slope_v085_signal(close):
    rec = _peak_crash_recovery(close, 5)
    base = _max(rec, 5) - _min(rec, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of acceleration of drawdown over 5d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_5d_slope_v086_signal(close):
    base = _peak_crash_drawdown(close, 5).diff(1).diff(1)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 10d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_10d_slope_v087_signal(close):
    base = _ema(_peak_crash_drawdown(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 10d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_10d_slope_v088_signal(close):
    base = _ema(_peak_crash_recovery(close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_10d_slope_v089_signal(high, low, close):
    base = _peak_crash_drawdown(close, 10) * close / _atr(high, low, close, 10).replace(0, np.nan)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 10d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_10d_slope_v090_signal(high, low, close):
    base = _peak_crash_recovery(close, 10) * close / _atr(high, low, close, 10).replace(0, np.nan)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -5% over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_count_10d_slope_v091_signal(close):
    base = (_peak_crash_drawdown(close, 10) < -0.05).rolling(10).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 5% over 10d in peak_and_crash domain
def f01_peak_and_crash_rec_count_10d_slope_v092_signal(close):
    base = (_peak_crash_recovery(close, 10) > 0.05).rolling(10).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_10d_slope_v093_signal(close):
    base = _z(_peak_crash_drawdown(close, 10).diff(2), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 10d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_10d_slope_v094_signal(close):
    base = _z(_peak_crash_recovery(close, 10).diff(2), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 10d in peak_and_crash domain
def f01_peak_and_crash_dd_range_10d_slope_v095_signal(close):
    dd = _peak_crash_drawdown(close, 10)
    base = _max(dd, 10) - _min(dd, 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of recovery values over rolling 10d in peak_and_crash domain
def f01_peak_and_crash_rec_range_10d_slope_v096_signal(close):
    rec = _peak_crash_recovery(close, 10)
    base = _max(rec, 10) - _min(rec, 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of acceleration of drawdown over 10d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_10d_slope_v097_signal(close):
    base = _peak_crash_drawdown(close, 10).diff(2).diff(2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 21d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_21d_slope_v098_signal(close):
    base = _ema(_peak_crash_drawdown(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 21d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_21d_slope_v099_signal(close):
    base = _ema(_peak_crash_recovery(close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_21d_slope_v100_signal(high, low, close):
    base = _peak_crash_drawdown(close, 21) * close / _atr(high, low, close, 21).replace(0, np.nan)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 21d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_21d_slope_v101_signal(high, low, close):
    base = _peak_crash_recovery(close, 21) * close / _atr(high, low, close, 21).replace(0, np.nan)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -10% over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_count_21d_slope_v102_signal(close):
    base = (_peak_crash_drawdown(close, 21) < -0.10).rolling(21).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 10% over 21d in peak_and_crash domain
def f01_peak_and_crash_rec_count_21d_slope_v103_signal(close):
    base = (_peak_crash_recovery(close, 21) > 0.10).rolling(21).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_21d_slope_v104_signal(close):
    base = _z(_peak_crash_drawdown(close, 21).diff(5), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 21d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_21d_slope_v105_signal(close):
    base = _z(_peak_crash_recovery(close, 21).diff(5), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 21d in peak_and_crash domain
def f01_peak_and_crash_dd_range_21d_slope_v106_signal(close):
    dd = _peak_crash_drawdown(close, 21)
    base = _max(dd, 21) - _min(dd, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of recovery values over rolling 21d in peak_and_crash domain
def f01_peak_and_crash_rec_range_21d_slope_v107_signal(close):
    rec = _peak_crash_recovery(close, 21)
    base = _max(rec, 21) - _min(rec, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of acceleration of drawdown over 21d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_21d_slope_v108_signal(close):
    base = _peak_crash_drawdown(close, 21).diff(5).diff(5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_63d_slope_v109_signal(closeadj):
    base = _ema(_peak_crash_drawdown(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 63d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_63d_slope_v110_signal(closeadj):
    base = _ema(_peak_crash_recovery(closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_63d_slope_v111_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_drawdown(closeadj, 63) * closeadj / _atr(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 63d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_63d_slope_v112_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_recovery(closeadj, 63) * closeadj / _atr(high * adj, low * adj, closeadj, 63).replace(0, np.nan)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -15% over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_count_63d_slope_v113_signal(closeadj):
    base = (_peak_crash_drawdown(closeadj, 63) < -0.15).rolling(63).sum()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 15% over 63d in peak_and_crash domain
def f01_peak_and_crash_rec_count_63d_slope_v114_signal(closeadj):
    base = (_peak_crash_recovery(closeadj, 63) > 0.15).rolling(63).sum()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_63d_slope_v115_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 63).diff(21), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 63d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_63d_slope_v116_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 63).diff(21), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 63d in peak_and_crash domain
def f01_peak_and_crash_dd_range_63d_slope_v117_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 63)
    base = _max(dd, 63) - _min(dd, 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of recovery values over rolling 63d in peak_and_crash domain
def f01_peak_and_crash_rec_range_63d_slope_v118_signal(closeadj):
    rec = _peak_crash_recovery(closeadj, 63)
    base = _max(rec, 63) - _min(rec, 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of acceleration of drawdown over 63d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_63d_slope_v119_signal(closeadj):
    base = _peak_crash_drawdown(closeadj, 63).diff(21).diff(21)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_126d_slope_v120_signal(closeadj):
    base = _ema(_peak_crash_drawdown(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 126d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_126d_slope_v121_signal(closeadj):
    base = _ema(_peak_crash_recovery(closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_126d_slope_v122_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_drawdown(closeadj, 126) * closeadj / _atr(high * adj, low * adj, closeadj, 126).replace(0, np.nan)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 126d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_126d_slope_v123_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_recovery(closeadj, 126) * closeadj / _atr(high * adj, low * adj, closeadj, 126).replace(0, np.nan)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -20% over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_count_126d_slope_v124_signal(closeadj):
    base = (_peak_crash_drawdown(closeadj, 126) < -0.20).rolling(126).sum()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 20% over 126d in peak_and_crash domain
def f01_peak_and_crash_rec_count_126d_slope_v125_signal(closeadj):
    base = (_peak_crash_recovery(closeadj, 126) > 0.20).rolling(126).sum()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_126d_slope_v126_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 126).diff(21), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 126d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_126d_slope_v127_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 126).diff(21), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 126d in peak_and_crash domain
def f01_peak_and_crash_dd_range_126d_slope_v128_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 126)
    base = _max(dd, 126) - _min(dd, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of recovery values over rolling 126d in peak_and_crash domain
def f01_peak_and_crash_rec_range_126d_slope_v129_signal(closeadj):
    rec = _peak_crash_recovery(closeadj, 126)
    base = _max(rec, 126) - _min(rec, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of acceleration of drawdown over 126d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_126d_slope_v130_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 126).diff(21).diff(21)
    res = res.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_252d_slope_v131_signal(closeadj):
    base = _ema(_peak_crash_drawdown(closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 252d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_252d_slope_v132_signal(closeadj):
    base = _ema(_peak_crash_recovery(closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_252d_slope_v133_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_drawdown(closeadj, 252) * closeadj / _atr(high * adj, low * adj, closeadj, 252).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 252d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_252d_slope_v134_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_recovery(closeadj, 252) * closeadj / _atr(high * adj, low * adj, closeadj, 252).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -25% over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_count_252d_slope_v135_signal(closeadj):
    base = (_peak_crash_drawdown(closeadj, 252) < -0.25).rolling(252).sum()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 25% over 252d in peak_and_crash domain
def f01_peak_and_crash_rec_count_252d_slope_v136_signal(closeadj):
    base = (_peak_crash_recovery(closeadj, 252) > 0.25).rolling(252).sum()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_252d_slope_v137_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 252).diff(63), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 252d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_252d_slope_v138_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 252).diff(63), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 252d in peak_and_crash domain
def f01_peak_and_crash_dd_range_252d_slope_v139_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 252)
    base = _max(dd, 252) - _min(dd, 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of recovery values over rolling 252d in peak_and_crash domain
def f01_peak_and_crash_rec_range_252d_slope_v140_signal(closeadj):
    rec = _peak_crash_recovery(closeadj, 252)
    base = _max(rec, 252) - _min(rec, 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of acceleration of drawdown over 252d in peak_and_crash domain
def f01_peak_and_crash_dd_accel_252d_slope_v141_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 252).diff(63).diff(63)
    res = res.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d EMA of drawdown in peak_and_crash domain
def f01_peak_and_crash_dd_ema_504d_slope_v142_signal(closeadj):
    base = _ema(_peak_crash_drawdown(closeadj, 504), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of 504d EMA of recovery in peak_and_crash domain
def f01_peak_and_crash_rec_ema_504d_slope_v143_signal(closeadj):
    base = _ema(_peak_crash_recovery(closeadj, 504), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of drawdown in ATR units over 504d in peak_and_crash domain
def f01_peak_and_crash_dd_atr_504d_slope_v144_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_drawdown(closeadj, 504) * closeadj / _atr(high * adj, low * adj, closeadj, 504).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of recovery in ATR units over 504d in peak_and_crash domain
def f01_peak_and_crash_rec_atr_504d_slope_v145_signal(high, low, close, closeadj):
    adj = closeadj / close.replace(0, np.nan)
    base = _peak_crash_recovery(closeadj, 504) * closeadj / _atr(high * adj, low * adj, closeadj, 504).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with drawdown < -30% over 504d in peak_and_crash domain
def f01_peak_and_crash_dd_count_504d_slope_v146_signal(closeadj):
    base = (_peak_crash_drawdown(closeadj, 504) < -0.30).rolling(504).sum()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of count of days with recovery > 30% over 504d in peak_and_crash domain
def f01_peak_and_crash_rec_count_504d_slope_v147_signal(closeadj):
    base = (_peak_crash_recovery(closeadj, 504) > 0.30).rolling(504).sum()
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of drawdown velocity over 504d in peak_and_crash domain
def f01_peak_and_crash_dd_vel_z_504d_slope_v148_signal(closeadj):
    base = _z(_peak_crash_drawdown(closeadj, 504).diff(63), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of z-score of recovery velocity over 504d in peak_and_crash domain
def f01_peak_and_crash_rec_vel_z_504d_slope_v149_signal(closeadj):
    base = _z(_peak_crash_recovery(closeadj, 504).diff(63), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of range of drawdown values over rolling 504d in peak_and_crash domain
def f01_peak_and_crash_dd_range_504d_slope_v150_signal(closeadj):
    dd = _peak_crash_drawdown(closeadj, 504)
    base = _max(dd, 504) - _min(dd, 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f01_peak_and_crash_drawdown_5d_slope_v001_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_5d_slope_v001_signal},
    "f01_peak_and_crash_recovery_5d_slope_v002_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_5d_slope_v002_signal},
    "f01_peak_and_crash_drawdown_z_5d_slope_v003_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_z_5d_slope_v003_signal},
    "f01_peak_and_crash_recovery_z_5d_slope_v004_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_z_5d_slope_v004_signal},
    "f01_peak_and_crash_rel_max_5d_slope_v005_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_max_5d_slope_v005_signal},
    "f01_peak_and_crash_rel_min_5d_slope_v006_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_min_5d_slope_v006_signal},
    "f01_peak_and_crash_drawdown_vol_5d_slope_v007_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_vol_5d_slope_v007_signal},
    "f01_peak_and_crash_recovery_vol_5d_slope_v008_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_vol_5d_slope_v008_signal},
    "f01_peak_and_crash_drawdown_mean_5d_slope_v009_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_mean_5d_slope_v009_signal},
    "f01_peak_and_crash_max_dd_5d_slope_v010_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_dd_5d_slope_v010_signal},
    "f01_peak_and_crash_max_rec_5d_slope_v011_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_rec_5d_slope_v011_signal},
    "f01_peak_and_crash_drawdown_10d_slope_v012_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_10d_slope_v012_signal},
    "f01_peak_and_crash_recovery_10d_slope_v013_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_10d_slope_v013_signal},
    "f01_peak_and_crash_drawdown_z_10d_slope_v014_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_z_10d_slope_v014_signal},
    "f01_peak_and_crash_recovery_z_10d_slope_v015_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_z_10d_slope_v015_signal},
    "f01_peak_and_crash_rel_max_10d_slope_v016_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_max_10d_slope_v016_signal},
    "f01_peak_and_crash_rel_min_10d_slope_v017_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_min_10d_slope_v017_signal},
    "f01_peak_and_crash_drawdown_vol_10d_slope_v018_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_vol_10d_slope_v018_signal},
    "f01_peak_and_crash_recovery_vol_10d_slope_v019_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_vol_10d_slope_v019_signal},
    "f01_peak_and_crash_drawdown_mean_10d_slope_v020_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_mean_10d_slope_v020_signal},
    "f01_peak_and_crash_max_dd_10d_slope_v021_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_dd_10d_slope_v021_signal},
    "f01_peak_and_crash_max_rec_10d_slope_v022_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_rec_10d_slope_v022_signal},
    "f01_peak_and_crash_drawdown_21d_slope_v023_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_21d_slope_v023_signal},
    "f01_peak_and_crash_recovery_21d_slope_v024_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_21d_slope_v024_signal},
    "f01_peak_and_crash_drawdown_z_21d_slope_v025_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_z_21d_slope_v025_signal},
    "f01_peak_and_crash_recovery_z_21d_slope_v026_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_z_21d_slope_v026_signal},
    "f01_peak_and_crash_rel_max_21d_slope_v027_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_max_21d_slope_v027_signal},
    "f01_peak_and_crash_rel_min_21d_slope_v028_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_min_21d_slope_v028_signal},
    "f01_peak_and_crash_drawdown_vol_21d_slope_v029_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_vol_21d_slope_v029_signal},
    "f01_peak_and_crash_recovery_vol_21d_slope_v030_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_vol_21d_slope_v030_signal},
    "f01_peak_and_crash_drawdown_mean_21d_slope_v031_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_mean_21d_slope_v031_signal},
    "f01_peak_and_crash_max_dd_21d_slope_v032_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_dd_21d_slope_v032_signal},
    "f01_peak_and_crash_max_rec_21d_slope_v033_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_rec_21d_slope_v033_signal},
    "f01_peak_and_crash_drawdown_63d_slope_v034_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_63d_slope_v034_signal},
    "f01_peak_and_crash_recovery_63d_slope_v035_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_63d_slope_v035_signal},
    "f01_peak_and_crash_drawdown_z_63d_slope_v036_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_63d_slope_v036_signal},
    "f01_peak_and_crash_recovery_z_63d_slope_v037_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_63d_slope_v037_signal},
    "f01_peak_and_crash_rel_max_63d_slope_v038_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_63d_slope_v038_signal},
    "f01_peak_and_crash_rel_min_63d_slope_v039_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_63d_slope_v039_signal},
    "f01_peak_and_crash_drawdown_vol_63d_slope_v040_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_63d_slope_v040_signal},
    "f01_peak_and_crash_recovery_vol_63d_slope_v041_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_63d_slope_v041_signal},
    "f01_peak_and_crash_drawdown_mean_63d_slope_v042_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_63d_slope_v042_signal},
    "f01_peak_and_crash_max_dd_63d_slope_v043_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_63d_slope_v043_signal},
    "f01_peak_and_crash_max_rec_63d_slope_v044_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_rec_63d_slope_v044_signal},
    "f01_peak_and_crash_drawdown_126d_slope_v045_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_126d_slope_v045_signal},
    "f01_peak_and_crash_recovery_126d_slope_v046_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_126d_slope_v046_signal},
    "f01_peak_and_crash_drawdown_z_126d_slope_v047_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_126d_slope_v047_signal},
    "f01_peak_and_crash_recovery_z_126d_slope_v048_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_126d_slope_v048_signal},
    "f01_peak_and_crash_rel_max_126d_slope_v049_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_126d_slope_v049_signal},
    "f01_peak_and_crash_rel_min_126d_slope_v050_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_126d_slope_v050_signal},
    "f01_peak_and_crash_drawdown_vol_126d_slope_v051_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_126d_slope_v051_signal},
    "f01_peak_and_crash_recovery_vol_126d_slope_v052_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_126d_slope_v052_signal},
    "f01_peak_and_crash_drawdown_mean_126d_slope_v053_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_126d_slope_v053_signal},
    "f01_peak_and_crash_max_dd_126d_slope_v054_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_126d_slope_v054_signal},
    "f01_peak_and_crash_max_rec_126d_slope_v055_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_rec_126d_slope_v055_signal},
    "f01_peak_and_crash_drawdown_252d_slope_v056_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_252d_slope_v056_signal},
    "f01_peak_and_crash_recovery_252d_slope_v057_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_252d_slope_v057_signal},
    "f01_peak_and_crash_drawdown_z_252d_slope_v058_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_252d_slope_v058_signal},
    "f01_peak_and_crash_recovery_z_252d_slope_v059_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_252d_slope_v059_signal},
    "f01_peak_and_crash_rel_max_252d_slope_v060_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_252d_slope_v060_signal},
    "f01_peak_and_crash_rel_min_252d_slope_v061_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_252d_slope_v061_signal},
    "f01_peak_and_crash_drawdown_vol_252d_slope_v062_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_252d_slope_v062_signal},
    "f01_peak_and_crash_recovery_vol_252d_slope_v063_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_252d_slope_v063_signal},
    "f01_peak_and_crash_drawdown_mean_252d_slope_v064_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_252d_slope_v064_signal},
    "f01_peak_and_crash_max_dd_252d_slope_v065_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_252d_slope_v065_signal},
    "f01_peak_and_crash_drawdown_504d_slope_v066_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_504d_slope_v066_signal},
    "f01_peak_and_crash_recovery_504d_slope_v067_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_504d_slope_v067_signal},
    "f01_peak_and_crash_drawdown_z_504d_slope_v068_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_504d_slope_v068_signal},
    "f01_peak_and_crash_recovery_z_504d_slope_v069_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_504d_slope_v069_signal},
    "f01_peak_and_crash_rel_max_504d_slope_v070_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_504d_slope_v070_signal},
    "f01_peak_and_crash_rel_min_504d_slope_v071_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_504d_slope_v071_signal},
    "f01_peak_and_crash_drawdown_vol_504d_slope_v072_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_504d_slope_v072_signal},
    "f01_peak_and_crash_recovery_vol_504d_slope_v073_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_504d_slope_v073_signal},
    "f01_peak_and_crash_drawdown_mean_504d_slope_v074_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_504d_slope_v074_signal},
    "f01_peak_and_crash_max_dd_504d_slope_v075_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_504d_slope_v075_signal},
    "f01_peak_and_crash_dd_ema_5d_slope_v076_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_ema_5d_slope_v076_signal},
    "f01_peak_and_crash_rec_ema_5d_slope_v077_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_ema_5d_slope_v077_signal},
    "f01_peak_and_crash_dd_atr_5d_slope_v078_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_dd_atr_5d_slope_v078_signal},
    "f01_peak_and_crash_rec_atr_5d_slope_v079_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_rec_atr_5d_slope_v079_signal},
    "f01_peak_and_crash_dd_count_5d_slope_v080_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_count_5d_slope_v080_signal},
    "f01_peak_and_crash_rec_count_5d_slope_v081_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_count_5d_slope_v081_signal},
    "f01_peak_and_crash_dd_vel_z_5d_slope_v082_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_vel_z_5d_slope_v082_signal},
    "f01_peak_and_crash_rec_vel_z_5d_slope_v083_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_vel_z_5d_slope_v083_signal},
    "f01_peak_and_crash_dd_range_5d_slope_v084_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_range_5d_slope_v084_signal},
    "f01_peak_and_crash_rec_range_5d_slope_v085_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_range_5d_slope_v085_signal},
    "f01_peak_and_crash_dd_accel_5d_slope_v086_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_accel_5d_slope_v086_signal},
    "f01_peak_and_crash_dd_ema_10d_slope_v087_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_ema_10d_slope_v087_signal},
    "f01_peak_and_crash_rec_ema_10d_slope_v088_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_ema_10d_slope_v088_signal},
    "f01_peak_and_crash_dd_atr_10d_slope_v089_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_dd_atr_10d_slope_v089_signal},
    "f01_peak_and_crash_rec_atr_10d_slope_v090_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_rec_atr_10d_slope_v090_signal},
    "f01_peak_and_crash_dd_count_10d_slope_v091_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_count_10d_slope_v091_signal},
    "f01_peak_and_crash_rec_count_10d_slope_v092_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_count_10d_slope_v092_signal},
    "f01_peak_and_crash_dd_vel_z_10d_slope_v093_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_vel_z_10d_slope_v093_signal},
    "f01_peak_and_crash_rec_vel_z_10d_slope_v094_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_vel_z_10d_slope_v094_signal},
    "f01_peak_and_crash_dd_range_10d_slope_v095_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_range_10d_slope_v095_signal},
    "f01_peak_and_crash_rec_range_10d_slope_v096_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_range_10d_slope_v096_signal},
    "f01_peak_and_crash_dd_accel_10d_slope_v097_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_accel_10d_slope_v097_signal},
    "f01_peak_and_crash_dd_ema_21d_slope_v098_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_ema_21d_slope_v098_signal},
    "f01_peak_and_crash_rec_ema_21d_slope_v099_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_ema_21d_slope_v099_signal},
    "f01_peak_and_crash_dd_atr_21d_slope_v100_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_dd_atr_21d_slope_v100_signal},
    "f01_peak_and_crash_rec_atr_21d_slope_v101_signal": {"inputs": ["high", "low", "close"], "func": f01_peak_and_crash_rec_atr_21d_slope_v101_signal},
    "f01_peak_and_crash_dd_count_21d_slope_v102_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_count_21d_slope_v102_signal},
    "f01_peak_and_crash_rec_count_21d_slope_v103_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_count_21d_slope_v103_signal},
    "f01_peak_and_crash_dd_vel_z_21d_slope_v104_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_vel_z_21d_slope_v104_signal},
    "f01_peak_and_crash_rec_vel_z_21d_slope_v105_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_vel_z_21d_slope_v105_signal},
    "f01_peak_and_crash_dd_range_21d_slope_v106_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_range_21d_slope_v106_signal},
    "f01_peak_and_crash_rec_range_21d_slope_v107_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rec_range_21d_slope_v107_signal},
    "f01_peak_and_crash_dd_accel_21d_slope_v108_signal": {"inputs": ["close"], "func": f01_peak_and_crash_dd_accel_21d_slope_v108_signal},
    "f01_peak_and_crash_dd_ema_63d_slope_v109_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_63d_slope_v109_signal},
    "f01_peak_and_crash_rec_ema_63d_slope_v110_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_63d_slope_v110_signal},
    "f01_peak_and_crash_dd_atr_63d_slope_v111_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_63d_slope_v111_signal},
    "f01_peak_and_crash_rec_atr_63d_slope_v112_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_63d_slope_v112_signal},
    "f01_peak_and_crash_dd_count_63d_slope_v113_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_63d_slope_v113_signal},
    "f01_peak_and_crash_rec_count_63d_slope_v114_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_63d_slope_v114_signal},
    "f01_peak_and_crash_dd_vel_z_63d_slope_v115_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_63d_slope_v115_signal},
    "f01_peak_and_crash_rec_vel_z_63d_slope_v116_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_63d_slope_v116_signal},
    "f01_peak_and_crash_dd_range_63d_slope_v117_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_63d_slope_v117_signal},
    "f01_peak_and_crash_rec_range_63d_slope_v118_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_range_63d_slope_v118_signal},
    "f01_peak_and_crash_dd_accel_63d_slope_v119_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_accel_63d_slope_v119_signal},
    "f01_peak_and_crash_dd_ema_126d_slope_v120_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_126d_slope_v120_signal},
    "f01_peak_and_crash_rec_ema_126d_slope_v121_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_126d_slope_v121_signal},
    "f01_peak_and_crash_dd_atr_126d_slope_v122_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_126d_slope_v122_signal},
    "f01_peak_and_crash_rec_atr_126d_slope_v123_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_126d_slope_v123_signal},
    "f01_peak_and_crash_dd_count_126d_slope_v124_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_126d_slope_v124_signal},
    "f01_peak_and_crash_rec_count_126d_slope_v125_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_126d_slope_v125_signal},
    "f01_peak_and_crash_dd_vel_z_126d_slope_v126_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_126d_slope_v126_signal},
    "f01_peak_and_crash_rec_vel_z_126d_slope_v127_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_126d_slope_v127_signal},
    "f01_peak_and_crash_dd_range_126d_slope_v128_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_126d_slope_v128_signal},
    "f01_peak_and_crash_rec_range_126d_slope_v129_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_range_126d_slope_v129_signal},
    "f01_peak_and_crash_dd_accel_126d_slope_v130_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_accel_126d_slope_v130_signal},
    "f01_peak_and_crash_dd_ema_252d_slope_v131_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_252d_slope_v131_signal},
    "f01_peak_and_crash_rec_ema_252d_slope_v132_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_252d_slope_v132_signal},
    "f01_peak_and_crash_dd_atr_252d_slope_v133_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_252d_slope_v133_signal},
    "f01_peak_and_crash_rec_atr_252d_slope_v134_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_252d_slope_v134_signal},
    "f01_peak_and_crash_dd_count_252d_slope_v135_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_252d_slope_v135_signal},
    "f01_peak_and_crash_rec_count_252d_slope_v136_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_252d_slope_v136_signal},
    "f01_peak_and_crash_dd_vel_z_252d_slope_v137_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_252d_slope_v137_signal},
    "f01_peak_and_crash_rec_vel_z_252d_slope_v138_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_252d_slope_v138_signal},
    "f01_peak_and_crash_dd_range_252d_slope_v139_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_252d_slope_v139_signal},
    "f01_peak_and_crash_rec_range_252d_slope_v140_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_range_252d_slope_v140_signal},
    "f01_peak_and_crash_dd_accel_252d_slope_v141_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_accel_252d_slope_v141_signal},
    "f01_peak_and_crash_dd_ema_504d_slope_v142_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_ema_504d_slope_v142_signal},
    "f01_peak_and_crash_rec_ema_504d_slope_v143_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_ema_504d_slope_v143_signal},
    "f01_peak_and_crash_dd_atr_504d_slope_v144_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_dd_atr_504d_slope_v144_signal},
    "f01_peak_and_crash_rec_atr_504d_slope_v145_signal": {"inputs": ["high", "low", "close", "closeadj"], "func": f01_peak_and_crash_rec_atr_504d_slope_v145_signal},
    "f01_peak_and_crash_dd_count_504d_slope_v146_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_count_504d_slope_v146_signal},
    "f01_peak_and_crash_rec_count_504d_slope_v147_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_count_504d_slope_v147_signal},
    "f01_peak_and_crash_dd_vel_z_504d_slope_v148_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_vel_z_504d_slope_v148_signal},
    "f01_peak_and_crash_rec_vel_z_504d_slope_v149_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rec_vel_z_504d_slope_v149_signal},
    "f01_peak_and_crash_dd_range_504d_slope_v150_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_dd_range_504d_slope_v150_signal},
}

F01_PEAK_AND_CRASH_REGISTRY_SLOPE = REGISTRY

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
        assert q.nunique() > 50 or "count" in name or "range" in name or "max_dd" in name or "max_rec" in name
        assert q.std() > 0
        assert not q.isna().all()
        source = inspect.getsource(info["func"])
        assert "_peak_crash_" in source
    print("All tests passed!")
