import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f213n_f213_net_income_stability_cycles_calc001_63d_slope_v001_signal(netinc, ebitda):
    res = (((((netinc * 60.7034 - ebitda).rolling(28).max()).pct_change(4)) * 0.564308).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc001_63d_slope_v001_signal'] = f213n_f213_net_income_stability_cycles_calc001_63d_slope_v001_signal

def f213n_f213_net_income_stability_cycles_calc002_5d_slope_v002_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(2)).rolling(22).var()).pct_change(15)).pct_change(15)) * 0.75875).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc002_5d_slope_v002_signal'] = f213n_f213_net_income_stability_cycles_calc002_5d_slope_v002_signal

def f213n_f213_net_income_stability_cycles_calc003_252d_slope_v003_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 52.3243)).diff(11)).rolling(11).mean()) * 0.931393).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc003_252d_slope_v003_signal'] = f213n_f213_net_income_stability_cycles_calc003_252d_slope_v003_signal

def f213n_f213_net_income_stability_cycles_calc004_252d_slope_v004_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 2.9346)).rolling(27).min()).rolling(12).mean()).rolling(24).min()) * 0.457491).diff(9).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc004_252d_slope_v004_signal'] = f213n_f213_net_income_stability_cycles_calc004_252d_slope_v004_signal

def f213n_f213_net_income_stability_cycles_calc005_252d_slope_v005_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 79.3847)).pct_change(3)).rolling(13).var()).rolling(19).max()) * 0.215193).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc005_252d_slope_v005_signal'] = f213n_f213_net_income_stability_cycles_calc005_252d_slope_v005_signal

def f213n_f213_net_income_stability_cycles_calc006_21d_slope_v006_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).std()).rolling(8).min()).rolling(29).var()).diff(16)) * 0.109272).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc006_21d_slope_v006_signal'] = f213n_f213_net_income_stability_cycles_calc006_21d_slope_v006_signal

def f213n_f213_net_income_stability_cycles_calc007_21d_slope_v007_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 80.6092)).rolling(11).max()).rolling(24).max()) * 0.887865).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc007_21d_slope_v007_signal'] = f213n_f213_net_income_stability_cycles_calc007_21d_slope_v007_signal

def f213n_f213_net_income_stability_cycles_calc008_21d_slope_v008_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 75.7014)).diff(20)).diff(13)) * 0.537489).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc008_21d_slope_v008_signal'] = f213n_f213_net_income_stability_cycles_calc008_21d_slope_v008_signal

def f213n_f213_net_income_stability_cycles_calc009_10d_slope_v009_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(13) / ebitda.pct_change(4)).rolling(20).max()).rolling(12).mean()).rolling(16).std()) * 0.532171).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc009_10d_slope_v009_signal'] = f213n_f213_net_income_stability_cycles_calc009_10d_slope_v009_signal

def f213n_f213_net_income_stability_cycles_calc010_10d_slope_v010_signal(netinc, ebitda):
    res = (((((netinc.pct_change(16) / ebitda.pct_change(8)).rolling(30).std()).rolling(16).std()) * 0.664171).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc010_10d_slope_v010_signal'] = f213n_f213_net_income_stability_cycles_calc010_10d_slope_v010_signal

def f213n_f213_net_income_stability_cycles_calc011_10d_slope_v011_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(20).max()).rolling(15).std()).rolling(29).std()).rolling(20).max()) * 0.248807).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc011_10d_slope_v011_signal'] = f213n_f213_net_income_stability_cycles_calc011_10d_slope_v011_signal

def f213n_f213_net_income_stability_cycles_calc012_126d_slope_v012_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(30).var()).rolling(12).std()).rolling(13).max()) * 0.894296).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc012_126d_slope_v012_signal'] = f213n_f213_net_income_stability_cycles_calc012_126d_slope_v012_signal

def f213n_f213_net_income_stability_cycles_calc013_126d_slope_v013_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 13.5358)).diff(16)).rolling(12).max()).rolling(27).mean()).pct_change(20)) * 0.852746).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc013_126d_slope_v013_signal'] = f213n_f213_net_income_stability_cycles_calc013_126d_slope_v013_signal

def f213n_f213_net_income_stability_cycles_calc014_126d_slope_v014_signal(netinc, ebitda):
    res = (((((netinc * 34.8994 - ebitda).rolling(21).min()).rolling(17).min()) * 0.698102).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc014_126d_slope_v014_signal'] = f213n_f213_net_income_stability_cycles_calc014_126d_slope_v014_signal

def f213n_f213_net_income_stability_cycles_calc015_42d_slope_v015_signal(netinc, ebitda):
    res = (((((netinc.pct_change(15) / ebitda.pct_change(18)).rolling(17).var()).pct_change(5)) * 0.985873).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc015_42d_slope_v015_signal'] = f213n_f213_net_income_stability_cycles_calc015_42d_slope_v015_signal

def f213n_f213_net_income_stability_cycles_calc016_126d_slope_v016_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(9) / ebitda.pct_change(1)).rolling(15).min()).diff(5)).rolling(8).min()).diff(15)) * 0.94564).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc016_126d_slope_v016_signal'] = f213n_f213_net_income_stability_cycles_calc016_126d_slope_v016_signal

def f213n_f213_net_income_stability_cycles_calc017_63d_slope_v017_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 69.7509)).diff(19)).rolling(29).var()).rolling(21).mean()).rolling(24).mean()) * 0.308568).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc017_63d_slope_v017_signal'] = f213n_f213_net_income_stability_cycles_calc017_63d_slope_v017_signal

def f213n_f213_net_income_stability_cycles_calc018_63d_slope_v018_signal(netinc, ebitda):
    res = (((((netinc.pct_change(17) / ebitda.pct_change(14)).diff(7)).rolling(21).std()) * 0.967807).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc018_63d_slope_v018_signal'] = f213n_f213_net_income_stability_cycles_calc018_63d_slope_v018_signal

def f213n_f213_net_income_stability_cycles_calc019_252d_slope_v019_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 18.2057)).rolling(24).max()).diff(13)).pct_change(14)) * 0.646419).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc019_252d_slope_v019_signal'] = f213n_f213_net_income_stability_cycles_calc019_252d_slope_v019_signal

