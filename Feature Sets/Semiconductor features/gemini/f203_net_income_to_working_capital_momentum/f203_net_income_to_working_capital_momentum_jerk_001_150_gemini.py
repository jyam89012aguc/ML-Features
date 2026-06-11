import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f203n_f203_net_income_to_working_capital_momentum_calc001_10d_jerk_v001_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 1.7098)).diff(30).rolling(28).min().rolling(37).std().rolling(50).mean() * 0.509854).diff(6).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc001_10d_jerk_v001_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc001_10d_jerk_v001_signal

def f203n_f203_net_income_to_working_capital_momentum_calc002_21d_jerk_v002_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(30).rolling(5).var().rolling(6).std().rolling(16).max() * 0.416349).diff(9).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc002_21d_jerk_v002_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc002_21d_jerk_v002_signal

def f203n_f203_net_income_to_working_capital_momentum_calc003_252d_jerk_v003_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(1) + 8.2728)).rolling(36).min().rolling(11).var().rolling(20).mean() * 0.531696).diff(6).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc003_252d_jerk_v003_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc003_252d_jerk_v003_signal

def f203n_f203_net_income_to_working_capital_momentum_calc004_150d_jerk_v004_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 0.7137)).pct_change(24).rolling(39).min() * 0.660706).diff(12).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc004_150d_jerk_v004_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc004_150d_jerk_v004_signal

def f203n_f203_net_income_to_working_capital_momentum_calc005_252d_jerk_v005_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.6941)).rolling(28).var().pct_change(2) * 0.276904).diff(2).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc005_252d_jerk_v005_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc005_252d_jerk_v005_signal

def f203n_f203_net_income_to_working_capital_momentum_calc006_105d_jerk_v006_signal(netinc, workingcapital):
    res = ((netinc * 6.6908 - workingcapital).rolling(5).max().pct_change(38).rolling(15).mean() * 0.184380).diff(6).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc006_105d_jerk_v006_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc006_105d_jerk_v006_signal

def f203n_f203_net_income_to_working_capital_momentum_calc007_105d_jerk_v007_signal(netinc, workingcapital):
    res = ((netinc.diff(4) / (workingcapital.shift(4) + 0.9561)).pct_change(19).rolling(50).mean() * 0.712578).diff(12).diff(19).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc007_105d_jerk_v007_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc007_105d_jerk_v007_signal

def f203n_f203_net_income_to_working_capital_momentum_calc008_5d_jerk_v008_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(30).std().rolling(42).mean().pct_change(25).diff(31) * 0.466484).diff(8).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc008_5d_jerk_v008_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc008_5d_jerk_v008_signal

def f203n_f203_net_income_to_working_capital_momentum_calc009_84d_jerk_v009_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(5) + 2.4705)).pct_change(49).rolling(46).max().rolling(15).mean() * 0.667608).diff(5).diff(5).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc009_84d_jerk_v009_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc009_84d_jerk_v009_signal

def f203n_f203_net_income_to_working_capital_momentum_calc010_126d_jerk_v010_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.5076)).rolling(10).var().diff(15).rolling(14).min() * 0.440195).diff(20).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc010_126d_jerk_v010_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc010_126d_jerk_v010_signal

def f203n_f203_net_income_to_working_capital_momentum_calc011_42d_jerk_v011_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(3) + 2.7004)).rolling(42).var().rolling(35).std().diff(6) * 0.794164).diff(19).diff(14).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc011_42d_jerk_v011_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc011_42d_jerk_v011_signal

def f203n_f203_net_income_to_working_capital_momentum_calc012_150d_jerk_v012_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 6.0007)).rolling(21).min().rolling(45).min().rolling(12).var() * 0.133680).diff(10).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc012_150d_jerk_v012_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc012_150d_jerk_v012_signal

def f203n_f203_net_income_to_working_capital_momentum_calc013_126d_jerk_v013_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(19).min().rolling(41).mean().diff(39).rolling(2).std() * 0.108668).diff(14).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc013_126d_jerk_v013_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc013_126d_jerk_v013_signal

def f203n_f203_net_income_to_working_capital_momentum_calc014_252d_jerk_v014_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(40).mean().rolling(39).min().rolling(46).mean() * 0.422529).diff(3).diff(10).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc014_252d_jerk_v014_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc014_252d_jerk_v014_signal

def f203n_f203_net_income_to_working_capital_momentum_calc015_21d_jerk_v015_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(29).var().rolling(48).mean().rolling(4).std().rolling(15).var() * 0.260834).diff(12).diff(4).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc015_21d_jerk_v015_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc015_21d_jerk_v015_signal

def f203n_f203_net_income_to_working_capital_momentum_calc016_150d_jerk_v016_signal(netinc, workingcapital):
    res = ((netinc * 2.9242 - workingcapital).pct_change(17).pct_change(44) * 0.880475).diff(3).diff(14).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc016_150d_jerk_v016_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc016_150d_jerk_v016_signal

def f203n_f203_net_income_to_working_capital_momentum_calc017_126d_jerk_v017_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(10).diff(38) * 0.373989).diff(4).diff(13).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc017_126d_jerk_v017_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc017_126d_jerk_v017_signal

def f203n_f203_net_income_to_working_capital_momentum_calc018_126d_jerk_v018_signal(netinc, workingcapital):
    res = ((netinc * 0.7131 - workingcapital).diff(24).rolling(42).max().rolling(35).std() * 0.468789).diff(4).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc018_126d_jerk_v018_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc018_126d_jerk_v018_signal

def f203n_f203_net_income_to_working_capital_momentum_calc019_21d_jerk_v019_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 5.0127)).rolling(10).var().rolling(21).var().rolling(29).var() * 0.655535).diff(20).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc019_21d_jerk_v019_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc019_21d_jerk_v019_signal

