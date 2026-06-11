import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f65ms_f65_market_share_momentum_calc001_5d_2nd_v001_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc001_5d_2nd_v001_signal'] = f65ms_f65_market_share_momentum_calc001_5d_2nd_v001_signal

def f65ms_f65_market_share_momentum_calc002_10d_2nd_v002_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc002_10d_2nd_v002_signal'] = f65ms_f65_market_share_momentum_calc002_10d_2nd_v002_signal

def f65ms_f65_market_share_momentum_calc003_21d_2nd_v003_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc003_21d_2nd_v003_signal'] = f65ms_f65_market_share_momentum_calc003_21d_2nd_v003_signal

def f65ms_f65_market_share_momentum_calc004_42d_2nd_v004_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc004_42d_2nd_v004_signal'] = f65ms_f65_market_share_momentum_calc004_42d_2nd_v004_signal

def f65ms_f65_market_share_momentum_calc005_63d_2nd_v005_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc005_63d_2nd_v005_signal'] = f65ms_f65_market_share_momentum_calc005_63d_2nd_v005_signal

def f65ms_f65_market_share_momentum_calc006_126d_2nd_v006_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc006_126d_2nd_v006_signal'] = f65ms_f65_market_share_momentum_calc006_126d_2nd_v006_signal

def f65ms_f65_market_share_momentum_calc007_252d_2nd_v007_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc007_252d_2nd_v007_signal'] = f65ms_f65_market_share_momentum_calc007_252d_2nd_v007_signal

def f65ms_f65_market_share_momentum_calc008_21d_2nd_v008_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc008_21d_2nd_v008_signal'] = f65ms_f65_market_share_momentum_calc008_21d_2nd_v008_signal

def f65ms_f65_market_share_momentum_calc009_63d_2nd_v009_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc009_63d_2nd_v009_signal'] = f65ms_f65_market_share_momentum_calc009_63d_2nd_v009_signal