def f213n_f213_net_income_stability_cycles_calc020_126d_slope_v020_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 47.4933)).rolling(30).min()).rolling(17).var()).rolling(7).mean()).rolling(14).var()) * 0.84032).diff(7).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc020_126d_slope_v020_signal'] = f213n_f213_net_income_stability_cycles_calc020_126d_slope_v020_signal

def f213n_f213_net_income_stability_cycles_calc021_10d_slope_v021_signal(netinc, ebitda):
    res = ((((((netinc * 35.1849 - ebitda).rolling(30).mean()).rolling(3).max()).rolling(3).max()) * 0.644281).diff(12).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc021_10d_slope_v021_signal'] = f213n_f213_net_income_stability_cycles_calc021_10d_slope_v021_signal

def f213n_f213_net_income_stability_cycles_calc022_5d_slope_v022_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(27).mean()).rolling(20).max()).rolling(29).var()) * 0.954328).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc022_5d_slope_v022_signal'] = f213n_f213_net_income_stability_cycles_calc022_5d_slope_v022_signal

def f213n_f213_net_income_stability_cycles_calc023_10d_slope_v023_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 18.9294)).rolling(21).std()).rolling(20).var()).rolling(30).std()).rolling(24).min()) * 0.618455).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc023_10d_slope_v023_signal'] = f213n_f213_net_income_stability_cycles_calc023_10d_slope_v023_signal

def f213n_f213_net_income_stability_cycles_calc024_63d_slope_v024_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 14.9701)).rolling(5).var()).rolling(23).var()).rolling(20).std()) * 0.812616).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc024_63d_slope_v024_signal'] = f213n_f213_net_income_stability_cycles_calc024_63d_slope_v024_signal

def f213n_f213_net_income_stability_cycles_calc025_10d_slope_v025_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(28).max()).rolling(27).min()).rolling(5).min()).diff(18)) * 0.497698).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc025_10d_slope_v025_signal'] = f213n_f213_net_income_stability_cycles_calc025_10d_slope_v025_signal

def f213n_f213_net_income_stability_cycles_calc026_21d_slope_v026_signal(netinc, ebitda):
    res = (((((netinc.diff(16) / (ebitda.shift(4) + 24.6976)).rolling(27).min()).pct_change(19)) * 0.148554).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc026_21d_slope_v026_signal'] = f213n_f213_net_income_stability_cycles_calc026_21d_slope_v026_signal

def f213n_f213_net_income_stability_cycles_calc027_252d_slope_v027_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(19) / ebitda.pct_change(19)).rolling(14).max()).pct_change(18)).diff(7)).rolling(12).var()) * 0.660242).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc027_252d_slope_v027_signal'] = f213n_f213_net_income_stability_cycles_calc027_252d_slope_v027_signal

def f213n_f213_net_income_stability_cycles_calc028_42d_slope_v028_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 76.3759)).rolling(17).mean()).rolling(12).mean()).rolling(17).max()) * 0.2971).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc028_42d_slope_v028_signal'] = f213n_f213_net_income_stability_cycles_calc028_42d_slope_v028_signal

def f213n_f213_net_income_stability_cycles_calc029_42d_slope_v029_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 30.6592)).rolling(30).var()).rolling(25).max()) * 0.982442).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc029_42d_slope_v029_signal'] = f213n_f213_net_income_stability_cycles_calc029_42d_slope_v029_signal

def f213n_f213_net_income_stability_cycles_calc030_63d_slope_v030_signal(netinc, ebitda):
    res = ((((((netinc.diff(2) / (ebitda.shift(9) + 17.4185)).rolling(13).std()).rolling(3).max()).pct_change(14)) * 0.317381).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc030_63d_slope_v030_signal'] = f213n_f213_net_income_stability_cycles_calc030_63d_slope_v030_signal

def f213n_f213_net_income_stability_cycles_calc031_63d_slope_v031_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 84.9372)).diff(11)).rolling(24).mean()) * 0.508571).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc031_63d_slope_v031_signal'] = f213n_f213_net_income_stability_cycles_calc031_63d_slope_v031_signal

def f213n_f213_net_income_stability_cycles_calc032_42d_slope_v032_signal(netinc, ebitda):
    res = (((((netinc.pct_change(13) / ebitda.pct_change(7)).rolling(2).var()).rolling(23).std()) * 0.637613).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc032_42d_slope_v032_signal'] = f213n_f213_net_income_stability_cycles_calc032_42d_slope_v032_signal

def f213n_f213_net_income_stability_cycles_calc033_10d_slope_v033_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 98.7098)).rolling(21).std()).diff(9)).rolling(23).min()).rolling(24).max()) * 0.820041).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc033_10d_slope_v033_signal'] = f213n_f213_net_income_stability_cycles_calc033_10d_slope_v033_signal

def f213n_f213_net_income_stability_cycles_calc034_10d_slope_v034_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(28).var()).rolling(28).std()).pct_change(16)) * 0.65027).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc034_10d_slope_v034_signal'] = f213n_f213_net_income_stability_cycles_calc034_10d_slope_v034_signal

def f213n_f213_net_income_stability_cycles_calc035_63d_slope_v035_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 1.1419)).rolling(5).mean()).rolling(30).std()).pct_change(16)).rolling(7).mean()) * 0.688673).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc035_63d_slope_v035_signal'] = f213n_f213_net_income_stability_cycles_calc035_63d_slope_v035_signal

def f213n_f213_net_income_stability_cycles_calc036_21d_slope_v036_signal(netinc, ebitda):
    res = (((((((netinc.diff(13) / (ebitda.shift(5) + 16.8199)).rolling(5).var()).pct_change(4)).rolling(28).min()).rolling(4).std()) * 0.735291).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc036_21d_slope_v036_signal'] = f213n_f213_net_income_stability_cycles_calc036_21d_slope_v036_signal

def f213n_f213_net_income_stability_cycles_calc037_252d_slope_v037_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 49.8469)).rolling(28).mean()).rolling(7).min()) * 0.134573).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc037_252d_slope_v037_signal'] = f213n_f213_net_income_stability_cycles_calc037_252d_slope_v037_signal

def f213n_f213_net_income_stability_cycles_calc038_252d_slope_v038_signal(netinc, ebitda):
    res = (((((netinc.pct_change(12) / ebitda.pct_change(15)).rolling(21).min()).pct_change(2)) * 0.076052).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc038_252d_slope_v038_signal'] = f213n_f213_net_income_stability_cycles_calc038_252d_slope_v038_signal

def f213n_f213_net_income_stability_cycles_calc039_252d_slope_v039_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 97.4533)).pct_change(9)).rolling(13).std()).rolling(8).min()) * 0.763178).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc039_252d_slope_v039_signal'] = f213n_f213_net_income_stability_cycles_calc039_252d_slope_v039_signal

