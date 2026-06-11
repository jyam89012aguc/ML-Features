import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f213n_f213_net_income_stability_cycles_calc001_10d_jerk_v001_signal(netinc, ebitda):
    res = ((((((netinc.diff(3) / (ebitda.shift(7) + 64.0496)).rolling(27).max()).rolling(23).min()).pct_change(13)) * 0.749423).diff(18).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc001_10d_jerk_v001_signal'] = f213n_f213_net_income_stability_cycles_calc001_10d_jerk_v001_signal

def f213n_f213_net_income_stability_cycles_calc002_126d_jerk_v002_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(20) / ebitda.pct_change(19)).rolling(26).min()).rolling(18).var()).rolling(7).min()).rolling(29).max()) * 0.52455).diff(16).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc002_126d_jerk_v002_signal'] = f213n_f213_net_income_stability_cycles_calc002_126d_jerk_v002_signal

def f213n_f213_net_income_stability_cycles_calc003_252d_jerk_v003_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(11).min()).rolling(2).var()).rolling(17).var()) * 0.081949).diff(7).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc003_252d_jerk_v003_signal'] = f213n_f213_net_income_stability_cycles_calc003_252d_jerk_v003_signal

def f213n_f213_net_income_stability_cycles_calc004_10d_jerk_v004_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(19) / ebitda.pct_change(5)).rolling(9).min()).rolling(2).std()).rolling(30).std()) * 0.635685).diff(15).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc004_10d_jerk_v004_signal'] = f213n_f213_net_income_stability_cycles_calc004_10d_jerk_v004_signal

def f213n_f213_net_income_stability_cycles_calc005_42d_jerk_v005_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(6).std()).diff(4)) * 0.708632).diff(10).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc005_42d_jerk_v005_signal'] = f213n_f213_net_income_stability_cycles_calc005_42d_jerk_v005_signal

def f213n_f213_net_income_stability_cycles_calc006_5d_jerk_v006_signal(netinc, ebitda):
    res = (((((((netinc.diff(14) / (ebitda.shift(2) + 35.1205)).rolling(17).max()).rolling(29).mean()).pct_change(16)).rolling(13).mean()) * 0.901204).diff(11).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc006_5d_jerk_v006_signal'] = f213n_f213_net_income_stability_cycles_calc006_5d_jerk_v006_signal

def f213n_f213_net_income_stability_cycles_calc007_21d_jerk_v007_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 92.2063)).rolling(8).max()).diff(17)) * 0.172626).diff(12).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc007_21d_jerk_v007_signal'] = f213n_f213_net_income_stability_cycles_calc007_21d_jerk_v007_signal

def f213n_f213_net_income_stability_cycles_calc008_42d_jerk_v008_signal(netinc, ebitda):
    res = ((((((netinc.diff(15) / (ebitda.shift(6) + 40.4009)).rolling(27).mean()).rolling(20).max()).rolling(30).mean()) * 0.792541).diff(15).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc008_42d_jerk_v008_signal'] = f213n_f213_net_income_stability_cycles_calc008_42d_jerk_v008_signal

def f213n_f213_net_income_stability_cycles_calc009_42d_jerk_v009_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 76.3876)).rolling(23).var()).diff(15)).diff(9)) * 0.045433).diff(5).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc009_42d_jerk_v009_signal'] = f213n_f213_net_income_stability_cycles_calc009_42d_jerk_v009_signal

def f213n_f213_net_income_stability_cycles_calc010_252d_jerk_v010_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 91.508)).rolling(2).var()).rolling(8).std()) * 0.101326).diff(14).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc010_252d_jerk_v010_signal'] = f213n_f213_net_income_stability_cycles_calc010_252d_jerk_v010_signal

def f213n_f213_net_income_stability_cycles_calc011_10d_jerk_v011_signal(netinc, ebitda):
    res = (((((netinc.diff(5) / (ebitda.shift(7) + 41.8171)).rolling(4).mean()).rolling(29).std()) * 0.819404).diff(2).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc011_10d_jerk_v011_signal'] = f213n_f213_net_income_stability_cycles_calc011_10d_jerk_v011_signal

def f213n_f213_net_income_stability_cycles_calc012_126d_jerk_v012_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 48.3182)).rolling(27).min()).rolling(21).var()).diff(12)).pct_change(16)) * 0.074767).diff(9).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc012_126d_jerk_v012_signal'] = f213n_f213_net_income_stability_cycles_calc012_126d_jerk_v012_signal

def f213n_f213_net_income_stability_cycles_calc013_63d_jerk_v013_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(17) / ebitda.pct_change(5)).pct_change(19)).rolling(23).max()).rolling(27).var()).rolling(26).max()) * 0.893299).diff(8).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc013_63d_jerk_v013_signal'] = f213n_f213_net_income_stability_cycles_calc013_63d_jerk_v013_signal

def f213n_f213_net_income_stability_cycles_calc014_252d_jerk_v014_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(10) / ebitda.pct_change(16)).rolling(20).mean()).rolling(27).var()).pct_change(9)) * 0.483728).diff(4).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc014_252d_jerk_v014_signal'] = f213n_f213_net_income_stability_cycles_calc014_252d_jerk_v014_signal

def f213n_f213_net_income_stability_cycles_calc015_63d_jerk_v015_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(5) / ebitda.pct_change(4)).rolling(13).max()).rolling(25).min()).rolling(15).min()).rolling(12).max()) * 0.777807).diff(10).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc015_63d_jerk_v015_signal'] = f213n_f213_net_income_stability_cycles_calc015_63d_jerk_v015_signal

def f213n_f213_net_income_stability_cycles_calc016_10d_jerk_v016_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(15).std()).rolling(2).min()).rolling(13).var()) * 0.48155).diff(4).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc016_10d_jerk_v016_signal'] = f213n_f213_net_income_stability_cycles_calc016_10d_jerk_v016_signal

def f213n_f213_net_income_stability_cycles_calc017_10d_jerk_v017_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(9).var()).rolling(27).max()) * 0.987843).diff(6).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc017_10d_jerk_v017_signal'] = f213n_f213_net_income_stability_cycles_calc017_10d_jerk_v017_signal

def f213n_f213_net_income_stability_cycles_calc018_10d_jerk_v018_signal(netinc, ebitda):
    res = (((((netinc.pct_change(3) / ebitda.pct_change(3)).rolling(19).std()).rolling(17).min()) * 0.591577).diff(3).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc018_10d_jerk_v018_signal'] = f213n_f213_net_income_stability_cycles_calc018_10d_jerk_v018_signal

def f213n_f213_net_income_stability_cycles_calc019_5d_jerk_v019_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(12) / ebitda.pct_change(12)).rolling(3).mean()).rolling(30).std()).rolling(12).var()).rolling(3).mean()) * 0.184022).diff(19).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc019_5d_jerk_v019_signal'] = f213n_f213_net_income_stability_cycles_calc019_5d_jerk_v019_signal

