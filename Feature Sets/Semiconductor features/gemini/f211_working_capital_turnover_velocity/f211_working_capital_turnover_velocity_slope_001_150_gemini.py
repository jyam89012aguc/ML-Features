import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f211w_f211_working_capital_turnover_velocity_calc001_21d_slope_v001_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 61.4814)).rolling(25).max()).rolling(12).max()).pct_change(19)).rolling(28).mean()) * 0.10156).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc001_21d_slope_v001_signal'] = f211w_f211_working_capital_turnover_velocity_calc001_21d_slope_v001_signal

def f211w_f211_working_capital_turnover_velocity_calc002_5d_slope_v002_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(1)).rolling(30).min()).diff(18)).rolling(22).var()) * 0.638625).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc002_5d_slope_v002_signal'] = f211w_f211_working_capital_turnover_velocity_calc002_5d_slope_v002_signal

def f211w_f211_working_capital_turnover_velocity_calc003_42d_slope_v003_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(15) / revenue.pct_change(3)).rolling(16).std()).rolling(17).min()) * 0.801202).diff(15).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc003_42d_slope_v003_signal'] = f211w_f211_working_capital_turnover_velocity_calc003_42d_slope_v003_signal

def f211w_f211_working_capital_turnover_velocity_calc004_10d_slope_v004_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(11) / (revenue.shift(6) + 34.0852)).rolling(5).max()).rolling(9).var()).rolling(5).min()).rolling(16).var()) * 0.150795).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc004_10d_slope_v004_signal'] = f211w_f211_working_capital_turnover_velocity_calc004_10d_slope_v004_signal

def f211w_f211_working_capital_turnover_velocity_calc005_10d_slope_v005_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 9.7715)).rolling(25).max()).rolling(8).var()).pct_change(6)) * 0.294408).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc005_10d_slope_v005_signal'] = f211w_f211_working_capital_turnover_velocity_calc005_10d_slope_v005_signal

def f211w_f211_working_capital_turnover_velocity_calc006_63d_slope_v006_signal(workingcapital, revenue):
    res = ((((((workingcapital * 46.7348 - revenue).rolling(8).std()).rolling(13).max()).rolling(3).mean()) * 0.871494).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc006_63d_slope_v006_signal'] = f211w_f211_working_capital_turnover_velocity_calc006_63d_slope_v006_signal

def f211w_f211_working_capital_turnover_velocity_calc007_42d_slope_v007_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 59.7921)).rolling(30).std()).rolling(25).var()).rolling(26).var()) * 0.835993).diff(13).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc007_42d_slope_v007_signal'] = f211w_f211_working_capital_turnover_velocity_calc007_42d_slope_v007_signal

def f211w_f211_working_capital_turnover_velocity_calc008_21d_slope_v008_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(18) / (revenue.shift(4) + 4.6197)).rolling(18).min()).rolling(26).min()) * 0.060135).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc008_21d_slope_v008_signal'] = f211w_f211_working_capital_turnover_velocity_calc008_21d_slope_v008_signal

def f211w_f211_working_capital_turnover_velocity_calc009_21d_slope_v009_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(11)).rolling(13).max()).pct_change(5)) * 0.620777).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc009_21d_slope_v009_signal'] = f211w_f211_working_capital_turnover_velocity_calc009_21d_slope_v009_signal

def f211w_f211_working_capital_turnover_velocity_calc010_63d_slope_v010_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(6).min()).rolling(30).max()).rolling(6).max()).rolling(21).var()) * 0.500076).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc010_63d_slope_v010_signal'] = f211w_f211_working_capital_turnover_velocity_calc010_63d_slope_v010_signal

def f211w_f211_working_capital_turnover_velocity_calc011_10d_slope_v011_signal(workingcapital, revenue):
    res = (((((((workingcapital * 39.3562 - revenue).rolling(24).min()).rolling(11).max()).rolling(28).min()).rolling(13).mean()) * 0.61417).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc011_10d_slope_v011_signal'] = f211w_f211_working_capital_turnover_velocity_calc011_10d_slope_v011_signal

def f211w_f211_working_capital_turnover_velocity_calc012_126d_slope_v012_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(10) / (revenue.shift(1) + 11.0495)).pct_change(19)).rolling(9).max()).diff(2)).rolling(17).max()) * 0.418209).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc012_126d_slope_v012_signal'] = f211w_f211_working_capital_turnover_velocity_calc012_126d_slope_v012_signal

def f211w_f211_working_capital_turnover_velocity_calc013_63d_slope_v013_signal(workingcapital, revenue):
    res = (((((((workingcapital * 62.9396 - revenue).rolling(8).mean()).rolling(16).mean()).rolling(15).var()).rolling(15).std()) * 0.617341).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc013_63d_slope_v013_signal'] = f211w_f211_working_capital_turnover_velocity_calc013_63d_slope_v013_signal

def f211w_f211_working_capital_turnover_velocity_calc014_42d_slope_v014_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 50.2318)).rolling(23).var()).rolling(18).min()).rolling(12).min()).rolling(16).std()) * 0.609248).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc014_42d_slope_v014_signal'] = f211w_f211_working_capital_turnover_velocity_calc014_42d_slope_v014_signal

def f211w_f211_working_capital_turnover_velocity_calc015_21d_slope_v015_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 54.6727)).rolling(11).max()).rolling(11).std()).pct_change(10)) * 0.672351).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc015_21d_slope_v015_signal'] = f211w_f211_working_capital_turnover_velocity_calc015_21d_slope_v015_signal

def f211w_f211_working_capital_turnover_velocity_calc016_126d_slope_v016_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 70.5283)).diff(18)).rolling(30).min()).rolling(28).min()).rolling(26).var()) * 0.3207).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc016_126d_slope_v016_signal'] = f211w_f211_working_capital_turnover_velocity_calc016_126d_slope_v016_signal

def f211w_f211_working_capital_turnover_velocity_calc017_21d_slope_v017_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(15) / revenue.pct_change(9)).rolling(8).std()).pct_change(18)).rolling(19).var()) * 0.946207).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc017_21d_slope_v017_signal'] = f211w_f211_working_capital_turnover_velocity_calc017_21d_slope_v017_signal