def f213n_f213_net_income_stability_cycles_calc040_42d_slope_v040_signal(netinc, ebitda):
    res = (((((netinc.pct_change(8) / ebitda.pct_change(6)).rolling(23).var()).diff(15)) * 0.937885).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc040_42d_slope_v040_signal'] = f213n_f213_net_income_stability_cycles_calc040_42d_slope_v040_signal

def f213n_f213_net_income_stability_cycles_calc041_252d_slope_v041_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 44.109)).rolling(12).max()).rolling(5).mean()) * 0.836554).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc041_252d_slope_v041_signal'] = f213n_f213_net_income_stability_cycles_calc041_252d_slope_v041_signal

def f213n_f213_net_income_stability_cycles_calc042_42d_slope_v042_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 51.8529)).diff(8)).rolling(14).mean()) * 0.027113).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc042_42d_slope_v042_signal'] = f213n_f213_net_income_stability_cycles_calc042_42d_slope_v042_signal

def f213n_f213_net_income_stability_cycles_calc043_63d_slope_v043_signal(netinc, ebitda):
    res = (((((((netinc * 5.9359 - ebitda).rolling(2).mean()).diff(16)).rolling(22).max()).rolling(11).min()) * 0.389777).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc043_63d_slope_v043_signal'] = f213n_f213_net_income_stability_cycles_calc043_63d_slope_v043_signal

def f213n_f213_net_income_stability_cycles_calc044_42d_slope_v044_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(9) / ebitda.pct_change(12)).rolling(30).min()).rolling(16).std()).rolling(30).max()) * 0.743108).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc044_42d_slope_v044_signal'] = f213n_f213_net_income_stability_cycles_calc044_42d_slope_v044_signal

def f213n_f213_net_income_stability_cycles_calc045_10d_slope_v045_signal(netinc, ebitda):
    res = (((((((netinc.diff(6) / (ebitda.shift(7) + 14.5263)).rolling(15).mean()).pct_change(10)).rolling(3).std()).rolling(15).min()) * 0.634351).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc045_10d_slope_v045_signal'] = f213n_f213_net_income_stability_cycles_calc045_10d_slope_v045_signal

def f213n_f213_net_income_stability_cycles_calc046_252d_slope_v046_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(15)).rolling(14).min()).rolling(13).min()) * 0.404186).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc046_252d_slope_v046_signal'] = f213n_f213_net_income_stability_cycles_calc046_252d_slope_v046_signal

def f213n_f213_net_income_stability_cycles_calc047_21d_slope_v047_signal(netinc, ebitda):
    res = (((((netinc.pct_change(8) / ebitda.pct_change(7)).rolling(8).max()).pct_change(20)) * 0.140452).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc047_21d_slope_v047_signal'] = f213n_f213_net_income_stability_cycles_calc047_21d_slope_v047_signal

def f213n_f213_net_income_stability_cycles_calc048_42d_slope_v048_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(5).min()).rolling(22).max()) * 0.758697).diff(15).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc048_42d_slope_v048_signal'] = f213n_f213_net_income_stability_cycles_calc048_42d_slope_v048_signal

def f213n_f213_net_income_stability_cycles_calc049_21d_slope_v049_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 90.4771)).rolling(30).max()).rolling(23).std()).rolling(18).min()) * 0.946618).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc049_21d_slope_v049_signal'] = f213n_f213_net_income_stability_cycles_calc049_21d_slope_v049_signal

def f213n_f213_net_income_stability_cycles_calc050_10d_slope_v050_signal(netinc, ebitda):
    res = (((((((netinc.diff(7) / (ebitda.shift(7) + 94.3256)).diff(19)).pct_change(5)).diff(13)).rolling(27).max()) * 0.033359).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc050_10d_slope_v050_signal'] = f213n_f213_net_income_stability_cycles_calc050_10d_slope_v050_signal

def f213n_f213_net_income_stability_cycles_calc051_10d_slope_v051_signal(netinc, ebitda):
    res = (((((((netinc * 41.1878 - ebitda).diff(2)).diff(4)).pct_change(3)).rolling(2).mean()) * 0.469208).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc051_10d_slope_v051_signal'] = f213n_f213_net_income_stability_cycles_calc051_10d_slope_v051_signal

def f213n_f213_net_income_stability_cycles_calc052_252d_slope_v052_signal(netinc, ebitda):
    res = (((((netinc.pct_change(12) / ebitda.pct_change(7)).rolling(11).std()).pct_change(3)) * 0.334878).diff(12).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc052_252d_slope_v052_signal'] = f213n_f213_net_income_stability_cycles_calc052_252d_slope_v052_signal

def f213n_f213_net_income_stability_cycles_calc053_63d_slope_v053_signal(netinc, ebitda):
    res = ((((((netinc.diff(15) / (ebitda.shift(8) + 90.9336)).rolling(27).mean()).rolling(7).max()).rolling(7).std()) * 0.58178).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc053_63d_slope_v053_signal'] = f213n_f213_net_income_stability_cycles_calc053_63d_slope_v053_signal

def f213n_f213_net_income_stability_cycles_calc054_5d_slope_v054_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(18) / ebitda.pct_change(16)).diff(8)).rolling(23).mean()).rolling(16).std()) * 0.615923).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc054_5d_slope_v054_signal'] = f213n_f213_net_income_stability_cycles_calc054_5d_slope_v054_signal

def f213n_f213_net_income_stability_cycles_calc055_252d_slope_v055_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 4.0339)).diff(12)).rolling(20).min()).rolling(7).max()).rolling(30).min()) * 0.872627).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc055_252d_slope_v055_signal'] = f213n_f213_net_income_stability_cycles_calc055_252d_slope_v055_signal

def f213n_f213_net_income_stability_cycles_calc056_42d_slope_v056_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 94.6657)).rolling(11).max()).diff(13)) * 0.565447).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc056_42d_slope_v056_signal'] = f213n_f213_net_income_stability_cycles_calc056_42d_slope_v056_signal

