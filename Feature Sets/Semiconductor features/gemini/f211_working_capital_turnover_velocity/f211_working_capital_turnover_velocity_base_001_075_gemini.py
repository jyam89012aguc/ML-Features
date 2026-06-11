import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f211w_f211_working_capital_turnover_velocity_calc001_126d_base_v001_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(5) / revenue.pct_change(4)).rolling(4).max()).rolling(15).max()).rolling(2).mean()).rolling(8).mean()) * 0.736719)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc001_126d_base_v001_signal'] = f211w_f211_working_capital_turnover_velocity_calc001_126d_base_v001_signal

def f211w_f211_working_capital_turnover_velocity_calc002_10d_base_v002_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(27).var()).pct_change(1)).pct_change(6)).diff(14)) * 0.036005)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc002_10d_base_v002_signal'] = f211w_f211_working_capital_turnover_velocity_calc002_10d_base_v002_signal

def f211w_f211_working_capital_turnover_velocity_calc003_21d_base_v003_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 27.8593)).pct_change(12)).rolling(10).max()).pct_change(2)) * 0.221007)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc003_21d_base_v003_signal'] = f211w_f211_working_capital_turnover_velocity_calc003_21d_base_v003_signal

def f211w_f211_working_capital_turnover_velocity_calc004_126d_base_v004_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(18) / revenue.pct_change(10)).pct_change(12)).rolling(8).max()).diff(3)).rolling(23).mean()) * 0.13233)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc004_126d_base_v004_signal'] = f211w_f211_working_capital_turnover_velocity_calc004_126d_base_v004_signal

def f211w_f211_working_capital_turnover_velocity_calc005_10d_base_v005_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(12)).rolling(13).std()).rolling(8).var()).diff(9)) * 0.975517)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc005_10d_base_v005_signal'] = f211w_f211_working_capital_turnover_velocity_calc005_10d_base_v005_signal

def f211w_f211_working_capital_turnover_velocity_calc006_126d_base_v006_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 93.6718)).rolling(10).min()).diff(18)).rolling(23).std()) * 0.645075)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc006_126d_base_v006_signal'] = f211w_f211_working_capital_turnover_velocity_calc006_126d_base_v006_signal

def f211w_f211_working_capital_turnover_velocity_calc007_21d_base_v007_signal(workingcapital, revenue):
    res = ((((workingcapital.diff(8) / (revenue.shift(1) + 84.3009)).rolling(20).std()).diff(11)) * 0.77048)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc007_21d_base_v007_signal'] = f211w_f211_working_capital_turnover_velocity_calc007_21d_base_v007_signal

def f211w_f211_working_capital_turnover_velocity_calc008_10d_base_v008_signal(workingcapital, revenue):
    res = ((((((revenue / (workingcapital + 65.5783)).rolling(19).max()).rolling(25).var()).rolling(15).max()).rolling(14).max()) * 0.397719)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc008_10d_base_v008_signal'] = f211w_f211_working_capital_turnover_velocity_calc008_10d_base_v008_signal

def f211w_f211_working_capital_turnover_velocity_calc009_21d_base_v009_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 22.0101)).diff(6)).pct_change(14)) * 0.987587)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc009_21d_base_v009_signal'] = f211w_f211_working_capital_turnover_velocity_calc009_21d_base_v009_signal

def f211w_f211_working_capital_turnover_velocity_calc010_63d_base_v010_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 6.4464)).diff(4)).diff(18)).pct_change(9)).pct_change(11)) * 0.383987)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc010_63d_base_v010_signal'] = f211w_f211_working_capital_turnover_velocity_calc010_63d_base_v010_signal

def f211w_f211_working_capital_turnover_velocity_calc011_5d_base_v011_signal(workingcapital, revenue):
    res = ((((workingcapital * 29.4207 - revenue).pct_change(10)).pct_change(17)) * 0.164995)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc011_5d_base_v011_signal'] = f211w_f211_working_capital_turnover_velocity_calc011_5d_base_v011_signal

def f211w_f211_working_capital_turnover_velocity_calc012_63d_base_v012_signal(workingcapital, revenue):
    res = (((((workingcapital * 19.9712 - revenue).rolling(2).min()).rolling(13).mean()).pct_change(10)) * 0.376436)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc012_63d_base_v012_signal'] = f211w_f211_working_capital_turnover_velocity_calc012_63d_base_v012_signal

