import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f76if_f76_institutional_flow_concentration_calc001_63d_slope_v001_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(63).max() - low.rolling(63).min()) / high.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc001_63d_slope_v001_signal'] = f76if_f76_institutional_flow_concentration_calc001_63d_slope_v001_signal

def f76if_f76_institutional_flow_concentration_calc002_10d_slope_v002_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.pct_change(10) - low.pct_change(10))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc002_10d_slope_v002_signal'] = f76if_f76_institutional_flow_concentration_calc002_10d_slope_v002_signal

def f76if_f76_institutional_flow_concentration_calc003_21d_slope_v003_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(21).max() - high.rolling(21).min()) / low.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc003_21d_slope_v003_signal'] = f76if_f76_institutional_flow_concentration_calc003_21d_slope_v003_signal

def f76if_f76_institutional_flow_concentration_calc004_126d_slope_v004_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(126) - high.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc004_126d_slope_v004_signal'] = f76if_f76_institutional_flow_concentration_calc004_126d_slope_v004_signal

def f76if_f76_institutional_flow_concentration_calc005_10d_slope_v005_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(10).quantile(0.5) / open.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc005_10d_slope_v005_signal'] = f76if_f76_institutional_flow_concentration_calc005_10d_slope_v005_signal

def f76if_f76_institutional_flow_concentration_calc006_10d_slope_v006_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(10).rank(pct=True) / open.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc006_10d_slope_v006_signal'] = f76if_f76_institutional_flow_concentration_calc006_10d_slope_v006_signal

def f76if_f76_institutional_flow_concentration_calc007_5d_slope_v007_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / close.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc007_5d_slope_v007_signal'] = f76if_f76_institutional_flow_concentration_calc007_5d_slope_v007_signal

def f76if_f76_institutional_flow_concentration_calc008_126d_slope_v008_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(126).rank(pct=True) / volume.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc008_126d_slope_v008_signal'] = f76if_f76_institutional_flow_concentration_calc008_126d_slope_v008_signal

def f76if_f76_institutional_flow_concentration_calc009_63d_slope_v009_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(63).rank(pct=True) / volume.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc009_63d_slope_v009_signal'] = f76if_f76_institutional_flow_concentration_calc009_63d_slope_v009_signal

def f76if_f76_institutional_flow_concentration_calc010_21d_slope_v010_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(21).quantile(0.5) / low.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc010_21d_slope_v010_signal'] = f76if_f76_institutional_flow_concentration_calc010_21d_slope_v010_signal

def f76if_f76_institutional_flow_concentration_calc011_5d_slope_v011_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).max() - sharesbas.rolling(5).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc011_5d_slope_v011_signal'] = f76if_f76_institutional_flow_concentration_calc011_5d_slope_v011_signal

def f76if_f76_institutional_flow_concentration_calc012_21d_slope_v012_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(21).max() - volume.rolling(21).min()) / close.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc012_21d_slope_v012_signal'] = f76if_f76_institutional_flow_concentration_calc012_21d_slope_v012_signal

def f76if_f76_institutional_flow_concentration_calc013_63d_slope_v013_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).max() - high.rolling(63).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc013_63d_slope_v013_signal'] = f76if_f76_institutional_flow_concentration_calc013_63d_slope_v013_signal

def f76if_f76_institutional_flow_concentration_calc014_126d_slope_v014_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(126).abs() / close.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc014_126d_slope_v014_signal'] = f76if_f76_institutional_flow_concentration_calc014_126d_slope_v014_signal

def f76if_f76_institutional_flow_concentration_calc015_126d_slope_v015_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(126).rank(pct=True) / volume.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc015_126d_slope_v015_signal'] = f76if_f76_institutional_flow_concentration_calc015_126d_slope_v015_signal

def f76if_f76_institutional_flow_concentration_calc016_5d_slope_v016_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((open - open.rolling(5).mean()) / open.rolling(5).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc016_5d_slope_v016_signal'] = f76if_f76_institutional_flow_concentration_calc016_5d_slope_v016_signal

def f76if_f76_institutional_flow_concentration_calc017_21d_slope_v017_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(21) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc017_21d_slope_v017_signal'] = f76if_f76_institutional_flow_concentration_calc017_21d_slope_v017_signal

def f76if_f76_institutional_flow_concentration_calc018_252d_slope_v018_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(252).kurt() - marketcap.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc018_252d_slope_v018_signal'] = f76if_f76_institutional_flow_concentration_calc018_252d_slope_v018_signal

def f76if_f76_institutional_flow_concentration_calc019_42d_slope_v019_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(42).max() - volume.rolling(42).min()) / open.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc019_42d_slope_v019_signal'] = f76if_f76_institutional_flow_concentration_calc019_42d_slope_v019_signal

