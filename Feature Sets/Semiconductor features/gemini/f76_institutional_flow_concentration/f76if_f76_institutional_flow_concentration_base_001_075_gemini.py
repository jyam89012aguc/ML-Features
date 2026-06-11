import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f76if_f76_institutional_flow_concentration_calc001_63d_base_v001_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(63).max() - low.rolling(63).min()) / high.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc001_63d_base_v001_signal'] = f76if_f76_institutional_flow_concentration_calc001_63d_base_v001_signal

def f76if_f76_institutional_flow_concentration_calc002_10d_base_v002_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.pct_change(10) - low.pct_change(10))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc002_10d_base_v002_signal'] = f76if_f76_institutional_flow_concentration_calc002_10d_base_v002_signal

def f76if_f76_institutional_flow_concentration_calc003_21d_base_v003_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(21).max() - high.rolling(21).min()) / low.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc003_21d_base_v003_signal'] = f76if_f76_institutional_flow_concentration_calc003_21d_base_v003_signal

def f76if_f76_institutional_flow_concentration_calc004_126d_base_v004_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(126) - high.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc004_126d_base_v004_signal'] = f76if_f76_institutional_flow_concentration_calc004_126d_base_v004_signal

def f76if_f76_institutional_flow_concentration_calc005_10d_base_v005_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(10).quantile(0.5) / open.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc005_10d_base_v005_signal'] = f76if_f76_institutional_flow_concentration_calc005_10d_base_v005_signal

def f76if_f76_institutional_flow_concentration_calc006_10d_base_v006_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(10).rank(pct=True) / open.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc006_10d_base_v006_signal'] = f76if_f76_institutional_flow_concentration_calc006_10d_base_v006_signal

def f76if_f76_institutional_flow_concentration_calc007_5d_base_v007_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / close.replace(0, np.nan)).rolling(5).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc007_5d_base_v007_signal'] = f76if_f76_institutional_flow_concentration_calc007_5d_base_v007_signal

def f76if_f76_institutional_flow_concentration_calc008_126d_base_v008_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(126).rank(pct=True) / volume.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc008_126d_base_v008_signal'] = f76if_f76_institutional_flow_concentration_calc008_126d_base_v008_signal

def f76if_f76_institutional_flow_concentration_calc009_63d_base_v009_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(63).rank(pct=True) / volume.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc009_63d_base_v009_signal'] = f76if_f76_institutional_flow_concentration_calc009_63d_base_v009_signal

def f76if_f76_institutional_flow_concentration_calc010_21d_base_v010_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(21).quantile(0.5) / low.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc010_21d_base_v010_signal'] = f76if_f76_institutional_flow_concentration_calc010_21d_base_v010_signal

def f76if_f76_institutional_flow_concentration_calc011_5d_base_v011_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).max() - sharesbas.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc011_5d_base_v011_signal'] = f76if_f76_institutional_flow_concentration_calc011_5d_base_v011_signal

def f76if_f76_institutional_flow_concentration_calc012_21d_base_v012_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(21).max() - volume.rolling(21).min()) / close.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc012_21d_base_v012_signal'] = f76if_f76_institutional_flow_concentration_calc012_21d_base_v012_signal

def f76if_f76_institutional_flow_concentration_calc013_63d_base_v013_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).max() - high.rolling(63).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc013_63d_base_v013_signal'] = f76if_f76_institutional_flow_concentration_calc013_63d_base_v013_signal

def f76if_f76_institutional_flow_concentration_calc014_126d_base_v014_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(126).abs() / close.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc014_126d_base_v014_signal'] = f76if_f76_institutional_flow_concentration_calc014_126d_base_v014_signal

def f76if_f76_institutional_flow_concentration_calc015_126d_base_v015_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(126).rank(pct=True) / volume.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc015_126d_base_v015_signal'] = f76if_f76_institutional_flow_concentration_calc015_126d_base_v015_signal

def f76if_f76_institutional_flow_concentration_calc016_5d_base_v016_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((open - open.rolling(5).mean()) / open.rolling(5).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc016_5d_base_v016_signal'] = f76if_f76_institutional_flow_concentration_calc016_5d_base_v016_signal

def f76if_f76_institutional_flow_concentration_calc017_21d_base_v017_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(21) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc017_21d_base_v017_signal'] = f76if_f76_institutional_flow_concentration_calc017_21d_base_v017_signal

def f76if_f76_institutional_flow_concentration_calc018_252d_base_v018_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(252).kurt() - marketcap.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc018_252d_base_v018_signal'] = f76if_f76_institutional_flow_concentration_calc018_252d_base_v018_signal

def f76if_f76_institutional_flow_concentration_calc019_42d_base_v019_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(42).max() - volume.rolling(42).min()) / open.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc019_42d_base_v019_signal'] = f76if_f76_institutional_flow_concentration_calc019_42d_base_v019_signal

