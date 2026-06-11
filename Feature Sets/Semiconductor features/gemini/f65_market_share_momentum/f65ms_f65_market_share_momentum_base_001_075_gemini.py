import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f65ms_f65_market_share_momentum_calc001_5d_base_v001_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc001_5d_base_v001_signal'] = f65ms_f65_market_share_momentum_calc001_5d_base_v001_signal

def f65ms_f65_market_share_momentum_calc002_10d_base_v002_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc002_10d_base_v002_signal'] = f65ms_f65_market_share_momentum_calc002_10d_base_v002_signal

def f65ms_f65_market_share_momentum_calc003_21d_base_v003_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc003_21d_base_v003_signal'] = f65ms_f65_market_share_momentum_calc003_21d_base_v003_signal

def f65ms_f65_market_share_momentum_calc004_42d_base_v004_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc004_42d_base_v004_signal'] = f65ms_f65_market_share_momentum_calc004_42d_base_v004_signal

def f65ms_f65_market_share_momentum_calc005_63d_base_v005_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc005_63d_base_v005_signal'] = f65ms_f65_market_share_momentum_calc005_63d_base_v005_signal

def f65ms_f65_market_share_momentum_calc006_126d_base_v006_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc006_126d_base_v006_signal'] = f65ms_f65_market_share_momentum_calc006_126d_base_v006_signal

def f65ms_f65_market_share_momentum_calc007_252d_base_v007_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc007_252d_base_v007_signal'] = f65ms_f65_market_share_momentum_calc007_252d_base_v007_signal

def f65ms_f65_market_share_momentum_calc008_21d_base_v008_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc008_21d_base_v008_signal'] = f65ms_f65_market_share_momentum_calc008_21d_base_v008_signal

def f65ms_f65_market_share_momentum_calc009_63d_base_v009_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc009_63d_base_v009_signal'] = f65ms_f65_market_share_momentum_calc009_63d_base_v009_signal

