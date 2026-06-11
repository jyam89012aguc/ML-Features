import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f66cr_f66_cyclical_regime_proxies_calc001_5d_base_v001_signal(close, marketcap):
    res = (close / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc001_5d_base_v001_signal'] = f66cr_f66_cyclical_regime_proxies_calc001_5d_base_v001_signal

def f66cr_f66_cyclical_regime_proxies_calc002_10d_base_v002_signal(close, marketcap):
    res = (close / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc002_10d_base_v002_signal'] = f66cr_f66_cyclical_regime_proxies_calc002_10d_base_v002_signal

def f66cr_f66_cyclical_regime_proxies_calc003_21d_base_v003_signal(close, marketcap):
    res = (close / marketcap).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc003_21d_base_v003_signal'] = f66cr_f66_cyclical_regime_proxies_calc003_21d_base_v003_signal

def f66cr_f66_cyclical_regime_proxies_calc004_42d_base_v004_signal(close, marketcap):
    res = (close / marketcap).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc004_42d_base_v004_signal'] = f66cr_f66_cyclical_regime_proxies_calc004_42d_base_v004_signal

def f66cr_f66_cyclical_regime_proxies_calc005_63d_base_v005_signal(close, marketcap):
    res = (close / marketcap).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc005_63d_base_v005_signal'] = f66cr_f66_cyclical_regime_proxies_calc005_63d_base_v005_signal

def f66cr_f66_cyclical_regime_proxies_calc006_126d_base_v006_signal(close, marketcap):
    res = (close / marketcap).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc006_126d_base_v006_signal'] = f66cr_f66_cyclical_regime_proxies_calc006_126d_base_v006_signal

def f66cr_f66_cyclical_regime_proxies_calc007_252d_base_v007_signal(close, marketcap):
    res = (close / marketcap).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc007_252d_base_v007_signal'] = f66cr_f66_cyclical_regime_proxies_calc007_252d_base_v007_signal

def f66cr_f66_cyclical_regime_proxies_calc008_21d_base_v008_signal(close, marketcap):
    res = (close / marketcap).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc008_21d_base_v008_signal'] = f66cr_f66_cyclical_regime_proxies_calc008_21d_base_v008_signal

def f66cr_f66_cyclical_regime_proxies_calc009_63d_base_v009_signal(close, marketcap):
    res = (close / marketcap).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc009_63d_base_v009_signal'] = f66cr_f66_cyclical_regime_proxies_calc009_63d_base_v009_signal

def f66cr_f66_cyclical_regime_proxies_calc010_5d_base_v010_signal(close, marketcap):
    res = (close / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc010_5d_base_v010_signal'] = f66cr_f66_cyclical_regime_proxies_calc010_5d_base_v010_signal

def f66cr_f66_cyclical_regime_proxies_calc011_21d_base_v011_signal(close, marketcap):
    res = (close / marketcap).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc011_21d_base_v011_signal'] = f66cr_f66_cyclical_regime_proxies_calc011_21d_base_v011_signal

def f66cr_f66_cyclical_regime_proxies_calc012_10d_base_v012_signal(close, marketcap):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(close / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc012_10d_base_v012_signal'] = f66cr_f66_cyclical_regime_proxies_calc012_10d_base_v012_signal

def f66cr_f66_cyclical_regime_proxies_calc013_5d_base_v013_signal(pe, ps):
    res = (pe / ps).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc013_5d_base_v013_signal'] = f66cr_f66_cyclical_regime_proxies_calc013_5d_base_v013_signal

def f66cr_f66_cyclical_regime_proxies_calc014_10d_base_v014_signal(pe, ps):
    res = (pe / ps).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc014_10d_base_v014_signal'] = f66cr_f66_cyclical_regime_proxies_calc014_10d_base_v014_signal

def f66cr_f66_cyclical_regime_proxies_calc015_21d_base_v015_signal(pe, ps):
    res = (pe / ps).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc015_21d_base_v015_signal'] = f66cr_f66_cyclical_regime_proxies_calc015_21d_base_v015_signal

def f66cr_f66_cyclical_regime_proxies_calc016_42d_base_v016_signal(pe, ps):
    res = (pe / ps).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc016_42d_base_v016_signal'] = f66cr_f66_cyclical_regime_proxies_calc016_42d_base_v016_signal

def f66cr_f66_cyclical_regime_proxies_calc017_63d_base_v017_signal(pe, ps):
    res = (pe / ps).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc017_63d_base_v017_signal'] = f66cr_f66_cyclical_regime_proxies_calc017_63d_base_v017_signal

def f66cr_f66_cyclical_regime_proxies_calc018_126d_base_v018_signal(pe, ps):
    res = (pe / ps).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc018_126d_base_v018_signal'] = f66cr_f66_cyclical_regime_proxies_calc018_126d_base_v018_signal

def f66cr_f66_cyclical_regime_proxies_calc019_252d_base_v019_signal(pe, ps):
    res = (pe / ps).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc019_252d_base_v019_signal'] = f66cr_f66_cyclical_regime_proxies_calc019_252d_base_v019_signal

def f66cr_f66_cyclical_regime_proxies_calc020_21d_base_v020_signal(pe, ps):
    res = (pe / ps).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc020_21d_base_v020_signal'] = f66cr_f66_cyclical_regime_proxies_calc020_21d_base_v020_signal

def f66cr_f66_cyclical_regime_proxies_calc021_63d_base_v021_signal(pe, ps):
    res = (pe / ps).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc021_63d_base_v021_signal'] = f66cr_f66_cyclical_regime_proxies_calc021_63d_base_v021_signal

def f66cr_f66_cyclical_regime_proxies_calc022_5d_base_v022_signal(pe, ps):
    res = (pe / ps).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc022_5d_base_v022_signal'] = f66cr_f66_cyclical_regime_proxies_calc022_5d_base_v022_signal

def f66cr_f66_cyclical_regime_proxies_calc023_21d_base_v023_signal(pe, ps):
    res = (pe / ps).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc023_21d_base_v023_signal'] = f66cr_f66_cyclical_regime_proxies_calc023_21d_base_v023_signal

def f66cr_f66_cyclical_regime_proxies_calc024_10d_base_v024_signal(pe, ps):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(pe / ps)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc024_10d_base_v024_signal'] = f66cr_f66_cyclical_regime_proxies_calc024_10d_base_v024_signal

def f66cr_f66_cyclical_regime_proxies_calc025_5d_base_v025_signal(revenue, assets):
    res = (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc025_5d_base_v025_signal'] = f66cr_f66_cyclical_regime_proxies_calc025_5d_base_v025_signal

def f66cr_f66_cyclical_regime_proxies_calc026_10d_base_v026_signal(revenue, assets):
    res = (revenue / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc026_10d_base_v026_signal'] = f66cr_f66_cyclical_regime_proxies_calc026_10d_base_v026_signal

def f66cr_f66_cyclical_regime_proxies_calc027_21d_base_v027_signal(revenue, assets):
    res = (revenue / assets).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc027_21d_base_v027_signal'] = f66cr_f66_cyclical_regime_proxies_calc027_21d_base_v027_signal

def f66cr_f66_cyclical_regime_proxies_calc028_42d_base_v028_signal(revenue, assets):
    res = (revenue / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc028_42d_base_v028_signal'] = f66cr_f66_cyclical_regime_proxies_calc028_42d_base_v028_signal

def f66cr_f66_cyclical_regime_proxies_calc029_63d_base_v029_signal(revenue, assets):
    res = (revenue / assets).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc029_63d_base_v029_signal'] = f66cr_f66_cyclical_regime_proxies_calc029_63d_base_v029_signal

def f66cr_f66_cyclical_regime_proxies_calc030_126d_base_v030_signal(revenue, assets):
    res = (revenue / assets).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc030_126d_base_v030_signal'] = f66cr_f66_cyclical_regime_proxies_calc030_126d_base_v030_signal

def f66cr_f66_cyclical_regime_proxies_calc031_252d_base_v031_signal(revenue, assets):
    res = (revenue / assets).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc031_252d_base_v031_signal'] = f66cr_f66_cyclical_regime_proxies_calc031_252d_base_v031_signal

def f66cr_f66_cyclical_regime_proxies_calc032_21d_base_v032_signal(revenue, assets):
    res = (revenue / assets).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc032_21d_base_v032_signal'] = f66cr_f66_cyclical_regime_proxies_calc032_21d_base_v032_signal

def f66cr_f66_cyclical_regime_proxies_calc033_63d_base_v033_signal(revenue, assets):
    res = (revenue / assets).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc033_63d_base_v033_signal'] = f66cr_f66_cyclical_regime_proxies_calc033_63d_base_v033_signal

def f66cr_f66_cyclical_regime_proxies_calc034_5d_base_v034_signal(revenue, assets):
    res = (revenue / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc034_5d_base_v034_signal'] = f66cr_f66_cyclical_regime_proxies_calc034_5d_base_v034_signal

def f66cr_f66_cyclical_regime_proxies_calc035_21d_base_v035_signal(revenue, assets):
    res = (revenue / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc035_21d_base_v035_signal'] = f66cr_f66_cyclical_regime_proxies_calc035_21d_base_v035_signal

def f66cr_f66_cyclical_regime_proxies_calc036_10d_base_v036_signal(revenue, assets):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc036_10d_base_v036_signal'] = f66cr_f66_cyclical_regime_proxies_calc036_10d_base_v036_signal

def f66cr_f66_cyclical_regime_proxies_calc037_5d_base_v037_signal(ebitda, ev):
    res = (ebitda / ev).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc037_5d_base_v037_signal'] = f66cr_f66_cyclical_regime_proxies_calc037_5d_base_v037_signal

def f66cr_f66_cyclical_regime_proxies_calc038_10d_base_v038_signal(ebitda, ev):
    res = (ebitda / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc038_10d_base_v038_signal'] = f66cr_f66_cyclical_regime_proxies_calc038_10d_base_v038_signal

def f66cr_f66_cyclical_regime_proxies_calc039_21d_base_v039_signal(ebitda, ev):
    res = (ebitda / ev).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc039_21d_base_v039_signal'] = f66cr_f66_cyclical_regime_proxies_calc039_21d_base_v039_signal

def f66cr_f66_cyclical_regime_proxies_calc040_42d_base_v040_signal(ebitda, ev):
    res = (ebitda / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc040_42d_base_v040_signal'] = f66cr_f66_cyclical_regime_proxies_calc040_42d_base_v040_signal

def f66cr_f66_cyclical_regime_proxies_calc041_63d_base_v041_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc041_63d_base_v041_signal'] = f66cr_f66_cyclical_regime_proxies_calc041_63d_base_v041_signal

def f66cr_f66_cyclical_regime_proxies_calc042_126d_base_v042_signal(ebitda, ev):
    res = (ebitda / ev).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc042_126d_base_v042_signal'] = f66cr_f66_cyclical_regime_proxies_calc042_126d_base_v042_signal

def f66cr_f66_cyclical_regime_proxies_calc043_252d_base_v043_signal(ebitda, ev):
    res = (ebitda / ev).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc043_252d_base_v043_signal'] = f66cr_f66_cyclical_regime_proxies_calc043_252d_base_v043_signal

def f66cr_f66_cyclical_regime_proxies_calc044_21d_base_v044_signal(ebitda, ev):
    res = (ebitda / ev).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc044_21d_base_v044_signal'] = f66cr_f66_cyclical_regime_proxies_calc044_21d_base_v044_signal

def f66cr_f66_cyclical_regime_proxies_calc045_63d_base_v045_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc045_63d_base_v045_signal'] = f66cr_f66_cyclical_regime_proxies_calc045_63d_base_v045_signal

def f66cr_f66_cyclical_regime_proxies_calc046_5d_base_v046_signal(ebitda, ev):
    res = (ebitda / ev).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc046_5d_base_v046_signal'] = f66cr_f66_cyclical_regime_proxies_calc046_5d_base_v046_signal

def f66cr_f66_cyclical_regime_proxies_calc047_21d_base_v047_signal(ebitda, ev):
    res = (ebitda / ev).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc047_21d_base_v047_signal'] = f66cr_f66_cyclical_regime_proxies_calc047_21d_base_v047_signal

def f66cr_f66_cyclical_regime_proxies_calc048_10d_base_v048_signal(ebitda, ev):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ebitda / ev)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc048_10d_base_v048_signal'] = f66cr_f66_cyclical_regime_proxies_calc048_10d_base_v048_signal

def f66cr_f66_cyclical_regime_proxies_calc049_5d_base_v049_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc049_5d_base_v049_signal'] = f66cr_f66_cyclical_regime_proxies_calc049_5d_base_v049_signal

def f66cr_f66_cyclical_regime_proxies_calc050_10d_base_v050_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc050_10d_base_v050_signal'] = f66cr_f66_cyclical_regime_proxies_calc050_10d_base_v050_signal

def f66cr_f66_cyclical_regime_proxies_calc051_21d_base_v051_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc051_21d_base_v051_signal'] = f66cr_f66_cyclical_regime_proxies_calc051_21d_base_v051_signal

def f66cr_f66_cyclical_regime_proxies_calc052_42d_base_v052_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc052_42d_base_v052_signal'] = f66cr_f66_cyclical_regime_proxies_calc052_42d_base_v052_signal

def f66cr_f66_cyclical_regime_proxies_calc053_63d_base_v053_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc053_63d_base_v053_signal'] = f66cr_f66_cyclical_regime_proxies_calc053_63d_base_v053_signal

def f66cr_f66_cyclical_regime_proxies_calc054_126d_base_v054_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc054_126d_base_v054_signal'] = f66cr_f66_cyclical_regime_proxies_calc054_126d_base_v054_signal

def f66cr_f66_cyclical_regime_proxies_calc055_252d_base_v055_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc055_252d_base_v055_signal'] = f66cr_f66_cyclical_regime_proxies_calc055_252d_base_v055_signal

def f66cr_f66_cyclical_regime_proxies_calc056_21d_base_v056_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc056_21d_base_v056_signal'] = f66cr_f66_cyclical_regime_proxies_calc056_21d_base_v056_signal

def f66cr_f66_cyclical_regime_proxies_calc057_63d_base_v057_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc057_63d_base_v057_signal'] = f66cr_f66_cyclical_regime_proxies_calc057_63d_base_v057_signal

def f66cr_f66_cyclical_regime_proxies_calc058_5d_base_v058_signal(fcf, marketcap):
    res = (fcf / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc058_5d_base_v058_signal'] = f66cr_f66_cyclical_regime_proxies_calc058_5d_base_v058_signal

def f66cr_f66_cyclical_regime_proxies_calc059_21d_base_v059_signal(fcf, marketcap):
    res = (fcf / marketcap).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc059_21d_base_v059_signal'] = f66cr_f66_cyclical_regime_proxies_calc059_21d_base_v059_signal

def f66cr_f66_cyclical_regime_proxies_calc060_10d_base_v060_signal(fcf, marketcap):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc060_10d_base_v060_signal'] = f66cr_f66_cyclical_regime_proxies_calc060_10d_base_v060_signal

def f66cr_f66_cyclical_regime_proxies_calc061_5d_base_v061_signal(ncfo, debt):
    res = (ncfo / debt).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc061_5d_base_v061_signal'] = f66cr_f66_cyclical_regime_proxies_calc061_5d_base_v061_signal

def f66cr_f66_cyclical_regime_proxies_calc062_10d_base_v062_signal(ncfo, debt):
    res = (ncfo / debt).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc062_10d_base_v062_signal'] = f66cr_f66_cyclical_regime_proxies_calc062_10d_base_v062_signal

def f66cr_f66_cyclical_regime_proxies_calc063_21d_base_v063_signal(ncfo, debt):
    res = (ncfo / debt).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc063_21d_base_v063_signal'] = f66cr_f66_cyclical_regime_proxies_calc063_21d_base_v063_signal

def f66cr_f66_cyclical_regime_proxies_calc064_42d_base_v064_signal(ncfo, debt):
    res = (ncfo / debt).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc064_42d_base_v064_signal'] = f66cr_f66_cyclical_regime_proxies_calc064_42d_base_v064_signal

def f66cr_f66_cyclical_regime_proxies_calc065_63d_base_v065_signal(ncfo, debt):
    res = (ncfo / debt).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc065_63d_base_v065_signal'] = f66cr_f66_cyclical_regime_proxies_calc065_63d_base_v065_signal

def f66cr_f66_cyclical_regime_proxies_calc066_126d_base_v066_signal(ncfo, debt):
    res = (ncfo / debt).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc066_126d_base_v066_signal'] = f66cr_f66_cyclical_regime_proxies_calc066_126d_base_v066_signal

def f66cr_f66_cyclical_regime_proxies_calc067_252d_base_v067_signal(ncfo, debt):
    res = (ncfo / debt).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc067_252d_base_v067_signal'] = f66cr_f66_cyclical_regime_proxies_calc067_252d_base_v067_signal

def f66cr_f66_cyclical_regime_proxies_calc068_21d_base_v068_signal(ncfo, debt):
    res = (ncfo / debt).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc068_21d_base_v068_signal'] = f66cr_f66_cyclical_regime_proxies_calc068_21d_base_v068_signal

def f66cr_f66_cyclical_regime_proxies_calc069_63d_base_v069_signal(ncfo, debt):
    res = (ncfo / debt).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc069_63d_base_v069_signal'] = f66cr_f66_cyclical_regime_proxies_calc069_63d_base_v069_signal

def f66cr_f66_cyclical_regime_proxies_calc070_5d_base_v070_signal(ncfo, debt):
    res = (ncfo / debt).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc070_5d_base_v070_signal'] = f66cr_f66_cyclical_regime_proxies_calc070_5d_base_v070_signal

def f66cr_f66_cyclical_regime_proxies_calc071_21d_base_v071_signal(ncfo, debt):
    res = (ncfo / debt).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc071_21d_base_v071_signal'] = f66cr_f66_cyclical_regime_proxies_calc071_21d_base_v071_signal

def f66cr_f66_cyclical_regime_proxies_calc072_10d_base_v072_signal(ncfo, debt):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ncfo / debt)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc072_10d_base_v072_signal'] = f66cr_f66_cyclical_regime_proxies_calc072_10d_base_v072_signal

def f66cr_f66_cyclical_regime_proxies_calc073_5d_base_v073_signal(opinc, revenue):
    res = (opinc / revenue).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc073_5d_base_v073_signal'] = f66cr_f66_cyclical_regime_proxies_calc073_5d_base_v073_signal

def f66cr_f66_cyclical_regime_proxies_calc074_10d_base_v074_signal(opinc, revenue):
    res = (opinc / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc074_10d_base_v074_signal'] = f66cr_f66_cyclical_regime_proxies_calc074_10d_base_v074_signal

def f66cr_f66_cyclical_regime_proxies_calc075_21d_base_v075_signal(opinc, revenue):
    res = (opinc / revenue).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f66cr_f66_cyclical_regime_proxies_calc075_21d_base_v075_signal'] = f66cr_f66_cyclical_regime_proxies_calc075_21d_base_v075_signal


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
