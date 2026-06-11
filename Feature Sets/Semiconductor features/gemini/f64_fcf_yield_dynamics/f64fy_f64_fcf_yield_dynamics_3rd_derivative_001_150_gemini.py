import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f64fy_f64_fcf_yield_dynamics_calc001_5d_3rd_v001_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc001_5d_3rd_v001_signal'] = f64fy_f64_fcf_yield_dynamics_calc001_5d_3rd_v001_signal

def f64fy_f64_fcf_yield_dynamics_calc002_10d_3rd_v002_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc002_10d_3rd_v002_signal'] = f64fy_f64_fcf_yield_dynamics_calc002_10d_3rd_v002_signal

def f64fy_f64_fcf_yield_dynamics_calc003_21d_3rd_v003_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc003_21d_3rd_v003_signal'] = f64fy_f64_fcf_yield_dynamics_calc003_21d_3rd_v003_signal

def f64fy_f64_fcf_yield_dynamics_calc004_42d_3rd_v004_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc004_42d_3rd_v004_signal'] = f64fy_f64_fcf_yield_dynamics_calc004_42d_3rd_v004_signal

def f64fy_f64_fcf_yield_dynamics_calc005_63d_3rd_v005_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc005_63d_3rd_v005_signal'] = f64fy_f64_fcf_yield_dynamics_calc005_63d_3rd_v005_signal

def f64fy_f64_fcf_yield_dynamics_calc006_126d_3rd_v006_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc006_126d_3rd_v006_signal'] = f64fy_f64_fcf_yield_dynamics_calc006_126d_3rd_v006_signal

def f64fy_f64_fcf_yield_dynamics_calc007_252d_3rd_v007_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc007_252d_3rd_v007_signal'] = f64fy_f64_fcf_yield_dynamics_calc007_252d_3rd_v007_signal

def f64fy_f64_fcf_yield_dynamics_calc008_21d_3rd_v008_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc008_21d_3rd_v008_signal'] = f64fy_f64_fcf_yield_dynamics_calc008_21d_3rd_v008_signal

def f64fy_f64_fcf_yield_dynamics_calc009_63d_3rd_v009_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc009_63d_3rd_v009_signal'] = f64fy_f64_fcf_yield_dynamics_calc009_63d_3rd_v009_signal

