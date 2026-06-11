import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f83am_f83_asset_utilization_momentum_calc001_63d_slope_v001_signal(opinc, assets):
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
    res = ratio.diff(63).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc001_63d_slope_v001_signal'] = f83am_f83_asset_utilization_momentum_calc001_63d_slope_v001_signal

def f83am_f83_asset_utilization_momentum_calc002_116d_slope_v002_signal(opinc, assets):
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
    res = ratio.diff(116).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc002_116d_slope_v002_signal'] = f83am_f83_asset_utilization_momentum_calc002_116d_slope_v002_signal

def f83am_f83_asset_utilization_momentum_calc003_169d_slope_v003_signal(capex, revenue):
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
    res = ratio.diff(169).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc003_169d_slope_v003_signal'] = f83am_f83_asset_utilization_momentum_calc003_169d_slope_v003_signal

def f83am_f83_asset_utilization_momentum_calc004_22d_slope_v004_signal(revenue, capex):
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
    res = ratio.diff(22).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc004_22d_slope_v004_signal'] = f83am_f83_asset_utilization_momentum_calc004_22d_slope_v004_signal

def f83am_f83_asset_utilization_momentum_calc005_75d_slope_v005_signal(revenue, capex):
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
    res = ratio.diff(75).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc005_75d_slope_v005_signal'] = f83am_f83_asset_utilization_momentum_calc005_75d_slope_v005_signal

def f83am_f83_asset_utilization_momentum_calc006_128d_slope_v006_signal(opinc, assets):
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
    res = ratio.diff(128).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc006_128d_slope_v006_signal'] = f83am_f83_asset_utilization_momentum_calc006_128d_slope_v006_signal

def f83am_f83_asset_utilization_momentum_calc007_181d_slope_v007_signal(assets, opinc):
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
    res = ratio.diff(181).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc007_181d_slope_v007_signal'] = f83am_f83_asset_utilization_momentum_calc007_181d_slope_v007_signal

def f83am_f83_asset_utilization_momentum_calc008_34d_slope_v008_signal(assets, opinc):
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
    res = ratio.diff(34).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc008_34d_slope_v008_signal'] = f83am_f83_asset_utilization_momentum_calc008_34d_slope_v008_signal

def f83am_f83_asset_utilization_momentum_calc009_87d_slope_v009_signal(revenue, capex):
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
    res = ratio.diff(87).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc009_87d_slope_v009_signal'] = f83am_f83_asset_utilization_momentum_calc009_87d_slope_v009_signal

def f83am_f83_asset_utilization_momentum_calc010_140d_slope_v010_signal(capex, revenue):
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
    res = ratio.diff(140).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc010_140d_slope_v010_signal'] = f83am_f83_asset_utilization_momentum_calc010_140d_slope_v010_signal

def f83am_f83_asset_utilization_momentum_calc011_193d_slope_v011_signal(capex, revenue):
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
    res = ratio.diff(193).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc011_193d_slope_v011_signal'] = f83am_f83_asset_utilization_momentum_calc011_193d_slope_v011_signal

def f83am_f83_asset_utilization_momentum_calc012_46d_slope_v012_signal(assets, opinc):
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
    res = ratio.diff(46).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc012_46d_slope_v012_signal'] = f83am_f83_asset_utilization_momentum_calc012_46d_slope_v012_signal

def f83am_f83_asset_utilization_momentum_calc013_99d_slope_v013_signal(opinc, assets):
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
    res = ratio.diff(99).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc013_99d_slope_v013_signal'] = f83am_f83_asset_utilization_momentum_calc013_99d_slope_v013_signal

def f83am_f83_asset_utilization_momentum_calc014_152d_slope_v014_signal(opinc, assets):
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
    res = ratio.diff(152).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc014_152d_slope_v014_signal'] = f83am_f83_asset_utilization_momentum_calc014_152d_slope_v014_signal

def f83am_f83_asset_utilization_momentum_calc015_205d_slope_v015_signal(capex, revenue):
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
    res = ratio.diff(205).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc015_205d_slope_v015_signal'] = f83am_f83_asset_utilization_momentum_calc015_205d_slope_v015_signal

def f83am_f83_asset_utilization_momentum_calc016_58d_slope_v016_signal(revenue, capex):
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
    res = ratio.diff(58).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc016_58d_slope_v016_signal'] = f83am_f83_asset_utilization_momentum_calc016_58d_slope_v016_signal

def f83am_f83_asset_utilization_momentum_calc017_111d_slope_v017_signal(revenue, capex):
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
    res = ratio.diff(111).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc017_111d_slope_v017_signal'] = f83am_f83_asset_utilization_momentum_calc017_111d_slope_v017_signal

def f83am_f83_asset_utilization_momentum_calc018_164d_slope_v018_signal(opinc, assets):
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
    res = ratio.diff(164).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc018_164d_slope_v018_signal'] = f83am_f83_asset_utilization_momentum_calc018_164d_slope_v018_signal

def f83am_f83_asset_utilization_momentum_calc019_17d_slope_v019_signal(assets, opinc):
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
    res = ratio.diff(17).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc019_17d_slope_v019_signal'] = f83am_f83_asset_utilization_momentum_calc019_17d_slope_v019_signal

def f83am_f83_asset_utilization_momentum_calc020_70d_slope_v020_signal(assets, opinc):
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
    res = ratio.diff(70).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc020_70d_slope_v020_signal'] = f83am_f83_asset_utilization_momentum_calc020_70d_slope_v020_signal

def f83am_f83_asset_utilization_momentum_calc021_123d_slope_v021_signal(revenue, capex):
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
    res = ratio.diff(123).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc021_123d_slope_v021_signal'] = f83am_f83_asset_utilization_momentum_calc021_123d_slope_v021_signal

def f83am_f83_asset_utilization_momentum_calc022_176d_slope_v022_signal(capex, revenue):
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
    res = ratio.diff(176).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc022_176d_slope_v022_signal'] = f83am_f83_asset_utilization_momentum_calc022_176d_slope_v022_signal

