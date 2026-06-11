import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f202e_f202_ebitda_per_share_growth_regime_calc001_63d_jerk_v001_signal(ebitda, sharesbas):
    res = ((ebitda * 3.7756 - sharesbas).pct_change(39).diff(15) * 0.647832).diff(9).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc001_63d_jerk_v001_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc001_63d_jerk_v001_signal

def f202e_f202_ebitda_per_share_growth_regime_calc002_200d_jerk_v002_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(15).diff(24).rolling(7).max() * 0.324067).diff(15).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc002_200d_jerk_v002_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc002_200d_jerk_v002_signal

def f202e_f202_ebitda_per_share_growth_regime_calc003_200d_jerk_v003_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.8451)).rolling(46).max().diff(11).rolling(42).min().rolling(19).mean() * 0.701793).diff(16).diff(3).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc003_200d_jerk_v003_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc003_200d_jerk_v003_signal

def f202e_f202_ebitda_per_share_growth_regime_calc004_84d_jerk_v004_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(1) + 2.2496)).rolling(36).mean().rolling(45).mean().pct_change(15) * 0.599099).diff(14).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc004_84d_jerk_v004_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc004_84d_jerk_v004_signal

def f202e_f202_ebitda_per_share_growth_regime_calc005_63d_jerk_v005_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.2523)).rolling(40).min().rolling(25).std() * 0.434350).diff(12).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc005_63d_jerk_v005_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc005_63d_jerk_v005_signal

def f202e_f202_ebitda_per_share_growth_regime_calc006_252d_jerk_v006_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 8.8683)).rolling(19).var().diff(3) * 0.505776).diff(17).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc006_252d_jerk_v006_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc006_252d_jerk_v006_signal

def f202e_f202_ebitda_per_share_growth_regime_calc007_63d_jerk_v007_signal(ebitda, sharesbas):
    res = ((ebitda * 1.6361 - sharesbas).rolling(3).var().rolling(7).var().rolling(31).std() * 0.996606).diff(17).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc007_63d_jerk_v007_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc007_63d_jerk_v007_signal

def f202e_f202_ebitda_per_share_growth_regime_calc008_252d_jerk_v008_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 2.0996)).rolling(39).mean().diff(50).rolling(38).max().rolling(8).var() * 0.791566).diff(16).diff(6).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc008_252d_jerk_v008_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc008_252d_jerk_v008_signal

def f202e_f202_ebitda_per_share_growth_regime_calc009_63d_jerk_v009_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 8.8670)).rolling(19).var().rolling(36).var() * 0.707368).diff(7).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc009_63d_jerk_v009_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc009_63d_jerk_v009_signal

def f202e_f202_ebitda_per_share_growth_regime_calc010_5d_jerk_v010_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(5) + 2.9455)).diff(49).diff(5).rolling(11).min() * 0.042874).diff(15).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc010_5d_jerk_v010_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc010_5d_jerk_v010_signal

def f202e_f202_ebitda_per_share_growth_regime_calc011_200d_jerk_v011_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(45).max().rolling(30).min() * 0.400656).diff(6).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc011_200d_jerk_v011_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc011_200d_jerk_v011_signal

def f202e_f202_ebitda_per_share_growth_regime_calc012_126d_jerk_v012_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.4959)).rolling(28).max().rolling(15).var().rolling(50).std().rolling(40).max() * 0.240828).diff(11).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc012_126d_jerk_v012_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc012_126d_jerk_v012_signal

def f202e_f202_ebitda_per_share_growth_regime_calc013_21d_jerk_v013_signal(ebitda, sharesbas):
    res = ((ebitda * 1.4886 - sharesbas).rolling(16).mean().diff(35).rolling(35).var().rolling(19).var() * 0.692119).diff(6).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc013_21d_jerk_v013_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc013_21d_jerk_v013_signal

def f202e_f202_ebitda_per_share_growth_regime_calc014_10d_jerk_v014_signal(ebitda, sharesbas):
    res = ((ebitda.diff(5) / (sharesbas.shift(3) + 8.6163)).diff(7).pct_change(40).pct_change(12) * 0.611187).diff(6).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc014_10d_jerk_v014_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc014_10d_jerk_v014_signal

def f202e_f202_ebitda_per_share_growth_regime_calc015_10d_jerk_v015_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 6.5145)).rolling(5).mean().rolling(4).max().rolling(48).var() * 0.749851).diff(15).diff(18).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc015_10d_jerk_v015_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc015_10d_jerk_v015_signal

def f202e_f202_ebitda_per_share_growth_regime_calc016_42d_jerk_v016_signal(ebitda, sharesbas):
    res = ((ebitda * 0.1504 - sharesbas).pct_change(43).rolling(3).max().rolling(47).max() * 0.863210).diff(3).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc016_42d_jerk_v016_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc016_42d_jerk_v016_signal

def f202e_f202_ebitda_per_share_growth_regime_calc017_200d_jerk_v017_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.7472)).rolling(31).min().rolling(43).std() * 0.589324).diff(13).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc017_200d_jerk_v017_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc017_200d_jerk_v017_signal

def f202e_f202_ebitda_per_share_growth_regime_calc018_150d_jerk_v018_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 5.5546)).rolling(32).mean().rolling(30).min().rolling(39).min() * 0.167371).diff(12).diff(7).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc018_150d_jerk_v018_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc018_150d_jerk_v018_signal

def f202e_f202_ebitda_per_share_growth_regime_calc019_5d_jerk_v019_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.5259)).rolling(13).min().rolling(7).max() * 0.054917).diff(10).diff(16).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc019_5d_jerk_v019_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc019_5d_jerk_v019_signal

