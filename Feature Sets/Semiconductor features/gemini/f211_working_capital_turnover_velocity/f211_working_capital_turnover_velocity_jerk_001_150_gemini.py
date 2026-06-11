import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f211w_f211_working_capital_turnover_velocity_calc001_21d_jerk_v001_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(8) / revenue.pct_change(8)).rolling(6).var()).rolling(14).mean()).rolling(20).max()) * 0.530413).diff(10).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc001_21d_jerk_v001_signal'] = f211w_f211_working_capital_turnover_velocity_calc001_21d_jerk_v001_signal

def f211w_f211_working_capital_turnover_velocity_calc002_5d_jerk_v002_signal(workingcapital, revenue):
    res = ((((((workingcapital * 82.402 - revenue).rolling(30).min()).diff(5)).rolling(30).var()) * 0.302238).diff(16).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc002_5d_jerk_v002_signal'] = f211w_f211_working_capital_turnover_velocity_calc002_5d_jerk_v002_signal

def f211w_f211_working_capital_turnover_velocity_calc003_252d_jerk_v003_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(8)).rolling(25).std()).rolling(20).mean()) * 0.939123).diff(17).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc003_252d_jerk_v003_signal'] = f211w_f211_working_capital_turnover_velocity_calc003_252d_jerk_v003_signal

def f211w_f211_working_capital_turnover_velocity_calc004_5d_jerk_v004_signal(workingcapital, revenue):
    res = (((((workingcapital * 36.7225 - revenue).rolling(3).max()).diff(4)) * 0.64753).diff(1).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc004_5d_jerk_v004_signal'] = f211w_f211_working_capital_turnover_velocity_calc004_5d_jerk_v004_signal

def f211w_f211_working_capital_turnover_velocity_calc005_126d_jerk_v005_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(9) / revenue.pct_change(16)).rolling(24).std()).diff(1)) * 0.445428).diff(10).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc005_126d_jerk_v005_signal'] = f211w_f211_working_capital_turnover_velocity_calc005_126d_jerk_v005_signal

def f211w_f211_working_capital_turnover_velocity_calc006_126d_jerk_v006_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 10.1879)).diff(20)).rolling(11).mean()).rolling(27).mean()).rolling(17).mean()) * 0.519903).diff(7).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc006_126d_jerk_v006_signal'] = f211w_f211_working_capital_turnover_velocity_calc006_126d_jerk_v006_signal

def f211w_f211_working_capital_turnover_velocity_calc007_10d_jerk_v007_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 77.8181)).rolling(17).max()).rolling(24).std()) * 0.824869).diff(16).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc007_10d_jerk_v007_signal'] = f211w_f211_working_capital_turnover_velocity_calc007_10d_jerk_v007_signal

def f211w_f211_working_capital_turnover_velocity_calc008_10d_jerk_v008_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 0.3735)).rolling(25).mean()).diff(4)).rolling(22).var()).rolling(16).std()) * 0.6682).diff(10).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc008_10d_jerk_v008_signal'] = f211w_f211_working_capital_turnover_velocity_calc008_10d_jerk_v008_signal

def f211w_f211_working_capital_turnover_velocity_calc009_42d_jerk_v009_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).mean()).pct_change(2)).rolling(29).mean()).rolling(23).std()) * 0.806915).diff(6).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc009_42d_jerk_v009_signal'] = f211w_f211_working_capital_turnover_velocity_calc009_42d_jerk_v009_signal

def f211w_f211_working_capital_turnover_velocity_calc010_21d_jerk_v010_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 89.4633)).rolling(14).min()).rolling(10).min()) * 0.945987).diff(13).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc010_21d_jerk_v010_signal'] = f211w_f211_working_capital_turnover_velocity_calc010_21d_jerk_v010_signal

def f211w_f211_working_capital_turnover_velocity_calc011_252d_jerk_v011_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 42.2318)).rolling(20).min()).rolling(27).min()) * 0.878401).diff(19).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc011_252d_jerk_v011_signal'] = f211w_f211_working_capital_turnover_velocity_calc011_252d_jerk_v011_signal

def f211w_f211_working_capital_turnover_velocity_calc012_10d_jerk_v012_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(16).min()).rolling(4).mean()) * 0.773581).diff(9).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc012_10d_jerk_v012_signal'] = f211w_f211_working_capital_turnover_velocity_calc012_10d_jerk_v012_signal

def f211w_f211_working_capital_turnover_velocity_calc013_5d_jerk_v013_signal(workingcapital, revenue):
    res = (((((((workingcapital * 70.4864 - revenue).diff(20)).rolling(15).mean()).diff(8)).rolling(13).min()) * 0.67437).diff(13).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc013_5d_jerk_v013_signal'] = f211w_f211_working_capital_turnover_velocity_calc013_5d_jerk_v013_signal

def f211w_f211_working_capital_turnover_velocity_calc014_252d_jerk_v014_signal(workingcapital, revenue):
    res = ((((((workingcapital * 82.6611 - revenue).pct_change(16)).pct_change(6)).rolling(26).mean()) * 0.884221).diff(16).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc014_252d_jerk_v014_signal'] = f211w_f211_working_capital_turnover_velocity_calc014_252d_jerk_v014_signal

def f211w_f211_working_capital_turnover_velocity_calc015_10d_jerk_v015_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(16).mean()).rolling(27).min()) * 0.282594).diff(19).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc015_10d_jerk_v015_signal'] = f211w_f211_working_capital_turnover_velocity_calc015_10d_jerk_v015_signal

def f211w_f211_working_capital_turnover_velocity_calc016_5d_jerk_v016_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(19).mean()).rolling(2).max()).pct_change(3)) * 0.448127).diff(20).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc016_5d_jerk_v016_signal'] = f211w_f211_working_capital_turnover_velocity_calc016_5d_jerk_v016_signal

def f211w_f211_working_capital_turnover_velocity_calc017_126d_jerk_v017_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 30.5293)).pct_change(15)).rolling(19).var()) * 0.508171).diff(20).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc017_126d_jerk_v017_signal'] = f211w_f211_working_capital_turnover_velocity_calc017_126d_jerk_v017_signal

def f211w_f211_working_capital_turnover_velocity_calc018_42d_jerk_v018_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 71.6941)).rolling(28).var()).diff(10)).rolling(18).max()) * 0.366029).diff(12).diff(4).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc018_42d_jerk_v018_signal'] = f211w_f211_working_capital_turnover_velocity_calc018_42d_jerk_v018_signal

def f211w_f211_working_capital_turnover_velocity_calc019_5d_jerk_v019_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 89.698)).rolling(29).mean()).rolling(8).min()) * 0.492574).diff(15).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc019_5d_jerk_v019_signal'] = f211w_f211_working_capital_turnover_velocity_calc019_5d_jerk_v019_signal

