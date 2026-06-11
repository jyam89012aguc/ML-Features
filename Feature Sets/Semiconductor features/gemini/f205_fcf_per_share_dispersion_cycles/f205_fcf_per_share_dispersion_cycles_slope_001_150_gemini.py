import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f205f_f205_fcf_per_share_dispersion_cycles_calc001_126d_slope_v001_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 4.0815)).rolling(20).min().rolling(19).max().rolling(17).mean() * 0.659647).diff(12).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc001_126d_slope_v001_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc001_126d_slope_v001_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc002_21d_slope_v002_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(3) + 3.6033)).rolling(2).std().rolling(50).var().diff(47).pct_change(45) * 0.392169).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc002_21d_slope_v002_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc002_21d_slope_v002_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc003_63d_slope_v003_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(7).rolling(36).min().pct_change(7) * 0.445143).diff(6).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc003_63d_slope_v003_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc003_63d_slope_v003_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc004_42d_slope_v004_signal(fcf, sharesbas):
    res = ((fcf * 5.4652 - sharesbas).rolling(8).min().pct_change(21).pct_change(20) * 0.236059).diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc004_42d_slope_v004_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc004_42d_slope_v004_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc005_252d_slope_v005_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 3.9096)).rolling(21).mean().rolling(34).max().rolling(37).max().rolling(8).max() * 0.520199).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc005_252d_slope_v005_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc005_252d_slope_v005_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc006_105d_slope_v006_signal(fcf, sharesbas):
    res = ((fcf * 0.9038 - sharesbas).rolling(16).min().rolling(39).mean().rolling(23).var().pct_change(24) * 0.869332).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc006_105d_slope_v006_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc006_105d_slope_v006_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc007_42d_slope_v007_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).diff(15).diff(39) * 0.039806).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc007_42d_slope_v007_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc007_42d_slope_v007_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc008_150d_slope_v008_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.3667)).rolling(25).max().rolling(35).max().rolling(30).mean().rolling(16).std() * 0.235150).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc008_150d_slope_v008_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc008_150d_slope_v008_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc009_21d_slope_v009_signal(fcf, sharesbas):
    res = ((fcf.diff(4) / (sharesbas.shift(2) + 4.7726)).pct_change(27).rolling(38).mean().rolling(8).max().rolling(11).max() * 0.955172).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc009_21d_slope_v009_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc009_21d_slope_v009_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc010_105d_slope_v010_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.8131)).diff(9).pct_change(15).rolling(34).std() * 0.296217).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc010_105d_slope_v010_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc010_105d_slope_v010_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc011_5d_slope_v011_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(48).std().rolling(47).mean().rolling(42).min().rolling(34).min() * 0.020567).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc011_5d_slope_v011_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc011_5d_slope_v011_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc012_150d_slope_v012_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(8).var().rolling(41).var().rolling(9).max().pct_change(13) * 0.270097).diff(8).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc012_150d_slope_v012_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc012_150d_slope_v012_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc013_150d_slope_v013_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(5) + 9.3722)).rolling(14).std().rolling(45).min().rolling(22).std() * 0.926755).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc013_150d_slope_v013_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc013_150d_slope_v013_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc014_252d_slope_v014_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(2) + 9.3696)).rolling(16).mean().pct_change(23).rolling(28).std().rolling(2).mean() * 0.606514).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc014_252d_slope_v014_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc014_252d_slope_v014_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc015_5d_slope_v015_signal(fcf, sharesbas):
    res = ((fcf * 5.4102 - sharesbas).rolling(31).std().rolling(45).mean().rolling(18).max() * 0.369229).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc015_5d_slope_v015_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc015_5d_slope_v015_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc016_63d_slope_v016_signal(fcf, sharesbas):
    res = ((fcf * 0.5579 - sharesbas).rolling(13).std().rolling(12).std().rolling(29).std().rolling(2).min() * 0.491414).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc016_63d_slope_v016_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc016_63d_slope_v016_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc017_21d_slope_v017_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 0.3393)).rolling(4).var().rolling(15).mean().rolling(22).var() * 0.925248).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc017_21d_slope_v017_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc017_21d_slope_v017_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc018_252d_slope_v018_signal(fcf, sharesbas):
    res = ((fcf.diff(4) / (sharesbas.shift(5) + 8.1157)).rolling(34).min().rolling(28).min().rolling(25).std().pct_change(10) * 0.040737).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc018_252d_slope_v018_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc018_252d_slope_v018_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc019_200d_slope_v019_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(40).var().diff(9).diff(19).rolling(19).mean() * 0.922994).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc019_200d_slope_v019_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc019_200d_slope_v019_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc020_63d_slope_v020_signal(fcf, sharesbas):
    res = ((fcf * 5.0822 - sharesbas).rolling(20).mean().rolling(39).var().rolling(21).min().diff(2) * 0.775383).diff(14).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc020_63d_slope_v020_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc020_63d_slope_v020_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc021_150d_slope_v021_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.5210)).rolling(34).mean().rolling(10).var().rolling(50).mean().pct_change(47) * 0.159464).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc021_150d_slope_v021_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc021_150d_slope_v021_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc022_252d_slope_v022_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(47).mean().diff(2) * 0.423975).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc022_252d_slope_v022_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc022_252d_slope_v022_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc023_200d_slope_v023_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.2839)).rolling(23).std().rolling(3).std().rolling(12).max() * 0.106770).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc023_200d_slope_v023_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc023_200d_slope_v023_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc024_63d_slope_v024_signal(fcf, sharesbas):
    res = ((fcf * 0.7936 - sharesbas).rolling(46).std().rolling(14).min().rolling(33).min() * 0.238974).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc024_63d_slope_v024_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc024_63d_slope_v024_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc025_21d_slope_v025_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 5.4869)).rolling(40).max().pct_change(42).rolling(27).var() * 0.782037).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc025_21d_slope_v025_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc025_21d_slope_v025_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc026_21d_slope_v026_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.6728)).rolling(5).std().diff(23).rolling(22).mean() * 0.641647).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc026_21d_slope_v026_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc026_21d_slope_v026_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc027_42d_slope_v027_signal(fcf, sharesbas):
    res = ((fcf.diff(7) / (sharesbas.shift(1) + 9.7924)).rolling(5).max().rolling(21).max() * 0.264942).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc027_42d_slope_v027_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc027_42d_slope_v027_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc028_5d_slope_v028_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 3.3751)).rolling(11).min().rolling(42).mean().rolling(22).max().pct_change(36) * 0.448121).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc028_5d_slope_v028_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc028_5d_slope_v028_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc029_126d_slope_v029_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 6.4066)).rolling(4).max().rolling(12).std().pct_change(26).rolling(29).var() * 0.378184).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc029_126d_slope_v029_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc029_126d_slope_v029_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc030_150d_slope_v030_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 7.6390)).rolling(21).mean().rolling(17).max().rolling(20).std().rolling(20).max() * 0.641234).diff(7).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc030_150d_slope_v030_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc030_150d_slope_v030_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc031_105d_slope_v031_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.9702)).pct_change(38).rolling(30).min().rolling(17).var().diff(49) * 0.305855).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc031_105d_slope_v031_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc031_105d_slope_v031_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc032_10d_slope_v032_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 3.3735)).rolling(29).std().rolling(14).max().rolling(10).std().rolling(2).std() * 0.903972).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc032_10d_slope_v032_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc032_10d_slope_v032_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc033_21d_slope_v033_signal(fcf, sharesbas):
    res = ((fcf * 2.6629 - sharesbas).rolling(13).std().rolling(31).max().rolling(35).max() * 0.146627).diff(9).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc033_21d_slope_v033_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc033_21d_slope_v033_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc034_5d_slope_v034_signal(fcf, sharesbas):
    res = ((fcf * 3.2227 - sharesbas).rolling(9).min().pct_change(46).rolling(28).mean() * 0.728902).diff(16).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc034_5d_slope_v034_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc034_5d_slope_v034_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc035_63d_slope_v035_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(32).min().rolling(49).var().rolling(50).var() * 0.527167).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc035_63d_slope_v035_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc035_63d_slope_v035_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc036_126d_slope_v036_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(3) + 8.4617)).rolling(28).std().rolling(44).min().rolling(25).std() * 0.014599).diff(12).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc036_126d_slope_v036_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc036_126d_slope_v036_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc037_10d_slope_v037_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(9).mean().rolling(46).var() * 0.821431).diff(20).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc037_10d_slope_v037_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc037_10d_slope_v037_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc038_84d_slope_v038_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 7.5219)).rolling(36).var().rolling(50).min().diff(21).rolling(9).min() * 0.548988).diff(12).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc038_84d_slope_v038_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc038_84d_slope_v038_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc039_63d_slope_v039_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(2) + 8.4581)).rolling(6).var().rolling(16).var().rolling(35).min().rolling(45).min() * 0.469811).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc039_63d_slope_v039_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc039_63d_slope_v039_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc040_42d_slope_v040_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 6.0459)).diff(44).rolling(10).max() * 0.767889).diff(12).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc040_42d_slope_v040_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc040_42d_slope_v040_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc041_63d_slope_v041_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(30).rolling(47).min().rolling(48).std() * 0.034625).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc041_63d_slope_v041_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc041_63d_slope_v041_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc042_42d_slope_v042_signal(fcf, sharesbas):
    res = ((fcf * 7.0636 - sharesbas).rolling(5).std().pct_change(43).rolling(21).std().rolling(45).max() * 0.443864).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc042_42d_slope_v042_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc042_42d_slope_v042_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc043_5d_slope_v043_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.1690)).rolling(35).max().rolling(37).min().rolling(5).std().rolling(47).max() * 0.854281).diff(20).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc043_5d_slope_v043_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc043_5d_slope_v043_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc044_84d_slope_v044_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 0.1995)).rolling(47).max().rolling(8).mean().rolling(7).std() * 0.925135).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc044_84d_slope_v044_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc044_84d_slope_v044_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc045_21d_slope_v045_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(5) + 7.8409)).pct_change(27).rolling(36).mean().pct_change(29) * 0.920800).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc045_21d_slope_v045_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc045_21d_slope_v045_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc046_5d_slope_v046_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(30).std().pct_change(31).rolling(45).max().rolling(14).max() * 0.614627).diff(10).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc046_5d_slope_v046_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc046_5d_slope_v046_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc047_10d_slope_v047_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.9141)).rolling(31).std().rolling(48).max() * 0.737019).diff(5).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc047_10d_slope_v047_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc047_10d_slope_v047_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc048_42d_slope_v048_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(3) + 8.5084)).rolling(42).max().rolling(21).std().rolling(4).std() * 0.652908).diff(3).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc048_42d_slope_v048_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc048_42d_slope_v048_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc049_126d_slope_v049_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.3803)).diff(17).rolling(6).max() * 0.101384).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc049_126d_slope_v049_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc049_126d_slope_v049_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc050_5d_slope_v050_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(1) + 1.9480)).rolling(42).min().diff(30).pct_change(49).rolling(16).mean() * 0.611398).diff(10).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc050_5d_slope_v050_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc050_5d_slope_v050_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc051_252d_slope_v051_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 6.4405)).rolling(43).std().rolling(26).mean().rolling(10).var() * 0.673672).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc051_252d_slope_v051_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc051_252d_slope_v051_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc052_126d_slope_v052_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 3.1438)).rolling(49).mean().rolling(23).std() * 0.883720).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc052_126d_slope_v052_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc052_126d_slope_v052_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc053_150d_slope_v053_signal(fcf, sharesbas):
    res = ((fcf * 7.6860 - sharesbas).rolling(13).min().pct_change(34) * 0.036914).diff(3).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc053_150d_slope_v053_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc053_150d_slope_v053_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc054_200d_slope_v054_signal(fcf, sharesbas):
    res = ((fcf * 5.0012 - sharesbas).rolling(33).var().rolling(24).var() * 0.463841).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc054_200d_slope_v054_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc054_200d_slope_v054_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc055_42d_slope_v055_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.6853)).rolling(40).std().rolling(21).min().rolling(42).mean() * 0.606676).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc055_42d_slope_v055_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc055_42d_slope_v055_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc056_200d_slope_v056_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(1) + 4.0607)).pct_change(39).rolling(49).min() * 0.133027).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc056_200d_slope_v056_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc056_200d_slope_v056_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc057_105d_slope_v057_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.7784)).rolling(4).var().rolling(41).min().diff(18) * 0.790377).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc057_105d_slope_v057_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc057_105d_slope_v057_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc058_252d_slope_v058_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(44).std().rolling(6).max().rolling(7).std() * 0.320545).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc058_252d_slope_v058_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc058_252d_slope_v058_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc059_105d_slope_v059_signal(fcf, sharesbas):
    res = ((fcf.diff(9) / (sharesbas.shift(1) + 6.0098)).rolling(3).mean().rolling(34).std().rolling(35).var().diff(21) * 0.477737).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc059_105d_slope_v059_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc059_105d_slope_v059_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc060_126d_slope_v060_signal(fcf, sharesbas):
    res = ((fcf * 1.1177 - sharesbas).pct_change(2).pct_change(27).rolling(30).std().rolling(44).min() * 0.512815).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc060_126d_slope_v060_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc060_126d_slope_v060_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc061_200d_slope_v061_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 6.4458)).rolling(48).mean().rolling(43).min() * 0.743307).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc061_200d_slope_v061_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc061_200d_slope_v061_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc062_63d_slope_v062_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.8633)).rolling(6).min().rolling(2).mean() * 0.635268).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc062_63d_slope_v062_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc062_63d_slope_v062_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc063_252d_slope_v063_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 5.9870)).rolling(18).var().rolling(13).min().rolling(40).mean().rolling(47).max() * 0.224985).diff(18).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc063_252d_slope_v063_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc063_252d_slope_v063_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc064_10d_slope_v064_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.0798)).rolling(31).std().rolling(37).min().rolling(42).var() * 0.195521).diff(8).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc064_10d_slope_v064_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc064_10d_slope_v064_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc065_105d_slope_v065_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.3639)).diff(9).rolling(19).min().rolling(8).mean().pct_change(44) * 0.948368).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc065_105d_slope_v065_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc065_105d_slope_v065_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc066_126d_slope_v066_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 4.5289)).rolling(47).var().rolling(25).std().rolling(27).mean() * 0.819812).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc066_126d_slope_v066_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc066_126d_slope_v066_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc067_105d_slope_v067_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(25).mean().rolling(3).std().rolling(28).var() * 0.825656).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc067_105d_slope_v067_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc067_105d_slope_v067_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc068_5d_slope_v068_signal(fcf, sharesbas):
    res = ((fcf * 9.5576 - sharesbas).diff(23).rolling(22).max().rolling(3).var().rolling(4).std() * 0.882725).diff(2).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc068_5d_slope_v068_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc068_5d_slope_v068_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc069_200d_slope_v069_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.1123)).rolling(46).min().pct_change(4) * 0.101554).diff(17).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc069_200d_slope_v069_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc069_200d_slope_v069_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc070_10d_slope_v070_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(5) + 9.7056)).pct_change(45).rolling(24).max().rolling(12).std().rolling(44).std() * 0.284438).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc070_10d_slope_v070_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc070_10d_slope_v070_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc071_63d_slope_v071_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.3507)).rolling(18).min().pct_change(33) * 0.030698).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc071_63d_slope_v071_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc071_63d_slope_v071_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc072_63d_slope_v072_signal(fcf, sharesbas):
    res = ((fcf.diff(7) / (sharesbas.shift(1) + 6.5211)).rolling(41).var().rolling(9).max().rolling(35).max() * 0.486132).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc072_63d_slope_v072_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc072_63d_slope_v072_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc073_84d_slope_v073_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 6.4376)).rolling(8).std().rolling(11).min() * 0.244813).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc073_84d_slope_v073_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc073_84d_slope_v073_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc074_105d_slope_v074_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(5) + 3.2540)).rolling(17).std().rolling(38).mean() * 0.635028).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc074_105d_slope_v074_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc074_105d_slope_v074_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc075_21d_slope_v075_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(5) + 3.7924)).rolling(2).std().rolling(24).max() * 0.939187).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc075_21d_slope_v075_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc075_21d_slope_v075_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc076_63d_slope_v076_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(8).mean().rolling(20).var() * 0.868670).diff(7).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc076_63d_slope_v076_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc076_63d_slope_v076_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc077_84d_slope_v077_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 5.1130)).rolling(36).var().rolling(41).min() * 0.880547).diff(3).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc077_84d_slope_v077_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc077_84d_slope_v077_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc078_10d_slope_v078_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(2) + 2.1575)).rolling(43).std().rolling(7).mean() * 0.797897).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc078_10d_slope_v078_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc078_10d_slope_v078_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc079_10d_slope_v079_signal(fcf, sharesbas):
    res = ((fcf * 1.8837 - sharesbas).rolling(39).max().diff(42).rolling(7).var().rolling(14).max() * 0.220621).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc079_10d_slope_v079_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc079_10d_slope_v079_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc080_5d_slope_v080_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 9.6340)).rolling(18).var().diff(41) * 0.565401).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc080_5d_slope_v080_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc080_5d_slope_v080_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc081_10d_slope_v081_signal(fcf, sharesbas):
    res = ((fcf.diff(9) / (sharesbas.shift(3) + 3.6277)).rolling(7).min().diff(7) * 0.598269).diff(6).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc081_10d_slope_v081_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc081_10d_slope_v081_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc082_21d_slope_v082_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(2) + 4.0310)).rolling(50).max().rolling(49).max().rolling(5).var().rolling(49).var() * 0.591806).diff(20).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc082_21d_slope_v082_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc082_21d_slope_v082_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc083_21d_slope_v083_signal(fcf, sharesbas):
    res = ((fcf.diff(9) / (sharesbas.shift(4) + 8.6885)).pct_change(8).diff(12).rolling(28).max().diff(31) * 0.809530).diff(11).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc083_21d_slope_v083_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc083_21d_slope_v083_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc084_126d_slope_v084_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(42).min().rolling(49).min().rolling(39).var().rolling(36).std() * 0.809103).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc084_126d_slope_v084_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc084_126d_slope_v084_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc085_252d_slope_v085_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.7677)).pct_change(37).diff(25).rolling(44).mean().rolling(42).min() * 0.921350).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc085_252d_slope_v085_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc085_252d_slope_v085_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc086_21d_slope_v086_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 0.4197)).rolling(11).min().rolling(8).mean().rolling(35).std() * 0.353014).diff(17).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc086_21d_slope_v086_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc086_21d_slope_v086_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc087_5d_slope_v087_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.0837)).pct_change(11).pct_change(10).diff(36) * 0.571560).diff(9).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc087_5d_slope_v087_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc087_5d_slope_v087_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc088_252d_slope_v088_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(2) + 6.3128)).diff(15).rolling(45).min().rolling(49).var().rolling(5).max() * 0.404312).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc088_252d_slope_v088_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc088_252d_slope_v088_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc089_105d_slope_v089_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(2).max().rolling(13).std().rolling(19).mean() * 0.680614).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc089_105d_slope_v089_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc089_105d_slope_v089_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc090_105d_slope_v090_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.9985)).pct_change(5).diff(43) * 0.729175).diff(7).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc090_105d_slope_v090_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc090_105d_slope_v090_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc091_10d_slope_v091_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(2) + 8.8300)).rolling(20).max().diff(24).rolling(16).var() * 0.739113).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc091_10d_slope_v091_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc091_10d_slope_v091_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc092_200d_slope_v092_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.8422)).pct_change(3).rolling(29).max().rolling(37).var() * 0.088704).diff(2).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc092_200d_slope_v092_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc092_200d_slope_v092_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc093_105d_slope_v093_signal(fcf, sharesbas):
    res = ((fcf.diff(5) / (sharesbas.shift(3) + 8.0397)).diff(39).rolling(2).std().pct_change(41).pct_change(43) * 0.474493).diff(3).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc093_105d_slope_v093_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc093_105d_slope_v093_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc094_21d_slope_v094_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.5459)).rolling(18).var().rolling(10).std().rolling(29).max().rolling(11).var() * 0.593540).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc094_21d_slope_v094_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc094_21d_slope_v094_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc095_5d_slope_v095_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(28).mean().rolling(38).max() * 0.085085).diff(2).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc095_5d_slope_v095_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc095_5d_slope_v095_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc096_200d_slope_v096_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.4754)).rolling(37).mean().diff(24).rolling(29).mean() * 0.618299).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc096_200d_slope_v096_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc096_200d_slope_v096_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc097_10d_slope_v097_signal(fcf, sharesbas):
    res = ((fcf * 6.8799 - sharesbas).rolling(37).mean().rolling(48).std() * 0.893796).diff(13).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc097_10d_slope_v097_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc097_10d_slope_v097_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc098_105d_slope_v098_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(5) + 4.4212)).rolling(39).max().rolling(37).var().pct_change(46).rolling(41).min() * 0.942102).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc098_105d_slope_v098_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc098_105d_slope_v098_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc099_5d_slope_v099_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(5) + 6.6661)).pct_change(31).rolling(28).max().pct_change(16).pct_change(15) * 0.072934).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc099_5d_slope_v099_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc099_5d_slope_v099_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc100_150d_slope_v100_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 9.4166)).rolling(33).mean().rolling(17).mean().rolling(14).max().rolling(29).var() * 0.551364).diff(13).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc100_150d_slope_v100_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc100_150d_slope_v100_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc101_252d_slope_v101_signal(fcf, sharesbas):
    res = ((fcf * 3.2962 - sharesbas).diff(14).rolling(12).std() * 0.354930).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc101_252d_slope_v101_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc101_252d_slope_v101_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc102_21d_slope_v102_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.5909)).rolling(29).var().rolling(32).mean().rolling(33).min() * 0.878227).diff(15).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc102_21d_slope_v102_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc102_21d_slope_v102_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc103_105d_slope_v103_signal(fcf, sharesbas):
    res = ((fcf.diff(10) / (sharesbas.shift(2) + 8.9619)).rolling(35).std().pct_change(28).rolling(46).max() * 0.316561).diff(14).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc103_105d_slope_v103_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc103_105d_slope_v103_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc104_126d_slope_v104_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.8427)).rolling(44).max().rolling(32).mean().rolling(49).std().rolling(23).max() * 0.213320).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc104_126d_slope_v104_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc104_126d_slope_v104_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc105_10d_slope_v105_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(15).std().rolling(15).min() * 0.652171).diff(11).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc105_10d_slope_v105_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc105_10d_slope_v105_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc106_10d_slope_v106_signal(fcf, sharesbas):
    res = ((fcf * 7.9229 - sharesbas).rolling(10).min().rolling(38).mean().diff(23) * 0.179206).diff(14).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc106_10d_slope_v106_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc106_10d_slope_v106_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc107_5d_slope_v107_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 4.5213)).rolling(48).var().diff(6).rolling(41).std().pct_change(33) * 0.103537).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc107_5d_slope_v107_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc107_5d_slope_v107_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc108_42d_slope_v108_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 5.2968)).rolling(33).var().rolling(2).max() * 0.430644).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc108_42d_slope_v108_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc108_42d_slope_v108_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc109_63d_slope_v109_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(23).diff(28) * 0.481631).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc109_63d_slope_v109_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc109_63d_slope_v109_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc110_21d_slope_v110_signal(fcf, sharesbas):
    res = ((fcf * 8.2460 - sharesbas).rolling(29).var().rolling(41).mean().diff(37).rolling(50).std() * 0.821232).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc110_21d_slope_v110_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc110_21d_slope_v110_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc111_200d_slope_v111_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 6.1250)).diff(11).diff(13).rolling(15).max().rolling(16).mean() * 0.247199).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc111_200d_slope_v111_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc111_200d_slope_v111_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc112_84d_slope_v112_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(23).min().rolling(47).var().rolling(10).mean() * 0.209126).diff(3).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc112_84d_slope_v112_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc112_84d_slope_v112_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc113_84d_slope_v113_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.0008)).rolling(18).var().rolling(40).var().rolling(42).mean().pct_change(7) * 0.289456).diff(14).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc113_84d_slope_v113_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc113_84d_slope_v113_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc114_105d_slope_v114_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(17).min().rolling(2).max().rolling(3).min() * 0.198887).diff(16).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc114_105d_slope_v114_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc114_105d_slope_v114_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc115_63d_slope_v115_signal(fcf, sharesbas):
    res = ((fcf.diff(6) / (sharesbas.shift(2) + 1.1261)).rolling(39).var().rolling(32).min() * 0.305046).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc115_63d_slope_v115_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc115_63d_slope_v115_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc116_10d_slope_v116_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(11).mean().diff(44) * 0.161762).diff(2).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc116_10d_slope_v116_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc116_10d_slope_v116_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc117_21d_slope_v117_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(2) + 3.6711)).rolling(10).min().rolling(13).var().rolling(8).var().rolling(21).std() * 0.660014).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc117_21d_slope_v117_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc117_21d_slope_v117_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc118_84d_slope_v118_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(7).rolling(3).min() * 0.563487).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc118_84d_slope_v118_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc118_84d_slope_v118_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc119_84d_slope_v119_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 8.4995)).rolling(15).max().rolling(46).std().rolling(5).mean() * 0.958827).diff(10).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc119_84d_slope_v119_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc119_84d_slope_v119_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc120_21d_slope_v120_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 2.1985)).rolling(41).min().rolling(35).max().rolling(9).min().rolling(32).var() * 0.239349).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc120_21d_slope_v120_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc120_21d_slope_v120_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc121_10d_slope_v121_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.3254)).rolling(12).mean().diff(39) * 0.026794).diff(8).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc121_10d_slope_v121_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc121_10d_slope_v121_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc122_252d_slope_v122_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 3.2520)).rolling(36).max().rolling(3).max() * 0.903794).diff(7).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc122_252d_slope_v122_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc122_252d_slope_v122_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc123_63d_slope_v123_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.2486)).rolling(23).min().rolling(45).std() * 0.361436).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc123_63d_slope_v123_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc123_63d_slope_v123_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc124_21d_slope_v124_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 0.2574)).pct_change(12).rolling(44).std().rolling(38).min() * 0.012237).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc124_21d_slope_v124_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc124_21d_slope_v124_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc125_42d_slope_v125_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).pct_change(47).pct_change(31).rolling(33).min().rolling(26).max() * 0.214811).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc125_42d_slope_v125_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc125_42d_slope_v125_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc126_252d_slope_v126_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 9.4461)).rolling(45).max().rolling(47).std() * 0.565778).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc126_252d_slope_v126_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc126_252d_slope_v126_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc127_10d_slope_v127_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.1438)).rolling(27).min().diff(24).rolling(50).var().rolling(40).max() * 0.491756).diff(12).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc127_10d_slope_v127_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc127_10d_slope_v127_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc128_5d_slope_v128_signal(fcf, sharesbas):
    res = ((fcf * 2.7026 - sharesbas).rolling(49).min().rolling(36).min() * 0.290084).diff(15).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc128_5d_slope_v128_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc128_5d_slope_v128_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc129_150d_slope_v129_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 8.6788)).rolling(45).var().rolling(30).min().rolling(26).var().rolling(35).mean() * 0.434871).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc129_150d_slope_v129_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc129_150d_slope_v129_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc130_5d_slope_v130_signal(fcf, sharesbas):
    res = ((fcf * 2.4386 - sharesbas).rolling(18).min().diff(43).rolling(13).min().rolling(9).std() * 0.424598).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc130_5d_slope_v130_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc130_5d_slope_v130_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_slope_v131_signal(fcf, sharesbas):
    res = ((fcf.diff(8) / (sharesbas.shift(5) + 5.0290)).rolling(45).min().rolling(50).std() * 0.041992).diff(11).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_slope_v131_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc131_42d_slope_v131_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc132_126d_slope_v132_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(48).std().pct_change(21).rolling(15).mean() * 0.264580).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc132_126d_slope_v132_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc132_126d_slope_v132_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc133_150d_slope_v133_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(22).var().pct_change(44).rolling(34).var() * 0.458410).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc133_150d_slope_v133_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc133_150d_slope_v133_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc134_63d_slope_v134_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 1.0696)).rolling(34).var().rolling(40).min() * 0.288993).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc134_63d_slope_v134_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc134_63d_slope_v134_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc135_63d_slope_v135_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(12).mean().diff(6) * 0.086467).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc135_63d_slope_v135_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc135_63d_slope_v135_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc136_84d_slope_v136_signal(fcf, sharesbas):
    res = ((fcf * 5.4755 - sharesbas).rolling(47).mean().rolling(25).max().rolling(44).mean().rolling(42).var() * 0.592557).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc136_84d_slope_v136_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc136_84d_slope_v136_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc137_150d_slope_v137_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 5.0057)).rolling(14).std().rolling(17).max() * 0.739492).diff(11).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc137_150d_slope_v137_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc137_150d_slope_v137_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc138_84d_slope_v138_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(44).mean().rolling(18).mean() * 0.334762).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc138_84d_slope_v138_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc138_84d_slope_v138_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc139_21d_slope_v139_signal(fcf, sharesbas):
    res = ((fcf.diff(2) / (sharesbas.shift(1) + 8.3467)).rolling(42).min().rolling(11).mean() * 0.329445).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc139_21d_slope_v139_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc139_21d_slope_v139_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc140_126d_slope_v140_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 2.6965)).rolling(40).mean().rolling(26).mean().rolling(50).max() * 0.906436).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc140_126d_slope_v140_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc140_126d_slope_v140_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc141_21d_slope_v141_signal(fcf, sharesbas):
    res = ((fcf * 6.7906 - sharesbas).rolling(24).var().rolling(7).var().rolling(32).var().pct_change(36) * 0.032142).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc141_21d_slope_v141_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc141_21d_slope_v141_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc142_21d_slope_v142_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 7.7211)).rolling(12).min().rolling(13).mean().rolling(21).max() * 0.017155).diff(14).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc142_21d_slope_v142_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc142_21d_slope_v142_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc143_21d_slope_v143_signal(fcf, sharesbas):
    res = ((fcf.diff(3) / (sharesbas.shift(2) + 4.0845)).rolling(47).max().rolling(24).min() * 0.805208).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc143_21d_slope_v143_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc143_21d_slope_v143_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc144_252d_slope_v144_signal(fcf, sharesbas):
    res = ((fcf.replace(0, np.nan) / sharesbas.replace(0, np.nan)).rolling(27).std().pct_change(20).diff(15) * 0.574684).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc144_252d_slope_v144_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc144_252d_slope_v144_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc145_252d_slope_v145_signal(fcf, sharesbas):
    res = ((fcf * 2.6161 - sharesbas).rolling(38).min().rolling(31).max().rolling(8).max().diff(40) * 0.607290).diff(4).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc145_252d_slope_v145_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc145_252d_slope_v145_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc146_252d_slope_v146_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 6.8964)).rolling(37).mean().rolling(8).std().rolling(35).std() * 0.996570).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc146_252d_slope_v146_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc146_252d_slope_v146_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc147_252d_slope_v147_signal(fcf, sharesbas):
    res = ((fcf / (sharesbas + 1.8562)).rolling(48).var().rolling(42).std().rolling(21).mean().rolling(28).min() * 0.955605).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc147_252d_slope_v147_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc147_252d_slope_v147_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc148_63d_slope_v148_signal(fcf, sharesbas):
    res = ((fcf * 7.9405 - sharesbas).pct_change(29).rolling(31).std() * 0.807452).diff(15).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc148_63d_slope_v148_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc148_63d_slope_v148_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc149_5d_slope_v149_signal(fcf, sharesbas):
    res = ((fcf * 5.9804 - sharesbas).rolling(22).mean().pct_change(40).rolling(39).var() * 0.819162).diff(16).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc149_5d_slope_v149_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc149_5d_slope_v149_signal

def f205f_f205_fcf_per_share_dispersion_cycles_calc150_42d_slope_v150_signal(fcf, sharesbas):
    res = ((sharesbas / (fcf + 9.7078)).pct_change(4).rolling(24).max().diff(8).pct_change(27) * 0.305128).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f205f_f205_fcf_per_share_dispersion_cycles_calc150_42d_slope_v150_signal'] = f205f_f205_fcf_per_share_dispersion_cycles_calc150_42d_slope_v150_signal


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