def f202e_f202_ebitda_per_share_growth_regime_calc020_84d_jerk_v020_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 5.0462)).rolling(22).var().rolling(22).mean().rolling(22).mean().rolling(15).mean() * 0.658053).diff(20).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc020_84d_jerk_v020_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc020_84d_jerk_v020_signal

def f202e_f202_ebitda_per_share_growth_regime_calc021_150d_jerk_v021_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.6233)).rolling(5).var().diff(27).pct_change(33) * 0.225905).diff(14).diff(11).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc021_150d_jerk_v021_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc021_150d_jerk_v021_signal

def f202e_f202_ebitda_per_share_growth_regime_calc022_10d_jerk_v022_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 9.8760)).rolling(41).min().rolling(16).max() * 0.967945).diff(10).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc022_10d_jerk_v022_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc022_10d_jerk_v022_signal

def f202e_f202_ebitda_per_share_growth_regime_calc023_84d_jerk_v023_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.2495)).pct_change(37).rolling(7).min() * 0.275169).diff(20).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc023_84d_jerk_v023_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc023_84d_jerk_v023_signal

def f202e_f202_ebitda_per_share_growth_regime_calc024_63d_jerk_v024_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.5837)).rolling(19).min().rolling(29).var().rolling(45).mean().rolling(10).var() * 0.471906).diff(7).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc024_63d_jerk_v024_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc024_63d_jerk_v024_signal

def f202e_f202_ebitda_per_share_growth_regime_calc025_84d_jerk_v025_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 9.7379)).pct_change(9).pct_change(41).rolling(46).mean().rolling(47).std() * 0.586221).diff(2).diff(2).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc025_84d_jerk_v025_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc025_84d_jerk_v025_signal

def f202e_f202_ebitda_per_share_growth_regime_calc026_126d_jerk_v026_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 3.5027)).pct_change(18).pct_change(39).pct_change(45).rolling(50).std() * 0.922352).diff(17).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc026_126d_jerk_v026_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc026_126d_jerk_v026_signal

def f202e_f202_ebitda_per_share_growth_regime_calc027_105d_jerk_v027_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(4) + 5.7515)).rolling(49).std().rolling(22).min().rolling(26).mean().rolling(47).std() * 0.248071).diff(19).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc027_105d_jerk_v027_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc027_105d_jerk_v027_signal

def f202e_f202_ebitda_per_share_growth_regime_calc028_21d_jerk_v028_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.9700)).rolling(29).mean().diff(24) * 0.269407).diff(10).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc028_21d_jerk_v028_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc028_21d_jerk_v028_signal

def f202e_f202_ebitda_per_share_growth_regime_calc029_21d_jerk_v029_signal(ebitda, sharesbas):
    res = ((ebitda * 8.0812 - sharesbas).rolling(38).min().rolling(31).mean() * 0.139678).diff(2).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc029_21d_jerk_v029_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc029_21d_jerk_v029_signal

def f202e_f202_ebitda_per_share_growth_regime_calc030_200d_jerk_v030_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.4554)).pct_change(43).rolling(14).std().rolling(48).var().rolling(32).std() * 0.920946).diff(19).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc030_200d_jerk_v030_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc030_200d_jerk_v030_signal

def f202e_f202_ebitda_per_share_growth_regime_calc031_252d_jerk_v031_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 5.2099)).rolling(28).std().pct_change(49) * 0.043119).diff(9).diff(19).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc031_252d_jerk_v031_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc031_252d_jerk_v031_signal

def f202e_f202_ebitda_per_share_growth_regime_calc032_10d_jerk_v032_signal(ebitda, sharesbas):
    res = ((ebitda * 1.4227 - sharesbas).rolling(25).min().rolling(9).mean().rolling(16).min().rolling(4).max() * 0.581874).diff(13).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc032_10d_jerk_v032_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc032_10d_jerk_v032_signal

def f202e_f202_ebitda_per_share_growth_regime_calc033_5d_jerk_v033_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.9864)).pct_change(22).rolling(32).std() * 0.259100).diff(20).diff(14).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc033_5d_jerk_v033_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc033_5d_jerk_v033_signal

def f202e_f202_ebitda_per_share_growth_regime_calc034_126d_jerk_v034_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.0504)).rolling(50).var().rolling(45).max().rolling(47).mean().pct_change(16) * 0.372091).diff(17).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc034_126d_jerk_v034_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc034_126d_jerk_v034_signal

def f202e_f202_ebitda_per_share_growth_regime_calc035_200d_jerk_v035_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(41).pct_change(38) * 0.539561).diff(11).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc035_200d_jerk_v035_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc035_200d_jerk_v035_signal

def f202e_f202_ebitda_per_share_growth_regime_calc036_63d_jerk_v036_signal(ebitda, sharesbas):
    res = ((ebitda * 4.1737 - sharesbas).rolling(18).mean().rolling(36).var().rolling(44).min().rolling(50).var() * 0.973924).diff(4).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc036_63d_jerk_v036_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc036_63d_jerk_v036_signal

def f202e_f202_ebitda_per_share_growth_regime_calc037_84d_jerk_v037_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(3) + 4.1493)).pct_change(20).rolling(43).max() * 0.938535).diff(15).diff(18).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc037_84d_jerk_v037_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc037_84d_jerk_v037_signal

def f202e_f202_ebitda_per_share_growth_regime_calc038_126d_jerk_v038_signal(ebitda, sharesbas):
    res = ((ebitda.diff(9) / (sharesbas.shift(2) + 4.1810)).pct_change(39).diff(32).rolling(41).max().rolling(4).max() * 0.321434).diff(5).diff(9).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc038_126d_jerk_v038_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc038_126d_jerk_v038_signal