def f211w_f211_working_capital_turnover_velocity_calc020_126d_jerk_v020_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(18).max()).rolling(17).std()).rolling(18).mean()).diff(2)) * 0.752006).diff(18).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc020_126d_jerk_v020_signal'] = f211w_f211_working_capital_turnover_velocity_calc020_126d_jerk_v020_signal

def f211w_f211_working_capital_turnover_velocity_calc021_252d_jerk_v021_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 58.5536)).diff(20)).rolling(30).max()).rolling(18).var()) * 0.915883).diff(13).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc021_252d_jerk_v021_signal'] = f211w_f211_working_capital_turnover_velocity_calc021_252d_jerk_v021_signal

def f211w_f211_working_capital_turnover_velocity_calc022_63d_jerk_v022_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(15).std()).rolling(24).max()) * 0.757127).diff(17).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc022_63d_jerk_v022_signal'] = f211w_f211_working_capital_turnover_velocity_calc022_63d_jerk_v022_signal

def f211w_f211_working_capital_turnover_velocity_calc023_252d_jerk_v023_signal(workingcapital, revenue):
    res = (((((((workingcapital * 70.1793 - revenue).rolling(23).var()).rolling(23).var()).rolling(24).std()).diff(6)) * 0.853493).diff(17).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc023_252d_jerk_v023_signal'] = f211w_f211_working_capital_turnover_velocity_calc023_252d_jerk_v023_signal

def f211w_f211_working_capital_turnover_velocity_calc024_126d_jerk_v024_signal(workingcapital, revenue):
    res = (((((((workingcapital * 63.7241 - revenue).diff(14)).diff(18)).rolling(30).var()).pct_change(14)) * 0.706146).diff(1).diff(17).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc024_126d_jerk_v024_signal'] = f211w_f211_working_capital_turnover_velocity_calc024_126d_jerk_v024_signal

def f211w_f211_working_capital_turnover_velocity_calc025_5d_jerk_v025_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(2) / (revenue.shift(4) + 2.6247)).rolling(6).var()).pct_change(2)).diff(10)).rolling(26).std()) * 0.15242).diff(18).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc025_5d_jerk_v025_signal'] = f211w_f211_working_capital_turnover_velocity_calc025_5d_jerk_v025_signal

def f211w_f211_working_capital_turnover_velocity_calc026_21d_jerk_v026_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 81.4212)).pct_change(10)).diff(2)).rolling(14).min()).rolling(27).min()) * 0.11043).diff(11).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc026_21d_jerk_v026_signal'] = f211w_f211_working_capital_turnover_velocity_calc026_21d_jerk_v026_signal

def f211w_f211_working_capital_turnover_velocity_calc027_5d_jerk_v027_signal(workingcapital, revenue):
    res = (((((((workingcapital * 1.3952 - revenue).diff(20)).rolling(26).std()).diff(7)).rolling(16).var()) * 0.256314).diff(6).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc027_5d_jerk_v027_signal'] = f211w_f211_working_capital_turnover_velocity_calc027_5d_jerk_v027_signal

def f211w_f211_working_capital_turnover_velocity_calc028_10d_jerk_v028_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(4) / (revenue.shift(7) + 96.2513)).rolling(6).var()).rolling(20).std()).pct_change(9)).rolling(12).mean()) * 0.730378).diff(15).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc028_10d_jerk_v028_signal'] = f211w_f211_working_capital_turnover_velocity_calc028_10d_jerk_v028_signal

def f211w_f211_working_capital_turnover_velocity_calc029_5d_jerk_v029_signal(workingcapital, revenue):
    res = (((((((workingcapital * 15.455 - revenue).rolling(4).var()).pct_change(11)).rolling(9).max()).rolling(18).std()) * 0.326177).diff(3).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc029_5d_jerk_v029_signal'] = f211w_f211_working_capital_turnover_velocity_calc029_5d_jerk_v029_signal

def f211w_f211_working_capital_turnover_velocity_calc030_10d_jerk_v030_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(8) / revenue.pct_change(7)).rolling(13).var()).rolling(8).var()).pct_change(20)) * 0.536295).diff(17).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc030_10d_jerk_v030_signal'] = f211w_f211_working_capital_turnover_velocity_calc030_10d_jerk_v030_signal

def f211w_f211_working_capital_turnover_velocity_calc031_63d_jerk_v031_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 82.3865)).rolling(21).max()).rolling(3).std()).diff(11)).rolling(27).min()) * 0.971511).diff(4).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc031_63d_jerk_v031_signal'] = f211w_f211_working_capital_turnover_velocity_calc031_63d_jerk_v031_signal

def f211w_f211_working_capital_turnover_velocity_calc032_21d_jerk_v032_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(11).mean()).diff(7)).rolling(18).var()) * 0.287172).diff(3).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc032_21d_jerk_v032_signal'] = f211w_f211_working_capital_turnover_velocity_calc032_21d_jerk_v032_signal

def f211w_f211_working_capital_turnover_velocity_calc033_10d_jerk_v033_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(3) / revenue.pct_change(7)).pct_change(7)).pct_change(14)).pct_change(4)).rolling(19).std()) * 0.767852).diff(14).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc033_10d_jerk_v033_signal'] = f211w_f211_working_capital_turnover_velocity_calc033_10d_jerk_v033_signal

def f211w_f211_working_capital_turnover_velocity_calc034_126d_jerk_v034_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 68.6357)).pct_change(9)).rolling(4).max()) * 0.033278).diff(19).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc034_126d_jerk_v034_signal'] = f211w_f211_working_capital_turnover_velocity_calc034_126d_jerk_v034_signal

def f211w_f211_working_capital_turnover_velocity_calc035_21d_jerk_v035_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(19).mean()).rolling(22).mean()).diff(20)).rolling(26).mean()) * 0.452103).diff(19).diff(2).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc035_21d_jerk_v035_signal'] = f211w_f211_working_capital_turnover_velocity_calc035_21d_jerk_v035_signal

def f211w_f211_working_capital_turnover_velocity_calc036_126d_jerk_v036_signal(workingcapital, revenue):
    res = (((((workingcapital * 84.8403 - revenue).rolling(26).var()).rolling(14).min()) * 0.360546).diff(13).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc036_126d_jerk_v036_signal'] = f211w_f211_working_capital_turnover_velocity_calc036_126d_jerk_v036_signal

def f211w_f211_working_capital_turnover_velocity_calc037_42d_jerk_v037_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(13) / (revenue.shift(9) + 15.7167)).pct_change(12)).rolling(19).mean()).pct_change(18)).rolling(5).std()) * 0.225468).diff(2).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc037_42d_jerk_v037_signal'] = f211w_f211_working_capital_turnover_velocity_calc037_42d_jerk_v037_signal