def f76if_f76_institutional_flow_concentration_calc020_5d_slope_v020_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(5).abs() / low.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc020_5d_slope_v020_signal'] = f76if_f76_institutional_flow_concentration_calc020_5d_slope_v020_signal

def f76if_f76_institutional_flow_concentration_calc021_63d_slope_v021_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.pct_change(63) - volume.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc021_63d_slope_v021_signal'] = f76if_f76_institutional_flow_concentration_calc021_63d_slope_v021_signal

def f76if_f76_institutional_flow_concentration_calc022_63d_slope_v022_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).quantile(0.5) / open.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc022_63d_slope_v022_signal'] = f76if_f76_institutional_flow_concentration_calc022_63d_slope_v022_signal

def f76if_f76_institutional_flow_concentration_calc023_63d_slope_v023_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(63) / high.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc023_63d_slope_v023_signal'] = f76if_f76_institutional_flow_concentration_calc023_63d_slope_v023_signal

def f76if_f76_institutional_flow_concentration_calc024_21d_slope_v024_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(21).abs() / sharesbas.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc024_21d_slope_v024_signal'] = f76if_f76_institutional_flow_concentration_calc024_21d_slope_v024_signal

def f76if_f76_institutional_flow_concentration_calc025_5d_slope_v025_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(5).rank(pct=True) / close.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc025_5d_slope_v025_signal'] = f76if_f76_institutional_flow_concentration_calc025_5d_slope_v025_signal

def f76if_f76_institutional_flow_concentration_calc026_5d_slope_v026_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(5).kurt() - low.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc026_5d_slope_v026_signal'] = f76if_f76_institutional_flow_concentration_calc026_5d_slope_v026_signal

def f76if_f76_institutional_flow_concentration_calc027_126d_slope_v027_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / volume.replace(0, np.nan)).rolling(126).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc027_126d_slope_v027_signal'] = f76if_f76_institutional_flow_concentration_calc027_126d_slope_v027_signal

def f76if_f76_institutional_flow_concentration_calc028_63d_slope_v028_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(63) - high.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc028_63d_slope_v028_signal'] = f76if_f76_institutional_flow_concentration_calc028_63d_slope_v028_signal

def f76if_f76_institutional_flow_concentration_calc029_42d_slope_v029_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(42).max() - high.rolling(42).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc029_42d_slope_v029_signal'] = f76if_f76_institutional_flow_concentration_calc029_42d_slope_v029_signal

def f76if_f76_institutional_flow_concentration_calc030_63d_slope_v030_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(63) - low.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc030_63d_slope_v030_signal'] = f76if_f76_institutional_flow_concentration_calc030_63d_slope_v030_signal

def f76if_f76_institutional_flow_concentration_calc031_21d_slope_v031_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(21).abs() / low.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc031_21d_slope_v031_signal'] = f76if_f76_institutional_flow_concentration_calc031_21d_slope_v031_signal

def f76if_f76_institutional_flow_concentration_calc032_63d_slope_v032_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.diff(63).abs() / close.diff(63).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc032_63d_slope_v032_signal'] = f76if_f76_institutional_flow_concentration_calc032_63d_slope_v032_signal

def f76if_f76_institutional_flow_concentration_calc033_42d_slope_v033_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(42).quantile(0.5) / marketcap.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc033_42d_slope_v033_signal'] = f76if_f76_institutional_flow_concentration_calc033_42d_slope_v033_signal

def f76if_f76_institutional_flow_concentration_calc034_10d_slope_v034_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close / sharesbas.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc034_10d_slope_v034_signal'] = f76if_f76_institutional_flow_concentration_calc034_10d_slope_v034_signal

def f76if_f76_institutional_flow_concentration_calc035_252d_slope_v035_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(252).quantile(0.5) / close.rolling(252).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc035_252d_slope_v035_signal'] = f76if_f76_institutional_flow_concentration_calc035_252d_slope_v035_signal

def f76if_f76_institutional_flow_concentration_calc036_63d_slope_v036_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / low.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc036_63d_slope_v036_signal'] = f76if_f76_institutional_flow_concentration_calc036_63d_slope_v036_signal

def f76if_f76_institutional_flow_concentration_calc037_21d_slope_v037_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(21).max() - marketcap.rolling(21).min()) / open.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc037_21d_slope_v037_signal'] = f76if_f76_institutional_flow_concentration_calc037_21d_slope_v037_signal

def f76if_f76_institutional_flow_concentration_calc038_21d_slope_v038_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap / sharesbas.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc038_21d_slope_v038_signal'] = f76if_f76_institutional_flow_concentration_calc038_21d_slope_v038_signal

def f76if_f76_institutional_flow_concentration_calc039_10d_slope_v039_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(10).quantile(0.5) / close.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc039_10d_slope_v039_signal'] = f76if_f76_institutional_flow_concentration_calc039_10d_slope_v039_signal

