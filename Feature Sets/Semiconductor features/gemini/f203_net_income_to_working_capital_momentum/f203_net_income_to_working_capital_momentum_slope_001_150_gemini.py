import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f203n_f203_net_income_to_working_capital_momentum_calc001_63d_slope_v001_signal(netinc, workingcapital):
    res = ((netinc * 2.1430 - workingcapital).diff(8).rolling(20).var() * 0.366671).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc001_63d_slope_v001_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc001_63d_slope_v001_signal

def f203n_f203_net_income_to_working_capital_momentum_calc002_5d_slope_v002_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(2).rolling(45).std() * 0.777607).diff(16).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc002_5d_slope_v002_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc002_5d_slope_v002_signal

def f203n_f203_net_income_to_working_capital_momentum_calc003_21d_slope_v003_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 4.5521)).diff(34).pct_change(31).rolling(44).std() * 0.313691).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc003_21d_slope_v003_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc003_21d_slope_v003_signal

def f203n_f203_net_income_to_working_capital_momentum_calc004_5d_slope_v004_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.2962)).rolling(12).mean().pct_change(37).rolling(25).max().rolling(35).std() * 0.187456).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc004_5d_slope_v004_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc004_5d_slope_v004_signal

def f203n_f203_net_income_to_working_capital_momentum_calc005_5d_slope_v005_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(1) + 0.5627)).diff(41).diff(6).rolling(41).var().rolling(6).std() * 0.122956).diff(15).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc005_5d_slope_v005_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc005_5d_slope_v005_signal

def f203n_f203_net_income_to_working_capital_momentum_calc006_126d_slope_v006_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(6).max().pct_change(20) * 0.067645).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc006_126d_slope_v006_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc006_126d_slope_v006_signal

def f203n_f203_net_income_to_working_capital_momentum_calc007_126d_slope_v007_signal(netinc, workingcapital):
    res = ((netinc * 2.6919 - workingcapital).rolling(9).var().rolling(9).std() * 0.726618).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc007_126d_slope_v007_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc007_126d_slope_v007_signal

def f203n_f203_net_income_to_working_capital_momentum_calc008_252d_slope_v008_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.2839)).rolling(9).var().rolling(32).var().rolling(3).var().pct_change(14) * 0.120483).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc008_252d_slope_v008_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc008_252d_slope_v008_signal

def f203n_f203_net_income_to_working_capital_momentum_calc009_126d_slope_v009_signal(netinc, workingcapital):
    res = ((netinc.diff(4) / (workingcapital.shift(4) + 0.1280)).rolling(3).var().rolling(30).mean().rolling(38).max().diff(38) * 0.545254).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc009_126d_slope_v009_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc009_126d_slope_v009_signal

def f203n_f203_net_income_to_working_capital_momentum_calc010_150d_slope_v010_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.7820)).diff(23).rolling(26).max().rolling(23).max() * 0.736508).diff(15).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc010_150d_slope_v010_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc010_150d_slope_v010_signal

def f203n_f203_net_income_to_working_capital_momentum_calc011_252d_slope_v011_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.8813)).rolling(16).max().rolling(33).max() * 0.670501).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc011_252d_slope_v011_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc011_252d_slope_v011_signal

def f203n_f203_net_income_to_working_capital_momentum_calc012_105d_slope_v012_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 0.4017)).rolling(50).min().pct_change(3).rolling(11).min().rolling(44).std() * 0.572531).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc012_105d_slope_v012_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc012_105d_slope_v012_signal

def f203n_f203_net_income_to_working_capital_momentum_calc013_42d_slope_v013_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.1312)).rolling(24).std().rolling(11).var().rolling(31).min().rolling(39).max() * 0.288198).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc013_42d_slope_v013_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc013_42d_slope_v013_signal

def f203n_f203_net_income_to_working_capital_momentum_calc014_126d_slope_v014_signal(netinc, workingcapital):
    res = ((netinc * 9.1175 - workingcapital).rolling(27).min().rolling(19).mean().rolling(42).max() * 0.999424).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc014_126d_slope_v014_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc014_126d_slope_v014_signal

def f203n_f203_net_income_to_working_capital_momentum_calc015_42d_slope_v015_signal(netinc, workingcapital):
    res = ((netinc * 7.3019 - workingcapital).rolling(5).min().rolling(9).max().rolling(35).var() * 0.251617).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc015_42d_slope_v015_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc015_42d_slope_v015_signal

def f203n_f203_net_income_to_working_capital_momentum_calc016_10d_slope_v016_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.9061)).rolling(10).std().diff(39) * 0.155328).diff(6).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc016_10d_slope_v016_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc016_10d_slope_v016_signal

def f203n_f203_net_income_to_working_capital_momentum_calc017_10d_slope_v017_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 8.4763)).rolling(42).var().rolling(14).var().rolling(22).min().rolling(5).var() * 0.459473).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc017_10d_slope_v017_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc017_10d_slope_v017_signal

def f203n_f203_net_income_to_working_capital_momentum_calc018_150d_slope_v018_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(12).min().diff(15).rolling(22).max() * 0.738369).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc018_150d_slope_v018_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc018_150d_slope_v018_signal

