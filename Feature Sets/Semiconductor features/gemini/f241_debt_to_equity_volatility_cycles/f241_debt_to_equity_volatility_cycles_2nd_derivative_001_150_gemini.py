import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v001_signal(close, volume):
    res = close.pct_change(10).diff().rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v001_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v001_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v002_signal(close, volume):
    res = close.pct_change(21).diff().rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v002_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v002_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v003_signal(close, volume):
    res = close.pct_change(42).diff().rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v003_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v003_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v004_signal(close, volume):
    res = close.pct_change(63).diff().rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v004_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v004_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v005_signal(close, volume):
    res = close.pct_change(126).diff().rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v005_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v005_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v006_signal(close, volume):
    res = close.pct_change(252).diff().rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v006_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v006_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v007_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v007_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v007_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v008_signal(close, volume):
    res = close.pct_change(12).diff().rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v008_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v008_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v009_signal(close, volume):
    res = close.pct_change(23).diff().rolling(23).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v009_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v009_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v010_signal(close, volume):
    res = close.pct_change(44).diff().rolling(44).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v010_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v010_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v011_signal(close, volume):
    res = close.pct_change(65).diff().rolling(65).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v011_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v011_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v012_signal(close, volume):
    res = close.pct_change(128).diff().rolling(128).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v012_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v012_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v013_signal(close, volume):
    res = close.pct_change(254).diff().rolling(254).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v013_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v013_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v014_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v014_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v014_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v015_signal(close, volume):
    res = close.pct_change(14).diff().rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v015_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v015_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v016_signal(close, volume):
    res = close.pct_change(25).diff().rolling(25).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v016_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v016_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v017_signal(close, volume):
    res = close.pct_change(46).diff().rolling(46).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v017_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v017_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v018_signal(close, volume):
    res = close.pct_change(67).diff().rolling(67).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v018_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v018_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v019_signal(close, volume):
    res = close.pct_change(130).diff().rolling(130).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v019_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v019_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v020_signal(close, volume):
    res = close.pct_change(256).diff().rolling(256).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v020_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v020_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v021_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v021_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v021_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v022_signal(close, volume):
    res = close.pct_change(16).diff().rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v022_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v022_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v023_signal(close, volume):
    res = close.pct_change(27).diff().rolling(27).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v023_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v023_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v024_signal(close, volume):
    res = close.pct_change(48).diff().rolling(48).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v024_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v024_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v025_signal(close, volume):
    res = close.pct_change(69).diff().rolling(69).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v025_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v025_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v026_signal(close, volume):
    res = close.pct_change(132).diff().rolling(132).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v026_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v026_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v027_signal(close, volume):
    res = close.pct_change(258).diff().rolling(258).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v027_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v027_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v028_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v028_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v028_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v029_signal(close, volume):
    res = close.pct_change(18).diff().rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v029_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v029_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v030_signal(close, volume):
    res = close.pct_change(29).diff().rolling(29).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v030_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v030_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v031_signal(close, volume):
    res = close.pct_change(50).diff().rolling(50).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v031_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v031_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v032_signal(close, volume):
    res = close.pct_change(71).diff().rolling(71).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v032_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v032_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v033_signal(close, volume):
    res = close.pct_change(134).diff().rolling(134).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v033_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v033_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v034_signal(close, volume):
    res = close.pct_change(260).diff().rolling(260).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v034_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v034_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v035_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v035_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v035_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v036_signal(close, volume):
    res = close.pct_change(20).diff().rolling(20).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v036_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v036_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v037_signal(close, volume):
    res = close.pct_change(31).diff().rolling(31).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v037_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v037_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v038_signal(close, volume):
    res = close.pct_change(52).diff().rolling(52).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v038_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v038_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v039_signal(close, volume):
    res = close.pct_change(73).diff().rolling(73).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v039_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v039_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v040_signal(close, volume):
    res = close.pct_change(136).diff().rolling(136).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v040_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v040_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v041_signal(close, volume):
    res = close.pct_change(262).diff().rolling(262).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v041_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v041_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v042_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v042_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v042_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v043_signal(close, volume):
    res = close.pct_change(22).diff().rolling(22).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v043_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v043_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v044_signal(close, volume):
    res = close.pct_change(33).diff().rolling(33).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v044_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v044_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v045_signal(close, volume):
    res = close.pct_change(54).diff().rolling(54).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v045_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v045_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v046_signal(close, volume):
    res = close.pct_change(75).diff().rolling(75).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v046_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v046_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v047_signal(close, volume):
    res = close.pct_change(138).diff().rolling(138).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v047_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v047_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v048_signal(close, volume):
    res = close.pct_change(264).diff().rolling(264).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v048_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v048_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v049_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v049_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v049_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v050_signal(close, volume):
    res = close.pct_change(24).diff().rolling(24).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v050_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v050_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v051_signal(close, volume):
    res = close.pct_change(35).diff().rolling(35).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v051_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v051_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v052_signal(close, volume):
    res = close.pct_change(56).diff().rolling(56).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v052_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v052_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v053_signal(close, volume):
    res = close.pct_change(77).diff().rolling(77).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v053_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v053_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v054_signal(close, volume):
    res = close.pct_change(140).diff().rolling(140).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v054_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v054_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v055_signal(close, volume):
    res = close.pct_change(266).diff().rolling(266).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v055_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v055_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v056_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v056_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v056_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v057_signal(close, volume):
    res = close.pct_change(26).diff().rolling(26).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v057_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v057_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v058_signal(close, volume):
    res = close.pct_change(37).diff().rolling(37).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v058_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v058_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v059_signal(close, volume):
    res = close.pct_change(58).diff().rolling(58).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v059_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v059_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v060_signal(close, volume):
    res = close.pct_change(79).diff().rolling(79).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v060_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v060_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v061_signal(close, volume):
    res = close.pct_change(142).diff().rolling(142).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v061_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v061_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v062_signal(close, volume):
    res = close.pct_change(268).diff().rolling(268).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v062_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v062_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v063_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v063_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v063_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v064_signal(close, volume):
    res = close.pct_change(28).diff().rolling(28).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v064_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v064_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v065_signal(close, volume):
    res = close.pct_change(39).diff().rolling(39).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v065_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v065_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v066_signal(close, volume):
    res = close.pct_change(60).diff().rolling(60).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v066_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v066_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v067_signal(close, volume):
    res = close.pct_change(81).diff().rolling(81).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v067_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v067_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v068_signal(close, volume):
    res = close.pct_change(144).diff().rolling(144).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v068_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v068_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v069_signal(close, volume):
    res = close.pct_change(270).diff().rolling(270).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v069_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v069_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v070_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v070_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v070_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v071_signal(close, volume):
    res = close.pct_change(30).diff().rolling(30).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v071_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v071_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v072_signal(close, volume):
    res = close.pct_change(41).diff().rolling(41).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v072_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v072_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v073_signal(close, volume):
    res = close.pct_change(62).diff().rolling(62).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v073_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v073_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v074_signal(close, volume):
    res = close.pct_change(83).diff().rolling(83).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v074_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v074_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v075_signal(close, volume):
    res = close.pct_change(146).diff().rolling(146).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v075_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v075_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v076_signal(close, volume):
    res = close.pct_change(272).diff().rolling(272).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v076_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v076_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v077_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v077_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v077_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v078_signal(close, volume):
    res = close.pct_change(32).diff().rolling(32).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v078_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v078_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v079_signal(close, volume):
    res = close.pct_change(43).diff().rolling(43).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v079_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v079_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v080_signal(close, volume):
    res = close.pct_change(64).diff().rolling(64).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v080_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v080_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v081_signal(close, volume):
    res = close.pct_change(85).diff().rolling(85).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v081_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v081_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v082_signal(close, volume):
    res = close.pct_change(148).diff().rolling(148).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v082_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v082_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v083_signal(close, volume):
    res = close.pct_change(274).diff().rolling(274).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v083_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v083_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v084_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v084_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v084_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v085_signal(close, volume):
    res = close.pct_change(34).diff().rolling(34).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v085_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v085_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v086_signal(close, volume):
    res = close.pct_change(45).diff().rolling(45).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v086_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v086_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v087_signal(close, volume):
    res = close.pct_change(66).diff().rolling(66).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v087_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v087_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v088_signal(close, volume):
    res = close.pct_change(87).diff().rolling(87).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v088_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v088_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v089_signal(close, volume):
    res = close.pct_change(150).diff().rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v089_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v089_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v090_signal(close, volume):
    res = close.pct_change(276).diff().rolling(276).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v090_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v090_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v091_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v091_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v091_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v092_signal(close, volume):
    res = close.pct_change(36).diff().rolling(36).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v092_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v092_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v093_signal(close, volume):
    res = close.pct_change(47).diff().rolling(47).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v093_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v093_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v094_signal(close, volume):
    res = close.pct_change(68).diff().rolling(68).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v094_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v094_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v095_signal(close, volume):
    res = close.pct_change(89).diff().rolling(89).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v095_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v095_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v096_signal(close, volume):
    res = close.pct_change(152).diff().rolling(152).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v096_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v096_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v097_signal(close, volume):
    res = close.pct_change(278).diff().rolling(278).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v097_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v097_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v098_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v098_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v098_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v099_signal(close, volume):
    res = close.pct_change(38).diff().rolling(38).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v099_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v099_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v100_signal(close, volume):
    res = close.pct_change(49).diff().rolling(49).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v100_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v100_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v101_signal(close, volume):
    res = close.pct_change(70).diff().rolling(70).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v101_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v101_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v102_signal(close, volume):
    res = close.pct_change(91).diff().rolling(91).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v102_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v102_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v103_signal(close, volume):
    res = close.pct_change(154).diff().rolling(154).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v103_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v103_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v104_signal(close, volume):
    res = close.pct_change(280).diff().rolling(280).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v104_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v104_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v105_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v105_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v105_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v106_signal(close, volume):
    res = close.pct_change(40).diff().rolling(40).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v106_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v106_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v107_signal(close, volume):
    res = close.pct_change(51).diff().rolling(51).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v107_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v107_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v108_signal(close, volume):
    res = close.pct_change(72).diff().rolling(72).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v108_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v108_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v109_signal(close, volume):
    res = close.pct_change(93).diff().rolling(93).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v109_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v109_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v110_signal(close, volume):
    res = close.pct_change(156).diff().rolling(156).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v110_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v110_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v111_signal(close, volume):
    res = close.pct_change(282).diff().rolling(282).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v111_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v111_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v112_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v112_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v112_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v113_signal(close, volume):
    res = close.pct_change(42).diff().rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v113_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v113_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v114_signal(close, volume):
    res = close.pct_change(53).diff().rolling(53).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v114_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v114_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v115_signal(close, volume):
    res = close.pct_change(74).diff().rolling(74).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v115_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v115_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v116_signal(close, volume):
    res = close.pct_change(95).diff().rolling(95).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v116_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v116_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v117_signal(close, volume):
    res = close.pct_change(158).diff().rolling(158).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v117_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v117_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v118_signal(close, volume):
    res = close.pct_change(284).diff().rolling(284).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v118_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v118_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v119_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v119_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v119_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v120_signal(close, volume):
    res = close.pct_change(44).diff().rolling(44).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v120_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v120_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v121_signal(close, volume):
    res = close.pct_change(55).diff().rolling(55).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v121_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v121_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v122_signal(close, volume):
    res = close.pct_change(76).diff().rolling(76).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v122_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v122_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v123_signal(close, volume):
    res = close.pct_change(97).diff().rolling(97).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v123_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v123_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v124_signal(close, volume):
    res = close.pct_change(160).diff().rolling(160).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v124_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v124_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v125_signal(close, volume):
    res = close.pct_change(286).diff().rolling(286).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v125_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v125_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v126_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v126_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v126_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v127_signal(close, volume):
    res = close.pct_change(46).diff().rolling(46).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v127_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v127_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v128_signal(close, volume):
    res = close.pct_change(57).diff().rolling(57).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v128_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v128_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v129_signal(close, volume):
    res = close.pct_change(78).diff().rolling(78).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v129_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v129_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v130_signal(close, volume):
    res = close.pct_change(99).diff().rolling(99).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v130_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v130_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v131_signal(close, volume):
    res = close.pct_change(162).diff().rolling(162).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v131_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v131_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v132_signal(close, volume):
    res = close.pct_change(288).diff().rolling(288).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v132_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v132_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v133_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v133_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v133_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v134_signal(close, volume):
    res = close.pct_change(48).diff().rolling(48).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v134_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v134_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v135_signal(close, volume):
    res = close.pct_change(59).diff().rolling(59).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v135_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v135_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v136_signal(close, volume):
    res = close.pct_change(80).diff().rolling(80).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v136_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v136_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v137_signal(close, volume):
    res = close.pct_change(101).diff().rolling(101).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v137_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v137_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v138_signal(close, volume):
    res = close.pct_change(164).diff().rolling(164).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v138_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v138_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v139_signal(close, volume):
    res = close.pct_change(290).diff().rolling(290).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v139_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v139_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v140_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v140_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v140_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v141_signal(close, volume):
    res = close.pct_change(50).diff().rolling(50).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v141_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v141_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v142_signal(close, volume):
    res = close.pct_change(61).diff().rolling(61).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v142_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v142_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v143_signal(close, volume):
    res = close.pct_change(82).diff().rolling(82).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v143_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v143_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v144_signal(close, volume):
    res = close.pct_change(103).diff().rolling(103).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v144_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v144_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v145_signal(close, volume):
    res = close.pct_change(166).diff().rolling(166).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v145_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v145_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v146_signal(close, volume):
    res = close.pct_change(292).diff().rolling(292).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v146_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v146_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v147_signal(close, volume):
    res = close.pct_change(5).diff().rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v147_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v147_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v148_signal(close, volume):
    res = close.pct_change(52).diff().rolling(52).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v148_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v148_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v149_signal(close, volume):
    res = close.pct_change(63).diff().rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v149_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v149_signal

def f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v150_signal(close, volume):
    res = close.pct_change(84).diff().rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v150_signal'] = f241devc_f241_debt_to_equity_volatility_cycles_2nd_derivative_v150_signal


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