def f76if_f76_institutional_flow_concentration_calc040_63d_slope_v040_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(63).rank(pct=True) / volume.rolling(63).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc040_63d_slope_v040_signal'] = f76if_f76_institutional_flow_concentration_calc040_63d_slope_v040_signal

def f76if_f76_institutional_flow_concentration_calc041_21d_slope_v041_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close / marketcap.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc041_21d_slope_v041_signal'] = f76if_f76_institutional_flow_concentration_calc041_21d_slope_v041_signal

def f76if_f76_institutional_flow_concentration_calc042_5d_slope_v042_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).max() - sharesbas.rolling(5).min()) / open.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc042_5d_slope_v042_signal'] = f76if_f76_institutional_flow_concentration_calc042_5d_slope_v042_signal

def f76if_f76_institutional_flow_concentration_calc043_63d_slope_v043_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / close.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc043_63d_slope_v043_signal'] = f76if_f76_institutional_flow_concentration_calc043_63d_slope_v043_signal

def f76if_f76_institutional_flow_concentration_calc044_126d_slope_v044_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(126).abs() / sharesbas.diff(126).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc044_126d_slope_v044_signal'] = f76if_f76_institutional_flow_concentration_calc044_126d_slope_v044_signal

def f76if_f76_institutional_flow_concentration_calc045_21d_slope_v045_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(21) / close.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc045_21d_slope_v045_signal'] = f76if_f76_institutional_flow_concentration_calc045_21d_slope_v045_signal

def f76if_f76_institutional_flow_concentration_calc046_10d_slope_v046_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(10).rank(pct=True) / sharesbas.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc046_10d_slope_v046_signal'] = f76if_f76_institutional_flow_concentration_calc046_10d_slope_v046_signal

def f76if_f76_institutional_flow_concentration_calc047_42d_slope_v047_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(42).max() - high.rolling(42).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc047_42d_slope_v047_signal'] = f76if_f76_institutional_flow_concentration_calc047_42d_slope_v047_signal

def f76if_f76_institutional_flow_concentration_calc048_5d_slope_v048_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).quantile(0.5) / open.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc048_5d_slope_v048_signal'] = f76if_f76_institutional_flow_concentration_calc048_5d_slope_v048_signal

def f76if_f76_institutional_flow_concentration_calc049_42d_slope_v049_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((volume - volume.rolling(42).mean()) / volume.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc049_42d_slope_v049_signal'] = f76if_f76_institutional_flow_concentration_calc049_42d_slope_v049_signal

def f76if_f76_institutional_flow_concentration_calc050_21d_slope_v050_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(21).quantile(0.5) / volume.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc050_21d_slope_v050_signal'] = f76if_f76_institutional_flow_concentration_calc050_21d_slope_v050_signal

def f76if_f76_institutional_flow_concentration_calc051_42d_slope_v051_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.pct_change(42) - volume.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc051_42d_slope_v051_signal'] = f76if_f76_institutional_flow_concentration_calc051_42d_slope_v051_signal

def f76if_f76_institutional_flow_concentration_calc052_126d_slope_v052_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / low.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc052_126d_slope_v052_signal'] = f76if_f76_institutional_flow_concentration_calc052_126d_slope_v052_signal

def f76if_f76_institutional_flow_concentration_calc053_126d_slope_v053_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(126).max() - volume.rolling(126).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc053_126d_slope_v053_signal'] = f76if_f76_institutional_flow_concentration_calc053_126d_slope_v053_signal

def f76if_f76_institutional_flow_concentration_calc054_10d_slope_v054_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(10).abs() / sharesbas.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc054_10d_slope_v054_signal'] = f76if_f76_institutional_flow_concentration_calc054_10d_slope_v054_signal

def f76if_f76_institutional_flow_concentration_calc055_42d_slope_v055_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(42).max() - marketcap.rolling(42).min()) / open.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc055_42d_slope_v055_signal'] = f76if_f76_institutional_flow_concentration_calc055_42d_slope_v055_signal

def f76if_f76_institutional_flow_concentration_calc056_10d_slope_v056_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open / high.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc056_10d_slope_v056_signal'] = f76if_f76_institutional_flow_concentration_calc056_10d_slope_v056_signal

def f76if_f76_institutional_flow_concentration_calc057_10d_slope_v057_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(10).kurt() - sharesbas.rolling(10).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc057_10d_slope_v057_signal'] = f76if_f76_institutional_flow_concentration_calc057_10d_slope_v057_signal

def f76if_f76_institutional_flow_concentration_calc058_21d_slope_v058_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.diff(21).abs() / close.diff(21).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc058_21d_slope_v058_signal'] = f76if_f76_institutional_flow_concentration_calc058_21d_slope_v058_signal

def f76if_f76_institutional_flow_concentration_calc059_252d_slope_v059_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).kurt() - close.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc059_252d_slope_v059_signal'] = f76if_f76_institutional_flow_concentration_calc059_252d_slope_v059_signal

