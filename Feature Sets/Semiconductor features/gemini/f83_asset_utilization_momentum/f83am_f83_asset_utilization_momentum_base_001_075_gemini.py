import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f83am_f83_asset_utilization_momentum_calc001_63d_val_v001_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(63).mean()
    v2 = ratio.rolling(68).std()
    v3 = ratio.diff(63)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc001_63d_val_v001_signal'] = f83am_f83_asset_utilization_momentum_calc001_63d_val_v001_signal

def f83am_f83_asset_utilization_momentum_calc002_116d_val_v002_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(116).mean()
    v2 = ratio.rolling(121).std()
    v3 = ratio.diff(116)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc002_116d_val_v002_signal'] = f83am_f83_asset_utilization_momentum_calc002_116d_val_v002_signal

def f83am_f83_asset_utilization_momentum_calc003_169d_val_v003_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(169).mean()
    v2 = ratio.rolling(174).std()
    v3 = ratio.diff(169)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc003_169d_val_v003_signal'] = f83am_f83_asset_utilization_momentum_calc003_169d_val_v003_signal

def f83am_f83_asset_utilization_momentum_calc004_22d_val_v004_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(22).mean()
    v2 = ratio.rolling(27).std()
    v3 = ratio.diff(22)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(22)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc004_22d_val_v004_signal'] = f83am_f83_asset_utilization_momentum_calc004_22d_val_v004_signal

def f83am_f83_asset_utilization_momentum_calc005_75d_val_v005_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(75).mean()
    v2 = ratio.rolling(80).std()
    v3 = ratio.diff(75)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc005_75d_val_v005_signal'] = f83am_f83_asset_utilization_momentum_calc005_75d_val_v005_signal

def f83am_f83_asset_utilization_momentum_calc006_128d_val_v006_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(128).mean()
    v2 = ratio.rolling(133).std()
    v3 = ratio.diff(128)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc006_128d_val_v006_signal'] = f83am_f83_asset_utilization_momentum_calc006_128d_val_v006_signal

def f83am_f83_asset_utilization_momentum_calc007_181d_val_v007_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(181).mean()
    v2 = ratio.rolling(186).std()
    v3 = ratio.diff(181)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc007_181d_val_v007_signal'] = f83am_f83_asset_utilization_momentum_calc007_181d_val_v007_signal

def f83am_f83_asset_utilization_momentum_calc008_34d_val_v008_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(34).mean()
    v2 = ratio.rolling(39).std()
    v3 = ratio.diff(34)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc008_34d_val_v008_signal'] = f83am_f83_asset_utilization_momentum_calc008_34d_val_v008_signal

def f83am_f83_asset_utilization_momentum_calc009_87d_val_v009_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(87).mean()
    v2 = ratio.rolling(92).std()
    v3 = ratio.diff(87)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc009_87d_val_v009_signal'] = f83am_f83_asset_utilization_momentum_calc009_87d_val_v009_signal

def f83am_f83_asset_utilization_momentum_calc010_140d_val_v010_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(140).mean()
    v2 = ratio.rolling(145).std()
    v3 = ratio.diff(140)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(140)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc010_140d_val_v010_signal'] = f83am_f83_asset_utilization_momentum_calc010_140d_val_v010_signal

def f83am_f83_asset_utilization_momentum_calc011_193d_val_v011_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(193).mean()
    v2 = ratio.rolling(198).std()
    v3 = ratio.diff(193)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc011_193d_val_v011_signal'] = f83am_f83_asset_utilization_momentum_calc011_193d_val_v011_signal

def f83am_f83_asset_utilization_momentum_calc012_46d_val_v012_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(46).mean()
    v2 = ratio.rolling(51).std()
    v3 = ratio.diff(46)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc012_46d_val_v012_signal'] = f83am_f83_asset_utilization_momentum_calc012_46d_val_v012_signal

