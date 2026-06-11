import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_252d_slope_v001_signal(capex, ebitda):
    res = (((((((capex * 12.9112 - ebitda).rolling(13).var()).rolling(26).max()).rolling(22).std()).rolling(17).std()) * 0.223822).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_252d_slope_v001_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_252d_slope_v001_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_42d_slope_v002_signal(capex, ebitda):
    res = (((((capex / (ebitda + 85.0957)).pct_change(18)).rolling(2).var()) * 0.267454).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_42d_slope_v002_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_42d_slope_v002_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_126d_slope_v003_signal(capex, ebitda):
    res = ((((((capex * 80.178 - ebitda).rolling(6).min()).rolling(19).std()).rolling(9).max()) * 0.34641).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_126d_slope_v003_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_126d_slope_v003_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_5d_slope_v004_signal(capex, ebitda):
    res = ((((((capex.diff(8) / (ebitda.shift(2) + 30.1389)).diff(3)).rolling(23).var()).rolling(11).min()) * 0.749928).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_5d_slope_v004_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_5d_slope_v004_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_252d_slope_v005_signal(capex, ebitda):
    res = (((((((capex * 19.8775 - ebitda).rolling(20).min()).pct_change(11)).rolling(4).std()).rolling(29).std()) * 0.360446).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_252d_slope_v005_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_252d_slope_v005_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_21d_slope_v006_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(8).max()).rolling(24).mean()) * 0.325786).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_21d_slope_v006_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_21d_slope_v006_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_252d_slope_v007_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 37.4602)).rolling(20).std()).rolling(12).mean()).rolling(4).mean()) * 0.060566).diff(9).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_252d_slope_v007_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_252d_slope_v007_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_10d_slope_v008_signal(capex, ebitda):
    res = (((((capex * 43.3701 - ebitda).rolling(16).max()).rolling(3).mean()) * 0.534163).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_10d_slope_v008_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_10d_slope_v008_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_126d_slope_v009_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(22).min()).rolling(22).max()) * 0.524015).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_126d_slope_v009_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_126d_slope_v009_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_10d_slope_v010_signal(capex, ebitda):
    res = (((((capex.diff(7) / (ebitda.shift(4) + 86.3861)).diff(7)).rolling(14).mean()) * 0.815529).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_10d_slope_v010_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_10d_slope_v010_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_5d_slope_v011_signal(capex, ebitda):
    res = (((((capex.pct_change(11) / ebitda.pct_change(11)).diff(11)).pct_change(5)) * 0.063145).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_5d_slope_v011_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_5d_slope_v011_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_21d_slope_v012_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(12).mean()).rolling(10).mean()) * 0.103921).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_21d_slope_v012_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_21d_slope_v012_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_126d_slope_v013_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 58.9235)).rolling(6).max()).rolling(6).std()).pct_change(5)).rolling(3).var()) * 0.148834).diff(2).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_126d_slope_v013_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_126d_slope_v013_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_21d_slope_v014_signal(capex, ebitda):
    res = ((((((capex.diff(5) / (ebitda.shift(3) + 23.2875)).rolling(22).std()).rolling(5).mean()).diff(20)) * 0.967769).diff(2).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_21d_slope_v014_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_21d_slope_v014_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_252d_slope_v015_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 7.645)).rolling(8).mean()).rolling(22).std()).rolling(13).std()).rolling(18).std()) * 0.753001).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_252d_slope_v015_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_252d_slope_v015_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_5d_slope_v016_signal(capex, ebitda):
    res = ((((((capex.pct_change(11) / ebitda.pct_change(14)).rolling(6).var()).rolling(11).std()).rolling(18).std()) * 0.165157).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_5d_slope_v016_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_5d_slope_v016_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_21d_slope_v017_signal(capex, ebitda):
    res = (((((((capex.diff(15) / (ebitda.shift(7) + 77.2743)).rolling(15).max()).rolling(8).min()).rolling(7).var()).diff(2)) * 0.30199).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_21d_slope_v017_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_21d_slope_v017_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_21d_slope_v018_signal(capex, ebitda):
    res = (((((((capex * 24.827 - ebitda).diff(12)).rolling(21).std()).rolling(28).min()).rolling(13).std()) * 0.745347).diff(13).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_21d_slope_v018_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_21d_slope_v018_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_252d_slope_v019_signal(capex, ebitda):
    res = (((((((capex.diff(6) / (ebitda.shift(7) + 77.4623)).pct_change(3)).rolling(17).var()).pct_change(13)).rolling(13).std()) * 0.337916).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_252d_slope_v019_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_252d_slope_v019_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_252d_slope_v020_signal(capex, ebitda):
    res = ((((((capex.diff(14) / (ebitda.shift(7) + 63.9941)).pct_change(12)).rolling(9).std()).rolling(29).min()) * 0.069367).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_252d_slope_v020_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_252d_slope_v020_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_126d_slope_v021_signal(capex, ebitda):
    res = ((((((capex.pct_change(13) / ebitda.pct_change(14)).diff(8)).rolling(8).var()).rolling(20).max()) * 0.292773).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_126d_slope_v021_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_126d_slope_v021_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_10d_slope_v022_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 76.2127)).rolling(30).std()).diff(13)).rolling(20).min()) * 0.873082).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_10d_slope_v022_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_10d_slope_v022_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_21d_slope_v023_signal(capex, ebitda):
    res = (((((((capex.pct_change(14) / ebitda.pct_change(7)).rolling(9).max()).rolling(10).var()).rolling(23).std()).rolling(15).var()) * 0.475325).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_21d_slope_v023_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_21d_slope_v023_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_21d_slope_v024_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(6).max()).rolling(20).var()).rolling(20).min()).diff(8)) * 0.430583).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_21d_slope_v024_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_21d_slope_v024_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_63d_slope_v025_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 75.2299)).rolling(4).max()).rolling(14).mean()).pct_change(17)).diff(7)) * 0.753739).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_63d_slope_v025_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_63d_slope_v025_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_5d_slope_v026_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 3.0198)).diff(6)).pct_change(1)).rolling(10).mean()) * 0.032659).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_5d_slope_v026_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_5d_slope_v026_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_63d_slope_v027_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(20).var()).rolling(5).std()).rolling(5).std()).rolling(14).var()) * 0.482334).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_63d_slope_v027_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_63d_slope_v027_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_63d_slope_v028_signal(capex, ebitda):
    res = ((((((capex.pct_change(6) / ebitda.pct_change(11)).pct_change(5)).diff(19)).pct_change(6)) * 0.777337).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_63d_slope_v028_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_63d_slope_v028_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_252d_slope_v029_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 70.2829)).rolling(25).std()).rolling(29).max()).pct_change(19)) * 0.347583).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_252d_slope_v029_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_252d_slope_v029_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_5d_slope_v030_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 21.6016)).rolling(24).min()).rolling(24).min()).rolling(20).var()).rolling(4).min()) * 0.814246).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_5d_slope_v030_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_5d_slope_v030_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_42d_slope_v031_signal(capex, ebitda):
    res = (((((capex.diff(14) / (ebitda.shift(9) + 45.2046)).rolling(5).max()).rolling(5).mean()) * 0.66879).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_42d_slope_v031_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_42d_slope_v031_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_5d_slope_v032_signal(capex, ebitda):
    res = (((((capex.pct_change(4) / ebitda.pct_change(13)).rolling(21).max()).rolling(25).var()) * 0.779562).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_5d_slope_v032_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_5d_slope_v032_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_5d_slope_v033_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 76.1657)).diff(14)).pct_change(16)).diff(7)) * 0.089678).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_5d_slope_v033_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_5d_slope_v033_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_63d_slope_v034_signal(capex, ebitda):
    res = (((((capex.pct_change(9) / ebitda.pct_change(3)).rolling(29).mean()).rolling(17).min()) * 0.285818).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_63d_slope_v034_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_63d_slope_v034_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_10d_slope_v035_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 3.866)).rolling(22).max()).diff(19)).diff(3)) * 0.984096).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_10d_slope_v035_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_10d_slope_v035_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_5d_slope_v036_signal(capex, ebitda):
    res = ((((((capex * 84.8572 - ebitda).pct_change(14)).rolling(14).mean()).rolling(3).max()) * 0.653034).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_5d_slope_v036_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_5d_slope_v036_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_63d_slope_v037_signal(capex, ebitda):
    res = (((((((capex * 60.262 - ebitda).rolling(11).var()).rolling(10).max()).rolling(3).std()).rolling(12).std()) * 0.251519).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_63d_slope_v037_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_63d_slope_v037_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_5d_slope_v038_signal(capex, ebitda):
    res = (((((capex / (ebitda + 42.6042)).rolling(14).max()).rolling(4).mean()) * 0.691452).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_5d_slope_v038_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_5d_slope_v038_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_252d_slope_v039_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 48.1072)).rolling(20).mean()).diff(10)).pct_change(1)).rolling(11).std()) * 0.848108).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_252d_slope_v039_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_252d_slope_v039_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_126d_slope_v040_signal(capex, ebitda):
    res = (((((capex / (ebitda + 86.7564)).rolling(28).std()).rolling(16).max()) * 0.168341).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_126d_slope_v040_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_126d_slope_v040_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_slope_v041_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(17).var()).rolling(11).min()).pct_change(14)).rolling(21).std()) * 0.484887).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_slope_v041_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_slope_v041_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_10d_slope_v042_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 55.4554)).rolling(5).min()).pct_change(19)).rolling(7).var()).rolling(22).std()) * 0.954704).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_10d_slope_v042_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_10d_slope_v042_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_5d_slope_v043_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 34.9003)).rolling(15).mean()).rolling(23).max()).rolling(23).min()) * 0.869439).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_5d_slope_v043_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_5d_slope_v043_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_42d_slope_v044_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 6.7363)).rolling(25).min()).rolling(30).var()).rolling(2).mean()).rolling(22).std()) * 0.54691).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_42d_slope_v044_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_42d_slope_v044_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_21d_slope_v045_signal(capex, ebitda):
    res = (((((((capex.pct_change(18) / ebitda.pct_change(20)).rolling(18).var()).rolling(13).max()).rolling(14).min()).rolling(11).max()) * 0.802552).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_21d_slope_v045_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_21d_slope_v045_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_63d_slope_v046_signal(capex, ebitda):
    res = (((((((capex * 98.1993 - ebitda).diff(11)).rolling(16).min()).rolling(23).var()).rolling(8).min()) * 0.595927).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_63d_slope_v046_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_63d_slope_v046_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_21d_slope_v047_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(14).min()).rolling(26).std()) * 0.300319).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_21d_slope_v047_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_21d_slope_v047_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_42d_slope_v048_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 36.7591)).pct_change(9)).rolling(28).mean()).rolling(2).std()) * 0.263811).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_42d_slope_v048_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_42d_slope_v048_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_63d_slope_v049_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(2).mean()).diff(14)) * 0.951798).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_63d_slope_v049_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_63d_slope_v049_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_63d_slope_v050_signal(capex, ebitda):
    res = (((((ebitda / (capex + 59.9906)).rolling(15).min()).rolling(8).std()) * 0.668869).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_63d_slope_v050_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_63d_slope_v050_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_126d_slope_v051_signal(capex, ebitda):
    res = (((((capex * 11.2209 - ebitda).rolling(7).std()).rolling(6).max()) * 0.354151).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_126d_slope_v051_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_126d_slope_v051_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_5d_slope_v052_signal(capex, ebitda):
    res = (((((((capex * 53.6514 - ebitda).rolling(11).max()).rolling(2).mean()).rolling(4).var()).rolling(25).mean()) * 0.471622).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_5d_slope_v052_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_5d_slope_v052_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_21d_slope_v053_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 45.2919)).diff(1)).pct_change(11)).rolling(12).std()) * 0.796483).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_21d_slope_v053_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_21d_slope_v053_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_10d_slope_v054_signal(capex, ebitda):
    res = (((((capex.diff(19) / (ebitda.shift(3) + 16.5567)).diff(12)).rolling(19).min()) * 0.640266).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_10d_slope_v054_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_10d_slope_v054_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_slope_v055_signal(capex, ebitda):
    res = (((((capex / (ebitda + 75.9412)).rolling(5).var()).rolling(11).max()) * 0.523707).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_slope_v055_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_slope_v055_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_10d_slope_v056_signal(capex, ebitda):
    res = ((((((capex.diff(5) / (ebitda.shift(9) + 30.1981)).rolling(15).max()).pct_change(15)).rolling(25).var()) * 0.610999).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_10d_slope_v056_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_10d_slope_v056_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_63d_slope_v057_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 3.7376)).rolling(26).std()).rolling(17).var()).rolling(22).max()) * 0.093302).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_63d_slope_v057_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_63d_slope_v057_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_126d_slope_v058_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 99.5391)).rolling(25).max()).diff(15)).rolling(30).var()).rolling(28).std()) * 0.465366).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_126d_slope_v058_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_126d_slope_v058_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_63d_slope_v059_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(20).max()).rolling(24).var()).pct_change(1)) * 0.322558).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_63d_slope_v059_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_63d_slope_v059_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_252d_slope_v060_signal(capex, ebitda):
    res = (((((((capex * 27.8979 - ebitda).rolling(24).mean()).rolling(13).var()).rolling(18).std()).rolling(27).max()) * 0.574394).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_252d_slope_v060_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_252d_slope_v060_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_42d_slope_v061_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(16).std()).pct_change(9)) * 0.075344).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_42d_slope_v061_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_42d_slope_v061_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_42d_slope_v062_signal(capex, ebitda):
    res = (((((capex / (ebitda + 89.3786)).rolling(23).min()).rolling(4).max()) * 0.091334).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_42d_slope_v062_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_42d_slope_v062_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_63d_slope_v063_signal(capex, ebitda):
    res = (((((capex.diff(12) / (ebitda.shift(4) + 89.9019)).rolling(25).min()).rolling(21).min()) * 0.067414).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_63d_slope_v063_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_63d_slope_v063_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_10d_slope_v064_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(27).var()).pct_change(1)) * 0.841902).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_10d_slope_v064_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_10d_slope_v064_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_21d_slope_v065_signal(capex, ebitda):
    res = (((((((capex.diff(5) / (ebitda.shift(5) + 67.5637)).rolling(26).mean()).rolling(10).mean()).rolling(16).mean()).diff(5)) * 0.245581).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_21d_slope_v065_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_21d_slope_v065_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_5d_slope_v066_signal(capex, ebitda):
    res = ((((((capex * 72.0426 - ebitda).rolling(16).var()).rolling(29).var()).rolling(2).max()) * 0.345168).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_5d_slope_v066_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_5d_slope_v066_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_10d_slope_v067_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 83.4262)).rolling(3).min()).rolling(26).std()).rolling(9).std()) * 0.561838).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_10d_slope_v067_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_10d_slope_v067_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_63d_slope_v068_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 79.5033)).diff(18)).pct_change(5)).rolling(14).max()) * 0.672143).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_63d_slope_v068_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_63d_slope_v068_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_5d_slope_v069_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 28.0255)).rolling(21).max()).rolling(16).mean()).rolling(5).std()).rolling(11).min()) * 0.903415).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_5d_slope_v069_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_5d_slope_v069_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_63d_slope_v070_signal(capex, ebitda):
    res = (((((capex * 13.9696 - ebitda).rolling(13).mean()).diff(8)) * 0.138402).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_63d_slope_v070_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_63d_slope_v070_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_10d_slope_v071_signal(capex, ebitda):
    res = (((((ebitda / (capex + 89.9947)).pct_change(12)).pct_change(2)) * 0.384801).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_10d_slope_v071_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_10d_slope_v071_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_5d_slope_v072_signal(capex, ebitda):
    res = (((((capex.diff(17) / (ebitda.shift(1) + 83.9163)).rolling(6).std()).rolling(15).mean()) * 0.584642).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_5d_slope_v072_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_5d_slope_v072_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_126d_slope_v073_signal(capex, ebitda):
    res = (((((capex * 58.5454 - ebitda).rolling(21).min()).rolling(4).min()) * 0.114118).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_126d_slope_v073_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_126d_slope_v073_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_5d_slope_v074_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 0.306)).rolling(7).std()).pct_change(11)).rolling(24).min()) * 0.643205).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_5d_slope_v074_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_5d_slope_v074_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_126d_slope_v075_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 49.2737)).rolling(20).min()).rolling(27).max()).rolling(9).std()).rolling(11).mean()) * 0.51384).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_126d_slope_v075_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_126d_slope_v075_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_126d_slope_v076_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(3)).rolling(12).var()).rolling(11).min()).rolling(25).min()) * 0.222851).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_126d_slope_v076_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_126d_slope_v076_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_252d_slope_v077_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 24.5818)).rolling(24).max()).rolling(4).mean()).diff(15)).rolling(15).min()) * 0.022592).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_252d_slope_v077_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_252d_slope_v077_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_126d_slope_v078_signal(capex, ebitda):
    res = (((((ebitda / (capex + 42.8583)).pct_change(19)).rolling(19).std()) * 0.067245).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_126d_slope_v078_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_126d_slope_v078_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_252d_slope_v079_signal(capex, ebitda):
    res = (((((((capex.pct_change(14) / ebitda.pct_change(3)).rolling(6).mean()).rolling(9).std()).rolling(23).mean()).rolling(14).mean()) * 0.324729).diff(16).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_252d_slope_v079_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_252d_slope_v079_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_126d_slope_v080_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 54.7547)).rolling(6).std()).rolling(8).std()).diff(16)) * 0.918814).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_126d_slope_v080_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_126d_slope_v080_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_63d_slope_v081_signal(capex, ebitda):
    res = (((((((capex.pct_change(17) / ebitda.pct_change(10)).rolling(15).var()).rolling(17).std()).rolling(4).mean()).rolling(29).var()) * 0.162206).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_63d_slope_v081_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_63d_slope_v081_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_63d_slope_v082_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 31.2257)).pct_change(18)).rolling(24).max()).rolling(29).std()).rolling(24).std()) * 0.031142).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_63d_slope_v082_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_63d_slope_v082_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_10d_slope_v083_signal(capex, ebitda):
    res = (((((capex * 14.4058 - ebitda).rolling(17).std()).pct_change(18)) * 0.438607).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_10d_slope_v083_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_10d_slope_v083_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_5d_slope_v084_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 49.1398)).rolling(18).std()).rolling(3).std()).rolling(5).mean()) * 0.552669).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_5d_slope_v084_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_5d_slope_v084_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_126d_slope_v085_signal(capex, ebitda):
    res = (((((capex.diff(12) / (ebitda.shift(3) + 87.0927)).rolling(16).min()).pct_change(8)) * 0.808235).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_126d_slope_v085_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_126d_slope_v085_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_5d_slope_v086_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 80.5677)).pct_change(12)).diff(13)).rolling(26).var()) * 0.488095).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_5d_slope_v086_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_5d_slope_v086_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_63d_slope_v087_signal(capex, ebitda):
    res = ((((((capex * 46.9792 - ebitda).rolling(7).std()).rolling(28).var()).pct_change(19)) * 0.412518).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_63d_slope_v087_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_63d_slope_v087_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_126d_slope_v088_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 36.8241)).rolling(6).max()).rolling(15).max()).rolling(14).var()) * 0.127907).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_126d_slope_v088_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_126d_slope_v088_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_21d_slope_v089_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(7).min()).rolling(9).max()).diff(11)).diff(1)) * 0.150135).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_21d_slope_v089_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_21d_slope_v089_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_42d_slope_v090_signal(capex, ebitda):
    res = (((((capex * 58.4722 - ebitda).rolling(15).var()).pct_change(12)) * 0.221201).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_42d_slope_v090_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_42d_slope_v090_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_10d_slope_v091_signal(capex, ebitda):
    res = ((((((capex.diff(16) / (ebitda.shift(8) + 14.8197)).rolling(25).min()).rolling(16).max()).pct_change(5)) * 0.201966).diff(12).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_10d_slope_v091_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_10d_slope_v091_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_5d_slope_v092_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 86.4155)).rolling(18).max()).rolling(4).std()).rolling(16).var()).rolling(23).max()) * 0.295481).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_5d_slope_v092_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_5d_slope_v092_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_252d_slope_v093_signal(capex, ebitda):
    res = (((((capex.diff(5) / (ebitda.shift(1) + 24.3772)).diff(13)).rolling(14).min()) * 0.445813).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_252d_slope_v093_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_252d_slope_v093_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_5d_slope_v094_signal(capex, ebitda):
    res = (((((ebitda / (capex + 39.6029)).rolling(4).mean()).rolling(30).std()) * 0.408856).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_5d_slope_v094_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_5d_slope_v094_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_5d_slope_v095_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 82.1884)).pct_change(9)).pct_change(18)).rolling(8).std()) * 0.834191).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_5d_slope_v095_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_5d_slope_v095_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_42d_slope_v096_signal(capex, ebitda):
    res = (((((((capex.pct_change(17) / ebitda.pct_change(6)).rolling(14).max()).rolling(25).min()).diff(3)).diff(7)) * 0.672181).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_42d_slope_v096_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_42d_slope_v096_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_5d_slope_v097_signal(capex, ebitda):
    res = (((((capex * 85.1969 - ebitda).rolling(19).mean()).rolling(15).var()) * 0.637313).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_5d_slope_v097_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_5d_slope_v097_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_63d_slope_v098_signal(capex, ebitda):
    res = (((((capex.diff(7) / (ebitda.shift(3) + 71.5477)).rolling(8).max()).rolling(3).var()) * 0.060959).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_63d_slope_v098_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_63d_slope_v098_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_5d_slope_v099_signal(capex, ebitda):
    res = (((((((capex * 10.9173 - ebitda).diff(2)).rolling(30).max()).rolling(8).mean()).rolling(25).max()) * 0.335166).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_5d_slope_v099_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_5d_slope_v099_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_63d_slope_v100_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 63.9283)).rolling(10).mean()).rolling(4).std()).rolling(14).var()) * 0.723688).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_63d_slope_v100_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_63d_slope_v100_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_63d_slope_v101_signal(capex, ebitda):
    res = (((((((capex.diff(11) / (ebitda.shift(4) + 34.0591)).diff(7)).rolling(11).min()).rolling(12).min()).rolling(18).var()) * 0.683362).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_63d_slope_v101_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_63d_slope_v101_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_10d_slope_v102_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(5).min()).rolling(28).min()).pct_change(15)) * 0.636378).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_10d_slope_v102_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_10d_slope_v102_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_21d_slope_v103_signal(capex, ebitda):
    res = (((((capex.pct_change(5) / ebitda.pct_change(15)).rolling(30).min()).rolling(18).max()) * 0.952825).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_21d_slope_v103_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_21d_slope_v103_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_126d_slope_v104_signal(capex, ebitda):
    res = (((((((capex.diff(4) / (ebitda.shift(7) + 70.3581)).rolling(15).min()).pct_change(17)).rolling(5).min()).rolling(20).mean()) * 0.484058).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_126d_slope_v104_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_126d_slope_v104_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_42d_slope_v105_signal(capex, ebitda):
    res = (((((capex.pct_change(17) / ebitda.pct_change(7)).rolling(15).std()).rolling(17).mean()) * 0.387673).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_42d_slope_v105_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_42d_slope_v105_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_126d_slope_v106_signal(capex, ebitda):
    res = ((((((capex.diff(18) / (ebitda.shift(4) + 32.1527)).diff(18)).rolling(20).mean()).rolling(15).var()) * 0.037522).diff(11).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_126d_slope_v106_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_126d_slope_v106_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_42d_slope_v107_signal(capex, ebitda):
    res = (((((((capex * 70.5884 - ebitda).rolling(26).max()).pct_change(17)).rolling(11).std()).rolling(14).std()) * 0.544524).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_42d_slope_v107_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_42d_slope_v107_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_126d_slope_v108_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 14.2884)).rolling(19).var()).pct_change(9)).rolling(15).min()).rolling(17).max()) * 0.468762).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_126d_slope_v108_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_126d_slope_v108_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_252d_slope_v109_signal(capex, ebitda):
    res = (((((capex.diff(7) / (ebitda.shift(1) + 20.8809)).rolling(30).std()).pct_change(15)) * 0.808492).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_252d_slope_v109_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_252d_slope_v109_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_42d_slope_v110_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 75.4196)).rolling(27).var()).diff(2)).rolling(12).std()).rolling(29).std()) * 0.431398).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_42d_slope_v110_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_42d_slope_v110_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_21d_slope_v111_signal(capex, ebitda):
    res = (((((ebitda / (capex + 94.3444)).rolling(20).max()).rolling(6).min()) * 0.42794).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_21d_slope_v111_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_21d_slope_v111_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_126d_slope_v112_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(4)).rolling(30).mean()).pct_change(17)) * 0.822078).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_126d_slope_v112_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_126d_slope_v112_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_10d_slope_v113_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 31.972)).rolling(2).mean()).rolling(4).min()).rolling(4).std()).rolling(28).mean()) * 0.689428).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_10d_slope_v113_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_10d_slope_v113_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_126d_slope_v114_signal(capex, ebitda):
    res = (((((capex.pct_change(16) / ebitda.pct_change(7)).rolling(25).var()).diff(16)) * 0.147996).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_126d_slope_v114_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_126d_slope_v114_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_42d_slope_v115_signal(capex, ebitda):
    res = ((((((capex.pct_change(19) / ebitda.pct_change(19)).rolling(14).mean()).rolling(24).var()).rolling(15).max()) * 0.616663).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_42d_slope_v115_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_42d_slope_v115_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_252d_slope_v116_signal(capex, ebitda):
    res = (((((((capex * 39.9362 - ebitda).diff(13)).rolling(29).max()).rolling(8).std()).rolling(26).var()) * 0.764272).diff(9).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_252d_slope_v116_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_252d_slope_v116_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_5d_slope_v117_signal(capex, ebitda):
    res = ((((((capex.pct_change(10) / ebitda.pct_change(5)).diff(12)).rolling(26).std()).rolling(21).min()) * 0.709132).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_5d_slope_v117_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_5d_slope_v117_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_126d_slope_v118_signal(capex, ebitda):
    res = (((((((capex * 18.3117 - ebitda).rolling(16).mean()).rolling(13).mean()).diff(10)).rolling(23).min()) * 0.831033).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_126d_slope_v118_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_126d_slope_v118_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_42d_slope_v119_signal(capex, ebitda):
    res = (((((capex.diff(16) / (ebitda.shift(10) + 5.1019)).diff(4)).rolling(4).mean()) * 0.121737).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_42d_slope_v119_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_42d_slope_v119_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_126d_slope_v120_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 82.8975)).rolling(19).var()).rolling(24).max()).rolling(23).std()) * 0.158364).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_126d_slope_v120_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_126d_slope_v120_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_252d_slope_v121_signal(capex, ebitda):
    res = ((((((capex.diff(15) / (ebitda.shift(9) + 46.9258)).rolling(18).max()).diff(7)).rolling(17).var()) * 0.339539).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_252d_slope_v121_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_252d_slope_v121_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_63d_slope_v122_signal(capex, ebitda):
    res = ((((((capex.diff(13) / (ebitda.shift(8) + 18.7704)).rolling(30).std()).diff(17)).rolling(22).min()) * 0.288014).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_63d_slope_v122_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_63d_slope_v122_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_252d_slope_v123_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(28).std()).diff(14)).rolling(13).min()).rolling(26).std()) * 0.825119).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_252d_slope_v123_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_252d_slope_v123_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_10d_slope_v124_signal(capex, ebitda):
    res = (((((capex.pct_change(6) / ebitda.pct_change(16)).rolling(2).var()).rolling(27).mean()) * 0.537952).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_10d_slope_v124_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_10d_slope_v124_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_126d_slope_v125_signal(capex, ebitda):
    res = (((((capex.pct_change(18) / ebitda.pct_change(13)).rolling(11).mean()).diff(13)) * 0.671795).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_126d_slope_v125_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_126d_slope_v125_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_21d_slope_v126_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(22).min()).rolling(25).std()) * 0.033606).diff(2).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_21d_slope_v126_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_21d_slope_v126_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_126d_slope_v127_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(7)).pct_change(1)).rolling(3).mean()).rolling(25).mean()) * 0.204185).diff(2).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_126d_slope_v127_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_126d_slope_v127_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_63d_slope_v128_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(25).mean()).rolling(27).mean()).rolling(29).var()).pct_change(18)) * 0.81434).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_63d_slope_v128_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_63d_slope_v128_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_10d_slope_v129_signal(capex, ebitda):
    res = (((((((capex.diff(8) / (ebitda.shift(6) + 52.7201)).rolling(26).max()).rolling(21).std()).diff(2)).rolling(25).max()) * 0.972749).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_10d_slope_v129_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_10d_slope_v129_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_5d_slope_v130_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 92.3539)).rolling(7).min()).rolling(22).max()).rolling(18).mean()) * 0.702152).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_5d_slope_v130_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_5d_slope_v130_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_10d_slope_v131_signal(capex, ebitda):
    res = ((((((capex * 98.506 - ebitda).pct_change(15)).diff(9)).pct_change(15)) * 0.670892).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_10d_slope_v131_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_10d_slope_v131_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_252d_slope_v132_signal(capex, ebitda):
    res = (((((((capex.pct_change(2) / ebitda.pct_change(12)).rolling(23).std()).pct_change(8)).rolling(29).mean()).rolling(15).max()) * 0.713452).diff(16).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_252d_slope_v132_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_252d_slope_v132_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_10d_slope_v133_signal(capex, ebitda):
    res = (((((capex * 60.5056 - ebitda).diff(10)).rolling(23).std()) * 0.616359).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_10d_slope_v133_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_10d_slope_v133_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_63d_slope_v134_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(24).min()).pct_change(4)).rolling(17).max()) * 0.988724).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_63d_slope_v134_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_63d_slope_v134_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_slope_v135_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 86.9863)).rolling(18).max()).diff(12)).rolling(4).mean()) * 0.13276).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_slope_v135_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_slope_v135_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_252d_slope_v136_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 78.2534)).rolling(15).min()).rolling(18).min()).pct_change(17)) * 0.168236).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_252d_slope_v136_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_252d_slope_v136_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_63d_slope_v137_signal(capex, ebitda):
    res = (((((ebitda / (capex + 69.9538)).rolling(22).max()).rolling(23).max()) * 0.200822).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_63d_slope_v137_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_63d_slope_v137_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_63d_slope_v138_signal(capex, ebitda):
    res = (((((capex * 0.1675 - ebitda).rolling(12).std()).rolling(21).var()) * 0.295605).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_63d_slope_v138_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_63d_slope_v138_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_42d_slope_v139_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 46.5388)).pct_change(7)).rolling(13).max()).diff(18)).rolling(12).mean()) * 0.435157).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_42d_slope_v139_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_42d_slope_v139_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_5d_slope_v140_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(19).min()).rolling(8).max()).rolling(4).max()) * 0.932367).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_5d_slope_v140_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_5d_slope_v140_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_63d_slope_v141_signal(capex, ebitda):
    res = ((((((capex * 95.7309 - ebitda).rolling(22).mean()).rolling(28).mean()).rolling(18).var()) * 0.855713).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_63d_slope_v141_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_63d_slope_v141_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_5d_slope_v142_signal(capex, ebitda):
    res = ((((((capex.diff(2) / (ebitda.shift(1) + 5.7026)).rolling(24).max()).diff(6)).rolling(16).max()) * 0.648459).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_5d_slope_v142_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_5d_slope_v142_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_252d_slope_v143_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 88.9105)).rolling(2).std()).rolling(5).mean()).diff(5)).rolling(22).var()) * 0.352589).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_252d_slope_v143_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_252d_slope_v143_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_5d_slope_v144_signal(capex, ebitda):
    res = (((((capex * 64.4102 - ebitda).rolling(23).min()).diff(20)) * 0.393597).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_5d_slope_v144_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_5d_slope_v144_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_10d_slope_v145_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 99.5468)).rolling(2).max()).rolling(7).min()).rolling(2).mean()).pct_change(16)) * 0.16881).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_10d_slope_v145_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_10d_slope_v145_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_5d_slope_v146_signal(capex, ebitda):
    res = (((((((capex.diff(6) / (ebitda.shift(7) + 94.048)).pct_change(19)).rolling(13).min()).rolling(17).std()).pct_change(10)) * 0.806139).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_5d_slope_v146_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_5d_slope_v146_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_126d_slope_v147_signal(capex, ebitda):
    res = (((((((capex.pct_change(10) / ebitda.pct_change(13)).rolling(30).var()).rolling(23).min()).pct_change(16)).rolling(3).var()) * 0.494922).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_126d_slope_v147_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_126d_slope_v147_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_63d_slope_v148_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 90.3315)).rolling(25).var()).rolling(10).mean()).rolling(22).min()) * 0.783206).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_63d_slope_v148_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_63d_slope_v148_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_63d_slope_v149_signal(capex, ebitda):
    res = (((((((capex.pct_change(17) / ebitda.pct_change(7)).pct_change(9)).rolling(8).max()).pct_change(10)).rolling(25).max()) * 0.659407).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_63d_slope_v149_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_63d_slope_v149_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_126d_slope_v150_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(14).min()).pct_change(10)) * 0.35611).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_126d_slope_v150_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_126d_slope_v150_signal


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