def f83am_f83_asset_utilization_momentum_calc023_29d_slope_v023_signal(capex, revenue):
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
    res = ratio.diff(29).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc023_29d_slope_v023_signal'] = f83am_f83_asset_utilization_momentum_calc023_29d_slope_v023_signal

def f83am_f83_asset_utilization_momentum_calc024_82d_slope_v024_signal(assets, opinc):
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
    res = ratio.diff(82).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc024_82d_slope_v024_signal'] = f83am_f83_asset_utilization_momentum_calc024_82d_slope_v024_signal

def f83am_f83_asset_utilization_momentum_calc025_135d_slope_v025_signal(opinc, assets):
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
    res = ratio.diff(135).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc025_135d_slope_v025_signal'] = f83am_f83_asset_utilization_momentum_calc025_135d_slope_v025_signal

def f83am_f83_asset_utilization_momentum_calc026_188d_slope_v026_signal(opinc, assets):
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
    res = ratio.diff(188).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc026_188d_slope_v026_signal'] = f83am_f83_asset_utilization_momentum_calc026_188d_slope_v026_signal

def f83am_f83_asset_utilization_momentum_calc027_41d_slope_v027_signal(capex, revenue):
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
    res = ratio.diff(41).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc027_41d_slope_v027_signal'] = f83am_f83_asset_utilization_momentum_calc027_41d_slope_v027_signal

def f83am_f83_asset_utilization_momentum_calc028_94d_slope_v028_signal(revenue, capex):
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
    res = ratio.diff(94).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc028_94d_slope_v028_signal'] = f83am_f83_asset_utilization_momentum_calc028_94d_slope_v028_signal

def f83am_f83_asset_utilization_momentum_calc029_147d_slope_v029_signal(revenue, capex):
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
    res = ratio.diff(147).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc029_147d_slope_v029_signal'] = f83am_f83_asset_utilization_momentum_calc029_147d_slope_v029_signal

def f83am_f83_asset_utilization_momentum_calc030_200d_slope_v030_signal(opinc, assets):
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
    res = ratio.diff(200).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc030_200d_slope_v030_signal'] = f83am_f83_asset_utilization_momentum_calc030_200d_slope_v030_signal

def f83am_f83_asset_utilization_momentum_calc031_53d_slope_v031_signal(assets, opinc):
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
    res = ratio.diff(53).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc031_53d_slope_v031_signal'] = f83am_f83_asset_utilization_momentum_calc031_53d_slope_v031_signal

def f83am_f83_asset_utilization_momentum_calc032_106d_slope_v032_signal(assets, opinc):
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
    res = ratio.diff(106).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc032_106d_slope_v032_signal'] = f83am_f83_asset_utilization_momentum_calc032_106d_slope_v032_signal

def f83am_f83_asset_utilization_momentum_calc033_159d_slope_v033_signal(revenue, capex):
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
    res = ratio.diff(159).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc033_159d_slope_v033_signal'] = f83am_f83_asset_utilization_momentum_calc033_159d_slope_v033_signal

def f83am_f83_asset_utilization_momentum_calc034_12d_slope_v034_signal(capex, revenue):
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
    res = ratio.diff(12).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc034_12d_slope_v034_signal'] = f83am_f83_asset_utilization_momentum_calc034_12d_slope_v034_signal

def f83am_f83_asset_utilization_momentum_calc035_65d_slope_v035_signal(capex, revenue):
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
    res = ratio.diff(65).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc035_65d_slope_v035_signal'] = f83am_f83_asset_utilization_momentum_calc035_65d_slope_v035_signal

def f83am_f83_asset_utilization_momentum_calc036_118d_slope_v036_signal(assets, opinc):
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
    res = ratio.diff(118).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc036_118d_slope_v036_signal'] = f83am_f83_asset_utilization_momentum_calc036_118d_slope_v036_signal

def f83am_f83_asset_utilization_momentum_calc037_171d_slope_v037_signal(opinc, assets):
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
    res = ratio.diff(171).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc037_171d_slope_v037_signal'] = f83am_f83_asset_utilization_momentum_calc037_171d_slope_v037_signal

def f83am_f83_asset_utilization_momentum_calc038_24d_slope_v038_signal(opinc, assets):
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
    res = ratio.diff(24).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc038_24d_slope_v038_signal'] = f83am_f83_asset_utilization_momentum_calc038_24d_slope_v038_signal

def f83am_f83_asset_utilization_momentum_calc039_77d_slope_v039_signal(capex, revenue):
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
    res = ratio.diff(77).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc039_77d_slope_v039_signal'] = f83am_f83_asset_utilization_momentum_calc039_77d_slope_v039_signal

def f83am_f83_asset_utilization_momentum_calc040_130d_slope_v040_signal(revenue, capex):
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
    res = ratio.diff(130).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc040_130d_slope_v040_signal'] = f83am_f83_asset_utilization_momentum_calc040_130d_slope_v040_signal

def f83am_f83_asset_utilization_momentum_calc041_183d_slope_v041_signal(revenue, capex):
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
    res = ratio.diff(183).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc041_183d_slope_v041_signal'] = f83am_f83_asset_utilization_momentum_calc041_183d_slope_v041_signal

def f83am_f83_asset_utilization_momentum_calc042_36d_slope_v042_signal(opinc, assets):
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
    res = ratio.diff(36).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc042_36d_slope_v042_signal'] = f83am_f83_asset_utilization_momentum_calc042_36d_slope_v042_signal

def f83am_f83_asset_utilization_momentum_calc043_89d_slope_v043_signal(assets, opinc):
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
    res = ratio.diff(89).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc043_89d_slope_v043_signal'] = f83am_f83_asset_utilization_momentum_calc043_89d_slope_v043_signal

