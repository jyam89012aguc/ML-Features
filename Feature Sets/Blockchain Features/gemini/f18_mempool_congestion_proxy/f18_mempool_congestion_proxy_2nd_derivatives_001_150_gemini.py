import inspect
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _roc(s, w):
    return s.pct_change(w)

def _zscore(s, w):
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)


def f18mcp_f18_mempool_congestion_proxy_calc001_15d_2nd_derivatives_v001_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc002_25d_2nd_derivatives_v002_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc003_35d_2nd_derivatives_v003_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc004_45d_2nd_derivatives_v004_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc005_55d_2nd_derivatives_v005_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc006_65d_2nd_derivatives_v006_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc007_75d_2nd_derivatives_v007_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc008_85d_2nd_derivatives_v008_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc009_95d_2nd_derivatives_v009_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc010_5d_2nd_derivatives_v010_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc011_15d_2nd_derivatives_v011_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc012_25d_2nd_derivatives_v012_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc013_35d_2nd_derivatives_v013_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc014_45d_2nd_derivatives_v014_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc015_55d_2nd_derivatives_v015_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc016_65d_2nd_derivatives_v016_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc017_75d_2nd_derivatives_v017_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc018_85d_2nd_derivatives_v018_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc019_95d_2nd_derivatives_v019_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc020_5d_2nd_derivatives_v020_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc021_15d_2nd_derivatives_v021_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc022_25d_2nd_derivatives_v022_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc023_35d_2nd_derivatives_v023_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc024_45d_2nd_derivatives_v024_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc025_55d_2nd_derivatives_v025_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc026_65d_2nd_derivatives_v026_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc027_75d_2nd_derivatives_v027_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc028_85d_2nd_derivatives_v028_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc029_95d_2nd_derivatives_v029_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc030_5d_2nd_derivatives_v030_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc031_15d_2nd_derivatives_v031_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc032_25d_2nd_derivatives_v032_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc033_35d_2nd_derivatives_v033_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc034_45d_2nd_derivatives_v034_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc035_55d_2nd_derivatives_v035_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc036_65d_2nd_derivatives_v036_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc037_75d_2nd_derivatives_v037_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc038_85d_2nd_derivatives_v038_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc039_95d_2nd_derivatives_v039_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc040_5d_2nd_derivatives_v040_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc041_15d_2nd_derivatives_v041_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc042_25d_2nd_derivatives_v042_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc043_35d_2nd_derivatives_v043_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc044_45d_2nd_derivatives_v044_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc045_55d_2nd_derivatives_v045_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc046_65d_2nd_derivatives_v046_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc047_75d_2nd_derivatives_v047_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc048_85d_2nd_derivatives_v048_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc049_95d_2nd_derivatives_v049_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc050_5d_2nd_derivatives_v050_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc051_15d_2nd_derivatives_v051_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc052_25d_2nd_derivatives_v052_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc053_35d_2nd_derivatives_v053_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc054_45d_2nd_derivatives_v054_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc055_55d_2nd_derivatives_v055_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc056_65d_2nd_derivatives_v056_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc057_75d_2nd_derivatives_v057_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc058_85d_2nd_derivatives_v058_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc059_95d_2nd_derivatives_v059_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc060_5d_2nd_derivatives_v060_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc061_15d_2nd_derivatives_v061_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc062_25d_2nd_derivatives_v062_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc063_35d_2nd_derivatives_v063_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc064_45d_2nd_derivatives_v064_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc065_55d_2nd_derivatives_v065_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc066_65d_2nd_derivatives_v066_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc067_75d_2nd_derivatives_v067_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc068_85d_2nd_derivatives_v068_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc069_95d_2nd_derivatives_v069_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc070_5d_2nd_derivatives_v070_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc071_15d_2nd_derivatives_v071_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc072_25d_2nd_derivatives_v072_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc073_35d_2nd_derivatives_v073_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc074_45d_2nd_derivatives_v074_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc075_55d_2nd_derivatives_v075_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc076_65d_2nd_derivatives_v076_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc077_75d_2nd_derivatives_v077_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc078_85d_2nd_derivatives_v078_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc079_95d_2nd_derivatives_v079_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc080_5d_2nd_derivatives_v080_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc081_15d_2nd_derivatives_v081_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc082_25d_2nd_derivatives_v082_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc083_35d_2nd_derivatives_v083_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc084_45d_2nd_derivatives_v084_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc085_55d_2nd_derivatives_v085_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc086_65d_2nd_derivatives_v086_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc087_75d_2nd_derivatives_v087_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc088_85d_2nd_derivatives_v088_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc089_95d_2nd_derivatives_v089_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc090_5d_2nd_derivatives_v090_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc091_15d_2nd_derivatives_v091_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc092_25d_2nd_derivatives_v092_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc093_35d_2nd_derivatives_v093_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc094_45d_2nd_derivatives_v094_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc095_55d_2nd_derivatives_v095_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc096_65d_2nd_derivatives_v096_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc097_75d_2nd_derivatives_v097_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc098_85d_2nd_derivatives_v098_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc099_95d_2nd_derivatives_v099_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc100_5d_2nd_derivatives_v100_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc101_15d_2nd_derivatives_v101_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc102_25d_2nd_derivatives_v102_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc103_35d_2nd_derivatives_v103_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc104_45d_2nd_derivatives_v104_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc105_55d_2nd_derivatives_v105_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc106_65d_2nd_derivatives_v106_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc107_75d_2nd_derivatives_v107_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc108_85d_2nd_derivatives_v108_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc109_95d_2nd_derivatives_v109_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc110_5d_2nd_derivatives_v110_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc111_15d_2nd_derivatives_v111_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc112_25d_2nd_derivatives_v112_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc113_35d_2nd_derivatives_v113_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc114_45d_2nd_derivatives_v114_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc115_55d_2nd_derivatives_v115_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc116_65d_2nd_derivatives_v116_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc117_75d_2nd_derivatives_v117_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc118_85d_2nd_derivatives_v118_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc119_95d_2nd_derivatives_v119_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc120_5d_2nd_derivatives_v120_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc121_15d_2nd_derivatives_v121_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc122_25d_2nd_derivatives_v122_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc123_35d_2nd_derivatives_v123_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc124_45d_2nd_derivatives_v124_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc125_55d_2nd_derivatives_v125_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc126_65d_2nd_derivatives_v126_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc127_75d_2nd_derivatives_v127_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc128_85d_2nd_derivatives_v128_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc129_95d_2nd_derivatives_v129_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc130_5d_2nd_derivatives_v130_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc131_15d_2nd_derivatives_v131_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc132_25d_2nd_derivatives_v132_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc133_35d_2nd_derivatives_v133_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc134_45d_2nd_derivatives_v134_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc135_55d_2nd_derivatives_v135_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc136_65d_2nd_derivatives_v136_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc137_75d_2nd_derivatives_v137_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc138_85d_2nd_derivatives_v138_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc139_95d_2nd_derivatives_v139_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc140_5d_2nd_derivatives_v140_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc141_15d_2nd_derivatives_v141_signal(volume):
    res = _roc((_sma(close, 15) / _sma(volume, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc142_25d_2nd_derivatives_v142_signal(volume):
    res = _roc((_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc143_35d_2nd_derivatives_v143_signal(volume):
    res = _roc((_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc144_45d_2nd_derivatives_v144_signal(volume):
    res = _roc((_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc145_55d_2nd_derivatives_v145_signal(volume):
    res = _roc((_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc146_65d_2nd_derivatives_v146_signal(volume):
    res = _roc((_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc147_75d_2nd_derivatives_v147_signal(volume):
    res = _roc((_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc148_85d_2nd_derivatives_v148_signal(volume):
    res = _roc((_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc149_95d_2nd_derivatives_v149_signal(volume):
    res = _roc((_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18mcp_f18_mempool_congestion_proxy_calc150_5d_2nd_derivatives_v150_signal(volume):
    res = _roc((_sma(close, 5) / _sma(volume, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['high', 'low', 'volume']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f18mcp_'))]
    
    print(f"Testing {{len(funcs)}} functions for f18_mempool_congestion_proxy...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f18mcp_'))]}

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