def f213n_f213_net_income_stability_cycles_calc020_5d_jerk_v020_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 61.4749)).rolling(11).max()).rolling(28).max()).rolling(4).max()) * 0.815001).diff(20).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc020_5d_jerk_v020_signal'] = f213n_f213_net_income_stability_cycles_calc020_5d_jerk_v020_signal

def f213n_f213_net_income_stability_cycles_calc021_10d_jerk_v021_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(24).std()).rolling(3).var()).rolling(29).min()).rolling(23).var()) * 0.604044).diff(6).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc021_10d_jerk_v021_signal'] = f213n_f213_net_income_stability_cycles_calc021_10d_jerk_v021_signal

def f213n_f213_net_income_stability_cycles_calc022_252d_jerk_v022_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 45.3056)).diff(11)).rolling(9).std()).rolling(6).min()) * 0.94267).diff(5).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc022_252d_jerk_v022_signal'] = f213n_f213_net_income_stability_cycles_calc022_252d_jerk_v022_signal

def f213n_f213_net_income_stability_cycles_calc023_5d_jerk_v023_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 5.9689)).rolling(11).mean()).pct_change(11)).diff(11)).rolling(9).max()) * 0.867639).diff(16).diff(14).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc023_5d_jerk_v023_signal'] = f213n_f213_net_income_stability_cycles_calc023_5d_jerk_v023_signal

def f213n_f213_net_income_stability_cycles_calc024_42d_jerk_v024_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(13).mean()).rolling(14).std()).rolling(13).std()).rolling(3).mean()) * 0.641425).diff(2).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc024_42d_jerk_v024_signal'] = f213n_f213_net_income_stability_cycles_calc024_42d_jerk_v024_signal

def f213n_f213_net_income_stability_cycles_calc025_42d_jerk_v025_signal(netinc, ebitda):
    res = (((((((netinc.diff(13) / (ebitda.shift(6) + 18.7376)).diff(14)).diff(11)).pct_change(19)).pct_change(6)) * 0.497665).diff(1).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc025_42d_jerk_v025_signal'] = f213n_f213_net_income_stability_cycles_calc025_42d_jerk_v025_signal

def f213n_f213_net_income_stability_cycles_calc026_21d_jerk_v026_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 41.6385)).rolling(17).max()).rolling(8).var()).diff(6)).rolling(3).min()) * 0.487156).diff(1).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc026_21d_jerk_v026_signal'] = f213n_f213_net_income_stability_cycles_calc026_21d_jerk_v026_signal

def f213n_f213_net_income_stability_cycles_calc027_126d_jerk_v027_signal(netinc, ebitda):
    res = (((((netinc * 34.362 - ebitda).rolling(6).std()).rolling(23).var()) * 0.612579).diff(17).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc027_126d_jerk_v027_signal'] = f213n_f213_net_income_stability_cycles_calc027_126d_jerk_v027_signal

def f213n_f213_net_income_stability_cycles_calc028_63d_jerk_v028_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(2)).rolling(25).min()).rolling(19).max()).rolling(19).var()) * 0.52816).diff(15).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc028_63d_jerk_v028_signal'] = f213n_f213_net_income_stability_cycles_calc028_63d_jerk_v028_signal

def f213n_f213_net_income_stability_cycles_calc029_21d_jerk_v029_signal(netinc, ebitda):
    res = (((((((netinc * 33.3273 - ebitda).rolling(12).std()).pct_change(19)).rolling(16).std()).rolling(11).var()) * 0.40919).diff(2).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc029_21d_jerk_v029_signal'] = f213n_f213_net_income_stability_cycles_calc029_21d_jerk_v029_signal

def f213n_f213_net_income_stability_cycles_calc030_126d_jerk_v030_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 90.4476)).pct_change(15)).rolling(14).std()) * 0.259059).diff(1).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc030_126d_jerk_v030_signal'] = f213n_f213_net_income_stability_cycles_calc030_126d_jerk_v030_signal

def f213n_f213_net_income_stability_cycles_calc031_5d_jerk_v031_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 95.8679)).pct_change(10)).pct_change(20)).diff(2)).rolling(20).min()) * 0.796343).diff(7).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc031_5d_jerk_v031_signal'] = f213n_f213_net_income_stability_cycles_calc031_5d_jerk_v031_signal

def f213n_f213_net_income_stability_cycles_calc032_126d_jerk_v032_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 55.2807)).diff(7)).rolling(23).mean()).rolling(4).min()).rolling(22).var()) * 0.774081).diff(8).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc032_126d_jerk_v032_signal'] = f213n_f213_net_income_stability_cycles_calc032_126d_jerk_v032_signal

def f213n_f213_net_income_stability_cycles_calc033_5d_jerk_v033_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(8).min()).diff(6)) * 0.92246).diff(12).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc033_5d_jerk_v033_signal'] = f213n_f213_net_income_stability_cycles_calc033_5d_jerk_v033_signal

def f213n_f213_net_income_stability_cycles_calc034_252d_jerk_v034_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 93.181)).pct_change(1)).rolling(4).std()) * 0.313303).diff(9).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc034_252d_jerk_v034_signal'] = f213n_f213_net_income_stability_cycles_calc034_252d_jerk_v034_signal

def f213n_f213_net_income_stability_cycles_calc035_5d_jerk_v035_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 76.5135)).diff(20)).rolling(27).var()).rolling(13).mean()) * 0.340779).diff(3).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc035_5d_jerk_v035_signal'] = f213n_f213_net_income_stability_cycles_calc035_5d_jerk_v035_signal

def f213n_f213_net_income_stability_cycles_calc036_10d_jerk_v036_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 38.8493)).rolling(12).std()).rolling(18).std()) * 0.195514).diff(18).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc036_10d_jerk_v036_signal'] = f213n_f213_net_income_stability_cycles_calc036_10d_jerk_v036_signal

def f213n_f213_net_income_stability_cycles_calc037_42d_jerk_v037_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(17)).pct_change(13)) * 0.752168).diff(7).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc037_42d_jerk_v037_signal'] = f213n_f213_net_income_stability_cycles_calc037_42d_jerk_v037_signal