def f211w_f211_working_capital_turnover_velocity_calc018_10d_slope_v018_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 11.0117)).rolling(3).std()).rolling(15).mean()).rolling(24).var()).rolling(5).min()) * 0.736073).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc018_10d_slope_v018_signal'] = f211w_f211_working_capital_turnover_velocity_calc018_10d_slope_v018_signal

def f211w_f211_working_capital_turnover_velocity_calc019_5d_slope_v019_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(16) / revenue.pct_change(16)).pct_change(10)).rolling(11).var()) * 0.968352).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc019_5d_slope_v019_signal'] = f211w_f211_working_capital_turnover_velocity_calc019_5d_slope_v019_signal

def f211w_f211_working_capital_turnover_velocity_calc020_252d_slope_v020_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 9.0371)).pct_change(13)).pct_change(16)) * 0.572651).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc020_252d_slope_v020_signal'] = f211w_f211_working_capital_turnover_velocity_calc020_252d_slope_v020_signal

def f211w_f211_working_capital_turnover_velocity_calc021_126d_slope_v021_signal(workingcapital, revenue):
    res = (((((workingcapital * 96.2169 - revenue).rolling(11).var()).rolling(22).min()) * 0.917519).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc021_126d_slope_v021_signal'] = f211w_f211_working_capital_turnover_velocity_calc021_126d_slope_v021_signal

def f211w_f211_working_capital_turnover_velocity_calc022_63d_slope_v022_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 49.4419)).rolling(25).std()).rolling(22).min()).rolling(24).var()) * 0.929789).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc022_63d_slope_v022_signal'] = f211w_f211_working_capital_turnover_velocity_calc022_63d_slope_v022_signal

def f211w_f211_working_capital_turnover_velocity_calc023_5d_slope_v023_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(6) / revenue.pct_change(20)).pct_change(14)).rolling(12).max()).rolling(14).mean()) * 0.784952).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc023_5d_slope_v023_signal'] = f211w_f211_working_capital_turnover_velocity_calc023_5d_slope_v023_signal

def f211w_f211_working_capital_turnover_velocity_calc024_10d_slope_v024_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 98.1704)).pct_change(9)).rolling(11).var()).rolling(25).max()) * 0.477905).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc024_10d_slope_v024_signal'] = f211w_f211_working_capital_turnover_velocity_calc024_10d_slope_v024_signal

def f211w_f211_working_capital_turnover_velocity_calc025_5d_slope_v025_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(8) / (revenue.shift(1) + 26.2292)).rolling(23).min()).rolling(30).max()) * 0.362361).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc025_5d_slope_v025_signal'] = f211w_f211_working_capital_turnover_velocity_calc025_5d_slope_v025_signal

def f211w_f211_working_capital_turnover_velocity_calc026_126d_slope_v026_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 11.8298)).rolling(6).min()).rolling(25).min()) * 0.907808).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc026_126d_slope_v026_signal'] = f211w_f211_working_capital_turnover_velocity_calc026_126d_slope_v026_signal

def f211w_f211_working_capital_turnover_velocity_calc027_21d_slope_v027_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(7) / revenue.pct_change(8)).pct_change(3)).rolling(16).max()).rolling(24).max()).rolling(4).var()) * 0.54825).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc027_21d_slope_v027_signal'] = f211w_f211_working_capital_turnover_velocity_calc027_21d_slope_v027_signal

def f211w_f211_working_capital_turnover_velocity_calc028_5d_slope_v028_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 6.2696)).rolling(29).var()).rolling(16).max()) * 0.546696).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc028_5d_slope_v028_signal'] = f211w_f211_working_capital_turnover_velocity_calc028_5d_slope_v028_signal

def f211w_f211_working_capital_turnover_velocity_calc029_126d_slope_v029_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(15).max()).rolling(20).min()) * 0.581485).diff(2).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc029_126d_slope_v029_signal'] = f211w_f211_working_capital_turnover_velocity_calc029_126d_slope_v029_signal

def f211w_f211_working_capital_turnover_velocity_calc030_63d_slope_v030_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(9) / revenue.pct_change(1)).rolling(4).max()).rolling(15).mean()) * 0.800777).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc030_63d_slope_v030_signal'] = f211w_f211_working_capital_turnover_velocity_calc030_63d_slope_v030_signal

def f211w_f211_working_capital_turnover_velocity_calc031_126d_slope_v031_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(5)).pct_change(14)) * 0.984241).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc031_126d_slope_v031_signal'] = f211w_f211_working_capital_turnover_velocity_calc031_126d_slope_v031_signal

def f211w_f211_working_capital_turnover_velocity_calc032_42d_slope_v032_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 44.9089)).pct_change(12)).rolling(7).mean()).rolling(14).max()).rolling(6).max()) * 0.908773).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc032_42d_slope_v032_signal'] = f211w_f211_working_capital_turnover_velocity_calc032_42d_slope_v032_signal

def f211w_f211_working_capital_turnover_velocity_calc033_252d_slope_v033_signal(workingcapital, revenue):
    res = ((((((workingcapital * 0.447 - revenue).pct_change(8)).rolling(16).std()).rolling(6).var()) * 0.032281).diff(9).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc033_252d_slope_v033_signal'] = f211w_f211_working_capital_turnover_velocity_calc033_252d_slope_v033_signal

def f211w_f211_working_capital_turnover_velocity_calc034_10d_slope_v034_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 93.7473)).rolling(4).std()).rolling(21).mean()) * 0.720523).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc034_10d_slope_v034_signal'] = f211w_f211_working_capital_turnover_velocity_calc034_10d_slope_v034_signal

def f211w_f211_working_capital_turnover_velocity_calc035_42d_slope_v035_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(8).max()).pct_change(2)) * 0.699221).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc035_42d_slope_v035_signal'] = f211w_f211_working_capital_turnover_velocity_calc035_42d_slope_v035_signal

def f211w_f211_working_capital_turnover_velocity_calc036_63d_slope_v036_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(19) / revenue.pct_change(20)).rolling(11).std()).rolling(23).std()).rolling(9).max()) * 0.239478).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc036_63d_slope_v036_signal'] = f211w_f211_working_capital_turnover_velocity_calc036_63d_slope_v036_signal

def f211w_f211_working_capital_turnover_velocity_calc037_21d_slope_v037_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(22).var()).diff(13)) * 0.555584).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc037_21d_slope_v037_signal'] = f211w_f211_working_capital_turnover_velocity_calc037_21d_slope_v037_signal