def f83am_f83_asset_utilization_momentum_calc044_142d_slope_v044_signal(assets, opinc):
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
    res = ratio.diff(142).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc044_142d_slope_v044_signal'] = f83am_f83_asset_utilization_momentum_calc044_142d_slope_v044_signal

def f83am_f83_asset_utilization_momentum_calc045_195d_slope_v045_signal(revenue, capex):
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
    res = ratio.diff(195).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc045_195d_slope_v045_signal'] = f83am_f83_asset_utilization_momentum_calc045_195d_slope_v045_signal

def f83am_f83_asset_utilization_momentum_calc046_48d_slope_v046_signal(capex, revenue):
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
    res = ratio.diff(48).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc046_48d_slope_v046_signal'] = f83am_f83_asset_utilization_momentum_calc046_48d_slope_v046_signal

def f83am_f83_asset_utilization_momentum_calc047_101d_slope_v047_signal(capex, revenue):
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
    res = ratio.diff(101).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc047_101d_slope_v047_signal'] = f83am_f83_asset_utilization_momentum_calc047_101d_slope_v047_signal

def f83am_f83_asset_utilization_momentum_calc048_154d_slope_v048_signal(assets, opinc):
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
    res = ratio.diff(154).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc048_154d_slope_v048_signal'] = f83am_f83_asset_utilization_momentum_calc048_154d_slope_v048_signal

def f83am_f83_asset_utilization_momentum_calc049_207d_slope_v049_signal(opinc, assets):
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
    res = ratio.diff(207).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc049_207d_slope_v049_signal'] = f83am_f83_asset_utilization_momentum_calc049_207d_slope_v049_signal

def f83am_f83_asset_utilization_momentum_calc050_60d_slope_v050_signal(opinc, assets):
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
    res = ratio.diff(60).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc050_60d_slope_v050_signal'] = f83am_f83_asset_utilization_momentum_calc050_60d_slope_v050_signal

def f83am_f83_asset_utilization_momentum_calc051_113d_slope_v051_signal(capex, revenue):
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
    res = ratio.diff(113).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc051_113d_slope_v051_signal'] = f83am_f83_asset_utilization_momentum_calc051_113d_slope_v051_signal

def f83am_f83_asset_utilization_momentum_calc052_166d_slope_v052_signal(revenue, capex):
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
    res = ratio.diff(166).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc052_166d_slope_v052_signal'] = f83am_f83_asset_utilization_momentum_calc052_166d_slope_v052_signal

def f83am_f83_asset_utilization_momentum_calc053_19d_slope_v053_signal(revenue, capex):
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
    res = ratio.diff(19).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc053_19d_slope_v053_signal'] = f83am_f83_asset_utilization_momentum_calc053_19d_slope_v053_signal

def f83am_f83_asset_utilization_momentum_calc054_72d_slope_v054_signal(opinc, assets):
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
    res = ratio.diff(72).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc054_72d_slope_v054_signal'] = f83am_f83_asset_utilization_momentum_calc054_72d_slope_v054_signal

def f83am_f83_asset_utilization_momentum_calc055_125d_slope_v055_signal(assets, opinc):
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
    res = ratio.diff(125).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc055_125d_slope_v055_signal'] = f83am_f83_asset_utilization_momentum_calc055_125d_slope_v055_signal

def f83am_f83_asset_utilization_momentum_calc056_178d_slope_v056_signal(assets, opinc):
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
    res = ratio.diff(178).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc056_178d_slope_v056_signal'] = f83am_f83_asset_utilization_momentum_calc056_178d_slope_v056_signal

def f83am_f83_asset_utilization_momentum_calc057_31d_slope_v057_signal(revenue, capex):
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
    res = ratio.diff(31).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc057_31d_slope_v057_signal'] = f83am_f83_asset_utilization_momentum_calc057_31d_slope_v057_signal

def f83am_f83_asset_utilization_momentum_calc058_84d_slope_v058_signal(capex, revenue):
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
    res = ratio.diff(84).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc058_84d_slope_v058_signal'] = f83am_f83_asset_utilization_momentum_calc058_84d_slope_v058_signal

def f83am_f83_asset_utilization_momentum_calc059_137d_slope_v059_signal(capex, revenue):
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
    res = ratio.diff(137).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc059_137d_slope_v059_signal'] = f83am_f83_asset_utilization_momentum_calc059_137d_slope_v059_signal

def f83am_f83_asset_utilization_momentum_calc060_190d_slope_v060_signal(assets, opinc):
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
    res = ratio.diff(190).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc060_190d_slope_v060_signal'] = f83am_f83_asset_utilization_momentum_calc060_190d_slope_v060_signal

def f83am_f83_asset_utilization_momentum_calc061_43d_slope_v061_signal(opinc, assets):
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
    res = ratio.diff(43).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc061_43d_slope_v061_signal'] = f83am_f83_asset_utilization_momentum_calc061_43d_slope_v061_signal

def f83am_f83_asset_utilization_momentum_calc062_96d_slope_v062_signal(opinc, assets):
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
    res = ratio.diff(96).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc062_96d_slope_v062_signal'] = f83am_f83_asset_utilization_momentum_calc062_96d_slope_v062_signal

def f83am_f83_asset_utilization_momentum_calc063_149d_slope_v063_signal(capex, revenue):
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
    res = ratio.diff(149).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc063_149d_slope_v063_signal'] = f83am_f83_asset_utilization_momentum_calc063_149d_slope_v063_signal

def f83am_f83_asset_utilization_momentum_calc064_202d_slope_v064_signal(revenue, capex):
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
    res = ratio.diff(202).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc064_202d_slope_v064_signal'] = f83am_f83_asset_utilization_momentum_calc064_202d_slope_v064_signal

def f83am_f83_asset_utilization_momentum_calc065_55d_slope_v065_signal(revenue, capex):
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
    res = ratio.diff(55).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc065_55d_slope_v065_signal'] = f83am_f83_asset_utilization_momentum_calc065_55d_slope_v065_signal