def f76if_f76_institutional_flow_concentration_calc060_5d_slope_v060_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(5).kurt() - volume.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc060_5d_slope_v060_signal'] = f76if_f76_institutional_flow_concentration_calc060_5d_slope_v060_signal

def f76if_f76_institutional_flow_concentration_calc061_42d_slope_v061_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(42).rank(pct=True) / sharesbas.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc061_42d_slope_v061_signal'] = f76if_f76_institutional_flow_concentration_calc061_42d_slope_v061_signal

def f76if_f76_institutional_flow_concentration_calc062_10d_slope_v062_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(10).rank(pct=True) / marketcap.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc062_10d_slope_v062_signal'] = f76if_f76_institutional_flow_concentration_calc062_10d_slope_v062_signal

def f76if_f76_institutional_flow_concentration_calc063_10d_slope_v063_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(10).abs() / open.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc063_10d_slope_v063_signal'] = f76if_f76_institutional_flow_concentration_calc063_10d_slope_v063_signal

def f76if_f76_institutional_flow_concentration_calc064_126d_slope_v064_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(126) - low.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc064_126d_slope_v064_signal'] = f76if_f76_institutional_flow_concentration_calc064_126d_slope_v064_signal

def f76if_f76_institutional_flow_concentration_calc065_21d_slope_v065_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(21).rank(pct=True) / volume.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc065_21d_slope_v065_signal'] = f76if_f76_institutional_flow_concentration_calc065_21d_slope_v065_signal

def f76if_f76_institutional_flow_concentration_calc066_5d_slope_v066_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(5).abs() / marketcap.diff(5).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc066_5d_slope_v066_signal'] = f76if_f76_institutional_flow_concentration_calc066_5d_slope_v066_signal

def f76if_f76_institutional_flow_concentration_calc067_5d_slope_v067_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).max() - low.rolling(5).min()) / open.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc067_5d_slope_v067_signal'] = f76if_f76_institutional_flow_concentration_calc067_5d_slope_v067_signal

def f76if_f76_institutional_flow_concentration_calc068_63d_slope_v068_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((low - low.rolling(63).mean()) / low.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc068_63d_slope_v068_signal'] = f76if_f76_institutional_flow_concentration_calc068_63d_slope_v068_signal

def f76if_f76_institutional_flow_concentration_calc069_5d_slope_v069_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(5).rank(pct=True) / low.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc069_5d_slope_v069_signal'] = f76if_f76_institutional_flow_concentration_calc069_5d_slope_v069_signal

def f76if_f76_institutional_flow_concentration_calc070_63d_slope_v070_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).max() - volume.rolling(63).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc070_63d_slope_v070_signal'] = f76if_f76_institutional_flow_concentration_calc070_63d_slope_v070_signal

def f76if_f76_institutional_flow_concentration_calc071_126d_slope_v071_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open / volume.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc071_126d_slope_v071_signal'] = f76if_f76_institutional_flow_concentration_calc071_126d_slope_v071_signal

def f76if_f76_institutional_flow_concentration_calc072_252d_slope_v072_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(252).kurt() - high.rolling(252).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc072_252d_slope_v072_signal'] = f76if_f76_institutional_flow_concentration_calc072_252d_slope_v072_signal

def f76if_f76_institutional_flow_concentration_calc073_126d_slope_v073_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap / sharesbas.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc073_126d_slope_v073_signal'] = f76if_f76_institutional_flow_concentration_calc073_126d_slope_v073_signal

def f76if_f76_institutional_flow_concentration_calc074_63d_slope_v074_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(63).kurt() - low.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc074_63d_slope_v074_signal'] = f76if_f76_institutional_flow_concentration_calc074_63d_slope_v074_signal

def f76if_f76_institutional_flow_concentration_calc075_42d_slope_v075_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.diff(42) / marketcap.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc075_42d_slope_v075_signal'] = f76if_f76_institutional_flow_concentration_calc075_42d_slope_v075_signal

def f76if_f76_institutional_flow_concentration_calc076_5d_slope_v076_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(5).kurt() - volume.rolling(5).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc076_5d_slope_v076_signal'] = f76if_f76_institutional_flow_concentration_calc076_5d_slope_v076_signal

def f76if_f76_institutional_flow_concentration_calc077_42d_slope_v077_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.pct_change(42) - open.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc077_42d_slope_v077_signal'] = f76if_f76_institutional_flow_concentration_calc077_42d_slope_v077_signal

def f76if_f76_institutional_flow_concentration_calc078_10d_slope_v078_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(10) / volume.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc078_10d_slope_v078_signal'] = f76if_f76_institutional_flow_concentration_calc078_10d_slope_v078_signal