def f213n_f213_net_income_stability_cycles_calc057_5d_slope_v057_signal(netinc, ebitda):
    res = (((((((netinc.diff(7) / (ebitda.shift(6) + 99.2904)).pct_change(16)).rolling(21).mean()).rolling(15).max()).rolling(13).std()) * 0.785148).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc057_5d_slope_v057_signal'] = f213n_f213_net_income_stability_cycles_calc057_5d_slope_v057_signal

def f213n_f213_net_income_stability_cycles_calc058_10d_slope_v058_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 51.3909)).rolling(24).std()).rolling(10).var()).rolling(15).min()).rolling(3).var()) * 0.972396).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc058_10d_slope_v058_signal'] = f213n_f213_net_income_stability_cycles_calc058_10d_slope_v058_signal

def f213n_f213_net_income_stability_cycles_calc059_126d_slope_v059_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 99.5102)).rolling(25).mean()).rolling(2).max()).rolling(14).var()).rolling(30).std()) * 0.65356).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc059_126d_slope_v059_signal'] = f213n_f213_net_income_stability_cycles_calc059_126d_slope_v059_signal

def f213n_f213_net_income_stability_cycles_calc060_42d_slope_v060_signal(netinc, ebitda):
    res = ((((((netinc * 38.9009 - ebitda).rolling(24).min()).rolling(6).var()).rolling(25).var()) * 0.691383).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc060_42d_slope_v060_signal'] = f213n_f213_net_income_stability_cycles_calc060_42d_slope_v060_signal

def f213n_f213_net_income_stability_cycles_calc061_63d_slope_v061_signal(netinc, ebitda):
    res = (((((netinc * 19.3711 - ebitda).rolling(27).mean()).rolling(27).std()) * 0.286008).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc061_63d_slope_v061_signal'] = f213n_f213_net_income_stability_cycles_calc061_63d_slope_v061_signal

def f213n_f213_net_income_stability_cycles_calc062_10d_slope_v062_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 7.534)).diff(1)).diff(11)) * 0.375921).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc062_10d_slope_v062_signal'] = f213n_f213_net_income_stability_cycles_calc062_10d_slope_v062_signal

def f213n_f213_net_income_stability_cycles_calc063_5d_slope_v063_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 15.7088)).diff(5)).rolling(25).std()) * 0.623604).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc063_5d_slope_v063_signal'] = f213n_f213_net_income_stability_cycles_calc063_5d_slope_v063_signal

def f213n_f213_net_income_stability_cycles_calc064_10d_slope_v064_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 9.2612)).rolling(14).mean()).rolling(22).var()).rolling(8).max()).rolling(28).min()) * 0.942364).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc064_10d_slope_v064_signal'] = f213n_f213_net_income_stability_cycles_calc064_10d_slope_v064_signal

def f213n_f213_net_income_stability_cycles_calc065_126d_slope_v065_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 98.7942)).rolling(18).std()).rolling(4).mean()).rolling(8).std()) * 0.603349).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc065_126d_slope_v065_signal'] = f213n_f213_net_income_stability_cycles_calc065_126d_slope_v065_signal

def f213n_f213_net_income_stability_cycles_calc066_10d_slope_v066_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 87.8298)).pct_change(8)).rolling(14).std()).diff(19)) * 0.573925).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc066_10d_slope_v066_signal'] = f213n_f213_net_income_stability_cycles_calc066_10d_slope_v066_signal

def f213n_f213_net_income_stability_cycles_calc067_63d_slope_v067_signal(netinc, ebitda):
    res = (((((netinc.pct_change(9) / ebitda.pct_change(12)).rolling(2).max()).diff(9)) * 0.637783).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc067_63d_slope_v067_signal'] = f213n_f213_net_income_stability_cycles_calc067_63d_slope_v067_signal

def f213n_f213_net_income_stability_cycles_calc068_252d_slope_v068_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(15)).rolling(25).mean()) * 0.070387).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc068_252d_slope_v068_signal'] = f213n_f213_net_income_stability_cycles_calc068_252d_slope_v068_signal

def f213n_f213_net_income_stability_cycles_calc069_21d_slope_v069_signal(netinc, ebitda):
    res = (((((((netinc.diff(12) / (ebitda.shift(10) + 58.855)).pct_change(11)).rolling(13).min()).diff(16)).rolling(17).var()) * 0.908007).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc069_21d_slope_v069_signal'] = f213n_f213_net_income_stability_cycles_calc069_21d_slope_v069_signal

def f213n_f213_net_income_stability_cycles_calc070_252d_slope_v070_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 48.9598)).rolling(15).var()).rolling(30).min()).rolling(12).min()).pct_change(13)) * 0.544999).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc070_252d_slope_v070_signal'] = f213n_f213_net_income_stability_cycles_calc070_252d_slope_v070_signal

def f213n_f213_net_income_stability_cycles_calc071_252d_slope_v071_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 89.919)).rolling(29).min()).diff(5)).rolling(13).min()) * 0.453133).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc071_252d_slope_v071_signal'] = f213n_f213_net_income_stability_cycles_calc071_252d_slope_v071_signal

def f213n_f213_net_income_stability_cycles_calc072_42d_slope_v072_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 79.1584)).rolling(14).mean()).rolling(6).min()) * 0.658537).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc072_42d_slope_v072_signal'] = f213n_f213_net_income_stability_cycles_calc072_42d_slope_v072_signal

def f213n_f213_net_income_stability_cycles_calc073_21d_slope_v073_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 19.8559)).rolling(21).min()).diff(16)) * 0.497376).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc073_21d_slope_v073_signal'] = f213n_f213_net_income_stability_cycles_calc073_21d_slope_v073_signal

def f213n_f213_net_income_stability_cycles_calc074_42d_slope_v074_signal(netinc, ebitda):
    res = (((((((netinc.diff(2) / (ebitda.shift(6) + 94.7384)).rolling(21).min()).rolling(6).var()).rolling(18).std()).rolling(27).min()) * 0.166624).diff(7).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc074_42d_slope_v074_signal'] = f213n_f213_net_income_stability_cycles_calc074_42d_slope_v074_signal

def f213n_f213_net_income_stability_cycles_calc075_42d_slope_v075_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).mean()).rolling(18).std()).rolling(12).var()).diff(12)) * 0.94772).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc075_42d_slope_v075_signal'] = f213n_f213_net_income_stability_cycles_calc075_42d_slope_v075_signal