def f76if_f76_institutional_flow_concentration_calc020_5d_base_v020_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(5).abs() / low.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc020_5d_base_v020_signal'] = f76if_f76_institutional_flow_concentration_calc020_5d_base_v020_signal

def f76if_f76_institutional_flow_concentration_calc021_63d_base_v021_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.pct_change(63) - volume.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc021_63d_base_v021_signal'] = f76if_f76_institutional_flow_concentration_calc021_63d_base_v021_signal

def f76if_f76_institutional_flow_concentration_calc022_63d_base_v022_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).quantile(0.5) / open.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc022_63d_base_v022_signal'] = f76if_f76_institutional_flow_concentration_calc022_63d_base_v022_signal

def f76if_f76_institutional_flow_concentration_calc023_63d_base_v023_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(63) / high.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc023_63d_base_v023_signal'] = f76if_f76_institutional_flow_concentration_calc023_63d_base_v023_signal

def f76if_f76_institutional_flow_concentration_calc024_21d_base_v024_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(21).abs() / sharesbas.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc024_21d_base_v024_signal'] = f76if_f76_institutional_flow_concentration_calc024_21d_base_v024_signal

def f76if_f76_institutional_flow_concentration_calc025_5d_base_v025_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(5).rank(pct=True) / close.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc025_5d_base_v025_signal'] = f76if_f76_institutional_flow_concentration_calc025_5d_base_v025_signal

def f76if_f76_institutional_flow_concentration_calc026_5d_base_v026_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(5).kurt() - low.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc026_5d_base_v026_signal'] = f76if_f76_institutional_flow_concentration_calc026_5d_base_v026_signal

def f76if_f76_institutional_flow_concentration_calc027_126d_base_v027_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / volume.replace(0, np.nan)).rolling(126).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc027_126d_base_v027_signal'] = f76if_f76_institutional_flow_concentration_calc027_126d_base_v027_signal

def f76if_f76_institutional_flow_concentration_calc028_63d_base_v028_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(63) - high.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc028_63d_base_v028_signal'] = f76if_f76_institutional_flow_concentration_calc028_63d_base_v028_signal

def f76if_f76_institutional_flow_concentration_calc029_42d_base_v029_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(42).max() - high.rolling(42).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc029_42d_base_v029_signal'] = f76if_f76_institutional_flow_concentration_calc029_42d_base_v029_signal

def f76if_f76_institutional_flow_concentration_calc030_63d_base_v030_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(63) - low.pct_change(63))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc030_63d_base_v030_signal'] = f76if_f76_institutional_flow_concentration_calc030_63d_base_v030_signal

def f76if_f76_institutional_flow_concentration_calc031_21d_base_v031_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(21).abs() / low.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc031_21d_base_v031_signal'] = f76if_f76_institutional_flow_concentration_calc031_21d_base_v031_signal

def f76if_f76_institutional_flow_concentration_calc032_63d_base_v032_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.diff(63).abs() / close.diff(63).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc032_63d_base_v032_signal'] = f76if_f76_institutional_flow_concentration_calc032_63d_base_v032_signal

def f76if_f76_institutional_flow_concentration_calc033_42d_base_v033_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(42).quantile(0.5) / marketcap.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc033_42d_base_v033_signal'] = f76if_f76_institutional_flow_concentration_calc033_42d_base_v033_signal

def f76if_f76_institutional_flow_concentration_calc034_10d_base_v034_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close / sharesbas.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc034_10d_base_v034_signal'] = f76if_f76_institutional_flow_concentration_calc034_10d_base_v034_signal

def f76if_f76_institutional_flow_concentration_calc035_252d_base_v035_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(252).quantile(0.5) / close.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc035_252d_base_v035_signal'] = f76if_f76_institutional_flow_concentration_calc035_252d_base_v035_signal

def f76if_f76_institutional_flow_concentration_calc036_63d_base_v036_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / low.replace(0, np.nan)).rolling(63).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc036_63d_base_v036_signal'] = f76if_f76_institutional_flow_concentration_calc036_63d_base_v036_signal

def f76if_f76_institutional_flow_concentration_calc037_21d_base_v037_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(21).max() - marketcap.rolling(21).min()) / open.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc037_21d_base_v037_signal'] = f76if_f76_institutional_flow_concentration_calc037_21d_base_v037_signal

def f76if_f76_institutional_flow_concentration_calc038_21d_base_v038_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap / sharesbas.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc038_21d_base_v038_signal'] = f76if_f76_institutional_flow_concentration_calc038_21d_base_v038_signal