def f211w_f211_working_capital_turnover_velocity_calc038_21d_slope_v038_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(8)).rolling(29).var()) * 0.410094).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc038_21d_slope_v038_signal'] = f211w_f211_working_capital_turnover_velocity_calc038_21d_slope_v038_signal

def f211w_f211_working_capital_turnover_velocity_calc039_252d_slope_v039_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 46.3562)).rolling(10).std()).rolling(12).std()).diff(3)) * 0.066471).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc039_252d_slope_v039_signal'] = f211w_f211_working_capital_turnover_velocity_calc039_252d_slope_v039_signal

def f211w_f211_working_capital_turnover_velocity_calc040_252d_slope_v040_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(9) / revenue.pct_change(13)).rolling(3).max()).pct_change(3)).rolling(27).std()).pct_change(19)) * 0.534923).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc040_252d_slope_v040_signal'] = f211w_f211_working_capital_turnover_velocity_calc040_252d_slope_v040_signal

def f211w_f211_working_capital_turnover_velocity_calc041_10d_slope_v041_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 47.9915)).rolling(25).mean()).pct_change(16)).rolling(24).std()).rolling(24).max()) * 0.862084).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc041_10d_slope_v041_signal'] = f211w_f211_working_capital_turnover_velocity_calc041_10d_slope_v041_signal

def f211w_f211_working_capital_turnover_velocity_calc042_42d_slope_v042_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(15) / revenue.pct_change(18)).rolling(10).var()).rolling(18).var()).rolling(16).min()) * 0.551038).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc042_42d_slope_v042_signal'] = f211w_f211_working_capital_turnover_velocity_calc042_42d_slope_v042_signal

def f211w_f211_working_capital_turnover_velocity_calc043_252d_slope_v043_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(29).max()).rolling(25).std()) * 0.470101).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc043_252d_slope_v043_signal'] = f211w_f211_working_capital_turnover_velocity_calc043_252d_slope_v043_signal

def f211w_f211_working_capital_turnover_velocity_calc044_5d_slope_v044_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 26.1513)).rolling(14).std()).rolling(28).max()).rolling(17).std()) * 0.926063).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc044_5d_slope_v044_signal'] = f211w_f211_working_capital_turnover_velocity_calc044_5d_slope_v044_signal

def f211w_f211_working_capital_turnover_velocity_calc045_126d_slope_v045_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(15) / revenue.pct_change(6)).rolling(6).std()).diff(18)).rolling(7).min()) * 0.340813).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc045_126d_slope_v045_signal'] = f211w_f211_working_capital_turnover_velocity_calc045_126d_slope_v045_signal

def f211w_f211_working_capital_turnover_velocity_calc046_126d_slope_v046_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 95.728)).rolling(4).std()).diff(5)).rolling(8).mean()).rolling(16).max()) * 0.523466).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc046_126d_slope_v046_signal'] = f211w_f211_working_capital_turnover_velocity_calc046_126d_slope_v046_signal

def f211w_f211_working_capital_turnover_velocity_calc047_5d_slope_v047_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 61.8217)).rolling(15).max()).rolling(2).mean()).rolling(25).max()).rolling(19).var()) * 0.66342).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc047_5d_slope_v047_signal'] = f211w_f211_working_capital_turnover_velocity_calc047_5d_slope_v047_signal

def f211w_f211_working_capital_turnover_velocity_calc048_5d_slope_v048_signal(workingcapital, revenue):
    res = (((((workingcapital * 50.2714 - revenue).rolling(8).std()).rolling(18).max()) * 0.693902).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc048_5d_slope_v048_signal'] = f211w_f211_working_capital_turnover_velocity_calc048_5d_slope_v048_signal

def f211w_f211_working_capital_turnover_velocity_calc049_252d_slope_v049_signal(workingcapital, revenue):
    res = (((((workingcapital * 35.5087 - revenue).diff(8)).rolling(23).var()) * 0.789038).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc049_252d_slope_v049_signal'] = f211w_f211_working_capital_turnover_velocity_calc049_252d_slope_v049_signal

def f211w_f211_working_capital_turnover_velocity_calc050_126d_slope_v050_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(3).min()).diff(1)).diff(6)).rolling(17).mean()) * 0.646897).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc050_126d_slope_v050_signal'] = f211w_f211_working_capital_turnover_velocity_calc050_126d_slope_v050_signal

def f211w_f211_working_capital_turnover_velocity_calc051_126d_slope_v051_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 78.4592)).rolling(17).max()).rolling(3).var()).rolling(23).mean()).rolling(30).var()) * 0.564539).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc051_126d_slope_v051_signal'] = f211w_f211_working_capital_turnover_velocity_calc051_126d_slope_v051_signal

def f211w_f211_working_capital_turnover_velocity_calc052_63d_slope_v052_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 65.8451)).pct_change(13)).rolling(11).mean()).rolling(20).std()).rolling(20).std()) * 0.185767).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc052_63d_slope_v052_signal'] = f211w_f211_working_capital_turnover_velocity_calc052_63d_slope_v052_signal

def f211w_f211_working_capital_turnover_velocity_calc053_126d_slope_v053_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 89.6629)).rolling(9).min()).pct_change(3)) * 0.335095).diff(11).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc053_126d_slope_v053_signal'] = f211w_f211_working_capital_turnover_velocity_calc053_126d_slope_v053_signal

def f211w_f211_working_capital_turnover_velocity_calc054_63d_slope_v054_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).std()).rolling(14).max()).rolling(7).min()) * 0.945761).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc054_63d_slope_v054_signal'] = f211w_f211_working_capital_turnover_velocity_calc054_63d_slope_v054_signal

def f211w_f211_working_capital_turnover_velocity_calc055_126d_slope_v055_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(10) / (revenue.shift(4) + 38.0693)).rolling(24).min()).pct_change(5)) * 0.766724).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc055_126d_slope_v055_signal'] = f211w_f211_working_capital_turnover_velocity_calc055_126d_slope_v055_signal

def f211w_f211_working_capital_turnover_velocity_calc056_21d_slope_v056_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 36.134)).rolling(7).mean()).rolling(16).min()) * 0.09969).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc056_21d_slope_v056_signal'] = f211w_f211_working_capital_turnover_velocity_calc056_21d_slope_v056_signal