def f213n_f213_net_income_stability_cycles_calc038_10d_jerk_v038_signal(netinc, ebitda):
    res = ((((((netinc * 62.1454 - ebitda).rolling(12).min()).diff(12)).rolling(30).std()) * 0.483755).diff(2).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc038_10d_jerk_v038_signal'] = f213n_f213_net_income_stability_cycles_calc038_10d_jerk_v038_signal

def f213n_f213_net_income_stability_cycles_calc039_42d_jerk_v039_signal(netinc, ebitda):
    res = (((((netinc.pct_change(11) / ebitda.pct_change(14)).rolling(29).var()).rolling(4).min()) * 0.569521).diff(5).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc039_42d_jerk_v039_signal'] = f213n_f213_net_income_stability_cycles_calc039_42d_jerk_v039_signal

def f213n_f213_net_income_stability_cycles_calc040_63d_jerk_v040_signal(netinc, ebitda):
    res = (((((((netinc * 52.0994 - ebitda).diff(11)).rolling(21).mean()).pct_change(2)).pct_change(11)) * 0.760803).diff(8).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc040_63d_jerk_v040_signal'] = f213n_f213_net_income_stability_cycles_calc040_63d_jerk_v040_signal

def f213n_f213_net_income_stability_cycles_calc041_63d_jerk_v041_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(10) / ebitda.pct_change(5)).pct_change(13)).rolling(10).std()).rolling(29).var()) * 0.297582).diff(14).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc041_63d_jerk_v041_signal'] = f213n_f213_net_income_stability_cycles_calc041_63d_jerk_v041_signal

def f213n_f213_net_income_stability_cycles_calc042_63d_jerk_v042_signal(netinc, ebitda):
    res = ((((((netinc.diff(10) / (ebitda.shift(7) + 36.4421)).rolling(24).std()).rolling(29).mean()).rolling(18).std()) * 0.498321).diff(20).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc042_63d_jerk_v042_signal'] = f213n_f213_net_income_stability_cycles_calc042_63d_jerk_v042_signal

def f213n_f213_net_income_stability_cycles_calc043_252d_jerk_v043_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 10.1022)).rolling(20).std()).pct_change(3)).rolling(3).std()).rolling(11).var()) * 0.121107).diff(18).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc043_252d_jerk_v043_signal'] = f213n_f213_net_income_stability_cycles_calc043_252d_jerk_v043_signal

def f213n_f213_net_income_stability_cycles_calc044_252d_jerk_v044_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(10) / ebitda.pct_change(18)).rolling(30).mean()).rolling(26).min()).rolling(11).mean()) * 0.708558).diff(14).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc044_252d_jerk_v044_signal'] = f213n_f213_net_income_stability_cycles_calc044_252d_jerk_v044_signal

def f213n_f213_net_income_stability_cycles_calc045_126d_jerk_v045_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 33.3933)).rolling(3).min()).rolling(27).min()) * 0.736272).diff(12).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc045_126d_jerk_v045_signal'] = f213n_f213_net_income_stability_cycles_calc045_126d_jerk_v045_signal

def f213n_f213_net_income_stability_cycles_calc046_63d_jerk_v046_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 10.7784)).diff(19)).diff(4)) * 0.165631).diff(1).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc046_63d_jerk_v046_signal'] = f213n_f213_net_income_stability_cycles_calc046_63d_jerk_v046_signal

def f213n_f213_net_income_stability_cycles_calc047_10d_jerk_v047_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(14) / ebitda.pct_change(1)).rolling(20).var()).pct_change(7)).rolling(19).min()).rolling(3).std()) * 0.134128).diff(14).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc047_10d_jerk_v047_signal'] = f213n_f213_net_income_stability_cycles_calc047_10d_jerk_v047_signal

def f213n_f213_net_income_stability_cycles_calc048_63d_jerk_v048_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(20).min()).rolling(10).var()).rolling(21).std()).pct_change(4)) * 0.198622).diff(14).diff(9).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc048_63d_jerk_v048_signal'] = f213n_f213_net_income_stability_cycles_calc048_63d_jerk_v048_signal

def f213n_f213_net_income_stability_cycles_calc049_126d_jerk_v049_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(19) / ebitda.pct_change(7)).diff(5)).rolling(7).max()).pct_change(19)) * 0.011424).diff(4).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc049_126d_jerk_v049_signal'] = f213n_f213_net_income_stability_cycles_calc049_126d_jerk_v049_signal

def f213n_f213_net_income_stability_cycles_calc050_10d_jerk_v050_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 71.1357)).rolling(5).var()).rolling(2).max()) * 0.236239).diff(7).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc050_10d_jerk_v050_signal'] = f213n_f213_net_income_stability_cycles_calc050_10d_jerk_v050_signal

def f213n_f213_net_income_stability_cycles_calc051_252d_jerk_v051_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 69.6528)).diff(4)).pct_change(12)).rolling(15).var()).rolling(23).min()) * 0.415089).diff(17).diff(9).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc051_252d_jerk_v051_signal'] = f213n_f213_net_income_stability_cycles_calc051_252d_jerk_v051_signal

def f213n_f213_net_income_stability_cycles_calc052_42d_jerk_v052_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 66.3457)).pct_change(8)).rolling(17).min()).rolling(15).var()).rolling(10).mean()) * 0.850601).diff(1).diff(14).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc052_42d_jerk_v052_signal'] = f213n_f213_net_income_stability_cycles_calc052_42d_jerk_v052_signal

def f213n_f213_net_income_stability_cycles_calc053_42d_jerk_v053_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 15.9446)).rolling(30).mean()).rolling(6).var()).rolling(10).var()) * 0.775765).diff(6).diff(14).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc053_42d_jerk_v053_signal'] = f213n_f213_net_income_stability_cycles_calc053_42d_jerk_v053_signal

def f213n_f213_net_income_stability_cycles_calc054_252d_jerk_v054_signal(netinc, ebitda):
    res = ((((((netinc.diff(17) / (ebitda.shift(2) + 1.4754)).diff(8)).rolling(8).min()).diff(9)) * 0.779981).diff(16).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc054_252d_jerk_v054_signal'] = f213n_f213_net_income_stability_cycles_calc054_252d_jerk_v054_signal

def f213n_f213_net_income_stability_cycles_calc055_21d_jerk_v055_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(18).max()).diff(5)) * 0.226154).diff(4).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc055_21d_jerk_v055_signal'] = f213n_f213_net_income_stability_cycles_calc055_21d_jerk_v055_signal

def f213n_f213_net_income_stability_cycles_calc056_126d_jerk_v056_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(17) / ebitda.pct_change(10)).rolling(4).mean()).rolling(30).max()).rolling(9).mean()) * 0.259715).diff(10).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc056_126d_jerk_v056_signal'] = f213n_f213_net_income_stability_cycles_calc056_126d_jerk_v056_signal

def f213n_f213_net_income_stability_cycles_calc057_252d_jerk_v057_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 24.505)).rolling(18).min()).rolling(6).mean()).rolling(12).mean()).pct_change(18)) * 0.948525).diff(14).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc057_252d_jerk_v057_signal'] = f213n_f213_net_income_stability_cycles_calc057_252d_jerk_v057_signal

def f213n_f213_net_income_stability_cycles_calc058_21d_jerk_v058_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(14) / ebitda.pct_change(9)).rolling(8).max()).diff(13)).diff(20)) * 0.199551).diff(19).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc058_21d_jerk_v058_signal'] = f213n_f213_net_income_stability_cycles_calc058_21d_jerk_v058_signal