def f211w_f211_working_capital_turnover_velocity_calc013_10d_base_v013_signal(workingcapital, revenue):
    res = ((((workingcapital * 5.8867 - revenue).rolling(23).std()).rolling(19).min()) * 0.870449)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc013_10d_base_v013_signal'] = f211w_f211_working_capital_turnover_velocity_calc013_10d_base_v013_signal

def f211w_f211_working_capital_turnover_velocity_calc014_10d_base_v014_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(18) / revenue.pct_change(7)).rolling(23).min()).diff(12)).rolling(30).min()) * 0.864984)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc014_10d_base_v014_signal'] = f211w_f211_working_capital_turnover_velocity_calc014_10d_base_v014_signal

def f211w_f211_working_capital_turnover_velocity_calc015_63d_base_v015_signal(workingcapital, revenue):
    res = ((((workingcapital * 45.2035 - revenue).rolling(9).max()).rolling(4).mean()) * 0.252948)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc015_63d_base_v015_signal'] = f211w_f211_working_capital_turnover_velocity_calc015_63d_base_v015_signal

def f211w_f211_working_capital_turnover_velocity_calc016_126d_base_v016_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 63.1472)).diff(16)).rolling(19).std()).rolling(25).std()) * 0.234363)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc016_126d_base_v016_signal'] = f211w_f211_working_capital_turnover_velocity_calc016_126d_base_v016_signal

def f211w_f211_working_capital_turnover_velocity_calc017_63d_base_v017_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 57.6635)).rolling(13).min()).rolling(15).min()).rolling(29).min()).diff(2)) * 0.248137)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc017_63d_base_v017_signal'] = f211w_f211_working_capital_turnover_velocity_calc017_63d_base_v017_signal

def f211w_f211_working_capital_turnover_velocity_calc018_126d_base_v018_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 65.3802)).rolling(19).std()).rolling(6).min()) * 0.643256)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc018_126d_base_v018_signal'] = f211w_f211_working_capital_turnover_velocity_calc018_126d_base_v018_signal

def f211w_f211_working_capital_turnover_velocity_calc019_42d_base_v019_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 18.4305)).rolling(28).max()).rolling(4).mean()).pct_change(8)).rolling(15).std()) * 0.463376)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc019_42d_base_v019_signal'] = f211w_f211_working_capital_turnover_velocity_calc019_42d_base_v019_signal

def f211w_f211_working_capital_turnover_velocity_calc020_42d_base_v020_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(15)).rolling(15).var()).diff(18)) * 0.857357)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc020_42d_base_v020_signal'] = f211w_f211_working_capital_turnover_velocity_calc020_42d_base_v020_signal

def f211w_f211_working_capital_turnover_velocity_calc021_126d_base_v021_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(2) / revenue.pct_change(19)).rolling(25).mean()).rolling(3).var()).rolling(20).mean()).rolling(18).min()) * 0.161701)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc021_126d_base_v021_signal'] = f211w_f211_working_capital_turnover_velocity_calc021_126d_base_v021_signal

def f211w_f211_working_capital_turnover_velocity_calc022_252d_base_v022_signal(workingcapital, revenue):
    res = ((((workingcapital * 53.1595 - revenue).diff(8)).rolling(5).min()) * 0.065742)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc022_252d_base_v022_signal'] = f211w_f211_working_capital_turnover_velocity_calc022_252d_base_v022_signal

def f211w_f211_working_capital_turnover_velocity_calc023_63d_base_v023_signal(workingcapital, revenue):
    res = ((((((workingcapital * 24.6969 - revenue).rolling(10).var()).rolling(23).std()).diff(11)).rolling(10).std()) * 0.592629)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc023_63d_base_v023_signal'] = f211w_f211_working_capital_turnover_velocity_calc023_63d_base_v023_signal

def f211w_f211_working_capital_turnover_velocity_calc024_42d_base_v024_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).max()).rolling(19).mean()).rolling(18).std()).rolling(6).var()) * 0.642591)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc024_42d_base_v024_signal'] = f211w_f211_working_capital_turnover_velocity_calc024_42d_base_v024_signal

def f211w_f211_working_capital_turnover_velocity_calc025_21d_base_v025_signal(workingcapital, revenue):
    res = ((((((workingcapital * 88.0983 - revenue).rolling(21).var()).pct_change(17)).rolling(23).mean()).pct_change(18)) * 0.871685)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc025_21d_base_v025_signal'] = f211w_f211_working_capital_turnover_velocity_calc025_21d_base_v025_signal