def f211w_f211_working_capital_turnover_velocity_calc038_63d_jerk_v038_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 59.7058)).diff(17)).rolling(7).std()).rolling(9).std()) * 0.536409).diff(20).diff(9).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc038_63d_jerk_v038_signal'] = f211w_f211_working_capital_turnover_velocity_calc038_63d_jerk_v038_signal

def f211w_f211_working_capital_turnover_velocity_calc039_10d_jerk_v039_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(18) / revenue.pct_change(15)).rolling(11).mean()).diff(3)).rolling(5).var()).rolling(25).std()) * 0.667558).diff(19).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc039_10d_jerk_v039_signal'] = f211w_f211_working_capital_turnover_velocity_calc039_10d_jerk_v039_signal

def f211w_f211_working_capital_turnover_velocity_calc040_21d_jerk_v040_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 35.7781)).rolling(17).var()).rolling(12).min()) * 0.66787).diff(20).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc040_21d_jerk_v040_signal'] = f211w_f211_working_capital_turnover_velocity_calc040_21d_jerk_v040_signal

def f211w_f211_working_capital_turnover_velocity_calc041_126d_jerk_v041_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 58.4586)).rolling(27).std()).rolling(24).std()).diff(14)) * 0.564241).diff(9).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc041_126d_jerk_v041_signal'] = f211w_f211_working_capital_turnover_velocity_calc041_126d_jerk_v041_signal

def f211w_f211_working_capital_turnover_velocity_calc042_10d_jerk_v042_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(16) / (revenue.shift(8) + 67.9901)).rolling(5).max()).rolling(22).std()).rolling(4).max()) * 0.334932).diff(9).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc042_10d_jerk_v042_signal'] = f211w_f211_working_capital_turnover_velocity_calc042_10d_jerk_v042_signal

def f211w_f211_working_capital_turnover_velocity_calc043_63d_jerk_v043_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(1) / revenue.pct_change(17)).pct_change(19)).rolling(14).max()) * 0.728874).diff(19).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc043_63d_jerk_v043_signal'] = f211w_f211_working_capital_turnover_velocity_calc043_63d_jerk_v043_signal

def f211w_f211_working_capital_turnover_velocity_calc044_5d_jerk_v044_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(19)).diff(10)) * 0.5426).diff(5).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc044_5d_jerk_v044_signal'] = f211w_f211_working_capital_turnover_velocity_calc044_5d_jerk_v044_signal

def f211w_f211_working_capital_turnover_velocity_calc045_63d_jerk_v045_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(20)).pct_change(17)).rolling(16).std()) * 0.398849).diff(6).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc045_63d_jerk_v045_signal'] = f211w_f211_working_capital_turnover_velocity_calc045_63d_jerk_v045_signal

def f211w_f211_working_capital_turnover_velocity_calc046_63d_jerk_v046_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 94.8763)).rolling(4).std()).rolling(13).var()).rolling(3).std()) * 0.656225).diff(7).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc046_63d_jerk_v046_signal'] = f211w_f211_working_capital_turnover_velocity_calc046_63d_jerk_v046_signal

def f211w_f211_working_capital_turnover_velocity_calc047_252d_jerk_v047_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 36.189)).rolling(22).max()).pct_change(9)).pct_change(9)).rolling(19).max()) * 0.470281).diff(19).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc047_252d_jerk_v047_signal'] = f211w_f211_working_capital_turnover_velocity_calc047_252d_jerk_v047_signal

def f211w_f211_working_capital_turnover_velocity_calc048_42d_jerk_v048_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 65.4022)).rolling(13).min()).pct_change(12)).rolling(27).min()).rolling(30).min()) * 0.367991).diff(20).diff(1).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc048_42d_jerk_v048_signal'] = f211w_f211_working_capital_turnover_velocity_calc048_42d_jerk_v048_signal

def f211w_f211_working_capital_turnover_velocity_calc049_63d_jerk_v049_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 88.2152)).rolling(7).std()).rolling(21).var()) * 0.441101).diff(4).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc049_63d_jerk_v049_signal'] = f211w_f211_working_capital_turnover_velocity_calc049_63d_jerk_v049_signal

def f211w_f211_working_capital_turnover_velocity_calc050_42d_jerk_v050_signal(workingcapital, revenue):
    res = (((((workingcapital * 81.1361 - revenue).diff(14)).rolling(9).mean()) * 0.715851).diff(2).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc050_42d_jerk_v050_signal'] = f211w_f211_working_capital_turnover_velocity_calc050_42d_jerk_v050_signal

def f211w_f211_working_capital_turnover_velocity_calc051_63d_jerk_v051_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 59.2755)).rolling(7).var()).rolling(14).max()) * 0.14203).diff(20).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc051_63d_jerk_v051_signal'] = f211w_f211_working_capital_turnover_velocity_calc051_63d_jerk_v051_signal

def f211w_f211_working_capital_turnover_velocity_calc052_126d_jerk_v052_signal(workingcapital, revenue):
    res = ((((((workingcapital * 1.9601 - revenue).pct_change(16)).rolling(9).std()).pct_change(14)) * 0.715156).diff(20).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc052_126d_jerk_v052_signal'] = f211w_f211_working_capital_turnover_velocity_calc052_126d_jerk_v052_signal

def f211w_f211_working_capital_turnover_velocity_calc053_252d_jerk_v053_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(9) / revenue.pct_change(6)).rolling(16).var()).rolling(20).max()).rolling(9).mean()).rolling(14).min()) * 0.76214).diff(5).diff(4).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc053_252d_jerk_v053_signal'] = f211w_f211_working_capital_turnover_velocity_calc053_252d_jerk_v053_signal

def f211w_f211_working_capital_turnover_velocity_calc054_5d_jerk_v054_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 20.3146)).rolling(30).min()).rolling(21).max()) * 0.8524).diff(2).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc054_5d_jerk_v054_signal'] = f211w_f211_working_capital_turnover_velocity_calc054_5d_jerk_v054_signal

def f211w_f211_working_capital_turnover_velocity_calc055_63d_jerk_v055_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(18) / revenue.pct_change(1)).rolling(18).min()).rolling(13).min()).pct_change(2)).diff(17)) * 0.101326).diff(14).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc055_63d_jerk_v055_signal'] = f211w_f211_working_capital_turnover_velocity_calc055_63d_jerk_v055_signal

def f211w_f211_working_capital_turnover_velocity_calc056_252d_jerk_v056_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).var()).pct_change(8)) * 0.763298).diff(3).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc056_252d_jerk_v056_signal'] = f211w_f211_working_capital_turnover_velocity_calc056_252d_jerk_v056_signal