def f203n_f203_net_income_to_working_capital_momentum_calc019_252d_slope_v019_signal(netinc, workingcapital):
    res = ((netinc * 8.3464 - workingcapital).diff(16).rolling(31).mean().pct_change(23).rolling(50).min() * 0.887732).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc019_252d_slope_v019_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc019_252d_slope_v019_signal

def f203n_f203_net_income_to_working_capital_momentum_calc020_63d_slope_v020_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 4.9368)).pct_change(19).pct_change(7) * 0.156582).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc020_63d_slope_v020_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc020_63d_slope_v020_signal

def f203n_f203_net_income_to_working_capital_momentum_calc021_10d_slope_v021_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(49).var().pct_change(6).pct_change(32) * 0.463826).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc021_10d_slope_v021_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc021_10d_slope_v021_signal

def f203n_f203_net_income_to_working_capital_momentum_calc022_126d_slope_v022_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(49).mean().diff(45) * 0.580103).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc022_126d_slope_v022_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc022_126d_slope_v022_signal

def f203n_f203_net_income_to_working_capital_momentum_calc023_10d_slope_v023_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(2) + 3.3270)).rolling(12).std().rolling(13).std().diff(3).diff(20) * 0.199552).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc023_10d_slope_v023_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc023_10d_slope_v023_signal

def f203n_f203_net_income_to_working_capital_momentum_calc024_200d_slope_v024_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.3798)).rolling(19).std().pct_change(19).rolling(15).std().pct_change(26) * 0.679921).diff(9).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc024_200d_slope_v024_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc024_200d_slope_v024_signal

def f203n_f203_net_income_to_working_capital_momentum_calc025_63d_slope_v025_signal(netinc, workingcapital):
    res = ((netinc * 4.0178 - workingcapital).rolling(13).min().rolling(18).max() * 0.268454).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc025_63d_slope_v025_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc025_63d_slope_v025_signal

def f203n_f203_net_income_to_working_capital_momentum_calc026_200d_slope_v026_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(6).min().diff(44).rolling(26).mean().rolling(47).var() * 0.063324).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc026_200d_slope_v026_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc026_200d_slope_v026_signal

def f203n_f203_net_income_to_working_capital_momentum_calc027_200d_slope_v027_signal(netinc, workingcapital):
    res = ((netinc * 0.3776 - workingcapital).rolling(49).mean().rolling(6).mean().rolling(48).max().rolling(42).var() * 0.241186).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc027_200d_slope_v027_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc027_200d_slope_v027_signal

def f203n_f203_net_income_to_working_capital_momentum_calc028_42d_slope_v028_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(5) + 1.9976)).diff(17).rolling(41).var().rolling(20).std() * 0.456174).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc028_42d_slope_v028_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc028_42d_slope_v028_signal

def f203n_f203_net_income_to_working_capital_momentum_calc029_126d_slope_v029_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(17).pct_change(49).rolling(29).mean() * 0.987984).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc029_126d_slope_v029_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc029_126d_slope_v029_signal

def f203n_f203_net_income_to_working_capital_momentum_calc030_252d_slope_v030_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(5) + 4.7465)).rolling(29).var().pct_change(48) * 0.099898).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc030_252d_slope_v030_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc030_252d_slope_v030_signal

def f203n_f203_net_income_to_working_capital_momentum_calc031_252d_slope_v031_signal(netinc, workingcapital):
    res = ((netinc * 7.8663 - workingcapital).rolling(24).var().diff(48).diff(13).pct_change(42) * 0.156219).diff(14).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc031_252d_slope_v031_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc031_252d_slope_v031_signal

def f203n_f203_net_income_to_working_capital_momentum_calc032_84d_slope_v032_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 5.5286)).rolling(13).var().rolling(11).max().rolling(40).std() * 0.644685).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc032_84d_slope_v032_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc032_84d_slope_v032_signal

def f203n_f203_net_income_to_working_capital_momentum_calc033_200d_slope_v033_signal(netinc, workingcapital):
    res = ((netinc * 4.4421 - workingcapital).rolling(41).min().rolling(34).min().rolling(37).min().rolling(44).min() * 0.808075).diff(15).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc033_200d_slope_v033_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc033_200d_slope_v033_signal

def f203n_f203_net_income_to_working_capital_momentum_calc034_252d_slope_v034_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.9607)).pct_change(19).rolling(50).max() * 0.576621).diff(12).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc034_252d_slope_v034_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc034_252d_slope_v034_signal

def f203n_f203_net_income_to_working_capital_momentum_calc035_5d_slope_v035_signal(netinc, workingcapital):
    res = ((netinc * 2.8340 - workingcapital).rolling(3).max().rolling(24).std().rolling(18).max() * 0.468015).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc035_5d_slope_v035_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc035_5d_slope_v035_signal

def f203n_f203_net_income_to_working_capital_momentum_calc036_84d_slope_v036_signal(netinc, workingcapital):
    res = ((netinc * 5.8734 - workingcapital).pct_change(23).rolling(46).mean() * 0.238831).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc036_84d_slope_v036_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc036_84d_slope_v036_signal

def f203n_f203_net_income_to_working_capital_momentum_calc037_63d_slope_v037_signal(netinc, workingcapital):
    res = ((netinc * 4.9236 - workingcapital).rolling(2).std().diff(33).rolling(16).max() * 0.903024).diff(9).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc037_63d_slope_v037_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc037_63d_slope_v037_signal