def f213n_f213_net_income_stability_cycles_calc076_21d_slope_v076_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 56.5762)).rolling(24).var()).rolling(29).std()) * 0.474053).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc076_21d_slope_v076_signal'] = f213n_f213_net_income_stability_cycles_calc076_21d_slope_v076_signal

def f213n_f213_net_income_stability_cycles_calc077_126d_slope_v077_signal(netinc, ebitda):
    res = (((((((netinc.diff(9) / (ebitda.shift(9) + 91.5822)).rolling(30).std()).rolling(12).std()).pct_change(19)).rolling(24).std()) * 0.963077).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc077_126d_slope_v077_signal'] = f213n_f213_net_income_stability_cycles_calc077_126d_slope_v077_signal

def f213n_f213_net_income_stability_cycles_calc078_63d_slope_v078_signal(netinc, ebitda):
    res = (((((((netinc.diff(16) / (ebitda.shift(10) + 23.7781)).rolling(14).mean()).pct_change(5)).rolling(12).max()).rolling(18).mean()) * 0.813264).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc078_63d_slope_v078_signal'] = f213n_f213_net_income_stability_cycles_calc078_63d_slope_v078_signal

def f213n_f213_net_income_stability_cycles_calc079_42d_slope_v079_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 60.2997)).diff(5)).rolling(29).var()).pct_change(2)) * 0.883092).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc079_42d_slope_v079_signal'] = f213n_f213_net_income_stability_cycles_calc079_42d_slope_v079_signal

def f213n_f213_net_income_stability_cycles_calc080_10d_slope_v080_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 22.411)).rolling(17).var()).rolling(21).var()).rolling(8).max()) * 0.012992).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc080_10d_slope_v080_signal'] = f213n_f213_net_income_stability_cycles_calc080_10d_slope_v080_signal

def f213n_f213_net_income_stability_cycles_calc081_63d_slope_v081_signal(netinc, ebitda):
    res = (((((netinc.diff(2) / (ebitda.shift(4) + 60.5476)).pct_change(13)).rolling(24).min()) * 0.299707).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc081_63d_slope_v081_signal'] = f213n_f213_net_income_stability_cycles_calc081_63d_slope_v081_signal

def f213n_f213_net_income_stability_cycles_calc082_21d_slope_v082_signal(netinc, ebitda):
    res = ((((((netinc.diff(1) / (ebitda.shift(1) + 26.1727)).pct_change(5)).rolling(22).min()).rolling(19).min()) * 0.151178).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc082_21d_slope_v082_signal'] = f213n_f213_net_income_stability_cycles_calc082_21d_slope_v082_signal

def f213n_f213_net_income_stability_cycles_calc083_63d_slope_v083_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(9) / ebitda.pct_change(7)).rolling(11).min()).rolling(20).std()).rolling(12).std()).rolling(5).mean()) * 0.317805).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc083_63d_slope_v083_signal'] = f213n_f213_net_income_stability_cycles_calc083_63d_slope_v083_signal

def f213n_f213_net_income_stability_cycles_calc084_252d_slope_v084_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 32.7211)).rolling(22).min()).rolling(14).var()).rolling(12).std()).rolling(28).max()) * 0.477559).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc084_252d_slope_v084_signal'] = f213n_f213_net_income_stability_cycles_calc084_252d_slope_v084_signal

def f213n_f213_net_income_stability_cycles_calc085_126d_slope_v085_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(17) / ebitda.pct_change(2)).diff(5)).rolling(4).min()).rolling(6).mean()).rolling(5).std()) * 0.564305).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc085_126d_slope_v085_signal'] = f213n_f213_net_income_stability_cycles_calc085_126d_slope_v085_signal

def f213n_f213_net_income_stability_cycles_calc086_10d_slope_v086_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(3)).rolling(14).min()).rolling(3).max()) * 0.240313).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc086_10d_slope_v086_signal'] = f213n_f213_net_income_stability_cycles_calc086_10d_slope_v086_signal

def f213n_f213_net_income_stability_cycles_calc087_42d_slope_v087_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).mean()).pct_change(9)) * 0.39807).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc087_42d_slope_v087_signal'] = f213n_f213_net_income_stability_cycles_calc087_42d_slope_v087_signal

def f213n_f213_net_income_stability_cycles_calc088_10d_slope_v088_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 5.7458)).rolling(26).std()).rolling(6).std()) * 0.679851).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc088_10d_slope_v088_signal'] = f213n_f213_net_income_stability_cycles_calc088_10d_slope_v088_signal

def f213n_f213_net_income_stability_cycles_calc089_63d_slope_v089_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(14)).rolling(4).max()) * 0.389775).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc089_63d_slope_v089_signal'] = f213n_f213_net_income_stability_cycles_calc089_63d_slope_v089_signal

def f213n_f213_net_income_stability_cycles_calc090_10d_slope_v090_signal(netinc, ebitda):
    res = (((((netinc.pct_change(1) / ebitda.pct_change(12)).rolling(30).max()).rolling(18).var()) * 0.21466).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc090_10d_slope_v090_signal'] = f213n_f213_net_income_stability_cycles_calc090_10d_slope_v090_signal

def f213n_f213_net_income_stability_cycles_calc091_42d_slope_v091_signal(netinc, ebitda):
    res = (((((((netinc.diff(20) / (ebitda.shift(5) + 21.3566)).rolling(7).min()).pct_change(7)).pct_change(20)).rolling(12).var()) * 0.535505).diff(7).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc091_42d_slope_v091_signal'] = f213n_f213_net_income_stability_cycles_calc091_42d_slope_v091_signal

def f213n_f213_net_income_stability_cycles_calc092_21d_slope_v092_signal(netinc, ebitda):
    res = (((((((netinc * 89.803 - ebitda).diff(17)).pct_change(13)).rolling(7).std()).rolling(3).mean()) * 0.39478).diff(13).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc092_21d_slope_v092_signal'] = f213n_f213_net_income_stability_cycles_calc092_21d_slope_v092_signal

def f213n_f213_net_income_stability_cycles_calc093_252d_slope_v093_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(19) / ebitda.pct_change(10)).rolling(30).std()).rolling(28).max()).rolling(13).var()).rolling(3).min()) * 0.924422).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc093_252d_slope_v093_signal'] = f213n_f213_net_income_stability_cycles_calc093_252d_slope_v093_signal