def f211w_f211_working_capital_turnover_velocity_calc057_63d_jerk_v057_signal(workingcapital, revenue):
    res = (((((workingcapital * 87.689 - revenue).rolling(2).max()).rolling(22).min()) * 0.410474).diff(7).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc057_63d_jerk_v057_signal'] = f211w_f211_working_capital_turnover_velocity_calc057_63d_jerk_v057_signal

def f211w_f211_working_capital_turnover_velocity_calc058_42d_jerk_v058_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).var()).rolling(23).var()).rolling(26).min()).rolling(15).std()) * 0.161683).diff(18).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc058_42d_jerk_v058_signal'] = f211w_f211_working_capital_turnover_velocity_calc058_42d_jerk_v058_signal

def f211w_f211_working_capital_turnover_velocity_calc059_42d_jerk_v059_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(16) / (revenue.shift(5) + 17.9541)).rolling(25).min()).rolling(29).std()).pct_change(4)).diff(8)) * 0.557912).diff(15).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc059_42d_jerk_v059_signal'] = f211w_f211_working_capital_turnover_velocity_calc059_42d_jerk_v059_signal

def f211w_f211_working_capital_turnover_velocity_calc060_5d_jerk_v060_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 21.5244)).diff(1)).pct_change(3)).pct_change(5)) * 0.40255).diff(16).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc060_5d_jerk_v060_signal'] = f211w_f211_working_capital_turnover_velocity_calc060_5d_jerk_v060_signal

def f211w_f211_working_capital_turnover_velocity_calc061_42d_jerk_v061_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(20) / revenue.pct_change(2)).rolling(21).min()).diff(17)).rolling(24).var()) * 0.26783).diff(20).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc061_42d_jerk_v061_signal'] = f211w_f211_working_capital_turnover_velocity_calc061_42d_jerk_v061_signal

def f211w_f211_working_capital_turnover_velocity_calc062_252d_jerk_v062_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(15) / (revenue.shift(1) + 82.0409)).rolling(27).mean()).rolling(18).max()) * 0.637485).diff(17).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc062_252d_jerk_v062_signal'] = f211w_f211_working_capital_turnover_velocity_calc062_252d_jerk_v062_signal

def f211w_f211_working_capital_turnover_velocity_calc063_63d_jerk_v063_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(8) / (revenue.shift(1) + 17.0313)).rolling(23).var()).rolling(14).min()).rolling(8).max()) * 0.04534).diff(17).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc063_63d_jerk_v063_signal'] = f211w_f211_working_capital_turnover_velocity_calc063_63d_jerk_v063_signal

def f211w_f211_working_capital_turnover_velocity_calc064_126d_jerk_v064_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(18) / (revenue.shift(5) + 70.3918)).pct_change(9)).rolling(21).std()).rolling(16).std()) * 0.910794).diff(13).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc064_126d_jerk_v064_signal'] = f211w_f211_working_capital_turnover_velocity_calc064_126d_jerk_v064_signal

def f211w_f211_working_capital_turnover_velocity_calc065_5d_jerk_v065_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(4) / (revenue.shift(9) + 26.1846)).rolling(27).mean()).rolling(10).max()).rolling(28).max()) * 0.408992).diff(19).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc065_5d_jerk_v065_signal'] = f211w_f211_working_capital_turnover_velocity_calc065_5d_jerk_v065_signal

def f211w_f211_working_capital_turnover_velocity_calc066_126d_jerk_v066_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(11) / revenue.pct_change(15)).rolling(29).max()).rolling(17).mean()).rolling(10).mean()) * 0.379539).diff(3).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc066_126d_jerk_v066_signal'] = f211w_f211_working_capital_turnover_velocity_calc066_126d_jerk_v066_signal

def f211w_f211_working_capital_turnover_velocity_calc067_126d_jerk_v067_signal(workingcapital, revenue):
    res = (((((((workingcapital * 78.8867 - revenue).rolling(24).mean()).pct_change(9)).rolling(11).std()).rolling(14).mean()) * 0.225975).diff(11).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc067_126d_jerk_v067_signal'] = f211w_f211_working_capital_turnover_velocity_calc067_126d_jerk_v067_signal

def f211w_f211_working_capital_turnover_velocity_calc068_63d_jerk_v068_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 93.1465)).diff(7)).rolling(25).min()).rolling(9).std()).diff(8)) * 0.477024).diff(9).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc068_63d_jerk_v068_signal'] = f211w_f211_working_capital_turnover_velocity_calc068_63d_jerk_v068_signal

def f211w_f211_working_capital_turnover_velocity_calc069_10d_jerk_v069_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 20.3564)).diff(16)).rolling(2).max()) * 0.254702).diff(18).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc069_10d_jerk_v069_signal'] = f211w_f211_working_capital_turnover_velocity_calc069_10d_jerk_v069_signal

def f211w_f211_working_capital_turnover_velocity_calc070_252d_jerk_v070_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 48.281)).rolling(14).var()).rolling(26).std()).rolling(6).max()).rolling(18).mean()) * 0.618254).diff(14).diff(16).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc070_252d_jerk_v070_signal'] = f211w_f211_working_capital_turnover_velocity_calc070_252d_jerk_v070_signal

def f211w_f211_working_capital_turnover_velocity_calc071_63d_jerk_v071_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(1)).rolling(23).mean()).rolling(14).std()) * 0.350343).diff(19).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc071_63d_jerk_v071_signal'] = f211w_f211_working_capital_turnover_velocity_calc071_63d_jerk_v071_signal

def f211w_f211_working_capital_turnover_velocity_calc072_21d_jerk_v072_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(6) / (revenue.shift(9) + 36.2241)).rolling(12).max()).rolling(7).var()).rolling(15).min()) * 0.854605).diff(7).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc072_21d_jerk_v072_signal'] = f211w_f211_working_capital_turnover_velocity_calc072_21d_jerk_v072_signal

def f211w_f211_working_capital_turnover_velocity_calc073_126d_jerk_v073_signal(workingcapital, revenue):
    res = (((((workingcapital * 75.2444 - revenue).rolling(23).max()).rolling(28).std()) * 0.367776).diff(4).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc073_126d_jerk_v073_signal'] = f211w_f211_working_capital_turnover_velocity_calc073_126d_jerk_v073_signal

def f211w_f211_working_capital_turnover_velocity_calc074_252d_jerk_v074_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(15).std()).rolling(6).min()) * 0.433574).diff(17).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc074_252d_jerk_v074_signal'] = f211w_f211_working_capital_turnover_velocity_calc074_252d_jerk_v074_signal

def f211w_f211_working_capital_turnover_velocity_calc075_126d_jerk_v075_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(6)).rolling(8).mean()) * 0.486888).diff(9).diff(16).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc075_126d_jerk_v075_signal'] = f211w_f211_working_capital_turnover_velocity_calc075_126d_jerk_v075_signal