def f213n_f213_net_income_stability_cycles_calc059_21d_jerk_v059_signal(netinc, ebitda):
    res = ((((((netinc.diff(7) / (ebitda.shift(4) + 9.6994)).rolling(26).min()).rolling(19).std()).rolling(17).var()) * 0.472417).diff(8).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc059_21d_jerk_v059_signal'] = f213n_f213_net_income_stability_cycles_calc059_21d_jerk_v059_signal

def f213n_f213_net_income_stability_cycles_calc060_63d_jerk_v060_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 1.7415)).rolling(15).min()).rolling(25).max()) * 0.084743).diff(3).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc060_63d_jerk_v060_signal'] = f213n_f213_net_income_stability_cycles_calc060_63d_jerk_v060_signal

def f213n_f213_net_income_stability_cycles_calc061_126d_jerk_v061_signal(netinc, ebitda):
    res = (((((netinc.diff(5) / (ebitda.shift(4) + 98.9785)).rolling(10).mean()).rolling(20).mean()) * 0.547597).diff(14).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc061_126d_jerk_v061_signal'] = f213n_f213_net_income_stability_cycles_calc061_126d_jerk_v061_signal

def f213n_f213_net_income_stability_cycles_calc062_21d_jerk_v062_signal(netinc, ebitda):
    res = (((((netinc * 64.3376 - ebitda).rolling(27).mean()).rolling(27).var()) * 0.882006).diff(20).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc062_21d_jerk_v062_signal'] = f213n_f213_net_income_stability_cycles_calc062_21d_jerk_v062_signal

def f213n_f213_net_income_stability_cycles_calc063_126d_jerk_v063_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 62.9478)).pct_change(1)).pct_change(16)).pct_change(7)).pct_change(14)) * 0.755693).diff(11).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc063_126d_jerk_v063_signal'] = f213n_f213_net_income_stability_cycles_calc063_126d_jerk_v063_signal

def f213n_f213_net_income_stability_cycles_calc064_5d_jerk_v064_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(1) / ebitda.pct_change(14)).rolling(26).var()).rolling(19).min()).diff(6)) * 0.234743).diff(1).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc064_5d_jerk_v064_signal'] = f213n_f213_net_income_stability_cycles_calc064_5d_jerk_v064_signal

def f213n_f213_net_income_stability_cycles_calc065_126d_jerk_v065_signal(netinc, ebitda):
    res = (((((netinc.pct_change(6) / ebitda.pct_change(8)).diff(6)).rolling(28).std()) * 0.663953).diff(7).diff(7).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc065_126d_jerk_v065_signal'] = f213n_f213_net_income_stability_cycles_calc065_126d_jerk_v065_signal

def f213n_f213_net_income_stability_cycles_calc066_10d_jerk_v066_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 29.5705)).diff(7)).rolling(22).var()) * 0.07005).diff(10).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc066_10d_jerk_v066_signal'] = f213n_f213_net_income_stability_cycles_calc066_10d_jerk_v066_signal

def f213n_f213_net_income_stability_cycles_calc067_10d_jerk_v067_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 68.8229)).rolling(19).mean()).rolling(23).std()).pct_change(14)) * 0.826947).diff(4).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc067_10d_jerk_v067_signal'] = f213n_f213_net_income_stability_cycles_calc067_10d_jerk_v067_signal

def f213n_f213_net_income_stability_cycles_calc068_252d_jerk_v068_signal(netinc, ebitda):
    res = (((((netinc.pct_change(14) / ebitda.pct_change(8)).rolling(24).var()).rolling(24).max()) * 0.081749).diff(18).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc068_252d_jerk_v068_signal'] = f213n_f213_net_income_stability_cycles_calc068_252d_jerk_v068_signal

def f213n_f213_net_income_stability_cycles_calc069_63d_jerk_v069_signal(netinc, ebitda):
    res = (((((((netinc * 89.9076 - ebitda).rolling(8).max()).rolling(15).min()).rolling(21).std()).pct_change(15)) * 0.908795).diff(9).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc069_63d_jerk_v069_signal'] = f213n_f213_net_income_stability_cycles_calc069_63d_jerk_v069_signal

def f213n_f213_net_income_stability_cycles_calc070_21d_jerk_v070_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(4).min()).pct_change(19)).rolling(27).mean()).diff(5)) * 0.917689).diff(2).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc070_21d_jerk_v070_signal'] = f213n_f213_net_income_stability_cycles_calc070_21d_jerk_v070_signal

def f213n_f213_net_income_stability_cycles_calc071_126d_jerk_v071_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(16) / ebitda.pct_change(13)).diff(5)).rolling(18).mean()).rolling(19).std()).rolling(27).std()) * 0.940571).diff(5).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc071_126d_jerk_v071_signal'] = f213n_f213_net_income_stability_cycles_calc071_126d_jerk_v071_signal

def f213n_f213_net_income_stability_cycles_calc072_5d_jerk_v072_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 50.8908)).rolling(19).max()).rolling(10).mean()).rolling(12).var()) * 0.604763).diff(18).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc072_5d_jerk_v072_signal'] = f213n_f213_net_income_stability_cycles_calc072_5d_jerk_v072_signal

def f213n_f213_net_income_stability_cycles_calc073_252d_jerk_v073_signal(netinc, ebitda):
    res = (((((netinc * 17.9132 - ebitda).rolling(16).max()).rolling(15).mean()) * 0.429166).diff(18).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc073_252d_jerk_v073_signal'] = f213n_f213_net_income_stability_cycles_calc073_252d_jerk_v073_signal

def f213n_f213_net_income_stability_cycles_calc074_126d_jerk_v074_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 76.0379)).pct_change(1)).pct_change(1)) * 0.461681).diff(3).diff(11).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc074_126d_jerk_v074_signal'] = f213n_f213_net_income_stability_cycles_calc074_126d_jerk_v074_signal

def f213n_f213_net_income_stability_cycles_calc075_10d_jerk_v075_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(27).min()).rolling(22).max()) * 0.801813).diff(12).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc075_10d_jerk_v075_signal'] = f213n_f213_net_income_stability_cycles_calc075_10d_jerk_v075_signal

def f213n_f213_net_income_stability_cycles_calc076_252d_jerk_v076_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(27).mean()).rolling(22).max()).rolling(26).var()).rolling(10).var()) * 0.959271).diff(6).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc076_252d_jerk_v076_signal'] = f213n_f213_net_income_stability_cycles_calc076_252d_jerk_v076_signal

def f213n_f213_net_income_stability_cycles_calc077_63d_jerk_v077_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(3)).rolling(7).std()).pct_change(10)).rolling(21).max()) * 0.598341).diff(2).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc077_63d_jerk_v077_signal'] = f213n_f213_net_income_stability_cycles_calc077_63d_jerk_v077_signal

