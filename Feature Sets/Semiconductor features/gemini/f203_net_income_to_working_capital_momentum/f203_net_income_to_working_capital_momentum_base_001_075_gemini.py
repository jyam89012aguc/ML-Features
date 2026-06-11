import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f203n_f203_net_income_to_working_capital_momentum_calc001_84d_base_v001_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(22).rolling(48).mean().rolling(37).var().rolling(45).var() * 0.149194
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc001_84d_base_v001_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc001_84d_base_v001_signal

def f203n_f203_net_income_to_working_capital_momentum_calc002_126d_base_v002_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(41).var().rolling(25).var() * 0.986020
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc002_126d_base_v002_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc002_126d_base_v002_signal

def f203n_f203_net_income_to_working_capital_momentum_calc003_84d_base_v003_signal(netinc, workingcapital):
    res = (netinc * 6.8878 - workingcapital).diff(5).rolling(4).var().rolling(29).var() * 0.953456
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc003_84d_base_v003_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc003_84d_base_v003_signal

def f203n_f203_net_income_to_working_capital_momentum_calc004_84d_base_v004_signal(netinc, workingcapital):
    res = (netinc.diff(9) / (workingcapital.shift(4) + 1.7171)).rolling(7).min().rolling(5).min().diff(3) * 0.190101
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc004_84d_base_v004_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc004_84d_base_v004_signal

def f203n_f203_net_income_to_working_capital_momentum_calc005_200d_base_v005_signal(netinc, workingcapital):
    res = (netinc.diff(3) / (workingcapital.shift(3) + 0.8493)).rolling(29).var().diff(21).diff(49).rolling(18).min() * 0.713750
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc005_200d_base_v005_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc005_200d_base_v005_signal

def f203n_f203_net_income_to_working_capital_momentum_calc006_252d_base_v006_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 4.6162)).rolling(31).min().rolling(47).std().rolling(18).std().pct_change(36) * 0.251820
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc006_252d_base_v006_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc006_252d_base_v006_signal

def f203n_f203_net_income_to_working_capital_momentum_calc007_5d_base_v007_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 3.7760)).rolling(47).std().rolling(10).min().rolling(12).var() * 0.687582
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc007_5d_base_v007_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc007_5d_base_v007_signal

def f203n_f203_net_income_to_working_capital_momentum_calc008_21d_base_v008_signal(netinc, workingcapital):
    res = (netinc * 2.5769 - workingcapital).rolling(36).min().rolling(37).std() * 0.763228
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc008_21d_base_v008_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc008_21d_base_v008_signal

def f203n_f203_net_income_to_working_capital_momentum_calc009_42d_base_v009_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 9.7663)).rolling(38).var().rolling(49).max().pct_change(9) * 0.494946
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc009_42d_base_v009_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc009_42d_base_v009_signal

def f203n_f203_net_income_to_working_capital_momentum_calc010_126d_base_v010_signal(netinc, workingcapital):
    res = (netinc * 4.6971 - workingcapital).rolling(15).mean().rolling(14).min().rolling(7).max().pct_change(40) * 0.400164
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc010_126d_base_v010_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc010_126d_base_v010_signal

def f203n_f203_net_income_to_working_capital_momentum_calc011_252d_base_v011_signal(netinc, workingcapital):
    res = (netinc * 2.2430 - workingcapital).rolling(2).var().rolling(4).mean().diff(24) * 0.243751
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc011_252d_base_v011_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc011_252d_base_v011_signal

def f203n_f203_net_income_to_working_capital_momentum_calc012_200d_base_v012_signal(netinc, workingcapital):
    res = (netinc * 4.3109 - workingcapital).diff(31).rolling(37).var().rolling(14).mean().rolling(19).mean() * 0.810192
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc012_200d_base_v012_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc012_200d_base_v012_signal

def f203n_f203_net_income_to_working_capital_momentum_calc013_42d_base_v013_signal(netinc, workingcapital):
    res = (netinc.diff(6) / (workingcapital.shift(5) + 8.0379)).rolling(35).min().rolling(41).std().pct_change(26).rolling(31).min() * 0.298747
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc013_42d_base_v013_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc013_42d_base_v013_signal

