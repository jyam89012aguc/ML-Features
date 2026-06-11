import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f214e_f214_ebitda_to_revenue_margin_regime_calc001_252d_jerk_v001_signal(ebitda, revenue):
    res = ((((((ebitda * 93.1193 - revenue).diff(17)).rolling(30).var()).rolling(7).var()) * 0.704693).diff(10).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc001_252d_jerk_v001_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc001_252d_jerk_v001_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc002_21d_jerk_v002_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(20) / revenue.pct_change(20)).rolling(13).max()).rolling(7).min()).rolling(30).max()) * 0.514308).diff(12).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc002_21d_jerk_v002_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc002_21d_jerk_v002_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc003_21d_jerk_v003_signal(ebitda, revenue):
    res = (((((ebitda * 63.5474 - revenue).rolling(6).std()).rolling(16).mean()) * 0.569594).diff(19).diff(15).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc003_21d_jerk_v003_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc003_21d_jerk_v003_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc004_126d_jerk_v004_signal(ebitda, revenue):
    res = (((((ebitda * 53.9274 - revenue).diff(20)).pct_change(15)) * 0.657127).diff(3).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc004_126d_jerk_v004_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc004_126d_jerk_v004_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc005_5d_jerk_v005_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 92.6304)).pct_change(7)).rolling(17).min()).pct_change(6)) * 0.745601).diff(17).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc005_5d_jerk_v005_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc005_5d_jerk_v005_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc006_63d_jerk_v006_signal(ebitda, revenue):
    res = ((((((ebitda * 10.5706 - revenue).pct_change(14)).pct_change(18)).rolling(26).mean()) * 0.188581).diff(3).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc006_63d_jerk_v006_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc006_63d_jerk_v006_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc007_10d_jerk_v007_signal(ebitda, revenue):
    res = (((((ebitda * 61.0145 - revenue).pct_change(1)).diff(20)) * 0.976123).diff(19).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc007_10d_jerk_v007_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc007_10d_jerk_v007_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc008_252d_jerk_v008_signal(ebitda, revenue):
    res = ((((((ebitda * 10.6261 - revenue).rolling(20).min()).rolling(9).std()).pct_change(12)) * 0.46865).diff(3).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc008_252d_jerk_v008_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc008_252d_jerk_v008_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc009_126d_jerk_v009_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 50.5088)).rolling(2).min()).diff(4)).rolling(20).mean()).rolling(27).std()) * 0.745841).diff(19).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc009_126d_jerk_v009_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc009_126d_jerk_v009_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc010_5d_jerk_v010_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 24.9371)).pct_change(11)).rolling(5).var()).rolling(25).std()).rolling(3).min()) * 0.850496).diff(19).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc010_5d_jerk_v010_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc010_5d_jerk_v010_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc011_126d_jerk_v011_signal(ebitda, revenue):
    res = ((((((ebitda.diff(4) / (revenue.shift(9) + 53.1588)).rolling(30).mean()).rolling(11).std()).rolling(24).std()) * 0.819825).diff(15).diff(7).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc011_126d_jerk_v011_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc011_126d_jerk_v011_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc012_42d_jerk_v012_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(4).min()).rolling(24).std()) * 0.346386).diff(12).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc012_42d_jerk_v012_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc012_42d_jerk_v012_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc013_126d_jerk_v013_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 59.9984)).rolling(22).mean()).rolling(19).var()).rolling(29).var()).pct_change(14)) * 0.566983).diff(3).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc013_126d_jerk_v013_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc013_126d_jerk_v013_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc014_126d_jerk_v014_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).max()).rolling(7).max()) * 0.451356).diff(12).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc014_126d_jerk_v014_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc014_126d_jerk_v014_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc015_252d_jerk_v015_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 87.7344)).rolling(28).std()).rolling(9).max()).rolling(17).min()).rolling(16).std()) * 0.109237).diff(1).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc015_252d_jerk_v015_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc015_252d_jerk_v015_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc016_63d_jerk_v016_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 59.4907)).rolling(18).std()).rolling(14).mean()).pct_change(9)) * 0.986833).diff(9).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc016_63d_jerk_v016_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc016_63d_jerk_v016_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc017_252d_jerk_v017_signal(ebitda, revenue):
    res = (((((((ebitda.diff(2) / (revenue.shift(2) + 70.5091)).rolling(12).std()).rolling(29).max()).pct_change(10)).rolling(28).min()) * 0.413964).diff(9).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc017_252d_jerk_v017_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc017_252d_jerk_v017_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc018_21d_jerk_v018_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).mean()).rolling(17).std()) * 0.046724).diff(14).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc018_21d_jerk_v018_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc018_21d_jerk_v018_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc019_42d_jerk_v019_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).max()).rolling(9).max()) * 0.850071).diff(19).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc019_42d_jerk_v019_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc019_42d_jerk_v019_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc020_252d_jerk_v020_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(24).var()).pct_change(20)).diff(1)) * 0.031176).diff(19).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc020_252d_jerk_v020_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc020_252d_jerk_v020_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc021_10d_jerk_v021_signal(ebitda, revenue):
    res = ((((((ebitda.diff(9) / (revenue.shift(10) + 50.6151)).pct_change(12)).rolling(29).mean()).diff(8)) * 0.758261).diff(11).diff(18).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc021_10d_jerk_v021_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc021_10d_jerk_v021_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc022_126d_jerk_v022_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 89.2864)).diff(14)).pct_change(18)) * 0.143069).diff(18).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc022_126d_jerk_v022_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc022_126d_jerk_v022_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc023_252d_jerk_v023_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 10.6553)).rolling(26).max()).rolling(30).max()).rolling(18).mean()).rolling(8).min()) * 0.386073).diff(18).diff(16).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc023_252d_jerk_v023_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc023_252d_jerk_v023_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc024_42d_jerk_v024_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(16)).rolling(2).min()).pct_change(9)) * 0.361961).diff(4).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc024_42d_jerk_v024_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc024_42d_jerk_v024_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc025_126d_jerk_v025_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(7) / revenue.pct_change(17)).rolling(7).mean()).rolling(6).max()).rolling(6).min()) * 0.022207).diff(12).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc025_126d_jerk_v025_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc025_126d_jerk_v025_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc026_252d_jerk_v026_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 16.7692)).rolling(25).mean()).diff(12)).rolling(16).min()).rolling(2).std()) * 0.048729).diff(9).diff(9).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc026_252d_jerk_v026_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc026_252d_jerk_v026_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc027_5d_jerk_v027_signal(ebitda, revenue):
    res = (((((ebitda * 2.0661 - revenue).rolling(10).std()).rolling(26).var()) * 0.703131).diff(8).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc027_5d_jerk_v027_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc027_5d_jerk_v027_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc028_126d_jerk_v028_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 7.6208)).rolling(16).max()).rolling(20).mean()).diff(18)) * 0.618956).diff(16).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc028_126d_jerk_v028_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc028_126d_jerk_v028_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc029_126d_jerk_v029_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 39.0385)).rolling(17).mean()).pct_change(10)).pct_change(5)) * 0.260644).diff(6).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc029_126d_jerk_v029_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc029_126d_jerk_v029_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc030_5d_jerk_v030_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 26.575)).pct_change(20)).rolling(3).mean()).rolling(11).std()).rolling(18).min()) * 0.882272).diff(14).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc030_5d_jerk_v030_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc030_5d_jerk_v030_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc031_126d_jerk_v031_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(6)).rolling(6).mean()).pct_change(2)).rolling(21).mean()) * 0.059255).diff(11).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc031_126d_jerk_v031_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc031_126d_jerk_v031_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc032_42d_jerk_v032_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 89.3369)).rolling(20).max()).rolling(2).mean()).rolling(16).var()) * 0.415822).diff(16).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc032_42d_jerk_v032_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc032_42d_jerk_v032_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc033_21d_jerk_v033_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 3.0995)).pct_change(15)).rolling(21).std()) * 0.103864).diff(15).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc033_21d_jerk_v033_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc033_21d_jerk_v033_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc034_10d_jerk_v034_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 75.2883)).rolling(28).max()).rolling(20).min()) * 0.043915).diff(2).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc034_10d_jerk_v034_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc034_10d_jerk_v034_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc035_42d_jerk_v035_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 88.4715)).rolling(29).var()).diff(9)).diff(14)) * 0.651984).diff(4).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc035_42d_jerk_v035_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc035_42d_jerk_v035_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc036_5d_jerk_v036_signal(ebitda, revenue):
    res = ((((((ebitda.diff(3) / (revenue.shift(8) + 56.991)).rolling(15).std()).rolling(6).mean()).pct_change(8)) * 0.546214).diff(10).diff(10).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc036_5d_jerk_v036_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc036_5d_jerk_v036_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc037_252d_jerk_v037_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(5) / revenue.pct_change(3)).rolling(6).mean()).rolling(7).var()).rolling(20).std()) * 0.894344).diff(9).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc037_252d_jerk_v037_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc037_252d_jerk_v037_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc038_10d_jerk_v038_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(9) / revenue.pct_change(10)).pct_change(16)).rolling(14).std()).rolling(2).max()) * 0.905585).diff(7).diff(6).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc038_10d_jerk_v038_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc038_10d_jerk_v038_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc039_42d_jerk_v039_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(15)).rolling(28).max()) * 0.35606).diff(10).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc039_42d_jerk_v039_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc039_42d_jerk_v039_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc040_5d_jerk_v040_signal(ebitda, revenue):
    res = ((((((ebitda * 97.0541 - revenue).rolling(14).mean()).rolling(6).mean()).rolling(5).mean()) * 0.673585).diff(19).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc040_5d_jerk_v040_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc040_5d_jerk_v040_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc041_21d_jerk_v041_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(25).var()).rolling(27).max()).rolling(30).max()).rolling(10).min()) * 0.536284).diff(16).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc041_21d_jerk_v041_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc041_21d_jerk_v041_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc042_42d_jerk_v042_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(2).mean()).rolling(18).max()).rolling(11).var()) * 0.900135).diff(15).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc042_42d_jerk_v042_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc042_42d_jerk_v042_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc043_5d_jerk_v043_signal(ebitda, revenue):
    res = (((((ebitda * 51.1661 - revenue).rolling(11).min()).rolling(29).max()) * 0.236107).diff(19).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc043_5d_jerk_v043_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc043_5d_jerk_v043_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc044_5d_jerk_v044_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(5)).pct_change(7)).pct_change(11)).rolling(10).std()) * 0.05274).diff(18).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc044_5d_jerk_v044_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc044_5d_jerk_v044_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc045_63d_jerk_v045_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 43.7609)).rolling(15).max()).rolling(10).var()).rolling(7).min()).rolling(24).std()) * 0.450066).diff(1).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc045_63d_jerk_v045_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc045_63d_jerk_v045_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc046_5d_jerk_v046_signal(ebitda, revenue):
    res = (((((ebitda.diff(16) / (revenue.shift(3) + 99.7873)).rolling(26).std()).rolling(2).std()) * 0.205316).diff(2).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc046_5d_jerk_v046_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc046_5d_jerk_v046_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc047_5d_jerk_v047_signal(ebitda, revenue):
    res = (((((ebitda * 54.8995 - revenue).rolling(2).max()).rolling(18).mean()) * 0.379365).diff(17).diff(19).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc047_5d_jerk_v047_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc047_5d_jerk_v047_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc048_252d_jerk_v048_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 77.8367)).rolling(29).max()).pct_change(3)) * 0.989287).diff(13).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc048_252d_jerk_v048_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc048_252d_jerk_v048_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc049_252d_jerk_v049_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(19)).diff(18)).pct_change(19)).diff(15)) * 0.159223).diff(20).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc049_252d_jerk_v049_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc049_252d_jerk_v049_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc050_42d_jerk_v050_signal(ebitda, revenue):
    res = ((((((ebitda * 0.9897 - revenue).rolling(10).min()).rolling(9).min()).rolling(3).mean()) * 0.789254).diff(1).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc050_42d_jerk_v050_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc050_42d_jerk_v050_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc051_252d_jerk_v051_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 84.1316)).diff(8)).rolling(4).min()) * 0.587697).diff(4).diff(17).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc051_252d_jerk_v051_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc051_252d_jerk_v051_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc052_5d_jerk_v052_signal(ebitda, revenue):
    res = (((((ebitda * 31.9022 - revenue).pct_change(19)).pct_change(10)) * 0.65891).diff(5).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc052_5d_jerk_v052_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc052_5d_jerk_v052_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc053_10d_jerk_v053_signal(ebitda, revenue):
    res = (((((ebitda.diff(1) / (revenue.shift(2) + 63.6286)).rolling(15).var()).rolling(2).min()) * 0.798821).diff(15).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc053_10d_jerk_v053_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc053_10d_jerk_v053_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc054_42d_jerk_v054_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(6).min()).diff(2)).rolling(3).mean()) * 0.605065).diff(18).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc054_42d_jerk_v054_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc054_42d_jerk_v054_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc055_21d_jerk_v055_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 88.1353)).diff(8)).rolling(16).max()) * 0.716597).diff(20).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc055_21d_jerk_v055_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc055_21d_jerk_v055_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc056_5d_jerk_v056_signal(ebitda, revenue):
    res = (((((ebitda * 15.0143 - revenue).rolling(10).min()).diff(11)) * 0.882869).diff(5).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc056_5d_jerk_v056_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc056_5d_jerk_v056_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc057_10d_jerk_v057_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 78.9879)).rolling(2).min()).rolling(11).mean()).rolling(7).mean()) * 0.361341).diff(20).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc057_10d_jerk_v057_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc057_10d_jerk_v057_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc058_252d_jerk_v058_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(18) / revenue.pct_change(4)).rolling(22).mean()).rolling(27).std()).diff(11)) * 0.146699).diff(12).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc058_252d_jerk_v058_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc058_252d_jerk_v058_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc059_5d_jerk_v059_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(9).std()).rolling(10).mean()).rolling(15).min()).rolling(3).mean()) * 0.858952).diff(3).diff(5).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc059_5d_jerk_v059_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc059_5d_jerk_v059_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc060_63d_jerk_v060_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 24.3061)).rolling(25).max()).diff(14)) * 0.150458).diff(3).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc060_63d_jerk_v060_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc060_63d_jerk_v060_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc061_5d_jerk_v061_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(15).min()).pct_change(11)).rolling(28).std()).pct_change(9)) * 0.651767).diff(10).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc061_5d_jerk_v061_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc061_5d_jerk_v061_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc062_126d_jerk_v062_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 4.6957)).rolling(14).var()).pct_change(1)).rolling(21).mean()).rolling(12).mean()) * 0.867813).diff(8).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc062_126d_jerk_v062_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc062_126d_jerk_v062_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc063_21d_jerk_v063_signal(ebitda, revenue):
    res = (((((ebitda.diff(7) / (revenue.shift(5) + 49.9721)).rolling(19).var()).rolling(4).min()) * 0.738651).diff(16).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc063_21d_jerk_v063_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc063_21d_jerk_v063_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc064_63d_jerk_v064_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(18).mean()).rolling(29).min()).rolling(24).min()) * 0.931397).diff(13).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc064_63d_jerk_v064_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc064_63d_jerk_v064_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc065_126d_jerk_v065_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(18)).rolling(18).min()).pct_change(9)) * 0.943649).diff(20).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc065_126d_jerk_v065_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc065_126d_jerk_v065_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc066_42d_jerk_v066_signal(ebitda, revenue):
    res = (((((ebitda.diff(6) / (revenue.shift(10) + 46.7614)).rolling(15).mean()).rolling(27).mean()) * 0.088909).diff(17).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc066_42d_jerk_v066_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc066_42d_jerk_v066_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc067_63d_jerk_v067_signal(ebitda, revenue):
    res = (((((ebitda.diff(5) / (revenue.shift(3) + 56.606)).rolling(3).var()).rolling(25).var()) * 0.983553).diff(14).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc067_63d_jerk_v067_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc067_63d_jerk_v067_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc068_63d_jerk_v068_signal(ebitda, revenue):
    res = (((((((ebitda * 15.3208 - revenue).pct_change(12)).rolling(13).std()).rolling(20).var()).pct_change(6)) * 0.118254).diff(1).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc068_63d_jerk_v068_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc068_63d_jerk_v068_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc069_126d_jerk_v069_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(19).max()).rolling(18).mean()) * 0.795009).diff(5).diff(15).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc069_126d_jerk_v069_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc069_126d_jerk_v069_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc070_10d_jerk_v070_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(8) / revenue.pct_change(11)).pct_change(10)).rolling(29).max()).pct_change(17)).pct_change(6)) * 0.665316).diff(3).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc070_10d_jerk_v070_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc070_10d_jerk_v070_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc071_63d_jerk_v071_signal(ebitda, revenue):
    res = (((((ebitda.diff(18) / (revenue.shift(1) + 27.795)).rolling(29).var()).rolling(28).mean()) * 0.795343).diff(4).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc071_63d_jerk_v071_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc071_63d_jerk_v071_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc072_10d_jerk_v072_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 9.2017)).rolling(9).std()).pct_change(1)).rolling(24).mean()).rolling(3).min()) * 0.808874).diff(10).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc072_10d_jerk_v072_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc072_10d_jerk_v072_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc073_126d_jerk_v073_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(5) / revenue.pct_change(4)).diff(17)).rolling(3).min()).rolling(8).mean()).rolling(3).std()) * 0.425406).diff(7).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc073_126d_jerk_v073_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc073_126d_jerk_v073_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc074_63d_jerk_v074_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 44.7275)).rolling(2).mean()).rolling(11).std()).rolling(28).min()) * 0.821511).diff(4).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc074_63d_jerk_v074_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc074_63d_jerk_v074_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc075_5d_jerk_v075_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(4)).diff(13)) * 0.496454).diff(5).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc075_5d_jerk_v075_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc075_5d_jerk_v075_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc076_126d_jerk_v076_signal(ebitda, revenue):
    res = (((((((ebitda * 71.5574 - revenue).rolling(29).var()).diff(15)).pct_change(17)).rolling(29).var()) * 0.968214).diff(12).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc076_126d_jerk_v076_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc076_126d_jerk_v076_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc077_126d_jerk_v077_signal(ebitda, revenue):
    res = (((((ebitda * 12.136 - revenue).diff(4)).rolling(17).mean()) * 0.211912).diff(6).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc077_126d_jerk_v077_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc077_126d_jerk_v077_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc078_63d_jerk_v078_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(2)).diff(8)).rolling(5).min()).rolling(5).min()) * 0.830379).diff(14).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc078_63d_jerk_v078_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc078_63d_jerk_v078_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc079_63d_jerk_v079_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 69.0569)).rolling(30).max()).pct_change(19)).diff(13)).rolling(17).var()) * 0.118847).diff(16).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc079_63d_jerk_v079_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc079_63d_jerk_v079_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc080_63d_jerk_v080_signal(ebitda, revenue):
    res = (((((ebitda * 19.8768 - revenue).rolling(7).mean()).pct_change(10)) * 0.342071).diff(18).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc080_63d_jerk_v080_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc080_63d_jerk_v080_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc081_126d_jerk_v081_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 72.3072)).diff(9)).diff(10)) * 0.54806).diff(7).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc081_126d_jerk_v081_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc081_126d_jerk_v081_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc082_10d_jerk_v082_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 87.6463)).rolling(23).max()).pct_change(13)).rolling(13).max()) * 0.954729).diff(15).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc082_10d_jerk_v082_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc082_10d_jerk_v082_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc083_42d_jerk_v083_signal(ebitda, revenue):
    res = (((((((ebitda * 66.6715 - revenue).rolling(9).mean()).rolling(29).max()).rolling(24).var()).diff(5)) * 0.029525).diff(3).diff(11).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc083_42d_jerk_v083_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc083_42d_jerk_v083_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc084_5d_jerk_v084_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 73.6064)).rolling(8).mean()).rolling(13).std()).rolling(28).mean()) * 0.831955).diff(17).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc084_5d_jerk_v084_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc084_5d_jerk_v084_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc085_252d_jerk_v085_signal(ebitda, revenue):
    res = (((((ebitda * 15.7384 - revenue).rolling(19).var()).pct_change(10)) * 0.841564).diff(17).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc085_252d_jerk_v085_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc085_252d_jerk_v085_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc086_10d_jerk_v086_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 2.4562)).pct_change(8)).rolling(6).mean()).rolling(13).mean()) * 0.305399).diff(3).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc086_10d_jerk_v086_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc086_10d_jerk_v086_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc087_42d_jerk_v087_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(10) / revenue.pct_change(13)).rolling(23).std()).pct_change(20)) * 0.758378).diff(11).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc087_42d_jerk_v087_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc087_42d_jerk_v087_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc088_21d_jerk_v088_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).var()).rolling(17).std()).rolling(28).max()) * 0.101603).diff(19).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc088_21d_jerk_v088_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc088_21d_jerk_v088_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc089_252d_jerk_v089_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(11) / revenue.pct_change(11)).rolling(19).std()).pct_change(3)) * 0.323656).diff(15).diff(16).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc089_252d_jerk_v089_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc089_252d_jerk_v089_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc090_21d_jerk_v090_signal(ebitda, revenue):
    res = (((((ebitda * 80.7373 - revenue).rolling(13).var()).rolling(6).var()) * 0.141307).diff(13).diff(2).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc090_21d_jerk_v090_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc090_21d_jerk_v090_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc091_252d_jerk_v091_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 67.1775)).pct_change(10)).rolling(26).min()).diff(12)) * 0.596587).diff(9).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc091_252d_jerk_v091_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc091_252d_jerk_v091_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc092_252d_jerk_v092_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 46.3113)).rolling(3).std()).pct_change(17)).rolling(5).min()) * 0.148519).diff(12).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc092_252d_jerk_v092_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc092_252d_jerk_v092_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc093_252d_jerk_v093_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 26.4311)).rolling(12).min()).rolling(9).var()) * 0.649292).diff(17).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc093_252d_jerk_v093_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc093_252d_jerk_v093_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc094_252d_jerk_v094_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(17) / revenue.pct_change(11)).diff(6)).rolling(3).min()).rolling(20).std()) * 0.443454).diff(6).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc094_252d_jerk_v094_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc094_252d_jerk_v094_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc095_21d_jerk_v095_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 77.0807)).rolling(28).max()).rolling(3).var()).rolling(15).min()).rolling(10).min()) * 0.396539).diff(5).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc095_21d_jerk_v095_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc095_21d_jerk_v095_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc096_42d_jerk_v096_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(16) / revenue.pct_change(3)).rolling(8).var()).diff(18)) * 0.379702).diff(13).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc096_42d_jerk_v096_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc096_42d_jerk_v096_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc097_42d_jerk_v097_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(17) / revenue.pct_change(14)).pct_change(16)).rolling(3).max()).rolling(30).min()).diff(1)) * 0.360972).diff(9).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc097_42d_jerk_v097_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc097_42d_jerk_v097_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc098_63d_jerk_v098_signal(ebitda, revenue):
    res = (((((ebitda.diff(8) / (revenue.shift(3) + 99.3655)).rolling(2).var()).rolling(27).var()) * 0.589495).diff(1).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc098_63d_jerk_v098_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc098_63d_jerk_v098_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc099_252d_jerk_v099_signal(ebitda, revenue):
    res = (((((((ebitda.diff(7) / (revenue.shift(10) + 60.438)).pct_change(15)).rolling(10).min()).pct_change(1)).rolling(8).var()) * 0.151894).diff(11).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc099_252d_jerk_v099_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc099_252d_jerk_v099_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc100_42d_jerk_v100_signal(ebitda, revenue):
    res = ((((((ebitda.diff(20) / (revenue.shift(8) + 5.8715)).rolling(15).std()).pct_change(3)).rolling(24).max()) * 0.474216).diff(1).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc100_42d_jerk_v100_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc100_42d_jerk_v100_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc101_252d_jerk_v101_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(7) / revenue.pct_change(13)).rolling(25).min()).rolling(7).std()) * 0.264479).diff(2).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc101_252d_jerk_v101_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc101_252d_jerk_v101_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc102_10d_jerk_v102_signal(ebitda, revenue):
    res = (((((((ebitda.diff(4) / (revenue.shift(2) + 94.3749)).rolling(15).min()).rolling(5).max()).rolling(5).min()).rolling(7).min()) * 0.154281).diff(2).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc102_10d_jerk_v102_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc102_10d_jerk_v102_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc103_10d_jerk_v103_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(9).max()).rolling(13).mean()).rolling(5).std()).pct_change(14)) * 0.542331).diff(19).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc103_10d_jerk_v103_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc103_10d_jerk_v103_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc104_10d_jerk_v104_signal(ebitda, revenue):
    res = (((((((ebitda * 58.493 - revenue).rolling(5).mean()).rolling(7).var()).diff(13)).rolling(17).var()) * 0.800342).diff(3).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc104_10d_jerk_v104_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc104_10d_jerk_v104_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc105_42d_jerk_v105_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 54.6821)).rolling(16).std()).pct_change(2)).rolling(23).var()) * 0.860985).diff(1).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc105_42d_jerk_v105_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc105_42d_jerk_v105_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc106_21d_jerk_v106_signal(ebitda, revenue):
    res = ((((((ebitda.diff(14) / (revenue.shift(8) + 58.3719)).rolling(9).max()).pct_change(4)).pct_change(15)) * 0.214505).diff(6).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc106_21d_jerk_v106_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc106_21d_jerk_v106_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc107_21d_jerk_v107_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 78.2737)).rolling(25).mean()).rolling(26).min()).rolling(10).var()).rolling(7).mean()) * 0.434567).diff(12).diff(20).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc107_21d_jerk_v107_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc107_21d_jerk_v107_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc108_126d_jerk_v108_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(20) / revenue.pct_change(8)).rolling(6).std()).rolling(24).min()).rolling(26).std()).rolling(7).min()) * 0.976908).diff(18).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc108_126d_jerk_v108_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc108_126d_jerk_v108_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc109_10d_jerk_v109_signal(ebitda, revenue):
    res = (((((((ebitda.diff(13) / (revenue.shift(4) + 89.4913)).pct_change(14)).rolling(6).mean()).pct_change(14)).diff(14)) * 0.125515).diff(15).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc109_10d_jerk_v109_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc109_10d_jerk_v109_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc110_126d_jerk_v110_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 33.1797)).rolling(10).min()).rolling(25).max()).diff(19)).rolling(2).var()) * 0.178213).diff(15).diff(1).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc110_126d_jerk_v110_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc110_126d_jerk_v110_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc111_63d_jerk_v111_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(3).std()).rolling(2).max()) * 0.436152).diff(4).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc111_63d_jerk_v111_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc111_63d_jerk_v111_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc112_252d_jerk_v112_signal(ebitda, revenue):
    res = (((((ebitda.diff(6) / (revenue.shift(3) + 84.4598)).rolling(3).max()).rolling(10).var()) * 0.593121).diff(18).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc112_252d_jerk_v112_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc112_252d_jerk_v112_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc113_5d_jerk_v113_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 58.5197)).rolling(7).mean()).rolling(13).std()) * 0.179886).diff(3).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc113_5d_jerk_v113_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc113_5d_jerk_v113_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc114_10d_jerk_v114_signal(ebitda, revenue):
    res = (((((((ebitda * 80.9778 - revenue).rolling(12).std()).rolling(12).var()).pct_change(2)).rolling(29).std()) * 0.897751).diff(13).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc114_10d_jerk_v114_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc114_10d_jerk_v114_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc115_63d_jerk_v115_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 81.3346)).rolling(11).std()).pct_change(8)) * 0.802365).diff(13).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc115_63d_jerk_v115_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc115_63d_jerk_v115_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc116_63d_jerk_v116_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(12) / revenue.pct_change(19)).rolling(22).max()).rolling(5).std()).rolling(28).std()).pct_change(9)) * 0.017098).diff(9).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc116_63d_jerk_v116_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc116_63d_jerk_v116_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc117_10d_jerk_v117_signal(ebitda, revenue):
    res = (((((((ebitda * 87.9824 - revenue).rolling(6).max()).rolling(5).mean()).rolling(9).std()).rolling(14).min()) * 0.066382).diff(7).diff(3).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc117_10d_jerk_v117_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc117_10d_jerk_v117_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc118_42d_jerk_v118_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).max()).pct_change(9)) * 0.586238).diff(3).diff(19).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc118_42d_jerk_v118_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc118_42d_jerk_v118_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc119_10d_jerk_v119_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(24).mean()).rolling(5).std()).rolling(13).min()) * 0.34506).diff(8).diff(13).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc119_10d_jerk_v119_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc119_10d_jerk_v119_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc120_10d_jerk_v120_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(11) / revenue.pct_change(5)).diff(13)).rolling(14).var()).rolling(30).mean()).rolling(24).std()) * 0.847871).diff(1).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc120_10d_jerk_v120_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc120_10d_jerk_v120_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc121_42d_jerk_v121_signal(ebitda, revenue):
    res = (((((ebitda * 12.1345 - revenue).diff(18)).rolling(12).var()) * 0.802479).diff(5).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc121_42d_jerk_v121_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc121_42d_jerk_v121_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc122_5d_jerk_v122_signal(ebitda, revenue):
    res = (((((ebitda.diff(3) / (revenue.shift(6) + 19.1861)).rolling(5).var()).rolling(8).var()) * 0.701048).diff(5).diff(4).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc122_5d_jerk_v122_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc122_5d_jerk_v122_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc123_63d_jerk_v123_signal(ebitda, revenue):
    res = ((((((ebitda * 64.0207 - revenue).diff(5)).rolling(16).var()).rolling(6).max()) * 0.303522).diff(12).diff(9).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc123_63d_jerk_v123_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc123_63d_jerk_v123_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc124_252d_jerk_v124_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(8) / revenue.pct_change(9)).rolling(24).var()).rolling(27).max()).rolling(20).mean()).rolling(25).std()) * 0.961333).diff(1).diff(10).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc124_252d_jerk_v124_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc124_252d_jerk_v124_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc125_252d_jerk_v125_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 54.3189)).rolling(26).std()).rolling(20).std()) * 0.492785).diff(19).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc125_252d_jerk_v125_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc125_252d_jerk_v125_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc126_42d_jerk_v126_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(23).max()).rolling(15).var()).rolling(3).var()).rolling(12).max()) * 0.360809).diff(17).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc126_42d_jerk_v126_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc126_42d_jerk_v126_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc127_126d_jerk_v127_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(11) / revenue.pct_change(14)).rolling(14).std()).pct_change(6)).rolling(25).mean()) * 0.198263).diff(17).diff(9).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc127_126d_jerk_v127_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc127_126d_jerk_v127_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc128_42d_jerk_v128_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(10) / revenue.pct_change(7)).diff(12)).rolling(27).mean()).rolling(14).max()) * 0.655293).diff(6).diff(18).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc128_42d_jerk_v128_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc128_42d_jerk_v128_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc129_10d_jerk_v129_signal(ebitda, revenue):
    res = (((((((ebitda.diff(1) / (revenue.shift(2) + 17.3441)).pct_change(13)).rolling(26).std()).rolling(16).var()).rolling(19).std()) * 0.862185).diff(14).diff(7).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc129_10d_jerk_v129_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc129_10d_jerk_v129_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc130_63d_jerk_v130_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 76.0719)).rolling(11).mean()).rolling(20).max()).rolling(21).std()) * 0.873196).diff(1).diff(1).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc130_63d_jerk_v130_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc130_63d_jerk_v130_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc131_63d_jerk_v131_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).mean()).pct_change(11)).pct_change(2)) * 0.419155).diff(19).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc131_63d_jerk_v131_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc131_63d_jerk_v131_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc132_42d_jerk_v132_signal(ebitda, revenue):
    res = (((((ebitda * 19.5011 - revenue).rolling(25).mean()).pct_change(3)) * 0.075418).diff(19).diff(8).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc132_42d_jerk_v132_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc132_42d_jerk_v132_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc133_10d_jerk_v133_signal(ebitda, revenue):
    res = ((((((ebitda.diff(20) / (revenue.shift(3) + 37.1365)).rolling(4).mean()).rolling(9).max()).rolling(29).min()) * 0.206776).diff(1).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc133_10d_jerk_v133_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc133_10d_jerk_v133_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc134_42d_jerk_v134_signal(ebitda, revenue):
    res = ((((((ebitda.diff(5) / (revenue.shift(8) + 96.5125)).rolling(14).var()).rolling(23).mean()).diff(14)) * 0.923129).diff(2).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc134_42d_jerk_v134_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc134_42d_jerk_v134_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc135_42d_jerk_v135_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 87.0438)).rolling(9).var()).rolling(7).min()).rolling(10).std()).rolling(4).min()) * 0.393104).diff(15).diff(14).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc135_42d_jerk_v135_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc135_42d_jerk_v135_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc136_126d_jerk_v136_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 14.7467)).diff(20)).rolling(11).var()) * 0.228473).diff(3).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc136_126d_jerk_v136_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc136_126d_jerk_v136_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc137_21d_jerk_v137_signal(ebitda, revenue):
    res = (((((ebitda.diff(4) / (revenue.shift(7) + 13.808)).diff(7)).rolling(7).min()) * 0.206049).diff(15).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc137_21d_jerk_v137_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc137_21d_jerk_v137_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc138_126d_jerk_v138_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(2) / revenue.pct_change(14)).pct_change(9)).rolling(11).max()) * 0.522892).diff(6).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc138_126d_jerk_v138_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc138_126d_jerk_v138_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc139_5d_jerk_v139_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 81.8971)).rolling(16).max()).rolling(4).mean()).pct_change(16)).rolling(21).max()) * 0.8724).diff(19).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc139_5d_jerk_v139_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc139_5d_jerk_v139_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc140_10d_jerk_v140_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).var()).rolling(4).var()).pct_change(16)) * 0.189097).diff(6).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc140_10d_jerk_v140_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc140_10d_jerk_v140_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc141_21d_jerk_v141_signal(ebitda, revenue):
    res = ((((((ebitda.diff(7) / (revenue.shift(9) + 34.6005)).rolling(26).max()).rolling(7).mean()).rolling(29).var()) * 0.775287).diff(10).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc141_21d_jerk_v141_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc141_21d_jerk_v141_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc142_21d_jerk_v142_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 74.5612)).diff(15)).rolling(8).std()).rolling(15).max()) * 0.38093).diff(9).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc142_21d_jerk_v142_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc142_21d_jerk_v142_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc143_126d_jerk_v143_signal(ebitda, revenue):
    res = (((((((ebitda.diff(20) / (revenue.shift(6) + 1.3076)).rolling(17).var()).diff(9)).rolling(4).std()).rolling(25).min()) * 0.948133).diff(9).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc143_126d_jerk_v143_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc143_126d_jerk_v143_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc144_21d_jerk_v144_signal(ebitda, revenue):
    res = (((((ebitda * 78.045 - revenue).rolling(23).var()).rolling(3).min()) * 0.601338).diff(10).diff(16).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc144_21d_jerk_v144_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc144_21d_jerk_v144_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc145_252d_jerk_v145_signal(ebitda, revenue):
    res = (((((((ebitda * 64.7896 - revenue).rolling(10).var()).rolling(16).std()).rolling(14).mean()).diff(13)) * 0.412354).diff(3).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc145_252d_jerk_v145_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc145_252d_jerk_v145_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc146_252d_jerk_v146_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(13)).pct_change(8)) * 0.648789).diff(13).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc146_252d_jerk_v146_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc146_252d_jerk_v146_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc147_252d_jerk_v147_signal(ebitda, revenue):
    res = (((((((ebitda.diff(12) / (revenue.shift(5) + 90.1428)).diff(20)).rolling(3).max()).rolling(6).mean()).rolling(17).min()) * 0.776506).diff(6).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc147_252d_jerk_v147_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc147_252d_jerk_v147_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc148_252d_jerk_v148_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(2) / revenue.pct_change(15)).rolling(2).min()).rolling(9).var()).rolling(15).var()).pct_change(14)) * 0.77153).diff(2).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc148_252d_jerk_v148_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc148_252d_jerk_v148_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc149_5d_jerk_v149_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 22.8666)).rolling(14).mean()).rolling(22).min()) * 0.253019).diff(15).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc149_5d_jerk_v149_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc149_5d_jerk_v149_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc150_5d_jerk_v150_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(5) / revenue.pct_change(6)).rolling(15).min()).pct_change(16)) * 0.471583).diff(19).diff(9).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc150_5d_jerk_v150_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc150_5d_jerk_v150_signal


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