def f203n_f203_net_income_to_working_capital_momentum_calc020_10d_jerk_v020_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 8.1867)).rolling(25).mean().rolling(21).mean().pct_change(28) * 0.999332).diff(20).diff(15).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc020_10d_jerk_v020_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc020_10d_jerk_v020_signal

def f203n_f203_net_income_to_working_capital_momentum_calc021_21d_jerk_v021_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(29).rolling(48).var().rolling(40).min() * 0.087628).diff(3).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc021_21d_jerk_v021_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc021_21d_jerk_v021_signal

def f203n_f203_net_income_to_working_capital_momentum_calc022_126d_jerk_v022_signal(netinc, workingcapital):
    res = ((netinc * 0.6949 - workingcapital).rolling(22).min().pct_change(23).rolling(18).min() * 0.619967).diff(11).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc022_126d_jerk_v022_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc022_126d_jerk_v022_signal

def f203n_f203_net_income_to_working_capital_momentum_calc023_42d_jerk_v023_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.2094)).rolling(29).max().rolling(3).min().rolling(24).max().rolling(39).mean() * 0.377695).diff(14).diff(18).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc023_42d_jerk_v023_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc023_42d_jerk_v023_signal

def f203n_f203_net_income_to_working_capital_momentum_calc024_126d_jerk_v024_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(4) + 8.4600)).rolling(46).max().rolling(48).std() * 0.662115).diff(17).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc024_126d_jerk_v024_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc024_126d_jerk_v024_signal

def f203n_f203_net_income_to_working_capital_momentum_calc025_150d_jerk_v025_signal(netinc, workingcapital):
    res = ((netinc * 5.8756 - workingcapital).rolling(27).std().rolling(47).min().rolling(18).min() * 0.701987).diff(20).diff(11).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc025_150d_jerk_v025_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc025_150d_jerk_v025_signal

def f203n_f203_net_income_to_working_capital_momentum_calc026_200d_jerk_v026_signal(netinc, workingcapital):
    res = ((netinc.diff(2) / (workingcapital.shift(2) + 1.5790)).rolling(30).mean().rolling(7).var().rolling(37).mean() * 0.687934).diff(13).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc026_200d_jerk_v026_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc026_200d_jerk_v026_signal

def f203n_f203_net_income_to_working_capital_momentum_calc027_84d_jerk_v027_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(7).std().rolling(10).min() * 0.350411).diff(16).diff(16).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc027_84d_jerk_v027_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc027_84d_jerk_v027_signal

def f203n_f203_net_income_to_working_capital_momentum_calc028_105d_jerk_v028_signal(netinc, workingcapital):
    res = ((netinc * 4.0035 - workingcapital).rolling(48).min().rolling(36).var() * 0.357563).diff(3).diff(14).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc028_105d_jerk_v028_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc028_105d_jerk_v028_signal

def f203n_f203_net_income_to_working_capital_momentum_calc029_126d_jerk_v029_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(2).std().rolling(47).min() * 0.793017).diff(19).diff(10).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc029_126d_jerk_v029_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc029_126d_jerk_v029_signal

def f203n_f203_net_income_to_working_capital_momentum_calc030_5d_jerk_v030_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(49).min().rolling(21).max().pct_change(12) * 0.767724).diff(6).diff(17).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc030_5d_jerk_v030_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc030_5d_jerk_v030_signal

def f203n_f203_net_income_to_working_capital_momentum_calc031_5d_jerk_v031_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(8).max().rolling(18).max() * 0.487532).diff(2).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc031_5d_jerk_v031_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc031_5d_jerk_v031_signal

def f203n_f203_net_income_to_working_capital_momentum_calc032_10d_jerk_v032_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(3) + 2.1258)).diff(3).rolling(13).min().rolling(45).min() * 0.192521).diff(10).diff(10).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc032_10d_jerk_v032_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc032_10d_jerk_v032_signal

def f203n_f203_net_income_to_working_capital_momentum_calc033_84d_jerk_v033_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(7).var().pct_change(49).rolling(45).mean() * 0.875822).diff(18).diff(11).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc033_84d_jerk_v033_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc033_84d_jerk_v033_signal

def f203n_f203_net_income_to_working_capital_momentum_calc034_5d_jerk_v034_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.0089)).rolling(26).max().rolling(40).std().diff(3) * 0.824244).diff(8).diff(12).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc034_5d_jerk_v034_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc034_5d_jerk_v034_signal

def f203n_f203_net_income_to_working_capital_momentum_calc035_105d_jerk_v035_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 0.9431)).rolling(4).var().pct_change(43).rolling(15).mean().rolling(33).std() * 0.247692).diff(10).diff(18).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc035_105d_jerk_v035_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc035_105d_jerk_v035_signal

def f203n_f203_net_income_to_working_capital_momentum_calc036_105d_jerk_v036_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 2.2756)).rolling(35).var().pct_change(11).diff(4) * 0.671283).diff(8).diff(19).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc036_105d_jerk_v036_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc036_105d_jerk_v036_signal

def f203n_f203_net_income_to_working_capital_momentum_calc037_84d_jerk_v037_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 9.8988)).rolling(10).std().diff(12).rolling(23).max() * 0.521192).diff(5).diff(6).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc037_84d_jerk_v037_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc037_84d_jerk_v037_signal

def f203n_f203_net_income_to_working_capital_momentum_calc038_42d_jerk_v038_signal(netinc, workingcapital):
    res = ((netinc * 3.4318 - workingcapital).rolling(29).var().rolling(22).var() * 0.758724).diff(20).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc038_42d_jerk_v038_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc038_42d_jerk_v038_signal

def f203n_f203_net_income_to_working_capital_momentum_calc039_126d_jerk_v039_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(37).rolling(10).min().rolling(32).mean() * 0.205462).diff(19).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc039_126d_jerk_v039_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc039_126d_jerk_v039_signal