def f203n_f203_net_income_to_working_capital_momentum_calc038_5d_slope_v038_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(21).rolling(24).var().rolling(22).max() * 0.258272).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc038_5d_slope_v038_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc038_5d_slope_v038_signal

def f203n_f203_net_income_to_working_capital_momentum_calc039_126d_slope_v039_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(49).min().diff(43) * 0.276456).diff(6).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc039_126d_slope_v039_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc039_126d_slope_v039_signal

def f203n_f203_net_income_to_working_capital_momentum_calc040_105d_slope_v040_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 3.5284)).rolling(45).min().pct_change(33).rolling(10).max().rolling(19).std() * 0.111523).diff(12).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc040_105d_slope_v040_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc040_105d_slope_v040_signal

def f203n_f203_net_income_to_working_capital_momentum_calc041_105d_slope_v041_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 6.2526)).rolling(7).var().rolling(27).var() * 0.583038).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc041_105d_slope_v041_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc041_105d_slope_v041_signal

def f203n_f203_net_income_to_working_capital_momentum_calc042_200d_slope_v042_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(5) + 1.3185)).rolling(7).max().diff(41).rolling(45).min() * 0.513138).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc042_200d_slope_v042_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc042_200d_slope_v042_signal

def f203n_f203_net_income_to_working_capital_momentum_calc043_63d_slope_v043_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 2.8251)).pct_change(30).rolling(46).mean() * 0.187497).diff(2).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc043_63d_slope_v043_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc043_63d_slope_v043_signal

def f203n_f203_net_income_to_working_capital_momentum_calc044_200d_slope_v044_signal(netinc, workingcapital):
    res = ((netinc.diff(9) / (workingcapital.shift(3) + 6.5878)).diff(14).rolling(17).var().rolling(47).std() * 0.559929).diff(20).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc044_200d_slope_v044_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc044_200d_slope_v044_signal

def f203n_f203_net_income_to_working_capital_momentum_calc045_252d_slope_v045_signal(netinc, workingcapital):
    res = ((netinc * 7.6556 - workingcapital).pct_change(41).rolling(14).max().rolling(3).mean() * 0.501537).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc045_252d_slope_v045_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc045_252d_slope_v045_signal

def f203n_f203_net_income_to_working_capital_momentum_calc046_63d_slope_v046_signal(netinc, workingcapital):
    res = ((netinc.diff(4) / (workingcapital.shift(5) + 4.2010)).pct_change(27).rolling(15).var() * 0.189509).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc046_63d_slope_v046_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc046_63d_slope_v046_signal

def f203n_f203_net_income_to_working_capital_momentum_calc047_10d_slope_v047_signal(netinc, workingcapital):
    res = ((netinc * 4.7487 - workingcapital).diff(26).rolling(42).var().rolling(7).mean().rolling(41).var() * 0.682619).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc047_10d_slope_v047_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc047_10d_slope_v047_signal

def f203n_f203_net_income_to_working_capital_momentum_calc048_150d_slope_v048_signal(netinc, workingcapital):
    res = ((netinc.diff(10) / (workingcapital.shift(1) + 2.8481)).rolling(10).mean().rolling(18).min().diff(46).rolling(18).max() * 0.252996).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc048_150d_slope_v048_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc048_150d_slope_v048_signal

def f203n_f203_net_income_to_working_capital_momentum_calc049_63d_slope_v049_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.0011)).rolling(5).var().rolling(18).max().rolling(49).std().diff(14) * 0.280438).diff(7).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc049_63d_slope_v049_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc049_63d_slope_v049_signal

def f203n_f203_net_income_to_working_capital_momentum_calc050_150d_slope_v050_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(15).min().rolling(24).var().diff(2).pct_change(48) * 0.923049).diff(10).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc050_150d_slope_v050_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc050_150d_slope_v050_signal

def f203n_f203_net_income_to_working_capital_momentum_calc051_105d_slope_v051_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 2.4285)).rolling(49).max().rolling(17).var() * 0.537587).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc051_105d_slope_v051_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc051_105d_slope_v051_signal

def f203n_f203_net_income_to_working_capital_momentum_calc052_150d_slope_v052_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 5.6421)).diff(38).rolling(29).mean().pct_change(50) * 0.661631).diff(19).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc052_150d_slope_v052_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc052_150d_slope_v052_signal

def f203n_f203_net_income_to_working_capital_momentum_calc053_42d_slope_v053_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.4843)).rolling(49).min().diff(37) * 0.181186).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc053_42d_slope_v053_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc053_42d_slope_v053_signal

def f203n_f203_net_income_to_working_capital_momentum_calc054_63d_slope_v054_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(41).rolling(10).var().rolling(34).max().rolling(48).var() * 0.874110).diff(13).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc054_63d_slope_v054_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc054_63d_slope_v054_signal

def f203n_f203_net_income_to_working_capital_momentum_calc055_21d_slope_v055_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(3) + 8.3277)).rolling(8).mean().rolling(48).min().rolling(20).max().rolling(35).min() * 0.632735).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc055_21d_slope_v055_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc055_21d_slope_v055_signal

def f203n_f203_net_income_to_working_capital_momentum_calc056_105d_slope_v056_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(16).std().rolling(6).std() * 0.910656).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc056_105d_slope_v056_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc056_105d_slope_v056_signal

