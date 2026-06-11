import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f214e_f214_ebitda_to_revenue_margin_regime_calc001_63d_slope_v001_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 4.0794)).pct_change(18)).rolling(15).max()).rolling(10).max()).rolling(2).std()) * 0.88713).diff(5).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc001_63d_slope_v001_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc001_63d_slope_v001_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc002_5d_slope_v002_signal(ebitda, revenue):
    res = (((((((ebitda.diff(8) / (revenue.shift(3) + 8.9298)).rolling(16).var()).rolling(26).var()).rolling(19).max()).pct_change(18)) * 0.39473).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc002_5d_slope_v002_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc002_5d_slope_v002_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc003_21d_slope_v003_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(14).std()).rolling(9).mean()).pct_change(8)) * 0.85349).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc003_21d_slope_v003_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc003_21d_slope_v003_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc004_126d_slope_v004_signal(ebitda, revenue):
    res = (((((((ebitda.diff(1) / (revenue.shift(3) + 80.4303)).rolling(4).std()).rolling(16).var()).rolling(30).min()).rolling(24).mean()) * 0.185597).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc004_126d_slope_v004_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc004_126d_slope_v004_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc005_10d_slope_v005_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(6) / revenue.pct_change(8)).rolling(7).mean()).rolling(15).std()).diff(6)).rolling(22).mean()) * 0.446019).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc005_10d_slope_v005_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc005_10d_slope_v005_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc006_126d_slope_v006_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(23).mean()).rolling(20).var()).rolling(15).mean()).rolling(26).mean()) * 0.076175).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc006_126d_slope_v006_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc006_126d_slope_v006_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc007_63d_slope_v007_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(18) / revenue.pct_change(3)).rolling(20).var()).diff(15)).diff(16)).rolling(24).std()) * 0.53482).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc007_63d_slope_v007_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc007_63d_slope_v007_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc008_42d_slope_v008_signal(ebitda, revenue):
    res = (((((((ebitda * 55.6457 - revenue).rolling(29).max()).rolling(4).std()).rolling(14).max()).rolling(6).max()) * 0.053568).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc008_42d_slope_v008_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc008_42d_slope_v008_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc009_63d_slope_v009_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 48.0112)).rolling(18).mean()).rolling(7).std()).diff(16)).rolling(2).std()) * 0.178931).diff(2).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc009_63d_slope_v009_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc009_63d_slope_v009_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc010_10d_slope_v010_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(8) / revenue.pct_change(5)).rolling(10).mean()).rolling(10).mean()) * 0.612741).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc010_10d_slope_v010_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc010_10d_slope_v010_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc011_42d_slope_v011_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(21).max()).diff(7)).diff(1)) * 0.651737).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc011_42d_slope_v011_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc011_42d_slope_v011_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc012_126d_slope_v012_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(2) / revenue.pct_change(9)).rolling(9).std()).pct_change(5)).rolling(24).std()).rolling(17).min()) * 0.022785).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc012_126d_slope_v012_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc012_126d_slope_v012_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc013_252d_slope_v013_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 93.0437)).rolling(4).max()).rolling(12).min()) * 0.691544).diff(2).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc013_252d_slope_v013_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc013_252d_slope_v013_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc014_42d_slope_v014_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).min()).rolling(30).min()).rolling(5).max()) * 0.203101).diff(20).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc014_42d_slope_v014_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc014_42d_slope_v014_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc015_63d_slope_v015_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(3)).rolling(11).min()).rolling(29).min()).rolling(3).max()) * 0.762547).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc015_63d_slope_v015_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc015_63d_slope_v015_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc016_63d_slope_v016_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(9) / revenue.pct_change(8)).pct_change(9)).rolling(21).mean()).rolling(14).min()).rolling(6).std()) * 0.530268).diff(19).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc016_63d_slope_v016_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc016_63d_slope_v016_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc017_5d_slope_v017_signal(ebitda, revenue):
    res = (((((ebitda * 80.1657 - revenue).rolling(14).var()).rolling(30).max()) * 0.208964).diff(12).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc017_5d_slope_v017_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc017_5d_slope_v017_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc018_252d_slope_v018_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 41.8266)).rolling(6).min()).rolling(20).mean()).rolling(27).max()).rolling(13).min()) * 0.960318).diff(12).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc018_252d_slope_v018_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc018_252d_slope_v018_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc019_5d_slope_v019_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(23).std()).rolling(21).var()).pct_change(7)) * 0.291201).diff(8).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc019_5d_slope_v019_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc019_5d_slope_v019_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc020_63d_slope_v020_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 41.7415)).pct_change(6)).rolling(6).min()) * 0.018365).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc020_63d_slope_v020_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc020_63d_slope_v020_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc021_252d_slope_v021_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(7) / revenue.pct_change(14)).pct_change(11)).diff(18)) * 0.299607).diff(11).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc021_252d_slope_v021_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc021_252d_slope_v021_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc022_21d_slope_v022_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(2) / revenue.pct_change(18)).rolling(23).max()).rolling(5).max()).diff(20)) * 0.109384).diff(14).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc022_21d_slope_v022_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc022_21d_slope_v022_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc023_10d_slope_v023_signal(ebitda, revenue):
    res = (((((ebitda.diff(3) / (revenue.shift(10) + 63.9831)).rolling(19).std()).rolling(27).var()) * 0.719868).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc023_10d_slope_v023_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc023_10d_slope_v023_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc024_10d_slope_v024_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(6) / revenue.pct_change(12)).rolling(19).var()).rolling(9).std()) * 0.953158).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc024_10d_slope_v024_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc024_10d_slope_v024_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc025_21d_slope_v025_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(3) / revenue.pct_change(3)).pct_change(17)).rolling(14).min()).rolling(13).mean()) * 0.940377).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc025_21d_slope_v025_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc025_21d_slope_v025_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc026_21d_slope_v026_signal(ebitda, revenue):
    res = ((((((ebitda.diff(13) / (revenue.shift(10) + 86.3704)).rolling(20).min()).diff(9)).diff(11)) * 0.772795).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc026_21d_slope_v026_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc026_21d_slope_v026_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc027_21d_slope_v027_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).max()).rolling(14).max()).pct_change(3)).rolling(8).min()) * 0.437854).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc027_21d_slope_v027_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc027_21d_slope_v027_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc028_10d_slope_v028_signal(ebitda, revenue):
    res = ((((((ebitda * 8.0 - revenue).pct_change(20)).rolling(18).var()).rolling(28).mean()) * 0.346392).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc028_10d_slope_v028_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc028_10d_slope_v028_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc029_10d_slope_v029_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(15)).rolling(5).std()).pct_change(8)) * 0.594026).diff(1).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc029_10d_slope_v029_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc029_10d_slope_v029_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc030_42d_slope_v030_signal(ebitda, revenue):
    res = (((((ebitda.diff(8) / (revenue.shift(6) + 87.0246)).rolling(5).min()).pct_change(10)) * 0.28066).diff(2).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc030_42d_slope_v030_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc030_42d_slope_v030_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc031_126d_slope_v031_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(26).var()).rolling(30).var()) * 0.647652).diff(10).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc031_126d_slope_v031_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc031_126d_slope_v031_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc032_10d_slope_v032_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 71.8676)).diff(1)).rolling(19).mean()) * 0.06472).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc032_10d_slope_v032_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc032_10d_slope_v032_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc033_42d_slope_v033_signal(ebitda, revenue):
    res = (((((((ebitda.diff(6) / (revenue.shift(3) + 94.0207)).rolling(16).max()).rolling(19).mean()).rolling(12).var()).rolling(8).std()) * 0.815513).diff(12).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc033_42d_slope_v033_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc033_42d_slope_v033_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc034_252d_slope_v034_signal(ebitda, revenue):
    res = ((((((ebitda.diff(6) / (revenue.shift(7) + 96.9492)).pct_change(16)).rolling(5).mean()).rolling(8).min()) * 0.283773).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc034_252d_slope_v034_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc034_252d_slope_v034_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc035_252d_slope_v035_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(14) / revenue.pct_change(11)).rolling(30).std()).rolling(16).min()) * 0.809551).diff(15).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc035_252d_slope_v035_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc035_252d_slope_v035_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc036_10d_slope_v036_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).mean()).rolling(22).mean()) * 0.402299).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc036_10d_slope_v036_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc036_10d_slope_v036_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc037_252d_slope_v037_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 62.967)).rolling(22).var()).rolling(23).max()).rolling(3).mean()) * 0.359968).diff(1).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc037_252d_slope_v037_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc037_252d_slope_v037_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc038_10d_slope_v038_signal(ebitda, revenue):
    res = ((((((ebitda.diff(5) / (revenue.shift(2) + 48.4361)).diff(7)).rolling(15).mean()).rolling(21).mean()) * 0.67877).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc038_10d_slope_v038_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc038_10d_slope_v038_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc039_10d_slope_v039_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(13) / revenue.pct_change(17)).rolling(17).mean()).rolling(3).std()).rolling(5).std()).rolling(14).std()) * 0.688454).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc039_10d_slope_v039_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc039_10d_slope_v039_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc040_21d_slope_v040_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(1) / revenue.pct_change(20)).rolling(25).max()).diff(16)) * 0.161091).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc040_21d_slope_v040_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc040_21d_slope_v040_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc041_21d_slope_v041_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 12.8693)).rolling(22).std()).diff(15)) * 0.376058).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc041_21d_slope_v041_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc041_21d_slope_v041_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc042_126d_slope_v042_signal(ebitda, revenue):
    res = ((((((ebitda.diff(20) / (revenue.shift(10) + 61.6333)).pct_change(16)).diff(8)).pct_change(12)) * 0.885749).diff(8).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc042_126d_slope_v042_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc042_126d_slope_v042_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc043_10d_slope_v043_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(19).mean()).rolling(3).min()) * 0.428285).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc043_10d_slope_v043_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc043_10d_slope_v043_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc044_10d_slope_v044_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(2).mean()).rolling(5).min()) * 0.497878).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc044_10d_slope_v044_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc044_10d_slope_v044_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc045_42d_slope_v045_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(18) / revenue.pct_change(18)).diff(3)).pct_change(16)) * 0.64191).diff(14).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc045_42d_slope_v045_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc045_42d_slope_v045_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc046_126d_slope_v046_signal(ebitda, revenue):
    res = ((((((ebitda.diff(9) / (revenue.shift(7) + 76.2283)).pct_change(9)).rolling(6).std()).rolling(8).std()) * 0.53345).diff(5).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc046_126d_slope_v046_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc046_126d_slope_v046_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc047_10d_slope_v047_signal(ebitda, revenue):
    res = ((((((ebitda.diff(17) / (revenue.shift(1) + 95.2332)).rolling(13).std()).rolling(23).max()).pct_change(19)) * 0.91125).diff(5).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc047_10d_slope_v047_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc047_10d_slope_v047_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc048_126d_slope_v048_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 81.5871)).rolling(28).std()).rolling(12).max()).rolling(13).std()) * 0.980996).diff(2).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc048_126d_slope_v048_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc048_126d_slope_v048_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc049_42d_slope_v049_signal(ebitda, revenue):
    res = (((((ebitda * 24.3001 - revenue).rolling(14).var()).diff(16)) * 0.889147).diff(9).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc049_42d_slope_v049_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc049_42d_slope_v049_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc050_5d_slope_v050_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 82.7845)).rolling(12).max()).rolling(2).std()).diff(3)).rolling(26).std()) * 0.016187).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc050_5d_slope_v050_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc050_5d_slope_v050_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc051_10d_slope_v051_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(8) / revenue.pct_change(19)).diff(12)).rolling(4).min()).rolling(25).var()) * 0.066185).diff(9).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc051_10d_slope_v051_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc051_10d_slope_v051_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc052_252d_slope_v052_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(3) / revenue.pct_change(6)).rolling(13).mean()).rolling(15).mean()).diff(9)).rolling(4).mean()) * 0.364301).diff(19).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc052_252d_slope_v052_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc052_252d_slope_v052_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc053_252d_slope_v053_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(1) / revenue.pct_change(19)).rolling(25).max()).rolling(20).min()) * 0.345376).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc053_252d_slope_v053_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc053_252d_slope_v053_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc054_63d_slope_v054_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 32.172)).rolling(10).mean()).rolling(15).std()) * 0.546179).diff(6).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc054_63d_slope_v054_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc054_63d_slope_v054_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc055_126d_slope_v055_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 1.5894)).rolling(8).mean()).rolling(9).max()).pct_change(14)) * 0.620294).diff(20).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc055_126d_slope_v055_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc055_126d_slope_v055_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc056_42d_slope_v056_signal(ebitda, revenue):
    res = ((((((ebitda * 46.3295 - revenue).rolling(4).std()).rolling(15).std()).rolling(30).min()) * 0.565199).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc056_42d_slope_v056_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc056_42d_slope_v056_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc057_10d_slope_v057_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(15) / revenue.pct_change(13)).rolling(12).min()).diff(19)) * 0.599903).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc057_10d_slope_v057_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc057_10d_slope_v057_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc058_63d_slope_v058_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(8) / revenue.pct_change(7)).rolling(30).max()).diff(10)).rolling(5).std()).rolling(4).max()) * 0.645773).diff(13).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc058_63d_slope_v058_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc058_63d_slope_v058_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc059_21d_slope_v059_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 30.9458)).rolling(3).std()).rolling(5).std()) * 0.04026).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc059_21d_slope_v059_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc059_21d_slope_v059_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc060_5d_slope_v060_signal(ebitda, revenue):
    res = (((((((ebitda.diff(12) / (revenue.shift(8) + 35.2621)).diff(15)).pct_change(10)).rolling(2).min()).diff(2)) * 0.033049).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc060_5d_slope_v060_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc060_5d_slope_v060_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc061_10d_slope_v061_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(10) / revenue.pct_change(18)).rolling(14).min()).rolling(20).var()).rolling(20).min()) * 0.560037).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc061_10d_slope_v061_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc061_10d_slope_v061_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc062_21d_slope_v062_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(12) / revenue.pct_change(14)).rolling(29).var()).rolling(3).var()) * 0.097246).diff(1).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc062_21d_slope_v062_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc062_21d_slope_v062_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc063_42d_slope_v063_signal(ebitda, revenue):
    res = (((((((ebitda * 24.502 - revenue).rolling(10).min()).rolling(15).max()).rolling(7).max()).rolling(16).min()) * 0.31844).diff(3).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc063_42d_slope_v063_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc063_42d_slope_v063_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc064_5d_slope_v064_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 88.2849)).rolling(3).std()).diff(12)).rolling(16).max()) * 0.564124).diff(1).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc064_5d_slope_v064_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc064_5d_slope_v064_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc065_10d_slope_v065_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(15) / revenue.pct_change(14)).rolling(11).min()).rolling(4).std()) * 0.11792).diff(11).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc065_10d_slope_v065_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc065_10d_slope_v065_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc066_63d_slope_v066_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(15).var()).diff(14)).rolling(11).std()) * 0.52403).diff(11).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc066_63d_slope_v066_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc066_63d_slope_v066_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc067_252d_slope_v067_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 26.2463)).rolling(5).max()).rolling(20).min()).rolling(20).max()) * 0.893104).diff(8).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc067_252d_slope_v067_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc067_252d_slope_v067_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc068_252d_slope_v068_signal(ebitda, revenue):
    res = (((((ebitda.diff(9) / (revenue.shift(5) + 60.7853)).rolling(30).max()).rolling(30).var()) * 0.827108).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc068_252d_slope_v068_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc068_252d_slope_v068_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc069_21d_slope_v069_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 1.8159)).rolling(18).var()).rolling(6).min()).rolling(25).max()).rolling(25).min()) * 0.753889).diff(7).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc069_21d_slope_v069_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc069_21d_slope_v069_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc070_63d_slope_v070_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 66.9339)).rolling(2).mean()).pct_change(19)) * 0.532515).diff(15).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc070_63d_slope_v070_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc070_63d_slope_v070_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc071_10d_slope_v071_signal(ebitda, revenue):
    res = (((((((ebitda.diff(16) / (revenue.shift(1) + 6.2143)).rolling(8).var()).rolling(22).var()).diff(14)).rolling(12).var()) * 0.17987).diff(16).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc071_10d_slope_v071_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc071_10d_slope_v071_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc072_252d_slope_v072_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 58.602)).rolling(20).var()).rolling(29).min()).rolling(14).var()) * 0.851961).diff(3).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc072_252d_slope_v072_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc072_252d_slope_v072_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc073_10d_slope_v073_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 72.3811)).pct_change(4)).rolling(25).std()) * 0.228977).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc073_10d_slope_v073_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc073_10d_slope_v073_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc074_21d_slope_v074_signal(ebitda, revenue):
    res = (((((((ebitda.diff(17) / (revenue.shift(10) + 85.8613)).rolling(22).var()).diff(16)).rolling(19).mean()).rolling(27).min()) * 0.857033).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc074_21d_slope_v074_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc074_21d_slope_v074_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc075_63d_slope_v075_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 60.9874)).diff(11)).rolling(14).min()).rolling(4).std()) * 0.935494).diff(3).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc075_63d_slope_v075_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc075_63d_slope_v075_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc076_10d_slope_v076_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 93.4614)).rolling(23).std()).diff(5)).rolling(29).mean()) * 0.549715).diff(8).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc076_10d_slope_v076_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc076_10d_slope_v076_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc077_10d_slope_v077_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 31.0717)).rolling(23).std()).rolling(24).min()).rolling(15).max()) * 0.2969).diff(17).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc077_10d_slope_v077_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc077_10d_slope_v077_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc078_126d_slope_v078_signal(ebitda, revenue):
    res = (((((((ebitda * 69.3453 - revenue).rolling(24).var()).diff(5)).rolling(29).max()).rolling(14).var()) * 0.794976).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc078_126d_slope_v078_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc078_126d_slope_v078_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc079_5d_slope_v079_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 15.3838)).rolling(8).var()).rolling(11).mean()).rolling(28).std()) * 0.798623).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc079_5d_slope_v079_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc079_5d_slope_v079_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc080_5d_slope_v080_signal(ebitda, revenue):
    res = (((((((ebitda * 15.6011 - revenue).rolling(15).var()).rolling(12).min()).rolling(16).std()).pct_change(11)) * 0.53583).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc080_5d_slope_v080_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc080_5d_slope_v080_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc081_10d_slope_v081_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 20.1841)).rolling(12).std()).rolling(20).min()) * 0.519908).diff(4).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc081_10d_slope_v081_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc081_10d_slope_v081_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc082_10d_slope_v082_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(4).min()).diff(4)).diff(14)) * 0.019762).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc082_10d_slope_v082_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc082_10d_slope_v082_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc083_21d_slope_v083_signal(ebitda, revenue):
    res = ((((((ebitda * 93.2882 - revenue).pct_change(11)).rolling(30).std()).diff(2)) * 0.020492).diff(6).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc083_21d_slope_v083_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc083_21d_slope_v083_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc084_21d_slope_v084_signal(ebitda, revenue):
    res = ((((((ebitda * 64.2113 - revenue).pct_change(16)).rolling(9).std()).rolling(8).mean()) * 0.216397).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc084_21d_slope_v084_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc084_21d_slope_v084_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc085_126d_slope_v085_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(19)).pct_change(1)) * 0.786556).diff(3).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc085_126d_slope_v085_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc085_126d_slope_v085_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc086_42d_slope_v086_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 71.7982)).pct_change(14)).pct_change(9)).diff(18)) * 0.94846).diff(15).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc086_42d_slope_v086_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc086_42d_slope_v086_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc087_126d_slope_v087_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(27).max()).pct_change(20)) * 0.109558).diff(6).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc087_126d_slope_v087_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc087_126d_slope_v087_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc088_21d_slope_v088_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 5.0996)).rolling(22).min()).rolling(12).std()).rolling(29).max()).rolling(7).mean()) * 0.362566).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc088_21d_slope_v088_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc088_21d_slope_v088_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc089_21d_slope_v089_signal(ebitda, revenue):
    res = ((((((ebitda * 59.9198 - revenue).diff(9)).rolling(25).max()).diff(5)) * 0.796611).diff(8).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc089_21d_slope_v089_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc089_21d_slope_v089_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc090_42d_slope_v090_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 24.9855)).rolling(3).mean()).rolling(18).mean()) * 0.193874).diff(15).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc090_42d_slope_v090_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc090_42d_slope_v090_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc091_63d_slope_v091_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(20) / revenue.pct_change(2)).rolling(29).min()).rolling(29).mean()) * 0.692951).diff(16).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc091_63d_slope_v091_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc091_63d_slope_v091_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc092_21d_slope_v092_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 69.3892)).rolling(21).max()).rolling(24).var()).rolling(7).var()).rolling(12).max()) * 0.791979).diff(4).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc092_21d_slope_v092_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc092_21d_slope_v092_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc093_42d_slope_v093_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 10.2922)).rolling(7).min()).rolling(2).std()).rolling(29).var()).rolling(6).var()) * 0.181993).diff(5).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc093_42d_slope_v093_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc093_42d_slope_v093_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc094_5d_slope_v094_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 37.6305)).diff(1)).diff(18)) * 0.379346).diff(7).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc094_5d_slope_v094_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc094_5d_slope_v094_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc095_10d_slope_v095_signal(ebitda, revenue):
    res = ((((((ebitda * 97.6186 - revenue).rolling(21).max()).rolling(12).max()).rolling(10).mean()) * 0.298539).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc095_10d_slope_v095_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc095_10d_slope_v095_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc096_5d_slope_v096_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(13) / revenue.pct_change(17)).rolling(21).mean()).pct_change(11)).rolling(27).std()) * 0.020118).diff(15).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc096_5d_slope_v096_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc096_5d_slope_v096_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc097_42d_slope_v097_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 25.8121)).diff(11)).rolling(9).min()).rolling(7).var()).rolling(17).min()) * 0.697951).diff(16).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc097_42d_slope_v097_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc097_42d_slope_v097_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc098_21d_slope_v098_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).min()).rolling(4).max()) * 0.166818).diff(5).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc098_21d_slope_v098_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc098_21d_slope_v098_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc099_252d_slope_v099_signal(ebitda, revenue):
    res = ((((((ebitda * 60.4982 - revenue).rolling(4).mean()).rolling(29).var()).pct_change(14)) * 0.037221).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc099_252d_slope_v099_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc099_252d_slope_v099_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc100_5d_slope_v100_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 15.2483)).diff(5)).diff(14)).rolling(28).std()) * 0.321391).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc100_5d_slope_v100_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc100_5d_slope_v100_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc101_126d_slope_v101_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 29.7362)).diff(9)).rolling(18).max()).rolling(22).mean()) * 0.758667).diff(18).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc101_126d_slope_v101_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc101_126d_slope_v101_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc102_21d_slope_v102_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 9.7999)).rolling(19).max()).pct_change(8)).diff(6)) * 0.210667).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc102_21d_slope_v102_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc102_21d_slope_v102_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc103_252d_slope_v103_signal(ebitda, revenue):
    res = (((((((ebitda.diff(5) / (revenue.shift(2) + 64.2724)).rolling(18).var()).diff(4)).diff(12)).rolling(6).max()) * 0.183245).diff(14).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc103_252d_slope_v103_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc103_252d_slope_v103_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc104_63d_slope_v104_signal(ebitda, revenue):
    res = (((((ebitda * 41.7739 - revenue).rolling(12).max()).rolling(19).var()) * 0.499513).diff(18).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc104_63d_slope_v104_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc104_63d_slope_v104_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc105_5d_slope_v105_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 39.0074)).rolling(17).max()).rolling(22).min()).rolling(17).max()).rolling(28).std()) * 0.979045).diff(11).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc105_5d_slope_v105_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc105_5d_slope_v105_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc106_63d_slope_v106_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(10) / revenue.pct_change(13)).pct_change(4)).rolling(15).max()).diff(5)) * 0.732014).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc106_63d_slope_v106_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc106_63d_slope_v106_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc107_21d_slope_v107_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 65.8845)).rolling(2).std()).rolling(24).var()) * 0.119557).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc107_21d_slope_v107_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc107_21d_slope_v107_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc108_5d_slope_v108_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(4) / revenue.pct_change(10)).rolling(30).max()).rolling(26).max()).pct_change(4)) * 0.6095).diff(3).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc108_5d_slope_v108_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc108_5d_slope_v108_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc109_42d_slope_v109_signal(ebitda, revenue):
    res = ((((((ebitda * 86.2838 - revenue).rolling(24).max()).rolling(5).max()).diff(6)) * 0.447583).diff(17).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc109_42d_slope_v109_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc109_42d_slope_v109_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc110_126d_slope_v110_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(25).mean()).diff(6)).diff(1)) * 0.730649).diff(2).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc110_126d_slope_v110_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc110_126d_slope_v110_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc111_5d_slope_v111_signal(ebitda, revenue):
    res = ((((((ebitda * 34.8488 - revenue).rolling(29).std()).rolling(2).mean()).rolling(22).var()) * 0.202774).diff(2).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc111_5d_slope_v111_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc111_5d_slope_v111_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc112_21d_slope_v112_signal(ebitda, revenue):
    res = (((((((ebitda.diff(17) / (revenue.shift(4) + 80.9803)).diff(6)).rolling(28).min()).pct_change(20)).rolling(23).std()) * 0.27475).diff(19).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc112_21d_slope_v112_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc112_21d_slope_v112_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc113_252d_slope_v113_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(29).std()).rolling(7).std()).pct_change(18)) * 0.068448).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc113_252d_slope_v113_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc113_252d_slope_v113_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc114_252d_slope_v114_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(16) / revenue.pct_change(14)).rolling(12).max()).diff(4)) * 0.885098).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc114_252d_slope_v114_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc114_252d_slope_v114_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc115_252d_slope_v115_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 75.0292)).rolling(11).max()).pct_change(4)).rolling(4).mean()) * 0.762604).diff(7).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc115_252d_slope_v115_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc115_252d_slope_v115_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc116_10d_slope_v116_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 66.416)).rolling(29).max()).rolling(25).max()).rolling(13).std()).rolling(16).std()) * 0.78528).diff(20).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc116_10d_slope_v116_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc116_10d_slope_v116_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc117_126d_slope_v117_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(22).mean()).rolling(15).mean()).pct_change(12)) * 0.527788).diff(19).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc117_126d_slope_v117_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc117_126d_slope_v117_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc118_10d_slope_v118_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 0.7268)).rolling(6).max()).rolling(21).min()) * 0.890877).diff(15).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc118_10d_slope_v118_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc118_10d_slope_v118_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc119_42d_slope_v119_signal(ebitda, revenue):
    res = (((((((ebitda * 11.7662 - revenue).diff(8)).rolling(24).max()).rolling(13).var()).diff(16)) * 0.909856).diff(6).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc119_42d_slope_v119_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc119_42d_slope_v119_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc120_126d_slope_v120_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(13) / revenue.pct_change(12)).rolling(14).max()).pct_change(6)).rolling(29).max()) * 0.980862).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc120_126d_slope_v120_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc120_126d_slope_v120_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc121_63d_slope_v121_signal(ebitda, revenue):
    res = (((((((ebitda * 82.9604 - revenue).rolling(30).max()).rolling(12).std()).rolling(9).var()).rolling(10).max()) * 0.145598).diff(14).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc121_63d_slope_v121_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc121_63d_slope_v121_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc122_126d_slope_v122_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 63.6825)).rolling(22).var()).rolling(6).min()).pct_change(20)) * 0.758716).diff(14).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc122_126d_slope_v122_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc122_126d_slope_v122_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc123_42d_slope_v123_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(19).mean()).rolling(19).mean()).pct_change(20)) * 0.987076).diff(15).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc123_42d_slope_v123_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc123_42d_slope_v123_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc124_21d_slope_v124_signal(ebitda, revenue):
    res = ((((((ebitda.diff(18) / (revenue.shift(6) + 68.6316)).rolling(4).var()).rolling(8).max()).pct_change(20)) * 0.49807).diff(17).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc124_21d_slope_v124_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc124_21d_slope_v124_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc125_252d_slope_v125_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(15) / revenue.pct_change(17)).rolling(14).std()).diff(19)).rolling(27).max()) * 0.412734).diff(18).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc125_252d_slope_v125_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc125_252d_slope_v125_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc126_5d_slope_v126_signal(ebitda, revenue):
    res = ((((((ebitda.diff(19) / (revenue.shift(9) + 99.7244)).rolling(27).mean()).rolling(7).max()).diff(17)) * 0.297108).diff(13).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc126_5d_slope_v126_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc126_5d_slope_v126_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc127_5d_slope_v127_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(14).min()).rolling(19).var()) * 0.177483).diff(20).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc127_5d_slope_v127_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc127_5d_slope_v127_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc128_5d_slope_v128_signal(ebitda, revenue):
    res = (((((ebitda * 1.906 - revenue).pct_change(8)).rolling(19).mean()) * 0.543477).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc128_5d_slope_v128_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc128_5d_slope_v128_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc129_63d_slope_v129_signal(ebitda, revenue):
    res = (((((((ebitda.pct_change(16) / revenue.pct_change(10)).rolling(9).max()).rolling(21).max()).diff(16)).rolling(28).var()) * 0.867435).diff(4).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc129_63d_slope_v129_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc129_63d_slope_v129_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc130_63d_slope_v130_signal(ebitda, revenue):
    res = (((((ebitda.diff(8) / (revenue.shift(1) + 34.8285)).rolling(2).mean()).rolling(3).std()) * 0.974563).diff(12).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc130_63d_slope_v130_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc130_63d_slope_v130_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc131_126d_slope_v131_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(20) / revenue.pct_change(12)).rolling(13).mean()).rolling(11).min()) * 0.675249).diff(4).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc131_126d_slope_v131_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc131_126d_slope_v131_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc132_63d_slope_v132_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(18).mean()).pct_change(16)).diff(1)).diff(4)) * 0.564027).diff(17).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc132_63d_slope_v132_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc132_63d_slope_v132_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc133_42d_slope_v133_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).diff(4)).rolling(9).mean()).rolling(11).var()) * 0.870623).diff(10).rolling(42).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc133_42d_slope_v133_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc133_42d_slope_v133_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc134_21d_slope_v134_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(16) / revenue.pct_change(9)).rolling(19).min()).rolling(28).min()).rolling(7).var()) * 0.5934).diff(10).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc134_21d_slope_v134_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc134_21d_slope_v134_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc135_5d_slope_v135_signal(ebitda, revenue):
    res = (((((((ebitda * 37.8452 - revenue).rolling(29).min()).rolling(6).min()).rolling(15).var()).pct_change(6)) * 0.781649).diff(6).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc135_5d_slope_v135_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc135_5d_slope_v135_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc136_252d_slope_v136_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).var()).rolling(17).var()) * 0.606809).diff(13).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc136_252d_slope_v136_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc136_252d_slope_v136_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc137_21d_slope_v137_signal(ebitda, revenue):
    res = ((((((ebitda * 54.1643 - revenue).rolling(7).var()).rolling(29).mean()).pct_change(8)) * 0.68104).diff(18).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc137_21d_slope_v137_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc137_21d_slope_v137_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc138_10d_slope_v138_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(10) / revenue.pct_change(11)).rolling(5).std()).rolling(24).std()).pct_change(20)) * 0.489317).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc138_10d_slope_v138_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc138_10d_slope_v138_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc139_5d_slope_v139_signal(ebitda, revenue):
    res = (((((((revenue / (ebitda + 74.1281)).rolling(22).std()).rolling(17).min()).rolling(15).std()).pct_change(9)) * 0.396499).diff(18).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc139_5d_slope_v139_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc139_5d_slope_v139_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc140_126d_slope_v140_signal(ebitda, revenue):
    res = ((((((ebitda * 54.6032 - revenue).rolling(7).std()).rolling(23).max()).rolling(7).var()) * 0.251453).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc140_126d_slope_v140_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc140_126d_slope_v140_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc141_10d_slope_v141_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(4).max()).rolling(4).min()).rolling(12).mean()) * 0.316375).diff(2).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc141_10d_slope_v141_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc141_10d_slope_v141_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc142_63d_slope_v142_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(10).var()).rolling(9).min()).pct_change(12)) * 0.05622).diff(7).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc142_63d_slope_v142_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc142_63d_slope_v142_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc143_21d_slope_v143_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 77.2605)).rolling(11).max()).diff(19)).rolling(8).min()) * 0.301612).diff(9).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc143_21d_slope_v143_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc143_21d_slope_v143_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc144_21d_slope_v144_signal(ebitda, revenue):
    res = (((((((ebitda * 84.7558 - revenue).rolling(9).mean()).rolling(5).std()).rolling(8).max()).rolling(4).min()) * 0.600974).diff(3).rolling(21).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc144_21d_slope_v144_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc144_21d_slope_v144_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc145_126d_slope_v145_signal(ebitda, revenue):
    res = (((((((ebitda / (revenue + 20.1838)).rolling(18).min()).rolling(30).max()).rolling(27).std()).rolling(4).max()) * 0.818988).diff(12).rolling(126).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc145_126d_slope_v145_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc145_126d_slope_v145_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc146_252d_slope_v146_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(23).var()).rolling(12).mean()) * 0.542439).diff(6).rolling(252).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc146_252d_slope_v146_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc146_252d_slope_v146_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc147_5d_slope_v147_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).mean()).rolling(20).max()).pct_change(4)).rolling(15).var()) * 0.309615).diff(16).rolling(5).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc147_5d_slope_v147_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc147_5d_slope_v147_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc148_10d_slope_v148_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(16) / revenue.pct_change(15)).rolling(20).std()).pct_change(13)).rolling(4).max()) * 0.861969).diff(10).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc148_10d_slope_v148_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc148_10d_slope_v148_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc149_10d_slope_v149_signal(ebitda, revenue):
    res = (((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).pct_change(14)).rolling(30).var()).rolling(3).var()).rolling(20).max()) * 0.398133).diff(19).rolling(10).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc149_10d_slope_v149_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc149_10d_slope_v149_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc150_63d_slope_v150_signal(ebitda, revenue):
    res = ((((((ebitda * 79.0506 - revenue).rolling(9).min()).rolling(2).max()).rolling(30).max()) * 0.685704).diff(8).rolling(63).mean())
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc150_63d_slope_v150_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc150_63d_slope_v150_signal


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