def f211w_f211_working_capital_turnover_velocity_calc076_252d_jerk_v076_signal(workingcapital, revenue):
    res = (((((((workingcapital * 63.0232 - revenue).pct_change(9)).rolling(2).var()).rolling(5).min()).rolling(29).var()) * 0.450858).diff(20).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc076_252d_jerk_v076_signal'] = f211w_f211_working_capital_turnover_velocity_calc076_252d_jerk_v076_signal

def f211w_f211_working_capital_turnover_velocity_calc077_63d_jerk_v077_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(12) / revenue.pct_change(11)).rolling(26).min()).diff(15)).rolling(14).mean()).rolling(11).max()) * 0.646148).diff(15).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc077_63d_jerk_v077_signal'] = f211w_f211_working_capital_turnover_velocity_calc077_63d_jerk_v077_signal

def f211w_f211_working_capital_turnover_velocity_calc078_252d_jerk_v078_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(7).mean()).rolling(9).var()) * 0.801563).diff(11).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc078_252d_jerk_v078_signal'] = f211w_f211_working_capital_turnover_velocity_calc078_252d_jerk_v078_signal

def f211w_f211_working_capital_turnover_velocity_calc079_126d_jerk_v079_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(15) / revenue.pct_change(12)).rolling(16).max()).rolling(7).min()).rolling(29).std()).rolling(6).mean()) * 0.272123).diff(8).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc079_126d_jerk_v079_signal'] = f211w_f211_working_capital_turnover_velocity_calc079_126d_jerk_v079_signal

def f211w_f211_working_capital_turnover_velocity_calc080_126d_jerk_v080_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 70.0996)).rolling(3).max()).rolling(26).mean()).rolling(18).min()) * 0.088463).diff(3).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc080_126d_jerk_v080_signal'] = f211w_f211_working_capital_turnover_velocity_calc080_126d_jerk_v080_signal

def f211w_f211_working_capital_turnover_velocity_calc081_21d_jerk_v081_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(8) / revenue.pct_change(8)).rolling(22).min()).rolling(6).std()).rolling(28).max()) * 0.092625).diff(6).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc081_21d_jerk_v081_signal'] = f211w_f211_working_capital_turnover_velocity_calc081_21d_jerk_v081_signal

def f211w_f211_working_capital_turnover_velocity_calc082_5d_jerk_v082_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(11) / (revenue.shift(8) + 66.3886)).rolling(6).min()).diff(18)).rolling(20).std()).rolling(16).max()) * 0.853161).diff(19).diff(14).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc082_5d_jerk_v082_signal'] = f211w_f211_working_capital_turnover_velocity_calc082_5d_jerk_v082_signal

def f211w_f211_working_capital_turnover_velocity_calc083_63d_jerk_v083_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 64.0147)).rolling(13).var()).rolling(10).min()).rolling(11).std()) * 0.533108).diff(1).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc083_63d_jerk_v083_signal'] = f211w_f211_working_capital_turnover_velocity_calc083_63d_jerk_v083_signal

def f211w_f211_working_capital_turnover_velocity_calc084_63d_jerk_v084_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 81.5564)).rolling(26).min()).rolling(11).min()).rolling(26).mean()).rolling(27).min()) * 0.840988).diff(10).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc084_63d_jerk_v084_signal'] = f211w_f211_working_capital_turnover_velocity_calc084_63d_jerk_v084_signal

def f211w_f211_working_capital_turnover_velocity_calc085_10d_jerk_v085_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(24).std()).diff(13)) * 0.547248).diff(13).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc085_10d_jerk_v085_signal'] = f211w_f211_working_capital_turnover_velocity_calc085_10d_jerk_v085_signal

def f211w_f211_working_capital_turnover_velocity_calc086_21d_jerk_v086_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(9) / revenue.pct_change(10)).rolling(27).max()).rolling(15).var()).rolling(29).std()).rolling(7).mean()) * 0.622817).diff(5).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc086_21d_jerk_v086_signal'] = f211w_f211_working_capital_turnover_velocity_calc086_21d_jerk_v086_signal

def f211w_f211_working_capital_turnover_velocity_calc087_5d_jerk_v087_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(9) / (revenue.shift(10) + 63.7256)).rolling(3).std()).rolling(2).max()) * 0.615375).diff(6).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc087_5d_jerk_v087_signal'] = f211w_f211_working_capital_turnover_velocity_calc087_5d_jerk_v087_signal

def f211w_f211_working_capital_turnover_velocity_calc088_21d_jerk_v088_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 26.9926)).rolling(12).std()).rolling(11).min()).pct_change(16)) * 0.710892).diff(12).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc088_21d_jerk_v088_signal'] = f211w_f211_working_capital_turnover_velocity_calc088_21d_jerk_v088_signal

def f211w_f211_working_capital_turnover_velocity_calc089_126d_jerk_v089_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 79.1633)).rolling(7).min()).rolling(30).std()).pct_change(9)).pct_change(13)) * 0.333644).diff(1).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc089_126d_jerk_v089_signal'] = f211w_f211_working_capital_turnover_velocity_calc089_126d_jerk_v089_signal

def f211w_f211_working_capital_turnover_velocity_calc090_252d_jerk_v090_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(4)).rolling(23).max()).rolling(17).std()).rolling(23).min()) * 0.387102).diff(10).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc090_252d_jerk_v090_signal'] = f211w_f211_working_capital_turnover_velocity_calc090_252d_jerk_v090_signal

def f211w_f211_working_capital_turnover_velocity_calc091_10d_jerk_v091_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(8).var()).rolling(30).var()).rolling(29).mean()).diff(7)) * 0.051342).diff(4).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc091_10d_jerk_v091_signal'] = f211w_f211_working_capital_turnover_velocity_calc091_10d_jerk_v091_signal

def f211w_f211_working_capital_turnover_velocity_calc092_126d_jerk_v092_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 43.4727)).rolling(20).mean()).pct_change(16)) * 0.024766).diff(20).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc092_126d_jerk_v092_signal'] = f211w_f211_working_capital_turnover_velocity_calc092_126d_jerk_v092_signal

def f211w_f211_working_capital_turnover_velocity_calc093_21d_jerk_v093_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(20) / revenue.pct_change(11)).rolling(13).mean()).diff(5)) * 0.253748).diff(18).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc093_21d_jerk_v093_signal'] = f211w_f211_working_capital_turnover_velocity_calc093_21d_jerk_v093_signal

def f211w_f211_working_capital_turnover_velocity_calc094_10d_jerk_v094_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 48.8355)).rolling(13).min()).diff(5)).rolling(30).var()).rolling(17).mean()) * 0.320405).diff(15).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc094_10d_jerk_v094_signal'] = f211w_f211_working_capital_turnover_velocity_calc094_10d_jerk_v094_signal

def f211w_f211_working_capital_turnover_velocity_calc095_21d_jerk_v095_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(19) / (revenue.shift(3) + 54.3191)).rolling(10).min()).pct_change(20)).pct_change(18)).rolling(4).std()) * 0.49029).diff(17).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc095_21d_jerk_v095_signal'] = f211w_f211_working_capital_turnover_velocity_calc095_21d_jerk_v095_signal