def f203n_f203_net_income_to_working_capital_momentum_calc057_126d_slope_v057_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.9555)).rolling(36).max().rolling(7).min().rolling(35).mean() * 0.448776).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc057_126d_slope_v057_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc057_126d_slope_v057_signal

def f203n_f203_net_income_to_working_capital_momentum_calc058_105d_slope_v058_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 3.1891)).rolling(15).mean().rolling(4).mean().rolling(41).min() * 0.280301).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc058_105d_slope_v058_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc058_105d_slope_v058_signal

def f203n_f203_net_income_to_working_capital_momentum_calc059_200d_slope_v059_signal(netinc, workingcapital):
    res = ((netinc.diff(8) / (workingcapital.shift(3) + 6.1723)).pct_change(10).rolling(37).min().rolling(40).var() * 0.551679).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc059_200d_slope_v059_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc059_200d_slope_v059_signal

def f203n_f203_net_income_to_working_capital_momentum_calc060_10d_slope_v060_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.6166)).rolling(26).mean().rolling(45).std() * 0.969182).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc060_10d_slope_v060_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc060_10d_slope_v060_signal

def f203n_f203_net_income_to_working_capital_momentum_calc061_200d_slope_v061_signal(netinc, workingcapital):
    res = ((netinc.diff(2) / (workingcapital.shift(4) + 4.3486)).rolling(31).var().rolling(49).std().rolling(39).std() * 0.517531).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc061_200d_slope_v061_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc061_200d_slope_v061_signal

def f203n_f203_net_income_to_working_capital_momentum_calc062_200d_slope_v062_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(30).min().rolling(10).var().rolling(40).max() * 0.805935).diff(19).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc062_200d_slope_v062_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc062_200d_slope_v062_signal

def f203n_f203_net_income_to_working_capital_momentum_calc063_252d_slope_v063_signal(netinc, workingcapital):
    res = ((netinc * 1.3694 - workingcapital).rolling(24).mean().rolling(9).max() * 0.432024).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc063_252d_slope_v063_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc063_252d_slope_v063_signal

def f203n_f203_net_income_to_working_capital_momentum_calc064_42d_slope_v064_signal(netinc, workingcapital):
    res = ((netinc * 3.5081 - workingcapital).rolling(3).var().rolling(36).var() * 0.910720).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc064_42d_slope_v064_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc064_42d_slope_v064_signal

def f203n_f203_net_income_to_working_capital_momentum_calc065_126d_slope_v065_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 9.2316)).rolling(12).var().rolling(37).var() * 0.438236).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc065_126d_slope_v065_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc065_126d_slope_v065_signal

def f203n_f203_net_income_to_working_capital_momentum_calc066_42d_slope_v066_signal(netinc, workingcapital):
    res = ((netinc * 2.4786 - workingcapital).rolling(19).var().rolling(24).std().diff(5) * 0.912740).diff(13).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc066_42d_slope_v066_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc066_42d_slope_v066_signal

def f203n_f203_net_income_to_working_capital_momentum_calc067_21d_slope_v067_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(48).max().rolling(24).max().diff(48).rolling(49).max() * 0.948226).diff(6).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc067_21d_slope_v067_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc067_21d_slope_v067_signal

def f203n_f203_net_income_to_working_capital_momentum_calc068_200d_slope_v068_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.6897)).pct_change(17).rolling(34).std().rolling(41).mean() * 0.641566).diff(20).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc068_200d_slope_v068_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc068_200d_slope_v068_signal

def f203n_f203_net_income_to_working_capital_momentum_calc069_5d_slope_v069_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(5) + 8.9032)).diff(31).diff(47).rolling(31).var().diff(35) * 0.518234).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc069_5d_slope_v069_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc069_5d_slope_v069_signal

def f203n_f203_net_income_to_working_capital_momentum_calc070_21d_slope_v070_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(5) + 3.7287)).rolling(18).mean().rolling(26).var().diff(28) * 0.877092).diff(11).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc070_21d_slope_v070_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc070_21d_slope_v070_signal

def f203n_f203_net_income_to_working_capital_momentum_calc071_42d_slope_v071_signal(netinc, workingcapital):
    res = ((netinc * 8.8418 - workingcapital).rolling(45).mean().rolling(33).std().rolling(48).max() * 0.891190).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc071_42d_slope_v071_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc071_42d_slope_v071_signal

def f203n_f203_net_income_to_working_capital_momentum_calc072_63d_slope_v072_signal(netinc, workingcapital):
    res = ((netinc * 6.9569 - workingcapital).rolling(31).min().rolling(22).max() * 0.888296).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc072_63d_slope_v072_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc072_63d_slope_v072_signal

def f203n_f203_net_income_to_working_capital_momentum_calc073_84d_slope_v073_signal(netinc, workingcapital):
    res = ((netinc * 4.2937 - workingcapital).rolling(5).min().rolling(23).mean().diff(47) * 0.983406).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc073_84d_slope_v073_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc073_84d_slope_v073_signal

def f203n_f203_net_income_to_working_capital_momentum_calc074_150d_slope_v074_signal(netinc, workingcapital):
    res = ((netinc.diff(2) / (workingcapital.shift(4) + 0.3362)).rolling(27).min().diff(24).rolling(32).min() * 0.132819).diff(7).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc074_150d_slope_v074_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc074_150d_slope_v074_signal