def f211w_f211_working_capital_turnover_velocity_calc057_63d_slope_v057_signal(workingcapital, revenue):
    res = (((((((workingcapital * 51.2928 - revenue).pct_change(11)).pct_change(13)).rolling(11).mean()).rolling(14).min()) * 0.111227).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc057_63d_slope_v057_signal'] = f211w_f211_working_capital_turnover_velocity_calc057_63d_slope_v057_signal

def f211w_f211_working_capital_turnover_velocity_calc058_126d_slope_v058_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(17) / revenue.pct_change(6)).rolling(6).std()).rolling(11).var()).rolling(17).var()) * 0.897103).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc058_126d_slope_v058_signal'] = f211w_f211_working_capital_turnover_velocity_calc058_126d_slope_v058_signal

def f211w_f211_working_capital_turnover_velocity_calc059_5d_slope_v059_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(10) / (revenue.shift(8) + 16.804)).diff(16)).rolling(21).max()) * 0.280443).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc059_5d_slope_v059_signal'] = f211w_f211_working_capital_turnover_velocity_calc059_5d_slope_v059_signal

def f211w_f211_working_capital_turnover_velocity_calc060_42d_slope_v060_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(13) / (revenue.shift(6) + 10.7865)).rolling(15).var()).pct_change(20)).rolling(11).std()) * 0.308565).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc060_42d_slope_v060_signal'] = f211w_f211_working_capital_turnover_velocity_calc060_42d_slope_v060_signal

def f211w_f211_working_capital_turnover_velocity_calc061_63d_slope_v061_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(11) / (revenue.shift(3) + 94.7332)).diff(16)).rolling(27).max()).rolling(12).std()).rolling(10).min()) * 0.206834).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc061_63d_slope_v061_signal'] = f211w_f211_working_capital_turnover_velocity_calc061_63d_slope_v061_signal

def f211w_f211_working_capital_turnover_velocity_calc062_21d_slope_v062_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 11.4774)).rolling(24).min()).rolling(16).std()).pct_change(10)).pct_change(3)) * 0.562573).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc062_21d_slope_v062_signal'] = f211w_f211_working_capital_turnover_velocity_calc062_21d_slope_v062_signal

def f211w_f211_working_capital_turnover_velocity_calc063_126d_slope_v063_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).min()).rolling(20).min()) * 0.630669).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc063_126d_slope_v063_signal'] = f211w_f211_working_capital_turnover_velocity_calc063_126d_slope_v063_signal

def f211w_f211_working_capital_turnover_velocity_calc064_63d_slope_v064_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(2) / revenue.pct_change(12)).rolling(22).max()).rolling(5).mean()).pct_change(8)).diff(12)) * 0.911984).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc064_63d_slope_v064_signal'] = f211w_f211_working_capital_turnover_velocity_calc064_63d_slope_v064_signal

def f211w_f211_working_capital_turnover_velocity_calc065_126d_slope_v065_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 61.3065)).rolling(9).var()).rolling(25).max()) * 0.561956).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc065_126d_slope_v065_signal'] = f211w_f211_working_capital_turnover_velocity_calc065_126d_slope_v065_signal

def f211w_f211_working_capital_turnover_velocity_calc066_63d_slope_v066_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(13) / revenue.pct_change(15)).diff(17)).rolling(13).std()).rolling(17).mean()).rolling(11).mean()) * 0.573731).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc066_63d_slope_v066_signal'] = f211w_f211_working_capital_turnover_velocity_calc066_63d_slope_v066_signal

def f211w_f211_working_capital_turnover_velocity_calc067_5d_slope_v067_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).max()).rolling(17).var()) * 0.931863).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc067_5d_slope_v067_signal'] = f211w_f211_working_capital_turnover_velocity_calc067_5d_slope_v067_signal

def f211w_f211_working_capital_turnover_velocity_calc068_42d_slope_v068_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 72.2272)).diff(4)).diff(6)).diff(8)) * 0.453398).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc068_42d_slope_v068_signal'] = f211w_f211_working_capital_turnover_velocity_calc068_42d_slope_v068_signal

def f211w_f211_working_capital_turnover_velocity_calc069_10d_slope_v069_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(13)).rolling(22).std()).diff(14)) * 0.33437).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc069_10d_slope_v069_signal'] = f211w_f211_working_capital_turnover_velocity_calc069_10d_slope_v069_signal

def f211w_f211_working_capital_turnover_velocity_calc070_5d_slope_v070_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 73.7651)).rolling(8).std()).rolling(26).var()).diff(3)).rolling(5).max()) * 0.875435).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc070_5d_slope_v070_signal'] = f211w_f211_working_capital_turnover_velocity_calc070_5d_slope_v070_signal

def f211w_f211_working_capital_turnover_velocity_calc071_10d_slope_v071_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(16) / revenue.pct_change(17)).rolling(14).max()).rolling(14).max()).rolling(5).max()) * 0.203133).diff(12).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc071_10d_slope_v071_signal'] = f211w_f211_working_capital_turnover_velocity_calc071_10d_slope_v071_signal

def f211w_f211_working_capital_turnover_velocity_calc072_21d_slope_v072_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(19) / revenue.pct_change(3)).rolling(5).var()).rolling(11).std()) * 0.615015).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc072_21d_slope_v072_signal'] = f211w_f211_working_capital_turnover_velocity_calc072_21d_slope_v072_signal

def f211w_f211_working_capital_turnover_velocity_calc073_10d_slope_v073_signal(workingcapital, revenue):
    res = ((((((workingcapital * 37.3933 - revenue).rolling(7).min()).rolling(22).min()).rolling(24).max()) * 0.148531).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc073_10d_slope_v073_signal'] = f211w_f211_working_capital_turnover_velocity_calc073_10d_slope_v073_signal

def f211w_f211_working_capital_turnover_velocity_calc074_63d_slope_v074_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 16.7699)).rolling(17).mean()).rolling(8).std()).pct_change(13)) * 0.293058).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc074_63d_slope_v074_signal'] = f211w_f211_working_capital_turnover_velocity_calc074_63d_slope_v074_signal

def f211w_f211_working_capital_turnover_velocity_calc075_63d_slope_v075_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 65.3417)).rolling(2).max()).pct_change(8)) * 0.410952).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc075_63d_slope_v075_signal'] = f211w_f211_working_capital_turnover_velocity_calc075_63d_slope_v075_signal