def f211w_f211_working_capital_turnover_velocity_calc096_42d_jerk_v096_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(30).std()).rolling(21).mean()).pct_change(12)).pct_change(20)) * 0.268082).diff(8).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc096_42d_jerk_v096_signal'] = f211w_f211_working_capital_turnover_velocity_calc096_42d_jerk_v096_signal

def f211w_f211_working_capital_turnover_velocity_calc097_126d_jerk_v097_signal(workingcapital, revenue):
    res = (((((workingcapital * 6.4278 - revenue).rolling(11).max()).rolling(15).var()) * 0.95782).diff(11).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc097_126d_jerk_v097_signal'] = f211w_f211_working_capital_turnover_velocity_calc097_126d_jerk_v097_signal

def f211w_f211_working_capital_turnover_velocity_calc098_5d_jerk_v098_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 52.3677)).rolling(5).std()).rolling(20).mean()).diff(13)) * 0.075346).diff(16).diff(17).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc098_5d_jerk_v098_signal'] = f211w_f211_working_capital_turnover_velocity_calc098_5d_jerk_v098_signal

def f211w_f211_working_capital_turnover_velocity_calc099_63d_jerk_v099_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 70.1613)).diff(16)).pct_change(3)) * 0.26082).diff(15).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc099_63d_jerk_v099_signal'] = f211w_f211_working_capital_turnover_velocity_calc099_63d_jerk_v099_signal

def f211w_f211_working_capital_turnover_velocity_calc100_21d_jerk_v100_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(14) / (revenue.shift(6) + 55.8462)).rolling(25).mean()).rolling(28).mean()).rolling(4).var()).rolling(18).std()) * 0.929479).diff(4).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc100_21d_jerk_v100_signal'] = f211w_f211_working_capital_turnover_velocity_calc100_21d_jerk_v100_signal

def f211w_f211_working_capital_turnover_velocity_calc101_126d_jerk_v101_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(19)).rolling(25).max()).rolling(15).max()) * 0.387624).diff(4).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc101_126d_jerk_v101_signal'] = f211w_f211_working_capital_turnover_velocity_calc101_126d_jerk_v101_signal

def f211w_f211_working_capital_turnover_velocity_calc102_21d_jerk_v102_signal(workingcapital, revenue):
    res = ((((((workingcapital * 67.4818 - revenue).rolling(12).max()).diff(6)).rolling(21).max()) * 0.698499).diff(15).diff(12).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc102_21d_jerk_v102_signal'] = f211w_f211_working_capital_turnover_velocity_calc102_21d_jerk_v102_signal

def f211w_f211_working_capital_turnover_velocity_calc103_21d_jerk_v103_signal(workingcapital, revenue):
    res = (((((workingcapital * 55.0531 - revenue).rolling(19).max()).rolling(14).std()) * 0.986913).diff(18).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc103_21d_jerk_v103_signal'] = f211w_f211_working_capital_turnover_velocity_calc103_21d_jerk_v103_signal

def f211w_f211_working_capital_turnover_velocity_calc104_21d_jerk_v104_signal(workingcapital, revenue):
    res = (((((workingcapital * 96.169 - revenue).rolling(6).max()).rolling(2).var()) * 0.44855).diff(10).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc104_21d_jerk_v104_signal'] = f211w_f211_working_capital_turnover_velocity_calc104_21d_jerk_v104_signal

def f211w_f211_working_capital_turnover_velocity_calc105_10d_jerk_v105_signal(workingcapital, revenue):
    res = (((((((workingcapital * 85.5865 - revenue).rolling(5).std()).rolling(16).mean()).rolling(6).var()).rolling(10).std()) * 0.031267).diff(12).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc105_10d_jerk_v105_signal'] = f211w_f211_working_capital_turnover_velocity_calc105_10d_jerk_v105_signal

def f211w_f211_working_capital_turnover_velocity_calc106_10d_jerk_v106_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 23.3761)).rolling(25).mean()).rolling(27).var()).rolling(7).min()).rolling(28).min()) * 0.804853).diff(19).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc106_10d_jerk_v106_signal'] = f211w_f211_working_capital_turnover_velocity_calc106_10d_jerk_v106_signal

def f211w_f211_working_capital_turnover_velocity_calc107_63d_jerk_v107_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(19) / (revenue.shift(7) + 64.2612)).pct_change(14)).rolling(29).min()).rolling(29).mean()) * 0.046624).diff(8).diff(20).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc107_63d_jerk_v107_signal'] = f211w_f211_working_capital_turnover_velocity_calc107_63d_jerk_v107_signal

def f211w_f211_working_capital_turnover_velocity_calc108_5d_jerk_v108_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(2) / (revenue.shift(5) + 63.4253)).rolling(6).max()).rolling(18).var()).diff(8)).rolling(3).std()) * 0.62955).diff(13).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc108_5d_jerk_v108_signal'] = f211w_f211_working_capital_turnover_velocity_calc108_5d_jerk_v108_signal

def f211w_f211_working_capital_turnover_velocity_calc109_252d_jerk_v109_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 59.5537)).rolling(4).var()).rolling(20).min()) * 0.504635).diff(2).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc109_252d_jerk_v109_signal'] = f211w_f211_working_capital_turnover_velocity_calc109_252d_jerk_v109_signal

def f211w_f211_working_capital_turnover_velocity_calc110_42d_jerk_v110_signal(workingcapital, revenue):
    res = (((((workingcapital * 26.3295 - revenue).rolling(14).min()).diff(19)) * 0.400556).diff(7).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc110_42d_jerk_v110_signal'] = f211w_f211_working_capital_turnover_velocity_calc110_42d_jerk_v110_signal

def f211w_f211_working_capital_turnover_velocity_calc111_63d_jerk_v111_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(8) / (revenue.shift(2) + 99.7082)).rolling(4).max()).rolling(23).mean()).rolling(15).min()).rolling(13).var()) * 0.523763).diff(7).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc111_63d_jerk_v111_signal'] = f211w_f211_working_capital_turnover_velocity_calc111_63d_jerk_v111_signal

def f211w_f211_working_capital_turnover_velocity_calc112_21d_jerk_v112_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(16).std()).rolling(28).mean()).rolling(8).std()).diff(12)) * 0.033723).diff(5).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc112_21d_jerk_v112_signal'] = f211w_f211_working_capital_turnover_velocity_calc112_21d_jerk_v112_signal

def f211w_f211_working_capital_turnover_velocity_calc113_5d_jerk_v113_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(20) / (revenue.shift(3) + 73.9842)).pct_change(4)).rolling(16).var()).rolling(2).min()).rolling(8).var()) * 0.248187).diff(18).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc113_5d_jerk_v113_signal'] = f211w_f211_working_capital_turnover_velocity_calc113_5d_jerk_v113_signal

