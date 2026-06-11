import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_21d_jerk_v001_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(30).max()).rolling(11).max()) * 0.038713).diff(8).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_21d_jerk_v001_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_21d_jerk_v001_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_252d_jerk_v002_signal(capex, ebitda):
    res = (((((capex.diff(20) / (ebitda.shift(9) + 88.3938)).pct_change(14)).rolling(24).max()) * 0.410343).diff(11).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_252d_jerk_v002_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_252d_jerk_v002_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_5d_jerk_v003_signal(capex, ebitda):
    res = (((((capex.pct_change(2) / ebitda.pct_change(12)).rolling(7).max()).rolling(10).max()) * 0.757896).diff(13).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_5d_jerk_v003_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_5d_jerk_v003_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_10d_jerk_v004_signal(capex, ebitda):
    res = (((((capex * 73.3084 - ebitda).rolling(3).max()).diff(15)) * 0.018027).diff(15).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_10d_jerk_v004_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_10d_jerk_v004_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_126d_jerk_v005_signal(capex, ebitda):
    res = (((((((capex.pct_change(9) / ebitda.pct_change(12)).diff(1)).rolling(19).std()).rolling(4).mean()).rolling(6).min()) * 0.149041).diff(11).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_126d_jerk_v005_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_126d_jerk_v005_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_21d_jerk_v006_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 11.0829)).rolling(19).std()).rolling(11).mean()).rolling(12).std()).rolling(30).std()) * 0.047683).diff(3).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_21d_jerk_v006_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_21d_jerk_v006_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_42d_jerk_v007_signal(capex, ebitda):
    res = (((((capex.diff(8) / (ebitda.shift(4) + 59.7028)).rolling(27).mean()).diff(4)) * 0.766343).diff(4).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_42d_jerk_v007_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_42d_jerk_v007_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_10d_jerk_v008_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 65.7164)).pct_change(9)).rolling(19).std()).rolling(28).min()) * 0.574582).diff(13).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_10d_jerk_v008_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_10d_jerk_v008_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_252d_jerk_v009_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 66.817)).rolling(19).std()).diff(12)).rolling(11).var()).rolling(4).var()) * 0.118789).diff(9).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_252d_jerk_v009_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_252d_jerk_v009_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_5d_jerk_v010_signal(capex, ebitda):
    res = (((((capex / (ebitda + 79.8388)).rolling(23).min()).rolling(13).var()) * 0.817321).diff(12).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_5d_jerk_v010_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_5d_jerk_v010_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_252d_jerk_v011_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 68.4579)).pct_change(4)).rolling(16).min()).rolling(9).std()).rolling(10).min()) * 0.684865).diff(13).diff(4).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_252d_jerk_v011_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_252d_jerk_v011_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_252d_jerk_v012_signal(capex, ebitda):
    res = (((((((capex.pct_change(12) / ebitda.pct_change(14)).pct_change(6)).pct_change(14)).rolling(30).var()).rolling(7).mean()) * 0.095132).diff(14).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_252d_jerk_v012_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_252d_jerk_v012_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_63d_jerk_v013_signal(capex, ebitda):
    res = (((((((capex * 25.8281 - ebitda).rolling(15).mean()).rolling(9).max()).rolling(21).mean()).pct_change(14)) * 0.126158).diff(8).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_63d_jerk_v013_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_63d_jerk_v013_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_252d_jerk_v014_signal(capex, ebitda):
    res = ((((((capex.pct_change(3) / ebitda.pct_change(14)).rolling(11).mean()).rolling(3).var()).diff(11)) * 0.914488).diff(20).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_252d_jerk_v014_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_252d_jerk_v014_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_63d_jerk_v015_signal(capex, ebitda):
    res = (((((ebitda / (capex + 14.3696)).rolling(27).var()).rolling(28).std()) * 0.814471).diff(17).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_63d_jerk_v015_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_63d_jerk_v015_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_63d_jerk_v016_signal(capex, ebitda):
    res = (((((capex / (ebitda + 95.7312)).rolling(21).var()).pct_change(8)) * 0.312405).diff(13).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_63d_jerk_v016_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_63d_jerk_v016_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_21d_jerk_v017_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 4.7152)).rolling(17).std()).rolling(26).var()).rolling(16).var()) * 0.675931).diff(13).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_21d_jerk_v017_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_21d_jerk_v017_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_10d_jerk_v018_signal(capex, ebitda):
    res = ((((((capex.pct_change(19) / ebitda.pct_change(1)).diff(9)).rolling(30).std()).rolling(18).mean()) * 0.072645).diff(7).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_10d_jerk_v018_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_10d_jerk_v018_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_10d_jerk_v019_signal(capex, ebitda):
    res = (((((((capex.pct_change(2) / ebitda.pct_change(6)).rolling(17).min()).rolling(23).mean()).diff(4)).rolling(2).var()) * 0.612736).diff(14).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_10d_jerk_v019_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_10d_jerk_v019_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_126d_jerk_v020_signal(capex, ebitda):
    res = (((((capex.diff(15) / (ebitda.shift(10) + 58.4962)).rolling(8).min()).pct_change(6)) * 0.939749).diff(17).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_126d_jerk_v020_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_126d_jerk_v020_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_252d_jerk_v021_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 42.7933)).rolling(7).std()).rolling(20).mean()).rolling(9).max()).rolling(20).min()) * 0.681602).diff(3).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_252d_jerk_v021_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_252d_jerk_v021_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_42d_jerk_v022_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 21.8613)).rolling(23).max()).rolling(17).min()).rolling(16).mean()).diff(10)) * 0.461299).diff(12).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_42d_jerk_v022_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_42d_jerk_v022_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_126d_jerk_v023_signal(capex, ebitda):
    res = ((((((capex.diff(12) / (ebitda.shift(4) + 61.9132)).rolling(2).mean()).pct_change(6)).rolling(6).mean()) * 0.724416).diff(13).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_126d_jerk_v023_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_126d_jerk_v023_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_10d_jerk_v024_signal(capex, ebitda):
    res = (((((capex / (ebitda + 56.0901)).rolling(12).max()).rolling(14).max()) * 0.553853).diff(15).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_10d_jerk_v024_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_10d_jerk_v024_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_5d_jerk_v025_signal(capex, ebitda):
    res = ((((((capex.diff(9) / (ebitda.shift(1) + 23.8502)).diff(15)).diff(12)).rolling(22).var()) * 0.773529).diff(3).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_5d_jerk_v025_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_5d_jerk_v025_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_126d_jerk_v026_signal(capex, ebitda):
    res = (((((capex / (ebitda + 72.3878)).rolling(28).std()).rolling(23).max()) * 0.245292).diff(5).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_126d_jerk_v026_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_126d_jerk_v026_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_10d_jerk_v027_signal(capex, ebitda):
    res = ((((((capex.diff(11) / (ebitda.shift(2) + 7.2599)).rolling(5).mean()).rolling(11).max()).rolling(6).std()) * 0.863921).diff(1).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_10d_jerk_v027_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_10d_jerk_v027_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_10d_jerk_v028_signal(capex, ebitda):
    res = (((((((capex * 53.5882 - ebitda).rolling(23).std()).diff(3)).pct_change(13)).rolling(5).max()) * 0.545967).diff(14).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_10d_jerk_v028_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_10d_jerk_v028_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_42d_jerk_v029_signal(capex, ebitda):
    res = ((((((capex.pct_change(16) / ebitda.pct_change(8)).rolling(2).max()).rolling(25).min()).rolling(20).max()) * 0.242808).diff(10).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_42d_jerk_v029_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_42d_jerk_v029_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_42d_jerk_v030_signal(capex, ebitda):
    res = (((((((capex.diff(1) / (ebitda.shift(6) + 48.2661)).diff(4)).pct_change(2)).rolling(2).min()).rolling(5).min()) * 0.05525).diff(14).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_42d_jerk_v030_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_42d_jerk_v030_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_21d_jerk_v031_signal(capex, ebitda):
    res = (((((capex / (ebitda + 56.1068)).rolling(16).std()).rolling(18).mean()) * 0.863934).diff(12).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_21d_jerk_v031_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_21d_jerk_v031_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_252d_jerk_v032_signal(capex, ebitda):
    res = ((((((capex.diff(3) / (ebitda.shift(10) + 11.1019)).rolling(15).var()).rolling(17).max()).rolling(21).std()) * 0.775459).diff(13).diff(12).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_252d_jerk_v032_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_252d_jerk_v032_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_21d_jerk_v033_signal(capex, ebitda):
    res = (((((capex / (ebitda + 39.0096)).rolling(16).min()).diff(4)) * 0.122586).diff(17).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_21d_jerk_v033_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_21d_jerk_v033_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_42d_jerk_v034_signal(capex, ebitda):
    res = (((((capex / (ebitda + 75.0333)).diff(13)).pct_change(13)) * 0.839528).diff(15).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_42d_jerk_v034_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_42d_jerk_v034_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_10d_jerk_v035_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 94.0016)).pct_change(17)).rolling(25).min()).rolling(28).var()).rolling(7).mean()) * 0.37481).diff(5).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_10d_jerk_v035_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_10d_jerk_v035_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_126d_jerk_v036_signal(capex, ebitda):
    res = ((((((capex.diff(10) / (ebitda.shift(7) + 65.5621)).rolling(7).min()).rolling(15).min()).rolling(25).std()) * 0.71304).diff(7).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_126d_jerk_v036_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_126d_jerk_v036_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_21d_jerk_v037_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 95.1477)).diff(4)).rolling(7).var()).rolling(18).var()).rolling(5).std()) * 0.118241).diff(20).diff(13).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_21d_jerk_v037_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_21d_jerk_v037_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_63d_jerk_v038_signal(capex, ebitda):
    res = ((((((capex.diff(14) / (ebitda.shift(5) + 73.7385)).rolling(14).var()).rolling(20).max()).rolling(20).min()) * 0.213065).diff(17).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_63d_jerk_v038_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_63d_jerk_v038_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_5d_jerk_v039_signal(capex, ebitda):
    res = (((((capex * 21.7234 - ebitda).rolling(23).min()).rolling(22).max()) * 0.550182).diff(8).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_5d_jerk_v039_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_5d_jerk_v039_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_126d_jerk_v040_signal(capex, ebitda):
    res = (((((((capex.pct_change(6) / ebitda.pct_change(5)).rolling(23).mean()).diff(6)).rolling(3).min()).rolling(12).min()) * 0.836081).diff(20).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_126d_jerk_v040_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_126d_jerk_v040_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_jerk_v041_signal(capex, ebitda):
    res = (((((capex / (ebitda + 6.535)).rolling(16).max()).rolling(6).std()) * 0.899686).diff(17).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_jerk_v041_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_jerk_v041_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_21d_jerk_v042_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).max()).rolling(22).min()).rolling(29).mean()).pct_change(16)) * 0.518222).diff(11).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_21d_jerk_v042_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_21d_jerk_v042_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_63d_jerk_v043_signal(capex, ebitda):
    res = (((((((capex.diff(17) / (ebitda.shift(5) + 61.3209)).rolling(16).max()).rolling(21).max()).rolling(12).mean()).rolling(29).std()) * 0.784257).diff(5).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_63d_jerk_v043_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_63d_jerk_v043_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_42d_jerk_v044_signal(capex, ebitda):
    res = (((((((capex * 12.5115 - ebitda).rolling(19).mean()).rolling(19).max()).diff(4)).rolling(15).mean()) * 0.283576).diff(3).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_42d_jerk_v044_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_42d_jerk_v044_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_10d_jerk_v045_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(4)).rolling(21).std()) * 0.681017).diff(15).diff(12).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_10d_jerk_v045_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_10d_jerk_v045_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_252d_jerk_v046_signal(capex, ebitda):
    res = (((((((capex.diff(14) / (ebitda.shift(2) + 35.3047)).rolling(8).min()).rolling(19).min()).rolling(4).max()).rolling(20).mean()) * 0.811617).diff(7).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_252d_jerk_v046_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_252d_jerk_v046_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_252d_jerk_v047_signal(capex, ebitda):
    res = (((((capex * 69.0052 - ebitda).diff(2)).rolling(26).mean()) * 0.588178).diff(7).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_252d_jerk_v047_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_252d_jerk_v047_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_42d_jerk_v048_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(7)).rolling(5).min()) * 0.981286).diff(8).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_42d_jerk_v048_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_42d_jerk_v048_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_42d_jerk_v049_signal(capex, ebitda):
    res = (((((((capex.diff(9) / (ebitda.shift(10) + 61.4306)).rolling(28).max()).rolling(9).mean()).rolling(23).min()).rolling(21).std()) * 0.526346).diff(12).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_42d_jerk_v049_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_42d_jerk_v049_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_21d_jerk_v050_signal(capex, ebitda):
    res = (((((((capex.pct_change(14) / ebitda.pct_change(8)).rolling(19).max()).pct_change(4)).rolling(17).std()).pct_change(9)) * 0.33625).diff(7).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_21d_jerk_v050_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_21d_jerk_v050_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_126d_jerk_v051_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 15.4973)).diff(6)).rolling(19).var()).rolling(22).mean()).diff(9)) * 0.902561).diff(16).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_126d_jerk_v051_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_126d_jerk_v051_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_10d_jerk_v052_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 90.4699)).rolling(14).max()).rolling(20).std()).rolling(10).max()).rolling(10).var()) * 0.114168).diff(4).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_10d_jerk_v052_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_10d_jerk_v052_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_126d_jerk_v053_signal(capex, ebitda):
    res = (((((ebitda / (capex + 77.2788)).rolling(9).max()).rolling(30).mean()) * 0.256655).diff(16).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_126d_jerk_v053_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_126d_jerk_v053_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_42d_jerk_v054_signal(capex, ebitda):
    res = (((((((capex.pct_change(19) / ebitda.pct_change(14)).rolling(13).var()).pct_change(19)).rolling(16).max()).rolling(22).std()) * 0.732141).diff(9).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_42d_jerk_v054_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_42d_jerk_v054_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_jerk_v055_signal(capex, ebitda):
    res = (((((capex.pct_change(15) / ebitda.pct_change(16)).rolling(22).var()).pct_change(3)) * 0.609053).diff(14).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_jerk_v055_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_jerk_v055_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_63d_jerk_v056_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(17).mean()).diff(5)).rolling(17).mean()) * 0.869798).diff(8).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_63d_jerk_v056_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_63d_jerk_v056_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_5d_jerk_v057_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 70.6641)).rolling(18).max()).pct_change(8)).pct_change(2)).rolling(23).min()) * 0.186655).diff(8).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_5d_jerk_v057_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_5d_jerk_v057_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_126d_jerk_v058_signal(capex, ebitda):
    res = ((((((capex.pct_change(18) / ebitda.pct_change(4)).rolling(10).var()).rolling(11).std()).pct_change(18)) * 0.316418).diff(9).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_126d_jerk_v058_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_126d_jerk_v058_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_126d_jerk_v059_signal(capex, ebitda):
    res = (((((((capex.pct_change(12) / ebitda.pct_change(1)).rolling(16).var()).rolling(13).min()).diff(3)).rolling(23).mean()) * 0.040201).diff(17).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_126d_jerk_v059_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_126d_jerk_v059_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_126d_jerk_v060_signal(capex, ebitda):
    res = (((((capex.diff(9) / (ebitda.shift(1) + 6.6061)).rolling(17).var()).rolling(8).var()) * 0.339636).diff(20).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_126d_jerk_v060_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_126d_jerk_v060_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_63d_jerk_v061_signal(capex, ebitda):
    res = (((((capex.pct_change(11) / ebitda.pct_change(10)).rolling(28).var()).rolling(4).var()) * 0.88931).diff(20).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_63d_jerk_v061_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_63d_jerk_v061_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_63d_jerk_v062_signal(capex, ebitda):
    res = ((((((capex.diff(3) / (ebitda.shift(2) + 90.9389)).rolling(21).var()).rolling(7).var()).diff(19)) * 0.185502).diff(19).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_63d_jerk_v062_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_63d_jerk_v062_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_5d_jerk_v063_signal(capex, ebitda):
    res = (((((((capex * 63.4539 - ebitda).rolling(21).min()).rolling(26).std()).rolling(20).std()).rolling(9).var()) * 0.18101).diff(8).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_5d_jerk_v063_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_5d_jerk_v063_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_42d_jerk_v064_signal(capex, ebitda):
    res = (((((capex.pct_change(7) / ebitda.pct_change(20)).pct_change(20)).pct_change(8)) * 0.255047).diff(10).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_42d_jerk_v064_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_42d_jerk_v064_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_21d_jerk_v065_signal(capex, ebitda):
    res = (((((capex.pct_change(13) / ebitda.pct_change(14)).rolling(25).max()).rolling(10).std()) * 0.851489).diff(14).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_21d_jerk_v065_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_21d_jerk_v065_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_10d_jerk_v066_signal(capex, ebitda):
    res = (((((capex.diff(18) / (ebitda.shift(10) + 80.6147)).rolling(13).min()).rolling(25).mean()) * 0.671055).diff(17).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_10d_jerk_v066_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_10d_jerk_v066_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_42d_jerk_v067_signal(capex, ebitda):
    res = (((((capex.diff(2) / (ebitda.shift(9) + 90.2627)).rolling(9).var()).diff(18)) * 0.259314).diff(6).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_42d_jerk_v067_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_42d_jerk_v067_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_63d_jerk_v068_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 94.477)).pct_change(1)).rolling(29).max()).rolling(7).var()) * 0.553395).diff(18).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_63d_jerk_v068_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_63d_jerk_v068_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_252d_jerk_v069_signal(capex, ebitda):
    res = ((((((capex * 62.1842 - ebitda).pct_change(20)).pct_change(14)).rolling(12).var()) * 0.375753).diff(7).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_252d_jerk_v069_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_252d_jerk_v069_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_63d_jerk_v070_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(18)).rolling(8).max()) * 0.854649).diff(1).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_63d_jerk_v070_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_63d_jerk_v070_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_252d_jerk_v071_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(11).var()).diff(20)) * 0.586929).diff(13).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_252d_jerk_v071_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_252d_jerk_v071_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_63d_jerk_v072_signal(capex, ebitda):
    res = ((((((capex.diff(19) / (ebitda.shift(9) + 96.2909)).rolling(15).mean()).diff(4)).rolling(24).min()) * 0.431105).diff(1).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_63d_jerk_v072_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_63d_jerk_v072_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_63d_jerk_v073_signal(capex, ebitda):
    res = (((((capex / (ebitda + 5.2439)).pct_change(17)).rolling(27).var()) * 0.839354).diff(15).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_63d_jerk_v073_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_63d_jerk_v073_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_21d_jerk_v074_signal(capex, ebitda):
    res = ((((((capex.pct_change(11) / ebitda.pct_change(1)).rolling(19).mean()).diff(17)).rolling(2).min()) * 0.822684).diff(4).diff(13).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_21d_jerk_v074_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_21d_jerk_v074_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_42d_jerk_v075_signal(capex, ebitda):
    res = (((((((capex.diff(6) / (ebitda.shift(4) + 66.2524)).diff(14)).rolling(18).max()).rolling(2).var()).rolling(12).var()) * 0.265544).diff(1).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_42d_jerk_v075_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_42d_jerk_v075_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_252d_jerk_v076_signal(capex, ebitda):
    res = (((((capex.diff(19) / (ebitda.shift(4) + 40.9552)).rolling(28).std()).diff(9)) * 0.849735).diff(6).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_252d_jerk_v076_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc076_252d_jerk_v076_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_42d_jerk_v077_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(3).var()).pct_change(5)) * 0.82481).diff(11).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_42d_jerk_v077_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc077_42d_jerk_v077_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_252d_jerk_v078_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(27).max()).rolling(22).mean()).rolling(26).min()) * 0.245903).diff(8).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_252d_jerk_v078_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc078_252d_jerk_v078_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_126d_jerk_v079_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 28.8235)).rolling(13).max()).rolling(2).std()).diff(3)) * 0.249604).diff(1).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_126d_jerk_v079_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc079_126d_jerk_v079_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_252d_jerk_v080_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 76.4363)).diff(7)).rolling(26).mean()).rolling(22).var()).rolling(29).max()) * 0.440489).diff(12).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_252d_jerk_v080_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc080_252d_jerk_v080_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_252d_jerk_v081_signal(capex, ebitda):
    res = (((((capex / (ebitda + 90.3799)).rolling(12).min()).rolling(6).min()) * 0.489931).diff(2).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_252d_jerk_v081_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc081_252d_jerk_v081_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_126d_jerk_v082_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(20)).rolling(25).min()).diff(8)).rolling(5).std()) * 0.258655).diff(18).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_126d_jerk_v082_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc082_126d_jerk_v082_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_126d_jerk_v083_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).pct_change(2)).rolling(30).min()).rolling(28).std()).rolling(30).mean()) * 0.202253).diff(15).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_126d_jerk_v083_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc083_126d_jerk_v083_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_21d_jerk_v084_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(16).min()).rolling(12).max()) * 0.461764).diff(2).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_21d_jerk_v084_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc084_21d_jerk_v084_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_63d_jerk_v085_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(10).max()).diff(10)).diff(8)) * 0.553183).diff(10).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_63d_jerk_v085_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc085_63d_jerk_v085_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_126d_jerk_v086_signal(capex, ebitda):
    res = (((((capex / (ebitda + 33.4948)).rolling(14).min()).rolling(15).min()) * 0.585684).diff(18).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_126d_jerk_v086_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc086_126d_jerk_v086_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_21d_jerk_v087_signal(capex, ebitda):
    res = (((((capex.diff(1) / (ebitda.shift(8) + 2.5997)).rolling(21).var()).rolling(13).min()) * 0.864677).diff(7).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_21d_jerk_v087_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc087_21d_jerk_v087_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_5d_jerk_v088_signal(capex, ebitda):
    res = (((((capex * 7.6955 - ebitda).pct_change(2)).diff(2)) * 0.749293).diff(19).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_5d_jerk_v088_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc088_5d_jerk_v088_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_126d_jerk_v089_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 3.4464)).rolling(25).var()).rolling(12).var()).rolling(18).std()).pct_change(11)) * 0.41086).diff(14).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_126d_jerk_v089_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc089_126d_jerk_v089_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_10d_jerk_v090_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 34.2615)).diff(1)).pct_change(2)).rolling(16).var()).rolling(29).mean()) * 0.186688).diff(19).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_10d_jerk_v090_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc090_10d_jerk_v090_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_5d_jerk_v091_signal(capex, ebitda):
    res = (((((capex / (ebitda + 6.087)).rolling(24).max()).pct_change(20)) * 0.250605).diff(17).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_5d_jerk_v091_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc091_5d_jerk_v091_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_63d_jerk_v092_signal(capex, ebitda):
    res = ((((((capex.pct_change(18) / ebitda.pct_change(4)).rolling(8).max()).diff(15)).pct_change(9)) * 0.826877).diff(13).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_63d_jerk_v092_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc092_63d_jerk_v092_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_5d_jerk_v093_signal(capex, ebitda):
    res = (((((((capex.pct_change(3) / ebitda.pct_change(17)).rolling(18).min()).rolling(23).min()).rolling(10).mean()).diff(15)) * 0.310284).diff(19).diff(14).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_5d_jerk_v093_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc093_5d_jerk_v093_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_42d_jerk_v094_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 67.1543)).rolling(24).var()).rolling(13).std()).rolling(12).min()).rolling(20).max()) * 0.851329).diff(12).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_42d_jerk_v094_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc094_42d_jerk_v094_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_63d_jerk_v095_signal(capex, ebitda):
    res = (((((capex.pct_change(8) / ebitda.pct_change(1)).rolling(24).max()).rolling(17).std()) * 0.076443).diff(14).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_63d_jerk_v095_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc095_63d_jerk_v095_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_252d_jerk_v096_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(4).std()).rolling(3).var()) * 0.282675).diff(12).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_252d_jerk_v096_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc096_252d_jerk_v096_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_10d_jerk_v097_signal(capex, ebitda):
    res = ((((((capex.diff(13) / (ebitda.shift(1) + 87.5795)).pct_change(8)).rolling(19).std()).rolling(28).max()) * 0.531295).diff(3).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_10d_jerk_v097_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc097_10d_jerk_v097_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_42d_jerk_v098_signal(capex, ebitda):
    res = (((((capex.diff(6) / (ebitda.shift(5) + 73.3499)).rolling(8).mean()).rolling(21).var()) * 0.500336).diff(9).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_42d_jerk_v098_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc098_42d_jerk_v098_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_5d_jerk_v099_signal(capex, ebitda):
    res = (((((capex.pct_change(17) / ebitda.pct_change(16)).pct_change(12)).rolling(19).mean()) * 0.889248).diff(14).diff(14).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_5d_jerk_v099_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc099_5d_jerk_v099_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_21d_jerk_v100_signal(capex, ebitda):
    res = (((((capex / (ebitda + 92.5746)).rolling(4).var()).rolling(23).max()) * 0.857237).diff(7).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_21d_jerk_v100_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc100_21d_jerk_v100_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_10d_jerk_v101_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 35.5986)).rolling(21).std()).rolling(26).max()).rolling(13).max()) * 0.37641).diff(6).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_10d_jerk_v101_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc101_10d_jerk_v101_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_42d_jerk_v102_signal(capex, ebitda):
    res = ((((((capex * 55.0827 - ebitda).diff(3)).rolling(19).std()).rolling(12).min()) * 0.331311).diff(12).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_42d_jerk_v102_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc102_42d_jerk_v102_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_252d_jerk_v103_signal(capex, ebitda):
    res = (((((ebitda / (capex + 88.7212)).rolling(8).max()).pct_change(4)) * 0.858044).diff(19).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_252d_jerk_v103_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc103_252d_jerk_v103_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_21d_jerk_v104_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 53.2961)).rolling(28).mean()).rolling(29).var()).rolling(8).min()).rolling(6).var()) * 0.945502).diff(20).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_21d_jerk_v104_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc104_21d_jerk_v104_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_21d_jerk_v105_signal(capex, ebitda):
    res = (((((capex.pct_change(19) / ebitda.pct_change(15)).pct_change(2)).pct_change(19)) * 0.11074).diff(4).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_21d_jerk_v105_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc105_21d_jerk_v105_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_5d_jerk_v106_signal(capex, ebitda):
    res = (((((((capex.diff(7) / (ebitda.shift(5) + 51.5495)).rolling(4).min()).rolling(9).std()).rolling(12).mean()).diff(12)) * 0.161643).diff(12).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_5d_jerk_v106_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc106_5d_jerk_v106_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_252d_jerk_v107_signal(capex, ebitda):
    res = ((((((capex.diff(8) / (ebitda.shift(1) + 5.492)).rolling(16).mean()).rolling(19).min()).rolling(23).mean()) * 0.071516).diff(4).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_252d_jerk_v107_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc107_252d_jerk_v107_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_63d_jerk_v108_signal(capex, ebitda):
    res = ((((((capex.pct_change(18) / ebitda.pct_change(10)).rolling(16).var()).rolling(25).min()).pct_change(14)) * 0.735594).diff(8).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_63d_jerk_v108_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc108_63d_jerk_v108_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_21d_jerk_v109_signal(capex, ebitda):
    res = (((((capex / (ebitda + 98.7965)).rolling(21).min()).pct_change(20)) * 0.307504).diff(9).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_21d_jerk_v109_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc109_21d_jerk_v109_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_10d_jerk_v110_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(13)).diff(13)) * 0.31065).diff(20).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_10d_jerk_v110_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc110_10d_jerk_v110_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_5d_jerk_v111_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 5.9815)).rolling(14).mean()).rolling(6).max()).rolling(28).min()).rolling(6).max()) * 0.74868).diff(5).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_5d_jerk_v111_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc111_5d_jerk_v111_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_126d_jerk_v112_signal(capex, ebitda):
    res = ((((((capex * 81.0742 - ebitda).rolling(2).std()).rolling(8).max()).diff(9)) * 0.358723).diff(16).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_126d_jerk_v112_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc112_126d_jerk_v112_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_252d_jerk_v113_signal(capex, ebitda):
    res = (((((ebitda / (capex + 93.2466)).diff(12)).rolling(6).min()) * 0.094623).diff(5).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_252d_jerk_v113_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc113_252d_jerk_v113_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_126d_jerk_v114_signal(capex, ebitda):
    res = (((((((capex.pct_change(1) / ebitda.pct_change(2)).rolling(29).min()).rolling(19).var()).rolling(21).var()).rolling(25).min()) * 0.69939).diff(5).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_126d_jerk_v114_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc114_126d_jerk_v114_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_252d_jerk_v115_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 19.2183)).rolling(7).var()).diff(2)).rolling(23).var()) * 0.463819).diff(17).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_252d_jerk_v115_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc115_252d_jerk_v115_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_126d_jerk_v116_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 92.9818)).rolling(2).max()).rolling(27).std()).pct_change(6)) * 0.905257).diff(9).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_126d_jerk_v116_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc116_126d_jerk_v116_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_42d_jerk_v117_signal(capex, ebitda):
    res = (((((((capex.pct_change(15) / ebitda.pct_change(13)).rolling(3).var()).diff(19)).rolling(10).mean()).pct_change(3)) * 0.840254).diff(17).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_42d_jerk_v117_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc117_42d_jerk_v117_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_63d_jerk_v118_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(12)).rolling(27).min()).rolling(9).std()) * 0.3943).diff(17).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_63d_jerk_v118_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc118_63d_jerk_v118_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_42d_jerk_v119_signal(capex, ebitda):
    res = (((((((capex.pct_change(12) / ebitda.pct_change(14)).rolling(28).max()).rolling(4).std()).rolling(14).std()).diff(2)) * 0.918211).diff(14).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_42d_jerk_v119_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc119_42d_jerk_v119_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_10d_jerk_v120_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(17).var()).pct_change(19)) * 0.032569).diff(9).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_10d_jerk_v120_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc120_10d_jerk_v120_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_5d_jerk_v121_signal(capex, ebitda):
    res = (((((capex.diff(7) / (ebitda.shift(9) + 75.3912)).pct_change(9)).pct_change(17)) * 0.613091).diff(19).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_5d_jerk_v121_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc121_5d_jerk_v121_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_126d_jerk_v122_signal(capex, ebitda):
    res = (((((((capex * 24.6646 - ebitda).pct_change(4)).rolling(16).var()).pct_change(19)).diff(2)) * 0.175119).diff(12).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_126d_jerk_v122_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc122_126d_jerk_v122_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_21d_jerk_v123_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(2)).pct_change(19)) * 0.559578).diff(11).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_21d_jerk_v123_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc123_21d_jerk_v123_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_10d_jerk_v124_signal(capex, ebitda):
    res = ((((((capex * 65.785 - ebitda).pct_change(17)).diff(14)).pct_change(11)) * 0.395966).diff(13).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_10d_jerk_v124_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc124_10d_jerk_v124_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_63d_jerk_v125_signal(capex, ebitda):
    res = (((((((ebitda / (capex + 89.1028)).rolling(30).max()).rolling(26).mean()).pct_change(4)).rolling(8).max()) * 0.370209).diff(5).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_63d_jerk_v125_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc125_63d_jerk_v125_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_21d_jerk_v126_signal(capex, ebitda):
    res = (((((((capex * 21.0459 - ebitda).rolling(23).var()).pct_change(14)).rolling(15).min()).diff(16)) * 0.438054).diff(17).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_21d_jerk_v126_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc126_21d_jerk_v126_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_63d_jerk_v127_signal(capex, ebitda):
    res = ((((((capex.pct_change(16) / ebitda.pct_change(9)).rolling(12).max()).pct_change(19)).rolling(12).min()) * 0.282971).diff(5).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_63d_jerk_v127_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc127_63d_jerk_v127_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_10d_jerk_v128_signal(capex, ebitda):
    res = (((((((capex * 35.8057 - ebitda).rolling(18).std()).diff(20)).rolling(10).min()).rolling(24).max()) * 0.206653).diff(15).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_10d_jerk_v128_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc128_10d_jerk_v128_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_5d_jerk_v129_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(26).var()).rolling(28).mean()).diff(4)) * 0.073083).diff(20).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_5d_jerk_v129_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc129_5d_jerk_v129_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_42d_jerk_v130_signal(capex, ebitda):
    res = (((((capex.diff(9) / (ebitda.shift(10) + 42.4976)).pct_change(12)).pct_change(14)) * 0.337952).diff(10).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_42d_jerk_v130_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc130_42d_jerk_v130_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_63d_jerk_v131_signal(capex, ebitda):
    res = (((((capex * 40.3899 - ebitda).rolling(25).var()).rolling(28).max()) * 0.528801).diff(6).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_63d_jerk_v131_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc131_63d_jerk_v131_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_252d_jerk_v132_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(5)).rolling(10).std()).rolling(6).std()).rolling(10).max()) * 0.778598).diff(18).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_252d_jerk_v132_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc132_252d_jerk_v132_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_21d_jerk_v133_signal(capex, ebitda):
    res = (((((((capex / (ebitda + 77.2521)).diff(17)).pct_change(9)).rolling(22).min()).diff(2)) * 0.598198).diff(3).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_21d_jerk_v133_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc133_21d_jerk_v133_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_5d_jerk_v134_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 27.532)).pct_change(8)).rolling(25).min()).rolling(13).std()) * 0.787761).diff(17).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_5d_jerk_v134_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc134_5d_jerk_v134_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_jerk_v135_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(9).var()).rolling(6).max()) * 0.486251).diff(13).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_jerk_v135_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc135_42d_jerk_v135_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_63d_jerk_v136_signal(capex, ebitda):
    res = (((((ebitda / (capex + 89.064)).diff(11)).diff(7)) * 0.484865).diff(13).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_63d_jerk_v136_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc136_63d_jerk_v136_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_63d_jerk_v137_signal(capex, ebitda):
    res = (((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(5)).pct_change(17)).rolling(25).var()).rolling(7).mean()) * 0.114944).diff(3).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_63d_jerk_v137_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc137_63d_jerk_v137_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_21d_jerk_v138_signal(capex, ebitda):
    res = ((((((capex.pct_change(8) / ebitda.pct_change(1)).rolling(12).min()).pct_change(11)).rolling(6).max()) * 0.842796).diff(3).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_21d_jerk_v138_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc138_21d_jerk_v138_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_42d_jerk_v139_signal(capex, ebitda):
    res = (((((((capex.pct_change(13) / ebitda.pct_change(16)).rolling(11).var()).diff(13)).rolling(16).mean()).rolling(21).max()) * 0.264625).diff(1).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_42d_jerk_v139_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc139_42d_jerk_v139_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_252d_jerk_v140_signal(capex, ebitda):
    res = (((((capex * 34.405 - ebitda).rolling(17).min()).rolling(13).var()) * 0.662978).diff(3).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_252d_jerk_v140_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc140_252d_jerk_v140_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_63d_jerk_v141_signal(capex, ebitda):
    res = (((((capex.diff(4) / (ebitda.shift(5) + 67.7909)).diff(4)).rolling(10).min()) * 0.28179).diff(20).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_63d_jerk_v141_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc141_63d_jerk_v141_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_10d_jerk_v142_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(16).min()).rolling(13).min()).rolling(26).min()) * 0.669505).diff(11).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_10d_jerk_v142_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc142_10d_jerk_v142_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_5d_jerk_v143_signal(capex, ebitda):
    res = ((((((capex.pct_change(9) / ebitda.pct_change(7)).rolling(26).std()).rolling(19).min()).rolling(23).min()) * 0.364412).diff(16).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_5d_jerk_v143_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc143_5d_jerk_v143_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_21d_jerk_v144_signal(capex, ebitda):
    res = (((((((capex.diff(6) / (ebitda.shift(3) + 85.9964)).pct_change(2)).rolling(14).min()).diff(8)).rolling(29).var()) * 0.794689).diff(4).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_21d_jerk_v144_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc144_21d_jerk_v144_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_10d_jerk_v145_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 36.0582)).diff(9)).rolling(16).min()).pct_change(8)) * 0.464537).diff(10).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_10d_jerk_v145_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc145_10d_jerk_v145_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_21d_jerk_v146_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 24.1152)).rolling(16).var()).rolling(12).max()).rolling(10).min()) * 0.080321).diff(4).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_21d_jerk_v146_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc146_21d_jerk_v146_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_21d_jerk_v147_signal(capex, ebitda):
    res = ((((((capex * 27.1093 - ebitda).diff(12)).rolling(8).min()).rolling(23).max()) * 0.957076).diff(11).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_21d_jerk_v147_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc147_21d_jerk_v147_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_10d_jerk_v148_signal(capex, ebitda):
    res = (((((((capex.pct_change(18) / ebitda.pct_change(1)).rolling(27).max()).pct_change(12)).rolling(25).min()).rolling(11).max()) * 0.535679).diff(16).diff(12).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_10d_jerk_v148_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc148_10d_jerk_v148_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_63d_jerk_v149_signal(capex, ebitda):
    res = (((((((capex.pct_change(17) / ebitda.pct_change(9)).rolling(26).mean()).rolling(15).std()).rolling(9).std()).rolling(25).std()) * 0.410608).diff(10).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_63d_jerk_v149_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc149_63d_jerk_v149_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_5d_jerk_v150_signal(capex, ebitda):
    res = (((((((capex.pct_change(19) / ebitda.pct_change(15)).rolling(10).mean()).diff(16)).diff(19)).rolling(25).min()) * 0.465714).diff(8).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_5d_jerk_v150_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc150_5d_jerk_v150_signal


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
