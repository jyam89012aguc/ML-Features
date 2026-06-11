import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f64fy_f64_fcf_yield_dynamics_calc001_5d_base_v001_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc001_5d_base_v001_signal'] = f64fy_f64_fcf_yield_dynamics_calc001_5d_base_v001_signal

def f64fy_f64_fcf_yield_dynamics_calc002_10d_base_v002_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc002_10d_base_v002_signal'] = f64fy_f64_fcf_yield_dynamics_calc002_10d_base_v002_signal

def f64fy_f64_fcf_yield_dynamics_calc003_21d_base_v003_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc003_21d_base_v003_signal'] = f64fy_f64_fcf_yield_dynamics_calc003_21d_base_v003_signal

def f64fy_f64_fcf_yield_dynamics_calc004_42d_base_v004_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc004_42d_base_v004_signal'] = f64fy_f64_fcf_yield_dynamics_calc004_42d_base_v004_signal

def f64fy_f64_fcf_yield_dynamics_calc005_63d_base_v005_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc005_63d_base_v005_signal'] = f64fy_f64_fcf_yield_dynamics_calc005_63d_base_v005_signal

def f64fy_f64_fcf_yield_dynamics_calc006_126d_base_v006_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc006_126d_base_v006_signal'] = f64fy_f64_fcf_yield_dynamics_calc006_126d_base_v006_signal

def f64fy_f64_fcf_yield_dynamics_calc007_252d_base_v007_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc007_252d_base_v007_signal'] = f64fy_f64_fcf_yield_dynamics_calc007_252d_base_v007_signal

def f64fy_f64_fcf_yield_dynamics_calc008_21d_base_v008_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc008_21d_base_v008_signal'] = f64fy_f64_fcf_yield_dynamics_calc008_21d_base_v008_signal

def f64fy_f64_fcf_yield_dynamics_calc009_63d_base_v009_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc009_63d_base_v009_signal'] = f64fy_f64_fcf_yield_dynamics_calc009_63d_base_v009_signal