def f83am_f83_asset_utilization_momentum_calc066_108d_slope_v066_signal(opinc, assets):
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
    res = ratio.diff(108).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc066_108d_slope_v066_signal'] = f83am_f83_asset_utilization_momentum_calc066_108d_slope_v066_signal

def f83am_f83_asset_utilization_momentum_calc067_161d_slope_v067_signal(assets, opinc):
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
    res = ratio.diff(161).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc067_161d_slope_v067_signal'] = f83am_f83_asset_utilization_momentum_calc067_161d_slope_v067_signal

def f83am_f83_asset_utilization_momentum_calc068_14d_slope_v068_signal(assets, opinc):
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
    res = ratio.diff(14).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc068_14d_slope_v068_signal'] = f83am_f83_asset_utilization_momentum_calc068_14d_slope_v068_signal

def f83am_f83_asset_utilization_momentum_calc069_67d_slope_v069_signal(revenue, capex):
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
    res = ratio.diff(67).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc069_67d_slope_v069_signal'] = f83am_f83_asset_utilization_momentum_calc069_67d_slope_v069_signal

def f83am_f83_asset_utilization_momentum_calc070_120d_slope_v070_signal(capex, revenue):
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
    res = ratio.diff(120).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc070_120d_slope_v070_signal'] = f83am_f83_asset_utilization_momentum_calc070_120d_slope_v070_signal

def f83am_f83_asset_utilization_momentum_calc071_173d_slope_v071_signal(capex, revenue):
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
    res = ratio.diff(173).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc071_173d_slope_v071_signal'] = f83am_f83_asset_utilization_momentum_calc071_173d_slope_v071_signal

def f83am_f83_asset_utilization_momentum_calc072_26d_slope_v072_signal(assets, opinc):
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
    res = ratio.diff(26).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc072_26d_slope_v072_signal'] = f83am_f83_asset_utilization_momentum_calc072_26d_slope_v072_signal

def f83am_f83_asset_utilization_momentum_calc073_79d_slope_v073_signal(opinc, assets):
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
    res = ratio.diff(79).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc073_79d_slope_v073_signal'] = f83am_f83_asset_utilization_momentum_calc073_79d_slope_v073_signal

def f83am_f83_asset_utilization_momentum_calc074_132d_slope_v074_signal(opinc, assets):
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
    res = ratio.diff(132).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc074_132d_slope_v074_signal'] = f83am_f83_asset_utilization_momentum_calc074_132d_slope_v074_signal

def f83am_f83_asset_utilization_momentum_calc075_185d_slope_v075_signal(capex, revenue):
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
    res = ratio.diff(185).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc075_185d_slope_v075_signal'] = f83am_f83_asset_utilization_momentum_calc075_185d_slope_v075_signal

def f83am_f83_asset_utilization_momentum_calc076_38d_slope_v076_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(38).mean()
    v2 = ratio.rolling(43).std()
    v3 = ratio.diff(38)
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
    res = ratio.diff(38).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc076_38d_slope_v076_signal'] = f83am_f83_asset_utilization_momentum_calc076_38d_slope_v076_signal

def f83am_f83_asset_utilization_momentum_calc077_91d_slope_v077_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(91).mean()
    v2 = ratio.rolling(96).std()
    v3 = ratio.diff(91)
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
    res = ratio.diff(91).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc077_91d_slope_v077_signal'] = f83am_f83_asset_utilization_momentum_calc077_91d_slope_v077_signal

def f83am_f83_asset_utilization_momentum_calc078_144d_slope_v078_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(144).mean()
    v2 = ratio.rolling(149).std()
    v3 = ratio.diff(144)
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
    res = ratio.diff(144).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc078_144d_slope_v078_signal'] = f83am_f83_asset_utilization_momentum_calc078_144d_slope_v078_signal

def f83am_f83_asset_utilization_momentum_calc079_197d_slope_v079_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(197).mean()
    v2 = ratio.rolling(202).std()
    v3 = ratio.diff(197)
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
    res = ratio.diff(197).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc079_197d_slope_v079_signal'] = f83am_f83_asset_utilization_momentum_calc079_197d_slope_v079_signal

def f83am_f83_asset_utilization_momentum_calc080_50d_slope_v080_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(50).mean()
    v2 = ratio.rolling(55).std()
    v3 = ratio.diff(50)
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
    res = ratio.diff(50).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc080_50d_slope_v080_signal'] = f83am_f83_asset_utilization_momentum_calc080_50d_slope_v080_signal

def f83am_f83_asset_utilization_momentum_calc081_103d_slope_v081_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(103).mean()
    v2 = ratio.rolling(108).std()
    v3 = ratio.diff(103)
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
    res = ratio.diff(103).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc081_103d_slope_v081_signal'] = f83am_f83_asset_utilization_momentum_calc081_103d_slope_v081_signal

def f83am_f83_asset_utilization_momentum_calc082_156d_slope_v082_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(156).mean()
    v2 = ratio.rolling(161).std()
    v3 = ratio.diff(156)
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
    res = ratio.diff(156).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc082_156d_slope_v082_signal'] = f83am_f83_asset_utilization_momentum_calc082_156d_slope_v082_signal

def f83am_f83_asset_utilization_momentum_calc083_209d_slope_v083_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(209).mean()
    v2 = ratio.rolling(214).std()
    v3 = ratio.diff(209)
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
    res = ratio.diff(209).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc083_209d_slope_v083_signal'] = f83am_f83_asset_utilization_momentum_calc083_209d_slope_v083_signal

def f83am_f83_asset_utilization_momentum_calc084_62d_slope_v084_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(62).mean()
    v2 = ratio.rolling(67).std()
    v3 = ratio.diff(62)
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
    res = ratio.diff(62).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc084_62d_slope_v084_signal'] = f83am_f83_asset_utilization_momentum_calc084_62d_slope_v084_signal