def f64fy_f64_fcf_yield_dynamics_calc010_5d_3rd_v010_signal(fcf, marketcap):
    res = ((fcf / marketcap).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc010_5d_3rd_v010_signal'] = f64fy_f64_fcf_yield_dynamics_calc010_5d_3rd_v010_signal

def f64fy_f64_fcf_yield_dynamics_calc011_21d_3rd_v011_signal(fcf, marketcap):
    res = ((fcf / marketcap).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc011_21d_3rd_v011_signal'] = f64fy_f64_fcf_yield_dynamics_calc011_21d_3rd_v011_signal

def f64fy_f64_fcf_yield_dynamics_calc012_10d_3rd_v012_signal(fcf, marketcap):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / marketcap)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc012_10d_3rd_v012_signal'] = f64fy_f64_fcf_yield_dynamics_calc012_10d_3rd_v012_signal

def f64fy_f64_fcf_yield_dynamics_calc013_63d_3rd_v013_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc013_63d_3rd_v013_signal'] = f64fy_f64_fcf_yield_dynamics_calc013_63d_3rd_v013_signal

def f64fy_f64_fcf_yield_dynamics_calc014_126d_3rd_v014_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc014_126d_3rd_v014_signal'] = f64fy_f64_fcf_yield_dynamics_calc014_126d_3rd_v014_signal

def f64fy_f64_fcf_yield_dynamics_calc015_252d_3rd_v015_signal(fcf, marketcap):
    res = ((fcf / marketcap).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc015_252d_3rd_v015_signal'] = f64fy_f64_fcf_yield_dynamics_calc015_252d_3rd_v015_signal

def f64fy_f64_fcf_yield_dynamics_calc016_5d_3rd_v016_signal(fcf, ev):
    res = ((fcf / ev).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc016_5d_3rd_v016_signal'] = f64fy_f64_fcf_yield_dynamics_calc016_5d_3rd_v016_signal

def f64fy_f64_fcf_yield_dynamics_calc017_10d_3rd_v017_signal(fcf, ev):
    res = ((fcf / ev).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc017_10d_3rd_v017_signal'] = f64fy_f64_fcf_yield_dynamics_calc017_10d_3rd_v017_signal

def f64fy_f64_fcf_yield_dynamics_calc018_21d_3rd_v018_signal(fcf, ev):
    res = ((fcf / ev).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc018_21d_3rd_v018_signal'] = f64fy_f64_fcf_yield_dynamics_calc018_21d_3rd_v018_signal

def f64fy_f64_fcf_yield_dynamics_calc019_42d_3rd_v019_signal(fcf, ev):
    res = ((fcf / ev).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc019_42d_3rd_v019_signal'] = f64fy_f64_fcf_yield_dynamics_calc019_42d_3rd_v019_signal

def f64fy_f64_fcf_yield_dynamics_calc020_63d_3rd_v020_signal(fcf, ev):
    res = ((fcf / ev).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc020_63d_3rd_v020_signal'] = f64fy_f64_fcf_yield_dynamics_calc020_63d_3rd_v020_signal

def f64fy_f64_fcf_yield_dynamics_calc021_126d_3rd_v021_signal(fcf, ev):
    res = ((fcf / ev).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc021_126d_3rd_v021_signal'] = f64fy_f64_fcf_yield_dynamics_calc021_126d_3rd_v021_signal

def f64fy_f64_fcf_yield_dynamics_calc022_252d_3rd_v022_signal(fcf, ev):
    res = ((fcf / ev).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc022_252d_3rd_v022_signal'] = f64fy_f64_fcf_yield_dynamics_calc022_252d_3rd_v022_signal

def f64fy_f64_fcf_yield_dynamics_calc023_21d_3rd_v023_signal(fcf, ev):
    res = ((fcf / ev).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc023_21d_3rd_v023_signal'] = f64fy_f64_fcf_yield_dynamics_calc023_21d_3rd_v023_signal

def f64fy_f64_fcf_yield_dynamics_calc024_63d_3rd_v024_signal(fcf, ev):
    res = ((fcf / ev).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc024_63d_3rd_v024_signal'] = f64fy_f64_fcf_yield_dynamics_calc024_63d_3rd_v024_signal

def f64fy_f64_fcf_yield_dynamics_calc025_5d_3rd_v025_signal(fcf, ev):
    res = ((fcf / ev).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc025_5d_3rd_v025_signal'] = f64fy_f64_fcf_yield_dynamics_calc025_5d_3rd_v025_signal

def f64fy_f64_fcf_yield_dynamics_calc026_21d_3rd_v026_signal(fcf, ev):
    res = ((fcf / ev).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc026_21d_3rd_v026_signal'] = f64fy_f64_fcf_yield_dynamics_calc026_21d_3rd_v026_signal

def f64fy_f64_fcf_yield_dynamics_calc027_10d_3rd_v027_signal(fcf, ev):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / ev)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc027_10d_3rd_v027_signal'] = f64fy_f64_fcf_yield_dynamics_calc027_10d_3rd_v027_signal

def f64fy_f64_fcf_yield_dynamics_calc028_63d_3rd_v028_signal(fcf, ev):
    res = ((fcf / ev).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc028_63d_3rd_v028_signal'] = f64fy_f64_fcf_yield_dynamics_calc028_63d_3rd_v028_signal

def f64fy_f64_fcf_yield_dynamics_calc029_126d_3rd_v029_signal(fcf, ev):
    res = ((fcf / ev).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc029_126d_3rd_v029_signal'] = f64fy_f64_fcf_yield_dynamics_calc029_126d_3rd_v029_signal

def f64fy_f64_fcf_yield_dynamics_calc030_252d_3rd_v030_signal(fcf, ev):
    res = ((fcf / ev).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc030_252d_3rd_v030_signal'] = f64fy_f64_fcf_yield_dynamics_calc030_252d_3rd_v030_signal

def f64fy_f64_fcf_yield_dynamics_calc031_5d_3rd_v031_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc031_5d_3rd_v031_signal'] = f64fy_f64_fcf_yield_dynamics_calc031_5d_3rd_v031_signal

def f64fy_f64_fcf_yield_dynamics_calc032_10d_3rd_v032_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc032_10d_3rd_v032_signal'] = f64fy_f64_fcf_yield_dynamics_calc032_10d_3rd_v032_signal

def f64fy_f64_fcf_yield_dynamics_calc033_21d_3rd_v033_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc033_21d_3rd_v033_signal'] = f64fy_f64_fcf_yield_dynamics_calc033_21d_3rd_v033_signal

def f64fy_f64_fcf_yield_dynamics_calc034_42d_3rd_v034_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc034_42d_3rd_v034_signal'] = f64fy_f64_fcf_yield_dynamics_calc034_42d_3rd_v034_signal

def f64fy_f64_fcf_yield_dynamics_calc035_63d_3rd_v035_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc035_63d_3rd_v035_signal'] = f64fy_f64_fcf_yield_dynamics_calc035_63d_3rd_v035_signal

def f64fy_f64_fcf_yield_dynamics_calc036_126d_3rd_v036_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc036_126d_3rd_v036_signal'] = f64fy_f64_fcf_yield_dynamics_calc036_126d_3rd_v036_signal

def f64fy_f64_fcf_yield_dynamics_calc037_252d_3rd_v037_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc037_252d_3rd_v037_signal'] = f64fy_f64_fcf_yield_dynamics_calc037_252d_3rd_v037_signal

def f64fy_f64_fcf_yield_dynamics_calc038_21d_3rd_v038_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc038_21d_3rd_v038_signal'] = f64fy_f64_fcf_yield_dynamics_calc038_21d_3rd_v038_signal

def f64fy_f64_fcf_yield_dynamics_calc039_63d_3rd_v039_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc039_63d_3rd_v039_signal'] = f64fy_f64_fcf_yield_dynamics_calc039_63d_3rd_v039_signal

def f64fy_f64_fcf_yield_dynamics_calc040_5d_3rd_v040_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc040_5d_3rd_v040_signal'] = f64fy_f64_fcf_yield_dynamics_calc040_5d_3rd_v040_signal

def f64fy_f64_fcf_yield_dynamics_calc041_21d_3rd_v041_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc041_21d_3rd_v041_signal'] = f64fy_f64_fcf_yield_dynamics_calc041_21d_3rd_v041_signal

def f64fy_f64_fcf_yield_dynamics_calc042_10d_3rd_v042_signal(ncfo, marketcap):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ncfo / marketcap)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc042_10d_3rd_v042_signal'] = f64fy_f64_fcf_yield_dynamics_calc042_10d_3rd_v042_signal

def f64fy_f64_fcf_yield_dynamics_calc043_63d_3rd_v043_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc043_63d_3rd_v043_signal'] = f64fy_f64_fcf_yield_dynamics_calc043_63d_3rd_v043_signal

def f64fy_f64_fcf_yield_dynamics_calc044_126d_3rd_v044_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc044_126d_3rd_v044_signal'] = f64fy_f64_fcf_yield_dynamics_calc044_126d_3rd_v044_signal

def f64fy_f64_fcf_yield_dynamics_calc045_252d_3rd_v045_signal(ncfo, marketcap):
    res = ((ncfo / marketcap).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc045_252d_3rd_v045_signal'] = f64fy_f64_fcf_yield_dynamics_calc045_252d_3rd_v045_signal

def f64fy_f64_fcf_yield_dynamics_calc046_5d_3rd_v046_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc046_5d_3rd_v046_signal'] = f64fy_f64_fcf_yield_dynamics_calc046_5d_3rd_v046_signal

def f64fy_f64_fcf_yield_dynamics_calc047_10d_3rd_v047_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc047_10d_3rd_v047_signal'] = f64fy_f64_fcf_yield_dynamics_calc047_10d_3rd_v047_signal

def f64fy_f64_fcf_yield_dynamics_calc048_21d_3rd_v048_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc048_21d_3rd_v048_signal'] = f64fy_f64_fcf_yield_dynamics_calc048_21d_3rd_v048_signal

def f64fy_f64_fcf_yield_dynamics_calc049_42d_3rd_v049_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc049_42d_3rd_v049_signal'] = f64fy_f64_fcf_yield_dynamics_calc049_42d_3rd_v049_signal

def f64fy_f64_fcf_yield_dynamics_calc050_63d_3rd_v050_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc050_63d_3rd_v050_signal'] = f64fy_f64_fcf_yield_dynamics_calc050_63d_3rd_v050_signal

def f64fy_f64_fcf_yield_dynamics_calc051_126d_3rd_v051_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc051_126d_3rd_v051_signal'] = f64fy_f64_fcf_yield_dynamics_calc051_126d_3rd_v051_signal

def f64fy_f64_fcf_yield_dynamics_calc052_252d_3rd_v052_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc052_252d_3rd_v052_signal'] = f64fy_f64_fcf_yield_dynamics_calc052_252d_3rd_v052_signal

def f64fy_f64_fcf_yield_dynamics_calc053_21d_3rd_v053_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc053_21d_3rd_v053_signal'] = f64fy_f64_fcf_yield_dynamics_calc053_21d_3rd_v053_signal

def f64fy_f64_fcf_yield_dynamics_calc054_63d_3rd_v054_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc054_63d_3rd_v054_signal'] = f64fy_f64_fcf_yield_dynamics_calc054_63d_3rd_v054_signal

def f64fy_f64_fcf_yield_dynamics_calc055_5d_3rd_v055_signal(ncfo, ev):
    res = ((ncfo / ev).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc055_5d_3rd_v055_signal'] = f64fy_f64_fcf_yield_dynamics_calc055_5d_3rd_v055_signal

def f64fy_f64_fcf_yield_dynamics_calc056_21d_3rd_v056_signal(ncfo, ev):
    res = ((ncfo / ev).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc056_21d_3rd_v056_signal'] = f64fy_f64_fcf_yield_dynamics_calc056_21d_3rd_v056_signal

def f64fy_f64_fcf_yield_dynamics_calc057_10d_3rd_v057_signal(ncfo, ev):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ncfo / ev)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc057_10d_3rd_v057_signal'] = f64fy_f64_fcf_yield_dynamics_calc057_10d_3rd_v057_signal

def f64fy_f64_fcf_yield_dynamics_calc058_63d_3rd_v058_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc058_63d_3rd_v058_signal'] = f64fy_f64_fcf_yield_dynamics_calc058_63d_3rd_v058_signal

def f64fy_f64_fcf_yield_dynamics_calc059_126d_3rd_v059_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc059_126d_3rd_v059_signal'] = f64fy_f64_fcf_yield_dynamics_calc059_126d_3rd_v059_signal

def f64fy_f64_fcf_yield_dynamics_calc060_252d_3rd_v060_signal(ncfo, ev):
    res = ((ncfo / ev).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc060_252d_3rd_v060_signal'] = f64fy_f64_fcf_yield_dynamics_calc060_252d_3rd_v060_signal

def f64fy_f64_fcf_yield_dynamics_calc061_5d_3rd_v061_signal(fcf, assets):
    res = ((fcf / assets).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc061_5d_3rd_v061_signal'] = f64fy_f64_fcf_yield_dynamics_calc061_5d_3rd_v061_signal

def f64fy_f64_fcf_yield_dynamics_calc062_10d_3rd_v062_signal(fcf, assets):
    res = ((fcf / assets).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc062_10d_3rd_v062_signal'] = f64fy_f64_fcf_yield_dynamics_calc062_10d_3rd_v062_signal

def f64fy_f64_fcf_yield_dynamics_calc063_21d_3rd_v063_signal(fcf, assets):
    res = ((fcf / assets).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc063_21d_3rd_v063_signal'] = f64fy_f64_fcf_yield_dynamics_calc063_21d_3rd_v063_signal

def f64fy_f64_fcf_yield_dynamics_calc064_42d_3rd_v064_signal(fcf, assets):
    res = ((fcf / assets).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc064_42d_3rd_v064_signal'] = f64fy_f64_fcf_yield_dynamics_calc064_42d_3rd_v064_signal

def f64fy_f64_fcf_yield_dynamics_calc065_63d_3rd_v065_signal(fcf, assets):
    res = ((fcf / assets).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc065_63d_3rd_v065_signal'] = f64fy_f64_fcf_yield_dynamics_calc065_63d_3rd_v065_signal

def f64fy_f64_fcf_yield_dynamics_calc066_126d_3rd_v066_signal(fcf, assets):
    res = ((fcf / assets).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc066_126d_3rd_v066_signal'] = f64fy_f64_fcf_yield_dynamics_calc066_126d_3rd_v066_signal

def f64fy_f64_fcf_yield_dynamics_calc067_252d_3rd_v067_signal(fcf, assets):
    res = ((fcf / assets).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc067_252d_3rd_v067_signal'] = f64fy_f64_fcf_yield_dynamics_calc067_252d_3rd_v067_signal

def f64fy_f64_fcf_yield_dynamics_calc068_21d_3rd_v068_signal(fcf, assets):
    res = ((fcf / assets).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc068_21d_3rd_v068_signal'] = f64fy_f64_fcf_yield_dynamics_calc068_21d_3rd_v068_signal

def f64fy_f64_fcf_yield_dynamics_calc069_63d_3rd_v069_signal(fcf, assets):
    res = ((fcf / assets).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc069_63d_3rd_v069_signal'] = f64fy_f64_fcf_yield_dynamics_calc069_63d_3rd_v069_signal

def f64fy_f64_fcf_yield_dynamics_calc070_5d_3rd_v070_signal(fcf, assets):
    res = ((fcf / assets).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc070_5d_3rd_v070_signal'] = f64fy_f64_fcf_yield_dynamics_calc070_5d_3rd_v070_signal

def f64fy_f64_fcf_yield_dynamics_calc071_21d_3rd_v071_signal(fcf, assets):
    res = ((fcf / assets).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc071_21d_3rd_v071_signal'] = f64fy_f64_fcf_yield_dynamics_calc071_21d_3rd_v071_signal

def f64fy_f64_fcf_yield_dynamics_calc072_10d_3rd_v072_signal(fcf, assets):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / assets)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc072_10d_3rd_v072_signal'] = f64fy_f64_fcf_yield_dynamics_calc072_10d_3rd_v072_signal

def f64fy_f64_fcf_yield_dynamics_calc073_63d_3rd_v073_signal(fcf, assets):
    res = ((fcf / assets).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc073_63d_3rd_v073_signal'] = f64fy_f64_fcf_yield_dynamics_calc073_63d_3rd_v073_signal

def f64fy_f64_fcf_yield_dynamics_calc074_126d_3rd_v074_signal(fcf, assets):
    res = ((fcf / assets).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc074_126d_3rd_v074_signal'] = f64fy_f64_fcf_yield_dynamics_calc074_126d_3rd_v074_signal

def f64fy_f64_fcf_yield_dynamics_calc075_252d_3rd_v075_signal(fcf, assets):
    res = ((fcf / assets).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc075_252d_3rd_v075_signal'] = f64fy_f64_fcf_yield_dynamics_calc075_252d_3rd_v075_signal

def f64fy_f64_fcf_yield_dynamics_calc076_5d_3rd_v076_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc076_5d_3rd_v076_signal'] = f64fy_f64_fcf_yield_dynamics_calc076_5d_3rd_v076_signal

def f64fy_f64_fcf_yield_dynamics_calc077_10d_3rd_v077_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc077_10d_3rd_v077_signal'] = f64fy_f64_fcf_yield_dynamics_calc077_10d_3rd_v077_signal

def f64fy_f64_fcf_yield_dynamics_calc078_21d_3rd_v078_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc078_21d_3rd_v078_signal'] = f64fy_f64_fcf_yield_dynamics_calc078_21d_3rd_v078_signal

def f64fy_f64_fcf_yield_dynamics_calc079_42d_3rd_v079_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc079_42d_3rd_v079_signal'] = f64fy_f64_fcf_yield_dynamics_calc079_42d_3rd_v079_signal

def f64fy_f64_fcf_yield_dynamics_calc080_63d_3rd_v080_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc080_63d_3rd_v080_signal'] = f64fy_f64_fcf_yield_dynamics_calc080_63d_3rd_v080_signal

def f64fy_f64_fcf_yield_dynamics_calc081_126d_3rd_v081_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc081_126d_3rd_v081_signal'] = f64fy_f64_fcf_yield_dynamics_calc081_126d_3rd_v081_signal

def f64fy_f64_fcf_yield_dynamics_calc082_252d_3rd_v082_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc082_252d_3rd_v082_signal'] = f64fy_f64_fcf_yield_dynamics_calc082_252d_3rd_v082_signal

def f64fy_f64_fcf_yield_dynamics_calc083_21d_3rd_v083_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc083_21d_3rd_v083_signal'] = f64fy_f64_fcf_yield_dynamics_calc083_21d_3rd_v083_signal

def f64fy_f64_fcf_yield_dynamics_calc084_63d_3rd_v084_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc084_63d_3rd_v084_signal'] = f64fy_f64_fcf_yield_dynamics_calc084_63d_3rd_v084_signal

def f64fy_f64_fcf_yield_dynamics_calc085_5d_3rd_v085_signal(fcf, revenue):
    res = ((fcf / revenue).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc085_5d_3rd_v085_signal'] = f64fy_f64_fcf_yield_dynamics_calc085_5d_3rd_v085_signal

def f64fy_f64_fcf_yield_dynamics_calc086_21d_3rd_v086_signal(fcf, revenue):
    res = ((fcf / revenue).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc086_21d_3rd_v086_signal'] = f64fy_f64_fcf_yield_dynamics_calc086_21d_3rd_v086_signal

def f64fy_f64_fcf_yield_dynamics_calc087_10d_3rd_v087_signal(fcf, revenue):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / revenue)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc087_10d_3rd_v087_signal'] = f64fy_f64_fcf_yield_dynamics_calc087_10d_3rd_v087_signal

def f64fy_f64_fcf_yield_dynamics_calc088_63d_3rd_v088_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc088_63d_3rd_v088_signal'] = f64fy_f64_fcf_yield_dynamics_calc088_63d_3rd_v088_signal

def f64fy_f64_fcf_yield_dynamics_calc089_126d_3rd_v089_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc089_126d_3rd_v089_signal'] = f64fy_f64_fcf_yield_dynamics_calc089_126d_3rd_v089_signal

def f64fy_f64_fcf_yield_dynamics_calc090_252d_3rd_v090_signal(fcf, revenue):
    res = ((fcf / revenue).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc090_252d_3rd_v090_signal'] = f64fy_f64_fcf_yield_dynamics_calc090_252d_3rd_v090_signal

def f64fy_f64_fcf_yield_dynamics_calc091_5d_3rd_v091_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc091_5d_3rd_v091_signal'] = f64fy_f64_fcf_yield_dynamics_calc091_5d_3rd_v091_signal

def f64fy_f64_fcf_yield_dynamics_calc092_10d_3rd_v092_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc092_10d_3rd_v092_signal'] = f64fy_f64_fcf_yield_dynamics_calc092_10d_3rd_v092_signal

def f64fy_f64_fcf_yield_dynamics_calc093_21d_3rd_v093_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc093_21d_3rd_v093_signal'] = f64fy_f64_fcf_yield_dynamics_calc093_21d_3rd_v093_signal

def f64fy_f64_fcf_yield_dynamics_calc094_42d_3rd_v094_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc094_42d_3rd_v094_signal'] = f64fy_f64_fcf_yield_dynamics_calc094_42d_3rd_v094_signal

def f64fy_f64_fcf_yield_dynamics_calc095_63d_3rd_v095_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc095_63d_3rd_v095_signal'] = f64fy_f64_fcf_yield_dynamics_calc095_63d_3rd_v095_signal

def f64fy_f64_fcf_yield_dynamics_calc096_126d_3rd_v096_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc096_126d_3rd_v096_signal'] = f64fy_f64_fcf_yield_dynamics_calc096_126d_3rd_v096_signal

def f64fy_f64_fcf_yield_dynamics_calc097_252d_3rd_v097_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc097_252d_3rd_v097_signal'] = f64fy_f64_fcf_yield_dynamics_calc097_252d_3rd_v097_signal

def f64fy_f64_fcf_yield_dynamics_calc098_21d_3rd_v098_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc098_21d_3rd_v098_signal'] = f64fy_f64_fcf_yield_dynamics_calc098_21d_3rd_v098_signal

def f64fy_f64_fcf_yield_dynamics_calc099_63d_3rd_v099_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc099_63d_3rd_v099_signal'] = f64fy_f64_fcf_yield_dynamics_calc099_63d_3rd_v099_signal

def f64fy_f64_fcf_yield_dynamics_calc100_5d_3rd_v100_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc100_5d_3rd_v100_signal'] = f64fy_f64_fcf_yield_dynamics_calc100_5d_3rd_v100_signal

def f64fy_f64_fcf_yield_dynamics_calc101_21d_3rd_v101_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc101_21d_3rd_v101_signal'] = f64fy_f64_fcf_yield_dynamics_calc101_21d_3rd_v101_signal

def f64fy_f64_fcf_yield_dynamics_calc102_10d_3rd_v102_signal(ebitda, marketcap):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ebitda / marketcap)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc102_10d_3rd_v102_signal'] = f64fy_f64_fcf_yield_dynamics_calc102_10d_3rd_v102_signal

def f64fy_f64_fcf_yield_dynamics_calc103_63d_3rd_v103_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc103_63d_3rd_v103_signal'] = f64fy_f64_fcf_yield_dynamics_calc103_63d_3rd_v103_signal

def f64fy_f64_fcf_yield_dynamics_calc104_126d_3rd_v104_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc104_126d_3rd_v104_signal'] = f64fy_f64_fcf_yield_dynamics_calc104_126d_3rd_v104_signal

def f64fy_f64_fcf_yield_dynamics_calc105_252d_3rd_v105_signal(ebitda, marketcap):
    res = ((ebitda / marketcap).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc105_252d_3rd_v105_signal'] = f64fy_f64_fcf_yield_dynamics_calc105_252d_3rd_v105_signal

def f64fy_f64_fcf_yield_dynamics_calc106_5d_3rd_v106_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc106_5d_3rd_v106_signal'] = f64fy_f64_fcf_yield_dynamics_calc106_5d_3rd_v106_signal

def f64fy_f64_fcf_yield_dynamics_calc107_10d_3rd_v107_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc107_10d_3rd_v107_signal'] = f64fy_f64_fcf_yield_dynamics_calc107_10d_3rd_v107_signal

def f64fy_f64_fcf_yield_dynamics_calc108_21d_3rd_v108_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc108_21d_3rd_v108_signal'] = f64fy_f64_fcf_yield_dynamics_calc108_21d_3rd_v108_signal

def f64fy_f64_fcf_yield_dynamics_calc109_42d_3rd_v109_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc109_42d_3rd_v109_signal'] = f64fy_f64_fcf_yield_dynamics_calc109_42d_3rd_v109_signal

def f64fy_f64_fcf_yield_dynamics_calc110_63d_3rd_v110_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc110_63d_3rd_v110_signal'] = f64fy_f64_fcf_yield_dynamics_calc110_63d_3rd_v110_signal

def f64fy_f64_fcf_yield_dynamics_calc111_126d_3rd_v111_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc111_126d_3rd_v111_signal'] = f64fy_f64_fcf_yield_dynamics_calc111_126d_3rd_v111_signal

def f64fy_f64_fcf_yield_dynamics_calc112_252d_3rd_v112_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc112_252d_3rd_v112_signal'] = f64fy_f64_fcf_yield_dynamics_calc112_252d_3rd_v112_signal

def f64fy_f64_fcf_yield_dynamics_calc113_21d_3rd_v113_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc113_21d_3rd_v113_signal'] = f64fy_f64_fcf_yield_dynamics_calc113_21d_3rd_v113_signal

def f64fy_f64_fcf_yield_dynamics_calc114_63d_3rd_v114_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc114_63d_3rd_v114_signal'] = f64fy_f64_fcf_yield_dynamics_calc114_63d_3rd_v114_signal

def f64fy_f64_fcf_yield_dynamics_calc115_5d_3rd_v115_signal(ebitda, ev):
    res = ((ebitda / ev).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc115_5d_3rd_v115_signal'] = f64fy_f64_fcf_yield_dynamics_calc115_5d_3rd_v115_signal

def f64fy_f64_fcf_yield_dynamics_calc116_21d_3rd_v116_signal(ebitda, ev):
    res = ((ebitda / ev).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc116_21d_3rd_v116_signal'] = f64fy_f64_fcf_yield_dynamics_calc116_21d_3rd_v116_signal

def f64fy_f64_fcf_yield_dynamics_calc117_10d_3rd_v117_signal(ebitda, ev):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(ebitda / ev)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc117_10d_3rd_v117_signal'] = f64fy_f64_fcf_yield_dynamics_calc117_10d_3rd_v117_signal

def f64fy_f64_fcf_yield_dynamics_calc118_63d_3rd_v118_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc118_63d_3rd_v118_signal'] = f64fy_f64_fcf_yield_dynamics_calc118_63d_3rd_v118_signal

def f64fy_f64_fcf_yield_dynamics_calc119_126d_3rd_v119_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc119_126d_3rd_v119_signal'] = f64fy_f64_fcf_yield_dynamics_calc119_126d_3rd_v119_signal

def f64fy_f64_fcf_yield_dynamics_calc120_252d_3rd_v120_signal(ebitda, ev):
    res = ((ebitda / ev).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc120_252d_3rd_v120_signal'] = f64fy_f64_fcf_yield_dynamics_calc120_252d_3rd_v120_signal

def f64fy_f64_fcf_yield_dynamics_calc121_5d_3rd_v121_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc121_5d_3rd_v121_signal'] = f64fy_f64_fcf_yield_dynamics_calc121_5d_3rd_v121_signal

def f64fy_f64_fcf_yield_dynamics_calc122_10d_3rd_v122_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc122_10d_3rd_v122_signal'] = f64fy_f64_fcf_yield_dynamics_calc122_10d_3rd_v122_signal

def f64fy_f64_fcf_yield_dynamics_calc123_21d_3rd_v123_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc123_21d_3rd_v123_signal'] = f64fy_f64_fcf_yield_dynamics_calc123_21d_3rd_v123_signal

def f64fy_f64_fcf_yield_dynamics_calc124_42d_3rd_v124_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc124_42d_3rd_v124_signal'] = f64fy_f64_fcf_yield_dynamics_calc124_42d_3rd_v124_signal

def f64fy_f64_fcf_yield_dynamics_calc125_63d_3rd_v125_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc125_63d_3rd_v125_signal'] = f64fy_f64_fcf_yield_dynamics_calc125_63d_3rd_v125_signal

def f64fy_f64_fcf_yield_dynamics_calc126_126d_3rd_v126_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc126_126d_3rd_v126_signal'] = f64fy_f64_fcf_yield_dynamics_calc126_126d_3rd_v126_signal

def f64fy_f64_fcf_yield_dynamics_calc127_252d_3rd_v127_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc127_252d_3rd_v127_signal'] = f64fy_f64_fcf_yield_dynamics_calc127_252d_3rd_v127_signal

def f64fy_f64_fcf_yield_dynamics_calc128_21d_3rd_v128_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc128_21d_3rd_v128_signal'] = f64fy_f64_fcf_yield_dynamics_calc128_21d_3rd_v128_signal

def f64fy_f64_fcf_yield_dynamics_calc129_63d_3rd_v129_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc129_63d_3rd_v129_signal'] = f64fy_f64_fcf_yield_dynamics_calc129_63d_3rd_v129_signal

def f64fy_f64_fcf_yield_dynamics_calc130_5d_3rd_v130_signal(fcf, liabilities):
    res = ((fcf / liabilities).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc130_5d_3rd_v130_signal'] = f64fy_f64_fcf_yield_dynamics_calc130_5d_3rd_v130_signal

def f64fy_f64_fcf_yield_dynamics_calc131_21d_3rd_v131_signal(fcf, liabilities):
    res = ((fcf / liabilities).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc131_21d_3rd_v131_signal'] = f64fy_f64_fcf_yield_dynamics_calc131_21d_3rd_v131_signal

def f64fy_f64_fcf_yield_dynamics_calc132_10d_3rd_v132_signal(fcf, liabilities):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / liabilities)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc132_10d_3rd_v132_signal'] = f64fy_f64_fcf_yield_dynamics_calc132_10d_3rd_v132_signal

def f64fy_f64_fcf_yield_dynamics_calc133_63d_3rd_v133_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc133_63d_3rd_v133_signal'] = f64fy_f64_fcf_yield_dynamics_calc133_63d_3rd_v133_signal

def f64fy_f64_fcf_yield_dynamics_calc134_126d_3rd_v134_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc134_126d_3rd_v134_signal'] = f64fy_f64_fcf_yield_dynamics_calc134_126d_3rd_v134_signal

def f64fy_f64_fcf_yield_dynamics_calc135_252d_3rd_v135_signal(fcf, liabilities):
    res = ((fcf / liabilities).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc135_252d_3rd_v135_signal'] = f64fy_f64_fcf_yield_dynamics_calc135_252d_3rd_v135_signal

def f64fy_f64_fcf_yield_dynamics_calc136_5d_3rd_v136_signal(fcf, equity):
    res = ((fcf / equity).rolling(5).mean()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc136_5d_3rd_v136_signal'] = f64fy_f64_fcf_yield_dynamics_calc136_5d_3rd_v136_signal

def f64fy_f64_fcf_yield_dynamics_calc137_10d_3rd_v137_signal(fcf, equity):
    res = ((fcf / equity).rolling(10).std()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc137_10d_3rd_v137_signal'] = f64fy_f64_fcf_yield_dynamics_calc137_10d_3rd_v137_signal

def f64fy_f64_fcf_yield_dynamics_calc138_21d_3rd_v138_signal(fcf, equity):
    res = ((fcf / equity).rolling(21).var()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc138_21d_3rd_v138_signal'] = f64fy_f64_fcf_yield_dynamics_calc138_21d_3rd_v138_signal

def f64fy_f64_fcf_yield_dynamics_calc139_42d_3rd_v139_signal(fcf, equity):
    res = ((fcf / equity).rolling(42).skew()).diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc139_42d_3rd_v139_signal'] = f64fy_f64_fcf_yield_dynamics_calc139_42d_3rd_v139_signal

def f64fy_f64_fcf_yield_dynamics_calc140_63d_3rd_v140_signal(fcf, equity):
    res = ((fcf / equity).rolling(63).kurt()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc140_63d_3rd_v140_signal'] = f64fy_f64_fcf_yield_dynamics_calc140_63d_3rd_v140_signal

def f64fy_f64_fcf_yield_dynamics_calc141_126d_3rd_v141_signal(fcf, equity):
    res = ((fcf / equity).rolling(126).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc141_126d_3rd_v141_signal'] = f64fy_f64_fcf_yield_dynamics_calc141_126d_3rd_v141_signal

def f64fy_f64_fcf_yield_dynamics_calc142_252d_3rd_v142_signal(fcf, equity):
    res = ((fcf / equity).rolling(252).min()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc142_252d_3rd_v142_signal'] = f64fy_f64_fcf_yield_dynamics_calc142_252d_3rd_v142_signal

def f64fy_f64_fcf_yield_dynamics_calc143_21d_3rd_v143_signal(fcf, equity):
    res = ((fcf / equity).rolling(21).median()).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc143_21d_3rd_v143_signal'] = f64fy_f64_fcf_yield_dynamics_calc143_21d_3rd_v143_signal

def f64fy_f64_fcf_yield_dynamics_calc144_63d_3rd_v144_signal(fcf, equity):
    res = ((fcf / equity).rolling(63).rank()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc144_63d_3rd_v144_signal'] = f64fy_f64_fcf_yield_dynamics_calc144_63d_3rd_v144_signal

def f64fy_f64_fcf_yield_dynamics_calc145_5d_3rd_v145_signal(fcf, equity):
    res = ((fcf / equity).diff(5)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc145_5d_3rd_v145_signal'] = f64fy_f64_fcf_yield_dynamics_calc145_5d_3rd_v145_signal

def f64fy_f64_fcf_yield_dynamics_calc146_21d_3rd_v146_signal(fcf, equity):
    res = ((fcf / equity).pct_change(21)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc146_21d_3rd_v146_signal'] = f64fy_f64_fcf_yield_dynamics_calc146_21d_3rd_v146_signal

def f64fy_f64_fcf_yield_dynamics_calc147_10d_3rd_v147_signal(fcf, equity):
    res = ((lambda x: (x - x.rolling(10).mean()) / x.rolling(10).std())(fcf / equity)).diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc147_10d_3rd_v147_signal'] = f64fy_f64_fcf_yield_dynamics_calc147_10d_3rd_v147_signal

def f64fy_f64_fcf_yield_dynamics_calc148_63d_3rd_v148_signal(fcf, equity):
    res = ((fcf / equity).rolling(63).mean()).diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc148_63d_3rd_v148_signal'] = f64fy_f64_fcf_yield_dynamics_calc148_63d_3rd_v148_signal

def f64fy_f64_fcf_yield_dynamics_calc149_126d_3rd_v149_signal(fcf, equity):
    res = ((fcf / equity).rolling(126).std()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc149_126d_3rd_v149_signal'] = f64fy_f64_fcf_yield_dynamics_calc149_126d_3rd_v149_signal

def f64fy_f64_fcf_yield_dynamics_calc150_252d_3rd_v150_signal(fcf, equity):
    res = ((fcf / equity).rolling(252).max()).diff(42).diff(42)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f64fy_f64_fcf_yield_dynamics_calc150_252d_3rd_v150_signal'] = f64fy_f64_fcf_yield_dynamics_calc150_252d_3rd_v150_signal


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