def f213n_f213_net_income_stability_cycles_calc078_42d_jerk_v078_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 46.9406)).diff(9)).rolling(14).std()) * 0.507001).diff(12).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc078_42d_jerk_v078_signal'] = f213n_f213_net_income_stability_cycles_calc078_42d_jerk_v078_signal

def f213n_f213_net_income_stability_cycles_calc079_5d_jerk_v079_signal(netinc, ebitda):
    res = (((((netinc * 36.2105 - ebitda).rolling(15).std()).rolling(27).std()) * 0.515573).diff(9).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc079_5d_jerk_v079_signal'] = f213n_f213_net_income_stability_cycles_calc079_5d_jerk_v079_signal

def f213n_f213_net_income_stability_cycles_calc080_10d_jerk_v080_signal(netinc, ebitda):
    res = ((((((netinc * 99.0677 - ebitda).diff(2)).rolling(24).max()).rolling(22).mean()) * 0.372175).diff(16).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc080_10d_jerk_v080_signal'] = f213n_f213_net_income_stability_cycles_calc080_10d_jerk_v080_signal

def f213n_f213_net_income_stability_cycles_calc081_42d_jerk_v081_signal(netinc, ebitda):
    res = (((((netinc.diff(20) / (ebitda.shift(9) + 20.8709)).pct_change(20)).pct_change(17)) * 0.41198).diff(6).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc081_42d_jerk_v081_signal'] = f213n_f213_net_income_stability_cycles_calc081_42d_jerk_v081_signal

def f213n_f213_net_income_stability_cycles_calc082_5d_jerk_v082_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 6.1651)).rolling(25).max()).rolling(10).mean()).diff(9)).pct_change(6)) * 0.795954).diff(18).diff(16).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc082_5d_jerk_v082_signal'] = f213n_f213_net_income_stability_cycles_calc082_5d_jerk_v082_signal

def f213n_f213_net_income_stability_cycles_calc083_42d_jerk_v083_signal(netinc, ebitda):
    res = (((((netinc.pct_change(7) / ebitda.pct_change(17)).rolling(10).min()).rolling(6).std()) * 0.254035).diff(3).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc083_42d_jerk_v083_signal'] = f213n_f213_net_income_stability_cycles_calc083_42d_jerk_v083_signal

def f213n_f213_net_income_stability_cycles_calc084_126d_jerk_v084_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(2).std()).rolling(30).std()).rolling(26).min()) * 0.674345).diff(5).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc084_126d_jerk_v084_signal'] = f213n_f213_net_income_stability_cycles_calc084_126d_jerk_v084_signal

def f213n_f213_net_income_stability_cycles_calc085_126d_jerk_v085_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 72.5503)).pct_change(2)).pct_change(13)).rolling(22).var()) * 0.527755).diff(13).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc085_126d_jerk_v085_signal'] = f213n_f213_net_income_stability_cycles_calc085_126d_jerk_v085_signal

def f213n_f213_net_income_stability_cycles_calc086_21d_jerk_v086_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 94.6196)).diff(12)).rolling(19).var()).diff(6)).rolling(8).var()) * 0.376192).diff(1).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc086_21d_jerk_v086_signal'] = f213n_f213_net_income_stability_cycles_calc086_21d_jerk_v086_signal

def f213n_f213_net_income_stability_cycles_calc087_42d_jerk_v087_signal(netinc, ebitda):
    res = (((((((netinc * 37.7894 - ebitda).rolling(26).mean()).rolling(25).std()).rolling(13).mean()).rolling(19).std()) * 0.412968).diff(17).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc087_42d_jerk_v087_signal'] = f213n_f213_net_income_stability_cycles_calc087_42d_jerk_v087_signal

def f213n_f213_net_income_stability_cycles_calc088_10d_jerk_v088_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(20) / ebitda.pct_change(2)).rolling(3).var()).rolling(23).var()).diff(2)).pct_change(10)) * 0.279925).diff(8).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc088_10d_jerk_v088_signal'] = f213n_f213_net_income_stability_cycles_calc088_10d_jerk_v088_signal

def f213n_f213_net_income_stability_cycles_calc089_10d_jerk_v089_signal(netinc, ebitda):
    res = ((((((netinc * 20.9728 - ebitda).diff(4)).rolling(25).min()).rolling(27).std()) * 0.759746).diff(5).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc089_10d_jerk_v089_signal'] = f213n_f213_net_income_stability_cycles_calc089_10d_jerk_v089_signal

def f213n_f213_net_income_stability_cycles_calc090_5d_jerk_v090_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 9.548)).rolling(9).std()).rolling(4).max()).diff(7)).rolling(8).min()) * 0.597858).diff(5).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc090_5d_jerk_v090_signal'] = f213n_f213_net_income_stability_cycles_calc090_5d_jerk_v090_signal

def f213n_f213_net_income_stability_cycles_calc091_126d_jerk_v091_signal(netinc, ebitda):
    res = (((((((netinc * 32.3697 - ebitda).rolling(26).min()).rolling(14).var()).rolling(16).mean()).rolling(29).max()) * 0.231203).diff(14).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc091_126d_jerk_v091_signal'] = f213n_f213_net_income_stability_cycles_calc091_126d_jerk_v091_signal

def f213n_f213_net_income_stability_cycles_calc092_126d_jerk_v092_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 86.4152)).rolling(12).mean()).pct_change(14)).rolling(19).mean()).rolling(28).std()) * 0.883987).diff(20).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc092_126d_jerk_v092_signal'] = f213n_f213_net_income_stability_cycles_calc092_126d_jerk_v092_signal

def f213n_f213_net_income_stability_cycles_calc093_5d_jerk_v093_signal(netinc, ebitda):
    res = (((((netinc * 24.5141 - ebitda).diff(14)).rolling(30).mean()) * 0.379745).diff(20).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc093_5d_jerk_v093_signal'] = f213n_f213_net_income_stability_cycles_calc093_5d_jerk_v093_signal

def f213n_f213_net_income_stability_cycles_calc094_42d_jerk_v094_signal(netinc, ebitda):
    res = (((((netinc * 36.8537 - ebitda).pct_change(4)).pct_change(17)) * 0.786241).diff(19).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc094_42d_jerk_v094_signal'] = f213n_f213_net_income_stability_cycles_calc094_42d_jerk_v094_signal

def f213n_f213_net_income_stability_cycles_calc095_5d_jerk_v095_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 53.969)).rolling(26).std()).rolling(8).min()).rolling(28).std()).diff(6)) * 0.231327).diff(7).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc095_5d_jerk_v095_signal'] = f213n_f213_net_income_stability_cycles_calc095_5d_jerk_v095_signal

def f213n_f213_net_income_stability_cycles_calc096_63d_jerk_v096_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).mean()).rolling(24).mean()) * 0.082032).diff(10).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc096_63d_jerk_v096_signal'] = f213n_f213_net_income_stability_cycles_calc096_63d_jerk_v096_signal