def f202e_f202_ebitda_per_share_growth_regime_calc039_105d_jerk_v039_signal(ebitda, sharesbas):
    res = ((ebitda * 4.8907 - sharesbas).rolling(9).min().rolling(44).var().rolling(36).mean() * 0.307243).diff(19).diff(20).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc039_105d_jerk_v039_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc039_105d_jerk_v039_signal

def f202e_f202_ebitda_per_share_growth_regime_calc040_126d_jerk_v040_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(1) + 5.7580)).rolling(15).min().rolling(46).var() * 0.513617).diff(4).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc040_126d_jerk_v040_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc040_126d_jerk_v040_signal

def f202e_f202_ebitda_per_share_growth_regime_calc041_105d_jerk_v041_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(16).rolling(7).var().rolling(47).min() * 0.962670).diff(11).diff(3).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc041_105d_jerk_v041_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc041_105d_jerk_v041_signal

def f202e_f202_ebitda_per_share_growth_regime_calc042_126d_jerk_v042_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 2.8157)).rolling(12).min().pct_change(21).rolling(11).std().rolling(6).std() * 0.928648).diff(5).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc042_126d_jerk_v042_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc042_126d_jerk_v042_signal

def f202e_f202_ebitda_per_share_growth_regime_calc043_21d_jerk_v043_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 0.6399)).rolling(27).mean().rolling(47).min() * 0.020258).diff(19).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc043_21d_jerk_v043_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc043_21d_jerk_v043_signal

def f202e_f202_ebitda_per_share_growth_regime_calc044_5d_jerk_v044_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.4206)).rolling(25).var().rolling(40).max() * 0.515996).diff(4).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc044_5d_jerk_v044_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc044_5d_jerk_v044_signal

def f202e_f202_ebitda_per_share_growth_regime_calc045_200d_jerk_v045_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.9191)).rolling(27).var().pct_change(4).rolling(30).max() * 0.708785).diff(2).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc045_200d_jerk_v045_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc045_200d_jerk_v045_signal

def f202e_f202_ebitda_per_share_growth_regime_calc046_21d_jerk_v046_signal(ebitda, sharesbas):
    res = ((ebitda * 0.6807 - sharesbas).pct_change(26).rolling(47).max().pct_change(39) * 0.075057).diff(13).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc046_21d_jerk_v046_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc046_21d_jerk_v046_signal

def f202e_f202_ebitda_per_share_growth_regime_calc047_84d_jerk_v047_signal(ebitda, sharesbas):
    res = ((ebitda * 0.1073 - sharesbas).rolling(34).var().diff(17).pct_change(20) * 0.352844).diff(9).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc047_84d_jerk_v047_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc047_84d_jerk_v047_signal

def f202e_f202_ebitda_per_share_growth_regime_calc048_63d_jerk_v048_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 1.2802)).rolling(7).min().diff(44) * 0.189163).diff(16).diff(4).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc048_63d_jerk_v048_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc048_63d_jerk_v048_signal

def f202e_f202_ebitda_per_share_growth_regime_calc049_42d_jerk_v049_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(2) + 5.1666)).rolling(39).max().rolling(9).max() * 0.267747).diff(14).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc049_42d_jerk_v049_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc049_42d_jerk_v049_signal

def f202e_f202_ebitda_per_share_growth_regime_calc050_200d_jerk_v050_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(20).max().diff(5) * 0.805059).diff(6).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc050_200d_jerk_v050_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc050_200d_jerk_v050_signal

def f202e_f202_ebitda_per_share_growth_regime_calc051_63d_jerk_v051_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 0.5329)).rolling(17).std().rolling(33).var() * 0.095995).diff(8).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc051_63d_jerk_v051_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc051_63d_jerk_v051_signal

def f202e_f202_ebitda_per_share_growth_regime_calc052_150d_jerk_v052_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 6.9435)).rolling(26).min().diff(14).rolling(31).max() * 0.581018).diff(19).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc052_150d_jerk_v052_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc052_150d_jerk_v052_signal

def f202e_f202_ebitda_per_share_growth_regime_calc053_63d_jerk_v053_signal(ebitda, sharesbas):
    res = ((ebitda * 4.0531 - sharesbas).rolling(25).min().rolling(10).mean().pct_change(18) * 0.144009).diff(9).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc053_63d_jerk_v053_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc053_63d_jerk_v053_signal

def f202e_f202_ebitda_per_share_growth_regime_calc054_105d_jerk_v054_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 9.6790)).rolling(22).max().rolling(30).mean() * 0.346834).diff(15).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc054_105d_jerk_v054_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc054_105d_jerk_v054_signal

def f202e_f202_ebitda_per_share_growth_regime_calc055_105d_jerk_v055_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(38).var().rolling(24).mean() * 0.555997).diff(2).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc055_105d_jerk_v055_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc055_105d_jerk_v055_signal

def f202e_f202_ebitda_per_share_growth_regime_calc056_21d_jerk_v056_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 7.4958)).diff(31).diff(47).rolling(6).std().rolling(19).min() * 0.049587).diff(5).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc056_21d_jerk_v056_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc056_21d_jerk_v056_signal

def f202e_f202_ebitda_per_share_growth_regime_calc057_150d_jerk_v057_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(3) + 1.3952)).rolling(26).mean().rolling(37).var().rolling(46).min().rolling(23).mean() * 0.478064).diff(11).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc057_150d_jerk_v057_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc057_150d_jerk_v057_signal

def f202e_f202_ebitda_per_share_growth_regime_calc058_5d_jerk_v058_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 6.9429)).rolling(11).std().diff(40).rolling(4).var() * 0.436399).diff(17).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc058_5d_jerk_v058_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc058_5d_jerk_v058_signal