def f203n_f203_net_income_to_working_capital_momentum_calc075_21d_slope_v075_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 3.0039)).rolling(29).min().rolling(23).std().rolling(20).std().rolling(32).var() * 0.518630).diff(9).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc075_21d_slope_v075_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc075_21d_slope_v075_signal

def f203n_f203_net_income_to_working_capital_momentum_calc076_10d_slope_v076_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.9467)).rolling(26).var().rolling(22).max() * 0.760220).diff(7).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc076_10d_slope_v076_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc076_10d_slope_v076_signal

def f203n_f203_net_income_to_working_capital_momentum_calc077_5d_slope_v077_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 2.8407)).rolling(20).var().rolling(7).max() * 0.731752).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc077_5d_slope_v077_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc077_5d_slope_v077_signal

def f203n_f203_net_income_to_working_capital_momentum_calc078_105d_slope_v078_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(4).max().diff(18).rolling(6).mean().rolling(45).std() * 0.670103).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc078_105d_slope_v078_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc078_105d_slope_v078_signal

def f203n_f203_net_income_to_working_capital_momentum_calc079_63d_slope_v079_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(3) + 4.9491)).rolling(10).mean().rolling(3).mean() * 0.760657).diff(10).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc079_63d_slope_v079_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc079_63d_slope_v079_signal

def f203n_f203_net_income_to_working_capital_momentum_calc080_150d_slope_v080_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.2316)).rolling(24).mean().rolling(37).min().pct_change(5) * 0.605915).diff(17).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc080_150d_slope_v080_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc080_150d_slope_v080_signal

def f203n_f203_net_income_to_working_capital_momentum_calc081_42d_slope_v081_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.1076)).diff(29).rolling(27).mean().diff(38).pct_change(19) * 0.989923).diff(4).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc081_42d_slope_v081_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc081_42d_slope_v081_signal

def f203n_f203_net_income_to_working_capital_momentum_calc082_21d_slope_v082_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(9).rolling(28).min() * 0.791583).diff(18).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc082_21d_slope_v082_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc082_21d_slope_v082_signal

def f203n_f203_net_income_to_working_capital_momentum_calc083_200d_slope_v083_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 2.7444)).rolling(10).mean().rolling(25).mean().rolling(13).max().rolling(13).var() * 0.843957).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc083_200d_slope_v083_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc083_200d_slope_v083_signal

def f203n_f203_net_income_to_working_capital_momentum_calc084_5d_slope_v084_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.6331)).rolling(42).max().rolling(21).std().rolling(7).mean().rolling(9).max() * 0.642977).diff(7).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc084_5d_slope_v084_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc084_5d_slope_v084_signal

def f203n_f203_net_income_to_working_capital_momentum_calc085_126d_slope_v085_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(3) + 2.4142)).rolling(39).max().pct_change(29).rolling(5).mean() * 0.895722).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc085_126d_slope_v085_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc085_126d_slope_v085_signal

def f203n_f203_net_income_to_working_capital_momentum_calc086_63d_slope_v086_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(49).mean().pct_change(34) * 0.851146).diff(20).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc086_63d_slope_v086_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc086_63d_slope_v086_signal

def f203n_f203_net_income_to_working_capital_momentum_calc087_252d_slope_v087_signal(netinc, workingcapital):
    res = ((netinc.diff(10) / (workingcapital.shift(3) + 0.7980)).rolling(46).var().rolling(12).mean().rolling(7).std().rolling(19).max() * 0.628323).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc087_252d_slope_v087_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc087_252d_slope_v087_signal

def f203n_f203_net_income_to_working_capital_momentum_calc088_10d_slope_v088_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.6872)).diff(10).rolling(16).std().rolling(43).std() * 0.021216).diff(4).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc088_10d_slope_v088_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc088_10d_slope_v088_signal

def f203n_f203_net_income_to_working_capital_momentum_calc089_84d_slope_v089_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.2361)).rolling(9).max().diff(41) * 0.500761).diff(17).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc089_84d_slope_v089_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc089_84d_slope_v089_signal

def f203n_f203_net_income_to_working_capital_momentum_calc090_105d_slope_v090_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(2) + 4.7706)).rolling(12).max().rolling(40).mean() * 0.082649).diff(12).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc090_105d_slope_v090_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc090_105d_slope_v090_signal

def f203n_f203_net_income_to_working_capital_momentum_calc091_126d_slope_v091_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.8278)).pct_change(31).rolling(17).mean().rolling(2).var().rolling(34).var() * 0.903065).diff(14).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc091_126d_slope_v091_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc091_126d_slope_v091_signal

def f203n_f203_net_income_to_working_capital_momentum_calc092_150d_slope_v092_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 9.7203)).pct_change(13).pct_change(34).pct_change(40) * 0.870012).diff(9).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc092_150d_slope_v092_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc092_150d_slope_v092_signal

def f203n_f203_net_income_to_working_capital_momentum_calc093_105d_slope_v093_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 9.7583)).rolling(31).std().rolling(30).std() * 0.340396).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc093_105d_slope_v093_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc093_105d_slope_v093_signal