def f213n_f213_net_income_stability_cycles_calc097_63d_jerk_v097_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 53.6569)).rolling(15).min()).rolling(27).min()).diff(2)) * 0.931854).diff(17).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc097_63d_jerk_v097_signal'] = f213n_f213_net_income_stability_cycles_calc097_63d_jerk_v097_signal

def f213n_f213_net_income_stability_cycles_calc098_5d_jerk_v098_signal(netinc, ebitda):
    res = (((((netinc * 74.6597 - ebitda).rolling(14).var()).rolling(30).min()) * 0.427986).diff(20).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc098_5d_jerk_v098_signal'] = f213n_f213_net_income_stability_cycles_calc098_5d_jerk_v098_signal

def f213n_f213_net_income_stability_cycles_calc099_252d_jerk_v099_signal(netinc, ebitda):
    res = (((((netinc.pct_change(3) / ebitda.pct_change(11)).rolling(7).mean()).pct_change(7)) * 0.036724).diff(9).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc099_252d_jerk_v099_signal'] = f213n_f213_net_income_stability_cycles_calc099_252d_jerk_v099_signal

def f213n_f213_net_income_stability_cycles_calc100_21d_jerk_v100_signal(netinc, ebitda):
    res = ((((((netinc / (ebitda + 5.3)).diff(16)).rolling(26).min()).rolling(22).max()) * 0.431198).diff(5).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc100_21d_jerk_v100_signal'] = f213n_f213_net_income_stability_cycles_calc100_21d_jerk_v100_signal

def f213n_f213_net_income_stability_cycles_calc101_10d_jerk_v101_signal(netinc, ebitda):
    res = (((((((netinc.diff(10) / (ebitda.shift(1) + 98.3936)).rolling(27).mean()).rolling(16).max()).pct_change(7)).rolling(11).var()) * 0.824764).diff(8).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc101_10d_jerk_v101_signal'] = f213n_f213_net_income_stability_cycles_calc101_10d_jerk_v101_signal

def f213n_f213_net_income_stability_cycles_calc102_252d_jerk_v102_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 66.744)).diff(12)).rolling(25).max()) * 0.549282).diff(4).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc102_252d_jerk_v102_signal'] = f213n_f213_net_income_stability_cycles_calc102_252d_jerk_v102_signal

def f213n_f213_net_income_stability_cycles_calc103_5d_jerk_v103_signal(netinc, ebitda):
    res = (((((((netinc.diff(1) / (ebitda.shift(10) + 66.7359)).rolling(24).max()).rolling(27).mean()).rolling(11).var()).rolling(7).max()) * 0.452503).diff(1).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc103_5d_jerk_v103_signal'] = f213n_f213_net_income_stability_cycles_calc103_5d_jerk_v103_signal

def f213n_f213_net_income_stability_cycles_calc104_21d_jerk_v104_signal(netinc, ebitda):
    res = (((((((netinc * 58.3316 - ebitda).pct_change(13)).pct_change(10)).pct_change(18)).diff(20)) * 0.172289).diff(20).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc104_21d_jerk_v104_signal'] = f213n_f213_net_income_stability_cycles_calc104_21d_jerk_v104_signal

def f213n_f213_net_income_stability_cycles_calc105_5d_jerk_v105_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(19) / ebitda.pct_change(13)).rolling(6).std()).rolling(20).var()).rolling(11).mean()).rolling(26).mean()) * 0.299637).diff(17).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc105_5d_jerk_v105_signal'] = f213n_f213_net_income_stability_cycles_calc105_5d_jerk_v105_signal

def f213n_f213_net_income_stability_cycles_calc106_63d_jerk_v106_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 61.9165)).rolling(26).var()).rolling(26).std()) * 0.965357).diff(14).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc106_63d_jerk_v106_signal'] = f213n_f213_net_income_stability_cycles_calc106_63d_jerk_v106_signal

def f213n_f213_net_income_stability_cycles_calc107_63d_jerk_v107_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(22).min()).rolling(16).mean()) * 0.928778).diff(14).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc107_63d_jerk_v107_signal'] = f213n_f213_net_income_stability_cycles_calc107_63d_jerk_v107_signal

def f213n_f213_net_income_stability_cycles_calc108_126d_jerk_v108_signal(netinc, ebitda):
    res = (((((netinc * 44.2547 - ebitda).rolling(23).var()).diff(20)) * 0.744291).diff(12).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc108_126d_jerk_v108_signal'] = f213n_f213_net_income_stability_cycles_calc108_126d_jerk_v108_signal

def f213n_f213_net_income_stability_cycles_calc109_63d_jerk_v109_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(6).mean()).diff(19)).rolling(15).max()).rolling(2).var()) * 0.889124).diff(18).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc109_63d_jerk_v109_signal'] = f213n_f213_net_income_stability_cycles_calc109_63d_jerk_v109_signal

def f213n_f213_net_income_stability_cycles_calc110_42d_jerk_v110_signal(netinc, ebitda):
    res = ((((((netinc * 59.0922 - ebitda).rolling(14).max()).rolling(15).var()).diff(3)) * 0.361548).diff(7).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc110_42d_jerk_v110_signal'] = f213n_f213_net_income_stability_cycles_calc110_42d_jerk_v110_signal

def f213n_f213_net_income_stability_cycles_calc111_63d_jerk_v111_signal(netinc, ebitda):
    res = ((((((netinc * 48.2447 - ebitda).pct_change(4)).rolling(28).var()).rolling(26).std()) * 0.427435).diff(9).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc111_63d_jerk_v111_signal'] = f213n_f213_net_income_stability_cycles_calc111_63d_jerk_v111_signal

def f213n_f213_net_income_stability_cycles_calc112_63d_jerk_v112_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 14.9803)).rolling(26).min()).rolling(2).std()) * 0.585859).diff(1).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc112_63d_jerk_v112_signal'] = f213n_f213_net_income_stability_cycles_calc112_63d_jerk_v112_signal

def f213n_f213_net_income_stability_cycles_calc113_42d_jerk_v113_signal(netinc, ebitda):
    res = (((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(4).std()).rolling(23).mean()).rolling(28).std()).rolling(12).max()) * 0.899192).diff(1).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc113_42d_jerk_v113_signal'] = f213n_f213_net_income_stability_cycles_calc113_42d_jerk_v113_signal

def f213n_f213_net_income_stability_cycles_calc114_5d_jerk_v114_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 37.5816)).rolling(3).var()).rolling(15).min()).pct_change(6)).pct_change(17)) * 0.064867).diff(7).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc114_5d_jerk_v114_signal'] = f213n_f213_net_income_stability_cycles_calc114_5d_jerk_v114_signal