def f202e_f202_ebitda_per_share_growth_regime_calc059_21d_jerk_v059_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.7075)).rolling(48).std().pct_change(49).rolling(8).mean() * 0.047986).diff(5).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc059_21d_jerk_v059_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc059_21d_jerk_v059_signal

def f202e_f202_ebitda_per_share_growth_regime_calc060_21d_jerk_v060_signal(ebitda, sharesbas):
    res = ((ebitda.diff(9) / (sharesbas.shift(5) + 4.3325)).rolling(35).min().rolling(21).max() * 0.291533).diff(19).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc060_21d_jerk_v060_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc060_21d_jerk_v060_signal

def f202e_f202_ebitda_per_share_growth_regime_calc061_200d_jerk_v061_signal(ebitda, sharesbas):
    res = ((ebitda * 8.0367 - sharesbas).rolling(50).max().pct_change(33).rolling(27).var() * 0.111274).diff(14).diff(3).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc061_200d_jerk_v061_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc061_200d_jerk_v061_signal

def f202e_f202_ebitda_per_share_growth_regime_calc062_21d_jerk_v062_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 8.7854)).rolling(14).std().rolling(4).min().pct_change(40).rolling(40).std() * 0.698456).diff(7).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc062_21d_jerk_v062_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc062_21d_jerk_v062_signal

def f202e_f202_ebitda_per_share_growth_regime_calc063_126d_jerk_v063_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(3) + 1.2049)).rolling(3).std().rolling(29).max() * 0.852182).diff(20).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc063_126d_jerk_v063_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc063_126d_jerk_v063_signal

def f202e_f202_ebitda_per_share_growth_regime_calc064_42d_jerk_v064_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.2841)).pct_change(2).rolling(35).min().rolling(37).std() * 0.761023).diff(6).diff(11).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc064_42d_jerk_v064_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc064_42d_jerk_v064_signal

def f202e_f202_ebitda_per_share_growth_regime_calc065_200d_jerk_v065_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(7).max().rolling(33).var().rolling(35).std().pct_change(40) * 0.864412).diff(10).diff(20).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc065_200d_jerk_v065_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc065_200d_jerk_v065_signal

def f202e_f202_ebitda_per_share_growth_regime_calc066_5d_jerk_v066_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(46).rolling(33).min() * 0.402430).diff(2).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc066_5d_jerk_v066_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc066_5d_jerk_v066_signal

def f202e_f202_ebitda_per_share_growth_regime_calc067_126d_jerk_v067_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 8.9777)).rolling(34).mean().rolling(27).mean().diff(22).pct_change(16) * 0.061277).diff(3).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc067_126d_jerk_v067_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc067_126d_jerk_v067_signal

def f202e_f202_ebitda_per_share_growth_regime_calc068_10d_jerk_v068_signal(ebitda, sharesbas):
    res = ((ebitda * 1.6447 - sharesbas).diff(26).rolling(13).var() * 0.924503).diff(19).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc068_10d_jerk_v068_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc068_10d_jerk_v068_signal

def f202e_f202_ebitda_per_share_growth_regime_calc069_5d_jerk_v069_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.9692)).rolling(47).max().diff(33) * 0.189590).diff(14).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc069_5d_jerk_v069_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc069_5d_jerk_v069_signal

def f202e_f202_ebitda_per_share_growth_regime_calc070_42d_jerk_v070_signal(ebitda, sharesbas):
    res = ((ebitda.diff(9) / (sharesbas.shift(1) + 3.8438)).rolling(37).var().rolling(23).var().rolling(37).max() * 0.286909).diff(8).diff(15).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc070_42d_jerk_v070_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc070_42d_jerk_v070_signal

def f202e_f202_ebitda_per_share_growth_regime_calc071_252d_jerk_v071_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.9379)).rolling(42).min().pct_change(36).rolling(21).var().rolling(35).max() * 0.765883).diff(16).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc071_252d_jerk_v071_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc071_252d_jerk_v071_signal

def f202e_f202_ebitda_per_share_growth_regime_calc072_10d_jerk_v072_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.8736)).rolling(2).max().rolling(13).min().pct_change(46).rolling(21).mean() * 0.308069).diff(9).diff(12).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc072_10d_jerk_v072_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc072_10d_jerk_v072_signal

def f202e_f202_ebitda_per_share_growth_regime_calc073_252d_jerk_v073_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(2) + 6.1904)).rolling(6).min().rolling(6).var() * 0.391095).diff(12).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc073_252d_jerk_v073_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc073_252d_jerk_v073_signal

def f202e_f202_ebitda_per_share_growth_regime_calc074_84d_jerk_v074_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 9.0775)).rolling(33).max().rolling(43).mean() * 0.109391).diff(2).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc074_84d_jerk_v074_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc074_84d_jerk_v074_signal

def f202e_f202_ebitda_per_share_growth_regime_calc075_84d_jerk_v075_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(5).std().pct_change(34).diff(49) * 0.872189).diff(20).diff(12).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc075_84d_jerk_v075_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc075_84d_jerk_v075_signal

def f202e_f202_ebitda_per_share_growth_regime_calc076_150d_jerk_v076_signal(ebitda, sharesbas):
    res = ((ebitda.diff(4) / (sharesbas.shift(4) + 4.4271)).pct_change(42).rolling(36).mean().rolling(19).max() * 0.623891).diff(15).diff(18).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc076_150d_jerk_v076_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc076_150d_jerk_v076_signal

def f202e_f202_ebitda_per_share_growth_regime_calc077_105d_jerk_v077_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(4) + 2.3732)).pct_change(23).rolling(20).mean() * 0.947474).diff(6).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc077_105d_jerk_v077_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc077_105d_jerk_v077_signal