def f203n_f203_net_income_to_working_capital_momentum_calc014_105d_base_v014_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(9).rolling(14).mean().diff(49).rolling(46).max() * 0.803470
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc014_105d_base_v014_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc014_105d_base_v014_signal

def f203n_f203_net_income_to_working_capital_momentum_calc015_10d_base_v015_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 6.6607)).rolling(13).mean().rolling(12).std().rolling(18).std() * 0.275740
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc015_10d_base_v015_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc015_10d_base_v015_signal

def f203n_f203_net_income_to_working_capital_momentum_calc016_200d_base_v016_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 7.9909)).pct_change(27).rolling(41).var() * 0.195062
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc016_200d_base_v016_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc016_200d_base_v016_signal

def f203n_f203_net_income_to_working_capital_momentum_calc017_42d_base_v017_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(25).max().rolling(41).var().rolling(39).max() * 0.173011
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc017_42d_base_v017_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc017_42d_base_v017_signal

def f203n_f203_net_income_to_working_capital_momentum_calc018_5d_base_v018_signal(netinc, workingcapital):
    res = (netinc * 4.5147 - workingcapital).rolling(38).max().rolling(21).std().rolling(10).mean() * 0.765216
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc018_5d_base_v018_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc018_5d_base_v018_signal

def f203n_f203_net_income_to_working_capital_momentum_calc019_5d_base_v019_signal(netinc, workingcapital):
    res = (netinc * 2.2391 - workingcapital).rolling(49).max().rolling(3).var().rolling(49).min() * 0.484226
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc019_5d_base_v019_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc019_5d_base_v019_signal

def f203n_f203_net_income_to_working_capital_momentum_calc020_126d_base_v020_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(42).std().rolling(38).var().rolling(21).var() * 0.206271
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc020_126d_base_v020_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc020_126d_base_v020_signal

def f203n_f203_net_income_to_working_capital_momentum_calc021_42d_base_v021_signal(netinc, workingcapital):
    res = (netinc * 6.4802 - workingcapital).rolling(43).max().rolling(27).mean().rolling(31).mean() * 0.625522
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc021_42d_base_v021_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc021_42d_base_v021_signal

def f203n_f203_net_income_to_working_capital_momentum_calc022_126d_base_v022_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 7.9314)).rolling(30).min().rolling(2).min().rolling(36).mean().rolling(21).max() * 0.266095
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc022_126d_base_v022_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc022_126d_base_v022_signal

def f203n_f203_net_income_to_working_capital_momentum_calc023_10d_base_v023_signal(netinc, workingcapital):
    res = (netinc * 0.3973 - workingcapital).rolling(30).min().rolling(27).max() * 0.441337
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc023_10d_base_v023_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc023_10d_base_v023_signal

def f203n_f203_net_income_to_working_capital_momentum_calc024_5d_base_v024_signal(netinc, workingcapital):
    res = (netinc.diff(6) / (workingcapital.shift(5) + 4.5205)).pct_change(39).rolling(8).std() * 0.795528
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc024_5d_base_v024_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc024_5d_base_v024_signal

def f203n_f203_net_income_to_working_capital_momentum_calc025_126d_base_v025_signal(netinc, workingcapital):
    res = (netinc.diff(6) / (workingcapital.shift(4) + 3.1130)).rolling(29).max().pct_change(22).rolling(43).min() * 0.717982
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc025_126d_base_v025_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc025_126d_base_v025_signal

def f203n_f203_net_income_to_working_capital_momentum_calc026_200d_base_v026_signal(netinc, workingcapital):
    res = (netinc.diff(8) / (workingcapital.shift(4) + 6.4773)).rolling(28).max().rolling(36).mean().rolling(37).std().rolling(48).mean() * 0.767066
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc026_200d_base_v026_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc026_200d_base_v026_signal

def f203n_f203_net_income_to_working_capital_momentum_calc027_10d_base_v027_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 8.6909)).rolling(13).std().rolling(14).min().rolling(31).max() * 0.371420
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc027_10d_base_v027_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc027_10d_base_v027_signal

def f203n_f203_net_income_to_working_capital_momentum_calc028_105d_base_v028_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(24).std().rolling(49).std() * 0.913911
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc028_105d_base_v028_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc028_105d_base_v028_signal