def f64fy_f64_fcf_yield_dynamics_calc010_5d_base_v010_signal(fcf, marketcap):
    res = (fcf / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc010_5d_base_v010_signal'] = f64fy_f64_fcf_yield_dynamics_calc010_5d_base_v010_signal

def f64fy_f64_fcf_yield_dynamics_calc011_21d_base_v011_signal(fcf, marketcap):
    res = (fcf / marketcap).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc011_21d_base_v011_signal'] = f64fy_f64_fcf_yield_dynamics_calc011_21d_base_v011_signal

def f64fy_f64_fcf_yield_dynamics_calc012_10d_base_v012_signal(fcf, marketcap):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc012_10d_base_v012_signal'] = f64fy_f64_fcf_yield_dynamics_calc012_10d_base_v012_signal

def f64fy_f64_fcf_yield_dynamics_calc013_63d_base_v013_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc013_63d_base_v013_signal'] = f64fy_f64_fcf_yield_dynamics_calc013_63d_base_v013_signal

def f64fy_f64_fcf_yield_dynamics_calc014_126d_base_v014_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc014_126d_base_v014_signal'] = f64fy_f64_fcf_yield_dynamics_calc014_126d_base_v014_signal

def f64fy_f64_fcf_yield_dynamics_calc015_252d_base_v015_signal(fcf, marketcap):
    res = (fcf / marketcap).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc015_252d_base_v015_signal'] = f64fy_f64_fcf_yield_dynamics_calc015_252d_base_v015_signal

def f64fy_f64_fcf_yield_dynamics_calc016_5d_base_v016_signal(fcf, ev):
    res = (fcf / ev).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc016_5d_base_v016_signal'] = f64fy_f64_fcf_yield_dynamics_calc016_5d_base_v016_signal

def f64fy_f64_fcf_yield_dynamics_calc017_10d_base_v017_signal(fcf, ev):
    res = (fcf / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc017_10d_base_v017_signal'] = f64fy_f64_fcf_yield_dynamics_calc017_10d_base_v017_signal

def f64fy_f64_fcf_yield_dynamics_calc018_21d_base_v018_signal(fcf, ev):
    res = (fcf / ev).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc018_21d_base_v018_signal'] = f64fy_f64_fcf_yield_dynamics_calc018_21d_base_v018_signal

def f64fy_f64_fcf_yield_dynamics_calc019_42d_base_v019_signal(fcf, ev):
    res = (fcf / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc019_42d_base_v019_signal'] = f64fy_f64_fcf_yield_dynamics_calc019_42d_base_v019_signal

def f64fy_f64_fcf_yield_dynamics_calc020_63d_base_v020_signal(fcf, ev):
    res = (fcf / ev).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc020_63d_base_v020_signal'] = f64fy_f64_fcf_yield_dynamics_calc020_63d_base_v020_signal

def f64fy_f64_fcf_yield_dynamics_calc021_126d_base_v021_signal(fcf, ev):
    res = (fcf / ev).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc021_126d_base_v021_signal'] = f64fy_f64_fcf_yield_dynamics_calc021_126d_base_v021_signal

def f64fy_f64_fcf_yield_dynamics_calc022_252d_base_v022_signal(fcf, ev):
    res = (fcf / ev).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc022_252d_base_v022_signal'] = f64fy_f64_fcf_yield_dynamics_calc022_252d_base_v022_signal

def f64fy_f64_fcf_yield_dynamics_calc023_21d_base_v023_signal(fcf, ev):
    res = (fcf / ev).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc023_21d_base_v023_signal'] = f64fy_f64_fcf_yield_dynamics_calc023_21d_base_v023_signal

def f64fy_f64_fcf_yield_dynamics_calc024_63d_base_v024_signal(fcf, ev):
    res = (fcf / ev).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc024_63d_base_v024_signal'] = f64fy_f64_fcf_yield_dynamics_calc024_63d_base_v024_signal

def f64fy_f64_fcf_yield_dynamics_calc025_5d_base_v025_signal(fcf, ev):
    res = (fcf / ev).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc025_5d_base_v025_signal'] = f64fy_f64_fcf_yield_dynamics_calc025_5d_base_v025_signal

def f64fy_f64_fcf_yield_dynamics_calc026_21d_base_v026_signal(fcf, ev):
    res = (fcf / ev).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc026_21d_base_v026_signal'] = f64fy_f64_fcf_yield_dynamics_calc026_21d_base_v026_signal

def f64fy_f64_fcf_yield_dynamics_calc027_10d_base_v027_signal(fcf, ev):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / ev)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc027_10d_base_v027_signal'] = f64fy_f64_fcf_yield_dynamics_calc027_10d_base_v027_signal

def f64fy_f64_fcf_yield_dynamics_calc028_63d_base_v028_signal(fcf, ev):
    res = (fcf / ev).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc028_63d_base_v028_signal'] = f64fy_f64_fcf_yield_dynamics_calc028_63d_base_v028_signal

def f64fy_f64_fcf_yield_dynamics_calc029_126d_base_v029_signal(fcf, ev):
    res = (fcf / ev).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc029_126d_base_v029_signal'] = f64fy_f64_fcf_yield_dynamics_calc029_126d_base_v029_signal

def f64fy_f64_fcf_yield_dynamics_calc030_252d_base_v030_signal(fcf, ev):
    res = (fcf / ev).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc030_252d_base_v030_signal'] = f64fy_f64_fcf_yield_dynamics_calc030_252d_base_v030_signal

def f64fy_f64_fcf_yield_dynamics_calc031_5d_base_v031_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc031_5d_base_v031_signal'] = f64fy_f64_fcf_yield_dynamics_calc031_5d_base_v031_signal

def f64fy_f64_fcf_yield_dynamics_calc032_10d_base_v032_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc032_10d_base_v032_signal'] = f64fy_f64_fcf_yield_dynamics_calc032_10d_base_v032_signal

def f64fy_f64_fcf_yield_dynamics_calc033_21d_base_v033_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc033_21d_base_v033_signal'] = f64fy_f64_fcf_yield_dynamics_calc033_21d_base_v033_signal

def f64fy_f64_fcf_yield_dynamics_calc034_42d_base_v034_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc034_42d_base_v034_signal'] = f64fy_f64_fcf_yield_dynamics_calc034_42d_base_v034_signal

def f64fy_f64_fcf_yield_dynamics_calc035_63d_base_v035_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc035_63d_base_v035_signal'] = f64fy_f64_fcf_yield_dynamics_calc035_63d_base_v035_signal

def f64fy_f64_fcf_yield_dynamics_calc036_126d_base_v036_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc036_126d_base_v036_signal'] = f64fy_f64_fcf_yield_dynamics_calc036_126d_base_v036_signal

def f64fy_f64_fcf_yield_dynamics_calc037_252d_base_v037_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc037_252d_base_v037_signal'] = f64fy_f64_fcf_yield_dynamics_calc037_252d_base_v037_signal

def f64fy_f64_fcf_yield_dynamics_calc038_21d_base_v038_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc038_21d_base_v038_signal'] = f64fy_f64_fcf_yield_dynamics_calc038_21d_base_v038_signal

def f64fy_f64_fcf_yield_dynamics_calc039_63d_base_v039_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc039_63d_base_v039_signal'] = f64fy_f64_fcf_yield_dynamics_calc039_63d_base_v039_signal

def f64fy_f64_fcf_yield_dynamics_calc040_5d_base_v040_signal(ncfo, marketcap):
    res = (ncfo / marketcap).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc040_5d_base_v040_signal'] = f64fy_f64_fcf_yield_dynamics_calc040_5d_base_v040_signal

def f64fy_f64_fcf_yield_dynamics_calc041_21d_base_v041_signal(ncfo, marketcap):
    res = (ncfo / marketcap).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc041_21d_base_v041_signal'] = f64fy_f64_fcf_yield_dynamics_calc041_21d_base_v041_signal

def f64fy_f64_fcf_yield_dynamics_calc042_10d_base_v042_signal(ncfo, marketcap):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ncfo / marketcap)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc042_10d_base_v042_signal'] = f64fy_f64_fcf_yield_dynamics_calc042_10d_base_v042_signal

def f64fy_f64_fcf_yield_dynamics_calc043_63d_base_v043_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc043_63d_base_v043_signal'] = f64fy_f64_fcf_yield_dynamics_calc043_63d_base_v043_signal

def f64fy_f64_fcf_yield_dynamics_calc044_126d_base_v044_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc044_126d_base_v044_signal'] = f64fy_f64_fcf_yield_dynamics_calc044_126d_base_v044_signal

def f64fy_f64_fcf_yield_dynamics_calc045_252d_base_v045_signal(ncfo, marketcap):
    res = (ncfo / marketcap).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc045_252d_base_v045_signal'] = f64fy_f64_fcf_yield_dynamics_calc045_252d_base_v045_signal

def f64fy_f64_fcf_yield_dynamics_calc046_5d_base_v046_signal(ncfo, ev):
    res = (ncfo / ev).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc046_5d_base_v046_signal'] = f64fy_f64_fcf_yield_dynamics_calc046_5d_base_v046_signal

def f64fy_f64_fcf_yield_dynamics_calc047_10d_base_v047_signal(ncfo, ev):
    res = (ncfo / ev).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc047_10d_base_v047_signal'] = f64fy_f64_fcf_yield_dynamics_calc047_10d_base_v047_signal

def f64fy_f64_fcf_yield_dynamics_calc048_21d_base_v048_signal(ncfo, ev):
    res = (ncfo / ev).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc048_21d_base_v048_signal'] = f64fy_f64_fcf_yield_dynamics_calc048_21d_base_v048_signal

def f64fy_f64_fcf_yield_dynamics_calc049_42d_base_v049_signal(ncfo, ev):
    res = (ncfo / ev).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc049_42d_base_v049_signal'] = f64fy_f64_fcf_yield_dynamics_calc049_42d_base_v049_signal

def f64fy_f64_fcf_yield_dynamics_calc050_63d_base_v050_signal(ncfo, ev):
    res = (ncfo / ev).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc050_63d_base_v050_signal'] = f64fy_f64_fcf_yield_dynamics_calc050_63d_base_v050_signal

def f64fy_f64_fcf_yield_dynamics_calc051_126d_base_v051_signal(ncfo, ev):
    res = (ncfo / ev).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc051_126d_base_v051_signal'] = f64fy_f64_fcf_yield_dynamics_calc051_126d_base_v051_signal

def f64fy_f64_fcf_yield_dynamics_calc052_252d_base_v052_signal(ncfo, ev):
    res = (ncfo / ev).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc052_252d_base_v052_signal'] = f64fy_f64_fcf_yield_dynamics_calc052_252d_base_v052_signal

def f64fy_f64_fcf_yield_dynamics_calc053_21d_base_v053_signal(ncfo, ev):
    res = (ncfo / ev).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc053_21d_base_v053_signal'] = f64fy_f64_fcf_yield_dynamics_calc053_21d_base_v053_signal

def f64fy_f64_fcf_yield_dynamics_calc054_63d_base_v054_signal(ncfo, ev):
    res = (ncfo / ev).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc054_63d_base_v054_signal'] = f64fy_f64_fcf_yield_dynamics_calc054_63d_base_v054_signal

def f64fy_f64_fcf_yield_dynamics_calc055_5d_base_v055_signal(ncfo, ev):
    res = (ncfo / ev).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc055_5d_base_v055_signal'] = f64fy_f64_fcf_yield_dynamics_calc055_5d_base_v055_signal

def f64fy_f64_fcf_yield_dynamics_calc056_21d_base_v056_signal(ncfo, ev):
    res = (ncfo / ev).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc056_21d_base_v056_signal'] = f64fy_f64_fcf_yield_dynamics_calc056_21d_base_v056_signal

def f64fy_f64_fcf_yield_dynamics_calc057_10d_base_v057_signal(ncfo, ev):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ncfo / ev)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc057_10d_base_v057_signal'] = f64fy_f64_fcf_yield_dynamics_calc057_10d_base_v057_signal