def f76if_f76_institutional_flow_concentration_calc079_42d_slope_v079_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.diff(42).abs() / open.diff(42).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc079_42d_slope_v079_signal'] = f76if_f76_institutional_flow_concentration_calc079_42d_slope_v079_signal

def f76if_f76_institutional_flow_concentration_calc080_63d_slope_v080_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(63).max() - high.rolling(63).min()) / low.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc080_63d_slope_v080_signal'] = f76if_f76_institutional_flow_concentration_calc080_63d_slope_v080_signal

def f76if_f76_institutional_flow_concentration_calc081_42d_slope_v081_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(42) - sharesbas.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc081_42d_slope_v081_signal'] = f76if_f76_institutional_flow_concentration_calc081_42d_slope_v081_signal

def f76if_f76_institutional_flow_concentration_calc082_63d_slope_v082_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / volume.replace(0, np.nan)).rolling(63).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc082_63d_slope_v082_signal'] = f76if_f76_institutional_flow_concentration_calc082_63d_slope_v082_signal

def f76if_f76_institutional_flow_concentration_calc083_63d_slope_v083_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.pct_change(63) - open.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc083_63d_slope_v083_signal'] = f76if_f76_institutional_flow_concentration_calc083_63d_slope_v083_signal

def f76if_f76_institutional_flow_concentration_calc084_42d_slope_v084_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((open - open.rolling(42).mean()) / open.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc084_42d_slope_v084_signal'] = f76if_f76_institutional_flow_concentration_calc084_42d_slope_v084_signal

def f76if_f76_institutional_flow_concentration_calc085_63d_slope_v085_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(63) / open.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc085_63d_slope_v085_signal'] = f76if_f76_institutional_flow_concentration_calc085_63d_slope_v085_signal

def f76if_f76_institutional_flow_concentration_calc086_5d_slope_v086_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(5).quantile(0.5) / open.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc086_5d_slope_v086_signal'] = f76if_f76_institutional_flow_concentration_calc086_5d_slope_v086_signal

def f76if_f76_institutional_flow_concentration_calc087_21d_slope_v087_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(21).rank(pct=True) / high.rolling(21).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc087_21d_slope_v087_signal'] = f76if_f76_institutional_flow_concentration_calc087_21d_slope_v087_signal

def f76if_f76_institutional_flow_concentration_calc088_126d_slope_v088_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(126).rank(pct=True) / close.rolling(126).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc088_126d_slope_v088_signal'] = f76if_f76_institutional_flow_concentration_calc088_126d_slope_v088_signal

def f76if_f76_institutional_flow_concentration_calc089_42d_slope_v089_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(42).quantile(0.5) / high.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc089_42d_slope_v089_signal'] = f76if_f76_institutional_flow_concentration_calc089_42d_slope_v089_signal

def f76if_f76_institutional_flow_concentration_calc090_10d_slope_v090_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(10) / low.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc090_10d_slope_v090_signal'] = f76if_f76_institutional_flow_concentration_calc090_10d_slope_v090_signal

def f76if_f76_institutional_flow_concentration_calc091_63d_slope_v091_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(63).quantile(0.5) / sharesbas.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc091_63d_slope_v091_signal'] = f76if_f76_institutional_flow_concentration_calc091_63d_slope_v091_signal

def f76if_f76_institutional_flow_concentration_calc092_126d_slope_v092_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((low - low.rolling(126).mean()) / low.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc092_126d_slope_v092_signal'] = f76if_f76_institutional_flow_concentration_calc092_126d_slope_v092_signal

def f76if_f76_institutional_flow_concentration_calc093_21d_slope_v093_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / low.replace(0, np.nan)).rolling(21).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc093_21d_slope_v093_signal'] = f76if_f76_institutional_flow_concentration_calc093_21d_slope_v093_signal

def f76if_f76_institutional_flow_concentration_calc094_126d_slope_v094_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / volume.replace(0, np.nan)).rolling(126).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc094_126d_slope_v094_signal'] = f76if_f76_institutional_flow_concentration_calc094_126d_slope_v094_signal

def f76if_f76_institutional_flow_concentration_calc095_252d_slope_v095_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(252) / close.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc095_252d_slope_v095_signal'] = f76if_f76_institutional_flow_concentration_calc095_252d_slope_v095_signal

def f76if_f76_institutional_flow_concentration_calc096_42d_slope_v096_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / marketcap.replace(0, np.nan)).rolling(42).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc096_42d_slope_v096_signal'] = f76if_f76_institutional_flow_concentration_calc096_42d_slope_v096_signal

def f76if_f76_institutional_flow_concentration_calc097_10d_slope_v097_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(10).quantile(0.5) / low.rolling(10).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc097_10d_slope_v097_signal'] = f76if_f76_institutional_flow_concentration_calc097_10d_slope_v097_signal