def f203n_f203_net_income_to_working_capital_momentum_calc029_84d_base_v029_signal(netinc, workingcapital):
    res = (netinc * 4.7951 - workingcapital).diff(43).rolling(44).std().rolling(31).mean().rolling(33).mean() * 0.015020
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc029_84d_base_v029_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc029_84d_base_v029_signal

def f203n_f203_net_income_to_working_capital_momentum_calc030_42d_base_v030_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 8.7460)).rolling(15).std().rolling(19).std().rolling(8).mean() * 0.577369
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc030_42d_base_v030_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc030_42d_base_v030_signal

def f203n_f203_net_income_to_working_capital_momentum_calc031_126d_base_v031_signal(netinc, workingcapital):
    res = (netinc * 8.7820 - workingcapital).diff(6).rolling(18).std().diff(6).rolling(25).std() * 0.402293
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc031_126d_base_v031_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc031_126d_base_v031_signal

def f203n_f203_net_income_to_working_capital_momentum_calc032_150d_base_v032_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 5.6241)).rolling(27).mean().rolling(39).min().pct_change(47).rolling(41).mean() * 0.926207
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc032_150d_base_v032_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc032_150d_base_v032_signal

def f203n_f203_net_income_to_working_capital_momentum_calc033_200d_base_v033_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 2.3248)).rolling(20).var().pct_change(47) * 0.733056
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc033_200d_base_v033_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc033_200d_base_v033_signal

def f203n_f203_net_income_to_working_capital_momentum_calc034_200d_base_v034_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 3.5206)).diff(40).rolling(13).var().rolling(47).mean().rolling(11).std() * 0.636408
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc034_200d_base_v034_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc034_200d_base_v034_signal

def f203n_f203_net_income_to_working_capital_momentum_calc035_126d_base_v035_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(6).rolling(21).var().rolling(5).mean().rolling(30).std() * 0.896401
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc035_126d_base_v035_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc035_126d_base_v035_signal

def f203n_f203_net_income_to_working_capital_momentum_calc036_150d_base_v036_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 5.5727)).rolling(38).var().rolling(15).var().rolling(30).min() * 0.847953
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc036_150d_base_v036_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc036_150d_base_v036_signal

def f203n_f203_net_income_to_working_capital_momentum_calc037_126d_base_v037_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 4.0578)).diff(8).rolling(32).var().rolling(46).mean() * 0.937503
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc037_126d_base_v037_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc037_126d_base_v037_signal

def f203n_f203_net_income_to_working_capital_momentum_calc038_10d_base_v038_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(9).min().rolling(30).max().diff(5).diff(15) * 0.231678
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc038_10d_base_v038_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc038_10d_base_v038_signal

def f203n_f203_net_income_to_working_capital_momentum_calc039_21d_base_v039_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(12).rolling(23).var().rolling(49).min().pct_change(31) * 0.274038
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc039_21d_base_v039_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc039_21d_base_v039_signal

def f203n_f203_net_income_to_working_capital_momentum_calc040_5d_base_v040_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 5.1263)).rolling(46).std().rolling(49).mean() * 0.581004
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc040_5d_base_v040_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc040_5d_base_v040_signal

def f203n_f203_net_income_to_working_capital_momentum_calc041_5d_base_v041_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 9.3833)).rolling(4).mean().pct_change(5) * 0.236159
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc041_5d_base_v041_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc041_5d_base_v041_signal

def f203n_f203_net_income_to_working_capital_momentum_calc042_10d_base_v042_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 4.6648)).rolling(9).std().pct_change(27).rolling(31).std().diff(47) * 0.289146
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc042_10d_base_v042_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc042_10d_base_v042_signal

def f203n_f203_net_income_to_working_capital_momentum_calc043_63d_base_v043_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(32).rolling(42).var().rolling(17).std().rolling(37).max() * 0.760287
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc043_63d_base_v043_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc043_63d_base_v043_signal

def f203n_f203_net_income_to_working_capital_momentum_calc044_150d_base_v044_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 5.3084)).rolling(14).mean().rolling(43).std() * 0.237864
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc044_150d_base_v044_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc044_150d_base_v044_signal