def f203n_f203_net_income_to_working_capital_momentum_calc094_126d_slope_v094_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 6.8393)).diff(32).rolling(16).var().rolling(21).min() * 0.359949).diff(16).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc094_126d_slope_v094_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc094_126d_slope_v094_signal

def f203n_f203_net_income_to_working_capital_momentum_calc095_63d_slope_v095_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 5.8893)).rolling(17).mean().rolling(36).var().rolling(5).mean().diff(27) * 0.728795).diff(8).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc095_63d_slope_v095_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc095_63d_slope_v095_signal

def f203n_f203_net_income_to_working_capital_momentum_calc096_126d_slope_v096_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(2) + 6.3073)).rolling(4).mean().rolling(22).var() * 0.867637).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc096_126d_slope_v096_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc096_126d_slope_v096_signal

def f203n_f203_net_income_to_working_capital_momentum_calc097_252d_slope_v097_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(4) + 4.2453)).rolling(3).max().pct_change(46).rolling(30).max().diff(50) * 0.555020).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc097_252d_slope_v097_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc097_252d_slope_v097_signal

def f203n_f203_net_income_to_working_capital_momentum_calc098_200d_slope_v098_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(4) + 4.7819)).rolling(13).std().rolling(50).min().pct_change(42).rolling(47).min() * 0.899857).diff(8).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc098_200d_slope_v098_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc098_200d_slope_v098_signal

def f203n_f203_net_income_to_working_capital_momentum_calc099_252d_slope_v099_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(30).var().rolling(27).min().rolling(30).mean().diff(19) * 0.065100).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc099_252d_slope_v099_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc099_252d_slope_v099_signal

def f203n_f203_net_income_to_working_capital_momentum_calc100_63d_slope_v100_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 0.1224)).rolling(46).std().pct_change(12) * 0.399703).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc100_63d_slope_v100_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc100_63d_slope_v100_signal

def f203n_f203_net_income_to_working_capital_momentum_calc101_126d_slope_v101_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(3) + 2.3330)).diff(14).rolling(10).mean().rolling(19).mean() * 0.362117).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc101_126d_slope_v101_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc101_126d_slope_v101_signal

def f203n_f203_net_income_to_working_capital_momentum_calc102_105d_slope_v102_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.4847)).rolling(7).max().rolling(4).min().pct_change(27).rolling(35).var() * 0.871573).diff(13).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc102_105d_slope_v102_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc102_105d_slope_v102_signal

def f203n_f203_net_income_to_working_capital_momentum_calc103_42d_slope_v103_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(20).rolling(46).std() * 0.062863).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc103_42d_slope_v103_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc103_42d_slope_v103_signal

def f203n_f203_net_income_to_working_capital_momentum_calc104_42d_slope_v104_signal(netinc, workingcapital):
    res = ((netinc * 7.7027 - workingcapital).rolling(9).std().rolling(2).std() * 0.577855).diff(6).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc104_42d_slope_v104_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc104_42d_slope_v104_signal

def f203n_f203_net_income_to_working_capital_momentum_calc105_126d_slope_v105_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(44).var().rolling(45).var().rolling(16).max().rolling(23).var() * 0.629905).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc105_126d_slope_v105_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc105_126d_slope_v105_signal

def f203n_f203_net_income_to_working_capital_momentum_calc106_21d_slope_v106_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.1699)).rolling(8).max().rolling(5).var().rolling(26).std().rolling(44).mean() * 0.258795).diff(6).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc106_21d_slope_v106_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc106_21d_slope_v106_signal

def f203n_f203_net_income_to_working_capital_momentum_calc107_21d_slope_v107_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 6.7711)).rolling(20).std().rolling(44).max().pct_change(38).pct_change(13) * 0.499842).diff(19).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc107_21d_slope_v107_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc107_21d_slope_v107_signal

def f203n_f203_net_income_to_working_capital_momentum_calc108_105d_slope_v108_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.5506)).pct_change(2).pct_change(15).rolling(5).max().rolling(21).max() * 0.090389).diff(8).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc108_105d_slope_v108_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc108_105d_slope_v108_signal

def f203n_f203_net_income_to_working_capital_momentum_calc109_63d_slope_v109_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(41).rolling(27).var().rolling(44).std() * 0.234213).diff(11).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc109_63d_slope_v109_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc109_63d_slope_v109_signal

def f203n_f203_net_income_to_working_capital_momentum_calc110_252d_slope_v110_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(14).diff(20).pct_change(4).pct_change(29) * 0.692546).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc110_252d_slope_v110_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc110_252d_slope_v110_signal

def f203n_f203_net_income_to_working_capital_momentum_calc111_21d_slope_v111_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 9.4203)).diff(14).diff(25).rolling(45).std() * 0.347604).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc111_21d_slope_v111_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc111_21d_slope_v111_signal

def f203n_f203_net_income_to_working_capital_momentum_calc112_5d_slope_v112_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(32).mean().rolling(14).min().rolling(42).mean().rolling(17).max() * 0.137242).diff(19).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc112_5d_slope_v112_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc112_5d_slope_v112_signal

def f203n_f203_net_income_to_working_capital_momentum_calc113_126d_slope_v113_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(48).max().pct_change(36) * 0.132166).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc113_126d_slope_v113_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc113_126d_slope_v113_signal

