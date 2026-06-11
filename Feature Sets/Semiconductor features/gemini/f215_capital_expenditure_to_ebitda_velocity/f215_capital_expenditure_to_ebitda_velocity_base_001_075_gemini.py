import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_252d_base_v001_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(18).std()).pct_change(11)).diff(20)) * 0.025822)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_252d_base_v001_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc001_252d_base_v001_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_252d_base_v002_signal(capex, ebitda):
    res = ((((((capex.diff(7) / (ebitda.shift(10) + 82.6625)).pct_change(6)).diff(17)).diff(20)).pct_change(17)) * 0.389467)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_252d_base_v002_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc002_252d_base_v002_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_252d_base_v003_signal(capex, ebitda):
    res = ((((capex * 48.2096 - ebitda).rolling(28).std()).rolling(24).mean()) * 0.401809)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_252d_base_v003_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc003_252d_base_v003_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_42d_base_v004_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).diff(15)).rolling(15).mean()).rolling(8).min()).rolling(28).std()) * 0.644953)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_42d_base_v004_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc004_42d_base_v004_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_5d_base_v005_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 76.2774)).rolling(7).max()).pct_change(17)).pct_change(20)).rolling(23).mean()) * 0.404175)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_5d_base_v005_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc005_5d_base_v005_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_63d_base_v006_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(30).var()).pct_change(7)).pct_change(8)).rolling(4).min()) * 0.921879)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_63d_base_v006_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc006_63d_base_v006_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_42d_base_v007_signal(capex, ebitda):
    res = ((((capex.diff(18) / (ebitda.shift(7) + 73.78)).rolling(20).min()).rolling(7).var()) * 0.913614)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_42d_base_v007_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc007_42d_base_v007_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_5d_base_v008_signal(capex, ebitda):
    res = (((((capex.diff(18) / (ebitda.shift(4) + 20.7041)).diff(20)).diff(1)).rolling(11).mean()) * 0.691547)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_5d_base_v008_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc008_5d_base_v008_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_21d_base_v009_signal(capex, ebitda):
    res = ((((capex * 77.5312 - ebitda).rolling(21).mean()).rolling(28).var()) * 0.608286)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_21d_base_v009_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc009_21d_base_v009_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_63d_base_v010_signal(capex, ebitda):
    res = ((((capex.diff(9) / (ebitda.shift(10) + 43.975)).rolling(18).max()).diff(9)) * 0.011952)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_63d_base_v010_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc010_63d_base_v010_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_126d_base_v011_signal(capex, ebitda):
    res = (((((capex / (ebitda + 78.6563)).rolling(18).min()).pct_change(1)).rolling(22).min()) * 0.805489)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_126d_base_v011_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc011_126d_base_v011_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_42d_base_v012_signal(capex, ebitda):
    res = ((((capex * 95.3894 - ebitda).rolling(14).mean()).diff(9)) * 0.275658)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_42d_base_v012_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc012_42d_base_v012_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_252d_base_v013_signal(capex, ebitda):
    res = ((((capex / (ebitda + 58.1338)).rolling(26).min()).rolling(5).mean()) * 0.718259)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_252d_base_v013_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc013_252d_base_v013_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_42d_base_v014_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(2).std()).rolling(22).max()) * 0.597096)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_42d_base_v014_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc014_42d_base_v014_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_63d_base_v015_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 3.2414)).rolling(21).std()).rolling(19).min()).rolling(22).std()).pct_change(10)) * 0.637809)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_63d_base_v015_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc015_63d_base_v015_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_252d_base_v016_signal(capex, ebitda):
    res = ((((((capex * 29.9848 - ebitda).diff(19)).rolling(20).var()).rolling(22).std()).diff(15)) * 0.526046)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_252d_base_v016_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc016_252d_base_v016_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_126d_base_v017_signal(capex, ebitda):
    res = ((((capex.pct_change(14) / ebitda.pct_change(19)).diff(20)).rolling(29).min()) * 0.083757)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_126d_base_v017_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc017_126d_base_v017_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_5d_base_v018_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 17.2319)).rolling(28).std()).rolling(9).mean()).rolling(5).max()).rolling(3).min()) * 0.472803)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_5d_base_v018_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc018_5d_base_v018_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_126d_base_v019_signal(capex, ebitda):
    res = ((((capex.diff(14) / (ebitda.shift(4) + 75.7653)).rolling(27).var()).rolling(14).max()) * 0.181726)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_126d_base_v019_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc019_126d_base_v019_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_126d_base_v020_signal(capex, ebitda):
    res = ((((capex / (ebitda + 65.131)).rolling(25).mean()).diff(10)) * 0.639087)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_126d_base_v020_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc020_126d_base_v020_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_252d_base_v021_signal(capex, ebitda):
    res = ((((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(20).mean()).rolling(6).mean()).rolling(16).std()).rolling(9).var()) * 0.654595)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_252d_base_v021_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc021_252d_base_v021_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_5d_base_v022_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 18.3457)).rolling(22).min()).pct_change(15)).rolling(6).mean()).pct_change(10)) * 0.901283)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_5d_base_v022_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc022_5d_base_v022_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_10d_base_v023_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 37.6057)).pct_change(14)).rolling(18).var()).pct_change(3)).diff(18)) * 0.140298)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_10d_base_v023_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc023_10d_base_v023_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_252d_base_v024_signal(capex, ebitda):
    res = (((((capex.pct_change(8) / ebitda.pct_change(13)).pct_change(17)).rolling(6).max()).rolling(13).mean()) * 0.369872)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_252d_base_v024_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc024_252d_base_v024_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_252d_base_v025_signal(capex, ebitda):
    res = ((((((capex.diff(16) / (ebitda.shift(4) + 71.7133)).rolling(15).min()).rolling(8).std()).rolling(9).std()).rolling(3).min()) * 0.452734)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_252d_base_v025_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc025_252d_base_v025_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_42d_base_v026_signal(capex, ebitda):
    res = ((((capex * 40.3829 - ebitda).rolling(13).std()).rolling(11).max()) * 0.464321)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_42d_base_v026_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc026_42d_base_v026_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_63d_base_v027_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 81.678)).rolling(14).max()).rolling(7).std()).rolling(20).min()).rolling(6).max()) * 0.958435)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_63d_base_v027_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc027_63d_base_v027_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_5d_base_v028_signal(capex, ebitda):
    res = ((((ebitda / (capex + 38.4448)).rolling(14).var()).rolling(20).max()) * 0.400192)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_5d_base_v028_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc028_5d_base_v028_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_63d_base_v029_signal(capex, ebitda):
    res = ((((((capex.diff(20) / (ebitda.shift(9) + 65.7647)).diff(16)).pct_change(13)).rolling(18).max()).rolling(24).min()) * 0.161234)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_63d_base_v029_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc029_63d_base_v029_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_42d_base_v030_signal(capex, ebitda):
    res = (((((ebitda / (capex + 45.1489)).rolling(7).max()).rolling(18).mean()).pct_change(9)) * 0.193545)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_42d_base_v030_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc030_42d_base_v030_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_63d_base_v031_signal(capex, ebitda):
    res = ((((capex * 81.3285 - ebitda).rolling(6).std()).rolling(2).min()) * 0.103733)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_63d_base_v031_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc031_63d_base_v031_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_5d_base_v032_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 0.5415)).diff(3)).pct_change(10)).diff(8)).pct_change(2)) * 0.075169)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_5d_base_v032_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc032_5d_base_v032_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_252d_base_v033_signal(capex, ebitda):
    res = ((((capex / (ebitda + 28.496)).rolling(27).max()).rolling(17).max()) * 0.927068)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_252d_base_v033_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc033_252d_base_v033_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_21d_base_v034_signal(capex, ebitda):
    res = ((((((capex * 15.3153 - ebitda).rolling(15).max()).diff(11)).pct_change(13)).rolling(7).var()) * 0.632856)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_21d_base_v034_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc034_21d_base_v034_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_126d_base_v035_signal(capex, ebitda):
    res = ((((((capex * 78.6118 - ebitda).diff(5)).rolling(18).mean()).rolling(9).std()).rolling(28).var()) * 0.931025)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_126d_base_v035_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc035_126d_base_v035_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_10d_base_v036_signal(capex, ebitda):
    res = (((((capex * 3.1949 - ebitda).rolling(30).max()).rolling(14).max()).rolling(20).std()) * 0.923838)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_10d_base_v036_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc036_10d_base_v036_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_252d_base_v037_signal(capex, ebitda):
    res = ((((ebitda / (capex + 77.7011)).rolling(17).mean()).diff(12)) * 0.912793)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_252d_base_v037_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc037_252d_base_v037_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_10d_base_v038_signal(capex, ebitda):
    res = (((((capex * 62.832 - ebitda).rolling(12).max()).rolling(6).min()).pct_change(10)) * 0.012723)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_10d_base_v038_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc038_10d_base_v038_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_252d_base_v039_signal(capex, ebitda):
    res = ((((capex.pct_change(9) / ebitda.pct_change(4)).rolling(9).var()).rolling(23).mean()) * 0.313428)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_252d_base_v039_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc039_252d_base_v039_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_10d_base_v040_signal(capex, ebitda):
    res = (((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(8).min()).diff(6)).rolling(17).mean()) * 0.616299)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_10d_base_v040_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc040_10d_base_v040_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_base_v041_signal(capex, ebitda):
    res = (((((capex.pct_change(2) / ebitda.pct_change(5)).pct_change(20)).diff(19)).rolling(25).max()) * 0.420663)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_base_v041_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc041_21d_base_v041_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_5d_base_v042_signal(capex, ebitda):
    res = (((((ebitda / (capex + 59.1196)).diff(6)).pct_change(10)).pct_change(10)) * 0.515324)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_5d_base_v042_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc042_5d_base_v042_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_21d_base_v043_signal(capex, ebitda):
    res = ((((capex.replace(0, np.nan) / ebitda.replace(0, np.nan)).rolling(25).min()).rolling(15).max()) * 0.290879)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_21d_base_v043_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc043_21d_base_v043_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_252d_base_v044_signal(capex, ebitda):
    res = ((((capex.diff(3) / (ebitda.shift(1) + 12.9542)).pct_change(20)).rolling(27).mean()) * 0.230983)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_252d_base_v044_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc044_252d_base_v044_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_42d_base_v045_signal(capex, ebitda):
    res = ((((capex.pct_change(3) / ebitda.pct_change(16)).diff(6)).pct_change(18)) * 0.967908)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_42d_base_v045_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc045_42d_base_v045_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_63d_base_v046_signal(capex, ebitda):
    res = ((((capex * 34.7766 - ebitda).rolling(27).max()).rolling(18).var()) * 0.272625)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_63d_base_v046_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc046_63d_base_v046_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_5d_base_v047_signal(capex, ebitda):
    res = (((((capex.diff(3) / (ebitda.shift(2) + 34.4969)).diff(20)).rolling(23).min()).rolling(9).var()) * 0.543717)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_5d_base_v047_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc047_5d_base_v047_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_63d_base_v048_signal(capex, ebitda):
    res = (((((capex / (ebitda + 66.6739)).rolling(20).mean()).rolling(30).std()).pct_change(1)) * 0.913389)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_63d_base_v048_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc048_63d_base_v048_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_126d_base_v049_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 31.2171)).pct_change(18)).rolling(7).std()).rolling(27).mean()).rolling(2).max()) * 0.884933)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_126d_base_v049_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc049_126d_base_v049_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_126d_base_v050_signal(capex, ebitda):
    res = ((((((capex.diff(6) / (ebitda.shift(1) + 20.9797)).rolling(14).max()).diff(9)).diff(1)).diff(15)) * 0.384967)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_126d_base_v050_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc050_126d_base_v050_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_63d_base_v051_signal(capex, ebitda):
    res = (((((capex / (ebitda + 54.0944)).rolling(24).var()).rolling(24).min()).rolling(8).max()) * 0.158521)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_63d_base_v051_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc051_63d_base_v051_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_252d_base_v052_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 20.452)).rolling(11).min()).rolling(29).var()).rolling(18).mean()).rolling(30).max()) * 0.241995)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_252d_base_v052_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc052_252d_base_v052_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_5d_base_v053_signal(capex, ebitda):
    res = (((((capex * 76.2325 - ebitda).rolling(21).mean()).rolling(3).std()).diff(4)) * 0.833623)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_5d_base_v053_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc053_5d_base_v053_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_63d_base_v054_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 69.9592)).pct_change(5)).pct_change(13)).rolling(5).min()).rolling(12).mean()) * 0.100803)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_63d_base_v054_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc054_63d_base_v054_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_base_v055_signal(capex, ebitda):
    res = ((((ebitda / (capex + 27.6401)).diff(4)).rolling(21).mean()) * 0.341733)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_base_v055_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc055_63d_base_v055_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_126d_base_v056_signal(capex, ebitda):
    res = ((((capex.diff(15) / (ebitda.shift(3) + 40.3875)).rolling(30).max()).rolling(23).min()) * 0.299363)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_126d_base_v056_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc056_126d_base_v056_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_5d_base_v057_signal(capex, ebitda):
    res = ((((((capex.pct_change(10) / ebitda.pct_change(16)).pct_change(2)).pct_change(18)).diff(5)).diff(7)) * 0.942934)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_5d_base_v057_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc057_5d_base_v057_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_5d_base_v058_signal(capex, ebitda):
    res = ((((((capex.diff(13) / (ebitda.shift(2) + 44.4349)).rolling(20).std()).rolling(15).var()).pct_change(16)).pct_change(13)) * 0.072253)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_5d_base_v058_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc058_5d_base_v058_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_42d_base_v059_signal(capex, ebitda):
    res = (((((capex / (ebitda + 13.3138)).rolling(2).std()).rolling(25).std()).rolling(4).min()) * 0.409296)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_42d_base_v059_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc059_42d_base_v059_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_126d_base_v060_signal(capex, ebitda):
    res = ((((capex / (ebitda + 53.5086)).rolling(18).min()).rolling(3).min()) * 0.026115)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_126d_base_v060_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc060_126d_base_v060_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_21d_base_v061_signal(capex, ebitda):
    res = (((((ebitda / (capex + 92.8198)).pct_change(1)).rolling(3).var()).rolling(25).std()) * 0.060797)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_21d_base_v061_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc061_21d_base_v061_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_63d_base_v062_signal(capex, ebitda):
    res = ((((((capex * 88.7212 - ebitda).rolling(2).mean()).pct_change(7)).rolling(3).max()).rolling(5).max()) * 0.095975)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_63d_base_v062_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc062_63d_base_v062_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_10d_base_v063_signal(capex, ebitda):
    res = ((((((capex / (ebitda + 5.9644)).rolling(12).var()).rolling(24).std()).rolling(26).std()).rolling(26).min()) * 0.735964)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_10d_base_v063_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc063_10d_base_v063_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_21d_base_v064_signal(capex, ebitda):
    res = ((((capex.pct_change(4) / ebitda.pct_change(19)).rolling(3).min()).rolling(21).mean()) * 0.692192)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_21d_base_v064_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc064_21d_base_v064_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_126d_base_v065_signal(capex, ebitda):
    res = (((((capex.pct_change(16) / ebitda.pct_change(10)).rolling(27).var()).rolling(22).var()).rolling(6).max()) * 0.052138)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_126d_base_v065_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc065_126d_base_v065_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_5d_base_v066_signal(capex, ebitda):
    res = ((((((ebitda / (capex + 31.9704)).rolling(5).mean()).rolling(2).max()).diff(18)).rolling(24).mean()) * 0.742223)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_5d_base_v066_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc066_5d_base_v066_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_63d_base_v067_signal(capex, ebitda):
    res = (((((capex.diff(12) / (ebitda.shift(9) + 59.5648)).rolling(14).min()).rolling(29).std()).rolling(21).std()) * 0.350904)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_63d_base_v067_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc067_63d_base_v067_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_252d_base_v068_signal(capex, ebitda):
    res = ((((((capex.diff(16) / (ebitda.shift(10) + 68.6143)).rolling(14).min()).rolling(9).mean()).pct_change(14)).rolling(27).mean()) * 0.15642)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_252d_base_v068_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc068_252d_base_v068_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_42d_base_v069_signal(capex, ebitda):
    res = (((((capex.diff(14) / (ebitda.shift(1) + 84.0516)).pct_change(5)).pct_change(14)).rolling(2).min()) * 0.313405)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_42d_base_v069_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc069_42d_base_v069_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_10d_base_v070_signal(capex, ebitda):
    res = ((((capex / (ebitda + 19.7544)).rolling(8).var()).diff(1)) * 0.793781)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_10d_base_v070_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc070_10d_base_v070_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_5d_base_v071_signal(capex, ebitda):
    res = (((((capex.diff(3) / (ebitda.shift(7) + 44.1778)).rolling(13).mean()).rolling(16).max()).rolling(3).max()) * 0.675803)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_5d_base_v071_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc071_5d_base_v071_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_21d_base_v072_signal(capex, ebitda):
    res = (((((capex.diff(3) / (ebitda.shift(4) + 12.982)).rolling(20).min()).rolling(3).var()).diff(13)) * 0.260547)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_21d_base_v072_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc072_21d_base_v072_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_21d_base_v073_signal(capex, ebitda):
    res = (((((capex / (ebitda + 73.2191)).diff(15)).rolling(20).mean()).diff(3)) * 0.36806)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_21d_base_v073_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc073_21d_base_v073_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_252d_base_v074_signal(capex, ebitda):
    res = (((((capex.pct_change(13) / ebitda.pct_change(14)).pct_change(13)).rolling(8).max()).rolling(12).min()) * 0.524219)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_252d_base_v074_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc074_252d_base_v074_signal

def f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_42d_base_v075_signal(capex, ebitda):
    res = ((((((capex.diff(7) / (ebitda.shift(6) + 88.529)).diff(18)).rolling(14).min()).rolling(2).max()).rolling(23).var()) * 0.552654)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_42d_base_v075_signal'] = f215c_f215_capital_expenditure_to_ebitda_velocity_calc075_42d_base_v075_signal


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
