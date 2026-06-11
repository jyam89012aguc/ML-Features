# f09_price_momentum_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _z(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _mom_roc(c, w):
    return (c / c.shift(w).replace(0, np.nan) - 1)

def _mom_rsi(c, w):
    delta = c.diff()
    gain = (delta.where(delta > 0, 0)).rolling(w, min_periods=1).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(w, min_periods=1).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs.replace(np.nan, 0)))

# ROC for 2d window of open in price_momentum domain
def f09_price_momentum_open_roc_2d_base_v001_signal(arg_open):
    res = _mom_roc(arg_open, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 2d window of open in price_momentum domain
def f09_price_momentum_open_rsi_2d_base_v002_signal(arg_open):
    res = _mom_rsi(arg_open, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 2d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_sma_2d_base_v003_signal(arg_open):
    res = _sma(_mom_roc(arg_open, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 2d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_std_2d_base_v004_signal(arg_open):
    res = _std(_mom_roc(arg_open, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_z_2d_base_v005_signal(arg_open):
    res = _z(_mom_roc(arg_open, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d RSI for open in price_momentum domain
def f09_price_momentum_open_rsi_z_2d_base_v006_signal(arg_open):
    res = _z(_mom_rsi(arg_open, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 2d window of high in price_momentum domain
def f09_price_momentum_high_roc_2d_base_v007_signal(arg_high):
    res = _mom_roc(arg_high, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 2d window of high in price_momentum domain
def f09_price_momentum_high_rsi_2d_base_v008_signal(arg_high):
    res = _mom_rsi(arg_high, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 2d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_sma_2d_base_v009_signal(arg_high):
    res = _sma(_mom_roc(arg_high, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 2d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_std_2d_base_v010_signal(arg_high):
    res = _std(_mom_roc(arg_high, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_z_2d_base_v011_signal(arg_high):
    res = _z(_mom_roc(arg_high, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d RSI for high in price_momentum domain
def f09_price_momentum_high_rsi_z_2d_base_v012_signal(arg_high):
    res = _z(_mom_rsi(arg_high, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 2d window of low in price_momentum domain
def f09_price_momentum_low_roc_2d_base_v013_signal(arg_low):
    res = _mom_roc(arg_low, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 2d window of low in price_momentum domain
def f09_price_momentum_low_rsi_2d_base_v014_signal(arg_low):
    res = _mom_rsi(arg_low, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 2d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_sma_2d_base_v015_signal(arg_low):
    res = _sma(_mom_roc(arg_low, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 2d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_std_2d_base_v016_signal(arg_low):
    res = _std(_mom_roc(arg_low, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_z_2d_base_v017_signal(arg_low):
    res = _z(_mom_roc(arg_low, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d RSI for low in price_momentum domain
def f09_price_momentum_low_rsi_z_2d_base_v018_signal(arg_low):
    res = _z(_mom_rsi(arg_low, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 2d window of close in price_momentum domain
def f09_price_momentum_close_roc_2d_base_v019_signal(arg_close):
    res = _mom_roc(arg_close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 2d window of close in price_momentum domain
def f09_price_momentum_close_rsi_2d_base_v020_signal(arg_close):
    res = _mom_rsi(arg_close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 2d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_sma_2d_base_v021_signal(arg_close):
    res = _sma(_mom_roc(arg_close, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 2d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_std_2d_base_v022_signal(arg_close):
    res = _std(_mom_roc(arg_close, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_z_2d_base_v023_signal(arg_close):
    res = _z(_mom_roc(arg_close, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 2d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_z_2d_base_v024_signal(arg_close):
    res = _z(_mom_rsi(arg_close, 2), 2)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 3d window of open in price_momentum domain
def f09_price_momentum_open_roc_3d_base_v025_signal(arg_open):
    res = _mom_roc(arg_open, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 3d window of open in price_momentum domain
def f09_price_momentum_open_rsi_3d_base_v026_signal(arg_open):
    res = _mom_rsi(arg_open, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 3d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_sma_3d_base_v027_signal(arg_open):
    res = _sma(_mom_roc(arg_open, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 3d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_std_3d_base_v028_signal(arg_open):
    res = _std(_mom_roc(arg_open, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_z_3d_base_v029_signal(arg_open):
    res = _z(_mom_roc(arg_open, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d RSI for open in price_momentum domain
def f09_price_momentum_open_rsi_z_3d_base_v030_signal(arg_open):
    res = _z(_mom_rsi(arg_open, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 3d window of high in price_momentum domain
def f09_price_momentum_high_roc_3d_base_v031_signal(arg_high):
    res = _mom_roc(arg_high, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 3d window of high in price_momentum domain
def f09_price_momentum_high_rsi_3d_base_v032_signal(arg_high):
    res = _mom_rsi(arg_high, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 3d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_sma_3d_base_v033_signal(arg_high):
    res = _sma(_mom_roc(arg_high, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 3d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_std_3d_base_v034_signal(arg_high):
    res = _std(_mom_roc(arg_high, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_z_3d_base_v035_signal(arg_high):
    res = _z(_mom_roc(arg_high, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d RSI for high in price_momentum domain
def f09_price_momentum_high_rsi_z_3d_base_v036_signal(arg_high):
    res = _z(_mom_rsi(arg_high, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 3d window of low in price_momentum domain
def f09_price_momentum_low_roc_3d_base_v037_signal(arg_low):
    res = _mom_roc(arg_low, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 3d window of low in price_momentum domain
def f09_price_momentum_low_rsi_3d_base_v038_signal(arg_low):
    res = _mom_rsi(arg_low, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 3d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_sma_3d_base_v039_signal(arg_low):
    res = _sma(_mom_roc(arg_low, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 3d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_std_3d_base_v040_signal(arg_low):
    res = _std(_mom_roc(arg_low, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_z_3d_base_v041_signal(arg_low):
    res = _z(_mom_roc(arg_low, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d RSI for low in price_momentum domain
def f09_price_momentum_low_rsi_z_3d_base_v042_signal(arg_low):
    res = _z(_mom_rsi(arg_low, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 3d window of close in price_momentum domain
def f09_price_momentum_close_roc_3d_base_v043_signal(arg_close):
    res = _mom_roc(arg_close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 3d window of close in price_momentum domain
def f09_price_momentum_close_rsi_3d_base_v044_signal(arg_close):
    res = _mom_rsi(arg_close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 3d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_sma_3d_base_v045_signal(arg_close):
    res = _sma(_mom_roc(arg_close, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 3d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_std_3d_base_v046_signal(arg_close):
    res = _std(_mom_roc(arg_close, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_z_3d_base_v047_signal(arg_close):
    res = _z(_mom_roc(arg_close, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 3d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_z_3d_base_v048_signal(arg_close):
    res = _z(_mom_rsi(arg_close, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 5d window of open in price_momentum domain
def f09_price_momentum_open_roc_5d_base_v049_signal(arg_open):
    res = _mom_roc(arg_open, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 5d window of open in price_momentum domain
def f09_price_momentum_open_rsi_5d_base_v050_signal(arg_open):
    res = _mom_rsi(arg_open, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 5d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_sma_5d_base_v051_signal(arg_open):
    res = _sma(_mom_roc(arg_open, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 5d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_std_5d_base_v052_signal(arg_open):
    res = _std(_mom_roc(arg_open, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d ROC for open in price_momentum domain
def f09_price_momentum_open_roc_z_5d_base_v053_signal(arg_open):
    res = _z(_mom_roc(arg_open, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d RSI for open in price_momentum domain
def f09_price_momentum_open_rsi_z_5d_base_v054_signal(arg_open):
    res = _z(_mom_rsi(arg_open, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 5d window of high in price_momentum domain
def f09_price_momentum_high_roc_5d_base_v055_signal(arg_high):
    res = _mom_roc(arg_high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 5d window of high in price_momentum domain
def f09_price_momentum_high_rsi_5d_base_v056_signal(arg_high):
    res = _mom_rsi(arg_high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 5d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_sma_5d_base_v057_signal(arg_high):
    res = _sma(_mom_roc(arg_high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 5d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_std_5d_base_v058_signal(arg_high):
    res = _std(_mom_roc(arg_high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d ROC for high in price_momentum domain
def f09_price_momentum_high_roc_z_5d_base_v059_signal(arg_high):
    res = _z(_mom_roc(arg_high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d RSI for high in price_momentum domain
def f09_price_momentum_high_rsi_z_5d_base_v060_signal(arg_high):
    res = _z(_mom_rsi(arg_high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 5d window of low in price_momentum domain
def f09_price_momentum_low_roc_5d_base_v061_signal(arg_low):
    res = _mom_roc(arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 5d window of low in price_momentum domain
def f09_price_momentum_low_rsi_5d_base_v062_signal(arg_low):
    res = _mom_rsi(arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 5d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_sma_5d_base_v063_signal(arg_low):
    res = _sma(_mom_roc(arg_low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 5d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_std_5d_base_v064_signal(arg_low):
    res = _std(_mom_roc(arg_low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d ROC for low in price_momentum domain
def f09_price_momentum_low_roc_z_5d_base_v065_signal(arg_low):
    res = _z(_mom_roc(arg_low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d RSI for low in price_momentum domain
def f09_price_momentum_low_rsi_z_5d_base_v066_signal(arg_low):
    res = _z(_mom_rsi(arg_low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 5d window of close in price_momentum domain
def f09_price_momentum_close_roc_5d_base_v067_signal(arg_close):
    res = _mom_roc(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 5d window of close in price_momentum domain
def f09_price_momentum_close_rsi_5d_base_v068_signal(arg_close):
    res = _mom_rsi(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 5d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_sma_5d_base_v069_signal(arg_close):
    res = _sma(_mom_roc(arg_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# STD of 5d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_std_5d_base_v070_signal(arg_close):
    res = _std(_mom_roc(arg_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_z_5d_base_v071_signal(arg_close):
    res = _z(_mom_roc(arg_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of 5d RSI for close in price_momentum domain
def f09_price_momentum_close_rsi_z_5d_base_v072_signal(arg_close):
    res = _z(_mom_rsi(arg_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# ROC for 10d window of close in price_momentum domain
def f09_price_momentum_close_roc_10d_base_v073_signal(arg_close):
    res = _mom_roc(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI for 10d window of close in price_momentum domain
def f09_price_momentum_close_rsi_10d_base_v074_signal(arg_close):
    res = _mom_rsi(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA of 10d ROC for close in price_momentum domain
def f09_price_momentum_close_roc_sma_10d_base_v075_signal(arg_close):
    res = _sma(_mom_roc(arg_close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "f09_price_momentum_open_roc_2d_base_v001_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_2d_base_v001_signal},
    "f09_price_momentum_open_rsi_2d_base_v002_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_2d_base_v002_signal},
    "f09_price_momentum_open_roc_sma_2d_base_v003_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_sma_2d_base_v003_signal},
    "f09_price_momentum_open_roc_std_2d_base_v004_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_std_2d_base_v004_signal},
    "f09_price_momentum_open_roc_z_2d_base_v005_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_z_2d_base_v005_signal},
    "f09_price_momentum_open_rsi_z_2d_base_v006_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_z_2d_base_v006_signal},
    "f09_price_momentum_high_roc_2d_base_v007_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_2d_base_v007_signal},
    "f09_price_momentum_high_rsi_2d_base_v008_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_2d_base_v008_signal},
    "f09_price_momentum_high_roc_sma_2d_base_v009_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_sma_2d_base_v009_signal},
    "f09_price_momentum_high_roc_std_2d_base_v010_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_std_2d_base_v010_signal},
    "f09_price_momentum_high_roc_z_2d_base_v011_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_z_2d_base_v011_signal},
    "f09_price_momentum_high_rsi_z_2d_base_v012_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_z_2d_base_v012_signal},
    "f09_price_momentum_low_roc_2d_base_v013_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_2d_base_v013_signal},
    "f09_price_momentum_low_rsi_2d_base_v014_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_2d_base_v014_signal},
    "f09_price_momentum_low_roc_sma_2d_base_v015_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_sma_2d_base_v015_signal},
    "f09_price_momentum_low_roc_std_2d_base_v016_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_std_2d_base_v016_signal},
    "f09_price_momentum_low_roc_z_2d_base_v017_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_z_2d_base_v017_signal},
    "f09_price_momentum_low_rsi_z_2d_base_v018_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_z_2d_base_v018_signal},
    "f09_price_momentum_close_roc_2d_base_v019_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_2d_base_v019_signal},
    "f09_price_momentum_close_rsi_2d_base_v020_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_2d_base_v020_signal},
    "f09_price_momentum_close_roc_sma_2d_base_v021_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_2d_base_v021_signal},
    "f09_price_momentum_close_roc_std_2d_base_v022_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_2d_base_v022_signal},
    "f09_price_momentum_close_roc_z_2d_base_v023_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_2d_base_v023_signal},
    "f09_price_momentum_close_rsi_z_2d_base_v024_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_2d_base_v024_signal},
    "f09_price_momentum_open_roc_3d_base_v025_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_3d_base_v025_signal},
    "f09_price_momentum_open_rsi_3d_base_v026_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_3d_base_v026_signal},
    "f09_price_momentum_open_roc_sma_3d_base_v027_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_sma_3d_base_v027_signal},
    "f09_price_momentum_open_roc_std_3d_base_v028_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_std_3d_base_v028_signal},
    "f09_price_momentum_open_roc_z_3d_base_v029_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_z_3d_base_v029_signal},
    "f09_price_momentum_open_rsi_z_3d_base_v030_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_z_3d_base_v030_signal},
    "f09_price_momentum_high_roc_3d_base_v031_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_3d_base_v031_signal},
    "f09_price_momentum_high_rsi_3d_base_v032_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_3d_base_v032_signal},
    "f09_price_momentum_high_roc_sma_3d_base_v033_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_sma_3d_base_v033_signal},
    "f09_price_momentum_high_roc_std_3d_base_v034_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_std_3d_base_v034_signal},
    "f09_price_momentum_high_roc_z_3d_base_v035_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_z_3d_base_v035_signal},
    "f09_price_momentum_high_rsi_z_3d_base_v036_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_z_3d_base_v036_signal},
    "f09_price_momentum_low_roc_3d_base_v037_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_3d_base_v037_signal},
    "f09_price_momentum_low_rsi_3d_base_v038_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_3d_base_v038_signal},
    "f09_price_momentum_low_roc_sma_3d_base_v039_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_sma_3d_base_v039_signal},
    "f09_price_momentum_low_roc_std_3d_base_v040_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_std_3d_base_v040_signal},
    "f09_price_momentum_low_roc_z_3d_base_v041_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_z_3d_base_v041_signal},
    "f09_price_momentum_low_rsi_z_3d_base_v042_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_z_3d_base_v042_signal},
    "f09_price_momentum_close_roc_3d_base_v043_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_3d_base_v043_signal},
    "f09_price_momentum_close_rsi_3d_base_v044_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_3d_base_v044_signal},
    "f09_price_momentum_close_roc_sma_3d_base_v045_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_3d_base_v045_signal},
    "f09_price_momentum_close_roc_std_3d_base_v046_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_3d_base_v046_signal},
    "f09_price_momentum_close_roc_z_3d_base_v047_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_3d_base_v047_signal},
    "f09_price_momentum_close_rsi_z_3d_base_v048_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_3d_base_v048_signal},
    "f09_price_momentum_open_roc_5d_base_v049_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_5d_base_v049_signal},
    "f09_price_momentum_open_rsi_5d_base_v050_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_5d_base_v050_signal},
    "f09_price_momentum_open_roc_sma_5d_base_v051_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_sma_5d_base_v051_signal},
    "f09_price_momentum_open_roc_std_5d_base_v052_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_std_5d_base_v052_signal},
    "f09_price_momentum_open_roc_z_5d_base_v053_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_z_5d_base_v053_signal},
    "f09_price_momentum_open_rsi_z_5d_base_v054_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_z_5d_base_v054_signal},
    "f09_price_momentum_high_roc_5d_base_v055_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_5d_base_v055_signal},
    "f09_price_momentum_high_rsi_5d_base_v056_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_5d_base_v056_signal},
    "f09_price_momentum_high_roc_sma_5d_base_v057_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_sma_5d_base_v057_signal},
    "f09_price_momentum_high_roc_std_5d_base_v058_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_std_5d_base_v058_signal},
    "f09_price_momentum_high_roc_z_5d_base_v059_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_z_5d_base_v059_signal},
    "f09_price_momentum_high_rsi_z_5d_base_v060_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_z_5d_base_v060_signal},
    "f09_price_momentum_low_roc_5d_base_v061_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_5d_base_v061_signal},
    "f09_price_momentum_low_rsi_5d_base_v062_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_5d_base_v062_signal},
    "f09_price_momentum_low_roc_sma_5d_base_v063_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_sma_5d_base_v063_signal},
    "f09_price_momentum_low_roc_std_5d_base_v064_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_std_5d_base_v064_signal},
    "f09_price_momentum_low_roc_z_5d_base_v065_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_z_5d_base_v065_signal},
    "f09_price_momentum_low_rsi_z_5d_base_v066_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_z_5d_base_v066_signal},
    "f09_price_momentum_close_roc_5d_base_v067_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_5d_base_v067_signal},
    "f09_price_momentum_close_rsi_5d_base_v068_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_5d_base_v068_signal},
    "f09_price_momentum_close_roc_sma_5d_base_v069_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_5d_base_v069_signal},
    "f09_price_momentum_close_roc_std_5d_base_v070_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_5d_base_v070_signal},
    "f09_price_momentum_close_roc_z_5d_base_v071_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_5d_base_v071_signal},
    "f09_price_momentum_close_rsi_z_5d_base_v072_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_5d_base_v072_signal},
    "f09_price_momentum_close_roc_10d_base_v073_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_10d_base_v073_signal},
    "f09_price_momentum_close_rsi_10d_base_v074_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_10d_base_v074_signal},
    "f09_price_momentum_close_roc_sma_10d_base_v075_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_10d_base_v075_signal},
}

F09_PRICE_MOMENTUM_REGISTRY_BASE_001_075 = REGISTRY

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
        q = y1.iloc[50:].dropna()
        assert len(q) > 0
        assert q.nunique() > 2
        assert q.std() > 0
        assert not q.isna().all()
        source = inspect.getsource(info["func"])
        assert "_mom_" in source
    print("All tests passed!")