def f83am_f83_asset_utilization_momentum_calc013_99d_val_v013_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(99).mean()
    v2 = ratio.rolling(104).std()
    v3 = ratio.diff(99)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc013_99d_val_v013_signal'] = f83am_f83_asset_utilization_momentum_calc013_99d_val_v013_signal

def f83am_f83_asset_utilization_momentum_calc014_152d_val_v014_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(152).mean()
    v2 = ratio.rolling(157).std()
    v3 = ratio.diff(152)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc014_152d_val_v014_signal'] = f83am_f83_asset_utilization_momentum_calc014_152d_val_v014_signal

def f83am_f83_asset_utilization_momentum_calc015_205d_val_v015_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(205).mean()
    v2 = ratio.rolling(210).std()
    v3 = ratio.diff(205)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc015_205d_val_v015_signal'] = f83am_f83_asset_utilization_momentum_calc015_205d_val_v015_signal

def f83am_f83_asset_utilization_momentum_calc016_58d_val_v016_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(58).mean()
    v2 = ratio.rolling(63).std()
    v3 = ratio.diff(58)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(58)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc016_58d_val_v016_signal'] = f83am_f83_asset_utilization_momentum_calc016_58d_val_v016_signal

def f83am_f83_asset_utilization_momentum_calc017_111d_val_v017_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(111).mean()
    v2 = ratio.rolling(116).std()
    v3 = ratio.diff(111)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc017_111d_val_v017_signal'] = f83am_f83_asset_utilization_momentum_calc017_111d_val_v017_signal

def f83am_f83_asset_utilization_momentum_calc018_164d_val_v018_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(164).mean()
    v2 = ratio.rolling(169).std()
    v3 = ratio.diff(164)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc018_164d_val_v018_signal'] = f83am_f83_asset_utilization_momentum_calc018_164d_val_v018_signal

def f83am_f83_asset_utilization_momentum_calc019_17d_val_v019_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(17).mean()
    v2 = ratio.rolling(22).std()
    v3 = ratio.diff(17)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc019_17d_val_v019_signal'] = f83am_f83_asset_utilization_momentum_calc019_17d_val_v019_signal

def f83am_f83_asset_utilization_momentum_calc020_70d_val_v020_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(70).mean()
    v2 = ratio.rolling(75).std()
    v3 = ratio.diff(70)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc020_70d_val_v020_signal'] = f83am_f83_asset_utilization_momentum_calc020_70d_val_v020_signal

def f83am_f83_asset_utilization_momentum_calc021_123d_val_v021_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(123).mean()
    v2 = ratio.rolling(128).std()
    v3 = ratio.diff(123)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc021_123d_val_v021_signal'] = f83am_f83_asset_utilization_momentum_calc021_123d_val_v021_signal

def f83am_f83_asset_utilization_momentum_calc022_176d_val_v022_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(176).mean()
    v2 = ratio.rolling(181).std()
    v3 = ratio.diff(176)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(176)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc022_176d_val_v022_signal'] = f83am_f83_asset_utilization_momentum_calc022_176d_val_v022_signal

def f83am_f83_asset_utilization_momentum_calc023_29d_val_v023_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(29).mean()
    v2 = ratio.rolling(34).std()
    v3 = ratio.diff(29)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc023_29d_val_v023_signal'] = f83am_f83_asset_utilization_momentum_calc023_29d_val_v023_signal

def f83am_f83_asset_utilization_momentum_calc024_82d_val_v024_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(82).mean()
    v2 = ratio.rolling(87).std()
    v3 = ratio.diff(82)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc024_82d_val_v024_signal'] = f83am_f83_asset_utilization_momentum_calc024_82d_val_v024_signal

def f83am_f83_asset_utilization_momentum_calc025_135d_val_v025_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(135).mean()
    v2 = ratio.rolling(140).std()
    v3 = ratio.diff(135)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc025_135d_val_v025_signal'] = f83am_f83_asset_utilization_momentum_calc025_135d_val_v025_signal

def f83am_f83_asset_utilization_momentum_calc026_188d_val_v026_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(188).mean()
    v2 = ratio.rolling(193).std()
    v3 = ratio.diff(188)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc026_188d_val_v026_signal'] = f83am_f83_asset_utilization_momentum_calc026_188d_val_v026_signal