def f213n_f213_net_income_stability_cycles_calc094_63d_slope_v094_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 89.0316)).pct_change(6)).pct_change(11)) * 0.836691).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc094_63d_slope_v094_signal'] = f213n_f213_net_income_stability_cycles_calc094_63d_slope_v094_signal

def f213n_f213_net_income_stability_cycles_calc095_42d_slope_v095_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 94.6848)).rolling(19).min()).rolling(11).max()).pct_change(8)) * 0.3908).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc095_42d_slope_v095_signal'] = f213n_f213_net_income_stability_cycles_calc095_42d_slope_v095_signal

def f213n_f213_net_income_stability_cycles_calc096_63d_slope_v096_signal(netinc, ebitda):
    res = (((((netinc.diff(1) / (ebitda.shift(10) + 10.8154)).rolling(16).var()).rolling(25).min()) * 0.010265).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc096_63d_slope_v096_signal'] = f213n_f213_net_income_stability_cycles_calc096_63d_slope_v096_signal

def f213n_f213_net_income_stability_cycles_calc097_10d_slope_v097_signal(netinc, ebitda):
    res = ((((((netinc.diff(7) / (ebitda.shift(7) + 9.8135)).diff(1)).rolling(26).var()).rolling(30).mean()) * 0.370689).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc097_10d_slope_v097_signal'] = f213n_f213_net_income_stability_cycles_calc097_10d_slope_v097_signal

def f213n_f213_net_income_stability_cycles_calc098_21d_slope_v098_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 14.2696)).rolling(4).mean()).diff(8)) * 0.457789).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc098_21d_slope_v098_signal'] = f213n_f213_net_income_stability_cycles_calc098_21d_slope_v098_signal

def f213n_f213_net_income_stability_cycles_calc099_252d_slope_v099_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(5)).rolling(4).std()) * 0.69102).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc099_252d_slope_v099_signal'] = f213n_f213_net_income_stability_cycles_calc099_252d_slope_v099_signal

def f213n_f213_net_income_stability_cycles_calc100_126d_slope_v100_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 37.8048)).rolling(23).mean()).rolling(26).mean()).rolling(24).var()).rolling(25).var()) * 0.046418).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc100_126d_slope_v100_signal'] = f213n_f213_net_income_stability_cycles_calc100_126d_slope_v100_signal

def f213n_f213_net_income_stability_cycles_calc101_10d_slope_v101_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 80.2139)).rolling(29).mean()).rolling(28).max()).pct_change(14)).rolling(24).max()) * 0.033925).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc101_10d_slope_v101_signal'] = f213n_f213_net_income_stability_cycles_calc101_10d_slope_v101_signal

def f213n_f213_net_income_stability_cycles_calc102_252d_slope_v102_signal(netinc, ebitda):
    res = ((((((netinc * 23.2289 - ebitda).rolling(28).min()).rolling(19).min()).rolling(13).std()) * 0.841487).diff(12).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc102_252d_slope_v102_signal'] = f213n_f213_net_income_stability_cycles_calc102_252d_slope_v102_signal

def f213n_f213_net_income_stability_cycles_calc103_126d_slope_v103_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(13).min()).pct_change(10)).rolling(28).std()) * 0.152782).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc103_126d_slope_v103_signal'] = f213n_f213_net_income_stability_cycles_calc103_126d_slope_v103_signal

def f213n_f213_net_income_stability_cycles_calc104_126d_slope_v104_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 54.2726)).rolling(22).var()).rolling(16).min()).pct_change(18)) * 0.363122).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc104_126d_slope_v104_signal'] = f213n_f213_net_income_stability_cycles_calc104_126d_slope_v104_signal

def f213n_f213_net_income_stability_cycles_calc105_5d_slope_v105_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(11) / ebitda.pct_change(18)).rolling(29).std()).pct_change(19)).rolling(28).std()).pct_change(7)) * 0.909933).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc105_5d_slope_v105_signal'] = f213n_f213_net_income_stability_cycles_calc105_5d_slope_v105_signal

def f213n_f213_net_income_stability_cycles_calc106_5d_slope_v106_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 82.362)).rolling(10).mean()).rolling(23).max()).rolling(25).std()).rolling(23).std()) * 0.873109).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc106_5d_slope_v106_signal'] = f213n_f213_net_income_stability_cycles_calc106_5d_slope_v106_signal

def f213n_f213_net_income_stability_cycles_calc107_42d_slope_v107_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(13) / ebitda.pct_change(17)).rolling(20).std()).rolling(25).var()).rolling(24).min()) * 0.727218).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc107_42d_slope_v107_signal'] = f213n_f213_net_income_stability_cycles_calc107_42d_slope_v107_signal

def f213n_f213_net_income_stability_cycles_calc108_10d_slope_v108_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(24).mean()).rolling(9).var()) * 0.454581).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc108_10d_slope_v108_signal'] = f213n_f213_net_income_stability_cycles_calc108_10d_slope_v108_signal

def f213n_f213_net_income_stability_cycles_calc109_21d_slope_v109_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 82.5407)).rolling(8).mean()).rolling(28).std()).pct_change(3)) * 0.541128).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc109_21d_slope_v109_signal'] = f213n_f213_net_income_stability_cycles_calc109_21d_slope_v109_signal

def f213n_f213_net_income_stability_cycles_calc110_21d_slope_v110_signal(netinc, ebitda):
    res = ((((((netinc.diff(12) / (ebitda.shift(7) + 45.3147)).rolling(13).min()).rolling(11).std()).rolling(21).min()) * 0.126574).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc110_21d_slope_v110_signal'] = f213n_f213_net_income_stability_cycles_calc110_21d_slope_v110_signal

def f213n_f213_net_income_stability_cycles_calc111_42d_slope_v111_signal(netinc, ebitda):
    res = (((((netinc.diff(16) / (ebitda.shift(1) + 63.5584)).rolling(24).var()).rolling(29).min()) * 0.591469).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc111_42d_slope_v111_signal'] = f213n_f213_net_income_stability_cycles_calc111_42d_slope_v111_signal

def f213n_f213_net_income_stability_cycles_calc112_252d_slope_v112_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 53.9478)).rolling(17).mean()).pct_change(3)).rolling(10).min()) * 0.106047).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc112_252d_slope_v112_signal'] = f213n_f213_net_income_stability_cycles_calc112_252d_slope_v112_signal