def f211w_f211_working_capital_turnover_velocity_calc026_21d_base_v026_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(4) / revenue.pct_change(4)).rolling(10).std()).rolling(21).var()).rolling(24).std()).rolling(8).var()) * 0.111515)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc026_21d_base_v026_signal'] = f211w_f211_working_capital_turnover_velocity_calc026_21d_base_v026_signal

def f211w_f211_working_capital_turnover_velocity_calc027_126d_base_v027_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(2) / revenue.pct_change(3)).pct_change(9)).rolling(2).mean()).rolling(26).var()) * 0.268704)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc027_126d_base_v027_signal'] = f211w_f211_working_capital_turnover_velocity_calc027_126d_base_v027_signal

def f211w_f211_working_capital_turnover_velocity_calc028_10d_base_v028_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 63.7476)).rolling(30).mean()).diff(5)) * 0.266716)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc028_10d_base_v028_signal'] = f211w_f211_working_capital_turnover_velocity_calc028_10d_base_v028_signal

def f211w_f211_working_capital_turnover_velocity_calc029_63d_base_v029_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 3.6992)).rolling(30).var()).pct_change(2)).rolling(8).var()) * 0.371832)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc029_63d_base_v029_signal'] = f211w_f211_working_capital_turnover_velocity_calc029_63d_base_v029_signal

def f211w_f211_working_capital_turnover_velocity_calc030_126d_base_v030_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 25.028)).pct_change(6)).rolling(2).min()) * 0.110738)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc030_126d_base_v030_signal'] = f211w_f211_working_capital_turnover_velocity_calc030_126d_base_v030_signal

def f211w_f211_working_capital_turnover_velocity_calc031_10d_base_v031_signal(workingcapital, revenue):
    res = ((((workingcapital.pct_change(9) / revenue.pct_change(6)).rolling(29).min()).rolling(29).mean()) * 0.335542)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc031_10d_base_v031_signal'] = f211w_f211_working_capital_turnover_velocity_calc031_10d_base_v031_signal

def f211w_f211_working_capital_turnover_velocity_calc032_42d_base_v032_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 22.3211)).diff(7)).rolling(12).min()) * 0.810255)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc032_42d_base_v032_signal'] = f211w_f211_working_capital_turnover_velocity_calc032_42d_base_v032_signal

def f211w_f211_working_capital_turnover_velocity_calc033_21d_base_v033_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(17) / revenue.pct_change(13)).rolling(2).var()).rolling(30).mean()).rolling(7).var()).rolling(10).max()) * 0.957551)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc033_21d_base_v033_signal'] = f211w_f211_working_capital_turnover_velocity_calc033_21d_base_v033_signal

def f211w_f211_working_capital_turnover_velocity_calc034_5d_base_v034_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 10.9294)).rolling(8).max()).rolling(3).var()).diff(14)) * 0.435872)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc034_5d_base_v034_signal'] = f211w_f211_working_capital_turnover_velocity_calc034_5d_base_v034_signal

def f211w_f211_working_capital_turnover_velocity_calc035_5d_base_v035_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(14) / revenue.pct_change(3)).rolling(12).max()).diff(4)).diff(10)) * 0.800381)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc035_5d_base_v035_signal'] = f211w_f211_working_capital_turnover_velocity_calc035_5d_base_v035_signal

def f211w_f211_working_capital_turnover_velocity_calc036_63d_base_v036_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 30.9975)).diff(13)).diff(6)).rolling(20).max()) * 0.410225)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc036_63d_base_v036_signal'] = f211w_f211_working_capital_turnover_velocity_calc036_63d_base_v036_signal

def f211w_f211_working_capital_turnover_velocity_calc037_21d_base_v037_signal(workingcapital, revenue):
    res = ((((((workingcapital * 40.6669 - revenue).diff(11)).rolling(16).min()).rolling(23).min()).rolling(18).std()) * 0.827051)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc037_21d_base_v037_signal'] = f211w_f211_working_capital_turnover_velocity_calc037_21d_base_v037_signal

def f211w_f211_working_capital_turnover_velocity_calc038_42d_base_v038_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(10) / revenue.pct_change(17)).rolling(12).max()).rolling(28).mean()).pct_change(8)).diff(10)) * 0.950635)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc038_42d_base_v038_signal'] = f211w_f211_working_capital_turnover_velocity_calc038_42d_base_v038_signal