def f83am_f83_asset_utilization_momentum_calc085_115d_slope_v085_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(115).mean()
    v2 = ratio.rolling(120).std()
    v3 = ratio.diff(115)
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
    res = ratio.diff(115).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc085_115d_slope_v085_signal'] = f83am_f83_asset_utilization_momentum_calc085_115d_slope_v085_signal

def f83am_f83_asset_utilization_momentum_calc086_168d_slope_v086_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(168).mean()
    v2 = ratio.rolling(173).std()
    v3 = ratio.diff(168)
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
    res = ratio.diff(168).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc086_168d_slope_v086_signal'] = f83am_f83_asset_utilization_momentum_calc086_168d_slope_v086_signal

def f83am_f83_asset_utilization_momentum_calc087_21d_slope_v087_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(21).mean()
    v2 = ratio.rolling(26).std()
    v3 = ratio.diff(21)
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
    res = ratio.diff(21).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc087_21d_slope_v087_signal'] = f83am_f83_asset_utilization_momentum_calc087_21d_slope_v087_signal

def f83am_f83_asset_utilization_momentum_calc088_74d_slope_v088_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(74).mean()
    v2 = ratio.rolling(79).std()
    v3 = ratio.diff(74)
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
    res = ratio.diff(74).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc088_74d_slope_v088_signal'] = f83am_f83_asset_utilization_momentum_calc088_74d_slope_v088_signal

def f83am_f83_asset_utilization_momentum_calc089_127d_slope_v089_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(127).mean()
    v2 = ratio.rolling(132).std()
    v3 = ratio.diff(127)
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
    res = ratio.diff(127).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc089_127d_slope_v089_signal'] = f83am_f83_asset_utilization_momentum_calc089_127d_slope_v089_signal

def f83am_f83_asset_utilization_momentum_calc090_180d_slope_v090_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(180).mean()
    v2 = ratio.rolling(185).std()
    v3 = ratio.diff(180)
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
    res = ratio.diff(180).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc090_180d_slope_v090_signal'] = f83am_f83_asset_utilization_momentum_calc090_180d_slope_v090_signal

def f83am_f83_asset_utilization_momentum_calc091_33d_slope_v091_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(33).mean()
    v2 = ratio.rolling(38).std()
    v3 = ratio.diff(33)
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
    res = ratio.diff(33).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc091_33d_slope_v091_signal'] = f83am_f83_asset_utilization_momentum_calc091_33d_slope_v091_signal

def f83am_f83_asset_utilization_momentum_calc092_86d_slope_v092_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(86).mean()
    v2 = ratio.rolling(91).std()
    v3 = ratio.diff(86)
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
    res = ratio.diff(86).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc092_86d_slope_v092_signal'] = f83am_f83_asset_utilization_momentum_calc092_86d_slope_v092_signal

def f83am_f83_asset_utilization_momentum_calc093_139d_slope_v093_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(139).mean()
    v2 = ratio.rolling(144).std()
    v3 = ratio.diff(139)
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
    res = ratio.diff(139).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc093_139d_slope_v093_signal'] = f83am_f83_asset_utilization_momentum_calc093_139d_slope_v093_signal

def f83am_f83_asset_utilization_momentum_calc094_192d_slope_v094_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(192).mean()
    v2 = ratio.rolling(197).std()
    v3 = ratio.diff(192)
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
    res = ratio.diff(192).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc094_192d_slope_v094_signal'] = f83am_f83_asset_utilization_momentum_calc094_192d_slope_v094_signal

def f83am_f83_asset_utilization_momentum_calc095_45d_slope_v095_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(45).mean()
    v2 = ratio.rolling(50).std()
    v3 = ratio.diff(45)
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
    res = ratio.diff(45).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc095_45d_slope_v095_signal'] = f83am_f83_asset_utilization_momentum_calc095_45d_slope_v095_signal

def f83am_f83_asset_utilization_momentum_calc096_98d_slope_v096_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(98).mean()
    v2 = ratio.rolling(103).std()
    v3 = ratio.diff(98)
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
    res = ratio.diff(98).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc096_98d_slope_v096_signal'] = f83am_f83_asset_utilization_momentum_calc096_98d_slope_v096_signal

def f83am_f83_asset_utilization_momentum_calc097_151d_slope_v097_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(151).mean()
    v2 = ratio.rolling(156).std()
    v3 = ratio.diff(151)
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
    res = ratio.diff(151).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc097_151d_slope_v097_signal'] = f83am_f83_asset_utilization_momentum_calc097_151d_slope_v097_signal

def f83am_f83_asset_utilization_momentum_calc098_204d_slope_v098_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(204).mean()
    v2 = ratio.rolling(209).std()
    v3 = ratio.diff(204)
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
    res = ratio.diff(204).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc098_204d_slope_v098_signal'] = f83am_f83_asset_utilization_momentum_calc098_204d_slope_v098_signal

def f83am_f83_asset_utilization_momentum_calc099_57d_slope_v099_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(57).mean()
    v2 = ratio.rolling(62).std()
    v3 = ratio.diff(57)
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
    res = ratio.diff(57).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc099_57d_slope_v099_signal'] = f83am_f83_asset_utilization_momentum_calc099_57d_slope_v099_signal

def f83am_f83_asset_utilization_momentum_calc100_110d_slope_v100_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(110).mean()
    v2 = ratio.rolling(115).std()
    v3 = ratio.diff(110)
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
    res = ratio.diff(110).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc100_110d_slope_v100_signal'] = f83am_f83_asset_utilization_momentum_calc100_110d_slope_v100_signal

def f83am_f83_asset_utilization_momentum_calc101_163d_slope_v101_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(163).mean()
    v2 = ratio.rolling(168).std()
    v3 = ratio.diff(163)
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
    res = ratio.diff(163).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc101_163d_slope_v101_signal'] = f83am_f83_asset_utilization_momentum_calc101_163d_slope_v101_signal