def f213n_f213_net_income_stability_cycles_calc113_5d_slope_v113_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 8.3882)).rolling(3).min()).rolling(11).var()).rolling(26).max()).diff(15)) * 0.719793).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc113_5d_slope_v113_signal'] = f213n_f213_net_income_stability_cycles_calc113_5d_slope_v113_signal

def f213n_f213_net_income_stability_cycles_calc114_63d_slope_v114_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(7).max()).rolling(10).min()) * 0.020088).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc114_63d_slope_v114_signal'] = f213n_f213_net_income_stability_cycles_calc114_63d_slope_v114_signal

def f213n_f213_net_income_stability_cycles_calc115_42d_slope_v115_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(19) / ebitda.pct_change(4)).rolling(7).min()).rolling(11).min()).pct_change(6)).rolling(11).mean()) * 0.53495).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc115_42d_slope_v115_signal'] = f213n_f213_net_income_stability_cycles_calc115_42d_slope_v115_signal

def f213n_f213_net_income_stability_cycles_calc116_21d_slope_v116_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 42.7305)).rolling(26).min()).diff(6)) * 0.683071).diff(13).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc116_21d_slope_v116_signal'] = f213n_f213_net_income_stability_cycles_calc116_21d_slope_v116_signal

def f213n_f213_net_income_stability_cycles_calc117_5d_slope_v117_signal(netinc, ebitda):
    res = (((((netinc.pct_change(8) / ebitda.pct_change(15)).rolling(7).mean()).rolling(6).std()) * 0.228954).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc117_5d_slope_v117_signal'] = f213n_f213_net_income_stability_cycles_calc117_5d_slope_v117_signal

def f213n_f213_net_income_stability_cycles_calc118_63d_slope_v118_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(17) / ebitda.pct_change(12)).rolling(15).mean()).rolling(3).min()).rolling(15).var()).rolling(24).max()) * 0.496223).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc118_63d_slope_v118_signal'] = f213n_f213_net_income_stability_cycles_calc118_63d_slope_v118_signal

def f213n_f213_net_income_stability_cycles_calc119_5d_slope_v119_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 6.611)).rolling(2).mean()).rolling(4).std()) * 0.26752).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc119_5d_slope_v119_signal'] = f213n_f213_net_income_stability_cycles_calc119_5d_slope_v119_signal

def f213n_f213_net_income_stability_cycles_calc120_10d_slope_v120_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(6)).rolling(15).max()) * 0.44718).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc120_10d_slope_v120_signal'] = f213n_f213_net_income_stability_cycles_calc120_10d_slope_v120_signal

def f213n_f213_net_income_stability_cycles_calc121_63d_slope_v121_signal(netinc, ebitda):
    res = (((((netinc.diff(10) / (ebitda.shift(3) + 4.0716)).rolling(27).max()).rolling(5).mean()) * 0.208398).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc121_63d_slope_v121_signal'] = f213n_f213_net_income_stability_cycles_calc121_63d_slope_v121_signal

def f213n_f213_net_income_stability_cycles_calc122_126d_slope_v122_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(23).std()).rolling(17).min()) * 0.529909).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc122_126d_slope_v122_signal'] = f213n_f213_net_income_stability_cycles_calc122_126d_slope_v122_signal

def f213n_f213_net_income_stability_cycles_calc123_10d_slope_v123_signal(netinc, ebitda):
    res = (((((netinc * 9.9948 - ebitda).pct_change(3)).rolling(18).min()) * 0.3901).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc123_10d_slope_v123_signal'] = f213n_f213_net_income_stability_cycles_calc123_10d_slope_v123_signal

def f213n_f213_net_income_stability_cycles_calc124_63d_slope_v124_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(14)).rolling(29).mean()) * 0.624402).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc124_63d_slope_v124_signal'] = f213n_f213_net_income_stability_cycles_calc124_63d_slope_v124_signal

def f213n_f213_net_income_stability_cycles_calc125_252d_slope_v125_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 39.5234)).rolling(17).std()).rolling(27).max()).rolling(30).max()).rolling(22).min()) * 0.198754).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc125_252d_slope_v125_signal'] = f213n_f213_net_income_stability_cycles_calc125_252d_slope_v125_signal

def f213n_f213_net_income_stability_cycles_calc126_10d_slope_v126_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(4).max()).diff(5)) * 0.291875).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc126_10d_slope_v126_signal'] = f213n_f213_net_income_stability_cycles_calc126_10d_slope_v126_signal

def f213n_f213_net_income_stability_cycles_calc127_21d_slope_v127_signal(netinc, ebitda):
    res = ((((((netinc.diff(11) / (ebitda.shift(5) + 27.8112)).pct_change(16)).rolling(17).max()).rolling(26).min()) * 0.285217).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc127_21d_slope_v127_signal'] = f213n_f213_net_income_stability_cycles_calc127_21d_slope_v127_signal

def f213n_f213_net_income_stability_cycles_calc128_126d_slope_v128_signal(netinc, ebitda):
    res = (((((netinc.diff(20) / (ebitda.shift(10) + 56.0627)).diff(16)).rolling(19).var()) * 0.67854).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc128_126d_slope_v128_signal'] = f213n_f213_net_income_stability_cycles_calc128_126d_slope_v128_signal

def f213n_f213_net_income_stability_cycles_calc129_63d_slope_v129_signal(netinc, ebitda):
    res = (((((netinc * 63.1735 - ebitda).rolling(30).var()).rolling(9).var()) * 0.256561).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc129_63d_slope_v129_signal'] = f213n_f213_net_income_stability_cycles_calc129_63d_slope_v129_signal

def f213n_f213_net_income_stability_cycles_calc130_10d_slope_v130_signal(netinc, ebitda):
    res = (((((((netinc.diff(11) / (ebitda.shift(9) + 34.9165)).rolling(23).min()).diff(7)).pct_change(20)).pct_change(5)) * 0.310221).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc130_10d_slope_v130_signal'] = f213n_f213_net_income_stability_cycles_calc130_10d_slope_v130_signal

def f213n_f213_net_income_stability_cycles_calc131_10d_slope_v131_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(7).max()).rolling(25).mean()).diff(10)).diff(8)) * 0.364257).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc131_10d_slope_v131_signal'] = f213n_f213_net_income_stability_cycles_calc131_10d_slope_v131_signal