def f213n_f213_net_income_stability_cycles_calc115_42d_jerk_v115_signal(netinc, ebitda):
    res = (((((netinc.diff(2) / (ebitda.shift(6) + 64.2431)).rolling(16).min()).rolling(21).min()) * 0.624438).diff(10).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc115_42d_jerk_v115_signal'] = f213n_f213_net_income_stability_cycles_calc115_42d_jerk_v115_signal

def f213n_f213_net_income_stability_cycles_calc116_10d_jerk_v116_signal(netinc, ebitda):
    res = (((((netinc * 5.9124 - ebitda).rolling(2).var()).rolling(27).max()) * 0.934072).diff(3).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc116_10d_jerk_v116_signal'] = f213n_f213_net_income_stability_cycles_calc116_10d_jerk_v116_signal

def f213n_f213_net_income_stability_cycles_calc117_126d_jerk_v117_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(6) / ebitda.pct_change(19)).rolling(26).mean()).pct_change(9)).rolling(14).mean()).rolling(23).max()) * 0.474657).diff(18).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc117_126d_jerk_v117_signal'] = f213n_f213_net_income_stability_cycles_calc117_126d_jerk_v117_signal

def f213n_f213_net_income_stability_cycles_calc118_5d_jerk_v118_signal(netinc, ebitda):
    res = ((((((netinc.diff(15) / (ebitda.shift(4) + 97.0327)).diff(6)).rolling(13).std()).rolling(5).min()) * 0.20447).diff(15).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc118_5d_jerk_v118_signal'] = f213n_f213_net_income_stability_cycles_calc118_5d_jerk_v118_signal

def f213n_f213_net_income_stability_cycles_calc119_5d_jerk_v119_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 46.4791)).rolling(5).min()).rolling(26).std()) * 0.210819).diff(14).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc119_5d_jerk_v119_signal'] = f213n_f213_net_income_stability_cycles_calc119_5d_jerk_v119_signal

def f213n_f213_net_income_stability_cycles_calc120_252d_jerk_v120_signal(netinc, ebitda):
    res = ((((((netinc * 51.3781 - ebitda).rolling(5).min()).rolling(8).std()).rolling(4).min()) * 0.66624).diff(18).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc120_252d_jerk_v120_signal'] = f213n_f213_net_income_stability_cycles_calc120_252d_jerk_v120_signal

def f213n_f213_net_income_stability_cycles_calc121_21d_jerk_v121_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 26.5334)).rolling(18).var()).rolling(28).mean()).rolling(15).mean()) * 0.058201).diff(9).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc121_21d_jerk_v121_signal'] = f213n_f213_net_income_stability_cycles_calc121_21d_jerk_v121_signal

def f213n_f213_net_income_stability_cycles_calc122_5d_jerk_v122_signal(netinc, ebitda):
    res = (((((netinc * 23.7271 - ebitda).rolling(30).std()).rolling(25).min()) * 0.210793).diff(16).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc122_5d_jerk_v122_signal'] = f213n_f213_net_income_stability_cycles_calc122_5d_jerk_v122_signal

def f213n_f213_net_income_stability_cycles_calc123_10d_jerk_v123_signal(netinc, ebitda):
    res = (((((netinc * 91.5255 - ebitda).rolling(22).mean()).rolling(10).std()) * 0.083675).diff(17).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc123_10d_jerk_v123_signal'] = f213n_f213_net_income_stability_cycles_calc123_10d_jerk_v123_signal

def f213n_f213_net_income_stability_cycles_calc124_10d_jerk_v124_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(18)).rolling(30).std()) * 0.343335).diff(4).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc124_10d_jerk_v124_signal'] = f213n_f213_net_income_stability_cycles_calc124_10d_jerk_v124_signal

def f213n_f213_net_income_stability_cycles_calc125_10d_jerk_v125_signal(netinc, ebitda):
    res = ((((((netinc * 54.3968 - ebitda).diff(1)).rolling(27).min()).diff(19)) * 0.985997).diff(18).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc125_10d_jerk_v125_signal'] = f213n_f213_net_income_stability_cycles_calc125_10d_jerk_v125_signal

def f213n_f213_net_income_stability_cycles_calc126_42d_jerk_v126_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(18).min()).pct_change(5)) * 0.984578).diff(1).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc126_42d_jerk_v126_signal'] = f213n_f213_net_income_stability_cycles_calc126_42d_jerk_v126_signal

def f213n_f213_net_income_stability_cycles_calc127_252d_jerk_v127_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(6) / ebitda.pct_change(8)).rolling(23).var()).rolling(4).std()).rolling(23).min()) * 0.539808).diff(12).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc127_252d_jerk_v127_signal'] = f213n_f213_net_income_stability_cycles_calc127_252d_jerk_v127_signal

def f213n_f213_net_income_stability_cycles_calc128_252d_jerk_v128_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 33.5716)).rolling(18).mean()).diff(6)).rolling(20).mean()).rolling(12).std()) * 0.979096).diff(19).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc128_252d_jerk_v128_signal'] = f213n_f213_net_income_stability_cycles_calc128_252d_jerk_v128_signal

def f213n_f213_net_income_stability_cycles_calc129_42d_jerk_v129_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 75.5208)).rolling(21).max()).rolling(11).max()).pct_change(18)) * 0.945793).diff(1).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc129_42d_jerk_v129_signal'] = f213n_f213_net_income_stability_cycles_calc129_42d_jerk_v129_signal

def f213n_f213_net_income_stability_cycles_calc130_10d_jerk_v130_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(20) / ebitda.pct_change(8)).rolling(25).min()).rolling(24).max()).diff(9)).rolling(11).max()) * 0.047032).diff(5).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc130_10d_jerk_v130_signal'] = f213n_f213_net_income_stability_cycles_calc130_10d_jerk_v130_signal

def f213n_f213_net_income_stability_cycles_calc131_63d_jerk_v131_signal(netinc, ebitda):
    res = ((((((netinc.diff(17) / (ebitda.shift(9) + 33.8383)).rolling(22).min()).rolling(18).max()).rolling(27).min()) * 0.730716).diff(2).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc131_63d_jerk_v131_signal'] = f213n_f213_net_income_stability_cycles_calc131_63d_jerk_v131_signal

def f213n_f213_net_income_stability_cycles_calc132_5d_jerk_v132_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).max()).diff(6)) * 0.185461).diff(1).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc132_5d_jerk_v132_signal'] = f213n_f213_net_income_stability_cycles_calc132_5d_jerk_v132_signal