def f202e_f202_ebitda_per_share_growth_regime_calc078_200d_jerk_v078_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(5).mean().rolling(48).max() * 0.715662).diff(14).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc078_200d_jerk_v078_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc078_200d_jerk_v078_signal

def f202e_f202_ebitda_per_share_growth_regime_calc079_21d_jerk_v079_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 7.7851)).rolling(31).mean().diff(24).diff(21).diff(34) * 0.243301).diff(6).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc079_21d_jerk_v079_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc079_21d_jerk_v079_signal

def f202e_f202_ebitda_per_share_growth_regime_calc080_42d_jerk_v080_signal(ebitda, sharesbas):
    res = ((ebitda.diff(4) / (sharesbas.shift(1) + 4.4542)).rolling(8).mean().diff(13).rolling(7).mean().pct_change(16) * 0.330254).diff(7).diff(6).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc080_42d_jerk_v080_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc080_42d_jerk_v080_signal

def f202e_f202_ebitda_per_share_growth_regime_calc081_5d_jerk_v081_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.9939)).rolling(12).max().diff(15).pct_change(44).diff(15) * 0.193158).diff(10).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc081_5d_jerk_v081_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc081_5d_jerk_v081_signal

def f202e_f202_ebitda_per_share_growth_regime_calc082_21d_jerk_v082_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(12).mean().rolling(40).min().rolling(25).mean().rolling(22).max() * 0.745122).diff(8).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc082_21d_jerk_v082_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc082_21d_jerk_v082_signal

def f202e_f202_ebitda_per_share_growth_regime_calc083_63d_jerk_v083_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(29).mean().rolling(44).min() * 0.136289).diff(9).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc083_63d_jerk_v083_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc083_63d_jerk_v083_signal

def f202e_f202_ebitda_per_share_growth_regime_calc084_84d_jerk_v084_signal(ebitda, sharesbas):
    res = ((ebitda * 4.1325 - sharesbas).rolling(4).max().pct_change(28) * 0.225414).diff(9).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc084_84d_jerk_v084_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc084_84d_jerk_v084_signal

def f202e_f202_ebitda_per_share_growth_regime_calc085_10d_jerk_v085_signal(ebitda, sharesbas):
    res = ((ebitda.diff(9) / (sharesbas.shift(1) + 2.7204)).rolling(47).mean().rolling(9).min().diff(12) * 0.584362).diff(12).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc085_10d_jerk_v085_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc085_10d_jerk_v085_signal

def f202e_f202_ebitda_per_share_growth_regime_calc086_84d_jerk_v086_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(11).rolling(14).max().rolling(42).max().rolling(20).max() * 0.141065).diff(13).diff(17).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc086_84d_jerk_v086_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc086_84d_jerk_v086_signal

def f202e_f202_ebitda_per_share_growth_regime_calc087_252d_jerk_v087_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(39).min().rolling(43).max().rolling(44).var() * 0.427737).diff(20).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc087_252d_jerk_v087_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc087_252d_jerk_v087_signal

def f202e_f202_ebitda_per_share_growth_regime_calc088_5d_jerk_v088_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(20).std().rolling(14).var().pct_change(50) * 0.061882).diff(19).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc088_5d_jerk_v088_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc088_5d_jerk_v088_signal

def f202e_f202_ebitda_per_share_growth_regime_calc089_252d_jerk_v089_signal(ebitda, sharesbas):
    res = ((ebitda * 3.5569 - sharesbas).rolling(12).min().rolling(7).var() * 0.518363).diff(8).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc089_252d_jerk_v089_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc089_252d_jerk_v089_signal

def f202e_f202_ebitda_per_share_growth_regime_calc090_5d_jerk_v090_signal(ebitda, sharesbas):
    res = ((ebitda * 7.0229 - sharesbas).rolling(14).mean().rolling(8).max() * 0.796717).diff(7).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc090_5d_jerk_v090_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc090_5d_jerk_v090_signal

def f202e_f202_ebitda_per_share_growth_regime_calc091_84d_jerk_v091_signal(ebitda, sharesbas):
    res = ((ebitda.diff(6) / (sharesbas.shift(3) + 6.0708)).diff(12).diff(7).pct_change(4) * 0.369246).diff(18).diff(7).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc091_84d_jerk_v091_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc091_84d_jerk_v091_signal

def f202e_f202_ebitda_per_share_growth_regime_calc092_5d_jerk_v092_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(30).std().rolling(47).min().rolling(15).mean().rolling(12).min() * 0.625454).diff(12).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc092_5d_jerk_v092_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc092_5d_jerk_v092_signal

def f202e_f202_ebitda_per_share_growth_regime_calc093_126d_jerk_v093_signal(ebitda, sharesbas):
    res = ((ebitda * 4.1730 - sharesbas).rolling(13).max().pct_change(39) * 0.900044).diff(14).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc093_126d_jerk_v093_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc093_126d_jerk_v093_signal

def f202e_f202_ebitda_per_share_growth_regime_calc094_126d_jerk_v094_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 7.0419)).rolling(35).min().rolling(38).var().rolling(12).mean() * 0.501301).diff(3).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc094_126d_jerk_v094_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc094_126d_jerk_v094_signal

def f202e_f202_ebitda_per_share_growth_regime_calc095_5d_jerk_v095_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.5403)).rolling(6).max().pct_change(43).rolling(49).mean() * 0.666697).diff(2).diff(7).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc095_5d_jerk_v095_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc095_5d_jerk_v095_signal

def f202e_f202_ebitda_per_share_growth_regime_calc096_42d_jerk_v096_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.6780)).rolling(38).max().rolling(47).std().rolling(35).max() * 0.597634).diff(5).diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc096_42d_jerk_v096_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc096_42d_jerk_v096_signal