def f203n_f203_net_income_to_working_capital_momentum_calc040_200d_jerk_v040_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(37).min().diff(18) * 0.950740).diff(7).diff(14).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc040_200d_jerk_v040_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc040_200d_jerk_v040_signal

def f203n_f203_net_income_to_working_capital_momentum_calc041_200d_jerk_v041_signal(netinc, workingcapital):
    res = ((netinc * 7.3241 - workingcapital).rolling(13).mean().rolling(37).max().rolling(6).std().rolling(50).var() * 0.952927).diff(19).diff(13).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc041_200d_jerk_v041_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc041_200d_jerk_v041_signal

def f203n_f203_net_income_to_working_capital_momentum_calc042_63d_jerk_v042_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 2.7156)).rolling(14).std().pct_change(7).rolling(4).var() * 0.539183).diff(20).diff(12).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc042_63d_jerk_v042_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc042_63d_jerk_v042_signal

def f203n_f203_net_income_to_working_capital_momentum_calc043_200d_jerk_v043_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(46).var().rolling(3).min() * 0.585749).diff(7).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc043_200d_jerk_v043_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc043_200d_jerk_v043_signal

def f203n_f203_net_income_to_working_capital_momentum_calc044_42d_jerk_v044_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(1) + 4.2149)).rolling(40).mean().pct_change(10) * 0.777163).diff(4).diff(9).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc044_42d_jerk_v044_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc044_42d_jerk_v044_signal

def f203n_f203_net_income_to_working_capital_momentum_calc045_21d_jerk_v045_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(5).std().rolling(31).max().rolling(29).std().rolling(15).max() * 0.637050).diff(13).diff(8).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc045_21d_jerk_v045_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc045_21d_jerk_v045_signal

def f203n_f203_net_income_to_working_capital_momentum_calc046_84d_jerk_v046_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(12).mean().rolling(28).var() * 0.361127).diff(4).diff(12).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc046_84d_jerk_v046_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc046_84d_jerk_v046_signal

def f203n_f203_net_income_to_working_capital_momentum_calc047_10d_jerk_v047_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.2054)).rolling(19).var().diff(14).rolling(30).std() * 0.766464).diff(19).diff(3).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc047_10d_jerk_v047_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc047_10d_jerk_v047_signal

def f203n_f203_net_income_to_working_capital_momentum_calc048_105d_jerk_v048_signal(netinc, workingcapital):
    res = ((netinc.diff(8) / (workingcapital.shift(4) + 8.2568)).rolling(12).var().rolling(26).mean().diff(20).rolling(7).max() * 0.528668).diff(8).diff(19).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc048_105d_jerk_v048_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc048_105d_jerk_v048_signal

def f203n_f203_net_income_to_working_capital_momentum_calc049_252d_jerk_v049_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(32).std().rolling(23).mean().rolling(23).min() * 0.872519).diff(4).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc049_252d_jerk_v049_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc049_252d_jerk_v049_signal

def f203n_f203_net_income_to_working_capital_momentum_calc050_5d_jerk_v050_signal(netinc, workingcapital):
    res = ((netinc.diff(10) / (workingcapital.shift(3) + 6.4316)).rolling(6).min().diff(42) * 0.951689).diff(2).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc050_5d_jerk_v050_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc050_5d_jerk_v050_signal

def f203n_f203_net_income_to_working_capital_momentum_calc051_10d_jerk_v051_signal(netinc, workingcapital):
    res = ((netinc * 6.5189 - workingcapital).rolling(16).std().rolling(5).min().rolling(19).std().rolling(24).var() * 0.748064).diff(19).diff(16).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc051_10d_jerk_v051_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc051_10d_jerk_v051_signal

def f203n_f203_net_income_to_working_capital_momentum_calc052_105d_jerk_v052_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(28).rolling(50).std() * 0.582475).diff(13).diff(12).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc052_105d_jerk_v052_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc052_105d_jerk_v052_signal

def f203n_f203_net_income_to_working_capital_momentum_calc053_84d_jerk_v053_signal(netinc, workingcapital):
    res = ((netinc * 6.1701 - workingcapital).rolling(24).std().rolling(29).min().rolling(3).max().rolling(38).var() * 0.087467).diff(19).diff(17).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc053_84d_jerk_v053_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc053_84d_jerk_v053_signal

def f203n_f203_net_income_to_working_capital_momentum_calc054_5d_jerk_v054_signal(netinc, workingcapital):
    res = ((netinc * 0.4477 - workingcapital).pct_change(24).rolling(19).max() * 0.043603).diff(6).diff(5).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc054_5d_jerk_v054_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc054_5d_jerk_v054_signal

def f203n_f203_net_income_to_working_capital_momentum_calc055_252d_jerk_v055_signal(netinc, workingcapital):
    res = ((netinc * 1.0006 - workingcapital).rolling(43).mean().rolling(4).var() * 0.708007).diff(13).diff(16).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc055_252d_jerk_v055_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc055_252d_jerk_v055_signal

def f203n_f203_net_income_to_working_capital_momentum_calc056_105d_jerk_v056_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 6.3150)).rolling(48).var().rolling(45).max().rolling(32).std() * 0.089073).diff(14).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc056_105d_jerk_v056_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc056_105d_jerk_v056_signal

def f203n_f203_net_income_to_working_capital_momentum_calc057_10d_jerk_v057_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(35).std().rolling(8).var().rolling(22).max().pct_change(19) * 0.211943).diff(19).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc057_10d_jerk_v057_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc057_10d_jerk_v057_signal

def f203n_f203_net_income_to_working_capital_momentum_calc058_126d_jerk_v058_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 0.1756)).pct_change(50).rolling(14).max() * 0.453531).diff(19).diff(18).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc058_126d_jerk_v058_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc058_126d_jerk_v058_signal