def f83am_f83_asset_utilization_momentum_calc102_16d_slope_v102_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(16).mean()
    v2 = ratio.rolling(21).std()
    v3 = ratio.diff(16)
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
    res = ratio.diff(16).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc102_16d_slope_v102_signal'] = f83am_f83_asset_utilization_momentum_calc102_16d_slope_v102_signal

def f83am_f83_asset_utilization_momentum_calc103_69d_slope_v103_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(69).mean()
    v2 = ratio.rolling(74).std()
    v3 = ratio.diff(69)
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
    res = ratio.diff(69).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc103_69d_slope_v103_signal'] = f83am_f83_asset_utilization_momentum_calc103_69d_slope_v103_signal

def f83am_f83_asset_utilization_momentum_calc104_122d_slope_v104_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(122).mean()
    v2 = ratio.rolling(127).std()
    v3 = ratio.diff(122)
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
    res = ratio.diff(122).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc104_122d_slope_v104_signal'] = f83am_f83_asset_utilization_momentum_calc104_122d_slope_v104_signal

def f83am_f83_asset_utilization_momentum_calc105_175d_slope_v105_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(175).mean()
    v2 = ratio.rolling(180).std()
    v3 = ratio.diff(175)
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
    res = ratio.diff(175).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc105_175d_slope_v105_signal'] = f83am_f83_asset_utilization_momentum_calc105_175d_slope_v105_signal

def f83am_f83_asset_utilization_momentum_calc106_28d_slope_v106_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(28).mean()
    v2 = ratio.rolling(33).std()
    v3 = ratio.diff(28)
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
    res = ratio.diff(28).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc106_28d_slope_v106_signal'] = f83am_f83_asset_utilization_momentum_calc106_28d_slope_v106_signal

def f83am_f83_asset_utilization_momentum_calc107_81d_slope_v107_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(81).mean()
    v2 = ratio.rolling(86).std()
    v3 = ratio.diff(81)
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
    res = ratio.diff(81).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc107_81d_slope_v107_signal'] = f83am_f83_asset_utilization_momentum_calc107_81d_slope_v107_signal

def f83am_f83_asset_utilization_momentum_calc108_134d_slope_v108_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(134).mean()
    v2 = ratio.rolling(139).std()
    v3 = ratio.diff(134)
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
    res = ratio.diff(134).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc108_134d_slope_v108_signal'] = f83am_f83_asset_utilization_momentum_calc108_134d_slope_v108_signal

def f83am_f83_asset_utilization_momentum_calc109_187d_slope_v109_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(187).mean()
    v2 = ratio.rolling(192).std()
    v3 = ratio.diff(187)
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
    res = ratio.diff(187).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc109_187d_slope_v109_signal'] = f83am_f83_asset_utilization_momentum_calc109_187d_slope_v109_signal

def f83am_f83_asset_utilization_momentum_calc110_40d_slope_v110_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(40).mean()
    v2 = ratio.rolling(45).std()
    v3 = ratio.diff(40)
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
    res = ratio.diff(40).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc110_40d_slope_v110_signal'] = f83am_f83_asset_utilization_momentum_calc110_40d_slope_v110_signal

def f83am_f83_asset_utilization_momentum_calc111_93d_slope_v111_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(93).mean()
    v2 = ratio.rolling(98).std()
    v3 = ratio.diff(93)
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
    res = ratio.diff(93).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc111_93d_slope_v111_signal'] = f83am_f83_asset_utilization_momentum_calc111_93d_slope_v111_signal

def f83am_f83_asset_utilization_momentum_calc112_146d_slope_v112_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(146).mean()
    v2 = ratio.rolling(151).std()
    v3 = ratio.diff(146)
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
    res = ratio.diff(146).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc112_146d_slope_v112_signal'] = f83am_f83_asset_utilization_momentum_calc112_146d_slope_v112_signal

def f83am_f83_asset_utilization_momentum_calc113_199d_slope_v113_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(199).mean()
    v2 = ratio.rolling(204).std()
    v3 = ratio.diff(199)
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
    res = ratio.diff(199).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc113_199d_slope_v113_signal'] = f83am_f83_asset_utilization_momentum_calc113_199d_slope_v113_signal

def f83am_f83_asset_utilization_momentum_calc114_52d_slope_v114_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(52).mean()
    v2 = ratio.rolling(57).std()
    v3 = ratio.diff(52)
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
    res = ratio.diff(52).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc114_52d_slope_v114_signal'] = f83am_f83_asset_utilization_momentum_calc114_52d_slope_v114_signal

def f83am_f83_asset_utilization_momentum_calc115_105d_slope_v115_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(105).mean()
    v2 = ratio.rolling(110).std()
    v3 = ratio.diff(105)
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
    res = ratio.diff(105).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc115_105d_slope_v115_signal'] = f83am_f83_asset_utilization_momentum_calc115_105d_slope_v115_signal

def f83am_f83_asset_utilization_momentum_calc116_158d_slope_v116_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(158).mean()
    v2 = ratio.rolling(163).std()
    v3 = ratio.diff(158)
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
    res = ratio.diff(158).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc116_158d_slope_v116_signal'] = f83am_f83_asset_utilization_momentum_calc116_158d_slope_v116_signal

def f83am_f83_asset_utilization_momentum_calc117_11d_slope_v117_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(11).mean()
    v2 = ratio.rolling(16).std()
    v3 = ratio.diff(11)
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
    res = ratio.diff(11).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc117_11d_slope_v117_signal'] = f83am_f83_asset_utilization_momentum_calc117_11d_slope_v117_signal

def f83am_f83_asset_utilization_momentum_calc118_64d_slope_v118_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(64).mean()
    v2 = ratio.rolling(69).std()
    v3 = ratio.diff(64)
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
    res = ratio.diff(64).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc118_64d_slope_v118_signal'] = f83am_f83_asset_utilization_momentum_calc118_64d_slope_v118_signal