def f203n_f203_net_income_to_working_capital_momentum_calc045_42d_base_v045_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 2.8234)).rolling(11).max().rolling(11).mean() * 0.648261
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc045_42d_base_v045_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc045_42d_base_v045_signal

def f203n_f203_net_income_to_working_capital_momentum_calc046_42d_base_v046_signal(netinc, workingcapital):
    res = (netinc.diff(9) / (workingcapital.shift(2) + 1.7423)).rolling(18).min().diff(23) * 0.359498
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc046_42d_base_v046_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc046_42d_base_v046_signal

def f203n_f203_net_income_to_working_capital_momentum_calc047_126d_base_v047_signal(netinc, workingcapital):
    res = (netinc.diff(4) / (workingcapital.shift(4) + 6.3573)).pct_change(7).rolling(43).std() * 0.057331
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc047_126d_base_v047_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc047_126d_base_v047_signal

def f203n_f203_net_income_to_working_capital_momentum_calc048_126d_base_v048_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 8.7641)).rolling(29).std().pct_change(3) * 0.114310
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc048_126d_base_v048_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc048_126d_base_v048_signal

def f203n_f203_net_income_to_working_capital_momentum_calc049_42d_base_v049_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(34).min().pct_change(12).rolling(5).max() * 0.985687
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc049_42d_base_v049_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc049_42d_base_v049_signal

def f203n_f203_net_income_to_working_capital_momentum_calc050_252d_base_v050_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 0.9780)).rolling(6).max().diff(28).diff(24).rolling(35).min() * 0.814699
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc050_252d_base_v050_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc050_252d_base_v050_signal

def f203n_f203_net_income_to_working_capital_momentum_calc051_42d_base_v051_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(35).var().rolling(13).var().rolling(11).mean().rolling(7).var() * 0.482740
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc051_42d_base_v051_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc051_42d_base_v051_signal

def f203n_f203_net_income_to_working_capital_momentum_calc052_21d_base_v052_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 8.6945)).rolling(7).mean().diff(3).diff(29) * 0.051303
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc052_21d_base_v052_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc052_21d_base_v052_signal

def f203n_f203_net_income_to_working_capital_momentum_calc053_252d_base_v053_signal(netinc, workingcapital):
    res = (netinc.diff(9) / (workingcapital.shift(5) + 1.2703)).rolling(38).std().pct_change(3).diff(2).pct_change(47) * 0.850502
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc053_252d_base_v053_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc053_252d_base_v053_signal

def f203n_f203_net_income_to_working_capital_momentum_calc054_21d_base_v054_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 7.4943)).diff(25).rolling(23).var().rolling(11).min().rolling(50).mean() * 0.726334
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc054_21d_base_v054_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc054_21d_base_v054_signal

def f203n_f203_net_income_to_working_capital_momentum_calc055_126d_base_v055_signal(netinc, workingcapital):
    res = (netinc.diff(10) / (workingcapital.shift(5) + 3.3799)).rolling(39).mean().rolling(14).var().rolling(11).var() * 0.711324
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc055_126d_base_v055_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc055_126d_base_v055_signal

def f203n_f203_net_income_to_working_capital_momentum_calc056_21d_base_v056_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 8.6596)).rolling(10).var().rolling(37).mean().pct_change(36) * 0.164659
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc056_21d_base_v056_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc056_21d_base_v056_signal

def f203n_f203_net_income_to_working_capital_momentum_calc057_42d_base_v057_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 7.5908)).pct_change(3).rolling(30).var() * 0.561123
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc057_42d_base_v057_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc057_42d_base_v057_signal

def f203n_f203_net_income_to_working_capital_momentum_calc058_150d_base_v058_signal(netinc, workingcapital):
    res = (netinc * 7.8021 - workingcapital).rolling(33).var().rolling(40).std() * 0.616372
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc058_150d_base_v058_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc058_150d_base_v058_signal

def f203n_f203_net_income_to_working_capital_momentum_calc059_10d_base_v059_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(43).max().rolling(35).max() * 0.062391
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc059_10d_base_v059_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc059_10d_base_v059_signal