def f203n_f203_net_income_to_working_capital_momentum_calc059_252d_jerk_v059_signal(netinc, workingcapital):
    res = ((netinc * 3.8689 - workingcapital).rolling(10).min().rolling(32).max() * 0.770603).diff(14).diff(15).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc059_252d_jerk_v059_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc059_252d_jerk_v059_signal

def f203n_f203_net_income_to_working_capital_momentum_calc060_150d_jerk_v060_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 4.1614)).rolling(29).max().rolling(35).mean().rolling(4).mean().rolling(18).max() * 0.866835).diff(19).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc060_150d_jerk_v060_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc060_150d_jerk_v060_signal

def f203n_f203_net_income_to_working_capital_momentum_calc061_252d_jerk_v061_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 3.7437)).rolling(24).max().diff(8).rolling(48).min().pct_change(10) * 0.616301).diff(9).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc061_252d_jerk_v061_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc061_252d_jerk_v061_signal

def f203n_f203_net_income_to_working_capital_momentum_calc062_10d_jerk_v062_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.4810)).rolling(12).mean().rolling(33).std().rolling(14).mean() * 0.905165).diff(15).diff(15).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc062_10d_jerk_v062_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc062_10d_jerk_v062_signal

def f203n_f203_net_income_to_working_capital_momentum_calc063_42d_jerk_v063_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 3.9251)).rolling(41).std().rolling(20).min().rolling(39).mean() * 0.818892).diff(17).diff(10).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc063_42d_jerk_v063_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc063_42d_jerk_v063_signal

def f203n_f203_net_income_to_working_capital_momentum_calc064_42d_jerk_v064_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(3) + 9.5450)).rolling(23).std().rolling(33).var().diff(47).rolling(11).min() * 0.727179).diff(15).diff(16).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc064_42d_jerk_v064_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc064_42d_jerk_v064_signal

def f203n_f203_net_income_to_working_capital_momentum_calc065_42d_jerk_v065_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 2.5571)).rolling(35).max().rolling(30).mean().rolling(8).min() * 0.144612).diff(12).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc065_42d_jerk_v065_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc065_42d_jerk_v065_signal

def f203n_f203_net_income_to_working_capital_momentum_calc066_105d_jerk_v066_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(4) + 8.1262)).rolling(13).std().pct_change(13).diff(33) * 0.887200).diff(4).diff(11).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc066_105d_jerk_v066_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc066_105d_jerk_v066_signal

def f203n_f203_net_income_to_working_capital_momentum_calc067_126d_jerk_v067_signal(netinc, workingcapital):
    res = ((netinc.diff(2) / (workingcapital.shift(5) + 3.5439)).rolling(46).min().rolling(12).max() * 0.446194).diff(5).diff(15).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc067_126d_jerk_v067_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc067_126d_jerk_v067_signal

def f203n_f203_net_income_to_working_capital_momentum_calc068_105d_jerk_v068_signal(netinc, workingcapital):
    res = ((netinc.diff(9) / (workingcapital.shift(5) + 5.8184)).rolling(19).var().rolling(4).var() * 0.590259).diff(9).diff(7).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc068_105d_jerk_v068_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc068_105d_jerk_v068_signal

def f203n_f203_net_income_to_working_capital_momentum_calc069_105d_jerk_v069_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.5396)).rolling(32).mean().rolling(10).min().pct_change(23).rolling(10).mean() * 0.484870).diff(19).diff(19).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc069_105d_jerk_v069_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc069_105d_jerk_v069_signal

def f203n_f203_net_income_to_working_capital_momentum_calc070_10d_jerk_v070_signal(netinc, workingcapital):
    res = ((netinc.diff(8) / (workingcapital.shift(1) + 6.0662)).pct_change(35).rolling(6).min().rolling(11).std() * 0.768172).diff(16).diff(17).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc070_10d_jerk_v070_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc070_10d_jerk_v070_signal

def f203n_f203_net_income_to_working_capital_momentum_calc071_105d_jerk_v071_signal(netinc, workingcapital):
    res = ((netinc * 7.4992 - workingcapital).rolling(16).mean().rolling(40).min().pct_change(5).rolling(23).var() * 0.566614).diff(14).diff(15).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc071_105d_jerk_v071_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc071_105d_jerk_v071_signal

def f203n_f203_net_income_to_working_capital_momentum_calc072_252d_jerk_v072_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(3) + 3.4596)).diff(46).rolling(28).var() * 0.123298).diff(4).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc072_252d_jerk_v072_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc072_252d_jerk_v072_signal

def f203n_f203_net_income_to_working_capital_momentum_calc073_200d_jerk_v073_signal(netinc, workingcapital):
    res = ((netinc * 7.3009 - workingcapital).pct_change(11).rolling(23).max().rolling(6).mean().diff(14) * 0.701807).diff(14).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc073_200d_jerk_v073_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc073_200d_jerk_v073_signal

def f203n_f203_net_income_to_working_capital_momentum_calc074_42d_jerk_v074_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(1) + 2.8815)).rolling(41).var().rolling(28).mean().rolling(8).std().rolling(30).var() * 0.028128).diff(16).diff(11).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc074_42d_jerk_v074_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc074_42d_jerk_v074_signal

def f203n_f203_net_income_to_working_capital_momentum_calc075_252d_jerk_v075_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.5980)).rolling(18).max().pct_change(17) * 0.778091).diff(11).diff(17).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc075_252d_jerk_v075_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc075_252d_jerk_v075_signal

def f203n_f203_net_income_to_working_capital_momentum_calc076_63d_jerk_v076_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.1058)).rolling(39).std().rolling(46).min().rolling(22).var() * 0.065629).diff(6).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc076_63d_jerk_v076_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc076_63d_jerk_v076_signal