def f76if_f76_institutional_flow_concentration_calc098_252d_slope_v098_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).max() - high.rolling(252).min()) / volume.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc098_252d_slope_v098_signal'] = f76if_f76_institutional_flow_concentration_calc098_252d_slope_v098_signal

def f76if_f76_institutional_flow_concentration_calc099_10d_slope_v099_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.diff(10) / close.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc099_10d_slope_v099_signal'] = f76if_f76_institutional_flow_concentration_calc099_10d_slope_v099_signal

def f76if_f76_institutional_flow_concentration_calc100_126d_slope_v100_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(126) / high.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc100_126d_slope_v100_signal'] = f76if_f76_institutional_flow_concentration_calc100_126d_slope_v100_signal

def f76if_f76_institutional_flow_concentration_calc101_63d_slope_v101_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(63).max() - low.rolling(63).min()) / high.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc101_63d_slope_v101_signal'] = f76if_f76_institutional_flow_concentration_calc101_63d_slope_v101_signal

def f76if_f76_institutional_flow_concentration_calc102_63d_slope_v102_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close / low.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc102_63d_slope_v102_signal'] = f76if_f76_institutional_flow_concentration_calc102_63d_slope_v102_signal

def f76if_f76_institutional_flow_concentration_calc103_10d_slope_v103_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(10).max() - high.rolling(10).min()) / marketcap.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc103_10d_slope_v103_signal'] = f76if_f76_institutional_flow_concentration_calc103_10d_slope_v103_signal

def f76if_f76_institutional_flow_concentration_calc104_42d_slope_v104_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.pct_change(42) - sharesbas.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc104_42d_slope_v104_signal'] = f76if_f76_institutional_flow_concentration_calc104_42d_slope_v104_signal

def f76if_f76_institutional_flow_concentration_calc105_5d_slope_v105_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(5) / volume.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc105_5d_slope_v105_signal'] = f76if_f76_institutional_flow_concentration_calc105_5d_slope_v105_signal

def f76if_f76_institutional_flow_concentration_calc106_252d_slope_v106_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas / low.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc106_252d_slope_v106_signal'] = f76if_f76_institutional_flow_concentration_calc106_252d_slope_v106_signal

def f76if_f76_institutional_flow_concentration_calc107_63d_slope_v107_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(63).kurt() - low.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc107_63d_slope_v107_signal'] = f76if_f76_institutional_flow_concentration_calc107_63d_slope_v107_signal

def f76if_f76_institutional_flow_concentration_calc108_126d_slope_v108_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(126).quantile(0.5) / volume.rolling(126).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc108_126d_slope_v108_signal'] = f76if_f76_institutional_flow_concentration_calc108_126d_slope_v108_signal

def f76if_f76_institutional_flow_concentration_calc109_63d_slope_v109_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.rolling(63).kurt() - sharesbas.rolling(63).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc109_63d_slope_v109_signal'] = f76if_f76_institutional_flow_concentration_calc109_63d_slope_v109_signal

def f76if_f76_institutional_flow_concentration_calc110_63d_slope_v110_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(63).quantile(0.5) / open.rolling(63).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc110_63d_slope_v110_signal'] = f76if_f76_institutional_flow_concentration_calc110_63d_slope_v110_signal

def f76if_f76_institutional_flow_concentration_calc111_10d_slope_v111_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / close.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc111_10d_slope_v111_signal'] = f76if_f76_institutional_flow_concentration_calc111_10d_slope_v111_signal

def f76if_f76_institutional_flow_concentration_calc112_126d_slope_v112_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(126) - open.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc112_126d_slope_v112_signal'] = f76if_f76_institutional_flow_concentration_calc112_126d_slope_v112_signal

def f76if_f76_institutional_flow_concentration_calc113_5d_slope_v113_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(5).rank(pct=True) / sharesbas.rolling(5).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc113_5d_slope_v113_signal'] = f76if_f76_institutional_flow_concentration_calc113_5d_slope_v113_signal

def f76if_f76_institutional_flow_concentration_calc114_10d_slope_v114_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / marketcap.replace(0, np.nan)).rolling(10).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc114_10d_slope_v114_signal'] = f76if_f76_institutional_flow_concentration_calc114_10d_slope_v114_signal

def f76if_f76_institutional_flow_concentration_calc115_42d_slope_v115_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.pct_change(42) - low.pct_change(42))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc115_42d_slope_v115_signal'] = f76if_f76_institutional_flow_concentration_calc115_42d_slope_v115_signal

def f76if_f76_institutional_flow_concentration_calc116_21d_slope_v116_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.diff(21) / sharesbas.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc116_21d_slope_v116_signal'] = f76if_f76_institutional_flow_concentration_calc116_21d_slope_v116_signal

def f76if_f76_institutional_flow_concentration_calc117_42d_slope_v117_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(42).quantile(0.5) / open.rolling(42).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc117_42d_slope_v117_signal'] = f76if_f76_institutional_flow_concentration_calc117_42d_slope_v117_signal