def f211w_f211_working_capital_turnover_velocity_calc039_10d_base_v039_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 80.6756)).rolling(30).min()).diff(19)).rolling(24).std()) * 0.154407)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc039_10d_base_v039_signal'] = f211w_f211_working_capital_turnover_velocity_calc039_10d_base_v039_signal

def f211w_f211_working_capital_turnover_velocity_calc040_126d_base_v040_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 38.4594)).pct_change(17)).rolling(3).min()) * 0.40166)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc040_126d_base_v040_signal'] = f211w_f211_working_capital_turnover_velocity_calc040_126d_base_v040_signal

def f211w_f211_working_capital_turnover_velocity_calc041_63d_base_v041_signal(workingcapital, revenue):
    res = ((((((workingcapital * 24.9949 - revenue).rolling(26).var()).rolling(21).min()).pct_change(17)).rolling(28).min()) * 0.84137)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc041_63d_base_v041_signal'] = f211w_f211_working_capital_turnover_velocity_calc041_63d_base_v041_signal

def f211w_f211_working_capital_turnover_velocity_calc042_63d_base_v042_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(9) / revenue.pct_change(8)).pct_change(17)).rolling(22).min()).rolling(10).std()) * 0.165975)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc042_63d_base_v042_signal'] = f211w_f211_working_capital_turnover_velocity_calc042_63d_base_v042_signal

def f211w_f211_working_capital_turnover_velocity_calc043_42d_base_v043_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 7.8406)).rolling(9).std()).rolling(24).min()) * 0.290014)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc043_42d_base_v043_signal'] = f211w_f211_working_capital_turnover_velocity_calc043_42d_base_v043_signal

def f211w_f211_working_capital_turnover_velocity_calc044_10d_base_v044_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(28).std()).rolling(14).min()) * 0.072944)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc044_10d_base_v044_signal'] = f211w_f211_working_capital_turnover_velocity_calc044_10d_base_v044_signal

def f211w_f211_working_capital_turnover_velocity_calc045_252d_base_v045_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(19) / (revenue.shift(7) + 58.4495)).pct_change(13)).pct_change(14)).rolling(25).max()) * 0.691613)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc045_252d_base_v045_signal'] = f211w_f211_working_capital_turnover_velocity_calc045_252d_base_v045_signal

def f211w_f211_working_capital_turnover_velocity_calc046_126d_base_v046_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(14).mean()).rolling(23).var()).diff(13)) * 0.601188)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc046_126d_base_v046_signal'] = f211w_f211_working_capital_turnover_velocity_calc046_126d_base_v046_signal

def f211w_f211_working_capital_turnover_velocity_calc047_126d_base_v047_signal(workingcapital, revenue):
    res = ((((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(23).max()).rolling(4).mean()).diff(14)).rolling(29).std()) * 0.468042)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc047_126d_base_v047_signal'] = f211w_f211_working_capital_turnover_velocity_calc047_126d_base_v047_signal

def f211w_f211_working_capital_turnover_velocity_calc048_42d_base_v048_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(11) / (revenue.shift(4) + 18.2547)).rolling(26).var()).pct_change(14)).rolling(28).var()) * 0.264953)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc048_42d_base_v048_signal'] = f211w_f211_working_capital_turnover_velocity_calc048_42d_base_v048_signal

def f211w_f211_working_capital_turnover_velocity_calc049_5d_base_v049_signal(workingcapital, revenue):
    res = ((((workingcapital.pct_change(8) / revenue.pct_change(3)).pct_change(1)).rolling(8).std()) * 0.744044)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc049_5d_base_v049_signal'] = f211w_f211_working_capital_turnover_velocity_calc049_5d_base_v049_signal

def f211w_f211_working_capital_turnover_velocity_calc050_252d_base_v050_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 2.136)).diff(9)).pct_change(12)).rolling(21).std()) * 0.159335)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc050_252d_base_v050_signal'] = f211w_f211_working_capital_turnover_velocity_calc050_252d_base_v050_signal

def f211w_f211_working_capital_turnover_velocity_calc051_63d_base_v051_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 96.3771)).rolling(23).max()).rolling(14).min()).diff(7)) * 0.71399)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc051_63d_base_v051_signal'] = f211w_f211_working_capital_turnover_velocity_calc051_63d_base_v051_signal

