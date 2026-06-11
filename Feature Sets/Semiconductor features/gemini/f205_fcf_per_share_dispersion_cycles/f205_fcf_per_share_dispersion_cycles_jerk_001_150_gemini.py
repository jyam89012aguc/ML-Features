import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f205f_f205_fcf_per_share_dispersion_cycles_calc001_63d_jerk_v001_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(2) + 6.5512)).rolling(32).mean().rolling(40).max().pct_change(18).diff(11) * 0.541422).diff(8).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc001_63d_jerk_v001_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc001_63d_jerk_v001_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc002_84d_jerk_v002_signal(fcf, sharesbas):
    res = ((fcf * 2.3562 - sharesbas).diff(2).pct_change(31) * 0.237797).diff(20).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc002_84d_jerk_v002_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc002_84d_jerk_v002_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc003_200d_jerk_v003_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.7062)).rolling(16).std().rolling(39).max() * 0.433603).diff(20).diff(18).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc003_200d_jerk_v003_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc003_200d_jerk_v003_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc004_5d_jerk_v004_signal(fcf, sharesbas):
    res = ((fcf * 6.9077 - sharesbas).diff(35).rolling(7).std().rolling(48).mean().rolling(14).std() * 0.889210).diff(9).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc004_5d_jerk_v004_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc004_5d_jerk_v004_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc005_5d_jerk_v005_signal(fcf, sharesbas):
    res = ((fcf.diff(4) / (sharesbas.shift(2) + 3.4538)).rolling(18).min().rolling(50).mean().rolling(48).min() * 0.745972).diff(10).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc005_5d_jerk_v005_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc005_5d_jerk_v005_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc006_252d_jerk_v006_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.5976)).rolling(35).std().rolling(29).max().rolling(38).var() * 0.304117).diff(15).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc006_252d_jerk_v006_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc006_252d_jerk_v006_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc007_42d_jerk_v007_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.0502)).rolling(38).max().rolling(24).min().pct_change(25) * 0.294950).diff(7).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc007_42d_jerk_v007_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc007_42d_jerk_v007_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc008_10d_jerk_v008_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.5539)).rolling(18).max().diff(19).pct_change(41) * 0.188746).diff(9).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc008_10d_jerk_v008_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc008_10d_jerk_v008_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc009_5d_jerk_v009_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.5157)).pct_change(48).pct_change(26) * 0.742679).diff(8).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc009_5d_jerk_v009_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc009_5d_jerk_v009_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc010_252d_jerk_v010_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(3) + 2.7477)).rolling(5).var().rolling(18).var().rolling(27).min() * 0.838766).diff(5).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc010_252d_jerk_v010_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc010_252d_jerk_v010_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc011_252d_jerk_v011_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(1) + 3.5283)).diff(47).pct_change(5).pct_change(41) * 0.151327).diff(12).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc011_252d_jerk_v011_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc011_252d_jerk_v011_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc012_42d_jerk_v012_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.8703)).pct_change(14).rolling(10).min() * 0.165235).diff(13).diff(8).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc012_42d_jerk_v012_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc012_42d_jerk_v012_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc013_126d_jerk_v013_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(1) + 5.8185)).rolling(47).var().rolling(5).mean() * 0.147368).diff(12).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc013_126d_jerk_v013_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc013_126d_jerk_v013_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc014_63d_jerk_v014_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(16).max().diff(17).rolling(6).std() * 0.398046).diff(18).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc014_63d_jerk_v014_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc014_63d_jerk_v014_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc015_42d_jerk_v015_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 4.8395)).pct_change(44).pct_change(49).diff(7).rolling(25).var() * 0.596352).diff(19).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc015_42d_jerk_v015_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc015_42d_jerk_v015_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc016_252d_jerk_v016_signal(fcf, sharesbas):
    res = ((fcf * 6.1987 - sharesbas).rolling(34).max().rolling(7).mean() * 0.697036).diff(10).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc016_252d_jerk_v016_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc016_252d_jerk_v016_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc017_105d_jerk_v017_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(5) + 9.6438)).rolling(2).std().diff(19) * 0.701257).diff(6).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc017_105d_jerk_v017_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc017_105d_jerk_v017_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc018_126d_jerk_v018_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.7951)).rolling(34).max().rolling(49).min().rolling(27).min().rolling(2).min() * 0.536364).diff(20).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc018_126d_jerk_v018_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc018_126d_jerk_v018_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc019_10d_jerk_v019_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(10).min().rolling(32).min().pct_change(17).diff(49) * 0.889638).diff(13).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc019_10d_jerk_v019_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc019_10d_jerk_v019_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc020_105d_jerk_v020_signal(fcf, sharesbas):
    res = ((fcf * 4.9529 - sharesbas).rolling(3).max().diff(24).rolling(31).max().rolling(5).std() * 0.220670).diff(12).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc020_105d_jerk_v020_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc020_105d_jerk_v020_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc021_200d_jerk_v021_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(28).rolling(17).max().rolling(25).max() * 0.420173).diff(17).diff(7).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc021_200d_jerk_v021_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc021_200d_jerk_v021_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc022_5d_jerk_v022_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(18).var().rolling(15).var().rolling(26).max() * 0.979791).diff(19).diff(15).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc022_5d_jerk_v022_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc022_5d_jerk_v022_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc023_84d_jerk_v023_signal(fcf, sharesbas):
    res = ((fcf * 0.7332 - sharesbas).rolling(25).min().rolling(41).mean().rolling(39).max().rolling(24).var() * 0.325876).diff(16).diff(10).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc023_84d_jerk_v023_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc023_84d_jerk_v023_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc024_252d_jerk_v024_signal(fcf, sharesbas):
    res = ((fcf * 0.7025 - sharesbas).rolling(32).mean().rolling(12).std().rolling(34).var() * 0.900298).diff(20).diff(4).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc024_252d_jerk_v024_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc024_252d_jerk_v024_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc025_126d_jerk_v025_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.7591)).rolling(27).max().rolling(43).mean() * 0.052671).diff(5).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc025_126d_jerk_v025_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc025_126d_jerk_v025_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc026_42d_jerk_v026_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 5.3877)).rolling(50).var().rolling(39).mean().rolling(14).min().pct_change(13) * 0.209498).diff(15).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc026_42d_jerk_v026_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc026_42d_jerk_v026_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc027_5d_jerk_v027_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(3) + 6.8659)).rolling(22).var().rolling(50).var().rolling(39).var() * 0.952422).diff(2).diff(3).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc027_5d_jerk_v027_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc027_5d_jerk_v027_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc028_105d_jerk_v028_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 3.9255)).rolling(16).std().rolling(42).var().rolling(23).var().rolling(40).mean() * 0.260003).diff(7).diff(17).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc028_105d_jerk_v028_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc028_105d_jerk_v028_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc029_21d_jerk_v029_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(45).min().rolling(36).std() * 0.741738).diff(16).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc029_21d_jerk_v029_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc029_21d_jerk_v029_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc030_126d_jerk_v030_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 6.9509)).rolling(22).min().rolling(42).var() * 0.698784).diff(12).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc030_126d_jerk_v030_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc030_126d_jerk_v030_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc031_42d_jerk_v031_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.4848)).rolling(34).var().rolling(23).std().rolling(15).min().rolling(2).std() * 0.781524).diff(12).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc031_42d_jerk_v031_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc031_42d_jerk_v031_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc032_126d_jerk_v032_signal(fcf, sharesbas):
    res = ((fcf * 4.8781 - sharesbas).rolling(12).var().rolling(37).var().rolling(34).std() * 0.912993).diff(12).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc032_126d_jerk_v032_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc032_126d_jerk_v032_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc033_126d_jerk_v033_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(2) + 4.5102)).rolling(4).var().rolling(6).min() * 0.789767).diff(20).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc033_126d_jerk_v033_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc033_126d_jerk_v033_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc034_10d_jerk_v034_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 9.0817)).rolling(12).std().rolling(29).mean().pct_change(3) * 0.273810).diff(10).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc034_10d_jerk_v034_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc034_10d_jerk_v034_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc035_105d_jerk_v035_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(3) + 8.4114)).rolling(16).max().rolling(18).var().pct_change(3) * 0.683162).diff(10).diff(17).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc035_105d_jerk_v035_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc035_105d_jerk_v035_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc036_150d_jerk_v036_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(46).var().rolling(45).var().diff(24).rolling(40).min() * 0.359143).diff(11).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc036_150d_jerk_v036_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc036_150d_jerk_v036_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc037_10d_jerk_v037_signal(fcf, sharesbas):
    res = ((fcf * 2.3751 - sharesbas).rolling(34).std().pct_change(7).rolling(11).var().rolling(50).var() * 0.938953).diff(13).diff(14).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc037_10d_jerk_v037_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc037_10d_jerk_v037_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc038_63d_jerk_v038_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.2451)).rolling(50).min().pct_change(40).rolling(11).var() * 0.328606).diff(2).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc038_63d_jerk_v038_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc038_63d_jerk_v038_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc039_84d_jerk_v039_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.2086)).rolling(13).var().rolling(45).max().rolling(36).min().pct_change(49) * 0.741454).diff(13).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc039_84d_jerk_v039_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc039_84d_jerk_v039_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc040_84d_jerk_v040_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(2) + 8.5207)).pct_change(27).rolling(49).std().rolling(35).std() * 0.786989).diff(16).diff(12).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc040_84d_jerk_v040_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc040_84d_jerk_v040_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc041_84d_jerk_v041_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(15).max().rolling(15).max().rolling(11).min().rolling(3).min() * 0.157496).diff(9).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc041_84d_jerk_v041_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc041_84d_jerk_v041_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc042_200d_jerk_v042_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(13).var().diff(27).diff(25).diff(46) * 0.718334).diff(19).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc042_200d_jerk_v042_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc042_200d_jerk_v042_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc043_21d_jerk_v043_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(3) + 2.9460)).rolling(4).var().pct_change(15).diff(3).rolling(45).min() * 0.273609).diff(11).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc043_21d_jerk_v043_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc043_21d_jerk_v043_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc044_42d_jerk_v044_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(3) + 7.1413)).rolling(47).max().rolling(49).mean().pct_change(8).rolling(35).mean() * 0.675035).diff(8).diff(9).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc044_42d_jerk_v044_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc044_42d_jerk_v044_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc045_126d_jerk_v045_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 5.5689)).rolling(7).min().rolling(24).var().diff(29).rolling(45).var() * 0.031587).diff(9).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc045_126d_jerk_v045_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc045_126d_jerk_v045_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc046_126d_jerk_v046_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.9472)).pct_change(49).rolling(45).var().diff(17) * 0.848853).diff(17).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc046_126d_jerk_v046_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc046_126d_jerk_v046_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc047_252d_jerk_v047_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 0.1490)).rolling(20).max().rolling(4).max() * 0.258106).diff(2).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc047_252d_jerk_v047_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc047_252d_jerk_v047_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc048_63d_jerk_v048_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(23).mean().rolling(32).mean().rolling(36).mean().rolling(7).mean() * 0.157398).diff(9).diff(20).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc048_63d_jerk_v048_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc048_63d_jerk_v048_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc049_42d_jerk_v049_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(29).mean().pct_change(44).rolling(18).var() * 0.282432).diff(12).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc049_42d_jerk_v049_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc049_42d_jerk_v049_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc050_63d_jerk_v050_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.1438)).rolling(25).mean().rolling(8).mean().rolling(43).min().rolling(47).min() * 0.759938).diff(13).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc050_63d_jerk_v050_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc050_63d_jerk_v050_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc051_84d_jerk_v051_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(5) + 8.3156)).rolling(11).std().rolling(36).std().pct_change(49).rolling(44).max() * 0.097194).diff(2).diff(2).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc051_84d_jerk_v051_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc051_84d_jerk_v051_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc052_5d_jerk_v052_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(45).pct_change(32) * 0.130353).diff(2).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc052_5d_jerk_v052_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc052_5d_jerk_v052_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc053_42d_jerk_v053_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(43).max().rolling(2).mean() * 0.850049).diff(15).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc053_42d_jerk_v053_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc053_42d_jerk_v053_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc054_5d_jerk_v054_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.3363)).rolling(47).mean().rolling(14).max().pct_change(19) * 0.246398).diff(3).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc054_5d_jerk_v054_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc054_5d_jerk_v054_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc055_252d_jerk_v055_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(3) + 9.5257)).rolling(28).mean().rolling(11).min() * 0.925203).diff(9).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc055_252d_jerk_v055_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc055_252d_jerk_v055_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc056_5d_jerk_v056_signal(fcf, sharesbas):
    res = ((fcf * 7.0071 - sharesbas).rolling(12).max().rolling(19).var() * 0.192929).diff(13).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc056_5d_jerk_v056_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc056_5d_jerk_v056_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc057_84d_jerk_v057_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 0.5094)).pct_change(28).rolling(21).std() * 0.473495).diff(7).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc057_84d_jerk_v057_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc057_84d_jerk_v057_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc058_150d_jerk_v058_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(47).rolling(27).max() * 0.798183).diff(8).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc058_150d_jerk_v058_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc058_150d_jerk_v058_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc059_63d_jerk_v059_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.7066)).rolling(32).min().rolling(26).var() * 0.081281).diff(3).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc059_63d_jerk_v059_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc059_63d_jerk_v059_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc060_10d_jerk_v060_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.5346)).rolling(24).var().rolling(30).var().rolling(10).mean() * 0.728956).diff(4).diff(14).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc060_10d_jerk_v060_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc060_10d_jerk_v060_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc061_84d_jerk_v061_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 9.8050)).rolling(22).std().rolling(12).std().rolling(12).std().rolling(28).min() * 0.100919).diff(13).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc061_84d_jerk_v061_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc061_84d_jerk_v061_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc062_150d_jerk_v062_signal(fcf, sharesbas):
    res = ((fcf * 4.0062 - sharesbas).rolling(32).min().rolling(24).var().rolling(11).var() * 0.236844).diff(3).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc062_150d_jerk_v062_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc062_150d_jerk_v062_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc063_63d_jerk_v063_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(50).rolling(10).std() * 0.170163).diff(10).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc063_63d_jerk_v063_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc063_63d_jerk_v063_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc064_84d_jerk_v064_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.5768)).diff(12).rolling(46).std().rolling(46).max() * 0.319391).diff(4).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc064_84d_jerk_v064_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc064_84d_jerk_v064_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc065_42d_jerk_v065_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(5) + 4.8669)).rolling(45).max().rolling(9).var().rolling(3).std().pct_change(33) * 0.417165).diff(18).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc065_42d_jerk_v065_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc065_42d_jerk_v065_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc066_10d_jerk_v066_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(4) + 3.9901)).rolling(50).var().diff(41).diff(2).rolling(41).max() * 0.307682).diff(7).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc066_10d_jerk_v066_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc066_10d_jerk_v066_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc067_252d_jerk_v067_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(5) + 4.7058)).diff(38).rolling(45).max() * 0.849238).diff(19).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc067_252d_jerk_v067_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc067_252d_jerk_v067_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc068_10d_jerk_v068_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(4) + 9.1350)).rolling(5).max().pct_change(32).diff(5).rolling(11).max() * 0.149215).diff(14).diff(3).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc068_10d_jerk_v068_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc068_10d_jerk_v068_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc069_126d_jerk_v069_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(4) + 6.6185)).rolling(43).var().rolling(45).std().rolling(4).std() * 0.194837).diff(5).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc069_126d_jerk_v069_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc069_126d_jerk_v069_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc070_5d_jerk_v070_signal(fcf, sharesbas):
    res = ((fcf.diff(7) / (sharesbas.shift(1) + 2.4775)).rolling(7).var().diff(43) * 0.437481).diff(10).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc070_5d_jerk_v070_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc070_5d_jerk_v070_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc071_42d_jerk_v071_signal(fcf, sharesbas):
    res = ((fcf * 6.9137 - sharesbas).rolling(16).mean().rolling(37).mean().rolling(49).min().rolling(6).max() * 0.176735).diff(9).diff(16).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc071_42d_jerk_v071_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc071_42d_jerk_v071_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc072_10d_jerk_v072_signal(fcf, sharesbas):
    res = ((fcf.diff(9) / (sharesbas.shift(1) + 0.8226)).rolling(17).mean().pct_change(34) * 0.684994).diff(11).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc072_10d_jerk_v072_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc072_10d_jerk_v072_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc073_63d_jerk_v073_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(1) + 2.9782)).rolling(19).std().pct_change(3).pct_change(31).rolling(31).var() * 0.659875).diff(3).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc073_63d_jerk_v073_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc073_63d_jerk_v073_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc074_63d_jerk_v074_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.6566)).rolling(16).std().rolling(9).max().diff(22) * 0.411466).diff(9).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc074_63d_jerk_v074_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc074_63d_jerk_v074_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc075_105d_jerk_v075_signal(fcf, sharesbas):
    res = ((fcf.diff(4) / (sharesbas.shift(1) + 2.3804)).diff(7).rolling(42).mean().rolling(15).min() * 0.742773).diff(18).diff(14).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc075_105d_jerk_v075_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc075_105d_jerk_v075_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc076_105d_jerk_v076_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.3375)).rolling(3).min().rolling(4).var().pct_change(6) * 0.531755).diff(8).diff(9).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc076_105d_jerk_v076_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc076_105d_jerk_v076_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc077_10d_jerk_v077_signal(fcf, sharesbas):
    res = ((fcf * 2.2127 - sharesbas).diff(14).rolling(8).var() * 0.034419).diff(5).diff(18).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc077_10d_jerk_v077_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc077_10d_jerk_v077_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc078_252d_jerk_v078_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.5106)).rolling(14).mean().diff(2).rolling(38).mean().rolling(50).var() * 0.075736).diff(10).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc078_252d_jerk_v078_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc078_252d_jerk_v078_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc079_150d_jerk_v079_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.6292)).pct_change(32).rolling(24).min() * 0.578377).diff(11).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc079_150d_jerk_v079_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc079_150d_jerk_v079_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc080_150d_jerk_v080_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(39).max().diff(14) * 0.118958).diff(4).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc080_150d_jerk_v080_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc080_150d_jerk_v080_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc081_252d_jerk_v081_signal(fcf, sharesbas):
    res = ((fcf * 6.3465 - sharesbas).diff(33).rolling(42).mean() * 0.676247).diff(16).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc081_252d_jerk_v081_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc081_252d_jerk_v081_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc082_63d_jerk_v082_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.3572)).diff(34).pct_change(49).diff(41).pct_change(19) * 0.170861).diff(20).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc082_63d_jerk_v082_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc082_63d_jerk_v082_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc083_105d_jerk_v083_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.1638)).rolling(42).var().rolling(42).max().rolling(40).min().pct_change(49) * 0.164133).diff(17).diff(19).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc083_105d_jerk_v083_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc083_105d_jerk_v083_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc084_21d_jerk_v084_signal(fcf, sharesbas):
    res = ((fcf.diff(4) / (sharesbas.shift(4) + 5.9809)).rolling(3).max().rolling(17).var().diff(26) * 0.014084).diff(3).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc084_21d_jerk_v084_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc084_21d_jerk_v084_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc085_5d_jerk_v085_signal(fcf, sharesbas):
    res = ((fcf * 5.0741 - sharesbas).pct_change(12).rolling(48).min().rolling(41).std() * 0.234948).diff(13).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc085_5d_jerk_v085_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc085_5d_jerk_v085_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc086_150d_jerk_v086_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(4) + 1.9073)).rolling(38).std().rolling(46).max().rolling(37).std().rolling(28).max() * 0.074256).diff(5).diff(18).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc086_150d_jerk_v086_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc086_150d_jerk_v086_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc087_5d_jerk_v087_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.4040)).rolling(35).min().diff(36) * 0.909957).diff(10).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc087_5d_jerk_v087_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc087_5d_jerk_v087_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc088_10d_jerk_v088_signal(fcf, sharesbas):
    res = ((fcf * 2.9988 - sharesbas).rolling(27).std().pct_change(17).rolling(42).var() * 0.262534).diff(12).diff(18).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc088_10d_jerk_v088_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc088_10d_jerk_v088_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc089_10d_jerk_v089_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.9948)).diff(42).diff(38).rolling(49).max().rolling(2).var() * 0.707300).diff(12).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc089_10d_jerk_v089_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc089_10d_jerk_v089_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc090_252d_jerk_v090_signal(fcf, sharesbas):
    res = ((fcf * 0.5415 - sharesbas).diff(43).rolling(25).std() * 0.504449).diff(8).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc090_252d_jerk_v090_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc090_252d_jerk_v090_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc091_126d_jerk_v091_signal(fcf, sharesbas):
    res = ((fcf.diff(9) / (sharesbas.shift(5) + 7.0052)).rolling(3).mean().rolling(40).max() * 0.737226).diff(13).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc091_126d_jerk_v091_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc091_126d_jerk_v091_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc092_10d_jerk_v092_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(3).max().pct_change(8) * 0.941445).diff(17).diff(15).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc092_10d_jerk_v092_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc092_10d_jerk_v092_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc093_63d_jerk_v093_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(1) + 8.7158)).diff(5).rolling(23).var().diff(10) * 0.206179).diff(13).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc093_63d_jerk_v093_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc093_63d_jerk_v093_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc094_21d_jerk_v094_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 7.5502)).rolling(34).mean().rolling(49).std().rolling(43).min() * 0.884601).diff(3).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc094_21d_jerk_v094_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc094_21d_jerk_v094_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc095_21d_jerk_v095_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(5) + 6.6707)).pct_change(49).diff(3).pct_change(8).rolling(42).std() * 0.896212).diff(19).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc095_21d_jerk_v095_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc095_21d_jerk_v095_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc096_150d_jerk_v096_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 7.1290)).rolling(20).var().pct_change(16).pct_change(38).rolling(37).std() * 0.319127).diff(12).diff(8).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc096_150d_jerk_v096_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc096_150d_jerk_v096_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc097_84d_jerk_v097_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(29).mean().pct_change(4).rolling(44).std() * 0.469380).diff(7).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc097_84d_jerk_v097_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc097_84d_jerk_v097_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc098_200d_jerk_v098_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(3) + 3.2312)).diff(33).pct_change(28).rolling(7).mean().rolling(20).mean() * 0.734080).diff(6).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc098_200d_jerk_v098_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc098_200d_jerk_v098_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc099_10d_jerk_v099_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.9269)).rolling(11).std().rolling(45).mean().pct_change(25) * 0.198906).diff(9).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc099_10d_jerk_v099_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc099_10d_jerk_v099_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc100_63d_jerk_v100_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 7.0511)).rolling(3).std().rolling(13).max().rolling(41).min().rolling(3).mean() * 0.720577).diff(17).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc100_63d_jerk_v100_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc100_63d_jerk_v100_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc101_42d_jerk_v101_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.2197)).diff(45).rolling(20).mean().rolling(15).mean() * 0.124430).diff(10).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc101_42d_jerk_v101_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc101_42d_jerk_v101_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc102_42d_jerk_v102_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 7.7514)).rolling(34).min().rolling(32).std().rolling(14).max().diff(41) * 0.025250).diff(13).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc102_42d_jerk_v102_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc102_42d_jerk_v102_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc103_200d_jerk_v103_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.3687)).rolling(35).mean().diff(44).diff(37) * 0.464277).diff(19).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc103_200d_jerk_v103_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc103_200d_jerk_v103_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc104_200d_jerk_v104_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(6).max().rolling(46).std() * 0.759792).diff(7).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc104_200d_jerk_v104_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc104_200d_jerk_v104_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc105_5d_jerk_v105_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(2) + 1.2967)).rolling(43).std().rolling(37).mean().rolling(18).max() * 0.184370).diff(7).diff(2).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc105_5d_jerk_v105_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc105_5d_jerk_v105_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc106_63d_jerk_v106_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.1092)).rolling(22).var().pct_change(13).rolling(9).max() * 0.262990).diff(6).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc106_63d_jerk_v106_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc106_63d_jerk_v106_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc107_84d_jerk_v107_signal(fcf, sharesbas):
    res = ((fcf * 5.4115 - sharesbas).rolling(40).mean().rolling(15).min() * 0.440973).diff(13).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc107_84d_jerk_v107_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc107_84d_jerk_v107_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc108_10d_jerk_v108_signal(fcf, sharesbas):
    res = ((fcf * 8.5263 - sharesbas).diff(20).rolling(22).var().rolling(4).max() * 0.736368).diff(10).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc108_10d_jerk_v108_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc108_10d_jerk_v108_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc109_252d_jerk_v109_signal(fcf, sharesbas):
    res = ((fcf * 9.9996 - sharesbas).rolling(28).std().rolling(24).mean().diff(31).rolling(16).max() * 0.285771).diff(19).diff(11).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc109_252d_jerk_v109_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc109_252d_jerk_v109_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc110_42d_jerk_v110_signal(fcf, sharesbas):
    res = ((fcf * 7.4388 - sharesbas).pct_change(15).rolling(21).var() * 0.980725).diff(2).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc110_42d_jerk_v110_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc110_42d_jerk_v110_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc111_42d_jerk_v111_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 5.7859)).pct_change(38).rolling(50).min() * 0.584205).diff(18).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc111_42d_jerk_v111_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc111_42d_jerk_v111_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc112_200d_jerk_v112_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.9617)).rolling(21).var().rolling(48).std().pct_change(5).rolling(33).min() * 0.467375).diff(8).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc112_200d_jerk_v112_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc112_200d_jerk_v112_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc113_63d_jerk_v113_signal(fcf, sharesbas):
    res = ((fcf * 6.5159 - sharesbas).rolling(15).std().rolling(14).min() * 0.892047).diff(13).diff(3).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc113_63d_jerk_v113_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc113_63d_jerk_v113_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc114_42d_jerk_v114_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.3163)).rolling(33).min().rolling(23).var() * 0.646120).diff(15).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc114_42d_jerk_v114_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc114_42d_jerk_v114_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc115_84d_jerk_v115_signal(fcf, sharesbas):
    res = ((fcf * 8.2205 - sharesbas).rolling(12).mean().pct_change(18).rolling(4).max().rolling(36).mean() * 0.933166).diff(11).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc115_84d_jerk_v115_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc115_84d_jerk_v115_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc116_200d_jerk_v116_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(4) + 1.6258)).rolling(2).max().pct_change(22) * 0.876401).diff(12).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc116_200d_jerk_v116_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc116_200d_jerk_v116_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc117_105d_jerk_v117_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(19).var().rolling(27).min() * 0.432402).diff(9).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc117_105d_jerk_v117_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc117_105d_jerk_v117_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc118_63d_jerk_v118_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 5.4593)).rolling(7).var().rolling(42).var().diff(43).diff(2) * 0.154940).diff(12).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc118_63d_jerk_v118_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc118_63d_jerk_v118_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc119_252d_jerk_v119_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 0.1570)).rolling(13).mean().diff(36) * 0.335698).diff(7).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc119_252d_jerk_v119_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc119_252d_jerk_v119_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc120_150d_jerk_v120_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 6.2603)).rolling(32).max().rolling(5).std().rolling(29).var().rolling(6).min() * 0.356719).diff(15).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc120_150d_jerk_v120_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc120_150d_jerk_v120_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc121_126d_jerk_v121_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.0500)).pct_change(42).pct_change(9).rolling(22).std().rolling(40).max() * 0.338031).diff(2).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc121_126d_jerk_v121_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc121_126d_jerk_v121_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc122_252d_jerk_v122_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.6001)).rolling(45).mean().rolling(25).min().rolling(45).var() * 0.873640).diff(19).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc122_252d_jerk_v122_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc122_252d_jerk_v122_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc123_150d_jerk_v123_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(39).std().rolling(50).min().pct_change(2).rolling(33).min() * 0.429334).diff(5).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc123_150d_jerk_v123_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc123_150d_jerk_v123_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc124_150d_jerk_v124_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 3.1150)).pct_change(48).diff(15).rolling(20).mean().rolling(2).std() * 0.712830).diff(8).diff(2).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc124_150d_jerk_v124_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc124_150d_jerk_v124_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc125_10d_jerk_v125_signal(fcf, sharesbas):
    res = ((fcf * 6.3158 - sharesbas).diff(48).pct_change(3) * 0.756130).diff(20).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc125_10d_jerk_v125_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc125_10d_jerk_v125_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc126_126d_jerk_v126_signal(fcf, sharesbas):
    res = ((fcf * 0.3970 - sharesbas).rolling(35).var().rolling(30).var() * 0.444403).diff(15).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc126_126d_jerk_v126_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc126_126d_jerk_v126_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc127_84d_jerk_v127_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.8074)).pct_change(45).rolling(4).min() * 0.701512).diff(16).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc127_84d_jerk_v127_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc127_84d_jerk_v127_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc128_84d_jerk_v128_signal(fcf, sharesbas):
    res = ((fcf * 9.0766 - sharesbas).rolling(34).min().diff(29).rolling(26).var() * 0.291481).diff(13).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc128_84d_jerk_v128_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc128_84d_jerk_v128_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc129_42d_jerk_v129_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.9722)).rolling(9).min().rolling(4).std().diff(43).rolling(39).var() * 0.941164).diff(5).diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc129_42d_jerk_v129_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc129_42d_jerk_v129_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc130_63d_jerk_v130_signal(fcf, sharesbas):
    res = ((fcf * 6.9263 - sharesbas).diff(9).pct_change(11) * 0.479520).diff(9).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc130_63d_jerk_v130_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc130_63d_jerk_v130_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_jerk_v131_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.1335)).rolling(18).max().rolling(38).var().diff(47) * 0.910495).diff(15).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_jerk_v131_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_jerk_v131_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc132_84d_jerk_v132_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 5.3780)).rolling(15).var().rolling(23).max().diff(50) * 0.125879).diff(10).diff(10).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc132_84d_jerk_v132_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc132_84d_jerk_v132_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc133_200d_jerk_v133_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 3.5777)).diff(12).rolling(33).std().rolling(49).mean() * 0.357194).diff(20).diff(18).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc133_200d_jerk_v133_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc133_200d_jerk_v133_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc134_84d_jerk_v134_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(19).max().pct_change(49).diff(36).rolling(34).max() * 0.705666).diff(15).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc134_84d_jerk_v134_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc134_84d_jerk_v134_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc135_150d_jerk_v135_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(3) + 6.8591)).rolling(3).var().rolling(47).var().rolling(20).max() * 0.777488).diff(14).diff(4).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc135_150d_jerk_v135_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc135_150d_jerk_v135_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc136_105d_jerk_v136_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.6424)).rolling(8).mean().rolling(36).var().rolling(48).mean().rolling(24).min() * 0.462339).diff(2).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc136_105d_jerk_v136_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc136_105d_jerk_v136_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc137_42d_jerk_v137_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(13).pct_change(45).rolling(23).std().rolling(29).max() * 0.518300).diff(5).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc137_42d_jerk_v137_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc137_42d_jerk_v137_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc138_84d_jerk_v138_signal(fcf, sharesbas):
    res = ((fcf.diff(7) / (sharesbas.shift(4) + 7.1266)).pct_change(39).diff(48) * 0.863301).diff(15).diff(8).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc138_84d_jerk_v138_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc138_84d_jerk_v138_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc139_63d_jerk_v139_signal(fcf, sharesbas):
    res = ((fcf.diff(9) / (sharesbas.shift(3) + 0.2591)).rolling(12).min().rolling(37).min() * 0.498378).diff(16).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc139_63d_jerk_v139_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc139_63d_jerk_v139_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc140_63d_jerk_v140_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.8423)).rolling(8).std().rolling(30).min() * 0.029547).diff(3).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc140_63d_jerk_v140_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc140_63d_jerk_v140_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc141_200d_jerk_v141_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(19).rolling(21).mean().rolling(36).min() * 0.570630).diff(11).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc141_200d_jerk_v141_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc141_200d_jerk_v141_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc142_5d_jerk_v142_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.0701)).rolling(30).min().rolling(22).mean() * 0.921823).diff(18).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc142_5d_jerk_v142_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc142_5d_jerk_v142_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc143_105d_jerk_v143_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(8).max().diff(13) * 0.262240).diff(17).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc143_105d_jerk_v143_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc143_105d_jerk_v143_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc144_150d_jerk_v144_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(1) + 6.6370)).diff(49).rolling(14).var().rolling(42).std() * 0.070990).diff(2).diff(2).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc144_150d_jerk_v144_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc144_150d_jerk_v144_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc145_63d_jerk_v145_signal(fcf, sharesbas):
    res = ((fcf * 2.0878 - sharesbas).rolling(47).std().rolling(50).min() * 0.599784).diff(14).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc145_63d_jerk_v145_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc145_63d_jerk_v145_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc146_252d_jerk_v146_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.0169)).rolling(10).var().diff(33).rolling(9).min().rolling(36).std() * 0.400801).diff(7).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc146_252d_jerk_v146_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc146_252d_jerk_v146_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc147_63d_jerk_v147_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(4) + 7.7984)).rolling(12).std().rolling(26).min().rolling(40).min() * 0.755969).diff(4).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc147_63d_jerk_v147_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc147_63d_jerk_v147_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc148_21d_jerk_v148_signal(fcf, sharesbas):
    res = ((fcf * 8.3851 - sharesbas).pct_change(26).rolling(33).mean().diff(13).rolling(13).var() * 0.695344).diff(20).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc148_21d_jerk_v148_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc148_21d_jerk_v148_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc149_42d_jerk_v149_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(2) + 8.4563)).pct_change(37).rolling(26).var() * 0.194464).diff(12).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc149_42d_jerk_v149_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc149_42d_jerk_v149_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc150_21d_jerk_v150_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(6).max().rolling(3).std().rolling(28).var().rolling(24).std() * 0.989596).diff(8).diff(6).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc150_21d_jerk_v150_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc150_21d_jerk_v150_signal


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