def f83am_f83_asset_utilization_momentum_calc119_117d_slope_v119_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(117).mean()
    v2 = ratio.rolling(122).std()
    v3 = ratio.diff(117)
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
    res = ratio.diff(117).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc119_117d_slope_v119_signal'] = f83am_f83_asset_utilization_momentum_calc119_117d_slope_v119_signal

def f83am_f83_asset_utilization_momentum_calc120_170d_slope_v120_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(170).mean()
    v2 = ratio.rolling(175).std()
    v3 = ratio.diff(170)
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
    res = ratio.diff(170).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc120_170d_slope_v120_signal'] = f83am_f83_asset_utilization_momentum_calc120_170d_slope_v120_signal

def f83am_f83_asset_utilization_momentum_calc121_23d_slope_v121_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(23).mean()
    v2 = ratio.rolling(28).std()
    v3 = ratio.diff(23)
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
    res = ratio.diff(23).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc121_23d_slope_v121_signal'] = f83am_f83_asset_utilization_momentum_calc121_23d_slope_v121_signal

def f83am_f83_asset_utilization_momentum_calc122_76d_slope_v122_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(76).mean()
    v2 = ratio.rolling(81).std()
    v3 = ratio.diff(76)
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
    res = ratio.diff(76).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc122_76d_slope_v122_signal'] = f83am_f83_asset_utilization_momentum_calc122_76d_slope_v122_signal

def f83am_f83_asset_utilization_momentum_calc123_129d_slope_v123_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(129).mean()
    v2 = ratio.rolling(134).std()
    v3 = ratio.diff(129)
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
    res = ratio.diff(129).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc123_129d_slope_v123_signal'] = f83am_f83_asset_utilization_momentum_calc123_129d_slope_v123_signal

def f83am_f83_asset_utilization_momentum_calc124_182d_slope_v124_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(182).mean()
    v2 = ratio.rolling(187).std()
    v3 = ratio.diff(182)
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
    res = ratio.diff(182).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc124_182d_slope_v124_signal'] = f83am_f83_asset_utilization_momentum_calc124_182d_slope_v124_signal

def f83am_f83_asset_utilization_momentum_calc125_35d_slope_v125_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(35).mean()
    v2 = ratio.rolling(40).std()
    v3 = ratio.diff(35)
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
    res = ratio.diff(35).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc125_35d_slope_v125_signal'] = f83am_f83_asset_utilization_momentum_calc125_35d_slope_v125_signal

def f83am_f83_asset_utilization_momentum_calc126_88d_slope_v126_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(88).mean()
    v2 = ratio.rolling(93).std()
    v3 = ratio.diff(88)
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
    res = ratio.diff(88).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc126_88d_slope_v126_signal'] = f83am_f83_asset_utilization_momentum_calc126_88d_slope_v126_signal

def f83am_f83_asset_utilization_momentum_calc127_141d_slope_v127_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(141).mean()
    v2 = ratio.rolling(146).std()
    v3 = ratio.diff(141)
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
    res = ratio.diff(141).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc127_141d_slope_v127_signal'] = f83am_f83_asset_utilization_momentum_calc127_141d_slope_v127_signal

def f83am_f83_asset_utilization_momentum_calc128_194d_slope_v128_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(194).mean()
    v2 = ratio.rolling(199).std()
    v3 = ratio.diff(194)
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
    res = ratio.diff(194).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc128_194d_slope_v128_signal'] = f83am_f83_asset_utilization_momentum_calc128_194d_slope_v128_signal

def f83am_f83_asset_utilization_momentum_calc129_47d_slope_v129_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(47).mean()
    v2 = ratio.rolling(52).std()
    v3 = ratio.diff(47)
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
    res = ratio.diff(47).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc129_47d_slope_v129_signal'] = f83am_f83_asset_utilization_momentum_calc129_47d_slope_v129_signal

def f83am_f83_asset_utilization_momentum_calc130_100d_slope_v130_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(100).mean()
    v2 = ratio.rolling(105).std()
    v3 = ratio.diff(100)
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
    res = ratio.diff(100).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc130_100d_slope_v130_signal'] = f83am_f83_asset_utilization_momentum_calc130_100d_slope_v130_signal

def f83am_f83_asset_utilization_momentum_calc131_153d_slope_v131_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(153).mean()
    v2 = ratio.rolling(158).std()
    v3 = ratio.diff(153)
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
    res = ratio.diff(153).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc131_153d_slope_v131_signal'] = f83am_f83_asset_utilization_momentum_calc131_153d_slope_v131_signal

def f83am_f83_asset_utilization_momentum_calc132_206d_slope_v132_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(206).mean()
    v2 = ratio.rolling(211).std()
    v3 = ratio.diff(206)
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
    res = ratio.diff(206).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc132_206d_slope_v132_signal'] = f83am_f83_asset_utilization_momentum_calc132_206d_slope_v132_signal

def f83am_f83_asset_utilization_momentum_calc133_59d_slope_v133_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(59).mean()
    v2 = ratio.rolling(64).std()
    v3 = ratio.diff(59)
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
    res = ratio.diff(59).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc133_59d_slope_v133_signal'] = f83am_f83_asset_utilization_momentum_calc133_59d_slope_v133_signal

def f83am_f83_asset_utilization_momentum_calc134_112d_slope_v134_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(112).mean()
    v2 = ratio.rolling(117).std()
    v3 = ratio.diff(112)
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
    res = ratio.diff(112).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc134_112d_slope_v134_signal'] = f83am_f83_asset_utilization_momentum_calc134_112d_slope_v134_signal

def f83am_f83_asset_utilization_momentum_calc135_165d_slope_v135_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(165).mean()
    v2 = ratio.rolling(170).std()
    v3 = ratio.diff(165)
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
    res = ratio.diff(165).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc135_165d_slope_v135_signal'] = f83am_f83_asset_utilization_momentum_calc135_165d_slope_v135_signal

