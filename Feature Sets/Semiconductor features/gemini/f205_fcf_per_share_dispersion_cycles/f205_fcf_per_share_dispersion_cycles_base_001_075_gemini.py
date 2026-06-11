import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f205f_f205_fcf_per_share_dispersion_cycles_calc001_126d_base_v001_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 5.1005)).pct_change(49).rolling(14).max() * 0.289010
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc001_126d_base_v001_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc001_126d_base_v001_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc002_126d_base_v002_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 1.2204)).pct_change(23).rolling(17).var().rolling(11).max() * 0.398143
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc002_126d_base_v002_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc002_126d_base_v002_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc003_21d_base_v003_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 5.5899)).rolling(25).mean().rolling(20).min().rolling(42).min().rolling(13).min() * 0.139331
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc003_21d_base_v003_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc003_21d_base_v003_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc004_5d_base_v004_signal(fcf, sharesbas):
    res = (fcf.diff(6) / (sharesbas.shift(3) + 1.8492)).diff(44).rolling(50).max() * 0.595292
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc004_5d_base_v004_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc004_5d_base_v004_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc005_252d_base_v005_signal(fcf, sharesbas):
    res = (fcf.diff(3) / (sharesbas.shift(1) + 0.5710)).rolling(30).std().rolling(16).mean() * 0.321406
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc005_252d_base_v005_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc005_252d_base_v005_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc006_105d_base_v006_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 4.5626)).diff(49).diff(39) * 0.578013
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc006_105d_base_v006_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc006_105d_base_v006_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc007_21d_base_v007_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(41).rolling(29).min().rolling(10).var().rolling(16).min() * 0.085714
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc007_21d_base_v007_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc007_21d_base_v007_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc008_252d_base_v008_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(41).var().rolling(14).mean() * 0.563103
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc008_252d_base_v008_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc008_252d_base_v008_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc009_150d_base_v009_signal(fcf, sharesbas):
    res = (fcf.diff(8) / (sharesbas.shift(3) + 9.8465)).rolling(35).min().rolling(21).min() * 0.172276
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc009_150d_base_v009_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc009_150d_base_v009_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc010_42d_base_v010_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 2.7312)).diff(35).pct_change(37).rolling(10).mean() * 0.398672
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc010_42d_base_v010_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc010_42d_base_v010_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc011_63d_base_v011_signal(fcf, sharesbas):
    res = (fcf.diff(10) / (sharesbas.shift(4) + 7.4418)).rolling(11).min().rolling(38).var().rolling(47).std().pct_change(20) * 0.878676
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc011_63d_base_v011_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc011_63d_base_v011_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc012_126d_base_v012_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 6.6777)).rolling(38).min().rolling(28).var() * 0.966859
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc012_126d_base_v012_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc012_126d_base_v012_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc013_10d_base_v013_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 0.5887)).diff(38).rolling(39).mean() * 0.355495
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc013_10d_base_v013_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc013_10d_base_v013_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc014_200d_base_v014_signal(fcf, sharesbas):
    res = (fcf * 7.2402 - sharesbas).diff(32).pct_change(49).rolling(6).mean() * 0.932970
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc014_200d_base_v014_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc014_200d_base_v014_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc015_63d_base_v015_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 3.1648)).diff(13).diff(45) * 0.737617
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc015_63d_base_v015_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc015_63d_base_v015_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc016_5d_base_v016_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 0.7965)).pct_change(10).rolling(42).var() * 0.752354
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc016_5d_base_v016_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc016_5d_base_v016_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc017_5d_base_v017_signal(fcf, sharesbas):
    res = (fcf * 1.6007 - sharesbas).rolling(10).var().diff(19) * 0.880183
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc017_5d_base_v017_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc017_5d_base_v017_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc018_252d_base_v018_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 2.0791)).rolling(36).mean().pct_change(45).diff(47) * 0.838790
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc018_252d_base_v018_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc018_252d_base_v018_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc019_42d_base_v019_signal(fcf, sharesbas):
    res = (fcf.diff(4) / (sharesbas.shift(2) + 5.8018)).diff(47).rolling(35).var() * 0.487928
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc019_42d_base_v019_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc019_42d_base_v019_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc020_105d_base_v020_signal(fcf, sharesbas):
    res = (fcf.diff(4) / (sharesbas.shift(3) + 7.9146)).rolling(33).min().rolling(3).max().diff(30) * 0.674542
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc020_105d_base_v020_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc020_105d_base_v020_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc021_252d_base_v021_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 3.0784)).pct_change(6).rolling(50).max().rolling(28).mean() * 0.050856
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc021_252d_base_v021_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc021_252d_base_v021_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc022_200d_base_v022_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 6.0667)).rolling(28).mean().rolling(9).mean() * 0.334778
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc022_200d_base_v022_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc022_200d_base_v022_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc023_150d_base_v023_signal(fcf, sharesbas):
    res = (fcf * 0.7621 - sharesbas).rolling(41).min().rolling(27).max() * 0.833304
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc023_150d_base_v023_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc023_150d_base_v023_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc024_126d_base_v024_signal(fcf, sharesbas):
    res = (fcf.diff(6) / (sharesbas.shift(2) + 6.3546)).diff(28).rolling(18).min().diff(11) * 0.551274
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc024_126d_base_v024_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc024_126d_base_v024_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc025_105d_base_v025_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 0.3143)).rolling(43).mean().rolling(44).mean() * 0.479695
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc025_105d_base_v025_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc025_105d_base_v025_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc026_5d_base_v026_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 2.8569)).rolling(12).max().rolling(41).max().diff(20).rolling(14).std() * 0.618687
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc026_5d_base_v026_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc026_5d_base_v026_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc027_84d_base_v027_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 7.9174)).rolling(37).max().rolling(11).min() * 0.767230
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc027_84d_base_v027_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc027_84d_base_v027_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc028_200d_base_v028_signal(fcf, sharesbas):
    res = (fcf.diff(2) / (sharesbas.shift(1) + 5.2836)).rolling(47).std().rolling(50).min().rolling(4).min() * 0.842184
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc028_200d_base_v028_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc028_200d_base_v028_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc029_42d_base_v029_signal(fcf, sharesbas):
    res = (fcf.diff(5) / (sharesbas.shift(1) + 4.4624)).rolling(31).max().rolling(23).min().diff(32).diff(7) * 0.980144
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc029_42d_base_v029_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc029_42d_base_v029_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc030_150d_base_v030_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(11).var().rolling(34).min().diff(3).rolling(7).max() * 0.490254
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc030_150d_base_v030_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc030_150d_base_v030_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc031_21d_base_v031_signal(fcf, sharesbas):
    res = (fcf.diff(2) / (sharesbas.shift(2) + 9.0607)).pct_change(48).pct_change(13).pct_change(17).rolling(5).mean() * 0.949387
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc031_21d_base_v031_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc031_21d_base_v031_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc032_200d_base_v032_signal(fcf, sharesbas):
    res = (fcf * 6.4203 - sharesbas).pct_change(47).rolling(16).var() * 0.269749
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc032_200d_base_v032_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc032_200d_base_v032_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc033_21d_base_v033_signal(fcf, sharesbas):
    res = (fcf.diff(6) / (sharesbas.shift(4) + 2.2944)).rolling(34).var().diff(10).rolling(19).max().rolling(16).mean() * 0.485316
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc033_21d_base_v033_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc033_21d_base_v033_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc034_5d_base_v034_signal(fcf, sharesbas):
    res = (fcf * 8.6939 - sharesbas).rolling(45).min().rolling(20).mean().diff(37).rolling(46).std() * 0.179723
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc034_5d_base_v034_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc034_5d_base_v034_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc035_105d_base_v035_signal(fcf, sharesbas):
    res = (fcf * 1.1350 - sharesbas).rolling(29).std().rolling(35).min().diff(11) * 0.962005
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc035_105d_base_v035_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc035_105d_base_v035_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc036_42d_base_v036_signal(fcf, sharesbas):
    res = (fcf * 1.9396 - sharesbas).rolling(17).min().rolling(42).std().rolling(9).min() * 0.633480
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc036_42d_base_v036_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc036_42d_base_v036_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc037_105d_base_v037_signal(fcf, sharesbas):
    res = (fcf.diff(9) / (sharesbas.shift(1) + 9.6426)).rolling(43).std().rolling(41).var().rolling(11).mean().rolling(18).max() * 0.394051
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc037_105d_base_v037_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc037_105d_base_v037_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc038_5d_base_v038_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 0.9547)).diff(27).rolling(4).std().rolling(10).mean() * 0.892285
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc038_5d_base_v038_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc038_5d_base_v038_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc039_150d_base_v039_signal(fcf, sharesbas):
    res = (fcf.diff(2) / (sharesbas.shift(2) + 3.3548)).rolling(48).std().rolling(21).std().pct_change(4) * 0.784457
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc039_150d_base_v039_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc039_150d_base_v039_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc040_63d_base_v040_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 1.4971)).rolling(46).mean().rolling(41).mean() * 0.616210
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc040_63d_base_v040_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc040_63d_base_v040_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc041_63d_base_v041_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 9.5306)).rolling(50).max().rolling(40).max().rolling(23).mean() * 0.584332
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc041_63d_base_v041_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc041_63d_base_v041_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc042_126d_base_v042_signal(fcf, sharesbas):
    res = (fcf.diff(5) / (sharesbas.shift(2) + 9.4805)).rolling(41).max().rolling(27).mean().pct_change(15) * 0.098478
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc042_126d_base_v042_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc042_126d_base_v042_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc043_84d_base_v043_signal(fcf, sharesbas):
    res = (fcf * 5.8104 - sharesbas).rolling(40).std().rolling(29).var().rolling(39).min().rolling(5).std() * 0.114932
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc043_84d_base_v043_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc043_84d_base_v043_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc044_21d_base_v044_signal(fcf, sharesbas):
    res = (fcf * 7.9479 - sharesbas).rolling(48).mean().rolling(12).max().rolling(32).var().diff(16) * 0.257444
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc044_21d_base_v044_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc044_21d_base_v044_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc045_5d_base_v045_signal(fcf, sharesbas):
    res = (fcf * 3.5860 - sharesbas).rolling(23).mean().rolling(8).var().pct_change(49).diff(38) * 0.353950
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc045_5d_base_v045_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc045_5d_base_v045_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc046_42d_base_v046_signal(fcf, sharesbas):
    res = (fcf.diff(6) / (sharesbas.shift(3) + 5.4607)).pct_change(22).pct_change(21) * 0.216343
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc046_42d_base_v046_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc046_42d_base_v046_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc047_126d_base_v047_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 2.1135)).rolling(5).min().pct_change(48).pct_change(49) * 0.449890
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc047_126d_base_v047_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc047_126d_base_v047_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc048_10d_base_v048_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(44).var().rolling(24).std() * 0.583669
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc048_10d_base_v048_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc048_10d_base_v048_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc049_21d_base_v049_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 5.0231)).rolling(20).mean().rolling(19).std() * 0.658787
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc049_21d_base_v049_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc049_21d_base_v049_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc050_10d_base_v050_signal(fcf, sharesbas):
    res = (fcf.diff(3) / (sharesbas.shift(5) + 8.1800)).rolling(12).max().rolling(28).var().rolling(30).mean().diff(26) * 0.983333
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc050_10d_base_v050_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc050_10d_base_v050_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc051_63d_base_v051_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 2.7982)).rolling(40).std().rolling(6).std().rolling(15).var().rolling(36).min() * 0.827503
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc051_63d_base_v051_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc051_63d_base_v051_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc052_105d_base_v052_signal(fcf, sharesbas):
    res = (fcf * 5.2485 - sharesbas).rolling(31).mean().pct_change(6).diff(22) * 0.903655
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc052_105d_base_v052_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc052_105d_base_v052_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc053_84d_base_v053_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(16).var().rolling(34).max().rolling(4).std() * 0.375968
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc053_84d_base_v053_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc053_84d_base_v053_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc054_21d_base_v054_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(22).pct_change(15).diff(15).rolling(27).var() * 0.226160
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc054_21d_base_v054_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc054_21d_base_v054_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc055_105d_base_v055_signal(fcf, sharesbas):
    res = (fcf * 3.5471 - sharesbas).rolling(38).min().rolling(47).min().rolling(17).mean() * 0.347440
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc055_105d_base_v055_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc055_105d_base_v055_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc056_5d_base_v056_signal(fcf, sharesbas):
    res = (fcf * 8.0628 - sharesbas).pct_change(28).rolling(11).min().rolling(5).mean() * 0.122589
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc056_5d_base_v056_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc056_5d_base_v056_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc057_10d_base_v057_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(31).rolling(28).mean().rolling(12).max().rolling(17).std() * 0.938599
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc057_10d_base_v057_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc057_10d_base_v057_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc058_63d_base_v058_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 7.0092)).diff(43).rolling(9).mean().rolling(2).max() * 0.468774
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc058_63d_base_v058_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc058_63d_base_v058_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc059_200d_base_v059_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 5.4311)).rolling(38).std().rolling(27).var() * 0.334501
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc059_200d_base_v059_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc059_200d_base_v059_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc060_5d_base_v060_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 7.9724)).rolling(39).std().rolling(38).mean().rolling(48).min().rolling(50).var() * 0.039083
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc060_5d_base_v060_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc060_5d_base_v060_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc061_10d_base_v061_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 5.9581)).rolling(39).mean().rolling(42).std() * 0.535131
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc061_10d_base_v061_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc061_10d_base_v061_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc062_150d_base_v062_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(24).diff(4).rolling(26).min().diff(8) * 0.169423
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc062_150d_base_v062_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc062_150d_base_v062_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc063_200d_base_v063_signal(fcf, sharesbas):
    res = (fcf * 2.5322 - sharesbas).rolling(20).var().rolling(43).mean().pct_change(32).pct_change(12) * 0.437159
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc063_200d_base_v063_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc063_200d_base_v063_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc064_5d_base_v064_signal(fcf, sharesbas):
    res = (fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(21).var().pct_change(12).rolling(32).std().rolling(12).max() * 0.509138
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc064_5d_base_v064_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc064_5d_base_v064_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc065_10d_base_v065_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 8.0151)).pct_change(26).rolling(24).mean() * 0.314015
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc065_10d_base_v065_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc065_10d_base_v065_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc066_150d_base_v066_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 2.0031)).rolling(4).std().rolling(47).min() * 0.839242
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc066_150d_base_v066_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc066_150d_base_v066_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc067_150d_base_v067_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 1.7415)).rolling(24).min().rolling(6).min().pct_change(10) * 0.137639
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc067_150d_base_v067_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc067_150d_base_v067_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc068_5d_base_v068_signal(fcf, sharesbas):
    res = (fcf * 4.8760 - sharesbas).diff(20).pct_change(48).rolling(19).std().diff(28) * 0.375031
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc068_5d_base_v068_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc068_5d_base_v068_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc069_126d_base_v069_signal(fcf, sharesbas):
    res = (fcf * 9.6020 - sharesbas).rolling(24).max().rolling(24).std() * 0.152216
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc069_126d_base_v069_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc069_126d_base_v069_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc070_5d_base_v070_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 9.5270)).rolling(49).mean().rolling(26).mean().rolling(31).mean() * 0.679545
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc070_5d_base_v070_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc070_5d_base_v070_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc071_42d_base_v071_signal(fcf, sharesbas):
    res = (fcf / (sharesbas + 3.3352)).pct_change(36).rolling(32).mean() * 0.424602
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc071_42d_base_v071_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc071_42d_base_v071_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc072_126d_base_v072_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 3.7592)).rolling(36).mean().rolling(37).min().pct_change(18) * 0.247797
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc072_126d_base_v072_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc072_126d_base_v072_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc073_42d_base_v073_signal(fcf, sharesbas):
    res = (sharesbas / (fcf + 7.8875)).rolling(13).min().pct_change(49).rolling(3).mean().pct_change(16) * 0.030617
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc073_42d_base_v073_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc073_42d_base_v073_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc074_63d_base_v074_signal(fcf, sharesbas):
    res = (fcf * 2.3611 - sharesbas).rolling(37).std().rolling(27).max().rolling(10).var() * 0.446910
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc074_63d_base_v074_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc074_63d_base_v074_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc075_252d_base_v075_signal(fcf, sharesbas):
    res = (fcf * 7.3398 - sharesbas).rolling(11).std().rolling(40).mean().rolling(38).var().rolling(26).min() * 0.379476
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc075_252d_base_v075_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc075_252d_base_v075_signal


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
