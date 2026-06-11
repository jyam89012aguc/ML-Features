# f09_price_momentum_slope_001_150_gemini.py
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

# Slope of v001 (ROC for 2d window of open)
def f09_price_momentum_open_roc_2d_slope_v001_signal(arg_open):
    base = _mom_roc(arg_open, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v002 (RSI for 2d window of open)
def f09_price_momentum_open_rsi_2d_slope_v002_signal(arg_open):
    base = _mom_rsi(arg_open, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v003 (SMA of 2d ROC for open)
def f09_price_momentum_open_roc_sma_2d_slope_v003_signal(arg_open):
    base = _sma(_mom_roc(arg_open, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v004 (STD of 2d ROC for open)
def f09_price_momentum_open_roc_std_2d_slope_v004_signal(arg_open):
    base = _std(_mom_roc(arg_open, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v005 (Z-score of 2d ROC for open)
def f09_price_momentum_open_roc_z_2d_slope_v005_signal(arg_open):
    base = _z(_mom_roc(arg_open, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v006 (Z-score of 2d RSI for open)
def f09_price_momentum_open_rsi_z_2d_slope_v006_signal(arg_open):
    base = _z(_mom_rsi(arg_open, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v007 (ROC for 2d window of high)
def f09_price_momentum_high_roc_2d_slope_v007_signal(arg_high):
    base = _mom_roc(arg_high, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v008 (RSI for 2d window of high)
def f09_price_momentum_high_rsi_2d_slope_v008_signal(arg_high):
    base = _mom_rsi(arg_high, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v009 (SMA of 2d ROC for high)
def f09_price_momentum_high_roc_sma_2d_slope_v009_signal(arg_high):
    base = _sma(_mom_roc(arg_high, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v010 (STD of 2d ROC for high)
def f09_price_momentum_high_roc_std_2d_slope_v010_signal(arg_high):
    base = _std(_mom_roc(arg_high, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v011 (Z-score of 2d ROC for high)
def f09_price_momentum_high_roc_z_2d_slope_v011_signal(arg_high):
    base = _z(_mom_roc(arg_high, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v012 (Z-score of 2d RSI for high)
def f09_price_momentum_high_rsi_z_2d_slope_v012_signal(arg_high):
    base = _z(_mom_rsi(arg_high, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v013 (ROC for 2d window of low)
def f09_price_momentum_low_roc_2d_slope_v013_signal(arg_low):
    base = _mom_roc(arg_low, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v014 (RSI for 2d window of low)
def f09_price_momentum_low_rsi_2d_slope_v014_signal(arg_low):
    base = _mom_rsi(arg_low, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v015 (SMA of 2d ROC for low)
def f09_price_momentum_low_roc_sma_2d_slope_v015_signal(arg_low):
    base = _sma(_mom_roc(arg_low, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v016 (STD of 2d ROC for low)
def f09_price_momentum_low_roc_std_2d_slope_v016_signal(arg_low):
    base = _std(_mom_roc(arg_low, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v017 (Z-score of 2d ROC for low)
def f09_price_momentum_low_roc_z_2d_slope_v017_signal(arg_low):
    base = _z(_mom_roc(arg_low, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v018 (Z-score of 2d RSI for low)
def f09_price_momentum_low_rsi_z_2d_slope_v018_signal(arg_low):
    base = _z(_mom_rsi(arg_low, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v019 (ROC for 2d window of close)
def f09_price_momentum_close_roc_2d_slope_v019_signal(arg_close):
    base = _mom_roc(arg_close, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v020 (RSI for 2d window of close)
def f09_price_momentum_close_rsi_2d_slope_v020_signal(arg_close):
    base = _mom_rsi(arg_close, 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v021 (SMA of 2d ROC for close)
def f09_price_momentum_close_roc_sma_2d_slope_v021_signal(arg_close):
    base = _sma(_mom_roc(arg_close, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v022 (STD of 2d ROC for close)
def f09_price_momentum_close_roc_std_2d_slope_v022_signal(arg_close):
    base = _std(_mom_roc(arg_close, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v023 (Z-score of 2d ROC for close)
def f09_price_momentum_close_roc_z_2d_slope_v023_signal(arg_close):
    base = _z(_mom_roc(arg_close, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v024 (Z-score of 2d RSI for close)
def f09_price_momentum_close_rsi_z_2d_slope_v024_signal(arg_close):
    base = _z(_mom_rsi(arg_close, 2), 2)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v025 (ROC for 3d window of open)
def f09_price_momentum_open_roc_3d_slope_v025_signal(arg_open):
    base = _mom_roc(arg_open, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v026 (RSI for 3d window of open)
def f09_price_momentum_open_rsi_3d_slope_v026_signal(arg_open):
    base = _mom_rsi(arg_open, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v027 (SMA of 3d ROC for open)
def f09_price_momentum_open_roc_sma_3d_slope_v027_signal(arg_open):
    base = _sma(_mom_roc(arg_open, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v028 (STD of 3d ROC for open)
def f09_price_momentum_open_roc_std_3d_slope_v028_signal(arg_open):
    base = _std(_mom_roc(arg_open, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v029 (Z-score of 3d ROC for open)
def f09_price_momentum_open_roc_z_3d_slope_v029_signal(arg_open):
    base = _z(_mom_roc(arg_open, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v030 (Z-score of 3d RSI for open)
def f09_price_momentum_open_rsi_z_3d_slope_v030_signal(arg_open):
    base = _z(_mom_rsi(arg_open, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v031 (ROC for 3d window of high)
def f09_price_momentum_high_roc_3d_slope_v031_signal(arg_high):
    base = _mom_roc(arg_high, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v032 (RSI for 3d window of high)
def f09_price_momentum_high_rsi_3d_slope_v032_signal(arg_high):
    base = _mom_rsi(arg_high, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v033 (SMA of 3d ROC for high)
def f09_price_momentum_high_roc_sma_3d_slope_v033_signal(arg_high):
    base = _sma(_mom_roc(arg_high, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v034 (STD of 3d ROC for high)
def f09_price_momentum_high_roc_std_3d_slope_v034_signal(arg_high):
    base = _std(_mom_roc(arg_high, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v035 (Z-score of 3d ROC for high)
def f09_price_momentum_high_roc_z_3d_slope_v035_signal(arg_high):
    base = _z(_mom_roc(arg_high, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v036 (Z-score of 3d RSI for high)
def f09_price_momentum_high_rsi_z_3d_slope_v036_signal(arg_high):
    base = _z(_mom_rsi(arg_high, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v037 (ROC for 3d window of low)
def f09_price_momentum_low_roc_3d_slope_v037_signal(arg_low):
    base = _mom_roc(arg_low, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v038 (RSI for 3d window of low)
def f09_price_momentum_low_rsi_3d_slope_v038_signal(arg_low):
    base = _mom_rsi(arg_low, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v039 (SMA of 3d ROC for low)
def f09_price_momentum_low_roc_sma_3d_slope_v039_signal(arg_low):
    base = _sma(_mom_roc(arg_low, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v040 (STD of 3d ROC for low)
def f09_price_momentum_low_roc_std_3d_slope_v040_signal(arg_low):
    base = _std(_mom_roc(arg_low, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v041 (Z-score of 3d ROC for low)
def f09_price_momentum_low_roc_z_3d_slope_v041_signal(arg_low):
    base = _z(_mom_roc(arg_low, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v042 (Z-score of 3d RSI for low)
def f09_price_momentum_low_rsi_z_3d_slope_v042_signal(arg_low):
    base = _z(_mom_rsi(arg_low, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v043 (ROC for 3d window of close)
def f09_price_momentum_close_roc_3d_slope_v043_signal(arg_close):
    base = _mom_roc(arg_close, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v044 (RSI for 3d window of close)
def f09_price_momentum_close_rsi_3d_slope_v044_signal(arg_close):
    base = _mom_rsi(arg_close, 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v045 (SMA of 3d ROC for close)
def f09_price_momentum_close_roc_sma_3d_slope_v045_signal(arg_close):
    base = _sma(_mom_roc(arg_close, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v046 (STD of 3d ROC for close)
def f09_price_momentum_close_roc_std_3d_slope_v046_signal(arg_close):
    base = _std(_mom_roc(arg_close, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v047 (Z-score of 3d ROC for close)
def f09_price_momentum_close_roc_z_3d_slope_v047_signal(arg_close):
    base = _z(_mom_roc(arg_close, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v048 (Z-score of 3d RSI for close)
def f09_price_momentum_close_rsi_z_3d_slope_v048_signal(arg_close):
    base = _z(_mom_rsi(arg_close, 3), 3)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v049 (ROC for 5d window of open)
def f09_price_momentum_open_roc_5d_slope_v049_signal(arg_open):
    base = _mom_roc(arg_open, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v050 (RSI for 5d window of open)
def f09_price_momentum_open_rsi_5d_slope_v050_signal(arg_open):
    base = _mom_rsi(arg_open, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v051 (SMA of 5d ROC for open)
def f09_price_momentum_open_roc_sma_5d_slope_v051_signal(arg_open):
    base = _sma(_mom_roc(arg_open, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v052 (STD of 5d ROC for open)
def f09_price_momentum_open_roc_std_5d_slope_v052_signal(arg_open):
    base = _std(_mom_roc(arg_open, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v053 (Z-score of 5d ROC for open)
def f09_price_momentum_open_roc_z_5d_slope_v053_signal(arg_open):
    base = _z(_mom_roc(arg_open, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v054 (Z-score of 5d RSI for open)
def f09_price_momentum_open_rsi_z_5d_slope_v054_signal(arg_open):
    base = _z(_mom_rsi(arg_open, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v055 (ROC for 5d window of high)
def f09_price_momentum_high_roc_5d_slope_v055_signal(arg_high):
    base = _mom_roc(arg_high, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v056 (RSI for 5d window of high)
def f09_price_momentum_high_rsi_5d_slope_v056_signal(arg_high):
    base = _mom_rsi(arg_high, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v057 (SMA of 5d ROC for high)
def f09_price_momentum_high_roc_sma_5d_slope_v057_signal(arg_high):
    base = _sma(_mom_roc(arg_high, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v058 (STD of 5d ROC for high)
def f09_price_momentum_high_roc_std_5d_slope_v058_signal(arg_high):
    base = _std(_mom_roc(arg_high, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v059 (Z-score of 5d ROC for high)
def f09_price_momentum_high_roc_z_5d_slope_v059_signal(arg_high):
    base = _z(_mom_roc(arg_high, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v060 (Z-score of 5d RSI for high)
def f09_price_momentum_high_rsi_z_5d_slope_v060_signal(arg_high):
    base = _z(_mom_rsi(arg_high, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v061 (ROC for 5d window of low)
def f09_price_momentum_low_roc_5d_slope_v061_signal(arg_low):
    base = _mom_roc(arg_low, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v062 (RSI for 5d window of low)
def f09_price_momentum_low_rsi_5d_slope_v062_signal(arg_low):
    base = _mom_rsi(arg_low, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v063 (SMA of 5d ROC for low)
def f09_price_momentum_low_roc_sma_5d_slope_v063_signal(arg_low):
    base = _sma(_mom_roc(arg_low, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v064 (STD of 5d ROC for low)
def f09_price_momentum_low_roc_std_5d_slope_v064_signal(arg_low):
    base = _std(_mom_roc(arg_low, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v065 (Z-score of 5d ROC for low)
def f09_price_momentum_low_roc_z_5d_slope_v065_signal(arg_low):
    base = _z(_mom_roc(arg_low, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v066 (Z-score of 5d RSI for low)
def f09_price_momentum_low_rsi_z_5d_slope_v066_signal(arg_low):
    base = _z(_mom_rsi(arg_low, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v067 (ROC for 5d window of close)
def f09_price_momentum_close_roc_5d_slope_v067_signal(arg_close):
    base = _mom_roc(arg_close, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v068 (RSI for 5d window of close)
def f09_price_momentum_close_rsi_5d_slope_v068_signal(arg_close):
    base = _mom_rsi(arg_close, 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v069 (SMA of 5d ROC for close)
def f09_price_momentum_close_roc_sma_5d_slope_v069_signal(arg_close):
    base = _sma(_mom_roc(arg_close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v070 (STD of 5d ROC for close)
def f09_price_momentum_close_roc_std_5d_slope_v070_signal(arg_close):
    base = _std(_mom_roc(arg_close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v071 (Z-score of 5d ROC for close)
def f09_price_momentum_close_roc_z_5d_slope_v071_signal(arg_close):
    base = _z(_mom_roc(arg_close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v072 (Z-score of 5d RSI for close)
def f09_price_momentum_close_rsi_z_5d_slope_v072_signal(arg_close):
    base = _z(_mom_rsi(arg_close, 5), 5)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v073 (ROC for 10d window of close)
def f09_price_momentum_close_roc_10d_slope_v073_signal(arg_close):
    base = _mom_roc(arg_close, 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v074 (RSI for 10d window of close)
def f09_price_momentum_close_rsi_10d_slope_v074_signal(arg_close):
    base = _mom_rsi(arg_close, 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v075 (SMA of 10d ROC for close)
def f09_price_momentum_close_roc_sma_10d_slope_v075_signal(arg_close):
    base = _sma(_mom_roc(arg_close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v076 (STD of 10d ROC for close)
def f09_price_momentum_close_roc_std_10d_slope_v076_signal(arg_close):
    base = _std(_mom_roc(arg_close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v077 (Z-score of 10d ROC for close)
def f09_price_momentum_close_roc_z_10d_slope_v077_signal(arg_close):
    base = _z(_mom_roc(arg_close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v078 (SMA of 10d RSI for close)
def f09_price_momentum_close_rsi_sma_10d_slope_v078_signal(arg_close):
    base = _sma(_mom_rsi(arg_close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v079 (STD of 10d RSI for close)
def f09_price_momentum_close_rsi_std_10d_slope_v079_signal(arg_close):
    base = _std(_mom_rsi(arg_close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v080 (Z-score of 10d RSI for close)
def f09_price_momentum_close_rsi_z_10d_slope_v080_signal(arg_close):
    base = _z(_mom_rsi(arg_close, 10), 10)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v081 (ROC for 14d window of close)
def f09_price_momentum_close_roc_14d_slope_v081_signal(arg_close):
    base = _mom_roc(arg_close, 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v082 (RSI for 14d window of close)
def f09_price_momentum_close_rsi_14d_slope_v082_signal(arg_close):
    base = _mom_rsi(arg_close, 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v083 (SMA of 14d ROC for close)
def f09_price_momentum_close_roc_sma_14d_slope_v083_signal(arg_close):
    base = _sma(_mom_roc(arg_close, 14), 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v084 (STD of 14d ROC for close)
def f09_price_momentum_close_roc_std_14d_slope_v084_signal(arg_close):
    base = _std(_mom_roc(arg_close, 14), 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v085 (Z-score of 14d ROC for close)
def f09_price_momentum_close_roc_z_14d_slope_v085_signal(arg_close):
    base = _z(_mom_roc(arg_close, 14), 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v086 (SMA of 14d RSI for close)
def f09_price_momentum_close_rsi_sma_14d_slope_v086_signal(arg_close):
    base = _sma(_mom_rsi(arg_close, 14), 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v087 (STD of 14d RSI for close)
def f09_price_momentum_close_rsi_std_14d_slope_v087_signal(arg_close):
    base = _std(_mom_rsi(arg_close, 14), 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v088 (Z-score of 14d RSI for close)
def f09_price_momentum_close_rsi_z_14d_slope_v088_signal(arg_close):
    base = _z(_mom_rsi(arg_close, 14), 14)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v089 (ROC for 21d window of close)
def f09_price_momentum_close_roc_21d_slope_v089_signal(arg_close):
    base = _mom_roc(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v090 (RSI for 21d window of close)
def f09_price_momentum_close_rsi_21d_slope_v090_signal(arg_close):
    base = _mom_rsi(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v091 (SMA of 21d ROC for close)
def f09_price_momentum_close_roc_sma_21d_slope_v091_signal(arg_close):
    base = _sma(_mom_roc(arg_close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v092 (STD of 21d ROC for close)
def f09_price_momentum_close_roc_std_21d_slope_v092_signal(arg_close):
    base = _std(_mom_roc(arg_close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v093 (Z-score of 21d ROC for close)
def f09_price_momentum_close_roc_z_21d_slope_v093_signal(arg_close):
    base = _z(_mom_roc(arg_close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v094 (SMA of 21d RSI for close)
def f09_price_momentum_close_rsi_sma_21d_slope_v094_signal(arg_close):
    base = _sma(_mom_rsi(arg_close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v095 (STD of 21d RSI for close)
def f09_price_momentum_close_rsi_std_21d_slope_v095_signal(arg_close):
    base = _std(_mom_rsi(arg_close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v096 (Z-score of 21d RSI for close)
def f09_price_momentum_close_rsi_z_21d_slope_v096_signal(arg_close):
    base = _z(_mom_rsi(arg_close, 21), 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v097 (ROC for 42d window of closeadj)
def f09_price_momentum_closeadj_roc_42d_slope_v097_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v098 (RSI for 42d window of closeadj)
def f09_price_momentum_closeadj_rsi_42d_slope_v098_signal(arg_closeadj):
    base = _mom_rsi(arg_closeadj, 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v099 (SMA of 42d ROC for closeadj)
def f09_price_momentum_closeadj_roc_sma_42d_slope_v099_signal(arg_closeadj):
    base = _sma(_mom_roc(arg_closeadj, 42), 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v100 (STD of 42d ROC for closeadj)
def f09_price_momentum_closeadj_roc_std_42d_slope_v100_signal(arg_closeadj):
    base = _std(_mom_roc(arg_closeadj, 42), 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v101 (Z-score of 42d ROC for closeadj)
def f09_price_momentum_closeadj_roc_z_42d_slope_v101_signal(arg_closeadj):
    base = _z(_mom_roc(arg_closeadj, 42), 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v102 (SMA of 42d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_sma_42d_slope_v102_signal(arg_closeadj):
    base = _sma(_mom_rsi(arg_closeadj, 42), 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v103 (STD of 42d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_std_42d_slope_v103_signal(arg_closeadj):
    base = _std(_mom_rsi(arg_closeadj, 42), 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v104 (Z-score of 42d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_z_42d_slope_v104_signal(arg_closeadj):
    base = _z(_mom_rsi(arg_closeadj, 42), 42)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v105 (ROC for 63d window of closeadj)
def f09_price_momentum_closeadj_roc_63d_slope_v105_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v106 (RSI for 63d window of closeadj)
def f09_price_momentum_closeadj_rsi_63d_slope_v106_signal(arg_closeadj):
    base = _mom_rsi(arg_closeadj, 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v107 (SMA of 63d ROC for closeadj)
def f09_price_momentum_closeadj_roc_sma_63d_slope_v107_signal(arg_closeadj):
    base = _sma(_mom_roc(arg_closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v108 (STD of 63d ROC for closeadj)
def f09_price_momentum_closeadj_roc_std_63d_slope_v108_signal(arg_closeadj):
    base = _std(_mom_roc(arg_closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v109 (Z-score of 63d ROC for closeadj)
def f09_price_momentum_closeadj_roc_z_63d_slope_v109_signal(arg_closeadj):
    base = _z(_mom_roc(arg_closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v110 (SMA of 63d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_sma_63d_slope_v110_signal(arg_closeadj):
    base = _sma(_mom_rsi(arg_closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v111 (STD of 63d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_std_63d_slope_v111_signal(arg_closeadj):
    base = _std(_mom_rsi(arg_closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v112 (Z-score of 63d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_z_63d_slope_v112_signal(arg_closeadj):
    base = _z(_mom_rsi(arg_closeadj, 63), 63)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v113 (ROC for 126d window of closeadj)
def f09_price_momentum_closeadj_roc_126d_slope_v113_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v114 (RSI for 126d window of closeadj)
def f09_price_momentum_closeadj_rsi_126d_slope_v114_signal(arg_closeadj):
    base = _mom_rsi(arg_closeadj, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v115 (SMA of 126d ROC for closeadj)
def f09_price_momentum_closeadj_roc_sma_126d_slope_v115_signal(arg_closeadj):
    base = _sma(_mom_roc(arg_closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v116 (STD of 126d ROC for closeadj)
def f09_price_momentum_closeadj_roc_std_126d_slope_v116_signal(arg_closeadj):
    base = _std(_mom_roc(arg_closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v117 (Z-score of 126d ROC for closeadj)
def f09_price_momentum_closeadj_roc_z_126d_slope_v117_signal(arg_closeadj):
    base = _z(_mom_roc(arg_closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v118 (SMA of 126d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_sma_126d_slope_v118_signal(arg_closeadj):
    base = _sma(_mom_rsi(arg_closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v119 (STD of 126d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_std_126d_slope_v119_signal(arg_closeadj):
    base = _std(_mom_rsi(arg_closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v120 (Z-score of 126d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_z_126d_slope_v120_signal(arg_closeadj):
    base = _z(_mom_rsi(arg_closeadj, 126), 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v121 (ROC for 252d window of closeadj)
def f09_price_momentum_closeadj_roc_252d_slope_v121_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v122 (RSI for 252d window of closeadj)
def f09_price_momentum_closeadj_rsi_252d_slope_v122_signal(arg_closeadj):
    base = _mom_rsi(arg_closeadj, 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v123 (SMA of 252d ROC for closeadj)
def f09_price_momentum_closeadj_roc_sma_252d_slope_v123_signal(arg_closeadj):
    base = _sma(_mom_roc(arg_closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v124 (STD of 252d ROC for closeadj)
def f09_price_momentum_closeadj_roc_std_252d_slope_v124_signal(arg_closeadj):
    base = _std(_mom_roc(arg_closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v125 (Z-score of 252d ROC for closeadj)
def f09_price_momentum_closeadj_roc_z_252d_slope_v125_signal(arg_closeadj):
    base = _z(_mom_roc(arg_closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v126 (SMA of 252d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_sma_252d_slope_v126_signal(arg_closeadj):
    base = _sma(_mom_rsi(arg_closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v127 (STD of 252d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_std_252d_slope_v127_signal(arg_closeadj):
    base = _std(_mom_rsi(arg_closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v128 (Z-score of 252d RSI for closeadj)
def f09_price_momentum_closeadj_rsi_z_252d_slope_v128_signal(arg_closeadj):
    base = _z(_mom_rsi(arg_closeadj, 252), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v129 (ROC Div 2d-21d)
def f09_price_momentum_roc_div_2d_21d_slope_v129_signal(arg_open, arg_close):
    base = _mom_roc(arg_open, 2) - _mom_roc(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v130 (ROC Div 3d-21d)
def f09_price_momentum_roc_div_3d_21d_slope_v130_signal(arg_open, arg_close):
    base = _mom_roc(arg_open, 3) - _mom_roc(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v131 (ROC Div 5d-21d)
def f09_price_momentum_roc_div_5d_21d_slope_v131_signal(arg_open, arg_close):
    base = _mom_roc(arg_open, 5) - _mom_roc(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v132 (ROC Div 10d-21d)
def f09_price_momentum_roc_div_10d_21d_slope_v132_signal(arg_close):
    base = _mom_roc(arg_close, 10) - _mom_roc(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v133 (ROC Div 21d-252d)
def f09_price_momentum_roc_div_21d_252d_slope_v133_signal(arg_close, arg_closeadj):
    base = _mom_roc(arg_close, 21) - _mom_roc(arg_closeadj, 252)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v134 (ROC Div 42d-252d)
def f09_price_momentum_roc_div_42d_252d_slope_v134_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 42) - _mom_roc(arg_closeadj, 252)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v135 (ROC Div 63d-252d)
def f09_price_momentum_roc_div_63d_252d_slope_v135_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 63) - _mom_roc(arg_closeadj, 252)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v136 (ROC Div 126d-252d)
def f09_price_momentum_roc_div_126d_252d_slope_v136_signal(arg_closeadj):
    base = _mom_roc(arg_closeadj, 126) - _mom_roc(arg_closeadj, 252)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v137 (ROC Rel Max 21d-252d)
def f09_price_momentum_closeadj_roc_rel_max_252d_slope_v137_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 21)
    base = roc / _max(roc, 252).replace(0, np.nan)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v138 (ROC Rel Max 63d-252d)
def f09_price_momentum_closeadj_roc_63d_rel_max_252d_slope_v138_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 63)
    base = roc / _max(roc, 252).replace(0, np.nan)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v139 (Avg Pos Ret 21d)
def f09_price_momentum_avg_pos_ret_21d_slope_v139_signal(arg_close):
    ret = arg_close.pct_change()
    base = ret.where(ret > 0, 0).rolling(21).mean()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v140 (Avg Pos Ret 63d)
def f09_price_momentum_avg_pos_ret_63d_slope_v140_signal(arg_closeadj):
    ret = arg_closeadj.pct_change()
    base = ret.where(ret > 0, 0).rolling(63).mean()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v141 (Pos ROC Count 21d)
def f09_price_momentum_pos_roc_count_21d_slope_v141_signal(arg_close):
    roc = _mom_roc(arg_close, 1)
    base = (roc > 0).rolling(21).sum()
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v142 (Pos ROC Count 63d)
def f09_price_momentum_pos_roc_count_63d_slope_v142_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 1)
    base = (roc > 0).rolling(63).sum()
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v143 (ROC 63d Z-score 252d)
def f09_price_momentum_roc_63d_z_252d_slope_v143_signal(arg_closeadj):
    roc = _mom_roc(arg_closeadj, 63)
    base = _z(roc, 252)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v144 (ROC 21d Z-score 126d)
def f09_price_momentum_roc_21d_z_126d_slope_v144_signal(arg_close):
    roc = _mom_roc(arg_close, 21)
    base = _z(roc, 126)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v145 (ROC 5d Z-score 63d)
def f09_price_momentum_roc_5d_z_63d_slope_v145_signal(arg_close):
    roc = _mom_roc(arg_close, 5)
    base = _z(roc, 63)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v146 (RSI Div 14d-50d)
def f09_price_momentum_rsi_div_14d_50d_slope_v146_signal(arg_close):
    base = _mom_rsi(arg_close, 14) - _mom_rsi(arg_close, 50)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v147 (RSI Div 7d-21d)
def f09_price_momentum_rsi_div_7d_21d_slope_v147_signal(arg_close):
    base = _mom_rsi(arg_close, 7) - _mom_rsi(arg_close, 21)
    res = base.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v148 (CloseAdj 50d RSI SMA)
def f09_price_momentum_closeadj_rsi_sma_50d_slope_v148_signal(arg_closeadj):
    base = _sma(_mom_rsi(arg_closeadj, 50), 50)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v149 (CloseAdj 50d RSI STD)
def f09_price_momentum_closeadj_rsi_std_50d_slope_v149_signal(arg_closeadj):
    base = _std(_mom_rsi(arg_closeadj, 50), 50)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Slope of v150 (CloseAdj 50d RSI Z)
def f09_price_momentum_closeadj_rsi_z_50d_slope_v150_signal(arg_closeadj):
    base = _z(_mom_rsi(arg_closeadj, 50), 50)
    res = base.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {}
for i in range(1, 151):
    name = f"f09_price_momentum_"
    # We need to match the names from base files but with _slope_
    # This is tedious but I'll try to be consistent with the logic above.
    pass

# Actually I'll manually populate REGISTRY for speed and accuracy
REGISTRY = {
    "f09_price_momentum_open_roc_2d_slope_v001_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_2d_slope_v001_signal},
    "f09_price_momentum_open_rsi_2d_slope_v002_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_2d_slope_v002_signal},
    "f09_price_momentum_open_roc_sma_2d_slope_v003_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_sma_2d_slope_v003_signal},
    "f09_price_momentum_open_roc_std_2d_slope_v004_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_std_2d_slope_v004_signal},
    "f09_price_momentum_open_roc_z_2d_slope_v005_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_z_2d_slope_v005_signal},
    "f09_price_momentum_open_rsi_z_2d_slope_v006_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_z_2d_slope_v006_signal},
    "f09_price_momentum_high_roc_2d_slope_v007_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_2d_slope_v007_signal},
    "f09_price_momentum_high_rsi_2d_slope_v008_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_2d_slope_v008_signal},
    "f09_price_momentum_high_roc_sma_2d_slope_v009_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_sma_2d_slope_v009_signal},
    "f09_price_momentum_high_roc_std_2d_slope_v010_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_std_2d_slope_v010_signal},
    "f09_price_momentum_high_roc_z_2d_slope_v011_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_z_2d_slope_v011_signal},
    "f09_price_momentum_high_rsi_z_2d_slope_v012_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_z_2d_slope_v012_signal},
    "f09_price_momentum_low_roc_2d_slope_v013_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_2d_slope_v013_signal},
    "f09_price_momentum_low_rsi_2d_slope_v014_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_2d_slope_v014_signal},
    "f09_price_momentum_low_roc_sma_2d_slope_v015_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_sma_2d_slope_v015_signal},
    "f09_price_momentum_low_roc_std_2d_slope_v016_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_std_2d_slope_v016_signal},
    "f09_price_momentum_low_roc_z_2d_slope_v017_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_z_2d_slope_v017_signal},
    "f09_price_momentum_low_rsi_z_2d_slope_v018_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_z_2d_slope_v018_signal},
    "f09_price_momentum_close_roc_2d_slope_v019_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_2d_slope_v019_signal},
    "f09_price_momentum_close_rsi_2d_slope_v020_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_2d_slope_v020_signal},
    "f09_price_momentum_close_roc_sma_2d_slope_v021_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_2d_slope_v021_signal},
    "f09_price_momentum_close_roc_std_2d_slope_v022_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_2d_slope_v022_signal},
    "f09_price_momentum_close_roc_z_2d_slope_v023_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_2d_slope_v023_signal},
    "f09_price_momentum_close_rsi_z_2d_slope_v024_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_2d_slope_v024_signal},
    "f09_price_momentum_open_roc_3d_slope_v025_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_3d_slope_v025_signal},
    "f09_price_momentum_open_rsi_3d_slope_v026_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_3d_slope_v026_signal},
    "f09_price_momentum_open_roc_sma_3d_slope_v027_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_sma_3d_slope_v027_signal},
    "f09_price_momentum_open_roc_std_3d_slope_v028_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_std_3d_slope_v028_signal},
    "f09_price_momentum_open_roc_z_3d_slope_v029_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_z_3d_slope_v029_signal},
    "f09_price_momentum_open_rsi_z_3d_slope_v030_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_z_3d_slope_v030_signal},
    "f09_price_momentum_high_roc_3d_slope_v031_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_3d_slope_v031_signal},
    "f09_price_momentum_high_rsi_3d_slope_v032_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_3d_slope_v032_signal},
    "f09_price_momentum_high_roc_sma_3d_slope_v033_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_sma_3d_slope_v033_signal},
    "f09_price_momentum_high_roc_std_3d_slope_v034_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_std_3d_slope_v034_signal},
    "f09_price_momentum_high_roc_z_3d_slope_v035_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_z_3d_slope_v035_signal},
    "f09_price_momentum_high_rsi_z_3d_slope_v036_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_z_3d_slope_v036_signal},
    "f09_price_momentum_low_roc_3d_slope_v037_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_3d_slope_v037_signal},
    "f09_price_momentum_low_rsi_3d_slope_v038_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_3d_slope_v038_signal},
    "f09_price_momentum_low_roc_sma_3d_slope_v039_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_sma_3d_slope_v039_signal},
    "f09_price_momentum_low_roc_std_3d_slope_v040_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_std_3d_slope_v040_signal},
    "f09_price_momentum_low_roc_z_3d_slope_v041_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_z_3d_slope_v041_signal},
    "f09_price_momentum_low_rsi_z_3d_slope_v042_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_z_3d_slope_v042_signal},
    "f09_price_momentum_close_roc_3d_slope_v043_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_3d_slope_v043_signal},
    "f09_price_momentum_close_rsi_3d_slope_v044_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_3d_slope_v044_signal},
    "f09_price_momentum_close_roc_sma_3d_slope_v045_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_3d_slope_v045_signal},
    "f09_price_momentum_close_roc_std_3d_slope_v046_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_3d_slope_v046_signal},
    "f09_price_momentum_close_roc_z_3d_slope_v047_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_3d_slope_v047_signal},
    "f09_price_momentum_close_rsi_z_3d_slope_v048_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_3d_slope_v048_signal},
    "f09_price_momentum_open_roc_5d_slope_v049_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_5d_slope_v049_signal},
    "f09_price_momentum_open_rsi_5d_slope_v050_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_5d_slope_v050_signal},
    "f09_price_momentum_open_roc_sma_5d_slope_v051_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_sma_5d_slope_v051_signal},
    "f09_price_momentum_open_roc_std_5d_slope_v052_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_std_5d_slope_v052_signal},
    "f09_price_momentum_open_roc_z_5d_slope_v053_signal": {"inputs": ["open"], "func": f09_price_momentum_open_roc_z_5d_slope_v053_signal},
    "f09_price_momentum_open_rsi_z_5d_slope_v054_signal": {"inputs": ["open"], "func": f09_price_momentum_open_rsi_z_5d_slope_v054_signal},
    "f09_price_momentum_high_roc_5d_slope_v055_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_5d_slope_v055_signal},
    "f09_price_momentum_high_rsi_5d_slope_v056_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_5d_slope_v056_signal},
    "f09_price_momentum_high_roc_sma_5d_slope_v057_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_sma_5d_slope_v057_signal},
    "f09_price_momentum_high_roc_std_5d_slope_v058_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_std_5d_slope_v058_signal},
    "f09_price_momentum_high_roc_z_5d_slope_v059_signal": {"inputs": ["high"], "func": f09_price_momentum_high_roc_z_5d_slope_v059_signal},
    "f09_price_momentum_high_rsi_z_5d_slope_v060_signal": {"inputs": ["high"], "func": f09_price_momentum_high_rsi_z_5d_slope_v060_signal},
    "f09_price_momentum_low_roc_5d_slope_v061_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_5d_slope_v061_signal},
    "f09_price_momentum_low_rsi_5d_slope_v062_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_5d_slope_v062_signal},
    "f09_price_momentum_low_roc_sma_5d_slope_v063_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_sma_5d_slope_v063_signal},
    "f09_price_momentum_low_roc_std_5d_slope_v064_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_std_5d_slope_v064_signal},
    "f09_price_momentum_low_roc_z_5d_slope_v065_signal": {"inputs": ["low"], "func": f09_price_momentum_low_roc_z_5d_slope_v065_signal},
    "f09_price_momentum_low_rsi_z_5d_slope_v066_signal": {"inputs": ["low"], "func": f09_price_momentum_low_rsi_z_5d_slope_v066_signal},
    "f09_price_momentum_close_roc_5d_slope_v067_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_5d_slope_v067_signal},
    "f09_price_momentum_close_rsi_5d_slope_v068_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_5d_slope_v068_signal},
    "f09_price_momentum_close_roc_sma_5d_slope_v069_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_5d_slope_v069_signal},
    "f09_price_momentum_close_roc_std_5d_slope_v070_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_5d_slope_v070_signal},
    "f09_price_momentum_close_roc_z_5d_slope_v071_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_5d_slope_v071_signal},
    "f09_price_momentum_close_rsi_z_5d_slope_v072_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_5d_slope_v072_signal},
    "f09_price_momentum_close_roc_10d_slope_v073_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_10d_slope_v073_signal},
    "f09_price_momentum_close_rsi_10d_slope_v074_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_10d_slope_v074_signal},
    "f09_price_momentum_close_roc_sma_10d_slope_v075_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_10d_slope_v075_signal},
    "f09_price_momentum_close_roc_std_10d_slope_v076_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_10d_slope_v076_signal},
    "f09_price_momentum_close_roc_z_10d_slope_v077_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_10d_slope_v077_signal},
    "f09_price_momentum_close_rsi_sma_10d_slope_v078_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_sma_10d_slope_v078_signal},
    "f09_price_momentum_close_rsi_std_10d_slope_v079_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_std_10d_slope_v079_signal},
    "f09_price_momentum_close_rsi_z_10d_slope_v080_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_10d_slope_v080_signal},
    "f09_price_momentum_close_roc_14d_slope_v081_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_14d_slope_v081_signal},
    "f09_price_momentum_close_rsi_14d_slope_v082_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_14d_slope_v082_signal},
    "f09_price_momentum_close_roc_sma_14d_slope_v083_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_14d_slope_v083_signal},
    "f09_price_momentum_close_roc_std_14d_slope_v084_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_14d_slope_v084_signal},
    "f09_price_momentum_close_roc_z_14d_slope_v085_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_14d_slope_v085_signal},
    "f09_price_momentum_close_rsi_sma_14d_slope_v086_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_sma_14d_slope_v086_signal},
    "f09_price_momentum_close_rsi_std_14d_slope_v087_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_std_14d_slope_v087_signal},
    "f09_price_momentum_close_rsi_z_14d_slope_v088_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_14d_slope_v088_signal},
    "f09_price_momentum_close_roc_21d_slope_v089_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_21d_slope_v089_signal},
    "f09_price_momentum_close_rsi_21d_slope_v090_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_21d_slope_v090_signal},
    "f09_price_momentum_close_roc_sma_21d_slope_v091_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_sma_21d_slope_v091_signal},
    "f09_price_momentum_close_roc_std_21d_slope_v092_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_std_21d_slope_v092_signal},
    "f09_price_momentum_close_roc_z_21d_slope_v093_signal": {"inputs": ["close"], "func": f09_price_momentum_close_roc_z_21d_slope_v093_signal},
    "f09_price_momentum_close_rsi_sma_21d_slope_v094_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_sma_21d_slope_v094_signal},
    "f09_price_momentum_close_rsi_std_21d_slope_v095_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_std_21d_slope_v095_signal},
    "f09_price_momentum_close_rsi_z_21d_slope_v096_signal": {"inputs": ["close"], "func": f09_price_momentum_close_rsi_z_21d_slope_v096_signal},
    "f09_price_momentum_closeadj_roc_42d_slope_v097_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_42d_slope_v097_signal},
    "f09_price_momentum_closeadj_rsi_42d_slope_v098_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_42d_slope_v098_signal},
    "f09_price_momentum_closeadj_roc_sma_42d_slope_v099_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_42d_slope_v099_signal},
    "f09_price_momentum_closeadj_roc_std_42d_slope_v100_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_42d_slope_v100_signal},
    "f09_price_momentum_closeadj_roc_z_42d_slope_v101_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_42d_slope_v101_signal},
    "f09_price_momentum_closeadj_rsi_sma_42d_slope_v102_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_42d_slope_v102_signal},
    "f09_price_momentum_closeadj_rsi_std_42d_slope_v103_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_42d_slope_v103_signal},
    "f09_price_momentum_closeadj_rsi_z_42d_slope_v104_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_42d_slope_v104_signal},
    "f09_price_momentum_closeadj_roc_63d_slope_v105_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_63d_slope_v105_signal},
    "f09_price_momentum_closeadj_rsi_63d_slope_v106_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_63d_slope_v106_signal},
    "f09_price_momentum_closeadj_roc_sma_63d_slope_v107_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_63d_slope_v107_signal},
    "f09_price_momentum_closeadj_roc_std_63d_slope_v108_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_63d_slope_v108_signal},
    "f09_price_momentum_closeadj_roc_z_63d_slope_v109_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_63d_slope_v109_signal},
    "f09_price_momentum_closeadj_rsi_sma_63d_slope_v110_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_63d_slope_v110_signal},
    "f09_price_momentum_closeadj_rsi_std_63d_slope_v111_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_63d_slope_v111_signal},
    "f09_price_momentum_closeadj_rsi_z_63d_slope_v112_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_63d_slope_v112_signal},
    "f09_price_momentum_closeadj_roc_126d_slope_v113_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_126d_slope_v113_signal},
    "f09_price_momentum_closeadj_rsi_126d_slope_v114_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_126d_slope_v114_signal},
    "f09_price_momentum_closeadj_roc_sma_126d_slope_v115_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_126d_slope_v115_signal},
    "f09_price_momentum_closeadj_roc_std_126d_slope_v116_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_126d_slope_v116_signal},
    "f09_price_momentum_closeadj_roc_z_126d_slope_v117_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_126d_slope_v117_signal},
    "f09_price_momentum_closeadj_rsi_sma_126d_slope_v118_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_126d_slope_v118_signal},
    "f09_price_momentum_closeadj_rsi_std_126d_slope_v119_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_126d_slope_v119_signal},
    "f09_price_momentum_closeadj_rsi_z_126d_slope_v120_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_126d_slope_v120_signal},
    "f09_price_momentum_closeadj_roc_252d_slope_v121_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_252d_slope_v121_signal},
    "f09_price_momentum_closeadj_rsi_252d_slope_v122_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_252d_slope_v122_signal},
    "f09_price_momentum_closeadj_roc_sma_252d_slope_v123_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_sma_252d_slope_v123_signal},
    "f09_price_momentum_closeadj_roc_std_252d_slope_v124_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_std_252d_slope_v124_signal},
    "f09_price_momentum_closeadj_roc_z_252d_slope_v125_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_z_252d_slope_v125_signal},
    "f09_price_momentum_closeadj_rsi_sma_252d_slope_v126_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_252d_slope_v126_signal},
    "f09_price_momentum_closeadj_rsi_std_252d_slope_v127_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_252d_slope_v127_signal},
    "f09_price_momentum_closeadj_rsi_z_252d_slope_v128_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_252d_slope_v128_signal},
    "f09_price_momentum_roc_div_2d_21d_slope_v129_signal": {"inputs": ["open", "close"], "func": f09_price_momentum_roc_div_2d_21d_slope_v129_signal},
    "f09_price_momentum_roc_div_3d_21d_slope_v130_signal": {"inputs": ["open", "close"], "func": f09_price_momentum_roc_div_3d_21d_slope_v130_signal},
    "f09_price_momentum_roc_div_5d_21d_slope_v131_signal": {"inputs": ["open", "close"], "func": f09_price_momentum_roc_div_5d_21d_slope_v131_signal},
    "f09_price_momentum_roc_div_10d_21d_slope_v132_signal": {"inputs": ["close"], "func": f09_price_momentum_roc_div_10d_21d_slope_v132_signal},
    "f09_price_momentum_roc_div_21d_252d_slope_v133_signal": {"inputs": ["close", "closeadj"], "func": f09_price_momentum_roc_div_21d_252d_slope_v133_signal},
    "f09_price_momentum_roc_div_42d_252d_slope_v134_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_div_42d_252d_slope_v134_signal},
    "f09_price_momentum_roc_div_63d_252d_slope_v135_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_div_63d_252d_slope_v135_signal},
    "f09_price_momentum_roc_div_126d_252d_slope_v136_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_div_126d_252d_slope_v136_signal},
    "f09_price_momentum_closeadj_roc_rel_max_252d_slope_v137_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_rel_max_252d_slope_v137_signal},
    "f09_price_momentum_closeadj_roc_63d_rel_max_252d_slope_v138_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_roc_63d_rel_max_252d_slope_v138_signal},
    "f09_price_momentum_avg_pos_ret_21d_slope_v139_signal": {"inputs": ["close"], "func": f09_price_momentum_avg_pos_ret_21d_slope_v139_signal},
    "f09_price_momentum_avg_pos_ret_63d_slope_v140_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_avg_pos_ret_63d_slope_v140_signal},
    "f09_price_momentum_pos_roc_count_21d_slope_v141_signal": {"inputs": ["close"], "func": f09_price_momentum_pos_roc_count_21d_slope_v141_signal},
    "f09_price_momentum_pos_roc_count_63d_slope_v142_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_pos_roc_count_63d_slope_v142_signal},
    "f09_price_momentum_roc_63d_z_252d_slope_v143_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_roc_63d_z_252d_slope_v143_signal},
    "f09_price_momentum_roc_21d_z_126d_slope_v144_signal": {"inputs": ["close"], "func": f09_price_momentum_roc_21d_z_126d_slope_v144_signal},
    "f09_price_momentum_roc_5d_z_63d_slope_v145_signal": {"inputs": ["close"], "func": f09_price_momentum_roc_5d_z_63d_slope_v145_signal},
    "f09_price_momentum_rsi_div_14d_50d_slope_v146_signal": {"inputs": ["close"], "func": f09_price_momentum_rsi_div_14d_50d_slope_v146_signal},
    "f09_price_momentum_rsi_div_7d_21d_slope_v147_signal": {"inputs": ["close"], "func": f09_price_momentum_rsi_div_7d_21d_slope_v147_signal},
    "f09_price_momentum_closeadj_rsi_sma_50d_slope_v148_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_sma_50d_slope_v148_signal},
    "f09_price_momentum_closeadj_rsi_std_50d_slope_v149_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_std_50d_slope_v149_signal},
    "f09_price_momentum_closeadj_rsi_z_50d_slope_v150_signal": {"inputs": ["closeadj"], "func": f09_price_momentum_closeadj_rsi_z_50d_slope_v150_signal},
}

F09_PRICE_MOMENTUM_REGISTRY_SLOPE = REGISTRY

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
        assert "diff" in source
    print("All tests passed!")