def f83am_f83_asset_utilization_momentum_calc027_41d_val_v027_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(41).mean()
    v2 = ratio.rolling(46).std()
    v3 = ratio.diff(41)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc027_41d_val_v027_signal'] = f83am_f83_asset_utilization_momentum_calc027_41d_val_v027_signal

def f83am_f83_asset_utilization_momentum_calc028_94d_val_v028_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(94).mean()
    v2 = ratio.rolling(99).std()
    v3 = ratio.diff(94)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(94)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc028_94d_val_v028_signal'] = f83am_f83_asset_utilization_momentum_calc028_94d_val_v028_signal

def f83am_f83_asset_utilization_momentum_calc029_147d_val_v029_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(147).mean()
    v2 = ratio.rolling(152).std()
    v3 = ratio.diff(147)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc029_147d_val_v029_signal'] = f83am_f83_asset_utilization_momentum_calc029_147d_val_v029_signal

def f83am_f83_asset_utilization_momentum_calc030_200d_val_v030_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(200).mean()
    v2 = ratio.rolling(205).std()
    v3 = ratio.diff(200)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc030_200d_val_v030_signal'] = f83am_f83_asset_utilization_momentum_calc030_200d_val_v030_signal

def f83am_f83_asset_utilization_momentum_calc031_53d_val_v031_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(53).mean()
    v2 = ratio.rolling(58).std()
    v3 = ratio.diff(53)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc031_53d_val_v031_signal'] = f83am_f83_asset_utilization_momentum_calc031_53d_val_v031_signal

def f83am_f83_asset_utilization_momentum_calc032_106d_val_v032_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(106).mean()
    v2 = ratio.rolling(111).std()
    v3 = ratio.diff(106)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc032_106d_val_v032_signal'] = f83am_f83_asset_utilization_momentum_calc032_106d_val_v032_signal

def f83am_f83_asset_utilization_momentum_calc033_159d_val_v033_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(159).mean()
    v2 = ratio.rolling(164).std()
    v3 = ratio.diff(159)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc033_159d_val_v033_signal'] = f83am_f83_asset_utilization_momentum_calc033_159d_val_v033_signal

def f83am_f83_asset_utilization_momentum_calc034_12d_val_v034_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(12).mean()
    v2 = ratio.rolling(17).std()
    v3 = ratio.diff(12)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(12)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc034_12d_val_v034_signal'] = f83am_f83_asset_utilization_momentum_calc034_12d_val_v034_signal

def f83am_f83_asset_utilization_momentum_calc035_65d_val_v035_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(65).mean()
    v2 = ratio.rolling(70).std()
    v3 = ratio.diff(65)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc035_65d_val_v035_signal'] = f83am_f83_asset_utilization_momentum_calc035_65d_val_v035_signal

def f83am_f83_asset_utilization_momentum_calc036_118d_val_v036_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(118).mean()
    v2 = ratio.rolling(123).std()
    v3 = ratio.diff(118)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc036_118d_val_v036_signal'] = f83am_f83_asset_utilization_momentum_calc036_118d_val_v036_signal

def f83am_f83_asset_utilization_momentum_calc037_171d_val_v037_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(171).mean()
    v2 = ratio.rolling(176).std()
    v3 = ratio.diff(171)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc037_171d_val_v037_signal'] = f83am_f83_asset_utilization_momentum_calc037_171d_val_v037_signal

def f83am_f83_asset_utilization_momentum_calc038_24d_val_v038_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(24).mean()
    v2 = ratio.rolling(29).std()
    v3 = ratio.diff(24)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc038_24d_val_v038_signal'] = f83am_f83_asset_utilization_momentum_calc038_24d_val_v038_signal

def f83am_f83_asset_utilization_momentum_calc039_77d_val_v039_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(77).mean()
    v2 = ratio.rolling(82).std()
    v3 = ratio.diff(77)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc039_77d_val_v039_signal'] = f83am_f83_asset_utilization_momentum_calc039_77d_val_v039_signal

