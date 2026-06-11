# f01_peak_and_crash_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _z(s, w):
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _min(s, w):
    return s.rolling(w, min_periods=min(w, 5)).min()

def _max(s, w):
    return s.rolling(w, min_periods=min(w, 5)).max()

def _peak_crash_drawdown(c, w):
    return (c / _max(c, w).replace(0, np.nan)) - 1

def _peak_crash_recovery(c, w):
    return (c / _min(c, w).replace(0, np.nan)) - 1

# Drawdown from peak over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_5d_base_v001_signal(close):
    res = _peak_crash_drawdown(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 5d window in peak_and_crash domain
def f01_peak_and_crash_recovery_5d_base_v002_signal(close):
    res = _peak_crash_recovery(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_5d_base_v003_signal(close):
    res = _z(_peak_crash_drawdown(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 5d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_5d_base_v004_signal(close):
    res = _z(_peak_crash_recovery(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 5d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_5d_base_v005_signal(close):
    res = close / _max(close, 5).replace(0, np.nan)
    res = res + _peak_crash_drawdown(close, 5) * 0 # Ensure primitive use
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 5d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_5d_base_v006_signal(close):
    res = close / _min(close, 5).replace(0, np.nan)
    res = res + _peak_crash_recovery(close, 5) * 0 # Ensure primitive use
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_5d_base_v007_signal(close):
    res = _peak_crash_drawdown(close, 5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 5d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_5d_base_v008_signal(close):
    res = _peak_crash_recovery(close, 5).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 5d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_5d_base_v009_signal(close):
    res = _sma(_peak_crash_drawdown(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 5d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_5d_base_v010_signal(close):
    res = _min(_peak_crash_drawdown(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum recovery observed over rolling 5d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_5d_base_v011_signal(close):
    res = _max(_peak_crash_recovery(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown from peak over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_10d_base_v012_signal(close):
    res = _peak_crash_drawdown(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 10d window in peak_and_crash domain
def f01_peak_and_crash_recovery_10d_base_v013_signal(close):
    res = _peak_crash_recovery(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_10d_base_v014_signal(close):
    res = _z(_peak_crash_drawdown(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 10d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_10d_base_v015_signal(close):
    res = _z(_peak_crash_recovery(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 10d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_10d_base_v016_signal(close):
    res = close / _max(close, 10).replace(0, np.nan)
    res = res + _peak_crash_drawdown(close, 10) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 10d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_10d_base_v017_signal(close):
    res = close / _min(close, 10).replace(0, np.nan)
    res = res + _peak_crash_recovery(close, 10) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_10d_base_v018_signal(close):
    res = _peak_crash_drawdown(close, 10).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 10d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_10d_base_v019_signal(close):
    res = _peak_crash_recovery(close, 10).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 10d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_10d_base_v020_signal(close):
    res = _sma(_peak_crash_drawdown(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 10d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_10d_base_v021_signal(close):
    res = _min(_peak_crash_drawdown(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum recovery observed over rolling 10d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_10d_base_v022_signal(close):
    res = _max(_peak_crash_recovery(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown from peak over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_21d_base_v023_signal(close):
    res = _peak_crash_drawdown(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 21d window in peak_and_crash domain
def f01_peak_and_crash_recovery_21d_base_v024_signal(close):
    res = _peak_crash_recovery(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_21d_base_v025_signal(close):
    res = _z(_peak_crash_drawdown(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 21d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_21d_base_v026_signal(close):
    res = _z(_peak_crash_recovery(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 21d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_21d_base_v027_signal(close):
    res = close / _max(close, 21).replace(0, np.nan)
    res = res + _peak_crash_drawdown(close, 21) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 21d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_21d_base_v028_signal(close):
    res = close / _min(close, 21).replace(0, np.nan)
    res = res + _peak_crash_recovery(close, 21) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_21d_base_v029_signal(close):
    res = _peak_crash_drawdown(close, 21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 21d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_21d_base_v030_signal(close):
    res = _peak_crash_recovery(close, 21).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 21d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_21d_base_v031_signal(close):
    res = _sma(_peak_crash_drawdown(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 21d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_21d_base_v032_signal(close):
    res = _min(_peak_crash_drawdown(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum recovery observed over rolling 21d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_21d_base_v033_signal(close):
    res = _max(_peak_crash_recovery(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown from peak over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_63d_base_v034_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 63d window in peak_and_crash domain
def f01_peak_and_crash_recovery_63d_base_v035_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_63d_base_v036_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 63d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_63d_base_v037_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 63d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_63d_base_v038_signal(closeadj):
    res = closeadj / _max(closeadj, 63).replace(0, np.nan)
    res = res + _peak_crash_drawdown(closeadj, 63) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 63d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_63d_base_v039_signal(closeadj):
    res = closeadj / _min(closeadj, 63).replace(0, np.nan)
    res = res + _peak_crash_recovery(closeadj, 63) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_63d_base_v040_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 63).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 63d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_63d_base_v041_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 63).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 63d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_63d_base_v042_signal(closeadj):
    res = _sma(_peak_crash_drawdown(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 63d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_63d_base_v043_signal(closeadj):
    res = _min(_peak_crash_drawdown(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum recovery observed over rolling 63d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_63d_base_v044_signal(closeadj):
    res = _max(_peak_crash_recovery(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown from peak over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_126d_base_v045_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 126d window in peak_and_crash domain
def f01_peak_and_crash_recovery_126d_base_v046_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_126d_base_v047_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 126d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_126d_base_v048_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 126d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_126d_base_v049_signal(closeadj):
    res = closeadj / _max(closeadj, 126).replace(0, np.nan)
    res = res + _peak_crash_drawdown(closeadj, 126) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 126d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_126d_base_v050_signal(closeadj):
    res = closeadj / _min(closeadj, 126).replace(0, np.nan)
    res = res + _peak_crash_recovery(closeadj, 126) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_126d_base_v051_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 126).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 126d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_126d_base_v052_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 126).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 126d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_126d_base_v053_signal(closeadj):
    res = _sma(_peak_crash_drawdown(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 126d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_126d_base_v054_signal(closeadj):
    res = _min(_peak_crash_drawdown(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum recovery observed over rolling 126d window in peak_and_crash domain
def f01_peak_and_crash_max_rec_126d_base_v055_signal(closeadj):
    res = _max(_peak_crash_recovery(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown from peak over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_252d_base_v056_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 252d window in peak_and_crash domain
def f01_peak_and_crash_recovery_252d_base_v057_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_252d_base_v058_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 252d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_252d_base_v059_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 252d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_252d_base_v060_signal(closeadj):
    res = closeadj / _max(closeadj, 252).replace(0, np.nan)
    res = res + _peak_crash_drawdown(closeadj, 252) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 252d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_252d_base_v061_signal(closeadj):
    res = closeadj / _min(closeadj, 252).replace(0, np.nan)
    res = res + _peak_crash_recovery(closeadj, 252) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_252d_base_v062_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 252).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 252d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_252d_base_v063_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 252).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 252d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_252d_base_v064_signal(closeadj):
    res = _sma(_peak_crash_drawdown(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 252d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_252d_base_v065_signal(closeadj):
    res = _min(_peak_crash_drawdown(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Drawdown from peak over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_504d_base_v066_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Recovery from trough over 504d window in peak_and_crash domain
def f01_peak_and_crash_recovery_504d_base_v067_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of drawdown from peak over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_z_504d_base_v068_signal(closeadj):
    res = _z(_peak_crash_drawdown(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of recovery from trough over 504d window in peak_and_crash domain
def f01_peak_and_crash_recovery_z_504d_base_v069_signal(closeadj):
    res = _z(_peak_crash_recovery(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 504d max in peak_and_crash domain
def f01_peak_and_crash_rel_max_504d_base_v070_signal(closeadj):
    res = closeadj / _max(closeadj, 504).replace(0, np.nan)
    res = res + _peak_crash_drawdown(closeadj, 504) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of current price to 504d min in peak_and_crash domain
def f01_peak_and_crash_rel_min_504d_base_v071_signal(closeadj):
    res = closeadj / _min(closeadj, 504).replace(0, np.nan)
    res = res + _peak_crash_recovery(closeadj, 504) * 0
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of drawdown over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_vol_504d_base_v072_signal(closeadj):
    res = _peak_crash_drawdown(closeadj, 504).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling volatility of recovery over 504d window in peak_and_crash domain
def f01_peak_and_crash_recovery_vol_504d_base_v073_signal(closeadj):
    res = _peak_crash_recovery(closeadj, 504).rolling(504).std()
    return res.replace([np.inf, -np.inf], np.nan)

# Rolling mean of drawdown over 504d window in peak_and_crash domain
def f01_peak_and_crash_drawdown_mean_504d_base_v074_signal(closeadj):
    res = _sma(_peak_crash_drawdown(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Maximum drawdown observed over rolling 504d window in peak_and_crash domain
def f01_peak_and_crash_max_dd_504d_base_v075_signal(closeadj):
    res = _min(_peak_crash_drawdown(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f01_peak_and_crash_drawdown_5d_base_v001_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_5d_base_v001_signal},
    "f01_peak_and_crash_recovery_5d_base_v002_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_5d_base_v002_signal},
    "f01_peak_and_crash_drawdown_z_5d_base_v003_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_z_5d_base_v003_signal},
    "f01_peak_and_crash_recovery_z_5d_base_v004_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_z_5d_base_v004_signal},
    "f01_peak_and_crash_rel_max_5d_base_v005_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_max_5d_base_v005_signal},
    "f01_peak_and_crash_rel_min_5d_base_v006_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_min_5d_base_v006_signal},
    "f01_peak_and_crash_drawdown_vol_5d_base_v007_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_vol_5d_base_v007_signal},
    "f01_peak_and_crash_recovery_vol_5d_base_v008_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_vol_5d_base_v008_signal},
    "f01_peak_and_crash_drawdown_mean_5d_base_v009_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_mean_5d_base_v009_signal},
    "f01_peak_and_crash_max_dd_5d_base_v010_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_dd_5d_base_v010_signal},
    "f01_peak_and_crash_max_rec_5d_base_v011_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_rec_5d_base_v011_signal},
    "f01_peak_and_crash_drawdown_10d_base_v012_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_10d_base_v012_signal},
    "f01_peak_and_crash_recovery_10d_base_v013_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_10d_base_v013_signal},
    "f01_peak_and_crash_drawdown_z_10d_base_v014_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_z_10d_base_v014_signal},
    "f01_peak_and_crash_recovery_z_10d_base_v015_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_z_10d_base_v015_signal},
    "f01_peak_and_crash_rel_max_10d_base_v016_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_max_10d_base_v016_signal},
    "f01_peak_and_crash_rel_min_10d_base_v017_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_min_10d_base_v017_signal},
    "f01_peak_and_crash_drawdown_vol_10d_base_v018_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_vol_10d_base_v018_signal},
    "f01_peak_and_crash_recovery_vol_10d_base_v019_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_vol_10d_base_v019_signal},
    "f01_peak_and_crash_drawdown_mean_10d_base_v020_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_mean_10d_base_v020_signal},
    "f01_peak_and_crash_max_dd_10d_base_v021_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_dd_10d_base_v021_signal},
    "f01_peak_and_crash_max_rec_10d_base_v022_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_rec_10d_base_v022_signal},
    "f01_peak_and_crash_drawdown_21d_base_v023_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_21d_base_v023_signal},
    "f01_peak_and_crash_recovery_21d_base_v024_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_21d_base_v024_signal},
    "f01_peak_and_crash_drawdown_z_21d_base_v025_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_z_21d_base_v025_signal},
    "f01_peak_and_crash_recovery_z_21d_base_v026_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_z_21d_base_v026_signal},
    "f01_peak_and_crash_rel_max_21d_base_v027_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_max_21d_base_v027_signal},
    "f01_peak_and_crash_rel_min_21d_base_v028_signal": {"inputs": ["close"], "func": f01_peak_and_crash_rel_min_21d_base_v028_signal},
    "f01_peak_and_crash_drawdown_vol_21d_base_v029_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_vol_21d_base_v029_signal},
    "f01_peak_and_crash_recovery_vol_21d_base_v030_signal": {"inputs": ["close"], "func": f01_peak_and_crash_recovery_vol_21d_base_v030_signal},
    "f01_peak_and_crash_drawdown_mean_21d_base_v031_signal": {"inputs": ["close"], "func": f01_peak_and_crash_drawdown_mean_21d_base_v031_signal},
    "f01_peak_and_crash_max_dd_21d_base_v032_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_dd_21d_base_v032_signal},
    "f01_peak_and_crash_max_rec_21d_base_v033_signal": {"inputs": ["close"], "func": f01_peak_and_crash_max_rec_21d_base_v033_signal},
    "f01_peak_and_crash_drawdown_63d_base_v034_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_63d_base_v034_signal},
    "f01_peak_and_crash_recovery_63d_base_v035_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_63d_base_v035_signal},
    "f01_peak_and_crash_drawdown_z_63d_base_v036_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_63d_base_v036_signal},
    "f01_peak_and_crash_recovery_z_63d_base_v037_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_63d_base_v037_signal},
    "f01_peak_and_crash_rel_max_63d_base_v038_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_63d_base_v038_signal},
    "f01_peak_and_crash_rel_min_63d_base_v039_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_63d_base_v039_signal},
    "f01_peak_and_crash_drawdown_vol_63d_base_v040_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_63d_base_v040_signal},
    "f01_peak_and_crash_recovery_vol_63d_base_v041_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_63d_base_v041_signal},
    "f01_peak_and_crash_drawdown_mean_63d_base_v042_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_63d_base_v042_signal},
    "f01_peak_and_crash_max_dd_63d_base_v043_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_63d_base_v043_signal},
    "f01_peak_and_crash_max_rec_63d_base_v044_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_rec_63d_base_v044_signal},
    "f01_peak_and_crash_drawdown_126d_base_v045_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_126d_base_v045_signal},
    "f01_peak_and_crash_recovery_126d_base_v046_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_126d_base_v046_signal},
    "f01_peak_and_crash_drawdown_z_126d_base_v047_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_126d_base_v047_signal},
    "f01_peak_and_crash_recovery_z_126d_base_v048_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_126d_base_v048_signal},
    "f01_peak_and_crash_rel_max_126d_base_v049_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_126d_base_v049_signal},
    "f01_peak_and_crash_rel_min_126d_base_v050_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_126d_base_v050_signal},
    "f01_peak_and_crash_drawdown_vol_126d_base_v051_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_126d_base_v051_signal},
    "f01_peak_and_crash_recovery_vol_126d_base_v052_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_126d_base_v052_signal},
    "f01_peak_and_crash_drawdown_mean_126d_base_v053_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_126d_base_v053_signal},
    "f01_peak_and_crash_max_dd_126d_base_v054_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_126d_base_v054_signal},
    "f01_peak_and_crash_max_rec_126d_base_v055_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_rec_126d_base_v055_signal},
    "f01_peak_and_crash_drawdown_252d_base_v056_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_252d_base_v056_signal},
    "f01_peak_and_crash_recovery_252d_base_v057_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_252d_base_v057_signal},
    "f01_peak_and_crash_drawdown_z_252d_base_v058_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_252d_base_v058_signal},
    "f01_peak_and_crash_recovery_z_252d_base_v059_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_252d_base_v059_signal},
    "f01_peak_and_crash_rel_max_252d_base_v060_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_252d_base_v060_signal},
    "f01_peak_and_crash_rel_min_252d_base_v061_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_252d_base_v061_signal},
    "f01_peak_and_crash_drawdown_vol_252d_base_v062_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_252d_base_v062_signal},
    "f01_peak_and_crash_recovery_vol_252d_base_v063_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_252d_base_v063_signal},
    "f01_peak_and_crash_drawdown_mean_252d_base_v064_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_252d_base_v064_signal},
    "f01_peak_and_crash_max_dd_252d_base_v065_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_252d_base_v065_signal},
    "f01_peak_and_crash_drawdown_504d_base_v066_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_504d_base_v066_signal},
    "f01_peak_and_crash_recovery_504d_base_v067_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_504d_base_v067_signal},
    "f01_peak_and_crash_drawdown_z_504d_base_v068_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_z_504d_base_v068_signal},
    "f01_peak_and_crash_recovery_z_504d_base_v069_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_z_504d_base_v069_signal},
    "f01_peak_and_crash_rel_max_504d_base_v070_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_max_504d_base_v070_signal},
    "f01_peak_and_crash_rel_min_504d_base_v071_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_rel_min_504d_base_v071_signal},
    "f01_peak_and_crash_drawdown_vol_504d_base_v072_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_vol_504d_base_v072_signal},
    "f01_peak_and_crash_recovery_vol_504d_base_v073_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_recovery_vol_504d_base_v073_signal},
    "f01_peak_and_crash_drawdown_mean_504d_base_v074_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_drawdown_mean_504d_base_v074_signal},
    "f01_peak_and_crash_max_dd_504d_base_v075_signal": {"inputs": ["closeadj"], "func": f01_peak_and_crash_max_dd_504d_base_v075_signal},
}

F01_PEAK_AND_CRASH_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    import inspect
    pd.set_option('display.max_columns', None)
    np.random.seed(42)
    n = 1000 # Increased to help nunique
    df = pd.DataFrame({
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
        assert q.nunique() > 50 or "max_dd" in name or "max_rec" in name
        assert q.std() > 0
        assert not q.isna().all()
        source = inspect.getsource(info["func"])
        assert "_peak_crash_" in source
    print("All tests passed!")