def f213n_f213_net_income_stability_cycles_calc132_63d_slope_v132_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(9)).rolling(16).max()).rolling(12).max()) * 0.823781).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc132_63d_slope_v132_signal'] = f213n_f213_net_income_stability_cycles_calc132_63d_slope_v132_signal

def f213n_f213_net_income_stability_cycles_calc133_21d_slope_v133_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 60.6378)).pct_change(9)).rolling(16).min()) * 0.257485).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc133_21d_slope_v133_signal'] = f213n_f213_net_income_stability_cycles_calc133_21d_slope_v133_signal

def f213n_f213_net_income_stability_cycles_calc134_63d_slope_v134_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(21).min()).rolling(17).mean()).rolling(14).min()).rolling(5).var()) * 0.510896).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc134_63d_slope_v134_signal'] = f213n_f213_net_income_stability_cycles_calc134_63d_slope_v134_signal

def f213n_f213_net_income_stability_cycles_calc135_10d_slope_v135_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 12.3794)).rolling(10).max()).rolling(27).std()).rolling(25).mean()).diff(14)) * 0.754922).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc135_10d_slope_v135_signal'] = f213n_f213_net_income_stability_cycles_calc135_10d_slope_v135_signal

def f213n_f213_net_income_stability_cycles_calc136_5d_slope_v136_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(11) / ebitda.pct_change(20)).rolling(15).var()).rolling(9).std()).rolling(21).std()) * 0.565236).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc136_5d_slope_v136_signal'] = f213n_f213_net_income_stability_cycles_calc136_5d_slope_v136_signal

def f213n_f213_net_income_stability_cycles_calc137_63d_slope_v137_signal(netinc, ebitda):
    res = (((((((netinc * 75.1975 - ebitda).rolling(26).var()).rolling(7).std()).pct_change(13)).rolling(19).std()) * 0.919295).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc137_63d_slope_v137_signal'] = f213n_f213_net_income_stability_cycles_calc137_63d_slope_v137_signal

def f213n_f213_net_income_stability_cycles_calc138_5d_slope_v138_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 95.4519)).pct_change(14)).rolling(9).std()) * 0.099354).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc138_5d_slope_v138_signal'] = f213n_f213_net_income_stability_cycles_calc138_5d_slope_v138_signal

def f213n_f213_net_income_stability_cycles_calc139_63d_slope_v139_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 16.6477)).rolling(15).var()).rolling(29).max()).rolling(29).max()).rolling(16).min()) * 0.180072).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc139_63d_slope_v139_signal'] = f213n_f213_net_income_stability_cycles_calc139_63d_slope_v139_signal

def f213n_f213_net_income_stability_cycles_calc140_10d_slope_v140_signal(netinc, ebitda):
    res = ((((((netinc * 10.1266 - ebitda).rolling(19).mean()).pct_change(9)).rolling(30).std()) * 0.090357).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc140_10d_slope_v140_signal'] = f213n_f213_net_income_stability_cycles_calc140_10d_slope_v140_signal

def f213n_f213_net_income_stability_cycles_calc141_42d_slope_v141_signal(netinc, ebitda):
    res = ((((((netinc * 78.9798 - ebitda).pct_change(15)).rolling(8).max()).rolling(6).var()) * 0.523457).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc141_42d_slope_v141_signal'] = f213n_f213_net_income_stability_cycles_calc141_42d_slope_v141_signal

def f213n_f213_net_income_stability_cycles_calc142_63d_slope_v142_signal(netinc, ebitda):
    res = ((((((netinc.diff(6) / (ebitda.shift(7) + 83.7103)).rolling(10).min()).rolling(24).std()).rolling(30).var()) * 0.679613).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc142_63d_slope_v142_signal'] = f213n_f213_net_income_stability_cycles_calc142_63d_slope_v142_signal

def f213n_f213_net_income_stability_cycles_calc143_42d_slope_v143_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(1)).rolling(20).min()).rolling(13).var()).rolling(2).min()) * 0.470319).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc143_42d_slope_v143_signal'] = f213n_f213_net_income_stability_cycles_calc143_42d_slope_v143_signal

def f213n_f213_net_income_stability_cycles_calc144_42d_slope_v144_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 72.4454)).rolling(10).var()).rolling(7).min()).rolling(9).std()) * 0.901004).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc144_42d_slope_v144_signal'] = f213n_f213_net_income_stability_cycles_calc144_42d_slope_v144_signal

def f213n_f213_net_income_stability_cycles_calc145_126d_slope_v145_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 51.7653)).rolling(24).mean()).rolling(4).std()) * 0.530318).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc145_126d_slope_v145_signal'] = f213n_f213_net_income_stability_cycles_calc145_126d_slope_v145_signal

def f213n_f213_net_income_stability_cycles_calc146_126d_slope_v146_signal(netinc, ebitda):
    res = (((((netinc.diff(17) / (ebitda.shift(5) + 55.3271)).pct_change(14)).rolling(29).var()) * 0.255383).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc146_126d_slope_v146_signal'] = f213n_f213_net_income_stability_cycles_calc146_126d_slope_v146_signal

def f213n_f213_net_income_stability_cycles_calc147_10d_slope_v147_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 41.0055)).diff(6)).rolling(19).var()).rolling(15).min()).rolling(9).std()) * 0.173296).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc147_10d_slope_v147_signal'] = f213n_f213_net_income_stability_cycles_calc147_10d_slope_v147_signal

def f213n_f213_net_income_stability_cycles_calc148_252d_slope_v148_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 96.1381)).rolling(26).mean()).rolling(19).min()).pct_change(12)).diff(6)) * 0.600582).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc148_252d_slope_v148_signal'] = f213n_f213_net_income_stability_cycles_calc148_252d_slope_v148_signal

def f213n_f213_net_income_stability_cycles_calc149_63d_slope_v149_signal(netinc, ebitda):
    res = (((((netinc * 93.2218 - ebitda).rolling(18).max()).rolling(14).mean()) * 0.250734).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc149_63d_slope_v149_signal'] = f213n_f213_net_income_stability_cycles_calc149_63d_slope_v149_signal

def f213n_f213_net_income_stability_cycles_calc150_10d_slope_v150_signal(netinc, ebitda):
    res = ((((((netinc * 4.9296 - ebitda).rolling(9).min()).rolling(7).min()).diff(4)) * 0.162791).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc150_10d_slope_v150_signal'] = f213n_f213_net_income_stability_cycles_calc150_10d_slope_v150_signal


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