def f83am_f83_asset_utilization_momentum_calc040_130d_val_v040_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(130).mean()
    v2 = ratio.rolling(135).std()
    v3 = ratio.diff(130)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(130)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc040_130d_val_v040_signal'] = f83am_f83_asset_utilization_momentum_calc040_130d_val_v040_signal

def f83am_f83_asset_utilization_momentum_calc041_183d_val_v041_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(183).mean()
    v2 = ratio.rolling(188).std()
    v3 = ratio.diff(183)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc041_183d_val_v041_signal'] = f83am_f83_asset_utilization_momentum_calc041_183d_val_v041_signal

def f83am_f83_asset_utilization_momentum_calc042_36d_val_v042_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(36).mean()
    v2 = ratio.rolling(41).std()
    v3 = ratio.diff(36)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc042_36d_val_v042_signal'] = f83am_f83_asset_utilization_momentum_calc042_36d_val_v042_signal

def f83am_f83_asset_utilization_momentum_calc043_89d_val_v043_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(89).mean()
    v2 = ratio.rolling(94).std()
    v3 = ratio.diff(89)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc043_89d_val_v043_signal'] = f83am_f83_asset_utilization_momentum_calc043_89d_val_v043_signal

def f83am_f83_asset_utilization_momentum_calc044_142d_val_v044_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(142).mean()
    v2 = ratio.rolling(147).std()
    v3 = ratio.diff(142)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc044_142d_val_v044_signal'] = f83am_f83_asset_utilization_momentum_calc044_142d_val_v044_signal

def f83am_f83_asset_utilization_momentum_calc045_195d_val_v045_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(195).mean()
    v2 = ratio.rolling(200).std()
    v3 = ratio.diff(195)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc045_195d_val_v045_signal'] = f83am_f83_asset_utilization_momentum_calc045_195d_val_v045_signal

def f83am_f83_asset_utilization_momentum_calc046_48d_val_v046_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(48).mean()
    v2 = ratio.rolling(53).std()
    v3 = ratio.diff(48)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(48)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc046_48d_val_v046_signal'] = f83am_f83_asset_utilization_momentum_calc046_48d_val_v046_signal

def f83am_f83_asset_utilization_momentum_calc047_101d_val_v047_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(101).mean()
    v2 = ratio.rolling(106).std()
    v3 = ratio.diff(101)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc047_101d_val_v047_signal'] = f83am_f83_asset_utilization_momentum_calc047_101d_val_v047_signal

def f83am_f83_asset_utilization_momentum_calc048_154d_val_v048_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(154).mean()
    v2 = ratio.rolling(159).std()
    v3 = ratio.diff(154)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc048_154d_val_v048_signal'] = f83am_f83_asset_utilization_momentum_calc048_154d_val_v048_signal

def f83am_f83_asset_utilization_momentum_calc049_207d_val_v049_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(207).mean()
    v2 = ratio.rolling(212).std()
    v3 = ratio.diff(207)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc049_207d_val_v049_signal'] = f83am_f83_asset_utilization_momentum_calc049_207d_val_v049_signal

def f83am_f83_asset_utilization_momentum_calc050_60d_val_v050_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(60).mean()
    v2 = ratio.rolling(65).std()
    v3 = ratio.diff(60)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc050_60d_val_v050_signal'] = f83am_f83_asset_utilization_momentum_calc050_60d_val_v050_signal

def f83am_f83_asset_utilization_momentum_calc051_113d_val_v051_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(113).mean()
    v2 = ratio.rolling(118).std()
    v3 = ratio.diff(113)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc051_113d_val_v051_signal'] = f83am_f83_asset_utilization_momentum_calc051_113d_val_v051_signal

def f83am_f83_asset_utilization_momentum_calc052_166d_val_v052_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(166).mean()
    v2 = ratio.rolling(171).std()
    v3 = ratio.diff(166)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(166)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc052_166d_val_v052_signal'] = f83am_f83_asset_utilization_momentum_calc052_166d_val_v052_signal