def f203n_f203_net_income_to_working_capital_momentum_calc077_10d_jerk_v077_signal(netinc, workingcapital):
    res = ((netinc.diff(9) / (workingcapital.shift(3) + 1.6726)).rolling(23).max().rolling(42).var().diff(18).pct_change(50) * 0.089110).diff(15).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc077_10d_jerk_v077_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc077_10d_jerk_v077_signal

def f203n_f203_net_income_to_working_capital_momentum_calc078_200d_jerk_v078_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.6803)).rolling(11).var().rolling(13).max().diff(39).rolling(12).var() * 0.709820).diff(12).diff(6).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc078_200d_jerk_v078_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc078_200d_jerk_v078_signal

def f203n_f203_net_income_to_working_capital_momentum_calc079_252d_jerk_v079_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).diff(18).pct_change(26) * 0.928230).diff(12).diff(10).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc079_252d_jerk_v079_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc079_252d_jerk_v079_signal

def f203n_f203_net_income_to_working_capital_momentum_calc080_126d_jerk_v080_signal(netinc, workingcapital):
    res = ((netinc.diff(2) / (workingcapital.shift(2) + 3.1660)).rolling(28).var().rolling(43).var().rolling(19).var().rolling(50).max() * 0.272426).diff(2).diff(13).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc080_126d_jerk_v080_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc080_126d_jerk_v080_signal

def f203n_f203_net_income_to_working_capital_momentum_calc081_84d_jerk_v081_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(29).std().rolling(47).var().pct_change(39) * 0.740701).diff(17).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc081_84d_jerk_v081_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc081_84d_jerk_v081_signal

def f203n_f203_net_income_to_working_capital_momentum_calc082_150d_jerk_v082_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 1.9609)).rolling(38).std().diff(23) * 0.864906).diff(15).diff(20).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc082_150d_jerk_v082_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc082_150d_jerk_v082_signal

def f203n_f203_net_income_to_working_capital_momentum_calc083_150d_jerk_v083_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(7).mean().diff(30).rolling(42).std().rolling(16).var() * 0.576695).diff(13).diff(12).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc083_150d_jerk_v083_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc083_150d_jerk_v083_signal

def f203n_f203_net_income_to_working_capital_momentum_calc084_200d_jerk_v084_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 2.5107)).pct_change(15).rolling(2).min().rolling(42).max() * 0.755845).diff(2).diff(12).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc084_200d_jerk_v084_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc084_200d_jerk_v084_signal

def f203n_f203_net_income_to_working_capital_momentum_calc085_84d_jerk_v085_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(3).rolling(5).mean() * 0.936237).diff(6).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc085_84d_jerk_v085_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc085_84d_jerk_v085_signal

def f203n_f203_net_income_to_working_capital_momentum_calc086_252d_jerk_v086_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 5.2500)).rolling(24).max().rolling(8).max().rolling(42).var() * 0.832275).diff(7).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc086_252d_jerk_v086_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc086_252d_jerk_v086_signal

def f203n_f203_net_income_to_working_capital_momentum_calc087_200d_jerk_v087_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(35).rolling(27).max().rolling(26).var() * 0.324291).diff(20).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc087_200d_jerk_v087_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc087_200d_jerk_v087_signal

def f203n_f203_net_income_to_working_capital_momentum_calc088_252d_jerk_v088_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.1114)).rolling(16).min().pct_change(23) * 0.754351).diff(20).diff(3).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc088_252d_jerk_v088_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc088_252d_jerk_v088_signal

def f203n_f203_net_income_to_working_capital_momentum_calc089_126d_jerk_v089_signal(netinc, workingcapital):
    res = ((netinc.diff(8) / (workingcapital.shift(4) + 0.7111)).diff(46).diff(29).pct_change(39) * 0.818087).diff(17).diff(17).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc089_126d_jerk_v089_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc089_126d_jerk_v089_signal

def f203n_f203_net_income_to_working_capital_momentum_calc090_5d_jerk_v090_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(32).var().rolling(31).mean() * 0.972436).diff(11).diff(8).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc090_5d_jerk_v090_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc090_5d_jerk_v090_signal

def f203n_f203_net_income_to_working_capital_momentum_calc091_10d_jerk_v091_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 6.3324)).pct_change(23).diff(35) * 0.832690).diff(18).diff(19).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc091_10d_jerk_v091_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc091_10d_jerk_v091_signal

def f203n_f203_net_income_to_working_capital_momentum_calc092_252d_jerk_v092_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(39).rolling(48).var().rolling(39).std().rolling(42).var() * 0.125762).diff(7).diff(8).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc092_252d_jerk_v092_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc092_252d_jerk_v092_signal

def f203n_f203_net_income_to_working_capital_momentum_calc093_105d_jerk_v093_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 2.3242)).rolling(50).max().rolling(12).max().rolling(16).mean() * 0.837806).diff(6).diff(10).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc093_105d_jerk_v093_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc093_105d_jerk_v093_signal

def f203n_f203_net_income_to_working_capital_momentum_calc094_42d_jerk_v094_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(5) + 1.6962)).rolling(44).max().rolling(28).max().rolling(47).max() * 0.298188).diff(10).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc094_42d_jerk_v094_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc094_42d_jerk_v094_signal

def f203n_f203_net_income_to_working_capital_momentum_calc095_126d_jerk_v095_signal(netinc, workingcapital):
    res = ((netinc.diff(3) / (workingcapital.shift(4) + 3.2155)).diff(20).rolling(45).std().rolling(14).var() * 0.894778).diff(10).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc095_126d_jerk_v095_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc095_126d_jerk_v095_signal

def f203n_f203_net_income_to_working_capital_momentum_calc096_126d_jerk_v096_signal(netinc, workingcapital):
    res = ((netinc * 1.2897 - workingcapital).rolling(44).max().rolling(19).var() * 0.928779).diff(8).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc096_126d_jerk_v096_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc096_126d_jerk_v096_signal