def f211w_f211_working_capital_turnover_velocity_calc052_5d_base_v052_signal(workingcapital, revenue):
    res = ((((((workingcapital / (revenue + 59.2506)).pct_change(2)).rolling(19).var()).rolling(23).min()).rolling(4).var()) * 0.82396)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc052_5d_base_v052_signal'] = f211w_f211_working_capital_turnover_velocity_calc052_5d_base_v052_signal

def f211w_f211_working_capital_turnover_velocity_calc053_63d_base_v053_signal(workingcapital, revenue):
    res = ((((((workingcapital.diff(14) / (revenue.shift(8) + 64.7896)).pct_change(15)).diff(5)).rolling(7).min()).diff(17)) * 0.022399)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc053_63d_base_v053_signal'] = f211w_f211_working_capital_turnover_velocity_calc053_63d_base_v053_signal

def f211w_f211_working_capital_turnover_velocity_calc054_126d_base_v054_signal(workingcapital, revenue):
    res = ((((((workingcapital.pct_change(15) / revenue.pct_change(14)).rolling(12).var()).pct_change(8)).pct_change(3)).rolling(30).var()) * 0.802035)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc054_126d_base_v054_signal'] = f211w_f211_working_capital_turnover_velocity_calc054_126d_base_v054_signal

def f211w_f211_working_capital_turnover_velocity_calc055_42d_base_v055_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).std()).rolling(13).std()).pct_change(9)) * 0.465414)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc055_42d_base_v055_signal'] = f211w_f211_working_capital_turnover_velocity_calc055_42d_base_v055_signal

def f211w_f211_working_capital_turnover_velocity_calc056_21d_base_v056_signal(workingcapital, revenue):
    res = ((((revenue / (workingcapital + 28.0379)).rolling(25).std()).rolling(17).min()) * 0.594232)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc056_21d_base_v056_signal'] = f211w_f211_working_capital_turnover_velocity_calc056_21d_base_v056_signal

def f211w_f211_working_capital_turnover_velocity_calc057_63d_base_v057_signal(workingcapital, revenue):
    res = ((((workingcapital.diff(16) / (revenue.shift(8) + 75.8406)).rolling(24).min()).rolling(11).std()) * 0.686797)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc057_63d_base_v057_signal'] = f211w_f211_working_capital_turnover_velocity_calc057_63d_base_v057_signal

def f211w_f211_working_capital_turnover_velocity_calc058_126d_base_v058_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(17) / (revenue.shift(6) + 58.1974)).diff(15)).rolling(11).var()).rolling(9).var()) * 0.473795)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc058_126d_base_v058_signal'] = f211w_f211_working_capital_turnover_velocity_calc058_126d_base_v058_signal

def f211w_f211_working_capital_turnover_velocity_calc059_5d_base_v059_signal(workingcapital, revenue):
    res = (((((workingcapital.pct_change(7) / revenue.pct_change(7)).rolling(25).var()).rolling(26).max()).rolling(21).max()) * 0.319237)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc059_5d_base_v059_signal'] = f211w_f211_working_capital_turnover_velocity_calc059_5d_base_v059_signal

def f211w_f211_working_capital_turnover_velocity_calc060_21d_base_v060_signal(workingcapital, revenue):
    res = ((((workingcapital.diff(10) / (revenue.shift(4) + 98.053)).diff(18)).rolling(10).std()) * 0.825976)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc060_21d_base_v060_signal'] = f211w_f211_working_capital_turnover_velocity_calc060_21d_base_v060_signal

def f211w_f211_working_capital_turnover_velocity_calc061_5d_base_v061_signal(workingcapital, revenue):
    res = (((((workingcapital * 97.4321 - revenue).rolling(17).min()).rolling(12).min()).rolling(3).std()) * 0.552292)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc061_5d_base_v061_signal'] = f211w_f211_working_capital_turnover_velocity_calc061_5d_base_v061_signal

def f211w_f211_working_capital_turnover_velocity_calc062_21d_base_v062_signal(workingcapital, revenue):
    res = ((((((workingcapital * 94.1123 - revenue).diff(2)).rolling(6).std()).pct_change(19)).rolling(4).var()) * 0.478175)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc062_21d_base_v062_signal'] = f211w_f211_working_capital_turnover_velocity_calc062_21d_base_v062_signal

def f211w_f211_working_capital_turnover_velocity_calc063_10d_base_v063_signal(workingcapital, revenue):
    res = (((((workingcapital * 11.9333 - revenue).rolling(16).min()).rolling(29).var()).rolling(15).max()) * 0.759155)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc063_10d_base_v063_signal'] = f211w_f211_working_capital_turnover_velocity_calc063_10d_base_v063_signal