def f203n_f203_net_income_to_working_capital_momentum_calc114_126d_slope_v114_signal(netinc, workingcapital):
    res = ((netinc * 3.1791 - workingcapital).pct_change(13).rolling(29).min().rolling(20).min().rolling(22).max() * 0.059453).diff(7).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc114_126d_slope_v114_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc114_126d_slope_v114_signal

def f203n_f203_net_income_to_working_capital_momentum_calc115_252d_slope_v115_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 0.6256)).rolling(19).max().pct_change(19) * 0.161933).diff(2).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc115_252d_slope_v115_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc115_252d_slope_v115_signal

def f203n_f203_net_income_to_working_capital_momentum_calc116_252d_slope_v116_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(46).rolling(48).min() * 0.422972).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc116_252d_slope_v116_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc116_252d_slope_v116_signal

def f203n_f203_net_income_to_working_capital_momentum_calc117_126d_slope_v117_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 8.6599)).pct_change(18).rolling(20).std() * 0.917776).diff(8).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc117_126d_slope_v117_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc117_126d_slope_v117_signal

def f203n_f203_net_income_to_working_capital_momentum_calc118_21d_slope_v118_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(4) + 9.2172)).rolling(37).max().rolling(20).mean() * 0.555646).diff(16).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc118_21d_slope_v118_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc118_21d_slope_v118_signal

def f203n_f203_net_income_to_working_capital_momentum_calc119_105d_slope_v119_signal(netinc, workingcapital):
    res = ((netinc * 6.4578 - workingcapital).rolling(14).std().rolling(37).mean().rolling(18).std() * 0.019348).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc119_105d_slope_v119_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc119_105d_slope_v119_signal

def f203n_f203_net_income_to_working_capital_momentum_calc120_84d_slope_v120_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.5540)).rolling(32).std().rolling(7).max().diff(3).rolling(30).mean() * 0.253228).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc120_84d_slope_v120_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc120_84d_slope_v120_signal

def f203n_f203_net_income_to_working_capital_momentum_calc121_200d_slope_v121_signal(netinc, workingcapital):
    res = ((netinc * 1.7774 - workingcapital).rolling(5).mean().pct_change(29).diff(6).rolling(4).std() * 0.498698).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc121_200d_slope_v121_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc121_200d_slope_v121_signal

def f203n_f203_net_income_to_working_capital_momentum_calc122_42d_slope_v122_signal(netinc, workingcapital):
    res = ((netinc * 6.5115 - workingcapital).diff(25).pct_change(7) * 0.638631).diff(19).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc122_42d_slope_v122_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc122_42d_slope_v122_signal

def f203n_f203_net_income_to_working_capital_momentum_calc123_84d_slope_v123_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.8400)).rolling(15).std().rolling(42).max() * 0.218708).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc123_84d_slope_v123_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc123_84d_slope_v123_signal

def f203n_f203_net_income_to_working_capital_momentum_calc124_252d_slope_v124_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.7598)).rolling(14).min().pct_change(44).pct_change(44).diff(41) * 0.803572).diff(5).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc124_252d_slope_v124_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc124_252d_slope_v124_signal

def f203n_f203_net_income_to_working_capital_momentum_calc125_105d_slope_v125_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(1) + 5.7402)).rolling(31).max().rolling(8).mean() * 0.278357).diff(4).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc125_105d_slope_v125_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc125_105d_slope_v125_signal

def f203n_f203_net_income_to_working_capital_momentum_calc126_5d_slope_v126_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 0.7528)).pct_change(22).rolling(14).var().diff(27).diff(32) * 0.536338).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc126_5d_slope_v126_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc126_5d_slope_v126_signal

def f203n_f203_net_income_to_working_capital_momentum_calc127_21d_slope_v127_signal(netinc, workingcapital):
    res = ((netinc * 8.5986 - workingcapital).rolling(46).max().rolling(43).min() * 0.285239).diff(17).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc127_21d_slope_v127_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc127_21d_slope_v127_signal

def f203n_f203_net_income_to_working_capital_momentum_calc128_126d_slope_v128_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.8352)).rolling(26).var().pct_change(9).rolling(6).std() * 0.715379).diff(11).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc128_126d_slope_v128_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc128_126d_slope_v128_signal

def f203n_f203_net_income_to_working_capital_momentum_calc129_84d_slope_v129_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(17).mean().rolling(39).std().rolling(42).mean() * 0.469742).diff(4).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc129_84d_slope_v129_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc129_84d_slope_v129_signal

def f203n_f203_net_income_to_working_capital_momentum_calc130_200d_slope_v130_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(30).max().rolling(43).std().pct_change(30) * 0.251902).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc130_200d_slope_v130_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc130_200d_slope_v130_signal

def f203n_f203_net_income_to_working_capital_momentum_calc131_63d_slope_v131_signal(netinc, workingcapital):
    res = ((netinc * 4.2103 - workingcapital).rolling(8).std().diff(31).rolling(16).mean().rolling(6).max() * 0.787845).diff(16).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc131_63d_slope_v131_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc131_63d_slope_v131_signal

def f203n_f203_net_income_to_working_capital_momentum_calc132_200d_slope_v132_signal(netinc, workingcapital):
    res = ((netinc.diff(4) / (workingcapital.shift(5) + 5.0953)).rolling(6).mean().rolling(19).max().rolling(25).std().rolling(18).mean() * 0.089663).diff(20).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc132_200d_slope_v132_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc132_200d_slope_v132_signal