def f203n_f203_net_income_to_working_capital_momentum_calc097_10d_jerk_v097_signal(netinc, workingcapital):
    res = ((netinc.diff(9) / (workingcapital.shift(3) + 6.5752)).rolling(43).min().pct_change(30).diff(9).rolling(35).std() * 0.718440).diff(7).diff(6).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc097_10d_jerk_v097_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc097_10d_jerk_v097_signal

def f203n_f203_net_income_to_working_capital_momentum_calc098_42d_jerk_v098_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(15).pct_change(37) * 0.462723).diff(8).diff(2).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc098_42d_jerk_v098_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc098_42d_jerk_v098_signal

def f203n_f203_net_income_to_working_capital_momentum_calc099_126d_jerk_v099_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(33).max().rolling(37).max() * 0.485336).diff(18).diff(12).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc099_126d_jerk_v099_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc099_126d_jerk_v099_signal

def f203n_f203_net_income_to_working_capital_momentum_calc100_126d_jerk_v100_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 3.1414)).rolling(18).max().rolling(17).max().rolling(13).std().rolling(46).var() * 0.356077).diff(9).diff(5).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc100_126d_jerk_v100_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc100_126d_jerk_v100_signal

def f203n_f203_net_income_to_working_capital_momentum_calc101_42d_jerk_v101_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 7.9483)).rolling(24).mean().diff(19) * 0.622747).diff(11).diff(5).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc101_42d_jerk_v101_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc101_42d_jerk_v101_signal

def f203n_f203_net_income_to_working_capital_momentum_calc102_5d_jerk_v102_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(4) + 7.7162)).rolling(22).std().rolling(33).max().rolling(45).min() * 0.754210).diff(14).diff(11).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc102_5d_jerk_v102_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc102_5d_jerk_v102_signal

def f203n_f203_net_income_to_working_capital_momentum_calc103_63d_jerk_v103_signal(netinc, workingcapital):
    res = ((netinc.diff(8) / (workingcapital.shift(4) + 2.6370)).rolling(24).var().diff(40).rolling(37).var().diff(7) * 0.491715).diff(19).diff(19).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc103_63d_jerk_v103_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc103_63d_jerk_v103_signal

def f203n_f203_net_income_to_working_capital_momentum_calc104_21d_jerk_v104_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 3.3561)).rolling(47).var().rolling(23).min().pct_change(11) * 0.473500).diff(6).diff(12).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc104_21d_jerk_v104_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc104_21d_jerk_v104_signal

def f203n_f203_net_income_to_working_capital_momentum_calc105_105d_jerk_v105_signal(netinc, workingcapital):
    res = ((netinc * 6.8281 - workingcapital).rolling(46).min().pct_change(12) * 0.279249).diff(6).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc105_105d_jerk_v105_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc105_105d_jerk_v105_signal

def f203n_f203_net_income_to_working_capital_momentum_calc106_10d_jerk_v106_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.7143)).rolling(46).var().pct_change(22).pct_change(39) * 0.241686).diff(3).diff(9).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc106_10d_jerk_v106_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc106_10d_jerk_v106_signal

def f203n_f203_net_income_to_working_capital_momentum_calc107_252d_jerk_v107_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 4.5651)).rolling(39).min().pct_change(24).rolling(12).mean().rolling(15).min() * 0.485647).diff(19).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc107_252d_jerk_v107_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc107_252d_jerk_v107_signal

def f203n_f203_net_income_to_working_capital_momentum_calc108_252d_jerk_v108_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(27).max().rolling(37).max().pct_change(36).rolling(41).min() * 0.209979).diff(5).diff(20).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc108_252d_jerk_v108_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc108_252d_jerk_v108_signal

def f203n_f203_net_income_to_working_capital_momentum_calc109_126d_jerk_v109_signal(netinc, workingcapital):
    res = ((netinc * 0.3204 - workingcapital).rolling(38).max().pct_change(48) * 0.218648).diff(17).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc109_126d_jerk_v109_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc109_126d_jerk_v109_signal

def f203n_f203_net_income_to_working_capital_momentum_calc110_126d_jerk_v110_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(19).var().diff(16) * 0.700599).diff(12).diff(8).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc110_126d_jerk_v110_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc110_126d_jerk_v110_signal

def f203n_f203_net_income_to_working_capital_momentum_calc111_5d_jerk_v111_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(24).max().pct_change(43) * 0.232077).diff(13).diff(10).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc111_5d_jerk_v111_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc111_5d_jerk_v111_signal

def f203n_f203_net_income_to_working_capital_momentum_calc112_42d_jerk_v112_signal(netinc, workingcapital):
    res = ((netinc.diff(9) / (workingcapital.shift(2) + 5.4571)).diff(21).diff(22).rolling(6).max() * 0.922006).diff(19).diff(7).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc112_42d_jerk_v112_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc112_42d_jerk_v112_signal

def f203n_f203_net_income_to_working_capital_momentum_calc113_10d_jerk_v113_signal(netinc, workingcapital):
    res = ((netinc * 4.3675 - workingcapital).diff(8).pct_change(44).rolling(16).mean() * 0.873208).diff(18).diff(11).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc113_10d_jerk_v113_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc113_10d_jerk_v113_signal

def f203n_f203_net_income_to_working_capital_momentum_calc114_105d_jerk_v114_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 9.7649)).diff(20).rolling(15).var().diff(39).diff(48) * 0.958176).diff(14).diff(6).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc114_105d_jerk_v114_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc114_105d_jerk_v114_signal

def f203n_f203_net_income_to_working_capital_momentum_calc115_150d_jerk_v115_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(5) + 8.4158)).rolling(8).std().rolling(22).max().rolling(18).mean().pct_change(17) * 0.731257).diff(4).diff(5).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc115_150d_jerk_v115_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc115_150d_jerk_v115_signal