def f211w_f211_working_capital_turnover_velocity_calc076_5d_slope_v076_signal(workingcapital, revenue):
    res = (((((((workingcapital * 27.5578 - revenue).rolling(20).mean()).rolling(10).mean()).pct_change(18)).pct_change(12)) * 0.536856).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc076_5d_slope_v076_signal'] = f211w_f211_working_capital_turnover_velocity_calc076_5d_slope_v076_signal

def f211w_f211_working_capital_turnover_velocity_calc077_252d_slope_v077_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 75.7029)).pct_change(8)).rolling(29).var()).rolling(16).mean()).rolling(13).var()) * 0.754804).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc077_252d_slope_v077_signal'] = f211w_f211_working_capital_turnover_velocity_calc077_252d_slope_v077_signal

def f211w_f211_working_capital_turnover_velocity_calc078_42d_slope_v078_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(19) / revenue.pct_change(12)).diff(14)).rolling(21).std()).rolling(27).std()).rolling(28).std()) * 0.125038).diff(7).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc078_42d_slope_v078_signal'] = f211w_f211_working_capital_turnover_velocity_calc078_42d_slope_v078_signal

def f211w_f211_working_capital_turnover_velocity_calc079_252d_slope_v079_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(9) / (revenue.shift(10) + 6.0298)).rolling(11).var()).rolling(10).max()).pct_change(17)).diff(4)) * 0.353799).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc079_252d_slope_v079_signal'] = f211w_f211_working_capital_turnover_velocity_calc079_252d_slope_v079_signal

def f211w_f211_working_capital_turnover_velocity_calc080_252d_slope_v080_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 78.5905)).rolling(28).var()).rolling(26).std()).pct_change(13)).rolling(6).min()) * 0.910393).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc080_252d_slope_v080_signal'] = f211w_f211_working_capital_turnover_velocity_calc080_252d_slope_v080_signal

def f211w_f211_working_capital_turnover_velocity_calc081_126d_slope_v081_signal(workingcapital, revenue):
    res = (((((((workingcapital * 26.9448 - revenue).rolling(24).var()).rolling(16).var()).rolling(12).min()).rolling(2).max()) * 0.415941).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc081_126d_slope_v081_signal'] = f211w_f211_working_capital_turnover_velocity_calc081_126d_slope_v081_signal

def f211w_f211_working_capital_turnover_velocity_calc082_126d_slope_v082_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 97.2178)).pct_change(7)).rolling(10).min()).rolling(28).var()) * 0.632144).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc082_126d_slope_v082_signal'] = f211w_f211_working_capital_turnover_velocity_calc082_126d_slope_v082_signal

def f211w_f211_working_capital_turnover_velocity_calc083_21d_slope_v083_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 54.7763)).pct_change(15)).rolling(5).mean()).pct_change(6)).rolling(16).min()) * 0.137982).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc083_21d_slope_v083_signal'] = f211w_f211_working_capital_turnover_velocity_calc083_21d_slope_v083_signal

def f211w_f211_working_capital_turnover_velocity_calc084_42d_slope_v084_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 20.3116)).rolling(10).var()).rolling(13).mean()).diff(6)).rolling(14).mean()) * 0.68482).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc084_42d_slope_v084_signal'] = f211w_f211_working_capital_turnover_velocity_calc084_42d_slope_v084_signal

def f211w_f211_working_capital_turnover_velocity_calc085_126d_slope_v085_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(20).std()).rolling(18).std()) * 0.239461).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc085_126d_slope_v085_signal'] = f211w_f211_working_capital_turnover_velocity_calc085_126d_slope_v085_signal

def f211w_f211_working_capital_turnover_velocity_calc086_5d_slope_v086_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 0.9055)).rolling(4).min()).diff(4)) * 0.346703).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc086_5d_slope_v086_signal'] = f211w_f211_working_capital_turnover_velocity_calc086_5d_slope_v086_signal

def f211w_f211_working_capital_turnover_velocity_calc087_21d_slope_v087_signal(workingcapital, revenue):
    res = (((((((workingcapital * 36.8194 - revenue).rolling(21).mean()).diff(6)).rolling(13).min()).diff(7)) * 0.30327).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc087_21d_slope_v087_signal'] = f211w_f211_working_capital_turnover_velocity_calc087_21d_slope_v087_signal

def f211w_f211_working_capital_turnover_velocity_calc088_42d_slope_v088_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 61.646)).diff(13)).rolling(15).var()).rolling(27).var()).rolling(9).std()) * 0.443536).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc088_42d_slope_v088_signal'] = f211w_f211_working_capital_turnover_velocity_calc088_42d_slope_v088_signal

def f211w_f211_working_capital_turnover_velocity_calc089_126d_slope_v089_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(10) / revenue.pct_change(1)).rolling(18).std()).rolling(18).max()).rolling(25).std()) * 0.552329).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc089_126d_slope_v089_signal'] = f211w_f211_working_capital_turnover_velocity_calc089_126d_slope_v089_signal

def f211w_f211_working_capital_turnover_velocity_calc090_21d_slope_v090_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 64.6524)).diff(20)).rolling(18).mean()).rolling(13).mean()) * 0.778126).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc090_21d_slope_v090_signal'] = f211w_f211_working_capital_turnover_velocity_calc090_21d_slope_v090_signal

def f211w_f211_working_capital_turnover_velocity_calc091_10d_slope_v091_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(20).mean()).rolling(2).mean()) * 0.832194).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc091_10d_slope_v091_signal'] = f211w_f211_working_capital_turnover_velocity_calc091_10d_slope_v091_signal

def f211w_f211_working_capital_turnover_velocity_calc092_10d_slope_v092_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(13)).rolling(22).mean()).rolling(19).max()) * 0.069259).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc092_10d_slope_v092_signal'] = f211w_f211_working_capital_turnover_velocity_calc092_10d_slope_v092_signal

def f211w_f211_working_capital_turnover_velocity_calc093_10d_slope_v093_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(17) / (revenue.shift(4) + 27.819)).rolling(22).max()).pct_change(3)).rolling(24).var()) * 0.313709).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc093_10d_slope_v093_signal'] = f211w_f211_working_capital_turnover_velocity_calc093_10d_slope_v093_signal

def f211w_f211_working_capital_turnover_velocity_calc094_126d_slope_v094_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(3).max()).rolling(23).var()).diff(6)).rolling(2).mean()) * 0.243865).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc094_126d_slope_v094_signal'] = f211w_f211_working_capital_turnover_velocity_calc094_126d_slope_v094_signal

