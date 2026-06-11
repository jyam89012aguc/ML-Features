import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_150d_jerk_v001_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(47).std().diff(25).pct_change(40).rolling(44).min() * 0.472529).diff(18).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_150d_jerk_v001_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc001_150d_jerk_v001_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_150d_jerk_v002_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.7392)).rolling(27).min().rolling(22).std().rolling(23).min().diff(10) * 0.345513).diff(15).diff(18).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_150d_jerk_v002_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc002_150d_jerk_v002_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_5d_jerk_v003_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(32).var().rolling(19).max().rolling(27).mean() * 0.946048).diff(10).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_5d_jerk_v003_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc003_5d_jerk_v003_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_5d_jerk_v004_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 2.8375)).rolling(32).var().rolling(2).var().rolling(19).min() * 0.692173).diff(20).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_5d_jerk_v004_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc004_5d_jerk_v004_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_150d_jerk_v005_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 9.4985)).rolling(15).var().diff(45).rolling(14).max().rolling(15).mean() * 0.633389).diff(4).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_150d_jerk_v005_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc005_150d_jerk_v005_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_42d_jerk_v006_signal(ncfo, liabilities):
    res = ((ncfo * 3.5159 - liabilities).diff(31).rolling(36).min().rolling(10).max() * 0.333406).diff(7).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_42d_jerk_v006_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc006_42d_jerk_v006_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_42d_jerk_v007_signal(ncfo, liabilities):
    res = ((ncfo * 1.2940 - liabilities).pct_change(39).pct_change(8).rolling(26).mean().rolling(11).var() * 0.084958).diff(7).diff(19).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_42d_jerk_v007_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc007_42d_jerk_v007_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_200d_jerk_v008_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(5) + 8.0341)).rolling(44).min().pct_change(25).rolling(42).std() * 0.243315).diff(8).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_200d_jerk_v008_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc008_200d_jerk_v008_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_150d_jerk_v009_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.5654)).pct_change(15).rolling(5).min().pct_change(12).rolling(2).std() * 0.780358).diff(2).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_150d_jerk_v009_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc009_150d_jerk_v009_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_252d_jerk_v010_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(6).max().rolling(26).max().rolling(3).max() * 0.192891).diff(5).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_252d_jerk_v010_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc010_252d_jerk_v010_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_252d_jerk_v011_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 7.3847)).rolling(40).min().rolling(2).var().rolling(21).std() * 0.272483).diff(11).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_252d_jerk_v011_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc011_252d_jerk_v011_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_126d_jerk_v012_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(1) + 2.6738)).diff(23).rolling(28).mean() * 0.989589).diff(10).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_126d_jerk_v012_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc012_126d_jerk_v012_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_126d_jerk_v013_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(22).max().rolling(18).mean().rolling(19).mean() * 0.301371).diff(12).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_126d_jerk_v013_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc013_126d_jerk_v013_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_5d_jerk_v014_signal(ncfo, liabilities):
    res = ((ncfo * 4.2110 - liabilities).rolling(12).var().rolling(46).mean() * 0.077705).diff(14).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_5d_jerk_v014_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc014_5d_jerk_v014_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_105d_jerk_v015_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.2520)).rolling(30).std().rolling(35).std().rolling(9).std() * 0.802902).diff(7).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_105d_jerk_v015_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc015_105d_jerk_v015_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_63d_jerk_v016_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.3949)).rolling(9).var().diff(32).rolling(12).std() * 0.783214).diff(4).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_63d_jerk_v016_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc016_63d_jerk_v016_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_84d_jerk_v017_signal(ncfo, liabilities):
    res = ((ncfo * 6.2771 - liabilities).rolling(22).mean().rolling(44).mean() * 0.624427).diff(20).diff(19).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_84d_jerk_v017_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc017_84d_jerk_v017_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_21d_jerk_v018_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.0998)).diff(42).pct_change(18) * 0.568165).diff(15).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_21d_jerk_v018_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc018_21d_jerk_v018_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_5d_jerk_v019_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(31).max().rolling(3).max().rolling(44).std().rolling(32).mean() * 0.634538).diff(20).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_5d_jerk_v019_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc019_5d_jerk_v019_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_150d_jerk_v020_signal(ncfo, liabilities):
    res = ((ncfo.diff(6) / (liabilities.shift(4) + 5.3563)).rolling(19).min().rolling(46).std().rolling(15).mean() * 0.379709).diff(5).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_150d_jerk_v020_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc020_150d_jerk_v020_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_5d_jerk_v021_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(1) + 8.4021)).rolling(40).max().rolling(11).max().rolling(41).max().rolling(9).max() * 0.377067).diff(3).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_5d_jerk_v021_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc021_5d_jerk_v021_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_84d_jerk_v022_signal(ncfo, liabilities):
    res = ((ncfo * 9.5037 - liabilities).pct_change(7).rolling(48).max().rolling(37).var().pct_change(17) * 0.890455).diff(15).diff(7).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_84d_jerk_v022_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc022_84d_jerk_v022_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_5d_jerk_v023_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 1.8179)).rolling(49).std().rolling(13).min().diff(18).rolling(20).min() * 0.419092).diff(12).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_5d_jerk_v023_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc023_5d_jerk_v023_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_150d_jerk_v024_signal(ncfo, liabilities):
    res = ((ncfo * 1.0535 - liabilities).diff(18).diff(39).rolling(24).mean() * 0.558752).diff(15).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_150d_jerk_v024_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc024_150d_jerk_v024_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_21d_jerk_v025_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.2510)).rolling(20).min().rolling(15).mean() * 0.263919).diff(14).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_21d_jerk_v025_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc025_21d_jerk_v025_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_10d_jerk_v026_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 8.4566)).rolling(48).mean().rolling(14).min().pct_change(16) * 0.711014).diff(14).diff(8).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_10d_jerk_v026_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc026_10d_jerk_v026_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_84d_jerk_v027_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.8552)).rolling(42).var().rolling(38).std().rolling(22).var() * 0.171689).diff(12).diff(20).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_84d_jerk_v027_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc027_84d_jerk_v027_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_252d_jerk_v028_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 4.2271)).rolling(10).max().rolling(36).mean() * 0.018350).diff(14).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_252d_jerk_v028_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc028_252d_jerk_v028_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_105d_jerk_v029_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(1) + 8.1776)).rolling(30).mean().rolling(4).mean() * 0.702033).diff(5).diff(3).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_105d_jerk_v029_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc029_105d_jerk_v029_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_252d_jerk_v030_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(3) + 6.1028)).rolling(26).min().pct_change(34).diff(23).rolling(14).var() * 0.340773).diff(14).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_252d_jerk_v030_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc030_252d_jerk_v030_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_200d_jerk_v031_signal(ncfo, liabilities):
    res = ((ncfo.diff(9) / (liabilities.shift(1) + 3.9244)).diff(47).rolling(2).min().rolling(44).min() * 0.964818).diff(5).diff(3).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_200d_jerk_v031_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc031_200d_jerk_v031_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_126d_jerk_v032_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.6559)).rolling(28).std().pct_change(41).rolling(14).mean() * 0.262817).diff(2).diff(7).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_126d_jerk_v032_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc032_126d_jerk_v032_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_126d_jerk_v033_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.7163)).rolling(32).min().rolling(47).mean().diff(39) * 0.424368).diff(4).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_126d_jerk_v033_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc033_126d_jerk_v033_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_200d_jerk_v034_signal(ncfo, liabilities):
    res = ((ncfo * 1.1900 - liabilities).rolling(11).std().pct_change(24).rolling(16).mean() * 0.958402).diff(17).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_200d_jerk_v034_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc034_200d_jerk_v034_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_21d_jerk_v035_signal(ncfo, liabilities):
    res = ((ncfo * 6.6330 - liabilities).rolling(24).mean().rolling(5).std().pct_change(49) * 0.707684).diff(4).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_21d_jerk_v035_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc035_21d_jerk_v035_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_10d_jerk_v036_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.8747)).rolling(20).mean().rolling(31).mean().rolling(40).std() * 0.376308).diff(19).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_10d_jerk_v036_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc036_10d_jerk_v036_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_252d_jerk_v037_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(5) + 9.8427)).pct_change(28).diff(12).rolling(21).min().rolling(9).var() * 0.928432).diff(8).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_252d_jerk_v037_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc037_252d_jerk_v037_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_126d_jerk_v038_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(8).rolling(30).max() * 0.730032).diff(10).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_126d_jerk_v038_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc038_126d_jerk_v038_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_84d_jerk_v039_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 5.0481)).rolling(19).var().rolling(45).min().pct_change(35).rolling(47).std() * 0.076392).diff(10).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_84d_jerk_v039_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc039_84d_jerk_v039_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_42d_jerk_v040_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.0514)).rolling(2).max().rolling(7).var().rolling(7).var().rolling(15).max() * 0.216855).diff(16).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_42d_jerk_v040_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc040_42d_jerk_v040_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_252d_jerk_v041_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.4782)).rolling(41).var().rolling(4).min().rolling(38).std() * 0.178549).diff(2).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_252d_jerk_v041_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc041_252d_jerk_v041_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_5d_jerk_v042_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(2) + 3.8018)).rolling(8).var().rolling(46).max().rolling(18).min().rolling(16).std() * 0.808072).diff(19).diff(2).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_5d_jerk_v042_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc042_5d_jerk_v042_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_10d_jerk_v043_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 0.7510)).diff(39).diff(47).rolling(18).var() * 0.828471).diff(14).diff(15).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_10d_jerk_v043_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc043_10d_jerk_v043_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_252d_jerk_v044_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 5.7259)).rolling(13).min().rolling(28).var().rolling(21).max().rolling(31).var() * 0.056084).diff(7).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_252d_jerk_v044_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc044_252d_jerk_v044_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_42d_jerk_v045_signal(ncfo, liabilities):
    res = ((ncfo * 9.7287 - liabilities).diff(49).diff(45) * 0.038177).diff(9).diff(19).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_42d_jerk_v045_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc045_42d_jerk_v045_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_42d_jerk_v046_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.6946)).rolling(23).mean().rolling(8).mean().pct_change(21).rolling(36).max() * 0.071867).diff(18).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_42d_jerk_v046_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc046_42d_jerk_v046_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_200d_jerk_v047_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(31).rolling(39).var().rolling(16).min().diff(17) * 0.449315).diff(11).diff(3).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_200d_jerk_v047_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc047_200d_jerk_v047_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_21d_jerk_v048_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 6.5360)).pct_change(30).pct_change(19).diff(15) * 0.707848).diff(18).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_21d_jerk_v048_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc048_21d_jerk_v048_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_42d_jerk_v049_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(4) + 1.8363)).rolling(7).max().pct_change(19).rolling(37).var() * 0.420100).diff(7).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_42d_jerk_v049_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc049_42d_jerk_v049_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_200d_jerk_v050_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 6.5260)).rolling(9).max().rolling(6).mean().pct_change(36) * 0.440421).diff(14).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_200d_jerk_v050_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc050_200d_jerk_v050_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_252d_jerk_v051_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(3).diff(33).rolling(36).var().rolling(31).std() * 0.022982).diff(5).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_252d_jerk_v051_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc051_252d_jerk_v051_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_42d_jerk_v052_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(4).var().rolling(16).mean().rolling(32).std().pct_change(32) * 0.022542).diff(15).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_42d_jerk_v052_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc052_42d_jerk_v052_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_63d_jerk_v053_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(1) + 2.5233)).pct_change(23).rolling(12).mean().rolling(11).min() * 0.700773).diff(19).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_63d_jerk_v053_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc053_63d_jerk_v053_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_84d_jerk_v054_signal(ncfo, liabilities):
    res = ((ncfo * 1.0292 - liabilities).rolling(32).mean().rolling(24).std().rolling(2).var() * 0.590531).diff(7).diff(2).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_84d_jerk_v054_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc054_84d_jerk_v054_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_84d_jerk_v055_signal(ncfo, liabilities):
    res = ((ncfo * 0.6605 - liabilities).diff(10).rolling(34).max() * 0.486618).diff(17).diff(14).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_84d_jerk_v055_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc055_84d_jerk_v055_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_200d_jerk_v056_signal(ncfo, liabilities):
    res = ((ncfo * 6.2513 - liabilities).diff(43).diff(34).pct_change(44) * 0.457179).diff(11).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_200d_jerk_v056_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc056_200d_jerk_v056_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_42d_jerk_v057_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(11).rolling(21).std().rolling(16).std() * 0.848243).diff(6).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_42d_jerk_v057_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc057_42d_jerk_v057_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_126d_jerk_v058_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 8.8189)).rolling(18).min().rolling(44).mean().rolling(3).var().diff(18) * 0.116734).diff(10).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_126d_jerk_v058_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc058_126d_jerk_v058_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_150d_jerk_v059_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.9275)).rolling(47).mean().rolling(15).std() * 0.385238).diff(4).diff(20).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_150d_jerk_v059_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc059_150d_jerk_v059_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_42d_jerk_v060_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.2788)).diff(26).rolling(40).std().rolling(10).std().rolling(34).var() * 0.624887).diff(12).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_42d_jerk_v060_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc060_42d_jerk_v060_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_63d_jerk_v061_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(48).rolling(27).var() * 0.331183).diff(18).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_63d_jerk_v061_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc061_63d_jerk_v061_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_105d_jerk_v062_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(4) + 3.1846)).rolling(30).min().rolling(9).min().rolling(35).mean() * 0.263272).diff(11).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_105d_jerk_v062_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc062_105d_jerk_v062_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_42d_jerk_v063_signal(ncfo, liabilities):
    res = ((ncfo * 0.4053 - liabilities).rolling(48).var().rolling(34).max().rolling(19).min().rolling(16).var() * 0.774019).diff(8).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_42d_jerk_v063_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc063_42d_jerk_v063_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_252d_jerk_v064_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(11).var().diff(40).rolling(22).mean() * 0.863971).diff(5).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_252d_jerk_v064_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc064_252d_jerk_v064_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_63d_jerk_v065_signal(ncfo, liabilities):
    res = ((ncfo * 4.6934 - liabilities).rolling(40).mean().pct_change(30) * 0.306962).diff(5).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_63d_jerk_v065_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc065_63d_jerk_v065_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_63d_jerk_v066_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(42).std().rolling(30).std() * 0.055725).diff(9).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_63d_jerk_v066_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc066_63d_jerk_v066_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_126d_jerk_v067_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.2369)).pct_change(47).pct_change(50) * 0.190119).diff(15).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_126d_jerk_v067_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc067_126d_jerk_v067_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_21d_jerk_v068_signal(ncfo, liabilities):
    res = ((ncfo * 9.7116 - liabilities).pct_change(23).pct_change(28) * 0.788935).diff(18).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_21d_jerk_v068_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc068_21d_jerk_v068_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_252d_jerk_v069_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 6.9115)).rolling(18).var().rolling(9).min() * 0.778222).diff(7).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_252d_jerk_v069_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc069_252d_jerk_v069_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_105d_jerk_v070_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.9418)).rolling(32).std().diff(36) * 0.862744).diff(3).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_105d_jerk_v070_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc070_105d_jerk_v070_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_21d_jerk_v071_signal(ncfo, liabilities):
    res = ((ncfo * 1.5092 - liabilities).rolling(16).max().rolling(48).max().rolling(18).max().pct_change(30) * 0.121678).diff(13).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_21d_jerk_v071_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc071_21d_jerk_v071_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_63d_jerk_v072_signal(ncfo, liabilities):
    res = ((ncfo.diff(6) / (liabilities.shift(5) + 5.3447)).rolling(40).min().diff(33).pct_change(24) * 0.383166).diff(17).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_63d_jerk_v072_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc072_63d_jerk_v072_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_150d_jerk_v073_signal(ncfo, liabilities):
    res = ((ncfo * 0.9282 - liabilities).rolling(15).var().pct_change(43) * 0.295051).diff(5).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_150d_jerk_v073_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc073_150d_jerk_v073_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_21d_jerk_v074_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.1832)).rolling(42).std().rolling(45).max() * 0.358173).diff(12).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_21d_jerk_v074_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc074_21d_jerk_v074_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_21d_jerk_v075_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.2558)).pct_change(16).rolling(43).var().rolling(17).min().rolling(22).mean() * 0.124073).diff(13).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_21d_jerk_v075_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc075_21d_jerk_v075_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_10d_jerk_v076_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 8.5949)).rolling(12).mean().rolling(22).var().rolling(15).std() * 0.783727).diff(17).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_10d_jerk_v076_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc076_10d_jerk_v076_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_21d_jerk_v077_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(13).rolling(3).max() * 0.947648).diff(2).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_21d_jerk_v077_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc077_21d_jerk_v077_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_21d_jerk_v078_signal(ncfo, liabilities):
    res = ((ncfo * 9.3479 - liabilities).rolling(41).std().rolling(14).mean() * 0.801197).diff(4).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_21d_jerk_v078_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc078_21d_jerk_v078_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_252d_jerk_v079_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 9.2303)).rolling(41).std().rolling(40).max().pct_change(3) * 0.166060).diff(4).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_252d_jerk_v079_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc079_252d_jerk_v079_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_84d_jerk_v080_signal(ncfo, liabilities):
    res = ((ncfo * 5.1696 - liabilities).rolling(49).var().pct_change(8).rolling(40).max().rolling(26).min() * 0.703161).diff(4).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_84d_jerk_v080_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc080_84d_jerk_v080_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_200d_jerk_v081_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(24).var().rolling(10).std().pct_change(11).rolling(19).mean() * 0.438986).diff(18).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_200d_jerk_v081_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc081_200d_jerk_v081_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_105d_jerk_v082_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.3703)).rolling(48).mean().pct_change(14).rolling(47).var() * 0.591556).diff(6).diff(20).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_105d_jerk_v082_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc082_105d_jerk_v082_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_126d_jerk_v083_signal(ncfo, liabilities):
    res = ((ncfo * 8.6927 - liabilities).rolling(13).mean().diff(28).rolling(49).max() * 0.541519).diff(18).diff(7).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_126d_jerk_v083_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc083_126d_jerk_v083_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_105d_jerk_v084_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(1) + 5.7442)).rolling(46).std().rolling(50).max().rolling(50).max().rolling(21).max() * 0.963950).diff(17).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_105d_jerk_v084_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc084_105d_jerk_v084_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_105d_jerk_v085_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 1.9723)).rolling(35).mean().rolling(43).max() * 0.703804).diff(11).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_105d_jerk_v085_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc085_105d_jerk_v085_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_84d_jerk_v086_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(1) + 0.5465)).rolling(11).max().rolling(25).var() * 0.815417).diff(4).diff(14).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_84d_jerk_v086_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc086_84d_jerk_v086_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_126d_jerk_v087_signal(ncfo, liabilities):
    res = ((ncfo * 6.0787 - liabilities).rolling(46).std().diff(47).rolling(49).max() * 0.386845).diff(16).diff(13).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_126d_jerk_v087_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc087_126d_jerk_v087_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_21d_jerk_v088_signal(ncfo, liabilities):
    res = ((ncfo.diff(9) / (liabilities.shift(5) + 2.0870)).rolling(11).max().rolling(12).std().rolling(29).std() * 0.287328).diff(15).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_21d_jerk_v088_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc088_21d_jerk_v088_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_150d_jerk_v089_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 0.4074)).rolling(37).min().diff(18).rolling(22).min().rolling(31).mean() * 0.772329).diff(8).diff(7).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_150d_jerk_v089_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc089_150d_jerk_v089_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_21d_jerk_v090_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(3).max().rolling(38).std().diff(25) * 0.718385).diff(17).diff(13).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_21d_jerk_v090_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc090_21d_jerk_v090_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_126d_jerk_v091_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(33).rolling(24).max().rolling(31).max().pct_change(43) * 0.419349).diff(5).diff(19).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_126d_jerk_v091_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc091_126d_jerk_v091_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_63d_jerk_v092_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 9.0414)).rolling(13).var().rolling(14).mean() * 0.661250).diff(14).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_63d_jerk_v092_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc092_63d_jerk_v092_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_84d_jerk_v093_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.0424)).rolling(18).mean().pct_change(29).rolling(26).max() * 0.328939).diff(3).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_84d_jerk_v093_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc093_84d_jerk_v093_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_10d_jerk_v094_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(50).rolling(43).min() * 0.780554).diff(4).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_10d_jerk_v094_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc094_10d_jerk_v094_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_150d_jerk_v095_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.9386)).rolling(44).var().rolling(26).var().diff(12).diff(36) * 0.469970).diff(8).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_150d_jerk_v095_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc095_150d_jerk_v095_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_63d_jerk_v096_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.9295)).pct_change(4).diff(45) * 0.358963).diff(16).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_63d_jerk_v096_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc096_63d_jerk_v096_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_63d_jerk_v097_signal(ncfo, liabilities):
    res = ((ncfo * 8.9492 - liabilities).rolling(2).std().rolling(29).std() * 0.347813).diff(9).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_63d_jerk_v097_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc097_63d_jerk_v097_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_150d_jerk_v098_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.1400)).rolling(39).max().rolling(5).std().rolling(50).var() * 0.236226).diff(15).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_150d_jerk_v098_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc098_150d_jerk_v098_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_252d_jerk_v099_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(3) + 2.3793)).pct_change(37).pct_change(11).diff(42).rolling(49).std() * 0.846974).diff(12).diff(10).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_252d_jerk_v099_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc099_252d_jerk_v099_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_21d_jerk_v100_signal(ncfo, liabilities):
    res = ((ncfo * 5.5504 - liabilities).pct_change(37).rolling(12).std().rolling(48).std() * 0.703753).diff(12).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_21d_jerk_v100_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc100_21d_jerk_v100_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_252d_jerk_v101_signal(ncfo, liabilities):
    res = ((ncfo * 7.6842 - liabilities).rolling(24).mean().rolling(11).min().rolling(48).max() * 0.341339).diff(8).diff(6).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_252d_jerk_v101_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc101_252d_jerk_v101_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_42d_jerk_v102_signal(ncfo, liabilities):
    res = ((ncfo.diff(9) / (liabilities.shift(2) + 4.8780)).rolling(50).std().rolling(31).std() * 0.923773).diff(12).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_42d_jerk_v102_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc102_42d_jerk_v102_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_252d_jerk_v103_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.3803)).pct_change(24).rolling(45).var() * 0.231449).diff(14).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_252d_jerk_v103_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc103_252d_jerk_v103_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_252d_jerk_v104_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(2) + 3.1104)).rolling(24).min().rolling(37).var().rolling(30).max() * 0.028680).diff(19).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_252d_jerk_v104_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc104_252d_jerk_v104_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_42d_jerk_v105_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(5) + 9.3390)).pct_change(31).rolling(49).mean() * 0.266873).diff(12).diff(6).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_42d_jerk_v105_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc105_42d_jerk_v105_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_63d_jerk_v106_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(41).var().rolling(24).std().rolling(27).mean() * 0.922077).diff(12).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_63d_jerk_v106_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc106_63d_jerk_v106_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_252d_jerk_v107_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(11).std().pct_change(39).rolling(6).min() * 0.553150).diff(15).diff(4).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_252d_jerk_v107_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc107_252d_jerk_v107_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_84d_jerk_v108_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(10).var().pct_change(39) * 0.685135).diff(9).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_84d_jerk_v108_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc108_84d_jerk_v108_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_126d_jerk_v109_signal(ncfo, liabilities):
    res = ((ncfo * 8.0595 - liabilities).rolling(27).min().rolling(25).var() * 0.316177).diff(20).diff(8).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_126d_jerk_v109_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc109_126d_jerk_v109_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_150d_jerk_v110_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 1.9336)).rolling(13).var().rolling(19).max() * 0.218797).diff(17).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_150d_jerk_v110_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc110_150d_jerk_v110_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_63d_jerk_v111_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 8.6801)).rolling(6).min().pct_change(25).rolling(48).min().rolling(25).max() * 0.415870).diff(5).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_63d_jerk_v111_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc111_63d_jerk_v111_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_200d_jerk_v112_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 1.1100)).rolling(40).var().rolling(32).max().rolling(39).mean() * 0.898255).diff(14).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_200d_jerk_v112_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc112_200d_jerk_v112_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_21d_jerk_v113_signal(ncfo, liabilities):
    res = ((ncfo * 6.8772 - liabilities).rolling(11).min().pct_change(37).rolling(21).mean() * 0.499454).diff(20).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_21d_jerk_v113_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc113_21d_jerk_v113_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_84d_jerk_v114_signal(ncfo, liabilities):
    res = ((ncfo * 3.4812 - liabilities).rolling(26).mean().rolling(28).var() * 0.495836).diff(4).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_84d_jerk_v114_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc114_84d_jerk_v114_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_126d_jerk_v115_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 4.8527)).rolling(31).mean().rolling(5).mean().diff(23) * 0.745480).diff(10).diff(7).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_126d_jerk_v115_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc115_126d_jerk_v115_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_84d_jerk_v116_signal(ncfo, liabilities):
    res = ((ncfo * 5.9225 - liabilities).rolling(27).max().rolling(10).min() * 0.842441).diff(2).diff(3).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_84d_jerk_v116_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc116_84d_jerk_v116_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_105d_jerk_v117_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.2926)).pct_change(35).pct_change(33).rolling(4).max() * 0.641035).diff(7).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_105d_jerk_v117_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc117_105d_jerk_v117_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_200d_jerk_v118_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 2.2494)).rolling(38).var().rolling(26).min().rolling(5).min() * 0.054030).diff(8).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_200d_jerk_v118_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc118_200d_jerk_v118_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_10d_jerk_v119_signal(ncfo, liabilities):
    res = ((ncfo.diff(4) / (liabilities.shift(4) + 6.2078)).pct_change(43).rolling(36).mean().rolling(29).mean().rolling(39).var() * 0.704235).diff(6).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_10d_jerk_v119_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc119_10d_jerk_v119_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_252d_jerk_v120_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 9.3152)).pct_change(14).rolling(32).std() * 0.238765).diff(18).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_252d_jerk_v120_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc120_252d_jerk_v120_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_21d_jerk_v121_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).diff(18).pct_change(4).pct_change(26) * 0.591828).diff(11).diff(13).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_21d_jerk_v121_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc121_21d_jerk_v121_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_5d_jerk_v122_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(1) + 8.8088)).rolling(39).min().pct_change(35).rolling(22).min() * 0.858710).diff(19).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_5d_jerk_v122_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc122_5d_jerk_v122_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_10d_jerk_v123_signal(ncfo, liabilities):
    res = ((ncfo * 4.1886 - liabilities).diff(34).rolling(8).mean().rolling(2).mean() * 0.803216).diff(15).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_10d_jerk_v123_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc123_10d_jerk_v123_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_5d_jerk_v124_signal(ncfo, liabilities):
    res = ((ncfo * 7.3048 - liabilities).rolling(48).std().rolling(9).min() * 0.215483).diff(18).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_5d_jerk_v124_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc124_5d_jerk_v124_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_63d_jerk_v125_signal(ncfo, liabilities):
    res = ((ncfo.diff(6) / (liabilities.shift(3) + 4.8701)).rolling(43).std().diff(43) * 0.452988).diff(15).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_63d_jerk_v125_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc125_63d_jerk_v125_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_10d_jerk_v126_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(12).min().rolling(34).std().rolling(29).var() * 0.713289).diff(4).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_10d_jerk_v126_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc126_10d_jerk_v126_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_63d_jerk_v127_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 6.3136)).rolling(24).std().diff(25).rolling(4).max().rolling(44).max() * 0.663595).diff(19).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_63d_jerk_v127_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc127_63d_jerk_v127_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_84d_jerk_v128_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 1.8117)).rolling(9).mean().rolling(13).min().rolling(44).var() * 0.572982).diff(4).diff(17).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_84d_jerk_v128_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc128_84d_jerk_v128_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_105d_jerk_v129_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(6).min().pct_change(46).rolling(14).min() * 0.863914).diff(4).diff(7).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_105d_jerk_v129_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc129_105d_jerk_v129_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_126d_jerk_v130_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.3630)).rolling(16).std().rolling(23).max() * 0.173261).diff(9).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_126d_jerk_v130_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc130_126d_jerk_v130_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_21d_jerk_v131_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(4) + 1.7569)).rolling(47).min().rolling(26).min().rolling(39).std() * 0.515929).diff(12).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_21d_jerk_v131_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc131_21d_jerk_v131_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_21d_jerk_v132_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.7910)).rolling(24).max().rolling(29).max().rolling(5).var().rolling(27).std() * 0.505599).diff(15).diff(3).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_21d_jerk_v132_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc132_21d_jerk_v132_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_252d_jerk_v133_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 0.6346)).rolling(31).mean().rolling(50).var().diff(33) * 0.606492).diff(18).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_252d_jerk_v133_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc133_252d_jerk_v133_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_84d_jerk_v134_signal(ncfo, liabilities):
    res = ((ncfo * 3.5139 - liabilities).rolling(22).std().rolling(20).std().rolling(49).max().rolling(29).mean() * 0.162496).diff(18).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_84d_jerk_v134_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc134_84d_jerk_v134_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_252d_jerk_v135_signal(ncfo, liabilities):
    res = ((ncfo.diff(7) / (liabilities.shift(3) + 8.5233)).pct_change(13).rolling(15).min() * 0.080739).diff(3).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_252d_jerk_v135_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc135_252d_jerk_v135_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_200d_jerk_v136_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 5.9517)).rolling(44).var().rolling(50).var().diff(42) * 0.906327).diff(2).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_200d_jerk_v136_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc136_200d_jerk_v136_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_42d_jerk_v137_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(13).mean().rolling(42).min().diff(42) * 0.377224).diff(11).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_42d_jerk_v137_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc137_42d_jerk_v137_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_42d_jerk_v138_signal(ncfo, liabilities):
    res = ((liabilities / (ncfo + 7.5766)).diff(3).pct_change(26).rolling(29).max().pct_change(28) * 0.159470).diff(17).diff(15).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_42d_jerk_v138_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc138_42d_jerk_v138_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_126d_jerk_v139_signal(ncfo, liabilities):
    res = ((ncfo.diff(5) / (liabilities.shift(1) + 1.1100)).rolling(23).max().rolling(46).var().rolling(17).std() * 0.403811).diff(11).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_126d_jerk_v139_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc139_126d_jerk_v139_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_150d_jerk_v140_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(33).min().rolling(3).std().rolling(37).var() * 0.328880).diff(17).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_150d_jerk_v140_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc140_150d_jerk_v140_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_200d_jerk_v141_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 8.7550)).rolling(20).var().rolling(10).max() * 0.559164).diff(18).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_200d_jerk_v141_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc141_200d_jerk_v141_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_105d_jerk_v142_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).pct_change(41).rolling(49).mean().rolling(23).var() * 0.383493).diff(12).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_105d_jerk_v142_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc142_105d_jerk_v142_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_42d_jerk_v143_signal(ncfo, liabilities):
    res = ((ncfo.replace(0, np.nan) / liabilities.replace(0, np.nan)).rolling(35).var().rolling(8).max() * 0.294139).diff(14).diff(8).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_42d_jerk_v143_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc143_42d_jerk_v143_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_252d_jerk_v144_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.7613)).rolling(12).mean().rolling(20).mean().rolling(38).mean().rolling(39).mean() * 0.112587).diff(9).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_252d_jerk_v144_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc144_252d_jerk_v144_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_21d_jerk_v145_signal(ncfo, liabilities):
    res = ((ncfo / (liabilities + 3.4234)).pct_change(39).pct_change(31).pct_change(28) * 0.886235).diff(13).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_21d_jerk_v145_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc145_21d_jerk_v145_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_63d_jerk_v146_signal(ncfo, liabilities):
    res = ((ncfo.diff(3) / (liabilities.shift(2) + 7.5920)).rolling(45).min().rolling(5).min() * 0.170553).diff(3).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_63d_jerk_v146_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc146_63d_jerk_v146_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_200d_jerk_v147_signal(ncfo, liabilities):
    res = ((ncfo * 6.0138 - liabilities).rolling(31).max().rolling(40).var() * 0.076054).diff(8).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_200d_jerk_v147_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc147_200d_jerk_v147_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_63d_jerk_v148_signal(ncfo, liabilities):
    res = ((ncfo.diff(8) / (liabilities.shift(1) + 7.8167)).rolling(46).std().rolling(45).mean().pct_change(4).rolling(17).mean() * 0.013217).diff(18).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_63d_jerk_v148_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc148_63d_jerk_v148_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_150d_jerk_v149_signal(ncfo, liabilities):
    res = ((ncfo.diff(10) / (liabilities.shift(2) + 4.6958)).pct_change(13).rolling(39).max().rolling(36).mean() * 0.789718).diff(11).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_150d_jerk_v149_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc149_150d_jerk_v149_signal

def f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_21d_jerk_v150_signal(ncfo, liabilities):
    res = ((ncfo * 4.7450 - liabilities).pct_change(20).rolling(36).min().rolling(11).var().diff(29) * 0.444835).diff(5).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_21d_jerk_v150_signal'] = f201o_f201_operating_cash_flow_to_liabilities_velocity_calc150_21d_jerk_v150_signal


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