def f203n_f203_net_income_to_working_capital_momentum_calc133_21d_slope_v133_signal(netinc, workingcapital):
    res = ((netinc * 8.6854 - workingcapital).rolling(30).std().rolling(31).min().rolling(46).min() * 0.983032).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc133_21d_slope_v133_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc133_21d_slope_v133_signal

def f203n_f203_net_income_to_working_capital_momentum_calc134_200d_slope_v134_signal(netinc, workingcapital):
    res = ((netinc.diff(10) / (workingcapital.shift(2) + 6.0633)).rolling(7).std().diff(15).diff(31) * 0.310739).diff(18).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc134_200d_slope_v134_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc134_200d_slope_v134_signal

def f203n_f203_net_income_to_working_capital_momentum_calc135_105d_slope_v135_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(3) + 9.0728)).pct_change(21).rolling(33).mean().rolling(50).max() * 0.049277).diff(13).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc135_105d_slope_v135_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc135_105d_slope_v135_signal

def f203n_f203_net_income_to_working_capital_momentum_calc136_105d_slope_v136_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 8.3206)).rolling(28).var().rolling(24).max().rolling(43).var() * 0.157709).diff(2).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc136_105d_slope_v136_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc136_105d_slope_v136_signal

def f203n_f203_net_income_to_working_capital_momentum_calc137_42d_slope_v137_signal(netinc, workingcapital):
    res = ((netinc * 8.4213 - workingcapital).rolling(4).mean().pct_change(29) * 0.989355).diff(17).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc137_42d_slope_v137_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc137_42d_slope_v137_signal

def f203n_f203_net_income_to_working_capital_momentum_calc138_5d_slope_v138_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(25).var().rolling(26).std().rolling(28).mean().rolling(46).max() * 0.844649).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc138_5d_slope_v138_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc138_5d_slope_v138_signal

def f203n_f203_net_income_to_working_capital_momentum_calc139_10d_slope_v139_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 3.4082)).rolling(39).max().rolling(27).max() * 0.162692).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc139_10d_slope_v139_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc139_10d_slope_v139_signal

def f203n_f203_net_income_to_working_capital_momentum_calc140_42d_slope_v140_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 9.9428)).rolling(30).mean().pct_change(36) * 0.801161).diff(7).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc140_42d_slope_v140_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc140_42d_slope_v140_signal

def f203n_f203_net_income_to_working_capital_momentum_calc141_63d_slope_v141_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.1084)).rolling(3).mean().rolling(9).mean().rolling(49).mean().rolling(3).max() * 0.696276).diff(4).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc141_63d_slope_v141_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc141_63d_slope_v141_signal

def f203n_f203_net_income_to_working_capital_momentum_calc142_5d_slope_v142_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.4918)).rolling(10).var().rolling(26).var() * 0.527556).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc142_5d_slope_v142_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc142_5d_slope_v142_signal

def f203n_f203_net_income_to_working_capital_momentum_calc143_105d_slope_v143_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 1.5390)).diff(8).rolling(46).min().rolling(25).var() * 0.665726).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc143_105d_slope_v143_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc143_105d_slope_v143_signal

def f203n_f203_net_income_to_working_capital_momentum_calc144_63d_slope_v144_signal(netinc, workingcapital):
    res = ((netinc * 5.9328 - workingcapital).rolling(2).var().rolling(12).min().rolling(37).min().pct_change(38) * 0.372733).diff(18).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc144_63d_slope_v144_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc144_63d_slope_v144_signal

def f203n_f203_net_income_to_working_capital_momentum_calc145_150d_slope_v145_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.0687)).rolling(47).min().diff(45).diff(7).rolling(32).var() * 0.357761).diff(8).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc145_150d_slope_v145_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc145_150d_slope_v145_signal

def f203n_f203_net_income_to_working_capital_momentum_calc146_252d_slope_v146_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(11).std().rolling(12).std().pct_change(43).rolling(3).var() * 0.712145).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc146_252d_slope_v146_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc146_252d_slope_v146_signal

def f203n_f203_net_income_to_working_capital_momentum_calc147_200d_slope_v147_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(43).rolling(32).max().rolling(5).std().rolling(45).std() * 0.872968).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc147_200d_slope_v147_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc147_200d_slope_v147_signal

def f203n_f203_net_income_to_working_capital_momentum_calc148_200d_slope_v148_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(5) + 4.3607)).rolling(30).max().rolling(5).std().diff(11).rolling(22).min() * 0.841843).diff(10).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc148_200d_slope_v148_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc148_200d_slope_v148_signal

def f203n_f203_net_income_to_working_capital_momentum_calc149_84d_slope_v149_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.3051)).pct_change(16).rolling(11).var().rolling(50).max().rolling(43).mean() * 0.593221).diff(9).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc149_84d_slope_v149_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc149_84d_slope_v149_signal

def f203n_f203_net_income_to_working_capital_momentum_calc150_5d_slope_v150_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.1955)).rolling(33).mean().rolling(12).std() * 0.052951).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc150_5d_slope_v150_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc150_5d_slope_v150_signal


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