def f211w_f211_working_capital_turnover_velocity_calc114_10d_jerk_v114_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(20) / revenue.pct_change(5)).diff(1)).rolling(20).min()).diff(17)).rolling(10).mean()) * 0.745348).diff(6).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc114_10d_jerk_v114_signal'] = f211w_f211_working_capital_turnover_velocity_calc114_10d_jerk_v114_signal

def f211w_f211_working_capital_turnover_velocity_calc115_21d_jerk_v115_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 20.1495)).diff(9)).diff(12)).pct_change(4)) * 0.692596).diff(1).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc115_21d_jerk_v115_signal'] = f211w_f211_working_capital_turnover_velocity_calc115_21d_jerk_v115_signal

def f211w_f211_working_capital_turnover_velocity_calc116_252d_jerk_v116_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(4).max()).rolling(8).std()).rolling(16).max()).rolling(24).max()) * 0.388793).diff(1).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc116_252d_jerk_v116_signal'] = f211w_f211_working_capital_turnover_velocity_calc116_252d_jerk_v116_signal

def f211w_f211_working_capital_turnover_velocity_calc117_10d_jerk_v117_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(16) / (revenue.shift(7) + 92.2348)).rolling(13).var()).diff(10)).rolling(18).std()).rolling(27).var()) * 0.308829).diff(2).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc117_10d_jerk_v117_signal'] = f211w_f211_working_capital_turnover_velocity_calc117_10d_jerk_v117_signal

def f211w_f211_working_capital_turnover_velocity_calc118_42d_jerk_v118_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 89.0512)).rolling(23).min()).rolling(4).std()).diff(13)) * 0.808561).diff(17).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc118_42d_jerk_v118_signal'] = f211w_f211_working_capital_turnover_velocity_calc118_42d_jerk_v118_signal

def f211w_f211_working_capital_turnover_velocity_calc119_252d_jerk_v119_signal(workingcapital, revenue):
    res = (((((((workingcapital.diff(8) / (revenue.shift(10) + 62.5899)).rolling(16).var()).rolling(6).max()).rolling(22).std()).rolling(20).std()) * 0.232879).diff(18).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc119_252d_jerk_v119_signal'] = f211w_f211_working_capital_turnover_velocity_calc119_252d_jerk_v119_signal

def f211w_f211_working_capital_turnover_velocity_calc120_252d_jerk_v120_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(14) / revenue.pct_change(5)).rolling(12).std()).rolling(19).mean()).rolling(25).max()).rolling(7).mean()) * 0.684761).diff(11).diff(5).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc120_252d_jerk_v120_signal'] = f211w_f211_working_capital_turnover_velocity_calc120_252d_jerk_v120_signal

def f211w_f211_working_capital_turnover_velocity_calc121_126d_jerk_v121_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(10) / revenue.pct_change(15)).diff(9)).rolling(26).std()).rolling(5).std()).rolling(7).std()) * 0.322314).diff(1).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc121_126d_jerk_v121_signal'] = f211w_f211_working_capital_turnover_velocity_calc121_126d_jerk_v121_signal

def f211w_f211_working_capital_turnover_velocity_calc122_63d_jerk_v122_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(8) / revenue.pct_change(8)).rolling(4).var()).diff(16)) * 0.565702).diff(5).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc122_63d_jerk_v122_signal'] = f211w_f211_working_capital_turnover_velocity_calc122_63d_jerk_v122_signal

def f211w_f211_working_capital_turnover_velocity_calc123_252d_jerk_v123_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(8).std()).rolling(3).std()) * 0.707779).diff(14).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc123_252d_jerk_v123_signal'] = f211w_f211_working_capital_turnover_velocity_calc123_252d_jerk_v123_signal

def f211w_f211_working_capital_turnover_velocity_calc124_21d_jerk_v124_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(24).min()).rolling(29).var()).rolling(30).min()).rolling(15).std()) * 0.228103).diff(13).diff(2).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc124_21d_jerk_v124_signal'] = f211w_f211_working_capital_turnover_velocity_calc124_21d_jerk_v124_signal

def f211w_f211_working_capital_turnover_velocity_calc125_63d_jerk_v125_signal(workingcapital, revenue):
    res = (((((((workingcapital * 73.5596 - revenue).rolling(22).max()).diff(2)).rolling(5).max()).rolling(16).min()) * 0.382767).diff(2).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc125_63d_jerk_v125_signal'] = f211w_f211_working_capital_turnover_velocity_calc125_63d_jerk_v125_signal

def f211w_f211_working_capital_turnover_velocity_calc126_63d_jerk_v126_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(13) / revenue.pct_change(17)).rolling(11).std()).rolling(14).min()) * 0.974154).diff(10).diff(10).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc126_63d_jerk_v126_signal'] = f211w_f211_working_capital_turnover_velocity_calc126_63d_jerk_v126_signal

def f211w_f211_working_capital_turnover_velocity_calc127_42d_jerk_v127_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(5) / revenue.pct_change(15)).rolling(25).mean()).rolling(5).max()).rolling(26).std()) * 0.298531).diff(19).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc127_42d_jerk_v127_signal'] = f211w_f211_working_capital_turnover_velocity_calc127_42d_jerk_v127_signal

def f211w_f211_working_capital_turnover_velocity_calc128_10d_jerk_v128_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(15) / revenue.pct_change(19)).rolling(4).min()).rolling(12).var()) * 0.326992).diff(6).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc128_10d_jerk_v128_signal'] = f211w_f211_working_capital_turnover_velocity_calc128_10d_jerk_v128_signal

def f211w_f211_working_capital_turnover_velocity_calc129_5d_jerk_v129_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(17) / revenue.pct_change(13)).rolling(7).max()).rolling(19).min()).rolling(3).min()).pct_change(6)) * 0.45041).diff(11).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc129_5d_jerk_v129_signal'] = f211w_f211_working_capital_turnover_velocity_calc129_5d_jerk_v129_signal

def f211w_f211_working_capital_turnover_velocity_calc130_252d_jerk_v130_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(5) / (revenue.shift(3) + 65.9871)).diff(15)).rolling(22).var()).rolling(5).std()) * 0.157088).diff(5).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc130_252d_jerk_v130_signal'] = f211w_f211_working_capital_turnover_velocity_calc130_252d_jerk_v130_signal

def f211w_f211_working_capital_turnover_velocity_calc131_5d_jerk_v131_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 62.2938)).rolling(9).min()).rolling(20).std()).diff(16)).rolling(15).min()) * 0.258049).diff(15).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc131_5d_jerk_v131_signal'] = f211w_f211_working_capital_turnover_velocity_calc131_5d_jerk_v131_signal

def f211w_f211_working_capital_turnover_velocity_calc132_63d_jerk_v132_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 60.0502)).rolling(6).std()).rolling(22).mean()) * 0.249819).diff(12).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc132_63d_jerk_v132_signal'] = f211w_f211_working_capital_turnover_velocity_calc132_63d_jerk_v132_signal