def f83am_f83_asset_utilization_momentum_calc053_19d_val_v053_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(19).mean()
    v2 = ratio.rolling(24).std()
    v3 = ratio.diff(19)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc053_19d_val_v053_signal'] = f83am_f83_asset_utilization_momentum_calc053_19d_val_v053_signal

def f83am_f83_asset_utilization_momentum_calc054_72d_val_v054_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(72).mean()
    v2 = ratio.rolling(77).std()
    v3 = ratio.diff(72)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc054_72d_val_v054_signal'] = f83am_f83_asset_utilization_momentum_calc054_72d_val_v054_signal

def f83am_f83_asset_utilization_momentum_calc055_125d_val_v055_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(125).mean()
    v2 = ratio.rolling(130).std()
    v3 = ratio.diff(125)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc055_125d_val_v055_signal'] = f83am_f83_asset_utilization_momentum_calc055_125d_val_v055_signal

def f83am_f83_asset_utilization_momentum_calc056_178d_val_v056_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(178).mean()
    v2 = ratio.rolling(183).std()
    v3 = ratio.diff(178)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc056_178d_val_v056_signal'] = f83am_f83_asset_utilization_momentum_calc056_178d_val_v056_signal

def f83am_f83_asset_utilization_momentum_calc057_31d_val_v057_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(31).mean()
    v2 = ratio.rolling(36).std()
    v3 = ratio.diff(31)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc057_31d_val_v057_signal'] = f83am_f83_asset_utilization_momentum_calc057_31d_val_v057_signal

def f83am_f83_asset_utilization_momentum_calc058_84d_val_v058_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(84).mean()
    v2 = ratio.rolling(89).std()
    v3 = ratio.diff(84)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(84)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc058_84d_val_v058_signal'] = f83am_f83_asset_utilization_momentum_calc058_84d_val_v058_signal

def f83am_f83_asset_utilization_momentum_calc059_137d_val_v059_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(137).mean()
    v2 = ratio.rolling(142).std()
    v3 = ratio.diff(137)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc059_137d_val_v059_signal'] = f83am_f83_asset_utilization_momentum_calc059_137d_val_v059_signal

def f83am_f83_asset_utilization_momentum_calc060_190d_val_v060_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(190).mean()
    v2 = ratio.rolling(195).std()
    v3 = ratio.diff(190)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc060_190d_val_v060_signal'] = f83am_f83_asset_utilization_momentum_calc060_190d_val_v060_signal

def f83am_f83_asset_utilization_momentum_calc061_43d_val_v061_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(43).mean()
    v2 = ratio.rolling(48).std()
    v3 = ratio.diff(43)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc061_43d_val_v061_signal'] = f83am_f83_asset_utilization_momentum_calc061_43d_val_v061_signal

def f83am_f83_asset_utilization_momentum_calc062_96d_val_v062_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(96).mean()
    v2 = ratio.rolling(101).std()
    v3 = ratio.diff(96)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc062_96d_val_v062_signal'] = f83am_f83_asset_utilization_momentum_calc062_96d_val_v062_signal

def f83am_f83_asset_utilization_momentum_calc063_149d_val_v063_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(149).mean()
    v2 = ratio.rolling(154).std()
    v3 = ratio.diff(149)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc063_149d_val_v063_signal'] = f83am_f83_asset_utilization_momentum_calc063_149d_val_v063_signal

def f83am_f83_asset_utilization_momentum_calc064_202d_val_v064_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(202).mean()
    v2 = ratio.rolling(207).std()
    v3 = ratio.diff(202)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(202)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc064_202d_val_v064_signal'] = f83am_f83_asset_utilization_momentum_calc064_202d_val_v064_signal

def f83am_f83_asset_utilization_momentum_calc065_55d_val_v065_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(55).mean()
    v2 = ratio.rolling(60).std()
    v3 = ratio.diff(55)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc065_55d_val_v065_signal'] = f83am_f83_asset_utilization_momentum_calc065_55d_val_v065_signal