def f211w_f211_working_capital_turnover_velocity_calc095_126d_slope_v095_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 1.2339)).rolling(25).std()).pct_change(9)).diff(4)) * 0.496485).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc095_126d_slope_v095_signal'] = f211w_f211_working_capital_turnover_velocity_calc095_126d_slope_v095_signal

def f211w_f211_working_capital_turnover_velocity_calc096_21d_slope_v096_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).max()).rolling(17).mean()).pct_change(19)) * 0.276541).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc096_21d_slope_v096_signal'] = f211w_f211_working_capital_turnover_velocity_calc096_21d_slope_v096_signal

def f211w_f211_working_capital_turnover_velocity_calc097_21d_slope_v097_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 15.8153)).pct_change(1)).rolling(3).std()) * 0.767862).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc097_21d_slope_v097_signal'] = f211w_f211_working_capital_turnover_velocity_calc097_21d_slope_v097_signal

def f211w_f211_working_capital_turnover_velocity_calc098_21d_slope_v098_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(2) / (revenue.shift(9) + 38.3596)).rolling(25).min()).rolling(10).var()) * 0.157083).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc098_21d_slope_v098_signal'] = f211w_f211_working_capital_turnover_velocity_calc098_21d_slope_v098_signal

def f211w_f211_working_capital_turnover_velocity_calc099_63d_slope_v099_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 37.3435)).rolling(30).mean()).rolling(29).min()).rolling(26).var()) * 0.502).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc099_63d_slope_v099_signal'] = f211w_f211_working_capital_turnover_velocity_calc099_63d_slope_v099_signal

def f211w_f211_working_capital_turnover_velocity_calc100_21d_slope_v100_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(12) / (revenue.shift(4) + 8.7299)).rolling(9).max()).rolling(13).min()).rolling(17).max()).pct_change(7)) * 0.457611).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc100_21d_slope_v100_signal'] = f211w_f211_working_capital_turnover_velocity_calc100_21d_slope_v100_signal

def f211w_f211_working_capital_turnover_velocity_calc101_252d_slope_v101_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(14) / (revenue.shift(1) + 79.6178)).pct_change(1)).rolling(2).var()).pct_change(13)).pct_change(10)) * 0.157555).diff(4).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc101_252d_slope_v101_signal'] = f211w_f211_working_capital_turnover_velocity_calc101_252d_slope_v101_signal

def f211w_f211_working_capital_turnover_velocity_calc102_10d_slope_v102_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 53.0285)).rolling(30).std()).pct_change(17)) * 0.243404).diff(14).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc102_10d_slope_v102_signal'] = f211w_f211_working_capital_turnover_velocity_calc102_10d_slope_v102_signal

def f211w_f211_working_capital_turnover_velocity_calc103_126d_slope_v103_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 89.5682)).pct_change(13)).rolling(20).mean()).rolling(3).max()).rolling(23).min()) * 0.459289).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc103_126d_slope_v103_signal'] = f211w_f211_working_capital_turnover_velocity_calc103_126d_slope_v103_signal

def f211w_f211_working_capital_turnover_velocity_calc104_10d_slope_v104_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(13) / (revenue.shift(6) + 29.2384)).rolling(8).mean()).rolling(26).std()) * 0.843895).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc104_10d_slope_v104_signal'] = f211w_f211_working_capital_turnover_velocity_calc104_10d_slope_v104_signal

def f211w_f211_working_capital_turnover_velocity_calc105_5d_slope_v105_signal(workingcapital, revenue):
    res = ((((((workingcapital * 15.6255 - revenue).pct_change(7)).rolling(11).min()).rolling(10).min()) * 0.171087).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc105_5d_slope_v105_signal'] = f211w_f211_working_capital_turnover_velocity_calc105_5d_slope_v105_signal

def f211w_f211_working_capital_turnover_velocity_calc106_5d_slope_v106_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 15.8458)).diff(8)).rolling(14).var()) * 0.682334).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc106_5d_slope_v106_signal'] = f211w_f211_working_capital_turnover_velocity_calc106_5d_slope_v106_signal

def f211w_f211_working_capital_turnover_velocity_calc107_5d_slope_v107_signal(workingcapital, revenue):
    res = (((((((workingcapital * 67.7506 - revenue).rolling(9).max()).rolling(16).mean()).rolling(27).mean()).pct_change(5)) * 0.264963).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc107_5d_slope_v107_signal'] = f211w_f211_working_capital_turnover_velocity_calc107_5d_slope_v107_signal

def f211w_f211_working_capital_turnover_velocity_calc108_5d_slope_v108_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(8) / (revenue.shift(3) + 6.2608)).diff(3)).rolling(20).max()).rolling(28).var()).rolling(2).mean()) * 0.775341).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc108_5d_slope_v108_signal'] = f211w_f211_working_capital_turnover_velocity_calc108_5d_slope_v108_signal

def f211w_f211_working_capital_turnover_velocity_calc109_10d_slope_v109_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 90.2594)).rolling(7).mean()).rolling(15).max()).pct_change(13)) * 0.444563).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc109_10d_slope_v109_signal'] = f211w_f211_working_capital_turnover_velocity_calc109_10d_slope_v109_signal

def f211w_f211_working_capital_turnover_velocity_calc110_5d_slope_v110_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(12) / (revenue.shift(4) + 38.3347)).rolling(3).std()).rolling(21).max()).rolling(9).max()) * 0.428131).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc110_5d_slope_v110_signal'] = f211w_f211_working_capital_turnover_velocity_calc110_5d_slope_v110_signal

def f211w_f211_working_capital_turnover_velocity_calc111_42d_slope_v111_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 41.258)).rolling(22).std()).pct_change(17)).rolling(22).std()) * 0.549675).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc111_42d_slope_v111_signal'] = f211w_f211_working_capital_turnover_velocity_calc111_42d_slope_v111_signal

def f211w_f211_working_capital_turnover_velocity_calc112_252d_slope_v112_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(12) / (revenue.shift(8) + 2.051)).rolling(12).max()).rolling(10).min()).rolling(2).std()).rolling(21).var()) * 0.384848).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc112_252d_slope_v112_signal'] = f211w_f211_working_capital_turnover_velocity_calc112_252d_slope_v112_signal