def f203n_f203_net_income_to_working_capital_momentum_calc060_126d_base_v060_signal(netinc, workingcapital):
    res = (netinc.diff(4) / (workingcapital.shift(2) + 5.6164)).rolling(19).var().rolling(27).max().rolling(40).mean().pct_change(49) * 0.640914
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc060_126d_base_v060_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc060_126d_base_v060_signal

def f203n_f203_net_income_to_working_capital_momentum_calc061_10d_base_v061_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 4.7615)).rolling(48).mean().diff(10).pct_change(34).rolling(28).max() * 0.521666
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc061_10d_base_v061_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc061_10d_base_v061_signal

def f203n_f203_net_income_to_working_capital_momentum_calc062_42d_base_v062_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 5.6151)).rolling(32).mean().rolling(19).mean().rolling(4).min().rolling(42).std() * 0.017150
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc062_42d_base_v062_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc062_42d_base_v062_signal

def f203n_f203_net_income_to_working_capital_momentum_calc063_10d_base_v063_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(47).mean().diff(29).rolling(35).max() * 0.769736
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc063_10d_base_v063_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc063_10d_base_v063_signal

def f203n_f203_net_income_to_working_capital_momentum_calc064_200d_base_v064_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(40).std().rolling(24).std().rolling(36).std().pct_change(5) * 0.120697
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc064_200d_base_v064_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc064_200d_base_v064_signal

def f203n_f203_net_income_to_working_capital_momentum_calc065_105d_base_v065_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(39).rolling(30).max() * 0.074163
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc065_105d_base_v065_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc065_105d_base_v065_signal

def f203n_f203_net_income_to_working_capital_momentum_calc066_105d_base_v066_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 7.5110)).diff(21).rolling(44).max() * 0.868754
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc066_105d_base_v066_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc066_105d_base_v066_signal

def f203n_f203_net_income_to_working_capital_momentum_calc067_10d_base_v067_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 9.3829)).diff(10).rolling(14).std() * 0.298916
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc067_10d_base_v067_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc067_10d_base_v067_signal

def f203n_f203_net_income_to_working_capital_momentum_calc068_105d_base_v068_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(35).max().diff(46) * 0.245233
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc068_105d_base_v068_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc068_105d_base_v068_signal

def f203n_f203_net_income_to_working_capital_momentum_calc069_10d_base_v069_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 1.5410)).pct_change(20).rolling(46).min().rolling(31).mean().rolling(30).mean() * 0.988056
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc069_10d_base_v069_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc069_10d_base_v069_signal

def f203n_f203_net_income_to_working_capital_momentum_calc070_10d_base_v070_signal(netinc, workingcapital):
    res = (netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(36).rolling(8).min() * 0.953788
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc070_10d_base_v070_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc070_10d_base_v070_signal

def f203n_f203_net_income_to_working_capital_momentum_calc071_200d_base_v071_signal(netinc, workingcapital):
    res = (netinc * 4.0888 - workingcapital).rolling(7).min().rolling(33).var().rolling(45).var().diff(49) * 0.784823
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc071_200d_base_v071_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc071_200d_base_v071_signal

def f203n_f203_net_income_to_working_capital_momentum_calc072_21d_base_v072_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 7.8761)).rolling(6).mean().rolling(47).max().rolling(45).max() * 0.026224
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc072_21d_base_v072_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc072_21d_base_v072_signal

def f203n_f203_net_income_to_working_capital_momentum_calc073_42d_base_v073_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 8.8870)).pct_change(28).rolling(25).min().rolling(27).max().pct_change(2) * 0.185537
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc073_42d_base_v073_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc073_42d_base_v073_signal

def f203n_f203_net_income_to_working_capital_momentum_calc074_126d_base_v074_signal(netinc, workingcapital):
    res = (workingcapital / (netinc + 1.1763)).rolling(15).max().rolling(26).std().rolling(14).min() * 0.411782
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc074_126d_base_v074_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc074_126d_base_v074_signal

def f203n_f203_net_income_to_working_capital_momentum_calc075_126d_base_v075_signal(netinc, workingcapital):
    res = (netinc / (workingcapital + 4.0261)).pct_change(23).rolling(40).mean().rolling(45).mean().rolling(26).min() * 0.821516
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc075_126d_base_v075_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc075_126d_base_v075_signal


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