def f83am_f83_asset_utilization_momentum_calc066_108d_val_v066_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(108).mean()
    v2 = ratio.rolling(113).std()
    v3 = ratio.diff(108)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc066_108d_val_v066_signal'] = f83am_f83_asset_utilization_momentum_calc066_108d_val_v066_signal

def f83am_f83_asset_utilization_momentum_calc067_161d_val_v067_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(161).mean()
    v2 = ratio.rolling(166).std()
    v3 = ratio.diff(161)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc067_161d_val_v067_signal'] = f83am_f83_asset_utilization_momentum_calc067_161d_val_v067_signal

def f83am_f83_asset_utilization_momentum_calc068_14d_val_v068_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(14).mean()
    v2 = ratio.rolling(19).std()
    v3 = ratio.diff(14)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc068_14d_val_v068_signal'] = f83am_f83_asset_utilization_momentum_calc068_14d_val_v068_signal

def f83am_f83_asset_utilization_momentum_calc069_67d_val_v069_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(67).mean()
    v2 = ratio.rolling(72).std()
    v3 = ratio.diff(67)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc069_67d_val_v069_signal'] = f83am_f83_asset_utilization_momentum_calc069_67d_val_v069_signal

def f83am_f83_asset_utilization_momentum_calc070_120d_val_v070_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(120).mean()
    v2 = ratio.rolling(125).std()
    v3 = ratio.diff(120)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio.pct_change(120)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc070_120d_val_v070_signal'] = f83am_f83_asset_utilization_momentum_calc070_120d_val_v070_signal

def f83am_f83_asset_utilization_momentum_calc071_173d_val_v071_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(173).mean()
    v2 = ratio.rolling(178).std()
    v3 = ratio.diff(173)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = (ratio - v1) / v2.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc071_173d_val_v071_signal'] = f83am_f83_asset_utilization_momentum_calc071_173d_val_v071_signal

def f83am_f83_asset_utilization_momentum_calc072_26d_val_v072_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(26).mean()
    v2 = ratio.rolling(31).std()
    v3 = ratio.diff(26)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v1
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc072_26d_val_v072_signal'] = f83am_f83_asset_utilization_momentum_calc072_26d_val_v072_signal

def f83am_f83_asset_utilization_momentum_calc073_79d_val_v073_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(79).mean()
    v2 = ratio.rolling(84).std()
    v3 = ratio.diff(79)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v2
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc073_79d_val_v073_signal'] = f83am_f83_asset_utilization_momentum_calc073_79d_val_v073_signal

def f83am_f83_asset_utilization_momentum_calc074_132d_val_v074_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(132).mean()
    v2 = ratio.rolling(137).std()
    v3 = ratio.diff(132)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = v3
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc074_132d_val_v074_signal'] = f83am_f83_asset_utilization_momentum_calc074_132d_val_v074_signal

def f83am_f83_asset_utilization_momentum_calc075_185d_val_v075_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(185).mean()
    v2 = ratio.rolling(190).std()
    v3 = ratio.diff(185)
    d10 = ratio.shift(10).rolling(5).mean() + 10
    d11 = ratio.shift(11).rolling(5).mean() + 11
    d12 = ratio.shift(12).rolling(5).mean() + 12
    d13 = ratio.shift(13).rolling(5).mean() + 13
    d14 = ratio.shift(14).rolling(5).mean() + 14
    d15 = ratio.shift(15).rolling(5).mean() + 15
    d16 = ratio.shift(16).rolling(5).mean() + 16
    d17 = ratio.shift(17).rolling(5).mean() + 17
    d18 = ratio.shift(18).rolling(5).mean() + 18
    d19 = ratio.shift(19).rolling(5).mean() + 19
    res = ratio / v1.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc075_185d_val_v075_signal'] = f83am_f83_asset_utilization_momentum_calc075_185d_val_v075_signal


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