def f211w_f211_working_capital_turnover_velocity_calc064_21d_base_v064_signal(workingcapital, revenue):
    res = ((((workingcapital.pct_change(7) / revenue.pct_change(9)).rolling(9).std()).rolling(19).std()) * 0.069026)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc064_21d_base_v064_signal'] = f211w_f211_working_capital_turnover_velocity_calc064_21d_base_v064_signal

def f211w_f211_working_capital_turnover_velocity_calc065_5d_base_v065_signal(workingcapital, revenue):
    res = (((((revenue / (workingcapital + 15.7376)).diff(10)).diff(15)).rolling(23).mean()) * 0.410347)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc065_5d_base_v065_signal'] = f211w_f211_working_capital_turnover_velocity_calc065_5d_base_v065_signal

def f211w_f211_working_capital_turnover_velocity_calc066_10d_base_v066_signal(workingcapital, revenue):
    res = ((((workingcapital * 92.3987 - revenue).diff(5)).rolling(28).var()) * 0.782071)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc066_10d_base_v066_signal'] = f211w_f211_working_capital_turnover_velocity_calc066_10d_base_v066_signal

def f211w_f211_working_capital_turnover_velocity_calc067_10d_base_v067_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(24).min()).rolling(24).var()) * 0.172604)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc067_10d_base_v067_signal'] = f211w_f211_working_capital_turnover_velocity_calc067_10d_base_v067_signal

def f211w_f211_working_capital_turnover_velocity_calc068_42d_base_v068_signal(workingcapital, revenue):
    res = (((((workingcapital / (revenue + 94.2734)).diff(11)).rolling(10).max()).rolling(4).mean()) * 0.500463)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc068_42d_base_v068_signal'] = f211w_f211_working_capital_turnover_velocity_calc068_42d_base_v068_signal

def f211w_f211_working_capital_turnover_velocity_calc069_10d_base_v069_signal(workingcapital, revenue):
    res = ((((workingcapital * 96.1949 - revenue).pct_change(6)).rolling(18).min()) * 0.829239)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc069_10d_base_v069_signal'] = f211w_f211_working_capital_turnover_velocity_calc069_10d_base_v069_signal

def f211w_f211_working_capital_turnover_velocity_calc070_126d_base_v070_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(12).min()).rolling(23).var()).rolling(29).mean()) * 0.282593)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc070_126d_base_v070_signal'] = f211w_f211_working_capital_turnover_velocity_calc070_126d_base_v070_signal

def f211w_f211_working_capital_turnover_velocity_calc071_10d_base_v071_signal(workingcapital, revenue):
    res = ((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).var()).rolling(5).var()) * 0.6898)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc071_10d_base_v071_signal'] = f211w_f211_working_capital_turnover_velocity_calc071_10d_base_v071_signal

def f211w_f211_working_capital_turnover_velocity_calc072_252d_base_v072_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 40.4771)).rolling(13).max()).rolling(26).max()) * 0.514304)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc072_252d_base_v072_signal'] = f211w_f211_working_capital_turnover_velocity_calc072_252d_base_v072_signal

def f211w_f211_working_capital_turnover_velocity_calc073_42d_base_v073_signal(workingcapital, revenue):
    res = (((((workingcapital.diff(7) / (revenue.shift(5) + 62.5783)).diff(16)).rolling(2).mean()).diff(20)) * 0.754791)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc073_42d_base_v073_signal'] = f211w_f211_working_capital_turnover_velocity_calc073_42d_base_v073_signal

def f211w_f211_working_capital_turnover_velocity_calc074_252d_base_v074_signal(workingcapital, revenue):
    res = ((((workingcapital / (revenue + 24.0058)).pct_change(4)).rolling(5).min()) * 0.165211)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc074_252d_base_v074_signal'] = f211w_f211_working_capital_turnover_velocity_calc074_252d_base_v074_signal

def f211w_f211_working_capital_turnover_velocity_calc075_126d_base_v075_signal(workingcapital, revenue):
    res = (((((workingcapital.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(16).std()).rolling(6).max()).rolling(8).min()) * 0.498408)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f211w_f211_working_capital_turnover_velocity_calc075_126d_base_v075_signal'] = f211w_f211_working_capital_turnover_velocity_calc075_126d_base_v075_signal


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