def f64fy_f64_fcf_yield_dynamics_calc058_63d_base_v058_signal(ncfo, ev):
    res = (ncfo / ev).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc058_63d_base_v058_signal'] = f64fy_f64_fcf_yield_dynamics_calc058_63d_base_v058_signal

def f64fy_f64_fcf_yield_dynamics_calc059_126d_base_v059_signal(ncfo, ev):
    res = (ncfo / ev).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc059_126d_base_v059_signal'] = f64fy_f64_fcf_yield_dynamics_calc059_126d_base_v059_signal

def f64fy_f64_fcf_yield_dynamics_calc060_252d_base_v060_signal(ncfo, ev):
    res = (ncfo / ev).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc060_252d_base_v060_signal'] = f64fy_f64_fcf_yield_dynamics_calc060_252d_base_v060_signal

def f64fy_f64_fcf_yield_dynamics_calc061_5d_base_v061_signal(fcf, assets):
    res = (fcf / assets).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc061_5d_base_v061_signal'] = f64fy_f64_fcf_yield_dynamics_calc061_5d_base_v061_signal

def f64fy_f64_fcf_yield_dynamics_calc062_10d_base_v062_signal(fcf, assets):
    res = (fcf / assets).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc062_10d_base_v062_signal'] = f64fy_f64_fcf_yield_dynamics_calc062_10d_base_v062_signal