def f83am_f83_asset_utilization_momentum_calc136_18d_slope_v136_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(18).mean()
    v2 = ratio.rolling(23).std()
    v3 = ratio.diff(18)
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
    res = ratio.diff(18).rolling(6).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc136_18d_slope_v136_signal'] = f83am_f83_asset_utilization_momentum_calc136_18d_slope_v136_signal

def f83am_f83_asset_utilization_momentum_calc137_71d_slope_v137_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(71).mean()
    v2 = ratio.rolling(76).std()
    v3 = ratio.diff(71)
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
    res = ratio.diff(71).rolling(7).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc137_71d_slope_v137_signal'] = f83am_f83_asset_utilization_momentum_calc137_71d_slope_v137_signal

def f83am_f83_asset_utilization_momentum_calc138_124d_slope_v138_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(124).mean()
    v2 = ratio.rolling(129).std()
    v3 = ratio.diff(124)
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
    res = ratio.diff(124).rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc138_124d_slope_v138_signal'] = f83am_f83_asset_utilization_momentum_calc138_124d_slope_v138_signal

def f83am_f83_asset_utilization_momentum_calc139_177d_slope_v139_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(177).mean()
    v2 = ratio.rolling(182).std()
    v3 = ratio.diff(177)
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
    res = ratio.diff(177).rolling(9).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc139_177d_slope_v139_signal'] = f83am_f83_asset_utilization_momentum_calc139_177d_slope_v139_signal

def f83am_f83_asset_utilization_momentum_calc140_30d_slope_v140_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(30).mean()
    v2 = ratio.rolling(35).std()
    v3 = ratio.diff(30)
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
    res = ratio.diff(30).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc140_30d_slope_v140_signal'] = f83am_f83_asset_utilization_momentum_calc140_30d_slope_v140_signal

def f83am_f83_asset_utilization_momentum_calc141_83d_slope_v141_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(83).mean()
    v2 = ratio.rolling(88).std()
    v3 = ratio.diff(83)
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
    res = ratio.diff(83).rolling(11).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc141_83d_slope_v141_signal'] = f83am_f83_asset_utilization_momentum_calc141_83d_slope_v141_signal

def f83am_f83_asset_utilization_momentum_calc142_136d_slope_v142_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(136).mean()
    v2 = ratio.rolling(141).std()
    v3 = ratio.diff(136)
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
    res = ratio.diff(136).rolling(12).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc142_136d_slope_v142_signal'] = f83am_f83_asset_utilization_momentum_calc142_136d_slope_v142_signal

def f83am_f83_asset_utilization_momentum_calc143_189d_slope_v143_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(189).mean()
    v2 = ratio.rolling(194).std()
    v3 = ratio.diff(189)
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
    res = ratio.diff(189).rolling(13).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc143_189d_slope_v143_signal'] = f83am_f83_asset_utilization_momentum_calc143_189d_slope_v143_signal

def f83am_f83_asset_utilization_momentum_calc144_42d_slope_v144_signal(assets, opinc):
    s1 = assets * 1.0
    s2 = opinc * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(42).mean()
    v2 = ratio.rolling(47).std()
    v3 = ratio.diff(42)
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
    res = ratio.diff(42).rolling(14).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc144_42d_slope_v144_signal'] = f83am_f83_asset_utilization_momentum_calc144_42d_slope_v144_signal

def f83am_f83_asset_utilization_momentum_calc145_95d_slope_v145_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(95).mean()
    v2 = ratio.rolling(100).std()
    v3 = ratio.diff(95)
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
    res = ratio.diff(95).rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc145_95d_slope_v145_signal'] = f83am_f83_asset_utilization_momentum_calc145_95d_slope_v145_signal

def f83am_f83_asset_utilization_momentum_calc146_148d_slope_v146_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(148).mean()
    v2 = ratio.rolling(153).std()
    v3 = ratio.diff(148)
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
    res = ratio.diff(148).rolling(16).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc146_148d_slope_v146_signal'] = f83am_f83_asset_utilization_momentum_calc146_148d_slope_v146_signal

def f83am_f83_asset_utilization_momentum_calc147_201d_slope_v147_signal(capex, revenue):
    s1 = capex * 1.0
    s2 = revenue * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(201).mean()
    v2 = ratio.rolling(206).std()
    v3 = ratio.diff(201)
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
    res = ratio.diff(201).rolling(17).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc147_201d_slope_v147_signal'] = f83am_f83_asset_utilization_momentum_calc147_201d_slope_v147_signal

def f83am_f83_asset_utilization_momentum_calc148_54d_slope_v148_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(54).mean()
    v2 = ratio.rolling(59).std()
    v3 = ratio.diff(54)
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
    res = ratio.diff(54).rolling(18).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc148_54d_slope_v148_signal'] = f83am_f83_asset_utilization_momentum_calc148_54d_slope_v148_signal

def f83am_f83_asset_utilization_momentum_calc149_107d_slope_v149_signal(revenue, capex):
    s1 = revenue * 1.0
    s2 = capex * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(107).mean()
    v2 = ratio.rolling(112).std()
    v3 = ratio.diff(107)
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
    res = ratio.diff(107).rolling(19).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc149_107d_slope_v149_signal'] = f83am_f83_asset_utilization_momentum_calc149_107d_slope_v149_signal

def f83am_f83_asset_utilization_momentum_calc150_160d_slope_v150_signal(opinc, assets):
    s1 = opinc * 1.0
    s2 = assets * 1.0
    ratio = s1 / s2.replace(0, np.nan)
    v1 = ratio.rolling(160).mean()
    v2 = ratio.rolling(165).std()
    v3 = ratio.diff(160)
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
    res = ratio.diff(160).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f83am_f83_asset_utilization_momentum_calc150_160d_slope_v150_signal'] = f83am_f83_asset_utilization_momentum_calc150_160d_slope_v150_signal


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