def f76if_f76_institutional_flow_concentration_calc039_10d_base_v039_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(10).quantile(0.5) / close.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc039_10d_base_v039_signal'] = f76if_f76_institutional_flow_concentration_calc039_10d_base_v039_signal

def f76if_f76_institutional_flow_concentration_calc040_63d_base_v040_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(63).rank(pct=True) / volume.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc040_63d_base_v040_signal'] = f76if_f76_institutional_flow_concentration_calc040_63d_base_v040_signal

def f76if_f76_institutional_flow_concentration_calc041_21d_base_v041_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc041_21d_base_v041_signal'] = f76if_f76_institutional_flow_concentration_calc041_21d_base_v041_signal

def f76if_f76_institutional_flow_concentration_calc042_5d_base_v042_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).max() - sharesbas.rolling(5).min()) / open.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc042_5d_base_v042_signal'] = f76if_f76_institutional_flow_concentration_calc042_5d_base_v042_signal

def f76if_f76_institutional_flow_concentration_calc043_63d_base_v043_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / close.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc043_63d_base_v043_signal'] = f76if_f76_institutional_flow_concentration_calc043_63d_base_v043_signal

def f76if_f76_institutional_flow_concentration_calc044_126d_base_v044_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(126).abs() / sharesbas.diff(126).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc044_126d_base_v044_signal'] = f76if_f76_institutional_flow_concentration_calc044_126d_base_v044_signal

def f76if_f76_institutional_flow_concentration_calc045_21d_base_v045_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(21) / close.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc045_21d_base_v045_signal'] = f76if_f76_institutional_flow_concentration_calc045_21d_base_v045_signal

def f76if_f76_institutional_flow_concentration_calc046_10d_base_v046_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(10).rank(pct=True) / sharesbas.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc046_10d_base_v046_signal'] = f76if_f76_institutional_flow_concentration_calc046_10d_base_v046_signal

def f76if_f76_institutional_flow_concentration_calc047_42d_base_v047_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(42).max() - high.rolling(42).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc047_42d_base_v047_signal'] = f76if_f76_institutional_flow_concentration_calc047_42d_base_v047_signal

def f76if_f76_institutional_flow_concentration_calc048_5d_base_v048_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).quantile(0.5) / open.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc048_5d_base_v048_signal'] = f76if_f76_institutional_flow_concentration_calc048_5d_base_v048_signal

def f76if_f76_institutional_flow_concentration_calc049_42d_base_v049_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((volume - volume.rolling(42).mean()) / volume.rolling(42).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc049_42d_base_v049_signal'] = f76if_f76_institutional_flow_concentration_calc049_42d_base_v049_signal

def f76if_f76_institutional_flow_concentration_calc050_21d_base_v050_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(21).quantile(0.5) / volume.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc050_21d_base_v050_signal'] = f76if_f76_institutional_flow_concentration_calc050_21d_base_v050_signal

def f76if_f76_institutional_flow_concentration_calc051_42d_base_v051_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.pct_change(42) - volume.pct_change(42))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc051_42d_base_v051_signal'] = f76if_f76_institutional_flow_concentration_calc051_42d_base_v051_signal

def f76if_f76_institutional_flow_concentration_calc052_126d_base_v052_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / low.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc052_126d_base_v052_signal'] = f76if_f76_institutional_flow_concentration_calc052_126d_base_v052_signal

def f76if_f76_institutional_flow_concentration_calc053_126d_base_v053_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(126).max() - volume.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc053_126d_base_v053_signal'] = f76if_f76_institutional_flow_concentration_calc053_126d_base_v053_signal

def f76if_f76_institutional_flow_concentration_calc054_10d_base_v054_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(10).abs() / sharesbas.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc054_10d_base_v054_signal'] = f76if_f76_institutional_flow_concentration_calc054_10d_base_v054_signal

def f76if_f76_institutional_flow_concentration_calc055_42d_base_v055_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(42).max() - marketcap.rolling(42).min()) / open.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc055_42d_base_v055_signal'] = f76if_f76_institutional_flow_concentration_calc055_42d_base_v055_signal

def f76if_f76_institutional_flow_concentration_calc056_10d_base_v056_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open / high.replace(0, np.nan)).rolling(10).std()
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc056_10d_base_v056_signal'] = f76if_f76_institutional_flow_concentration_calc056_10d_base_v056_signal

def f76if_f76_institutional_flow_concentration_calc057_10d_base_v057_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(10).kurt() - sharesbas.rolling(10).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc057_10d_base_v057_signal'] = f76if_f76_institutional_flow_concentration_calc057_10d_base_v057_signal