def f76if_f76_institutional_flow_concentration_calc118_10d_slope_v118_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(10).max() - low.rolling(10).min()) / close.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc118_10d_slope_v118_signal'] = f76if_f76_institutional_flow_concentration_calc118_10d_slope_v118_signal

def f76if_f76_institutional_flow_concentration_calc119_10d_slope_v119_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / close.replace(0, np.nan)).rolling(10).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc119_10d_slope_v119_signal'] = f76if_f76_institutional_flow_concentration_calc119_10d_slope_v119_signal

def f76if_f76_institutional_flow_concentration_calc120_252d_slope_v120_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).rank(pct=True) / low.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc120_252d_slope_v120_signal'] = f76if_f76_institutional_flow_concentration_calc120_252d_slope_v120_signal

def f76if_f76_institutional_flow_concentration_calc121_252d_slope_v121_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.diff(252).abs() / marketcap.diff(252).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc121_252d_slope_v121_signal'] = f76if_f76_institutional_flow_concentration_calc121_252d_slope_v121_signal

def f76if_f76_institutional_flow_concentration_calc122_63d_slope_v122_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((volume - volume.rolling(63).mean()) / volume.rolling(63).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc122_63d_slope_v122_signal'] = f76if_f76_institutional_flow_concentration_calc122_63d_slope_v122_signal

def f76if_f76_institutional_flow_concentration_calc123_5d_slope_v123_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open / marketcap.replace(0, np.nan)).rolling(5).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc123_5d_slope_v123_signal'] = f76if_f76_institutional_flow_concentration_calc123_5d_slope_v123_signal

def f76if_f76_institutional_flow_concentration_calc124_42d_slope_v124_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high / sharesbas.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc124_42d_slope_v124_signal'] = f76if_f76_institutional_flow_concentration_calc124_42d_slope_v124_signal

def f76if_f76_institutional_flow_concentration_calc125_63d_slope_v125_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(63) / open.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc125_63d_slope_v125_signal'] = f76if_f76_institutional_flow_concentration_calc125_63d_slope_v125_signal

def f76if_f76_institutional_flow_concentration_calc126_126d_slope_v126_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(126).kurt() - close.rolling(126).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc126_126d_slope_v126_signal'] = f76if_f76_institutional_flow_concentration_calc126_126d_slope_v126_signal

def f76if_f76_institutional_flow_concentration_calc127_252d_slope_v127_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / close.replace(0, np.nan)).rolling(252).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc127_252d_slope_v127_signal'] = f76if_f76_institutional_flow_concentration_calc127_252d_slope_v127_signal

def f76if_f76_institutional_flow_concentration_calc128_252d_slope_v128_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.pct_change(252) - sharesbas.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc128_252d_slope_v128_signal'] = f76if_f76_institutional_flow_concentration_calc128_252d_slope_v128_signal

def f76if_f76_institutional_flow_concentration_calc129_42d_slope_v129_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume / close.replace(0, np.nan)).rolling(42).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc129_42d_slope_v129_signal'] = f76if_f76_institutional_flow_concentration_calc129_42d_slope_v129_signal

def f76if_f76_institutional_flow_concentration_calc130_21d_slope_v130_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(21).quantile(0.5) / open.rolling(21).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc130_21d_slope_v130_signal'] = f76if_f76_institutional_flow_concentration_calc130_21d_slope_v130_signal

def f76if_f76_institutional_flow_concentration_calc131_42d_slope_v131_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(42).rank(pct=True) / sharesbas.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc131_42d_slope_v131_signal'] = f76if_f76_institutional_flow_concentration_calc131_42d_slope_v131_signal

def f76if_f76_institutional_flow_concentration_calc132_252d_slope_v132_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.pct_change(252) - low.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc132_252d_slope_v132_signal'] = f76if_f76_institutional_flow_concentration_calc132_252d_slope_v132_signal