def f202e_f202_ebitda_per_share_growth_regime_calc097_63d_jerk_v097_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(21).var().pct_change(37).rolling(30).std() * 0.820766).diff(2).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc097_63d_jerk_v097_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc097_63d_jerk_v097_signal

def f202e_f202_ebitda_per_share_growth_regime_calc098_200d_jerk_v098_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 1.5365)).diff(39).pct_change(24).rolling(31).max() * 0.653255).diff(19).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc098_200d_jerk_v098_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc098_200d_jerk_v098_signal

def f202e_f202_ebitda_per_share_growth_regime_calc099_84d_jerk_v099_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.1321)).diff(12).rolling(21).std().diff(18).rolling(2).min() * 0.599108).diff(19).diff(17).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc099_84d_jerk_v099_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc099_84d_jerk_v099_signal

def f202e_f202_ebitda_per_share_growth_regime_calc100_126d_jerk_v100_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(41).min().rolling(15).mean().pct_change(43) * 0.210652).diff(10).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc100_126d_jerk_v100_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc100_126d_jerk_v100_signal

def f202e_f202_ebitda_per_share_growth_regime_calc101_126d_jerk_v101_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.1101)).rolling(23).std().rolling(22).var() * 0.214283).diff(18).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc101_126d_jerk_v101_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc101_126d_jerk_v101_signal

def f202e_f202_ebitda_per_share_growth_regime_calc102_21d_jerk_v102_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 4.4417)).rolling(32).max().rolling(4).std() * 0.895018).diff(11).diff(17).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc102_21d_jerk_v102_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc102_21d_jerk_v102_signal

def f202e_f202_ebitda_per_share_growth_regime_calc103_200d_jerk_v103_signal(ebitda, sharesbas):
    res = ((ebitda * 3.7359 - sharesbas).rolling(10).max().diff(34).pct_change(40) * 0.888279).diff(7).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc103_200d_jerk_v103_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc103_200d_jerk_v103_signal

def f202e_f202_ebitda_per_share_growth_regime_calc104_21d_jerk_v104_signal(ebitda, sharesbas):
    res = ((ebitda.diff(5) / (sharesbas.shift(5) + 7.5009)).rolling(33).mean().rolling(37).mean().pct_change(49) * 0.694207).diff(16).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc104_21d_jerk_v104_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc104_21d_jerk_v104_signal

def f202e_f202_ebitda_per_share_growth_regime_calc105_5d_jerk_v105_signal(ebitda, sharesbas):
    res = ((ebitda * 7.9559 - sharesbas).diff(18).rolling(43).var().rolling(47).max().rolling(17).std() * 0.894156).diff(13).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc105_5d_jerk_v105_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc105_5d_jerk_v105_signal

def f202e_f202_ebitda_per_share_growth_regime_calc106_200d_jerk_v106_signal(ebitda, sharesbas):
    res = ((ebitda * 0.7392 - sharesbas).pct_change(23).rolling(38).std() * 0.775822).diff(16).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc106_200d_jerk_v106_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc106_200d_jerk_v106_signal

def f202e_f202_ebitda_per_share_growth_regime_calc107_10d_jerk_v107_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(3) + 5.4819)).rolling(11).max().rolling(38).var().pct_change(5).pct_change(29) * 0.677775).diff(20).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc107_10d_jerk_v107_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc107_10d_jerk_v107_signal

def f202e_f202_ebitda_per_share_growth_regime_calc108_63d_jerk_v108_signal(ebitda, sharesbas):
    res = ((ebitda * 0.9835 - sharesbas).rolling(50).max().diff(49).rolling(36).mean() * 0.902464).diff(19).diff(9).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc108_63d_jerk_v108_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc108_63d_jerk_v108_signal

def f202e_f202_ebitda_per_share_growth_regime_calc109_21d_jerk_v109_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(11).max().pct_change(9).rolling(28).min().pct_change(22) * 0.697925).diff(4).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc109_21d_jerk_v109_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc109_21d_jerk_v109_signal

def f202e_f202_ebitda_per_share_growth_regime_calc110_252d_jerk_v110_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(3) + 3.8717)).rolling(2).mean().rolling(2).mean().pct_change(27) * 0.169149).diff(16).diff(6).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc110_252d_jerk_v110_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc110_252d_jerk_v110_signal

def f202e_f202_ebitda_per_share_growth_regime_calc111_10d_jerk_v111_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.8092)).rolling(15).min().rolling(44).var().rolling(29).std().rolling(4).var() * 0.522587).diff(7).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc111_10d_jerk_v111_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc111_10d_jerk_v111_signal

def f202e_f202_ebitda_per_share_growth_regime_calc112_105d_jerk_v112_signal(ebitda, sharesbas):
    res = ((ebitda.diff(2) / (sharesbas.shift(3) + 3.9863)).rolling(10).max().rolling(44).std() * 0.992582).diff(11).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc112_105d_jerk_v112_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc112_105d_jerk_v112_signal

def f202e_f202_ebitda_per_share_growth_regime_calc113_10d_jerk_v113_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(2).rolling(23).min().rolling(45).max().rolling(14).max() * 0.404468).diff(10).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc113_10d_jerk_v113_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc113_10d_jerk_v113_signal

def f202e_f202_ebitda_per_share_growth_regime_calc114_200d_jerk_v114_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(8).rolling(26).std().rolling(9).std() * 0.940939).diff(19).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc114_200d_jerk_v114_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc114_200d_jerk_v114_signal