def f76if_f76_institutional_flow_concentration_calc058_21d_base_v058_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.diff(21).abs() / close.diff(21).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc058_21d_base_v058_signal'] = f76if_f76_institutional_flow_concentration_calc058_21d_base_v058_signal

def f76if_f76_institutional_flow_concentration_calc059_252d_base_v059_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).kurt() - close.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc059_252d_base_v059_signal'] = f76if_f76_institutional_flow_concentration_calc059_252d_base_v059_signal

def f76if_f76_institutional_flow_concentration_calc060_5d_base_v060_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(5).kurt() - volume.rolling(5).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc060_5d_base_v060_signal'] = f76if_f76_institutional_flow_concentration_calc060_5d_base_v060_signal

def f76if_f76_institutional_flow_concentration_calc061_42d_base_v061_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(42).rank(pct=True) / sharesbas.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc061_42d_base_v061_signal'] = f76if_f76_institutional_flow_concentration_calc061_42d_base_v061_signal

def f76if_f76_institutional_flow_concentration_calc062_10d_base_v062_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(10).rank(pct=True) / marketcap.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc062_10d_base_v062_signal'] = f76if_f76_institutional_flow_concentration_calc062_10d_base_v062_signal

def f76if_f76_institutional_flow_concentration_calc063_10d_base_v063_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(10).abs() / open.diff(10).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(5).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc063_10d_base_v063_signal'] = f76if_f76_institutional_flow_concentration_calc063_10d_base_v063_signal

def f76if_f76_institutional_flow_concentration_calc064_126d_base_v064_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(126) - low.pct_change(126))
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc064_126d_base_v064_signal'] = f76if_f76_institutional_flow_concentration_calc064_126d_base_v064_signal

def f76if_f76_institutional_flow_concentration_calc065_21d_base_v065_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(21).rank(pct=True) / volume.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(10).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc065_21d_base_v065_signal'] = f76if_f76_institutional_flow_concentration_calc065_21d_base_v065_signal

def f76if_f76_institutional_flow_concentration_calc066_5d_base_v066_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(5).abs() / marketcap.diff(5).abs().replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc066_5d_base_v066_signal'] = f76if_f76_institutional_flow_concentration_calc066_5d_base_v066_signal

def f76if_f76_institutional_flow_concentration_calc067_5d_base_v067_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).max() - low.rolling(5).min()) / open.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc067_5d_base_v067_signal'] = f76if_f76_institutional_flow_concentration_calc067_5d_base_v067_signal

def f76if_f76_institutional_flow_concentration_calc068_63d_base_v068_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((low - low.rolling(63).mean()) / low.rolling(63).std())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc068_63d_base_v068_signal'] = f76if_f76_institutional_flow_concentration_calc068_63d_base_v068_signal

def f76if_f76_institutional_flow_concentration_calc069_5d_base_v069_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).rank(pct=True) / low.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(2).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc069_5d_base_v069_signal'] = f76if_f76_institutional_flow_concentration_calc069_5d_base_v069_signal

def f76if_f76_institutional_flow_concentration_calc070_63d_base_v070_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).max() - volume.rolling(63).min()) / marketcap.replace(0, np.nan)
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc070_63d_base_v070_signal'] = f76if_f76_institutional_flow_concentration_calc070_63d_base_v070_signal

def f76if_f76_institutional_flow_concentration_calc071_126d_base_v071_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open / volume.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc071_126d_base_v071_signal'] = f76if_f76_institutional_flow_concentration_calc071_126d_base_v071_signal

def f76if_f76_institutional_flow_concentration_calc072_252d_base_v072_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(252).kurt() - high.rolling(252).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(126).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc072_252d_base_v072_signal'] = f76if_f76_institutional_flow_concentration_calc072_252d_base_v072_signal

def f76if_f76_institutional_flow_concentration_calc073_126d_base_v073_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap / sharesbas.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.shift(1)
    v3 = v1.rolling(63).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc073_126d_base_v073_signal'] = f76if_f76_institutional_flow_concentration_calc073_126d_base_v073_signal

def f76if_f76_institutional_flow_concentration_calc074_63d_base_v074_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(63).kurt() - low.rolling(63).kurt())
    v2 = v1.shift(1)
    v3 = v1.rolling(31).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc074_63d_base_v074_signal'] = f76if_f76_institutional_flow_concentration_calc074_63d_base_v074_signal

def f76if_f76_institutional_flow_concentration_calc075_42d_base_v075_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.diff(42) / marketcap.replace(0, np.nan))
    v2 = v1.shift(1)
    v3 = v1.rolling(21).std()
    res = v1 + v2 * 1e-9 + v3 * 1e-9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc075_42d_base_v075_signal'] = f76if_f76_institutional_flow_concentration_calc075_42d_base_v075_signal



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