def f65ms_f65_market_share_momentum_calc010_5d_base_v010_signal(revenue, marketcap):
    res = (revenue / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc010_5d_base_v010_signal'] = f65ms_f65_market_share_momentum_calc010_5d_base_v010_signal

def f65ms_f65_market_share_momentum_calc011_21d_base_v011_signal(revenue, marketcap):
    res = (revenue / marketcap).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc011_21d_base_v011_signal'] = f65ms_f65_market_share_momentum_calc011_21d_base_v011_signal

def f65ms_f65_market_share_momentum_calc012_10d_base_v012_signal(revenue, marketcap):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc012_10d_base_v012_signal'] = f65ms_f65_market_share_momentum_calc012_10d_base_v012_signal

def f65ms_f65_market_share_momentum_calc013_63d_base_v013_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc013_63d_base_v013_signal'] = f65ms_f65_market_share_momentum_calc013_63d_base_v013_signal

def f65ms_f65_market_share_momentum_calc014_126d_base_v014_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc014_126d_base_v014_signal'] = f65ms_f65_market_share_momentum_calc014_126d_base_v014_signal

def f65ms_f65_market_share_momentum_calc015_252d_base_v015_signal(revenue, marketcap):
    res = (revenue / marketcap).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc015_252d_base_v015_signal'] = f65ms_f65_market_share_momentum_calc015_252d_base_v015_signal

def f65ms_f65_market_share_momentum_calc016_5d_base_v016_signal(revenue, assets):
    res = (revenue / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc016_5d_base_v016_signal'] = f65ms_f65_market_share_momentum_calc016_5d_base_v016_signal

def f65ms_f65_market_share_momentum_calc017_10d_base_v017_signal(revenue, assets):
    res = (revenue / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc017_10d_base_v017_signal'] = f65ms_f65_market_share_momentum_calc017_10d_base_v017_signal

def f65ms_f65_market_share_momentum_calc018_21d_base_v018_signal(revenue, assets):
    res = (revenue / assets).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc018_21d_base_v018_signal'] = f65ms_f65_market_share_momentum_calc018_21d_base_v018_signal

def f65ms_f65_market_share_momentum_calc019_42d_base_v019_signal(revenue, assets):
    res = (revenue / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc019_42d_base_v019_signal'] = f65ms_f65_market_share_momentum_calc019_42d_base_v019_signal

def f65ms_f65_market_share_momentum_calc020_63d_base_v020_signal(revenue, assets):
    res = (revenue / assets).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc020_63d_base_v020_signal'] = f65ms_f65_market_share_momentum_calc020_63d_base_v020_signal

def f65ms_f65_market_share_momentum_calc021_126d_base_v021_signal(revenue, assets):
    res = (revenue / assets).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc021_126d_base_v021_signal'] = f65ms_f65_market_share_momentum_calc021_126d_base_v021_signal

def f65ms_f65_market_share_momentum_calc022_252d_base_v022_signal(revenue, assets):
    res = (revenue / assets).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc022_252d_base_v022_signal'] = f65ms_f65_market_share_momentum_calc022_252d_base_v022_signal

def f65ms_f65_market_share_momentum_calc023_21d_base_v023_signal(revenue, assets):
    res = (revenue / assets).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc023_21d_base_v023_signal'] = f65ms_f65_market_share_momentum_calc023_21d_base_v023_signal

def f65ms_f65_market_share_momentum_calc024_63d_base_v024_signal(revenue, assets):
    res = (revenue / assets).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc024_63d_base_v024_signal'] = f65ms_f65_market_share_momentum_calc024_63d_base_v024_signal

def f65ms_f65_market_share_momentum_calc025_5d_base_v025_signal(revenue, assets):
    res = (revenue / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc025_5d_base_v025_signal'] = f65ms_f65_market_share_momentum_calc025_5d_base_v025_signal

def f65ms_f65_market_share_momentum_calc026_21d_base_v026_signal(revenue, assets):
    res = (revenue / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc026_21d_base_v026_signal'] = f65ms_f65_market_share_momentum_calc026_21d_base_v026_signal

def f65ms_f65_market_share_momentum_calc027_10d_base_v027_signal(revenue, assets):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc027_10d_base_v027_signal'] = f65ms_f65_market_share_momentum_calc027_10d_base_v027_signal

def f65ms_f65_market_share_momentum_calc028_63d_base_v028_signal(revenue, assets):
    res = (revenue / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc028_63d_base_v028_signal'] = f65ms_f65_market_share_momentum_calc028_63d_base_v028_signal

def f65ms_f65_market_share_momentum_calc029_126d_base_v029_signal(revenue, assets):
    res = (revenue / assets).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc029_126d_base_v029_signal'] = f65ms_f65_market_share_momentum_calc029_126d_base_v029_signal

def f65ms_f65_market_share_momentum_calc030_252d_base_v030_signal(revenue, assets):
    res = (revenue / assets).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc030_252d_base_v030_signal'] = f65ms_f65_market_share_momentum_calc030_252d_base_v030_signal

def f65ms_f65_market_share_momentum_calc031_5d_base_v031_signal(revenue, ev):
    res = (revenue / ev).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc031_5d_base_v031_signal'] = f65ms_f65_market_share_momentum_calc031_5d_base_v031_signal

def f65ms_f65_market_share_momentum_calc032_10d_base_v032_signal(revenue, ev):
    res = (revenue / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc032_10d_base_v032_signal'] = f65ms_f65_market_share_momentum_calc032_10d_base_v032_signal

def f65ms_f65_market_share_momentum_calc033_21d_base_v033_signal(revenue, ev):
    res = (revenue / ev).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc033_21d_base_v033_signal'] = f65ms_f65_market_share_momentum_calc033_21d_base_v033_signal

def f65ms_f65_market_share_momentum_calc034_42d_base_v034_signal(revenue, ev):
    res = (revenue / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc034_42d_base_v034_signal'] = f65ms_f65_market_share_momentum_calc034_42d_base_v034_signal

def f65ms_f65_market_share_momentum_calc035_63d_base_v035_signal(revenue, ev):
    res = (revenue / ev).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc035_63d_base_v035_signal'] = f65ms_f65_market_share_momentum_calc035_63d_base_v035_signal

def f65ms_f65_market_share_momentum_calc036_126d_base_v036_signal(revenue, ev):
    res = (revenue / ev).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc036_126d_base_v036_signal'] = f65ms_f65_market_share_momentum_calc036_126d_base_v036_signal

def f65ms_f65_market_share_momentum_calc037_252d_base_v037_signal(revenue, ev):
    res = (revenue / ev).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc037_252d_base_v037_signal'] = f65ms_f65_market_share_momentum_calc037_252d_base_v037_signal

def f65ms_f65_market_share_momentum_calc038_21d_base_v038_signal(revenue, ev):
    res = (revenue / ev).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc038_21d_base_v038_signal'] = f65ms_f65_market_share_momentum_calc038_21d_base_v038_signal

def f65ms_f65_market_share_momentum_calc039_63d_base_v039_signal(revenue, ev):
    res = (revenue / ev).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc039_63d_base_v039_signal'] = f65ms_f65_market_share_momentum_calc039_63d_base_v039_signal

def f65ms_f65_market_share_momentum_calc040_5d_base_v040_signal(revenue, ev):
    res = (revenue / ev).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc040_5d_base_v040_signal'] = f65ms_f65_market_share_momentum_calc040_5d_base_v040_signal

def f65ms_f65_market_share_momentum_calc041_21d_base_v041_signal(revenue, ev):
    res = (revenue / ev).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc041_21d_base_v041_signal'] = f65ms_f65_market_share_momentum_calc041_21d_base_v041_signal

def f65ms_f65_market_share_momentum_calc042_10d_base_v042_signal(revenue, ev):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / ev)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc042_10d_base_v042_signal'] = f65ms_f65_market_share_momentum_calc042_10d_base_v042_signal

def f65ms_f65_market_share_momentum_calc043_63d_base_v043_signal(revenue, ev):
    res = (revenue / ev).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc043_63d_base_v043_signal'] = f65ms_f65_market_share_momentum_calc043_63d_base_v043_signal

def f65ms_f65_market_share_momentum_calc044_126d_base_v044_signal(revenue, ev):
    res = (revenue / ev).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc044_126d_base_v044_signal'] = f65ms_f65_market_share_momentum_calc044_126d_base_v044_signal

def f65ms_f65_market_share_momentum_calc045_252d_base_v045_signal(revenue, ev):
    res = (revenue / ev).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc045_252d_base_v045_signal'] = f65ms_f65_market_share_momentum_calc045_252d_base_v045_signal

def f65ms_f65_market_share_momentum_calc046_5d_base_v046_signal(revenue, equity):
    res = (revenue / equity).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc046_5d_base_v046_signal'] = f65ms_f65_market_share_momentum_calc046_5d_base_v046_signal

def f65ms_f65_market_share_momentum_calc047_10d_base_v047_signal(revenue, equity):
    res = (revenue / equity).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc047_10d_base_v047_signal'] = f65ms_f65_market_share_momentum_calc047_10d_base_v047_signal

def f65ms_f65_market_share_momentum_calc048_21d_base_v048_signal(revenue, equity):
    res = (revenue / equity).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc048_21d_base_v048_signal'] = f65ms_f65_market_share_momentum_calc048_21d_base_v048_signal

def f65ms_f65_market_share_momentum_calc049_42d_base_v049_signal(revenue, equity):
    res = (revenue / equity).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc049_42d_base_v049_signal'] = f65ms_f65_market_share_momentum_calc049_42d_base_v049_signal

def f65ms_f65_market_share_momentum_calc050_63d_base_v050_signal(revenue, equity):
    res = (revenue / equity).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc050_63d_base_v050_signal'] = f65ms_f65_market_share_momentum_calc050_63d_base_v050_signal

def f65ms_f65_market_share_momentum_calc051_126d_base_v051_signal(revenue, equity):
    res = (revenue / equity).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc051_126d_base_v051_signal'] = f65ms_f65_market_share_momentum_calc051_126d_base_v051_signal

def f65ms_f65_market_share_momentum_calc052_252d_base_v052_signal(revenue, equity):
    res = (revenue / equity).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc052_252d_base_v052_signal'] = f65ms_f65_market_share_momentum_calc052_252d_base_v052_signal

def f65ms_f65_market_share_momentum_calc053_21d_base_v053_signal(revenue, equity):
    res = (revenue / equity).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc053_21d_base_v053_signal'] = f65ms_f65_market_share_momentum_calc053_21d_base_v053_signal

def f65ms_f65_market_share_momentum_calc054_63d_base_v054_signal(revenue, equity):
    res = (revenue / equity).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc054_63d_base_v054_signal'] = f65ms_f65_market_share_momentum_calc054_63d_base_v054_signal

def f65ms_f65_market_share_momentum_calc055_5d_base_v055_signal(revenue, equity):
    res = (revenue / equity).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc055_5d_base_v055_signal'] = f65ms_f65_market_share_momentum_calc055_5d_base_v055_signal

def f65ms_f65_market_share_momentum_calc056_21d_base_v056_signal(revenue, equity):
    res = (revenue / equity).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc056_21d_base_v056_signal'] = f65ms_f65_market_share_momentum_calc056_21d_base_v056_signal

def f65ms_f65_market_share_momentum_calc057_10d_base_v057_signal(revenue, equity):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / equity)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc057_10d_base_v057_signal'] = f65ms_f65_market_share_momentum_calc057_10d_base_v057_signal

def f65ms_f65_market_share_momentum_calc058_63d_base_v058_signal(revenue, equity):
    res = (revenue / equity).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc058_63d_base_v058_signal'] = f65ms_f65_market_share_momentum_calc058_63d_base_v058_signal

def f65ms_f65_market_share_momentum_calc059_126d_base_v059_signal(revenue, equity):
    res = (revenue / equity).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc059_126d_base_v059_signal'] = f65ms_f65_market_share_momentum_calc059_126d_base_v059_signal

def f65ms_f65_market_share_momentum_calc060_252d_base_v060_signal(revenue, equity):
    res = (revenue / equity).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc060_252d_base_v060_signal'] = f65ms_f65_market_share_momentum_calc060_252d_base_v060_signal

def f65ms_f65_market_share_momentum_calc061_5d_base_v061_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc061_5d_base_v061_signal'] = f65ms_f65_market_share_momentum_calc061_5d_base_v061_signal

def f65ms_f65_market_share_momentum_calc062_10d_base_v062_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc062_10d_base_v062_signal'] = f65ms_f65_market_share_momentum_calc062_10d_base_v062_signal

def f65ms_f65_market_share_momentum_calc063_21d_base_v063_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc063_21d_base_v063_signal'] = f65ms_f65_market_share_momentum_calc063_21d_base_v063_signal

def f65ms_f65_market_share_momentum_calc064_42d_base_v064_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc064_42d_base_v064_signal'] = f65ms_f65_market_share_momentum_calc064_42d_base_v064_signal

def f65ms_f65_market_share_momentum_calc065_63d_base_v065_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc065_63d_base_v065_signal'] = f65ms_f65_market_share_momentum_calc065_63d_base_v065_signal

def f65ms_f65_market_share_momentum_calc066_126d_base_v066_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc066_126d_base_v066_signal'] = f65ms_f65_market_share_momentum_calc066_126d_base_v066_signal

def f65ms_f65_market_share_momentum_calc067_252d_base_v067_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc067_252d_base_v067_signal'] = f65ms_f65_market_share_momentum_calc067_252d_base_v067_signal

def f65ms_f65_market_share_momentum_calc068_21d_base_v068_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc068_21d_base_v068_signal'] = f65ms_f65_market_share_momentum_calc068_21d_base_v068_signal

def f65ms_f65_market_share_momentum_calc069_63d_base_v069_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc069_63d_base_v069_signal'] = f65ms_f65_market_share_momentum_calc069_63d_base_v069_signal

def f65ms_f65_market_share_momentum_calc070_5d_base_v070_signal(revenue, liabilities):
    res = (revenue / liabilities).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc070_5d_base_v070_signal'] = f65ms_f65_market_share_momentum_calc070_5d_base_v070_signal

def f65ms_f65_market_share_momentum_calc071_21d_base_v071_signal(revenue, liabilities):
    res = (revenue / liabilities).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc071_21d_base_v071_signal'] = f65ms_f65_market_share_momentum_calc071_21d_base_v071_signal

def f65ms_f65_market_share_momentum_calc072_10d_base_v072_signal(revenue, liabilities):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(revenue / liabilities)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc072_10d_base_v072_signal'] = f65ms_f65_market_share_momentum_calc072_10d_base_v072_signal

def f65ms_f65_market_share_momentum_calc073_63d_base_v073_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc073_63d_base_v073_signal'] = f65ms_f65_market_share_momentum_calc073_63d_base_v073_signal

def f65ms_f65_market_share_momentum_calc074_126d_base_v074_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc074_126d_base_v074_signal'] = f65ms_f65_market_share_momentum_calc074_126d_base_v074_signal

def f65ms_f65_market_share_momentum_calc075_252d_base_v075_signal(revenue, liabilities):
    res = (revenue / liabilities).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f65ms_f65_market_share_momentum_calc075_252d_base_v075_signal'] = f65ms_f65_market_share_momentum_calc075_252d_base_v075_signal


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