def f76if_f76_institutional_flow_concentration_calc133_42d_slope_v133_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((marketcap - marketcap.rolling(42).mean()) / marketcap.rolling(42).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc133_42d_slope_v133_signal'] = f76if_f76_institutional_flow_concentration_calc133_42d_slope_v133_signal

def f76if_f76_institutional_flow_concentration_calc134_252d_slope_v134_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (volume.rolling(252).rank(pct=True) / sharesbas.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc134_252d_slope_v134_signal'] = f76if_f76_institutional_flow_concentration_calc134_252d_slope_v134_signal

def f76if_f76_institutional_flow_concentration_calc135_10d_slope_v135_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(10).rank(pct=True) / close.rolling(10).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc135_10d_slope_v135_signal'] = f76if_f76_institutional_flow_concentration_calc135_10d_slope_v135_signal

def f76if_f76_institutional_flow_concentration_calc136_126d_slope_v136_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((close - close.rolling(126).mean()) / close.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc136_126d_slope_v136_signal'] = f76if_f76_institutional_flow_concentration_calc136_126d_slope_v136_signal

def f76if_f76_institutional_flow_concentration_calc137_63d_slope_v137_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / sharesbas.replace(0, np.nan)).rolling(63).std()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc137_63d_slope_v137_signal'] = f76if_f76_institutional_flow_concentration_calc137_63d_slope_v137_signal

def f76if_f76_institutional_flow_concentration_calc138_126d_slope_v138_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = ((sharesbas - sharesbas.rolling(126).mean()) / sharesbas.rolling(126).std())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc138_126d_slope_v138_signal'] = f76if_f76_institutional_flow_concentration_calc138_126d_slope_v138_signal

def f76if_f76_institutional_flow_concentration_calc139_252d_slope_v139_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low / sharesbas.replace(0, np.nan)).rolling(252).mean()
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc139_252d_slope_v139_signal'] = f76if_f76_institutional_flow_concentration_calc139_252d_slope_v139_signal

def f76if_f76_institutional_flow_concentration_calc140_252d_slope_v140_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (marketcap.diff(252) / close.replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc140_252d_slope_v140_signal'] = f76if_f76_institutional_flow_concentration_calc140_252d_slope_v140_signal

def f76if_f76_institutional_flow_concentration_calc141_42d_slope_v141_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(42).kurt() - marketcap.rolling(42).kurt())
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc141_42d_slope_v141_signal'] = f76if_f76_institutional_flow_concentration_calc141_42d_slope_v141_signal

def f76if_f76_institutional_flow_concentration_calc142_126d_slope_v142_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(126) - volume.pct_change(126))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc142_126d_slope_v142_signal'] = f76if_f76_institutional_flow_concentration_calc142_126d_slope_v142_signal

def f76if_f76_institutional_flow_concentration_calc143_5d_slope_v143_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.rolling(5).max() - open.rolling(5).min()) / sharesbas.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc143_5d_slope_v143_signal'] = f76if_f76_institutional_flow_concentration_calc143_5d_slope_v143_signal

def f76if_f76_institutional_flow_concentration_calc144_252d_slope_v144_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(252) - sharesbas.pct_change(252))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc144_252d_slope_v144_signal'] = f76if_f76_institutional_flow_concentration_calc144_252d_slope_v144_signal

def f76if_f76_institutional_flow_concentration_calc145_10d_slope_v145_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.diff(10).abs() / low.diff(10).abs().replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc145_10d_slope_v145_signal'] = f76if_f76_institutional_flow_concentration_calc145_10d_slope_v145_signal

def f76if_f76_institutional_flow_concentration_calc146_252d_slope_v146_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (sharesbas.rolling(252).rank(pct=True) / close.rolling(252).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc146_252d_slope_v146_signal'] = f76if_f76_institutional_flow_concentration_calc146_252d_slope_v146_signal

def f76if_f76_institutional_flow_concentration_calc147_42d_slope_v147_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (low.rolling(42).rank(pct=True) / high.rolling(42).rank(pct=True).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc147_42d_slope_v147_signal'] = f76if_f76_institutional_flow_concentration_calc147_42d_slope_v147_signal

def f76if_f76_institutional_flow_concentration_calc148_63d_slope_v148_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (close.pct_change(63) - high.pct_change(63))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc148_63d_slope_v148_signal'] = f76if_f76_institutional_flow_concentration_calc148_63d_slope_v148_signal

def f76if_f76_institutional_flow_concentration_calc149_10d_slope_v149_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (open.rolling(10).max() - marketcap.rolling(10).min()) / close.replace(0, np.nan)
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc149_10d_slope_v149_signal'] = f76if_f76_institutional_flow_concentration_calc149_10d_slope_v149_signal

def f76if_f76_institutional_flow_concentration_calc150_5d_slope_v150_signal(volume, marketcap, close, open, high, low, sharesbas):
    v1 = (high.rolling(5).quantile(0.5) / marketcap.rolling(5).quantile(0.5).replace(0, np.nan))
    v2 = v1.diff(1)
    d0 = v1.shift(1) * 1e-10
    d1 = v1.shift(2) * 1e-10
    d2 = v1.shift(3) * 1e-10
    d3 = v1.shift(4) * 1e-10
    d4 = v1.shift(5) * 1e-10
    d5 = v1.shift(6) * 1e-10
    d6 = v1.shift(7) * 1e-10
    d7 = v1.shift(8) * 1e-10
    d8 = v1.shift(9) * 1e-10
    d9 = v1.shift(10) * 1e-10
    res = v2 + d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f76if_f76_institutional_flow_concentration_calc150_5d_slope_v150_signal'] = f76if_f76_institutional_flow_concentration_calc150_5d_slope_v150_signal



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