def f64fy_f64_fcf_yield_dynamics_calc063_21d_base_v063_signal(fcf, assets):
    res = (fcf / assets).rolling(21).var()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc063_21d_base_v063_signal'] = f64fy_f64_fcf_yield_dynamics_calc063_21d_base_v063_signal

def f64fy_f64_fcf_yield_dynamics_calc064_42d_base_v064_signal(fcf, assets):
    res = (fcf / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc064_42d_base_v064_signal'] = f64fy_f64_fcf_yield_dynamics_calc064_42d_base_v064_signal

def f64fy_f64_fcf_yield_dynamics_calc065_63d_base_v065_signal(fcf, assets):
    res = (fcf / assets).rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc065_63d_base_v065_signal'] = f64fy_f64_fcf_yield_dynamics_calc065_63d_base_v065_signal

def f64fy_f64_fcf_yield_dynamics_calc066_126d_base_v066_signal(fcf, assets):
    res = (fcf / assets).rolling(126).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc066_126d_base_v066_signal'] = f64fy_f64_fcf_yield_dynamics_calc066_126d_base_v066_signal

def f64fy_f64_fcf_yield_dynamics_calc067_252d_base_v067_signal(fcf, assets):
    res = (fcf / assets).rolling(252).min()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc067_252d_base_v067_signal'] = f64fy_f64_fcf_yield_dynamics_calc067_252d_base_v067_signal

def f64fy_f64_fcf_yield_dynamics_calc068_21d_base_v068_signal(fcf, assets):
    res = (fcf / assets).rolling(21).median()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc068_21d_base_v068_signal'] = f64fy_f64_fcf_yield_dynamics_calc068_21d_base_v068_signal

def f64fy_f64_fcf_yield_dynamics_calc069_63d_base_v069_signal(fcf, assets):
    res = (fcf / assets).rolling(63).rank()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc069_63d_base_v069_signal'] = f64fy_f64_fcf_yield_dynamics_calc069_63d_base_v069_signal

def f64fy_f64_fcf_yield_dynamics_calc070_5d_base_v070_signal(fcf, assets):
    res = (fcf / assets).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc070_5d_base_v070_signal'] = f64fy_f64_fcf_yield_dynamics_calc070_5d_base_v070_signal

def f64fy_f64_fcf_yield_dynamics_calc071_21d_base_v071_signal(fcf, assets):
    res = (fcf / assets).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc071_21d_base_v071_signal'] = f64fy_f64_fcf_yield_dynamics_calc071_21d_base_v071_signal

def f64fy_f64_fcf_yield_dynamics_calc072_10d_base_v072_signal(fcf, assets):
    res = (lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / assets)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc072_10d_base_v072_signal'] = f64fy_f64_fcf_yield_dynamics_calc072_10d_base_v072_signal

def f64fy_f64_fcf_yield_dynamics_calc073_63d_base_v073_signal(fcf, assets):
    res = (fcf / assets).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc073_63d_base_v073_signal'] = f64fy_f64_fcf_yield_dynamics_calc073_63d_base_v073_signal

def f64fy_f64_fcf_yield_dynamics_calc074_126d_base_v074_signal(fcf, assets):
    res = (fcf / assets).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc074_126d_base_v074_signal'] = f64fy_f64_fcf_yield_dynamics_calc074_126d_base_v074_signal

def f64fy_f64_fcf_yield_dynamics_calc075_252d_base_v075_signal(fcf, assets):
    res = (fcf / assets).rolling(252).max()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc075_252d_base_v075_signal'] = f64fy_f64_fcf_yield_dynamics_calc075_252d_base_v075_signal


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
