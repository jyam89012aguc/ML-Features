import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f214e_f214_ebitda_to_revenue_margin_regime_calc001_5d_base_v001_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(14) / revenue.pct_change(18)).diff(4)).rolling(11).var()) * 0.480919)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc001_5d_base_v001_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc001_5d_base_v001_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc002_21d_base_v002_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(19) / revenue.pct_change(20)).rolling(17).std()).pct_change(8)).rolling(16).min()) * 0.524296)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc002_21d_base_v002_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc002_21d_base_v002_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc003_126d_base_v003_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 78.9039)).pct_change(17)).diff(6)).rolling(11).var()) * 0.714974)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc003_126d_base_v003_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc003_126d_base_v003_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc004_10d_base_v004_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(18) / revenue.pct_change(4)).rolling(28).std()).rolling(6).mean()) * 0.078201)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc004_10d_base_v004_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc004_10d_base_v004_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc005_10d_base_v005_signal(ebitda, revenue):
    res = (((((ebitda / (revenue + 60.6973)).diff(1)).rolling(18).mean()).rolling(15).std()) * 0.871091)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc005_10d_base_v005_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc005_10d_base_v005_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc006_21d_base_v006_signal(ebitda, revenue):
    res = ((((ebitda * 49.0048 - revenue).pct_change(16)).rolling(18).min()) * 0.209878)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc006_21d_base_v006_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc006_21d_base_v006_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc007_126d_base_v007_signal(ebitda, revenue):
    res = (((((ebitda.diff(6) / (revenue.shift(6) + 8.8005)).diff(12)).rolling(22).max()).rolling(17).var()) * 0.456907)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc007_126d_base_v007_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc007_126d_base_v007_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc008_10d_base_v008_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 37.9531)).pct_change(15)).rolling(30).min()).diff(18)).rolling(25).std()) * 0.855483)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc008_10d_base_v008_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc008_10d_base_v008_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc009_5d_base_v009_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 39.3103)).rolling(23).min()).rolling(8).std()) * 0.548387)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc009_5d_base_v009_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc009_5d_base_v009_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc010_42d_base_v010_signal(ebitda, revenue):
    res = ((((ebitda.diff(19) / (revenue.shift(10) + 78.7424)).rolling(6).std()).rolling(20).max()) * 0.723737)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc010_42d_base_v010_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc010_42d_base_v010_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc011_63d_base_v011_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(14) / revenue.pct_change(11)).rolling(22).mean()).rolling(9).var()).rolling(19).max()).rolling(9).std()) * 0.413701)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc011_63d_base_v011_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc011_63d_base_v011_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc012_10d_base_v012_signal(ebitda, revenue):
    res = ((((((ebitda.diff(8) / (revenue.shift(10) + 32.5777)).rolling(10).var()).rolling(5).min()).rolling(25).min()).diff(15)) * 0.366418)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc012_10d_base_v012_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc012_10d_base_v012_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc013_126d_base_v013_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 74.3916)).rolling(10).var()).pct_change(9)).rolling(27).max()).pct_change(16)) * 0.49324)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc013_126d_base_v013_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc013_126d_base_v013_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc014_63d_base_v014_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 71.5775)).rolling(7).max()).rolling(4).min()) * 0.124149)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc014_63d_base_v014_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc014_63d_base_v014_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc015_10d_base_v015_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(17) / revenue.pct_change(16)).rolling(17).std()).diff(11)) * 0.25156)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc015_10d_base_v015_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc015_10d_base_v015_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc016_10d_base_v016_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 57.9999)).pct_change(4)).rolling(27).std()).rolling(14).var()).diff(2)) * 0.557146)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc016_10d_base_v016_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc016_10d_base_v016_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc017_63d_base_v017_signal(ebitda, revenue):
    res = ((((((ebitda * 18.9252 - revenue).rolling(18).min()).rolling(18).max()).pct_change(19)).rolling(13).min()) * 0.046904)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc017_63d_base_v017_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc017_63d_base_v017_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc018_126d_base_v018_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 21.1375)).rolling(14).max()).rolling(27).mean()).pct_change(2)).rolling(2).std()) * 0.735181)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc018_126d_base_v018_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc018_126d_base_v018_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc019_21d_base_v019_signal(ebitda, revenue):
    res = ((((ebitda.diff(13) / (revenue.shift(2) + 97.8012)).rolling(4).min()).rolling(28).var()) * 0.241562)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc019_21d_base_v019_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc019_21d_base_v019_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc020_252d_base_v020_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(1) / revenue.pct_change(5)).rolling(26).std()).diff(19)).diff(12)).diff(1)) * 0.21585)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc020_252d_base_v020_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc020_252d_base_v020_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc021_5d_base_v021_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 30.3488)).rolling(15).max()).rolling(4).min()) * 0.478409)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc021_5d_base_v021_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc021_5d_base_v021_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc022_10d_base_v022_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 68.7087)).rolling(25).std()).rolling(5).std()).rolling(7).std()).rolling(29).mean()) * 0.499868)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc022_10d_base_v022_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc022_10d_base_v022_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc023_126d_base_v023_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 92.4064)).pct_change(3)).rolling(5).mean()).rolling(14).min()).rolling(6).mean()) * 0.950912)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc023_126d_base_v023_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc023_126d_base_v023_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc024_10d_base_v024_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(5) / revenue.pct_change(11)).rolling(26).max()).rolling(9).min()).rolling(21).std()).diff(7)) * 0.615158)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc024_10d_base_v024_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc024_10d_base_v024_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc025_5d_base_v025_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 29.4319)).rolling(16).std()).diff(10)).pct_change(17)).rolling(6).mean()) * 0.198596)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc025_5d_base_v025_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc025_5d_base_v025_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc026_252d_base_v026_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(1) / revenue.pct_change(18)).diff(17)).rolling(12).std()).pct_change(1)) * 0.182614)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc026_252d_base_v026_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc026_252d_base_v026_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc027_63d_base_v027_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 66.5259)).pct_change(19)).rolling(24).std()) * 0.972344)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc027_63d_base_v027_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc027_63d_base_v027_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc028_252d_base_v028_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(1) / revenue.pct_change(7)).rolling(21).max()).rolling(6).var()).pct_change(19)).rolling(28).min()) * 0.958323)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc028_252d_base_v028_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc028_252d_base_v028_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc029_5d_base_v029_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 77.6587)).rolling(19).var()).rolling(19).var()).rolling(14).var()) * 0.234286)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc029_5d_base_v029_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc029_5d_base_v029_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc030_21d_base_v030_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 76.281)).rolling(3).min()).rolling(5).min()) * 0.137727)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc030_21d_base_v030_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc030_21d_base_v030_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc031_21d_base_v031_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 61.4637)).rolling(3).max()).rolling(25).min()).diff(3)).rolling(15).min()) * 0.479724)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc031_21d_base_v031_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc031_21d_base_v031_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc032_252d_base_v032_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(10) / revenue.pct_change(17)).rolling(12).var()).rolling(29).var()) * 0.414094)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc032_252d_base_v032_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc032_252d_base_v032_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc033_10d_base_v033_signal(ebitda, revenue):
    res = ((((revenue / (ebitda + 82.794)).rolling(2).mean()).rolling(13).max()) * 0.68076)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc033_10d_base_v033_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc033_10d_base_v033_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc034_42d_base_v034_signal(ebitda, revenue):
    res = ((((ebitda * 95.6632 - revenue).rolling(16).var()).rolling(23).max()) * 0.56314)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc034_42d_base_v034_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc034_42d_base_v034_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc035_252d_base_v035_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(28).std()).pct_change(9)) * 0.37453)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc035_252d_base_v035_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc035_252d_base_v035_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc036_42d_base_v036_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 43.4751)).rolling(2).std()).pct_change(14)) * 0.118349)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc036_42d_base_v036_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc036_42d_base_v036_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc037_63d_base_v037_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(19).mean()).rolling(18).mean()).rolling(27).mean()).diff(12)) * 0.450339)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc037_63d_base_v037_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc037_63d_base_v037_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc038_42d_base_v038_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 10.8295)).rolling(3).max()).rolling(16).min()) * 0.590892)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc038_42d_base_v038_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc038_42d_base_v038_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc039_5d_base_v039_signal(ebitda, revenue):
    res = (((((ebitda.diff(8) / (revenue.shift(6) + 24.7257)).rolling(10).max()).rolling(11).min()).rolling(27).std()) * 0.462707)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc039_5d_base_v039_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc039_5d_base_v039_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc040_42d_base_v040_signal(ebitda, revenue):
    res = (((((revenue / (ebitda + 17.5806)).rolling(29).max()).rolling(23).max()).rolling(16).var()) * 0.699983)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc040_42d_base_v040_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc040_42d_base_v040_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc041_42d_base_v041_signal(ebitda, revenue):
    res = ((((ebitda * 70.3704 - revenue).rolling(8).var()).diff(7)) * 0.594237)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc041_42d_base_v041_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc041_42d_base_v041_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc042_63d_base_v042_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(13).mean()).rolling(4).max()) * 0.816134)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc042_63d_base_v042_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc042_63d_base_v042_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc043_63d_base_v043_signal(ebitda, revenue):
    res = (((((ebitda.diff(16) / (revenue.shift(1) + 24.1307)).rolling(15).min()).rolling(11).mean()).rolling(22).var()) * 0.145458)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc043_63d_base_v043_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc043_63d_base_v043_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc044_63d_base_v044_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(5).min()).rolling(3).var()).rolling(25).mean()).diff(9)) * 0.076455)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc044_63d_base_v044_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc044_63d_base_v044_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc045_63d_base_v045_signal(ebitda, revenue):
    res = ((((ebitda * 23.6716 - revenue).rolling(9).var()).diff(3)) * 0.762907)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc045_63d_base_v045_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc045_63d_base_v045_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc046_21d_base_v046_signal(ebitda, revenue):
    res = (((((ebitda * 78.4673 - revenue).diff(20)).pct_change(16)).rolling(27).min()) * 0.051451)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc046_21d_base_v046_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc046_21d_base_v046_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc047_63d_base_v047_signal(ebitda, revenue):
    res = (((((ebitda * 52.9659 - revenue).diff(4)).pct_change(14)).rolling(21).min()) * 0.492968)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc047_63d_base_v047_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc047_63d_base_v047_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc048_63d_base_v048_signal(ebitda, revenue):
    res = (((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(17).mean()).rolling(20).min()).rolling(9).var()) * 0.110014)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc048_63d_base_v048_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc048_63d_base_v048_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc049_10d_base_v049_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(7) / revenue.pct_change(17)).rolling(11).max()).rolling(20).max()).rolling(21).mean()).rolling(27).min()) * 0.756951)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc049_10d_base_v049_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc049_10d_base_v049_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc050_5d_base_v050_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 6.7929)).rolling(3).min()).rolling(16).max()) * 0.816095)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc050_5d_base_v050_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc050_5d_base_v050_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc051_252d_base_v051_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 90.4172)).diff(1)).diff(9)).rolling(29).mean()).rolling(27).max()) * 0.837366)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc051_252d_base_v051_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc051_252d_base_v051_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc052_5d_base_v052_signal(ebitda, revenue):
    res = ((((((ebitda * 23.5976 - revenue).rolling(30).min()).rolling(30).std()).rolling(4).mean()).rolling(2).min()) * 0.680659)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc052_5d_base_v052_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc052_5d_base_v052_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc053_126d_base_v053_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 83.6444)).rolling(30).min()).rolling(11).var()).rolling(6).max()).rolling(26).std()) * 0.503577)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc053_126d_base_v053_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc053_126d_base_v053_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc054_5d_base_v054_signal(ebitda, revenue):
    res = (((((ebitda * 45.184 - revenue).rolling(13).max()).rolling(2).min()).rolling(7).max()) * 0.872574)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc054_5d_base_v054_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc054_5d_base_v054_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc055_5d_base_v055_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(28).mean()).pct_change(6)).pct_change(7)).rolling(20).min()) * 0.264311)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc055_5d_base_v055_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc055_5d_base_v055_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc056_5d_base_v056_signal(ebitda, revenue):
    res = ((((((ebitda.pct_change(17) / revenue.pct_change(16)).rolling(27).var()).rolling(21).std()).diff(14)).rolling(30).max()) * 0.405165)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc056_5d_base_v056_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc056_5d_base_v056_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc057_63d_base_v057_signal(ebitda, revenue):
    res = ((((ebitda.diff(13) / (revenue.shift(10) + 15.1287)).rolling(13).max()).rolling(24).std()) * 0.721681)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc057_63d_base_v057_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc057_63d_base_v057_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc058_5d_base_v058_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(30).min()).rolling(22).max()) * 0.784661)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc058_5d_base_v058_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc058_5d_base_v058_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc059_10d_base_v059_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(8) / revenue.pct_change(11)).rolling(5).var()).pct_change(15)).rolling(27).max()) * 0.288435)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc059_10d_base_v059_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc059_10d_base_v059_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc060_252d_base_v060_signal(ebitda, revenue):
    res = (((((ebitda * 80.5007 - revenue).diff(10)).pct_change(20)).rolling(14).min()) * 0.666628)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc060_252d_base_v060_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc060_252d_base_v060_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc061_63d_base_v061_signal(ebitda, revenue):
    res = ((((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(6).var()).rolling(16).mean()).rolling(6).mean()).rolling(12).max()) * 0.269535)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc061_63d_base_v061_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc061_63d_base_v061_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc062_5d_base_v062_signal(ebitda, revenue):
    res = ((((((ebitda.diff(12) / (revenue.shift(10) + 38.6549)).rolling(6).max()).rolling(18).mean()).rolling(27).max()).pct_change(8)) * 0.166611)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc062_5d_base_v062_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc062_5d_base_v062_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc063_21d_base_v063_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(14).var()).rolling(6).min()) * 0.532049)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc063_21d_base_v063_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc063_21d_base_v063_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc064_252d_base_v064_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 52.7682)).rolling(4).var()).rolling(28).std()) * 0.599904)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc064_252d_base_v064_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc064_252d_base_v064_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc065_5d_base_v065_signal(ebitda, revenue):
    res = ((((((revenue / (ebitda + 58.6911)).rolling(5).min()).rolling(8).std()).rolling(25).min()).rolling(30).min()) * 0.751555)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc065_5d_base_v065_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc065_5d_base_v065_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc066_5d_base_v066_signal(ebitda, revenue):
    res = ((((ebitda * 34.2387 - revenue).rolling(12).min()).pct_change(1)) * 0.971392)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc066_5d_base_v066_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc066_5d_base_v066_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc067_10d_base_v067_signal(ebitda, revenue):
    res = ((((((ebitda / (revenue + 36.0956)).rolling(15).mean()).rolling(22).var()).rolling(29).mean()).rolling(24).std()) * 0.947025)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc067_10d_base_v067_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc067_10d_base_v067_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc068_21d_base_v068_signal(ebitda, revenue):
    res = (((((ebitda.pct_change(3) / revenue.pct_change(16)).diff(3)).pct_change(17)).rolling(24).std()) * 0.781944)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc068_21d_base_v068_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc068_21d_base_v068_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc069_21d_base_v069_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(18) / revenue.pct_change(18)).pct_change(13)).rolling(28).min()) * 0.57177)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc069_21d_base_v069_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc069_21d_base_v069_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc070_63d_base_v070_signal(ebitda, revenue):
    res = ((((ebitda / (revenue + 14.6315)).pct_change(11)).rolling(7).max()) * 0.276069)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc070_63d_base_v070_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc070_63d_base_v070_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc071_42d_base_v071_signal(ebitda, revenue):
    res = ((((ebitda * 62.6964 - revenue).diff(19)).rolling(24).min()) * 0.938241)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc071_42d_base_v071_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc071_42d_base_v071_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc072_63d_base_v072_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(19) / revenue.pct_change(10)).rolling(12).var()).rolling(10).max()) * 0.315383)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc072_63d_base_v072_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc072_63d_base_v072_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc073_21d_base_v073_signal(ebitda, revenue):
    res = ((((ebitda.pct_change(5) / revenue.pct_change(20)).rolling(29).mean()).diff(16)) * 0.058315)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc073_21d_base_v073_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc073_21d_base_v073_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc074_21d_base_v074_signal(ebitda, revenue):
    res = ((((ebitda.replace(0, np.nan) / revenue.replace(0, np.nan)).rolling(23).min()).diff(2)) * 0.920173)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc074_21d_base_v074_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc074_21d_base_v074_signal

def f214e_f214_ebitda_to_revenue_margin_regime_calc075_10d_base_v075_signal(ebitda, revenue):
    res = ((((ebitda.diff(18) / (revenue.shift(7) + 83.2691)).rolling(24).min()).diff(5)) * 0.537061)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f214e_f214_ebitda_to_revenue_margin_regime_calc075_10d_base_v075_signal'] = f214e_f214_ebitda_to_revenue_margin_regime_calc075_10d_base_v075_signal


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
