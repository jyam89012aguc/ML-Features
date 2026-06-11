import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f66cr_f66_cyclical_regime_proxies_calc001_5d_3rd_v001_signal(close, marketcap):
    res = ((close / marketcap).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc001_5d_3rd_v001_signal'] = f66cr_f66_cyclical_regime_proxies_calc001_5d_3rd_v001_signal

def f66cr_f66_cyclical_regime_proxies_calc002_10d_3rd_v002_signal(close, marketcap):
    res = ((close / marketcap).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc002_10d_3rd_v002_signal'] = f66cr_f66_cyclical_regime_proxies_calc002_10d_3rd_v002_signal

def f66cr_f66_cyclical_regime_proxies_calc003_21d_3rd_v003_signal(close, marketcap):
    res = ((close / marketcap).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc003_21d_3rd_v003_signal'] = f66cr_f66_cyclical_regime_proxies_calc003_21d_3rd_v003_signal

def f66cr_f66_cyclical_regime_proxies_calc004_42d_3rd_v004_signal(close, marketcap):
    res = ((close / marketcap).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc004_42d_3rd_v004_signal'] = f66cr_f66_cyclical_regime_proxies_calc004_42d_3rd_v004_signal

def f66cr_f66_cyclical_regime_proxies_calc005_63d_3rd_v005_signal(close, marketcap):
    res = ((close / marketcap).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc005_63d_3rd_v005_signal'] = f66cr_f66_cyclical_regime_proxies_calc005_63d_3rd_v005_signal

def f66cr_f66_cyclical_regime_proxies_calc006_126d_3rd_v006_signal(close, marketcap):
    res = ((close / marketcap).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc006_126d_3rd_v006_signal'] = f66cr_f66_cyclical_regime_proxies_calc006_126d_3rd_v006_signal

def f66cr_f66_cyclical_regime_proxies_calc007_252d_3rd_v007_signal(close, marketcap):
    res = ((close / marketcap).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc007_252d_3rd_v007_signal'] = f66cr_f66_cyclical_regime_proxies_calc007_252d_3rd_v007_signal

def f66cr_f66_cyclical_regime_proxies_calc008_21d_3rd_v008_signal(close, marketcap):
    res = ((close / marketcap).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc008_21d_3rd_v008_signal'] = f66cr_f66_cyclical_regime_proxies_calc008_21d_3rd_v008_signal

def f66cr_f66_cyclical_regime_proxies_calc009_63d_3rd_v009_signal(close, marketcap):
    res = ((close / marketcap).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc009_63d_3rd_v009_signal'] = f66cr_f66_cyclical_regime_proxies_calc009_63d_3rd_v009_signal

def f66cr_f66_cyclical_regime_proxies_calc010_5d_3rd_v010_signal(close, marketcap):
    res = ((close / marketcap).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc010_5d_3rd_v010_signal'] = f66cr_f66_cyclical_regime_proxies_calc010_5d_3rd_v010_signal

def f66cr_f66_cyclical_regime_proxies_calc011_21d_3rd_v011_signal(close, marketcap):
    res = ((close / marketcap).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc011_21d_3rd_v011_signal'] = f66cr_f66_cyclical_regime_proxies_calc011_21d_3rd_v011_signal

def f66cr_f66_cyclical_regime_proxies_calc012_10d_3rd_v012_signal(close, marketcap):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(close / marketcap)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc012_10d_3rd_v012_signal'] = f66cr_f66_cyclical_regime_proxies_calc012_10d_3rd_v012_signal

def f66cr_f66_cyclical_regime_proxies_calc013_5d_3rd_v013_signal(pe, ps):
    res = ((pe / ps).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc013_5d_3rd_v013_signal'] = f66cr_f66_cyclical_regime_proxies_calc013_5d_3rd_v013_signal

def f66cr_f66_cyclical_regime_proxies_calc014_10d_3rd_v014_signal(pe, ps):
    res = ((pe / ps).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc014_10d_3rd_v014_signal'] = f66cr_f66_cyclical_regime_proxies_calc014_10d_3rd_v014_signal

def f66cr_f66_cyclical_regime_proxies_calc015_21d_3rd_v015_signal(pe, ps):
    res = ((pe / ps).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc015_21d_3rd_v015_signal'] = f66cr_f66_cyclical_regime_proxies_calc015_21d_3rd_v015_signal

def f66cr_f66_cyclical_regime_proxies_calc016_42d_3rd_v016_signal(pe, ps):
    res = ((pe / ps).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc016_42d_3rd_v016_signal'] = f66cr_f66_cyclical_regime_proxies_calc016_42d_3rd_v016_signal

def f66cr_f66_cyclical_regime_proxies_calc017_63d_3rd_v017_signal(pe, ps):
    res = ((pe / ps).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc017_63d_3rd_v017_signal'] = f66cr_f66_cyclical_regime_proxies_calc017_63d_3rd_v017_signal

def f66cr_f66_cyclical_regime_proxies_calc018_126d_3rd_v018_signal(pe, ps):
    res = ((pe / ps).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc018_126d_3rd_v018_signal'] = f66cr_f66_cyclical_regime_proxies_calc018_126d_3rd_v018_signal

def f66cr_f66_cyclical_regime_proxies_calc019_252d_3rd_v019_signal(pe, ps):
    res = ((pe / ps).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc019_252d_3rd_v019_signal'] = f66cr_f66_cyclical_regime_proxies_calc019_252d_3rd_v019_signal

def f66cr_f66_cyclical_regime_proxies_calc020_21d_3rd_v020_signal(pe, ps):
    res = ((pe / ps).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc020_21d_3rd_v020_signal'] = f66cr_f66_cyclical_regime_proxies_calc020_21d_3rd_v020_signal

def f66cr_f66_cyclical_regime_proxies_calc021_63d_3rd_v021_signal(pe, ps):
    res = ((pe / ps).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc021_63d_3rd_v021_signal'] = f66cr_f66_cyclical_regime_proxies_calc021_63d_3rd_v021_signal

def f66cr_f66_cyclical_regime_proxies_calc022_5d_3rd_v022_signal(pe, ps):
    res = ((pe / ps).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc022_5d_3rd_v022_signal'] = f66cr_f66_cyclical_regime_proxies_calc022_5d_3rd_v022_signal

def f66cr_f66_cyclical_regime_proxies_calc023_21d_3rd_v023_signal(pe, ps):
    res = ((pe / ps).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc023_21d_3rd_v023_signal'] = f66cr_f66_cyclical_regime_proxies_calc023_21d_3rd_v023_signal

def f66cr_f66_cyclical_regime_proxies_calc024_10d_3rd_v024_signal(pe, ps):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(pe / ps)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc024_10d_3rd_v024_signal'] = f66cr_f66_cyclical_regime_proxies_calc024_10d_3rd_v024_signal

def f66cr_f66_cyclical_regime_proxies_calc025_5d_3rd_v025_signal(revenue, assets):
    res = ((revenue / assets).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc025_5d_3rd_v025_signal'] = f66cr_f66_cyclical_regime_proxies_calc025_5d_3rd_v025_signal

def f66cr_f66_cyclical_regime_proxies_calc026_10d_3rd_v026_signal(revenue, assets):
    res = ((revenue / assets).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc026_10d_3rd_v026_signal'] = f66cr_f66_cyclical_regime_proxies_calc026_10d_3rd_v026_signal

def f66cr_f66_cyclical_regime_proxies_calc027_21d_3rd_v027_signal(revenue, assets):
    res = ((revenue / assets).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc027_21d_3rd_v027_signal'] = f66cr_f66_cyclical_regime_proxies_calc027_21d_3rd_v027_signal

def f66cr_f66_cyclical_regime_proxies_calc028_42d_3rd_v028_signal(revenue, assets):
    res = ((revenue / assets).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc028_42d_3rd_v028_signal'] = f66cr_f66_cyclical_regime_proxies_calc028_42d_3rd_v028_signal

def f66cr_f66_cyclical_regime_proxies_calc029_63d_3rd_v029_signal(revenue, assets):
    res = ((revenue / assets).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc029_63d_3rd_v029_signal'] = f66cr_f66_cyclical_regime_proxies_calc029_63d_3rd_v029_signal

def f66cr_f66_cyclical_regime_proxies_calc030_126d_3rd_v030_signal(revenue, assets):
    res = ((revenue / assets).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc030_126d_3rd_v030_signal'] = f66cr_f66_cyclical_regime_proxies_calc030_126d_3rd_v030_signal

def f66cr_f66_cyclical_regime_proxies_calc031_252d_3rd_v031_signal(revenue, assets):
    res = ((revenue / assets).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc031_252d_3rd_v031_signal'] = f66cr_f66_cyclical_regime_proxies_calc031_252d_3rd_v031_signal

def f66cr_f66_cyclical_regime_proxies_calc032_21d_3rd_v032_signal(revenue, assets):
    res = ((revenue / assets).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc032_21d_3rd_v032_signal'] = f66cr_f66_cyclical_regime_proxies_calc032_21d_3rd_v032_signal

def f66cr_f66_cyclical_regime_proxies_calc033_63d_3rd_v033_signal(revenue, assets):
    res = ((revenue / assets).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc033_63d_3rd_v033_signal'] = f66cr_f66_cyclical_regime_proxies_calc033_63d_3rd_v033_signal

def f66cr_f66_cyclical_regime_proxies_calc034_5d_3rd_v034_signal(revenue, assets):
    res = ((revenue / assets).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc034_5d_3rd_v034_signal'] = f66cr_f66_cyclical_regime_proxies_calc034_5d_3rd_v034_signal

def f66cr_f66_cyclical_regime_proxies_calc035_21d_3rd_v035_signal(revenue, assets):
    res = ((revenue / assets).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc035_21d_3rd_v035_signal'] = f66cr_f66_cyclical_regime_proxies_calc035_21d_3rd_v035_signal

def f66cr_f66_cyclical_regime_proxies_calc036_10d_3rd_v036_signal(revenue, assets):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / assets)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc036_10d_3rd_v036_signal'] = f66cr_f66_cyclical_regime_proxies_calc036_10d_3rd_v036_signal

def f66cr_f66_cyclical_regime_proxies_calc037_5d_3rd_v037_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc037_5d_3rd_v037_signal'] = f66cr_f66_cyclical_regime_proxies_calc037_5d_3rd_v037_signal

def f66cr_f66_cyclical_regime_proxies_calc038_10d_3rd_v038_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc038_10d_3rd_v038_signal'] = f66cr_f66_cyclical_regime_proxies_calc038_10d_3rd_v038_signal

def f66cr_f66_cyclical_regime_proxies_calc039_21d_3rd_v039_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc039_21d_3rd_v039_signal'] = f66cr_f66_cyclical_regime_proxies_calc039_21d_3rd_v039_signal

def f66cr_f66_cyclical_regime_proxies_calc040_42d_3rd_v040_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc040_42d_3rd_v040_signal'] = f66cr_f66_cyclical_regime_proxies_calc040_42d_3rd_v040_signal

def f66cr_f66_cyclical_regime_proxies_calc041_63d_3rd_v041_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc041_63d_3rd_v041_signal'] = f66cr_f66_cyclical_regime_proxies_calc041_63d_3rd_v041_signal

def f66cr_f66_cyclical_regime_proxies_calc042_126d_3rd_v042_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc042_126d_3rd_v042_signal'] = f66cr_f66_cyclical_regime_proxies_calc042_126d_3rd_v042_signal

def f66cr_f66_cyclical_regime_proxies_calc043_252d_3rd_v043_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc043_252d_3rd_v043_signal'] = f66cr_f66_cyclical_regime_proxies_calc043_252d_3rd_v043_signal

def f66cr_f66_cyclical_regime_proxies_calc044_21d_3rd_v044_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc044_21d_3rd_v044_signal'] = f66cr_f66_cyclical_regime_proxies_calc044_21d_3rd_v044_signal

def f66cr_f66_cyclical_regime_proxies_calc045_63d_3rd_v045_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc045_63d_3rd_v045_signal'] = f66cr_f66_cyclical_regime_proxies_calc045_63d_3rd_v045_signal

def f66cr_f66_cyclical_regime_proxies_calc046_5d_3rd_v046_signal(ebitda, ev):
    res = ((ebitda / ev).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc046_5d_3rd_v046_signal'] = f66cr_f66_cyclical_regime_proxies_calc046_5d_3rd_v046_signal

def f66cr_f66_cyclical_regime_proxies_calc047_21d_3rd_v047_signal(ebitda, ev):
    res = ((ebitda / ev).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc047_21d_3rd_v047_signal'] = f66cr_f66_cyclical_regime_proxies_calc047_21d_3rd_v047_signal

def f66cr_f66_cyclical_regime_proxies_calc048_10d_3rd_v048_signal(ebitda, ev):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ebitda / ev)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc048_10d_3rd_v048_signal'] = f66cr_f66_cyclical_regime_proxies_calc048_10d_3rd_v048_signal

def f66cr_f66_cyclical_regime_proxies_calc049_5d_3rd_v049_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc049_5d_3rd_v049_signal'] = f66cr_f66_cyclical_regime_proxies_calc049_5d_3rd_v049_signal

def f66cr_f66_cyclical_regime_proxies_calc050_10d_3rd_v050_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc050_10d_3rd_v050_signal'] = f66cr_f66_cyclical_regime_proxies_calc050_10d_3rd_v050_signal

def f66cr_f66_cyclical_regime_proxies_calc051_21d_3rd_v051_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc051_21d_3rd_v051_signal'] = f66cr_f66_cyclical_regime_proxies_calc051_21d_3rd_v051_signal

def f66cr_f66_cyclical_regime_proxies_calc052_42d_3rd_v052_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc052_42d_3rd_v052_signal'] = f66cr_f66_cyclical_regime_proxies_calc052_42d_3rd_v052_signal

def f66cr_f66_cyclical_regime_proxies_calc053_63d_3rd_v053_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc053_63d_3rd_v053_signal'] = f66cr_f66_cyclical_regime_proxies_calc053_63d_3rd_v053_signal

def f66cr_f66_cyclical_regime_proxies_calc054_126d_3rd_v054_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc054_126d_3rd_v054_signal'] = f66cr_f66_cyclical_regime_proxies_calc054_126d_3rd_v054_signal

def f66cr_f66_cyclical_regime_proxies_calc055_252d_3rd_v055_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc055_252d_3rd_v055_signal'] = f66cr_f66_cyclical_regime_proxies_calc055_252d_3rd_v055_signal

def f66cr_f66_cyclical_regime_proxies_calc056_21d_3rd_v056_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc056_21d_3rd_v056_signal'] = f66cr_f66_cyclical_regime_proxies_calc056_21d_3rd_v056_signal

def f66cr_f66_cyclical_regime_proxies_calc057_63d_3rd_v057_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc057_63d_3rd_v057_signal'] = f66cr_f66_cyclical_regime_proxies_calc057_63d_3rd_v057_signal

def f66cr_f66_cyclical_regime_proxies_calc058_5d_3rd_v058_signal(fcf, marketcap):
    res = ((fcf / marketcap).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc058_5d_3rd_v058_signal'] = f66cr_f66_cyclical_regime_proxies_calc058_5d_3rd_v058_signal

def f66cr_f66_cyclical_regime_proxies_calc059_21d_3rd_v059_signal(fcf, marketcap):
    res = ((fcf / marketcap).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc059_21d_3rd_v059_signal'] = f66cr_f66_cyclical_regime_proxies_calc059_21d_3rd_v059_signal

def f66cr_f66_cyclical_regime_proxies_calc060_10d_3rd_v060_signal(fcf, marketcap):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / marketcap)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc060_10d_3rd_v060_signal'] = f66cr_f66_cyclical_regime_proxies_calc060_10d_3rd_v060_signal

def f66cr_f66_cyclical_regime_proxies_calc061_5d_3rd_v061_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc061_5d_3rd_v061_signal'] = f66cr_f66_cyclical_regime_proxies_calc061_5d_3rd_v061_signal

def f66cr_f66_cyclical_regime_proxies_calc062_10d_3rd_v062_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc062_10d_3rd_v062_signal'] = f66cr_f66_cyclical_regime_proxies_calc062_10d_3rd_v062_signal

def f66cr_f66_cyclical_regime_proxies_calc063_21d_3rd_v063_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc063_21d_3rd_v063_signal'] = f66cr_f66_cyclical_regime_proxies_calc063_21d_3rd_v063_signal

def f66cr_f66_cyclical_regime_proxies_calc064_42d_3rd_v064_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc064_42d_3rd_v064_signal'] = f66cr_f66_cyclical_regime_proxies_calc064_42d_3rd_v064_signal

def f66cr_f66_cyclical_regime_proxies_calc065_63d_3rd_v065_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc065_63d_3rd_v065_signal'] = f66cr_f66_cyclical_regime_proxies_calc065_63d_3rd_v065_signal

def f66cr_f66_cyclical_regime_proxies_calc066_126d_3rd_v066_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc066_126d_3rd_v066_signal'] = f66cr_f66_cyclical_regime_proxies_calc066_126d_3rd_v066_signal

def f66cr_f66_cyclical_regime_proxies_calc067_252d_3rd_v067_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc067_252d_3rd_v067_signal'] = f66cr_f66_cyclical_regime_proxies_calc067_252d_3rd_v067_signal

def f66cr_f66_cyclical_regime_proxies_calc068_21d_3rd_v068_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc068_21d_3rd_v068_signal'] = f66cr_f66_cyclical_regime_proxies_calc068_21d_3rd_v068_signal

def f66cr_f66_cyclical_regime_proxies_calc069_63d_3rd_v069_signal(ncfo, debt):
    res = ((ncfo / debt).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc069_63d_3rd_v069_signal'] = f66cr_f66_cyclical_regime_proxies_calc069_63d_3rd_v069_signal

def f66cr_f66_cyclical_regime_proxies_calc070_5d_3rd_v070_signal(ncfo, debt):
    res = ((ncfo / debt).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc070_5d_3rd_v070_signal'] = f66cr_f66_cyclical_regime_proxies_calc070_5d_3rd_v070_signal

def f66cr_f66_cyclical_regime_proxies_calc071_21d_3rd_v071_signal(ncfo, debt):
    res = ((ncfo / debt).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc071_21d_3rd_v071_signal'] = f66cr_f66_cyclical_regime_proxies_calc071_21d_3rd_v071_signal

def f66cr_f66_cyclical_regime_proxies_calc072_10d_3rd_v072_signal(ncfo, debt):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ncfo / debt)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc072_10d_3rd_v072_signal'] = f66cr_f66_cyclical_regime_proxies_calc072_10d_3rd_v072_signal

def f66cr_f66_cyclical_regime_proxies_calc073_5d_3rd_v073_signal(opinc, revenue):
    res = ((opinc / revenue).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc073_5d_3rd_v073_signal'] = f66cr_f66_cyclical_regime_proxies_calc073_5d_3rd_v073_signal

def f66cr_f66_cyclical_regime_proxies_calc074_10d_3rd_v074_signal(opinc, revenue):
    res = ((opinc / revenue).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc074_10d_3rd_v074_signal'] = f66cr_f66_cyclical_regime_proxies_calc074_10d_3rd_v074_signal

def f66cr_f66_cyclical_regime_proxies_calc075_21d_3rd_v075_signal(opinc, revenue):
    res = ((opinc / revenue).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc075_21d_3rd_v075_signal'] = f66cr_f66_cyclical_regime_proxies_calc075_21d_3rd_v075_signal

def f66cr_f66_cyclical_regime_proxies_calc076_5d_3rd_v076_signal(netinc, equity):
    res = ((netinc / equity).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc076_5d_3rd_v076_signal'] = f66cr_f66_cyclical_regime_proxies_calc076_5d_3rd_v076_signal

def f66cr_f66_cyclical_regime_proxies_calc077_10d_3rd_v077_signal(netinc, equity):
    res = ((netinc / equity).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc077_10d_3rd_v077_signal'] = f66cr_f66_cyclical_regime_proxies_calc077_10d_3rd_v077_signal

def f66cr_f66_cyclical_regime_proxies_calc078_21d_3rd_v078_signal(netinc, equity):
    res = ((netinc / equity).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc078_21d_3rd_v078_signal'] = f66cr_f66_cyclical_regime_proxies_calc078_21d_3rd_v078_signal

def f66cr_f66_cyclical_regime_proxies_calc079_42d_3rd_v079_signal(netinc, equity):
    res = ((netinc / equity).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc079_42d_3rd_v079_signal'] = f66cr_f66_cyclical_regime_proxies_calc079_42d_3rd_v079_signal

def f66cr_f66_cyclical_regime_proxies_calc080_63d_3rd_v080_signal(netinc, equity):
    res = ((netinc / equity).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc080_63d_3rd_v080_signal'] = f66cr_f66_cyclical_regime_proxies_calc080_63d_3rd_v080_signal

def f66cr_f66_cyclical_regime_proxies_calc081_126d_3rd_v081_signal(netinc, equity):
    res = ((netinc / equity).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc081_126d_3rd_v081_signal'] = f66cr_f66_cyclical_regime_proxies_calc081_126d_3rd_v081_signal

def f66cr_f66_cyclical_regime_proxies_calc082_252d_3rd_v082_signal(netinc, equity):
    res = ((netinc / equity).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc082_252d_3rd_v082_signal'] = f66cr_f66_cyclical_regime_proxies_calc082_252d_3rd_v082_signal

def f66cr_f66_cyclical_regime_proxies_calc083_21d_3rd_v083_signal(netinc, equity):
    res = ((netinc / equity).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc083_21d_3rd_v083_signal'] = f66cr_f66_cyclical_regime_proxies_calc083_21d_3rd_v083_signal

def f66cr_f66_cyclical_regime_proxies_calc084_63d_3rd_v084_signal(netinc, equity):
    res = ((netinc / equity).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc084_63d_3rd_v084_signal'] = f66cr_f66_cyclical_regime_proxies_calc084_63d_3rd_v084_signal

def f66cr_f66_cyclical_regime_proxies_calc085_5d_3rd_v085_signal(netinc, equity):
    res = ((netinc / equity).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc085_5d_3rd_v085_signal'] = f66cr_f66_cyclical_regime_proxies_calc085_5d_3rd_v085_signal

def f66cr_f66_cyclical_regime_proxies_calc086_21d_3rd_v086_signal(netinc, equity):
    res = ((netinc / equity).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc086_21d_3rd_v086_signal'] = f66cr_f66_cyclical_regime_proxies_calc086_21d_3rd_v086_signal

def f66cr_f66_cyclical_regime_proxies_calc087_10d_3rd_v087_signal(netinc, equity):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(netinc / equity)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc087_10d_3rd_v087_signal'] = f66cr_f66_cyclical_regime_proxies_calc087_10d_3rd_v087_signal

def f66cr_f66_cyclical_regime_proxies_calc088_5d_3rd_v088_signal(capex, revenue):
    res = ((capex / revenue).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc088_5d_3rd_v088_signal'] = f66cr_f66_cyclical_regime_proxies_calc088_5d_3rd_v088_signal

def f66cr_f66_cyclical_regime_proxies_calc089_10d_3rd_v089_signal(capex, revenue):
    res = ((capex / revenue).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc089_10d_3rd_v089_signal'] = f66cr_f66_cyclical_regime_proxies_calc089_10d_3rd_v089_signal

def f66cr_f66_cyclical_regime_proxies_calc090_21d_3rd_v090_signal(capex, revenue):
    res = ((capex / revenue).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc090_21d_3rd_v090_signal'] = f66cr_f66_cyclical_regime_proxies_calc090_21d_3rd_v090_signal

def f66cr_f66_cyclical_regime_proxies_calc091_42d_3rd_v091_signal(capex, revenue):
    res = ((capex / revenue).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc091_42d_3rd_v091_signal'] = f66cr_f66_cyclical_regime_proxies_calc091_42d_3rd_v091_signal

def f66cr_f66_cyclical_regime_proxies_calc092_63d_3rd_v092_signal(capex, revenue):
    res = ((capex / revenue).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc092_63d_3rd_v092_signal'] = f66cr_f66_cyclical_regime_proxies_calc092_63d_3rd_v092_signal

def f66cr_f66_cyclical_regime_proxies_calc093_126d_3rd_v093_signal(capex, revenue):
    res = ((capex / revenue).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc093_126d_3rd_v093_signal'] = f66cr_f66_cyclical_regime_proxies_calc093_126d_3rd_v093_signal

def f66cr_f66_cyclical_regime_proxies_calc094_252d_3rd_v094_signal(capex, revenue):
    res = ((capex / revenue).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc094_252d_3rd_v094_signal'] = f66cr_f66_cyclical_regime_proxies_calc094_252d_3rd_v094_signal

def f66cr_f66_cyclical_regime_proxies_calc095_21d_3rd_v095_signal(capex, revenue):
    res = ((capex / revenue).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc095_21d_3rd_v095_signal'] = f66cr_f66_cyclical_regime_proxies_calc095_21d_3rd_v095_signal

def f66cr_f66_cyclical_regime_proxies_calc096_63d_3rd_v096_signal(capex, revenue):
    res = ((capex / revenue).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc096_63d_3rd_v096_signal'] = f66cr_f66_cyclical_regime_proxies_calc096_63d_3rd_v096_signal

def f66cr_f66_cyclical_regime_proxies_calc097_5d_3rd_v097_signal(capex, revenue):
    res = ((capex / revenue).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc097_5d_3rd_v097_signal'] = f66cr_f66_cyclical_regime_proxies_calc097_5d_3rd_v097_signal

def f66cr_f66_cyclical_regime_proxies_calc098_21d_3rd_v098_signal(capex, revenue):
    res = ((capex / revenue).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc098_21d_3rd_v098_signal'] = f66cr_f66_cyclical_regime_proxies_calc098_21d_3rd_v098_signal

def f66cr_f66_cyclical_regime_proxies_calc099_10d_3rd_v099_signal(capex, revenue):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(capex / revenue)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc099_10d_3rd_v099_signal'] = f66cr_f66_cyclical_regime_proxies_calc099_10d_3rd_v099_signal

def f66cr_f66_cyclical_regime_proxies_calc100_5d_3rd_v100_signal(gp, assets):
    res = ((gp / assets).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc100_5d_3rd_v100_signal'] = f66cr_f66_cyclical_regime_proxies_calc100_5d_3rd_v100_signal

def f66cr_f66_cyclical_regime_proxies_calc101_10d_3rd_v101_signal(gp, assets):
    res = ((gp / assets).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc101_10d_3rd_v101_signal'] = f66cr_f66_cyclical_regime_proxies_calc101_10d_3rd_v101_signal

def f66cr_f66_cyclical_regime_proxies_calc102_21d_3rd_v102_signal(gp, assets):
    res = ((gp / assets).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc102_21d_3rd_v102_signal'] = f66cr_f66_cyclical_regime_proxies_calc102_21d_3rd_v102_signal

def f66cr_f66_cyclical_regime_proxies_calc103_42d_3rd_v103_signal(gp, assets):
    res = ((gp / assets).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc103_42d_3rd_v103_signal'] = f66cr_f66_cyclical_regime_proxies_calc103_42d_3rd_v103_signal

def f66cr_f66_cyclical_regime_proxies_calc104_63d_3rd_v104_signal(gp, assets):
    res = ((gp / assets).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc104_63d_3rd_v104_signal'] = f66cr_f66_cyclical_regime_proxies_calc104_63d_3rd_v104_signal

def f66cr_f66_cyclical_regime_proxies_calc105_126d_3rd_v105_signal(gp, assets):
    res = ((gp / assets).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc105_126d_3rd_v105_signal'] = f66cr_f66_cyclical_regime_proxies_calc105_126d_3rd_v105_signal

def f66cr_f66_cyclical_regime_proxies_calc106_252d_3rd_v106_signal(gp, assets):
    res = ((gp / assets).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc106_252d_3rd_v106_signal'] = f66cr_f66_cyclical_regime_proxies_calc106_252d_3rd_v106_signal

def f66cr_f66_cyclical_regime_proxies_calc107_21d_3rd_v107_signal(gp, assets):
    res = ((gp / assets).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc107_21d_3rd_v107_signal'] = f66cr_f66_cyclical_regime_proxies_calc107_21d_3rd_v107_signal

def f66cr_f66_cyclical_regime_proxies_calc108_63d_3rd_v108_signal(gp, assets):
    res = ((gp / assets).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc108_63d_3rd_v108_signal'] = f66cr_f66_cyclical_regime_proxies_calc108_63d_3rd_v108_signal

def f66cr_f66_cyclical_regime_proxies_calc109_5d_3rd_v109_signal(gp, assets):
    res = ((gp / assets).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc109_5d_3rd_v109_signal'] = f66cr_f66_cyclical_regime_proxies_calc109_5d_3rd_v109_signal

def f66cr_f66_cyclical_regime_proxies_calc110_21d_3rd_v110_signal(gp, assets):
    res = ((gp / assets).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc110_21d_3rd_v110_signal'] = f66cr_f66_cyclical_regime_proxies_calc110_21d_3rd_v110_signal

def f66cr_f66_cyclical_regime_proxies_calc111_10d_3rd_v111_signal(gp, assets):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(gp / assets)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc111_10d_3rd_v111_signal'] = f66cr_f66_cyclical_regime_proxies_calc111_10d_3rd_v111_signal

def f66cr_f66_cyclical_regime_proxies_calc112_5d_3rd_v112_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc112_5d_3rd_v112_signal'] = f66cr_f66_cyclical_regime_proxies_calc112_5d_3rd_v112_signal

def f66cr_f66_cyclical_regime_proxies_calc113_10d_3rd_v113_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc113_10d_3rd_v113_signal'] = f66cr_f66_cyclical_regime_proxies_calc113_10d_3rd_v113_signal

def f66cr_f66_cyclical_regime_proxies_calc114_21d_3rd_v114_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc114_21d_3rd_v114_signal'] = f66cr_f66_cyclical_regime_proxies_calc114_21d_3rd_v114_signal

def f66cr_f66_cyclical_regime_proxies_calc115_42d_3rd_v115_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc115_42d_3rd_v115_signal'] = f66cr_f66_cyclical_regime_proxies_calc115_42d_3rd_v115_signal

def f66cr_f66_cyclical_regime_proxies_calc116_63d_3rd_v116_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc116_63d_3rd_v116_signal'] = f66cr_f66_cyclical_regime_proxies_calc116_63d_3rd_v116_signal

def f66cr_f66_cyclical_regime_proxies_calc117_126d_3rd_v117_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc117_126d_3rd_v117_signal'] = f66cr_f66_cyclical_regime_proxies_calc117_126d_3rd_v117_signal

def f66cr_f66_cyclical_regime_proxies_calc118_252d_3rd_v118_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc118_252d_3rd_v118_signal'] = f66cr_f66_cyclical_regime_proxies_calc118_252d_3rd_v118_signal

def f66cr_f66_cyclical_regime_proxies_calc119_21d_3rd_v119_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc119_21d_3rd_v119_signal'] = f66cr_f66_cyclical_regime_proxies_calc119_21d_3rd_v119_signal

def f66cr_f66_cyclical_regime_proxies_calc120_63d_3rd_v120_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc120_63d_3rd_v120_signal'] = f66cr_f66_cyclical_regime_proxies_calc120_63d_3rd_v120_signal

def f66cr_f66_cyclical_regime_proxies_calc121_5d_3rd_v121_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc121_5d_3rd_v121_signal'] = f66cr_f66_cyclical_regime_proxies_calc121_5d_3rd_v121_signal

def f66cr_f66_cyclical_regime_proxies_calc122_21d_3rd_v122_signal(workingcapital, liabilities):
    res = ((workingcapital / liabilities).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc122_21d_3rd_v122_signal'] = f66cr_f66_cyclical_regime_proxies_calc122_21d_3rd_v122_signal

def f66cr_f66_cyclical_regime_proxies_calc123_10d_3rd_v123_signal(workingcapital, liabilities):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(workingcapital / liabilities)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc123_10d_3rd_v123_signal'] = f66cr_f66_cyclical_regime_proxies_calc123_10d_3rd_v123_signal

def f66cr_f66_cyclical_regime_proxies_calc124_5d_3rd_v124_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc124_5d_3rd_v124_signal'] = f66cr_f66_cyclical_regime_proxies_calc124_5d_3rd_v124_signal

def f66cr_f66_cyclical_regime_proxies_calc125_10d_3rd_v125_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc125_10d_3rd_v125_signal'] = f66cr_f66_cyclical_regime_proxies_calc125_10d_3rd_v125_signal

def f66cr_f66_cyclical_regime_proxies_calc126_21d_3rd_v126_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc126_21d_3rd_v126_signal'] = f66cr_f66_cyclical_regime_proxies_calc126_21d_3rd_v126_signal

def f66cr_f66_cyclical_regime_proxies_calc127_42d_3rd_v127_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc127_42d_3rd_v127_signal'] = f66cr_f66_cyclical_regime_proxies_calc127_42d_3rd_v127_signal

def f66cr_f66_cyclical_regime_proxies_calc128_63d_3rd_v128_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc128_63d_3rd_v128_signal'] = f66cr_f66_cyclical_regime_proxies_calc128_63d_3rd_v128_signal

def f66cr_f66_cyclical_regime_proxies_calc129_126d_3rd_v129_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc129_126d_3rd_v129_signal'] = f66cr_f66_cyclical_regime_proxies_calc129_126d_3rd_v129_signal

def f66cr_f66_cyclical_regime_proxies_calc130_252d_3rd_v130_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc130_252d_3rd_v130_signal'] = f66cr_f66_cyclical_regime_proxies_calc130_252d_3rd_v130_signal

def f66cr_f66_cyclical_regime_proxies_calc131_21d_3rd_v131_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc131_21d_3rd_v131_signal'] = f66cr_f66_cyclical_regime_proxies_calc131_21d_3rd_v131_signal

def f66cr_f66_cyclical_regime_proxies_calc132_63d_3rd_v132_signal(volume, sharesbas):
    res = ((volume / sharesbas).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc132_63d_3rd_v132_signal'] = f66cr_f66_cyclical_regime_proxies_calc132_63d_3rd_v132_signal

def f66cr_f66_cyclical_regime_proxies_calc133_5d_3rd_v133_signal(volume, sharesbas):
    res = ((volume / sharesbas).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc133_5d_3rd_v133_signal'] = f66cr_f66_cyclical_regime_proxies_calc133_5d_3rd_v133_signal

def f66cr_f66_cyclical_regime_proxies_calc134_21d_3rd_v134_signal(volume, sharesbas):
    res = ((volume / sharesbas).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc134_21d_3rd_v134_signal'] = f66cr_f66_cyclical_regime_proxies_calc134_21d_3rd_v134_signal

def f66cr_f66_cyclical_regime_proxies_calc135_10d_3rd_v135_signal(volume, sharesbas):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(volume / sharesbas)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc135_10d_3rd_v135_signal'] = f66cr_f66_cyclical_regime_proxies_calc135_10d_3rd_v135_signal

def f66cr_f66_cyclical_regime_proxies_calc136_5d_3rd_v136_signal(low, high):
    res = ((low / high).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc136_5d_3rd_v136_signal'] = f66cr_f66_cyclical_regime_proxies_calc136_5d_3rd_v136_signal

def f66cr_f66_cyclical_regime_proxies_calc137_10d_3rd_v137_signal(low, high):
    res = ((low / high).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc137_10d_3rd_v137_signal'] = f66cr_f66_cyclical_regime_proxies_calc137_10d_3rd_v137_signal

def f66cr_f66_cyclical_regime_proxies_calc138_21d_3rd_v138_signal(low, high):
    res = ((low / high).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc138_21d_3rd_v138_signal'] = f66cr_f66_cyclical_regime_proxies_calc138_21d_3rd_v138_signal

def f66cr_f66_cyclical_regime_proxies_calc139_42d_3rd_v139_signal(low, high):
    res = ((low / high).rolling(42).skew()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc139_42d_3rd_v139_signal'] = f66cr_f66_cyclical_regime_proxies_calc139_42d_3rd_v139_signal

def f66cr_f66_cyclical_regime_proxies_calc140_63d_3rd_v140_signal(low, high):
    res = ((low / high).rolling(63).kurt()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc140_63d_3rd_v140_signal'] = f66cr_f66_cyclical_regime_proxies_calc140_63d_3rd_v140_signal

def f66cr_f66_cyclical_regime_proxies_calc141_126d_3rd_v141_signal(low, high):
    res = ((low / high).rolling(126).max()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc141_126d_3rd_v141_signal'] = f66cr_f66_cyclical_regime_proxies_calc141_126d_3rd_v141_signal

def f66cr_f66_cyclical_regime_proxies_calc142_252d_3rd_v142_signal(low, high):
    res = ((low / high).rolling(252).min()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc142_252d_3rd_v142_signal'] = f66cr_f66_cyclical_regime_proxies_calc142_252d_3rd_v142_signal

def f66cr_f66_cyclical_regime_proxies_calc143_21d_3rd_v143_signal(low, high):
    res = ((low / high).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc143_21d_3rd_v143_signal'] = f66cr_f66_cyclical_regime_proxies_calc143_21d_3rd_v143_signal

def f66cr_f66_cyclical_regime_proxies_calc144_63d_3rd_v144_signal(low, high):
    res = ((low / high).rolling(63).rank()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc144_63d_3rd_v144_signal'] = f66cr_f66_cyclical_regime_proxies_calc144_63d_3rd_v144_signal

def f66cr_f66_cyclical_regime_proxies_calc145_5d_3rd_v145_signal(low, high):
    res = ((low / high).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc145_5d_3rd_v145_signal'] = f66cr_f66_cyclical_regime_proxies_calc145_5d_3rd_v145_signal

def f66cr_f66_cyclical_regime_proxies_calc146_21d_3rd_v146_signal(low, high):
    res = ((low / high).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc146_21d_3rd_v146_signal'] = f66cr_f66_cyclical_regime_proxies_calc146_21d_3rd_v146_signal

def f66cr_f66_cyclical_regime_proxies_calc147_10d_3rd_v147_signal(low, high):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(low / high)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc147_10d_3rd_v147_signal'] = f66cr_f66_cyclical_regime_proxies_calc147_10d_3rd_v147_signal

def f66cr_f66_cyclical_regime_proxies_calc148_5d_3rd_v148_signal(evebitda, ps):
    res = ((evebitda / ps).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc148_5d_3rd_v148_signal'] = f66cr_f66_cyclical_regime_proxies_calc148_5d_3rd_v148_signal

def f66cr_f66_cyclical_regime_proxies_calc149_10d_3rd_v149_signal(evebitda, ps):
    res = ((evebitda / ps).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc149_10d_3rd_v149_signal'] = f66cr_f66_cyclical_regime_proxies_calc149_10d_3rd_v149_signal

def f66cr_f66_cyclical_regime_proxies_calc150_21d_3rd_v150_signal(evebitda, ps):
    res = ((evebitda / ps).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc150_21d_3rd_v150_signal'] = f66cr_f66_cyclical_regime_proxies_calc150_21d_3rd_v150_signal


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