def f203n_f203_net_income_to_working_capital_momentum_calc116_126d_jerk_v116_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 3.6045)).rolling(12).max().pct_change(3) * 0.126474).diff(8).diff(2).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc116_126d_jerk_v116_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc116_126d_jerk_v116_signal

def f203n_f203_net_income_to_working_capital_momentum_calc117_126d_jerk_v117_signal(netinc, workingcapital):
    res = ((netinc * 0.8266 - workingcapital).diff(19).rolling(40).min() * 0.367910).diff(13).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc117_126d_jerk_v117_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc117_126d_jerk_v117_signal

def f203n_f203_net_income_to_working_capital_momentum_calc118_252d_jerk_v118_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(4) + 6.1071)).rolling(32).max().rolling(3).mean().rolling(16).std().rolling(45).var() * 0.411081).diff(4).diff(13).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc118_252d_jerk_v118_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc118_252d_jerk_v118_signal

def f203n_f203_net_income_to_working_capital_momentum_calc119_21d_jerk_v119_signal(netinc, workingcapital):
    res = ((netinc.diff(9) / (workingcapital.shift(4) + 7.5314)).rolling(28).std().diff(2).diff(36) * 0.953141).diff(16).diff(13).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc119_21d_jerk_v119_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc119_21d_jerk_v119_signal

def f203n_f203_net_income_to_working_capital_momentum_calc120_5d_jerk_v120_signal(netinc, workingcapital):
    res = ((netinc.diff(10) / (workingcapital.shift(5) + 2.8636)).rolling(49).std().rolling(50).min().pct_change(31).diff(19) * 0.646778).diff(15).diff(6).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc120_5d_jerk_v120_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc120_5d_jerk_v120_signal

def f203n_f203_net_income_to_working_capital_momentum_calc121_63d_jerk_v121_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 7.8997)).rolling(47).var().diff(31).rolling(33).min() * 0.364704).diff(15).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc121_63d_jerk_v121_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc121_63d_jerk_v121_signal

def f203n_f203_net_income_to_working_capital_momentum_calc122_126d_jerk_v122_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.3172)).rolling(32).min().diff(22) * 0.380751).diff(9).diff(4).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc122_126d_jerk_v122_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc122_126d_jerk_v122_signal

def f203n_f203_net_income_to_working_capital_momentum_calc123_10d_jerk_v123_signal(netinc, workingcapital):
    res = ((netinc * 7.3629 - workingcapital).rolling(44).min().rolling(35).max().rolling(33).std() * 0.292927).diff(12).diff(11).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc123_10d_jerk_v123_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc123_10d_jerk_v123_signal

def f203n_f203_net_income_to_working_capital_momentum_calc124_126d_jerk_v124_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.2550)).rolling(11).max().rolling(8).std().rolling(5).min() * 0.531354).diff(8).diff(15).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc124_126d_jerk_v124_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc124_126d_jerk_v124_signal

def f203n_f203_net_income_to_working_capital_momentum_calc125_200d_jerk_v125_signal(netinc, workingcapital):
    res = ((netinc * 0.2726 - workingcapital).rolling(33).min().diff(7) * 0.063646).diff(15).diff(16).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc125_200d_jerk_v125_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc125_200d_jerk_v125_signal

def f203n_f203_net_income_to_working_capital_momentum_calc126_42d_jerk_v126_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(46).max().pct_change(15) * 0.458633).diff(2).diff(19).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc126_42d_jerk_v126_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc126_42d_jerk_v126_signal

def f203n_f203_net_income_to_working_capital_momentum_calc127_200d_jerk_v127_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 0.6783)).rolling(36).max().rolling(40).std() * 0.214176).diff(11).diff(5).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc127_200d_jerk_v127_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc127_200d_jerk_v127_signal

def f203n_f203_net_income_to_working_capital_momentum_calc128_5d_jerk_v128_signal(netinc, workingcapital):
    res = ((netinc * 2.4869 - workingcapital).diff(24).rolling(30).var().rolling(50).std() * 0.277789).diff(19).diff(13).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc128_5d_jerk_v128_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc128_5d_jerk_v128_signal

def f203n_f203_net_income_to_working_capital_momentum_calc129_84d_jerk_v129_signal(netinc, workingcapital):
    res = ((netinc * 8.8499 - workingcapital).pct_change(21).rolling(7).min().rolling(49).std().pct_change(19) * 0.927608).diff(6).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc129_84d_jerk_v129_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc129_84d_jerk_v129_signal

def f203n_f203_net_income_to_working_capital_momentum_calc130_84d_jerk_v130_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 8.1063)).pct_change(2).diff(44).rolling(49).max().rolling(12).var() * 0.814648).diff(19).diff(13).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc130_84d_jerk_v130_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc130_84d_jerk_v130_signal

def f203n_f203_net_income_to_working_capital_momentum_calc131_150d_jerk_v131_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(43).rolling(16).min().diff(30) * 0.096415).diff(8).diff(16).rolling(150).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc131_150d_jerk_v131_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc131_150d_jerk_v131_signal

def f203n_f203_net_income_to_working_capital_momentum_calc132_105d_jerk_v132_signal(netinc, workingcapital):
    res = ((netinc * 4.3177 - workingcapital).rolling(31).min().rolling(33).var().rolling(46).mean() * 0.342674).diff(3).diff(3).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc132_105d_jerk_v132_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc132_105d_jerk_v132_signal

def f203n_f203_net_income_to_working_capital_momentum_calc133_63d_jerk_v133_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 0.1854)).rolling(10).max().diff(32).rolling(30).max().rolling(23).var() * 0.577262).diff(15).diff(17).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc133_63d_jerk_v133_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc133_63d_jerk_v133_signal