def f211w_f211_working_capital_turnover_velocity_calc113_5d_slope_v113_signal(workingcapital, revenue):
    res = (((((workingcapital * 89.5869 - revenue).rolling(5).std()).rolling(23).std()) * 0.772968).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc113_5d_slope_v113_signal'] = f211w_f211_working_capital_turnover_velocity_calc113_5d_slope_v113_signal

def f211w_f211_working_capital_turnover_velocity_calc114_21d_slope_v114_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(2) / (revenue.shift(4) + 53.4156)).rolling(9).std()).rolling(12).max()) * 0.785412).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc114_21d_slope_v114_signal'] = f211w_f211_working_capital_turnover_velocity_calc114_21d_slope_v114_signal

def f211w_f211_working_capital_turnover_velocity_calc115_63d_slope_v115_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 2.9178)).rolling(11).max()).rolling(17).std()).rolling(4).mean()) * 0.69655).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc115_63d_slope_v115_signal'] = f211w_f211_working_capital_turnover_velocity_calc115_63d_slope_v115_signal

def f211w_f211_working_capital_turnover_velocity_calc116_10d_slope_v116_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 60.2061)).rolling(24).var()).rolling(27).std()) * 0.029529).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc116_10d_slope_v116_signal'] = f211w_f211_working_capital_turnover_velocity_calc116_10d_slope_v116_signal

def f211w_f211_working_capital_turnover_velocity_calc117_5d_slope_v117_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 2.2891)).diff(13)).rolling(5).max()).rolling(11).var()) * 0.584877).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc117_5d_slope_v117_signal'] = f211w_f211_working_capital_turnover_velocity_calc117_5d_slope_v117_signal

def f211w_f211_working_capital_turnover_velocity_calc118_10d_slope_v118_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(11) / revenue.pct_change(6)).diff(20)).pct_change(12)).rolling(23).std()).rolling(28).max()) * 0.727705).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc118_10d_slope_v118_signal'] = f211w_f211_working_capital_turnover_velocity_calc118_10d_slope_v118_signal

def f211w_f211_working_capital_turnover_velocity_calc119_42d_slope_v119_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(7).mean()).rolling(12).max()).pct_change(20)).rolling(22).std()) * 0.684728).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc119_42d_slope_v119_signal'] = f211w_f211_working_capital_turnover_velocity_calc119_42d_slope_v119_signal

def f211w_f211_working_capital_turnover_velocity_calc120_5d_slope_v120_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 93.6751)).rolling(28).mean()).diff(11)).rolling(2).min()).rolling(8).var()) * 0.147831).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc120_5d_slope_v120_signal'] = f211w_f211_working_capital_turnover_velocity_calc120_5d_slope_v120_signal

def f211w_f211_working_capital_turnover_velocity_calc121_126d_slope_v121_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(7).min()).rolling(17).min()).rolling(13).min()).rolling(14).max()) * 0.261525).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc121_126d_slope_v121_signal'] = f211w_f211_working_capital_turnover_velocity_calc121_126d_slope_v121_signal

def f211w_f211_working_capital_turnover_velocity_calc122_252d_slope_v122_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 48.001)).rolling(12).mean()).rolling(5).var()).rolling(12).mean()) * 0.85677).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc122_252d_slope_v122_signal'] = f211w_f211_working_capital_turnover_velocity_calc122_252d_slope_v122_signal

def f211w_f211_working_capital_turnover_velocity_calc123_42d_slope_v123_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(15).mean()).diff(6)).rolling(30).max()).rolling(7).min()) * 0.083502).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc123_42d_slope_v123_signal'] = f211w_f211_working_capital_turnover_velocity_calc123_42d_slope_v123_signal

def f211w_f211_working_capital_turnover_velocity_calc124_5d_slope_v124_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(18) / revenue.pct_change(9)).rolling(9).var()).rolling(3).mean()).rolling(20).min()) * 0.96491).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc124_5d_slope_v124_signal'] = f211w_f211_working_capital_turnover_velocity_calc124_5d_slope_v124_signal

def f211w_f211_working_capital_turnover_velocity_calc125_252d_slope_v125_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(3) / revenue.pct_change(10)).rolling(17).max()).rolling(5).std()).rolling(8).mean()).rolling(22).std()) * 0.063415).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc125_252d_slope_v125_signal'] = f211w_f211_working_capital_turnover_velocity_calc125_252d_slope_v125_signal

def f211w_f211_working_capital_turnover_velocity_calc126_5d_slope_v126_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 47.4097)).rolling(14).max()).rolling(13).std()).rolling(13).min()).rolling(16).std()) * 0.123199).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc126_5d_slope_v126_signal'] = f211w_f211_working_capital_turnover_velocity_calc126_5d_slope_v126_signal

def f211w_f211_working_capital_turnover_velocity_calc127_21d_slope_v127_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(2) / revenue.pct_change(5)).rolling(4).mean()).diff(12)).pct_change(18)).rolling(26).min()) * 0.268133).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc127_21d_slope_v127_signal'] = f211w_f211_working_capital_turnover_velocity_calc127_21d_slope_v127_signal

def f211w_f211_working_capital_turnover_velocity_calc128_10d_slope_v128_signal(workingcapital, revenue):
    res = (((((workingcapital * 55.4048 - revenue).rolling(11).min()).rolling(14).mean()) * 0.833981).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc128_10d_slope_v128_signal'] = f211w_f211_working_capital_turnover_velocity_calc128_10d_slope_v128_signal

def f211w_f211_working_capital_turnover_velocity_calc129_63d_slope_v129_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(8).std()).pct_change(7)) * 0.516481).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc129_63d_slope_v129_signal'] = f211w_f211_working_capital_turnover_velocity_calc129_63d_slope_v129_signal

def f211w_f211_working_capital_turnover_velocity_calc130_5d_slope_v130_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(14) / (revenue.shift(4) + 42.3952)).diff(3)).rolling(14).mean()).rolling(14).max()) * 0.978514).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc130_5d_slope_v130_signal'] = f211w_f211_working_capital_turnover_velocity_calc130_5d_slope_v130_signal

def f211w_f211_working_capital_turnover_velocity_calc131_21d_slope_v131_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(6).min()).rolling(20).std()) * 0.519294).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc131_21d_slope_v131_signal'] = f211w_f211_working_capital_turnover_velocity_calc131_21d_slope_v131_signal