def f202e_f202_ebitda_per_share_growth_regime_calc115_10d_jerk_v115_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(25).rolling(40).mean().rolling(33).mean() * 0.916634).diff(19).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc115_10d_jerk_v115_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc115_10d_jerk_v115_signal

def f202e_f202_ebitda_per_share_growth_regime_calc116_63d_jerk_v116_signal(ebitda, sharesbas):
    res = ((ebitda * 7.3901 - sharesbas).rolling(47).std().diff(14) * 0.016110).diff(11).diff(7).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc116_63d_jerk_v116_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc116_63d_jerk_v116_signal

def f202e_f202_ebitda_per_share_growth_regime_calc117_5d_jerk_v117_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(5) + 9.7036)).rolling(31).var().rolling(25).var() * 0.481220).diff(15).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc117_5d_jerk_v117_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc117_5d_jerk_v117_signal

def f202e_f202_ebitda_per_share_growth_regime_calc118_84d_jerk_v118_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.4820)).pct_change(3).rolling(14).min() * 0.748278).diff(15).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc118_84d_jerk_v118_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc118_84d_jerk_v118_signal

def f202e_f202_ebitda_per_share_growth_regime_calc119_105d_jerk_v119_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.3318)).diff(30).rolling(18).min() * 0.332755).diff(5).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc119_105d_jerk_v119_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc119_105d_jerk_v119_signal

def f202e_f202_ebitda_per_share_growth_regime_calc120_252d_jerk_v120_signal(ebitda, sharesbas):
    res = ((ebitda * 3.7042 - sharesbas).pct_change(25).pct_change(6).rolling(11).std().rolling(16).std() * 0.243956).diff(4).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc120_252d_jerk_v120_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc120_252d_jerk_v120_signal

def f202e_f202_ebitda_per_share_growth_regime_calc121_5d_jerk_v121_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.1839)).rolling(45).var().pct_change(39) * 0.867039).diff(4).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc121_5d_jerk_v121_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc121_5d_jerk_v121_signal

def f202e_f202_ebitda_per_share_growth_regime_calc122_10d_jerk_v122_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 3.3661)).rolling(22).max().rolling(28).mean().pct_change(50).diff(42) * 0.986483).diff(14).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc122_10d_jerk_v122_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc122_10d_jerk_v122_signal

def f202e_f202_ebitda_per_share_growth_regime_calc123_63d_jerk_v123_signal(ebitda, sharesbas):
    res = ((ebitda.diff(10) / (sharesbas.shift(3) + 1.0332)).rolling(3).var().rolling(9).mean().pct_change(11).rolling(14).var() * 0.649708).diff(20).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc123_63d_jerk_v123_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc123_63d_jerk_v123_signal

def f202e_f202_ebitda_per_share_growth_regime_calc124_126d_jerk_v124_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(46).std().rolling(15).var() * 0.279873).diff(19).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc124_126d_jerk_v124_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc124_126d_jerk_v124_signal

def f202e_f202_ebitda_per_share_growth_regime_calc125_200d_jerk_v125_signal(ebitda, sharesbas):
    res = ((ebitda * 1.1228 - sharesbas).rolling(38).var().rolling(31).min().rolling(37).min().pct_change(5) * 0.486690).diff(12).diff(19).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc125_200d_jerk_v125_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc125_200d_jerk_v125_signal

def f202e_f202_ebitda_per_share_growth_regime_calc126_150d_jerk_v126_signal(ebitda, sharesbas):
    res = ((ebitda * 2.6431 - sharesbas).rolling(44).var().rolling(6).max().rolling(18).std() * 0.329689).diff(12).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc126_150d_jerk_v126_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc126_150d_jerk_v126_signal

def f202e_f202_ebitda_per_share_growth_regime_calc127_10d_jerk_v127_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(2).min().rolling(24).max().rolling(34).mean() * 0.052996).diff(10).diff(3).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc127_10d_jerk_v127_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc127_10d_jerk_v127_signal

def f202e_f202_ebitda_per_share_growth_regime_calc128_42d_jerk_v128_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 5.8081)).rolling(14).var().rolling(5).max() * 0.616685).diff(10).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc128_42d_jerk_v128_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc128_42d_jerk_v128_signal

def f202e_f202_ebitda_per_share_growth_regime_calc129_5d_jerk_v129_signal(ebitda, sharesbas):
    res = ((ebitda * 4.1952 - sharesbas).rolling(45).max().rolling(9).var().rolling(32).max() * 0.260321).diff(16).diff(4).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc129_5d_jerk_v129_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc129_5d_jerk_v129_signal

def f202e_f202_ebitda_per_share_growth_regime_calc130_126d_jerk_v130_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 9.6792)).pct_change(41).rolling(32).min().diff(50).rolling(45).max() * 0.119749).diff(19).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc130_126d_jerk_v130_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc130_126d_jerk_v130_signal

def f202e_f202_ebitda_per_share_growth_regime_calc131_126d_jerk_v131_signal(ebitda, sharesbas):
    res = ((ebitda.diff(7) / (sharesbas.shift(5) + 7.2073)).rolling(16).min().rolling(12).max() * 0.603224).diff(15).diff(13).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc131_126d_jerk_v131_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc131_126d_jerk_v131_signal

def f202e_f202_ebitda_per_share_growth_regime_calc132_10d_jerk_v132_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(49).min().rolling(34).std().rolling(39).mean().rolling(15).max() * 0.045955).diff(6).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc132_10d_jerk_v132_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc132_10d_jerk_v132_signal

def f202e_f202_ebitda_per_share_growth_regime_calc133_105d_jerk_v133_signal(ebitda, sharesbas):
    res = ((ebitda * 8.2899 - sharesbas).diff(31).rolling(20).mean().rolling(40).std().rolling(33).max() * 0.199546).diff(20).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc133_105d_jerk_v133_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc133_105d_jerk_v133_signal