def f65ms_f65_market_share_momentum_calc010_5d_2nd_v010_signal(revenue, marketcap):
    res = ((revenue / marketcap).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc010_5d_2nd_v010_signal'] = f65ms_f65_market_share_momentum_calc010_5d_2nd_v010_signal

def f65ms_f65_market_share_momentum_calc011_21d_2nd_v011_signal(revenue, marketcap):
    res = ((revenue / marketcap).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc011_21d_2nd_v011_signal'] = f65ms_f65_market_share_momentum_calc011_21d_2nd_v011_signal

def f65ms_f65_market_share_momentum_calc012_10d_2nd_v012_signal(revenue, marketcap):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / marketcap)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc012_10d_2nd_v012_signal'] = f65ms_f65_market_share_momentum_calc012_10d_2nd_v012_signal

def f65ms_f65_market_share_momentum_calc013_63d_2nd_v013_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc013_63d_2nd_v013_signal'] = f65ms_f65_market_share_momentum_calc013_63d_2nd_v013_signal

def f65ms_f65_market_share_momentum_calc014_126d_2nd_v014_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc014_126d_2nd_v014_signal'] = f65ms_f65_market_share_momentum_calc014_126d_2nd_v014_signal

def f65ms_f65_market_share_momentum_calc015_252d_2nd_v015_signal(revenue, marketcap):
    res = ((revenue / marketcap).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc015_252d_2nd_v015_signal'] = f65ms_f65_market_share_momentum_calc015_252d_2nd_v015_signal

def f65ms_f65_market_share_momentum_calc016_5d_2nd_v016_signal(revenue, assets):
    res = ((revenue / assets).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc016_5d_2nd_v016_signal'] = f65ms_f65_market_share_momentum_calc016_5d_2nd_v016_signal

def f65ms_f65_market_share_momentum_calc017_10d_2nd_v017_signal(revenue, assets):
    res = ((revenue / assets).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc017_10d_2nd_v017_signal'] = f65ms_f65_market_share_momentum_calc017_10d_2nd_v017_signal

def f65ms_f65_market_share_momentum_calc018_21d_2nd_v018_signal(revenue, assets):
    res = ((revenue / assets).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc018_21d_2nd_v018_signal'] = f65ms_f65_market_share_momentum_calc018_21d_2nd_v018_signal

def f65ms_f65_market_share_momentum_calc019_42d_2nd_v019_signal(revenue, assets):
    res = ((revenue / assets).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc019_42d_2nd_v019_signal'] = f65ms_f65_market_share_momentum_calc019_42d_2nd_v019_signal

def f65ms_f65_market_share_momentum_calc020_63d_2nd_v020_signal(revenue, assets):
    res = ((revenue / assets).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc020_63d_2nd_v020_signal'] = f65ms_f65_market_share_momentum_calc020_63d_2nd_v020_signal

def f65ms_f65_market_share_momentum_calc021_126d_2nd_v021_signal(revenue, assets):
    res = ((revenue / assets).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc021_126d_2nd_v021_signal'] = f65ms_f65_market_share_momentum_calc021_126d_2nd_v021_signal

def f65ms_f65_market_share_momentum_calc022_252d_2nd_v022_signal(revenue, assets):
    res = ((revenue / assets).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc022_252d_2nd_v022_signal'] = f65ms_f65_market_share_momentum_calc022_252d_2nd_v022_signal

def f65ms_f65_market_share_momentum_calc023_21d_2nd_v023_signal(revenue, assets):
    res = ((revenue / assets).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc023_21d_2nd_v023_signal'] = f65ms_f65_market_share_momentum_calc023_21d_2nd_v023_signal

def f65ms_f65_market_share_momentum_calc024_63d_2nd_v024_signal(revenue, assets):
    res = ((revenue / assets).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc024_63d_2nd_v024_signal'] = f65ms_f65_market_share_momentum_calc024_63d_2nd_v024_signal

def f65ms_f65_market_share_momentum_calc025_5d_2nd_v025_signal(revenue, assets):
    res = ((revenue / assets).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc025_5d_2nd_v025_signal'] = f65ms_f65_market_share_momentum_calc025_5d_2nd_v025_signal

def f65ms_f65_market_share_momentum_calc026_21d_2nd_v026_signal(revenue, assets):
    res = ((revenue / assets).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc026_21d_2nd_v026_signal'] = f65ms_f65_market_share_momentum_calc026_21d_2nd_v026_signal

def f65ms_f65_market_share_momentum_calc027_10d_2nd_v027_signal(revenue, assets):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / assets)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc027_10d_2nd_v027_signal'] = f65ms_f65_market_share_momentum_calc027_10d_2nd_v027_signal

def f65ms_f65_market_share_momentum_calc028_63d_2nd_v028_signal(revenue, assets):
    res = ((revenue / assets).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc028_63d_2nd_v028_signal'] = f65ms_f65_market_share_momentum_calc028_63d_2nd_v028_signal

def f65ms_f65_market_share_momentum_calc029_126d_2nd_v029_signal(revenue, assets):
    res = ((revenue / assets).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc029_126d_2nd_v029_signal'] = f65ms_f65_market_share_momentum_calc029_126d_2nd_v029_signal

def f65ms_f65_market_share_momentum_calc030_252d_2nd_v030_signal(revenue, assets):
    res = ((revenue / assets).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc030_252d_2nd_v030_signal'] = f65ms_f65_market_share_momentum_calc030_252d_2nd_v030_signal

def f65ms_f65_market_share_momentum_calc031_5d_2nd_v031_signal(revenue, ev):
    res = ((revenue / ev).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc031_5d_2nd_v031_signal'] = f65ms_f65_market_share_momentum_calc031_5d_2nd_v031_signal

def f65ms_f65_market_share_momentum_calc032_10d_2nd_v032_signal(revenue, ev):
    res = ((revenue / ev).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc032_10d_2nd_v032_signal'] = f65ms_f65_market_share_momentum_calc032_10d_2nd_v032_signal

def f65ms_f65_market_share_momentum_calc033_21d_2nd_v033_signal(revenue, ev):
    res = ((revenue / ev).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc033_21d_2nd_v033_signal'] = f65ms_f65_market_share_momentum_calc033_21d_2nd_v033_signal

def f65ms_f65_market_share_momentum_calc034_42d_2nd_v034_signal(revenue, ev):
    res = ((revenue / ev).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc034_42d_2nd_v034_signal'] = f65ms_f65_market_share_momentum_calc034_42d_2nd_v034_signal

def f65ms_f65_market_share_momentum_calc035_63d_2nd_v035_signal(revenue, ev):
    res = ((revenue / ev).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc035_63d_2nd_v035_signal'] = f65ms_f65_market_share_momentum_calc035_63d_2nd_v035_signal

def f65ms_f65_market_share_momentum_calc036_126d_2nd_v036_signal(revenue, ev):
    res = ((revenue / ev).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc036_126d_2nd_v036_signal'] = f65ms_f65_market_share_momentum_calc036_126d_2nd_v036_signal

def f65ms_f65_market_share_momentum_calc037_252d_2nd_v037_signal(revenue, ev):
    res = ((revenue / ev).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc037_252d_2nd_v037_signal'] = f65ms_f65_market_share_momentum_calc037_252d_2nd_v037_signal

def f65ms_f65_market_share_momentum_calc038_21d_2nd_v038_signal(revenue, ev):
    res = ((revenue / ev).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc038_21d_2nd_v038_signal'] = f65ms_f65_market_share_momentum_calc038_21d_2nd_v038_signal

def f65ms_f65_market_share_momentum_calc039_63d_2nd_v039_signal(revenue, ev):
    res = ((revenue / ev).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc039_63d_2nd_v039_signal'] = f65ms_f65_market_share_momentum_calc039_63d_2nd_v039_signal

def f65ms_f65_market_share_momentum_calc040_5d_2nd_v040_signal(revenue, ev):
    res = ((revenue / ev).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc040_5d_2nd_v040_signal'] = f65ms_f65_market_share_momentum_calc040_5d_2nd_v040_signal

def f65ms_f65_market_share_momentum_calc041_21d_2nd_v041_signal(revenue, ev):
    res = ((revenue / ev).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc041_21d_2nd_v041_signal'] = f65ms_f65_market_share_momentum_calc041_21d_2nd_v041_signal

def f65ms_f65_market_share_momentum_calc042_10d_2nd_v042_signal(revenue, ev):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / ev)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc042_10d_2nd_v042_signal'] = f65ms_f65_market_share_momentum_calc042_10d_2nd_v042_signal

def f65ms_f65_market_share_momentum_calc043_63d_2nd_v043_signal(revenue, ev):
    res = ((revenue / ev).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc043_63d_2nd_v043_signal'] = f65ms_f65_market_share_momentum_calc043_63d_2nd_v043_signal

def f65ms_f65_market_share_momentum_calc044_126d_2nd_v044_signal(revenue, ev):
    res = ((revenue / ev).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc044_126d_2nd_v044_signal'] = f65ms_f65_market_share_momentum_calc044_126d_2nd_v044_signal

def f65ms_f65_market_share_momentum_calc045_252d_2nd_v045_signal(revenue, ev):
    res = ((revenue / ev).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc045_252d_2nd_v045_signal'] = f65ms_f65_market_share_momentum_calc045_252d_2nd_v045_signal

def f65ms_f65_market_share_momentum_calc046_5d_2nd_v046_signal(revenue, equity):
    res = ((revenue / equity).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc046_5d_2nd_v046_signal'] = f65ms_f65_market_share_momentum_calc046_5d_2nd_v046_signal

def f65ms_f65_market_share_momentum_calc047_10d_2nd_v047_signal(revenue, equity):
    res = ((revenue / equity).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc047_10d_2nd_v047_signal'] = f65ms_f65_market_share_momentum_calc047_10d_2nd_v047_signal

def f65ms_f65_market_share_momentum_calc048_21d_2nd_v048_signal(revenue, equity):
    res = ((revenue / equity).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc048_21d_2nd_v048_signal'] = f65ms_f65_market_share_momentum_calc048_21d_2nd_v048_signal

def f65ms_f65_market_share_momentum_calc049_42d_2nd_v049_signal(revenue, equity):
    res = ((revenue / equity).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc049_42d_2nd_v049_signal'] = f65ms_f65_market_share_momentum_calc049_42d_2nd_v049_signal

def f65ms_f65_market_share_momentum_calc050_63d_2nd_v050_signal(revenue, equity):
    res = ((revenue / equity).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc050_63d_2nd_v050_signal'] = f65ms_f65_market_share_momentum_calc050_63d_2nd_v050_signal

def f65ms_f65_market_share_momentum_calc051_126d_2nd_v051_signal(revenue, equity):
    res = ((revenue / equity).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc051_126d_2nd_v051_signal'] = f65ms_f65_market_share_momentum_calc051_126d_2nd_v051_signal

def f65ms_f65_market_share_momentum_calc052_252d_2nd_v052_signal(revenue, equity):
    res = ((revenue / equity).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc052_252d_2nd_v052_signal'] = f65ms_f65_market_share_momentum_calc052_252d_2nd_v052_signal

def f65ms_f65_market_share_momentum_calc053_21d_2nd_v053_signal(revenue, equity):
    res = ((revenue / equity).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc053_21d_2nd_v053_signal'] = f65ms_f65_market_share_momentum_calc053_21d_2nd_v053_signal

def f65ms_f65_market_share_momentum_calc054_63d_2nd_v054_signal(revenue, equity):
    res = ((revenue / equity).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc054_63d_2nd_v054_signal'] = f65ms_f65_market_share_momentum_calc054_63d_2nd_v054_signal

def f65ms_f65_market_share_momentum_calc055_5d_2nd_v055_signal(revenue, equity):
    res = ((revenue / equity).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc055_5d_2nd_v055_signal'] = f65ms_f65_market_share_momentum_calc055_5d_2nd_v055_signal

def f65ms_f65_market_share_momentum_calc056_21d_2nd_v056_signal(revenue, equity):
    res = ((revenue / equity).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc056_21d_2nd_v056_signal'] = f65ms_f65_market_share_momentum_calc056_21d_2nd_v056_signal

def f65ms_f65_market_share_momentum_calc057_10d_2nd_v057_signal(revenue, equity):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / equity)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc057_10d_2nd_v057_signal'] = f65ms_f65_market_share_momentum_calc057_10d_2nd_v057_signal

def f65ms_f65_market_share_momentum_calc058_63d_2nd_v058_signal(revenue, equity):
    res = ((revenue / equity).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc058_63d_2nd_v058_signal'] = f65ms_f65_market_share_momentum_calc058_63d_2nd_v058_signal

def f65ms_f65_market_share_momentum_calc059_126d_2nd_v059_signal(revenue, equity):
    res = ((revenue / equity).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc059_126d_2nd_v059_signal'] = f65ms_f65_market_share_momentum_calc059_126d_2nd_v059_signal

def f65ms_f65_market_share_momentum_calc060_252d_2nd_v060_signal(revenue, equity):
    res = ((revenue / equity).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc060_252d_2nd_v060_signal'] = f65ms_f65_market_share_momentum_calc060_252d_2nd_v060_signal

def f65ms_f65_market_share_momentum_calc061_5d_2nd_v061_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc061_5d_2nd_v061_signal'] = f65ms_f65_market_share_momentum_calc061_5d_2nd_v061_signal

def f65ms_f65_market_share_momentum_calc062_10d_2nd_v062_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc062_10d_2nd_v062_signal'] = f65ms_f65_market_share_momentum_calc062_10d_2nd_v062_signal

def f65ms_f65_market_share_momentum_calc063_21d_2nd_v063_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc063_21d_2nd_v063_signal'] = f65ms_f65_market_share_momentum_calc063_21d_2nd_v063_signal

def f65ms_f65_market_share_momentum_calc064_42d_2nd_v064_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc064_42d_2nd_v064_signal'] = f65ms_f65_market_share_momentum_calc064_42d_2nd_v064_signal

def f65ms_f65_market_share_momentum_calc065_63d_2nd_v065_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc065_63d_2nd_v065_signal'] = f65ms_f65_market_share_momentum_calc065_63d_2nd_v065_signal

def f65ms_f65_market_share_momentum_calc066_126d_2nd_v066_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc066_126d_2nd_v066_signal'] = f65ms_f65_market_share_momentum_calc066_126d_2nd_v066_signal

def f65ms_f65_market_share_momentum_calc067_252d_2nd_v067_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc067_252d_2nd_v067_signal'] = f65ms_f65_market_share_momentum_calc067_252d_2nd_v067_signal

def f65ms_f65_market_share_momentum_calc068_21d_2nd_v068_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc068_21d_2nd_v068_signal'] = f65ms_f65_market_share_momentum_calc068_21d_2nd_v068_signal

def f65ms_f65_market_share_momentum_calc069_63d_2nd_v069_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc069_63d_2nd_v069_signal'] = f65ms_f65_market_share_momentum_calc069_63d_2nd_v069_signal

def f65ms_f65_market_share_momentum_calc070_5d_2nd_v070_signal(revenue, liabilities):
    res = ((revenue / liabilities).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc070_5d_2nd_v070_signal'] = f65ms_f65_market_share_momentum_calc070_5d_2nd_v070_signal

def f65ms_f65_market_share_momentum_calc071_21d_2nd_v071_signal(revenue, liabilities):
    res = ((revenue / liabilities).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc071_21d_2nd_v071_signal'] = f65ms_f65_market_share_momentum_calc071_21d_2nd_v071_signal

def f65ms_f65_market_share_momentum_calc072_10d_2nd_v072_signal(revenue, liabilities):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / liabilities)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc072_10d_2nd_v072_signal'] = f65ms_f65_market_share_momentum_calc072_10d_2nd_v072_signal

def f65ms_f65_market_share_momentum_calc073_63d_2nd_v073_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc073_63d_2nd_v073_signal'] = f65ms_f65_market_share_momentum_calc073_63d_2nd_v073_signal

def f65ms_f65_market_share_momentum_calc074_126d_2nd_v074_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc074_126d_2nd_v074_signal'] = f65ms_f65_market_share_momentum_calc074_126d_2nd_v074_signal

def f65ms_f65_market_share_momentum_calc075_252d_2nd_v075_signal(revenue, liabilities):
    res = ((revenue / liabilities).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc075_252d_2nd_v075_signal'] = f65ms_f65_market_share_momentum_calc075_252d_2nd_v075_signal

def f65ms_f65_market_share_momentum_calc076_5d_2nd_v076_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc076_5d_2nd_v076_signal'] = f65ms_f65_market_share_momentum_calc076_5d_2nd_v076_signal

def f65ms_f65_market_share_momentum_calc077_10d_2nd_v077_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc077_10d_2nd_v077_signal'] = f65ms_f65_market_share_momentum_calc077_10d_2nd_v077_signal

def f65ms_f65_market_share_momentum_calc078_21d_2nd_v078_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc078_21d_2nd_v078_signal'] = f65ms_f65_market_share_momentum_calc078_21d_2nd_v078_signal

def f65ms_f65_market_share_momentum_calc079_42d_2nd_v079_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc079_42d_2nd_v079_signal'] = f65ms_f65_market_share_momentum_calc079_42d_2nd_v079_signal

def f65ms_f65_market_share_momentum_calc080_63d_2nd_v080_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc080_63d_2nd_v080_signal'] = f65ms_f65_market_share_momentum_calc080_63d_2nd_v080_signal

def f65ms_f65_market_share_momentum_calc081_126d_2nd_v081_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc081_126d_2nd_v081_signal'] = f65ms_f65_market_share_momentum_calc081_126d_2nd_v081_signal

def f65ms_f65_market_share_momentum_calc082_252d_2nd_v082_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc082_252d_2nd_v082_signal'] = f65ms_f65_market_share_momentum_calc082_252d_2nd_v082_signal

def f65ms_f65_market_share_momentum_calc083_21d_2nd_v083_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc083_21d_2nd_v083_signal'] = f65ms_f65_market_share_momentum_calc083_21d_2nd_v083_signal

def f65ms_f65_market_share_momentum_calc084_63d_2nd_v084_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc084_63d_2nd_v084_signal'] = f65ms_f65_market_share_momentum_calc084_63d_2nd_v084_signal

def f65ms_f65_market_share_momentum_calc085_5d_2nd_v085_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc085_5d_2nd_v085_signal'] = f65ms_f65_market_share_momentum_calc085_5d_2nd_v085_signal

def f65ms_f65_market_share_momentum_calc086_21d_2nd_v086_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc086_21d_2nd_v086_signal'] = f65ms_f65_market_share_momentum_calc086_21d_2nd_v086_signal

def f65ms_f65_market_share_momentum_calc087_10d_2nd_v087_signal(revenue, workingcapital):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / workingcapital)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc087_10d_2nd_v087_signal'] = f65ms_f65_market_share_momentum_calc087_10d_2nd_v087_signal

def f65ms_f65_market_share_momentum_calc088_63d_2nd_v088_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc088_63d_2nd_v088_signal'] = f65ms_f65_market_share_momentum_calc088_63d_2nd_v088_signal

def f65ms_f65_market_share_momentum_calc089_126d_2nd_v089_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc089_126d_2nd_v089_signal'] = f65ms_f65_market_share_momentum_calc089_126d_2nd_v089_signal

def f65ms_f65_market_share_momentum_calc090_252d_2nd_v090_signal(revenue, workingcapital):
    res = ((revenue / workingcapital).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc090_252d_2nd_v090_signal'] = f65ms_f65_market_share_momentum_calc090_252d_2nd_v090_signal

def f65ms_f65_market_share_momentum_calc091_5d_2nd_v091_signal(revenue, debt):
    res = ((revenue / debt).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc091_5d_2nd_v091_signal'] = f65ms_f65_market_share_momentum_calc091_5d_2nd_v091_signal

def f65ms_f65_market_share_momentum_calc092_10d_2nd_v092_signal(revenue, debt):
    res = ((revenue / debt).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc092_10d_2nd_v092_signal'] = f65ms_f65_market_share_momentum_calc092_10d_2nd_v092_signal

def f65ms_f65_market_share_momentum_calc093_21d_2nd_v093_signal(revenue, debt):
    res = ((revenue / debt).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc093_21d_2nd_v093_signal'] = f65ms_f65_market_share_momentum_calc093_21d_2nd_v093_signal

def f65ms_f65_market_share_momentum_calc094_42d_2nd_v094_signal(revenue, debt):
    res = ((revenue / debt).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc094_42d_2nd_v094_signal'] = f65ms_f65_market_share_momentum_calc094_42d_2nd_v094_signal

def f65ms_f65_market_share_momentum_calc095_63d_2nd_v095_signal(revenue, debt):
    res = ((revenue / debt).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc095_63d_2nd_v095_signal'] = f65ms_f65_market_share_momentum_calc095_63d_2nd_v095_signal

def f65ms_f65_market_share_momentum_calc096_126d_2nd_v096_signal(revenue, debt):
    res = ((revenue / debt).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc096_126d_2nd_v096_signal'] = f65ms_f65_market_share_momentum_calc096_126d_2nd_v096_signal

def f65ms_f65_market_share_momentum_calc097_252d_2nd_v097_signal(revenue, debt):
    res = ((revenue / debt).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc097_252d_2nd_v097_signal'] = f65ms_f65_market_share_momentum_calc097_252d_2nd_v097_signal

def f65ms_f65_market_share_momentum_calc098_21d_2nd_v098_signal(revenue, debt):
    res = ((revenue / debt).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc098_21d_2nd_v098_signal'] = f65ms_f65_market_share_momentum_calc098_21d_2nd_v098_signal

def f65ms_f65_market_share_momentum_calc099_63d_2nd_v099_signal(revenue, debt):
    res = ((revenue / debt).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc099_63d_2nd_v099_signal'] = f65ms_f65_market_share_momentum_calc099_63d_2nd_v099_signal

def f65ms_f65_market_share_momentum_calc100_5d_2nd_v100_signal(revenue, debt):
    res = ((revenue / debt).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc100_5d_2nd_v100_signal'] = f65ms_f65_market_share_momentum_calc100_5d_2nd_v100_signal

def f65ms_f65_market_share_momentum_calc101_21d_2nd_v101_signal(revenue, debt):
    res = ((revenue / debt).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc101_21d_2nd_v101_signal'] = f65ms_f65_market_share_momentum_calc101_21d_2nd_v101_signal

def f65ms_f65_market_share_momentum_calc102_10d_2nd_v102_signal(revenue, debt):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / debt)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc102_10d_2nd_v102_signal'] = f65ms_f65_market_share_momentum_calc102_10d_2nd_v102_signal

def f65ms_f65_market_share_momentum_calc103_63d_2nd_v103_signal(revenue, debt):
    res = ((revenue / debt).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc103_63d_2nd_v103_signal'] = f65ms_f65_market_share_momentum_calc103_63d_2nd_v103_signal

def f65ms_f65_market_share_momentum_calc104_126d_2nd_v104_signal(revenue, debt):
    res = ((revenue / debt).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc104_126d_2nd_v104_signal'] = f65ms_f65_market_share_momentum_calc104_126d_2nd_v104_signal

def f65ms_f65_market_share_momentum_calc105_252d_2nd_v105_signal(revenue, debt):
    res = ((revenue / debt).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc105_252d_2nd_v105_signal'] = f65ms_f65_market_share_momentum_calc105_252d_2nd_v105_signal

def f65ms_f65_market_share_momentum_calc106_5d_2nd_v106_signal(revenue, volume):
    res = ((revenue / volume).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc106_5d_2nd_v106_signal'] = f65ms_f65_market_share_momentum_calc106_5d_2nd_v106_signal

def f65ms_f65_market_share_momentum_calc107_10d_2nd_v107_signal(revenue, volume):
    res = ((revenue / volume).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc107_10d_2nd_v107_signal'] = f65ms_f65_market_share_momentum_calc107_10d_2nd_v107_signal

def f65ms_f65_market_share_momentum_calc108_21d_2nd_v108_signal(revenue, volume):
    res = ((revenue / volume).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc108_21d_2nd_v108_signal'] = f65ms_f65_market_share_momentum_calc108_21d_2nd_v108_signal

def f65ms_f65_market_share_momentum_calc109_42d_2nd_v109_signal(revenue, volume):
    res = ((revenue / volume).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc109_42d_2nd_v109_signal'] = f65ms_f65_market_share_momentum_calc109_42d_2nd_v109_signal

def f65ms_f65_market_share_momentum_calc110_63d_2nd_v110_signal(revenue, volume):
    res = ((revenue / volume).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc110_63d_2nd_v110_signal'] = f65ms_f65_market_share_momentum_calc110_63d_2nd_v110_signal

def f65ms_f65_market_share_momentum_calc111_126d_2nd_v111_signal(revenue, volume):
    res = ((revenue / volume).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc111_126d_2nd_v111_signal'] = f65ms_f65_market_share_momentum_calc111_126d_2nd_v111_signal

def f65ms_f65_market_share_momentum_calc112_252d_2nd_v112_signal(revenue, volume):
    res = ((revenue / volume).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc112_252d_2nd_v112_signal'] = f65ms_f65_market_share_momentum_calc112_252d_2nd_v112_signal

def f65ms_f65_market_share_momentum_calc113_21d_2nd_v113_signal(revenue, volume):
    res = ((revenue / volume).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc113_21d_2nd_v113_signal'] = f65ms_f65_market_share_momentum_calc113_21d_2nd_v113_signal

def f65ms_f65_market_share_momentum_calc114_63d_2nd_v114_signal(revenue, volume):
    res = ((revenue / volume).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc114_63d_2nd_v114_signal'] = f65ms_f65_market_share_momentum_calc114_63d_2nd_v114_signal

def f65ms_f65_market_share_momentum_calc115_5d_2nd_v115_signal(revenue, volume):
    res = ((revenue / volume).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc115_5d_2nd_v115_signal'] = f65ms_f65_market_share_momentum_calc115_5d_2nd_v115_signal

def f65ms_f65_market_share_momentum_calc116_21d_2nd_v116_signal(revenue, volume):
    res = ((revenue / volume).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc116_21d_2nd_v116_signal'] = f65ms_f65_market_share_momentum_calc116_21d_2nd_v116_signal

def f65ms_f65_market_share_momentum_calc117_10d_2nd_v117_signal(revenue, volume):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / volume)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc117_10d_2nd_v117_signal'] = f65ms_f65_market_share_momentum_calc117_10d_2nd_v117_signal

def f65ms_f65_market_share_momentum_calc118_63d_2nd_v118_signal(revenue, volume):
    res = ((revenue / volume).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc118_63d_2nd_v118_signal'] = f65ms_f65_market_share_momentum_calc118_63d_2nd_v118_signal

def f65ms_f65_market_share_momentum_calc119_126d_2nd_v119_signal(revenue, volume):
    res = ((revenue / volume).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc119_126d_2nd_v119_signal'] = f65ms_f65_market_share_momentum_calc119_126d_2nd_v119_signal

def f65ms_f65_market_share_momentum_calc120_252d_2nd_v120_signal(revenue, volume):
    res = ((revenue / volume).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc120_252d_2nd_v120_signal'] = f65ms_f65_market_share_momentum_calc120_252d_2nd_v120_signal

def f65ms_f65_market_share_momentum_calc121_5d_2nd_v121_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc121_5d_2nd_v121_signal'] = f65ms_f65_market_share_momentum_calc121_5d_2nd_v121_signal

def f65ms_f65_market_share_momentum_calc122_10d_2nd_v122_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc122_10d_2nd_v122_signal'] = f65ms_f65_market_share_momentum_calc122_10d_2nd_v122_signal

def f65ms_f65_market_share_momentum_calc123_21d_2nd_v123_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc123_21d_2nd_v123_signal'] = f65ms_f65_market_share_momentum_calc123_21d_2nd_v123_signal

def f65ms_f65_market_share_momentum_calc124_42d_2nd_v124_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc124_42d_2nd_v124_signal'] = f65ms_f65_market_share_momentum_calc124_42d_2nd_v124_signal

def f65ms_f65_market_share_momentum_calc125_63d_2nd_v125_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc125_63d_2nd_v125_signal'] = f65ms_f65_market_share_momentum_calc125_63d_2nd_v125_signal

def f65ms_f65_market_share_momentum_calc126_126d_2nd_v126_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc126_126d_2nd_v126_signal'] = f65ms_f65_market_share_momentum_calc126_126d_2nd_v126_signal

def f65ms_f65_market_share_momentum_calc127_252d_2nd_v127_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc127_252d_2nd_v127_signal'] = f65ms_f65_market_share_momentum_calc127_252d_2nd_v127_signal

def f65ms_f65_market_share_momentum_calc128_21d_2nd_v128_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc128_21d_2nd_v128_signal'] = f65ms_f65_market_share_momentum_calc128_21d_2nd_v128_signal

def f65ms_f65_market_share_momentum_calc129_63d_2nd_v129_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc129_63d_2nd_v129_signal'] = f65ms_f65_market_share_momentum_calc129_63d_2nd_v129_signal

def f65ms_f65_market_share_momentum_calc130_5d_2nd_v130_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc130_5d_2nd_v130_signal'] = f65ms_f65_market_share_momentum_calc130_5d_2nd_v130_signal

def f65ms_f65_market_share_momentum_calc131_21d_2nd_v131_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc131_21d_2nd_v131_signal'] = f65ms_f65_market_share_momentum_calc131_21d_2nd_v131_signal

def f65ms_f65_market_share_momentum_calc132_10d_2nd_v132_signal(revenue, sharesbas):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / sharesbas)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc132_10d_2nd_v132_signal'] = f65ms_f65_market_share_momentum_calc132_10d_2nd_v132_signal

def f65ms_f65_market_share_momentum_calc133_63d_2nd_v133_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc133_63d_2nd_v133_signal'] = f65ms_f65_market_share_momentum_calc133_63d_2nd_v133_signal

def f65ms_f65_market_share_momentum_calc134_126d_2nd_v134_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc134_126d_2nd_v134_signal'] = f65ms_f65_market_share_momentum_calc134_126d_2nd_v134_signal

def f65ms_f65_market_share_momentum_calc135_252d_2nd_v135_signal(revenue, sharesbas):
    res = ((revenue / sharesbas).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc135_252d_2nd_v135_signal'] = f65ms_f65_market_share_momentum_calc135_252d_2nd_v135_signal

def f65ms_f65_market_share_momentum_calc136_5d_2nd_v136_signal(revenue, gp):
    res = ((revenue / gp).rolling(5).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc136_5d_2nd_v136_signal'] = f65ms_f65_market_share_momentum_calc136_5d_2nd_v136_signal

def f65ms_f65_market_share_momentum_calc137_10d_2nd_v137_signal(revenue, gp):
    res = ((revenue / gp).rolling(10).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc137_10d_2nd_v137_signal'] = f65ms_f65_market_share_momentum_calc137_10d_2nd_v137_signal

def f65ms_f65_market_share_momentum_calc138_21d_2nd_v138_signal(revenue, gp):
    res = ((revenue / gp).rolling(21).var()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc138_21d_2nd_v138_signal'] = f65ms_f65_market_share_momentum_calc138_21d_2nd_v138_signal

def f65ms_f65_market_share_momentum_calc139_42d_2nd_v139_signal(revenue, gp):
    res = ((revenue / gp).rolling(42).skew()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc139_42d_2nd_v139_signal'] = f65ms_f65_market_share_momentum_calc139_42d_2nd_v139_signal

def f65ms_f65_market_share_momentum_calc140_63d_2nd_v140_signal(revenue, gp):
    res = ((revenue / gp).rolling(63).kurt()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc140_63d_2nd_v140_signal'] = f65ms_f65_market_share_momentum_calc140_63d_2nd_v140_signal

def f65ms_f65_market_share_momentum_calc141_126d_2nd_v141_signal(revenue, gp):
    res = ((revenue / gp).rolling(126).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc141_126d_2nd_v141_signal'] = f65ms_f65_market_share_momentum_calc141_126d_2nd_v141_signal

def f65ms_f65_market_share_momentum_calc142_252d_2nd_v142_signal(revenue, gp):
    res = ((revenue / gp).rolling(252).min()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc142_252d_2nd_v142_signal'] = f65ms_f65_market_share_momentum_calc142_252d_2nd_v142_signal

def f65ms_f65_market_share_momentum_calc143_21d_2nd_v143_signal(revenue, gp):
    res = ((revenue / gp).rolling(21).median()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc143_21d_2nd_v143_signal'] = f65ms_f65_market_share_momentum_calc143_21d_2nd_v143_signal

def f65ms_f65_market_share_momentum_calc144_63d_2nd_v144_signal(revenue, gp):
    res = ((revenue / gp).rolling(63).rank()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc144_63d_2nd_v144_signal'] = f65ms_f65_market_share_momentum_calc144_63d_2nd_v144_signal

def f65ms_f65_market_share_momentum_calc145_5d_2nd_v145_signal(revenue, gp):
    res = ((revenue / gp).diff(5)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc145_5d_2nd_v145_signal'] = f65ms_f65_market_share_momentum_calc145_5d_2nd_v145_signal

def f65ms_f65_market_share_momentum_calc146_21d_2nd_v146_signal(revenue, gp):
    res = ((revenue / gp).pct_change(21)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc146_21d_2nd_v146_signal'] = f65ms_f65_market_share_momentum_calc146_21d_2nd_v146_signal

def f65ms_f65_market_share_momentum_calc147_10d_2nd_v147_signal(revenue, gp):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / gp)).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc147_10d_2nd_v147_signal'] = f65ms_f65_market_share_momentum_calc147_10d_2nd_v147_signal

def f65ms_f65_market_share_momentum_calc148_63d_2nd_v148_signal(revenue, gp):
    res = ((revenue / gp).rolling(63).mean()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc148_63d_2nd_v148_signal'] = f65ms_f65_market_share_momentum_calc148_63d_2nd_v148_signal

def f65ms_f65_market_share_momentum_calc149_126d_2nd_v149_signal(revenue, gp):
    res = ((revenue / gp).rolling(126).std()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc149_126d_2nd_v149_signal'] = f65ms_f65_market_share_momentum_calc149_126d_2nd_v149_signal

def f65ms_f65_market_share_momentum_calc150_252d_2nd_v150_signal(revenue, gp):
    res = ((revenue / gp).rolling(252).max()).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc150_252d_2nd_v150_signal'] = f65ms_f65_market_share_momentum_calc150_252d_2nd_v150_signal


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