def f211w_f211_working_capital_turnover_velocity_calc132_63d_slope_v132_signal(workingcapital, revenue):
    res = ((((((workingcapital * 75.8619 - revenue).rolling(10).min()).rolling(22).min()).rolling(20).min()) * 0.930857).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc132_63d_slope_v132_signal'] = f211w_f211_working_capital_turnover_velocity_calc132_63d_slope_v132_signal

def f211w_f211_working_capital_turnover_velocity_calc133_42d_slope_v133_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 3.8428)).rolling(24).var()).rolling(3).std()).diff(16)) * 0.279906).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc133_42d_slope_v133_signal'] = f211w_f211_working_capital_turnover_velocity_calc133_42d_slope_v133_signal

def f211w_f211_working_capital_turnover_velocity_calc134_21d_slope_v134_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(9) / revenue.pct_change(16)).rolling(29).mean()).rolling(6).std()).rolling(25).var()).rolling(26).min()) * 0.811038).diff(11).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc134_21d_slope_v134_signal'] = f211w_f211_working_capital_turnover_velocity_calc134_21d_slope_v134_signal

def f211w_f211_working_capital_turnover_velocity_calc135_21d_slope_v135_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).min()).rolling(29).max()).rolling(28).var()).rolling(18).mean()) * 0.60288).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc135_21d_slope_v135_signal'] = f211w_f211_working_capital_turnover_velocity_calc135_21d_slope_v135_signal

def f211w_f211_working_capital_turnover_velocity_calc136_5d_slope_v136_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 31.1812)).pct_change(7)).pct_change(2)) * 0.506659).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc136_5d_slope_v136_signal'] = f211w_f211_working_capital_turnover_velocity_calc136_5d_slope_v136_signal

def f211w_f211_working_capital_turnover_velocity_calc137_5d_slope_v137_signal(workingcapital, revenue):
    res = ((((((workingcapital * 45.6992 - revenue).diff(4)).diff(1)).rolling(13).std()) * 0.90967).diff(16).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc137_5d_slope_v137_signal'] = f211w_f211_working_capital_turnover_velocity_calc137_5d_slope_v137_signal

def f211w_f211_working_capital_turnover_velocity_calc138_63d_slope_v138_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(16) / (revenue.shift(10) + 44.6657)).pct_change(9)).diff(3)) * 0.95131).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc138_63d_slope_v138_signal'] = f211w_f211_working_capital_turnover_velocity_calc138_63d_slope_v138_signal

def f211w_f211_working_capital_turnover_velocity_calc139_5d_slope_v139_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(8)).rolling(22).var()).rolling(18).min()) * 0.169649).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc139_5d_slope_v139_signal'] = f211w_f211_working_capital_turnover_velocity_calc139_5d_slope_v139_signal

def f211w_f211_working_capital_turnover_velocity_calc140_252d_slope_v140_signal(workingcapital, revenue):
    res = (((((workingcapital * 78.0523 - revenue).rolling(10).std()).rolling(27).max()) * 0.762221).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc140_252d_slope_v140_signal'] = f211w_f211_working_capital_turnover_velocity_calc140_252d_slope_v140_signal

def f211w_f211_working_capital_turnover_velocity_calc141_126d_slope_v141_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(14) / (revenue.shift(7) + 96.7057)).rolling(11).min()).diff(17)) * 0.639886).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc141_126d_slope_v141_signal'] = f211w_f211_working_capital_turnover_velocity_calc141_126d_slope_v141_signal

def f211w_f211_working_capital_turnover_velocity_calc142_42d_slope_v142_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(12) / (revenue.shift(9) + 58.4903)).diff(4)).rolling(4).min()).rolling(10).var()) * 0.017201).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc142_42d_slope_v142_signal'] = f211w_f211_working_capital_turnover_velocity_calc142_42d_slope_v142_signal

def f211w_f211_working_capital_turnover_velocity_calc143_252d_slope_v143_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 27.7608)).pct_change(20)).rolling(23).min()) * 0.652997).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc143_252d_slope_v143_signal'] = f211w_f211_working_capital_turnover_velocity_calc143_252d_slope_v143_signal

def f211w_f211_working_capital_turnover_velocity_calc144_126d_slope_v144_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(2)).rolling(24).max()).rolling(28).max()) * 0.034946).diff(7).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc144_126d_slope_v144_signal'] = f211w_f211_working_capital_turnover_velocity_calc144_126d_slope_v144_signal

def f211w_f211_working_capital_turnover_velocity_calc145_21d_slope_v145_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(18) / (revenue.shift(8) + 72.6823)).pct_change(18)).rolling(11).std()) * 0.227916).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc145_21d_slope_v145_signal'] = f211w_f211_working_capital_turnover_velocity_calc145_21d_slope_v145_signal

def f211w_f211_working_capital_turnover_velocity_calc146_42d_slope_v146_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 12.8816)).rolling(25).std()).pct_change(10)).rolling(27).min()) * 0.263479).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc146_42d_slope_v146_signal'] = f211w_f211_working_capital_turnover_velocity_calc146_42d_slope_v146_signal

def f211w_f211_working_capital_turnover_velocity_calc147_21d_slope_v147_signal(workingcapital, revenue):
    res = (((((((workingcapital * 26.1299 - revenue).rolling(17).mean()).rolling(18).std()).rolling(29).mean()).diff(13)) * 0.29817).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc147_21d_slope_v147_signal'] = f211w_f211_working_capital_turnover_velocity_calc147_21d_slope_v147_signal

def f211w_f211_working_capital_turnover_velocity_calc148_21d_slope_v148_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(6).min()).rolling(29).var()).diff(6)).pct_change(3)) * 0.863432).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc148_21d_slope_v148_signal'] = f211w_f211_working_capital_turnover_velocity_calc148_21d_slope_v148_signal

def f211w_f211_working_capital_turnover_velocity_calc149_21d_slope_v149_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 63.1402)).rolling(26).max()).rolling(17).std()) * 0.183288).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc149_21d_slope_v149_signal'] = f211w_f211_working_capital_turnover_velocity_calc149_21d_slope_v149_signal

def f211w_f211_working_capital_turnover_velocity_calc150_10d_slope_v150_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 61.4865)).rolling(8).max()).diff(12)) * 0.630818).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc150_10d_slope_v150_signal'] = f211w_f211_working_capital_turnover_velocity_calc150_10d_slope_v150_signal


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