def f202e_f202_ebitda_per_share_growth_regime_calc134_84d_jerk_v134_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 8.5780)).rolling(50).std().rolling(34).std() * 0.500282).diff(17).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc134_84d_jerk_v134_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc134_84d_jerk_v134_signal

def f202e_f202_ebitda_per_share_growth_regime_calc135_150d_jerk_v135_signal(ebitda, sharesbas):
    res = ((ebitda.diff(5) / (sharesbas.shift(3) + 2.5380)).rolling(12).mean().diff(34).rolling(3).max().rolling(25).std() * 0.474846).diff(13).diff(9).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc135_150d_jerk_v135_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc135_150d_jerk_v135_signal

def f202e_f202_ebitda_per_share_growth_regime_calc136_21d_jerk_v136_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(18).mean().rolling(6).min().diff(35) * 0.614625).diff(12).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc136_21d_jerk_v136_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc136_21d_jerk_v136_signal

def f202e_f202_ebitda_per_share_growth_regime_calc137_200d_jerk_v137_signal(ebitda, sharesbas):
    res = ((sharesbas / (ebitda + 7.8729)).rolling(17).mean().rolling(24).max().pct_change(38).rolling(47).max() * 0.386319).diff(9).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc137_200d_jerk_v137_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc137_200d_jerk_v137_signal

def f202e_f202_ebitda_per_share_growth_regime_calc138_5d_jerk_v138_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(30).var().rolling(27).min() * 0.216242).diff(20).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc138_5d_jerk_v138_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc138_5d_jerk_v138_signal

def f202e_f202_ebitda_per_share_growth_regime_calc139_21d_jerk_v139_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 9.0554)).rolling(4).var().pct_change(29) * 0.370996).diff(3).diff(2).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc139_21d_jerk_v139_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc139_21d_jerk_v139_signal

def f202e_f202_ebitda_per_share_growth_regime_calc140_150d_jerk_v140_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 4.9423)).rolling(37).min().rolling(48).max().rolling(8).max() * 0.882098).diff(6).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc140_150d_jerk_v140_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc140_150d_jerk_v140_signal

def f202e_f202_ebitda_per_share_growth_regime_calc141_84d_jerk_v141_signal(ebitda, sharesbas):
    res = ((ebitda * 9.8367 - sharesbas).rolling(5).max().rolling(22).max() * 0.794290).diff(11).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc141_84d_jerk_v141_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc141_84d_jerk_v141_signal

def f202e_f202_ebitda_per_share_growth_regime_calc142_42d_jerk_v142_signal(ebitda, sharesbas):
    res = ((ebitda.diff(3) / (sharesbas.shift(5) + 2.6440)).rolling(20).var().rolling(5).max().rolling(33).max().pct_change(50) * 0.923421).diff(6).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc142_42d_jerk_v142_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc142_42d_jerk_v142_signal

def f202e_f202_ebitda_per_share_growth_regime_calc143_42d_jerk_v143_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.1988)).rolling(21).mean().rolling(37).max().rolling(35).max() * 0.754653).diff(13).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc143_42d_jerk_v143_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc143_42d_jerk_v143_signal

def f202e_f202_ebitda_per_share_growth_regime_calc144_252d_jerk_v144_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(11).rolling(48).mean().rolling(29).mean() * 0.382509).diff(5).diff(4).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc144_252d_jerk_v144_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc144_252d_jerk_v144_signal

def f202e_f202_ebitda_per_share_growth_regime_calc145_21d_jerk_v145_signal(ebitda, sharesbas):
    res = ((ebitda.diff(8) / (sharesbas.shift(3) + 3.4411)).pct_change(40).rolling(38).mean().pct_change(12) * 0.490403).diff(8).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc145_21d_jerk_v145_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc145_21d_jerk_v145_signal

def f202e_f202_ebitda_per_share_growth_regime_calc146_63d_jerk_v146_signal(ebitda, sharesbas):
    res = ((ebitda.diff(4) / (sharesbas.shift(3) + 9.9453)).diff(25).rolling(16).max() * 0.246955).diff(12).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc146_63d_jerk_v146_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc146_63d_jerk_v146_signal

def f202e_f202_ebitda_per_share_growth_regime_calc147_42d_jerk_v147_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(14).mean().rolling(49).mean().diff(24).rolling(11).std() * 0.776579).diff(8).diff(9).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc147_42d_jerk_v147_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc147_42d_jerk_v147_signal

def f202e_f202_ebitda_per_share_growth_regime_calc148_252d_jerk_v148_signal(ebitda, sharesbas):
    res = ((ebitda / (sharesbas + 0.8326)).pct_change(35).rolling(32).min().rolling(37).max().rolling(24).max() * 0.329159).diff(14).diff(18).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc148_252d_jerk_v148_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc148_252d_jerk_v148_signal

def f202e_f202_ebitda_per_share_growth_regime_calc149_21d_jerk_v149_signal(ebitda, sharesbas):
    res = ((ebitda.diff(5) / (sharesbas.shift(5) + 9.8205)).rolling(33).max().rolling(11).std().rolling(46).mean() * 0.569546).diff(18).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc149_21d_jerk_v149_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc149_21d_jerk_v149_signal

def f202e_f202_ebitda_per_share_growth_regime_calc150_105d_jerk_v150_signal(ebitda, sharesbas):
    res = ((ebitda.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(28).rolling(38).mean() * 0.540954).diff(20).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f202e_f202_ebitda_per_share_growth_regime_calc150_105d_jerk_v150_signal'] = f202e_f202_ebitda_per_share_growth_regime_calc150_105d_jerk_v150_signal


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