def f203n_f203_net_income_to_working_capital_momentum_calc134_5d_jerk_v134_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).pct_change(27).rolling(37).std() * 0.527070).diff(20).diff(18).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc134_5d_jerk_v134_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc134_5d_jerk_v134_signal

def f203n_f203_net_income_to_working_capital_momentum_calc135_84d_jerk_v135_signal(netinc, workingcapital):
    res = ((netinc.diff(6) / (workingcapital.shift(1) + 1.2383)).rolling(13).std().rolling(19).mean() * 0.618955).diff(11).diff(2).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc135_84d_jerk_v135_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc135_84d_jerk_v135_signal

def f203n_f203_net_income_to_working_capital_momentum_calc136_252d_jerk_v136_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(14).max().pct_change(17).pct_change(36).diff(37) * 0.026489).diff(7).diff(9).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc136_252d_jerk_v136_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc136_252d_jerk_v136_signal

def f203n_f203_net_income_to_working_capital_momentum_calc137_21d_jerk_v137_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 9.2354)).rolling(9).max().rolling(12).std() * 0.849228).diff(4).diff(10).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc137_21d_jerk_v137_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc137_21d_jerk_v137_signal

def f203n_f203_net_income_to_working_capital_momentum_calc138_42d_jerk_v138_signal(netinc, workingcapital):
    res = ((netinc.diff(8) / (workingcapital.shift(4) + 9.5273)).rolling(5).mean().rolling(26).std().diff(37) * 0.659325).diff(2).diff(20).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc138_42d_jerk_v138_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc138_42d_jerk_v138_signal

def f203n_f203_net_income_to_working_capital_momentum_calc139_10d_jerk_v139_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 4.6859)).rolling(18).std().rolling(28).min().rolling(20).std() * 0.171902).diff(8).diff(8).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc139_10d_jerk_v139_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc139_10d_jerk_v139_signal

def f203n_f203_net_income_to_working_capital_momentum_calc140_63d_jerk_v140_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 0.4103)).pct_change(28).pct_change(35).rolling(46).var().rolling(24).max() * 0.034990).diff(15).diff(5).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc140_63d_jerk_v140_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc140_63d_jerk_v140_signal

def f203n_f203_net_income_to_working_capital_momentum_calc141_200d_jerk_v141_signal(netinc, workingcapital):
    res = ((netinc.diff(5) / (workingcapital.shift(4) + 9.3215)).rolling(22).mean().rolling(50).min().diff(37) * 0.780069).diff(14).diff(4).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc141_200d_jerk_v141_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc141_200d_jerk_v141_signal

def f203n_f203_net_income_to_working_capital_momentum_calc142_126d_jerk_v142_signal(netinc, workingcapital):
    res = ((netinc.diff(7) / (workingcapital.shift(2) + 1.4521)).rolling(6).max().rolling(45).std().rolling(2).mean().rolling(49).mean() * 0.381750).diff(9).diff(20).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc142_126d_jerk_v142_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc142_126d_jerk_v142_signal

def f203n_f203_net_income_to_working_capital_momentum_calc143_105d_jerk_v143_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(26).std().rolling(9).max() * 0.740097).diff(8).diff(5).rolling(105).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc143_105d_jerk_v143_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc143_105d_jerk_v143_signal

def f203n_f203_net_income_to_working_capital_momentum_calc144_21d_jerk_v144_signal(netinc, workingcapital):
    res = ((workingcapital / (netinc + 9.9279)).rolling(38).mean().diff(24).rolling(39).mean().rolling(48).std() * 0.729029).diff(13).diff(5).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc144_21d_jerk_v144_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc144_21d_jerk_v144_signal

def f203n_f203_net_income_to_working_capital_momentum_calc145_126d_jerk_v145_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 0.3665)).rolling(13).max().rolling(44).min().diff(47) * 0.910520).diff(4).diff(15).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc145_126d_jerk_v145_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc145_126d_jerk_v145_signal

def f203n_f203_net_income_to_working_capital_momentum_calc146_84d_jerk_v146_signal(netinc, workingcapital):
    res = ((netinc.replace(0, np.nan) / workingcapital.replace(0, np.nan)).rolling(17).max().rolling(8).var().rolling(49).var().rolling(10).std() * 0.869077).diff(15).diff(15).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc146_84d_jerk_v146_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc146_84d_jerk_v146_signal

def f203n_f203_net_income_to_working_capital_momentum_calc147_252d_jerk_v147_signal(netinc, workingcapital):
    res = ((netinc * 0.1907 - workingcapital).pct_change(39).rolling(3).min() * 0.331400).diff(15).diff(19).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc147_252d_jerk_v147_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc147_252d_jerk_v147_signal

def f203n_f203_net_income_to_working_capital_momentum_calc148_200d_jerk_v148_signal(netinc, workingcapital):
    res = ((netinc / (workingcapital + 0.4836)).pct_change(6).rolling(27).mean().rolling(46).mean().rolling(5).min() * 0.620682).diff(6).diff(11).rolling(200).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc148_200d_jerk_v148_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc148_200d_jerk_v148_signal

def f203n_f203_net_income_to_working_capital_momentum_calc149_126d_jerk_v149_signal(netinc, workingcapital):
    res = ((netinc * 0.1751 - workingcapital).rolling(29).var().rolling(34).mean().diff(18).rolling(29).std() * 0.656217).diff(8).diff(3).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc149_126d_jerk_v149_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc149_126d_jerk_v149_signal

def f203n_f203_net_income_to_working_capital_momentum_calc150_21d_jerk_v150_signal(netinc, workingcapital):
    res = ((netinc * 5.5984 - workingcapital).rolling(9).std().rolling(41).var().rolling(27).mean() * 0.854055).diff(7).diff(7).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f203n_f203_net_income_to_working_capital_momentum_calc150_21d_jerk_v150_signal'] = f203n_f203_net_income_to_working_capital_momentum_calc150_21d_jerk_v150_signal


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