def f211w_f211_working_capital_turnover_velocity_calc133_10d_jerk_v133_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 85.3975)).rolling(7).min()).rolling(23).std()) * 0.663657).diff(10).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc133_10d_jerk_v133_signal'] = f211w_f211_working_capital_turnover_velocity_calc133_10d_jerk_v133_signal

def f211w_f211_working_capital_turnover_velocity_calc134_126d_jerk_v134_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(18) / (revenue.shift(3) + 69.1822)).rolling(26).mean()).rolling(12).var()) * 0.59307).diff(12).diff(13).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc134_126d_jerk_v134_signal'] = f211w_f211_working_capital_turnover_velocity_calc134_126d_jerk_v134_signal

def f211w_f211_working_capital_turnover_velocity_calc135_252d_jerk_v135_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 6.8599)).diff(9)).rolling(18).var()) * 0.428777).diff(14).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc135_252d_jerk_v135_signal'] = f211w_f211_working_capital_turnover_velocity_calc135_252d_jerk_v135_signal

def f211w_f211_working_capital_turnover_velocity_calc136_10d_jerk_v136_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(20)).pct_change(10)).rolling(21).min()).pct_change(11)) * 0.609813).diff(9).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc136_10d_jerk_v136_signal'] = f211w_f211_working_capital_turnover_velocity_calc136_10d_jerk_v136_signal

def f211w_f211_working_capital_turnover_velocity_calc137_63d_jerk_v137_signal(workingcapital, revenue):
    res = (((((((workingcapital * 99.5029 - revenue).diff(16)).rolling(27).min()).rolling(30).std()).rolling(9).max()) * 0.356776).diff(10).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc137_63d_jerk_v137_signal'] = f211w_f211_working_capital_turnover_velocity_calc137_63d_jerk_v137_signal

def f211w_f211_working_capital_turnover_velocity_calc138_5d_jerk_v138_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).var()).rolling(27).max()) * 0.465588).diff(7).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc138_5d_jerk_v138_signal'] = f211w_f211_working_capital_turnover_velocity_calc138_5d_jerk_v138_signal

def f211w_f211_working_capital_turnover_velocity_calc139_126d_jerk_v139_signal(workingcapital, revenue):
    res = ((((((workingcapital * 20.1986 - revenue).pct_change(1)).rolling(23).mean()).rolling(12).var()) * 0.285994).diff(13).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc139_126d_jerk_v139_signal'] = f211w_f211_working_capital_turnover_velocity_calc139_126d_jerk_v139_signal

def f211w_f211_working_capital_turnover_velocity_calc140_63d_jerk_v140_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(5)).rolling(6).min()) * 0.825402).diff(15).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc140_63d_jerk_v140_signal'] = f211w_f211_working_capital_turnover_velocity_calc140_63d_jerk_v140_signal

def f211w_f211_working_capital_turnover_velocity_calc141_21d_jerk_v141_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(10) / revenue.pct_change(19)).rolling(19).var()).rolling(2).max()).rolling(20).std()).diff(11)) * 0.807883).diff(12).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc141_21d_jerk_v141_signal'] = f211w_f211_working_capital_turnover_velocity_calc141_21d_jerk_v141_signal

def f211w_f211_working_capital_turnover_velocity_calc142_10d_jerk_v142_signal(workingcapital, revenue):
    res = ((((((workingcapital * 28.118 - revenue).rolling(21).std()).rolling(29).mean()).pct_change(10)) * 0.04055).diff(11).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc142_10d_jerk_v142_signal'] = f211w_f211_working_capital_turnover_velocity_calc142_10d_jerk_v142_signal

def f211w_f211_working_capital_turnover_velocity_calc143_21d_jerk_v143_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 41.4456)).rolling(7).var()).rolling(13).mean()).pct_change(2)).pct_change(7)) * 0.497113).diff(3).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc143_21d_jerk_v143_signal'] = f211w_f211_working_capital_turnover_velocity_calc143_21d_jerk_v143_signal

def f211w_f211_working_capital_turnover_velocity_calc144_63d_jerk_v144_signal(workingcapital, revenue):
    res = (((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(17)).rolling(26).var()).rolling(6).var()).pct_change(4)) * 0.48301).diff(17).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc144_63d_jerk_v144_signal'] = f211w_f211_working_capital_turnover_velocity_calc144_63d_jerk_v144_signal

def f211w_f211_working_capital_turnover_velocity_calc145_10d_jerk_v145_signal(workingcapital, revenue):
    res = (((((((workingcapital / (revenue + 72.4846)).pct_change(20)).pct_change(3)).rolling(16).var()).rolling(5).mean()) * 0.460181).diff(17).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc145_10d_jerk_v145_signal'] = f211w_f211_working_capital_turnover_velocity_calc145_10d_jerk_v145_signal

def f211w_f211_working_capital_turnover_velocity_calc146_5d_jerk_v146_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(7) / (revenue.shift(6) + 57.7982)).rolling(12).max()).pct_change(15)).diff(4)) * 0.3159).diff(9).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc146_5d_jerk_v146_signal'] = f211w_f211_working_capital_turnover_velocity_calc146_5d_jerk_v146_signal

def f211w_f211_working_capital_turnover_velocity_calc147_10d_jerk_v147_signal(workingcapital, revenue):
    res = (((((((revenue / (workingcapital + 27.4363)).rolling(19).var()).rolling(10).var()).rolling(24).std()).pct_change(10)) * 0.024952).diff(19).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc147_10d_jerk_v147_signal'] = f211w_f211_working_capital_turnover_velocity_calc147_10d_jerk_v147_signal

def f211w_f211_working_capital_turnover_velocity_calc148_10d_jerk_v148_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 7.2172)).rolling(30).min()).diff(2)) * 0.610998).diff(4).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc148_10d_jerk_v148_signal'] = f211w_f211_working_capital_turnover_velocity_calc148_10d_jerk_v148_signal

def f211w_f211_working_capital_turnover_velocity_calc149_5d_jerk_v149_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(20) / (revenue.shift(10) + 8.7033)).rolling(28).var()).rolling(24).std()).pct_change(18)) * 0.394078).diff(3).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc149_5d_jerk_v149_signal'] = f211w_f211_working_capital_turnover_velocity_calc149_5d_jerk_v149_signal

def f211w_f211_working_capital_turnover_velocity_calc150_63d_jerk_v150_signal(workingcapital, revenue):
    res = (((((((workingcapital.pct_change(15) / revenue.pct_change(10)).diff(15)).rolling(9).min()).rolling(6).std()).pct_change(20)) * 0.806594).diff(9).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc150_63d_jerk_v150_signal'] = f211w_f211_working_capital_turnover_velocity_calc150_63d_jerk_v150_signal


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