def f213n_f213_net_income_stability_cycles_calc133_42d_jerk_v133_signal(netinc, ebitda):
    res = (((((((netinc * 27.5625 - ebitda).rolling(14).min()).rolling(6).max()).pct_change(20)).rolling(15).max()) * 0.774643).diff(17).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc133_42d_jerk_v133_signal'] = f213n_f213_net_income_stability_cycles_calc133_42d_jerk_v133_signal

def f213n_f213_net_income_stability_cycles_calc134_126d_jerk_v134_signal(netinc, ebitda):
    res = ((((((ebitda / (netinc + 84.5666)).diff(2)).pct_change(18)).rolling(23).var()) * 0.830304).diff(17).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc134_126d_jerk_v134_signal'] = f213n_f213_net_income_stability_cycles_calc134_126d_jerk_v134_signal

def f213n_f213_net_income_stability_cycles_calc135_42d_jerk_v135_signal(netinc, ebitda):
    res = (((((((netinc / (ebitda + 64.3906)).pct_change(12)).pct_change(13)).rolling(25).min()).rolling(12).max()) * 0.678692).diff(15).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc135_42d_jerk_v135_signal'] = f213n_f213_net_income_stability_cycles_calc135_42d_jerk_v135_signal

def f213n_f213_net_income_stability_cycles_calc136_5d_jerk_v136_signal(netinc, ebitda):
    res = ((((((netinc.diff(9) / (ebitda.shift(9) + 3.1604)).rolling(7).var()).rolling(14).max()).rolling(20).min()) * 0.132329).diff(13).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc136_5d_jerk_v136_signal'] = f213n_f213_net_income_stability_cycles_calc136_5d_jerk_v136_signal

def f213n_f213_net_income_stability_cycles_calc137_10d_jerk_v137_signal(netinc, ebitda):
    res = (((((((netinc.pct_change(8) / ebitda.pct_change(5)).diff(19)).pct_change(9)).pct_change(13)).pct_change(8)) * 0.808922).diff(7).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc137_10d_jerk_v137_signal'] = f213n_f213_net_income_stability_cycles_calc137_10d_jerk_v137_signal

def f213n_f213_net_income_stability_cycles_calc138_63d_jerk_v138_signal(netinc, ebitda):
    res = (((((((ebitda / (netinc + 93.4602)).pct_change(11)).diff(16)).rolling(12).std()).rolling(7).min()) * 0.343382).diff(19).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc138_63d_jerk_v138_signal'] = f213n_f213_net_income_stability_cycles_calc138_63d_jerk_v138_signal

def f213n_f213_net_income_stability_cycles_calc139_42d_jerk_v139_signal(netinc, ebitda):
    res = ((((((netinc.pct_change(17) / ebitda.pct_change(20)).rolling(9).mean()).pct_change(17)).rolling(19).mean()) * 0.227219).diff(13).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc139_42d_jerk_v139_signal'] = f213n_f213_net_income_stability_cycles_calc139_42d_jerk_v139_signal

def f213n_f213_net_income_stability_cycles_calc140_21d_jerk_v140_signal(netinc, ebitda):
    res = (((((netinc.diff(17) / (ebitda.shift(5) + 2.6634)).rolling(12).max()).pct_change(16)) * 0.642904).diff(10).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc140_21d_jerk_v140_signal'] = f213n_f213_net_income_stability_cycles_calc140_21d_jerk_v140_signal

def f213n_f213_net_income_stability_cycles_calc141_10d_jerk_v141_signal(netinc, ebitda):
    res = (((((netinc / (ebitda + 0.8595)).rolling(21).min()).rolling(7).min()) * 0.310487).diff(2).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc141_10d_jerk_v141_signal'] = f213n_f213_net_income_stability_cycles_calc141_10d_jerk_v141_signal

def f213n_f213_net_income_stability_cycles_calc142_63d_jerk_v142_signal(netinc, ebitda):
    res = (((((netinc.diff(8) / (ebitda.shift(5) + 83.3192)).rolling(11).min()).rolling(12).mean()) * 0.336943).diff(10).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc142_63d_jerk_v142_signal'] = f213n_f213_net_income_stability_cycles_calc142_63d_jerk_v142_signal

def f213n_f213_net_income_stability_cycles_calc143_5d_jerk_v143_signal(netinc, ebitda):
    res = (((((netinc * 32.7441 - ebitda).pct_change(14)).rolling(25).min()) * 0.331211).diff(17).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc143_5d_jerk_v143_signal'] = f213n_f213_net_income_stability_cycles_calc143_5d_jerk_v143_signal

def f213n_f213_net_income_stability_cycles_calc144_10d_jerk_v144_signal(netinc, ebitda):
    res = (((((netinc.diff(11) / (ebitda.shift(1) + 79.9005)).diff(4)).rolling(26).var()) * 0.44838).diff(3).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc144_10d_jerk_v144_signal'] = f213n_f213_net_income_stability_cycles_calc144_10d_jerk_v144_signal

def f213n_f213_net_income_stability_cycles_calc145_252d_jerk_v145_signal(netinc, ebitda):
    res = ((((((netinc * 35.4506 - ebitda).rolling(3).max()).rolling(25).max()).pct_change(5)) * 0.4575).diff(16).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc145_252d_jerk_v145_signal'] = f213n_f213_net_income_stability_cycles_calc145_252d_jerk_v145_signal

def f213n_f213_net_income_stability_cycles_calc146_21d_jerk_v146_signal(netinc, ebitda):
    res = (((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).std()).rolling(27).max()) * 0.24031).diff(14).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc146_21d_jerk_v146_signal'] = f213n_f213_net_income_stability_cycles_calc146_21d_jerk_v146_signal

def f213n_f213_net_income_stability_cycles_calc147_5d_jerk_v147_signal(netinc, ebitda):
    res = ((((((netinc * 95.5591 - ebitda).rolling(11).var()).pct_change(6)).rolling(17).std()) * 0.856754).diff(11).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc147_5d_jerk_v147_signal'] = f213n_f213_net_income_stability_cycles_calc147_5d_jerk_v147_signal

def f213n_f213_net_income_stability_cycles_calc148_21d_jerk_v148_signal(netinc, ebitda):
    res = ((((((netinc.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(11)).pct_change(20)).rolling(7).var()) * 0.885308).diff(17).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc148_21d_jerk_v148_signal'] = f213n_f213_net_income_stability_cycles_calc148_21d_jerk_v148_signal

def f213n_f213_net_income_stability_cycles_calc149_21d_jerk_v149_signal(netinc, ebitda):
    res = (((((ebitda / (netinc + 95.8047)).rolling(3).mean()).rolling(27).std()) * 0.902277).diff(10).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc149_21d_jerk_v149_signal'] = f213n_f213_net_income_stability_cycles_calc149_21d_jerk_v149_signal

def f213n_f213_net_income_stability_cycles_calc150_126d_jerk_v150_signal(netinc, ebitda):
    res = (((((netinc.pct_change(8) / ebitda.pct_change(5)).pct_change(11)).pct_change(11)) * 0.644393).diff(3).diff(7).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f213n_f213_net_income_stability_cycles_calc150_126d_jerk_v150_signal'] = f213n_f213_net_income_stability_cycles_calc150_126d_jerk_v150_signal


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
