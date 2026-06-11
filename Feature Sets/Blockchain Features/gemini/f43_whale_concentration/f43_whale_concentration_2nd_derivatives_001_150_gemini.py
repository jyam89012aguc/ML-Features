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


def f43whl_f43_whale_concentration_calc001_15d_2nd_derivatives_v001_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc002_25d_2nd_derivatives_v002_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc003_35d_2nd_derivatives_v003_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc004_45d_2nd_derivatives_v004_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc005_55d_2nd_derivatives_v005_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc006_65d_2nd_derivatives_v006_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc007_75d_2nd_derivatives_v007_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc008_85d_2nd_derivatives_v008_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc009_95d_2nd_derivatives_v009_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc010_5d_2nd_derivatives_v010_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc011_15d_2nd_derivatives_v011_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc012_25d_2nd_derivatives_v012_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc013_35d_2nd_derivatives_v013_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc014_45d_2nd_derivatives_v014_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc015_55d_2nd_derivatives_v015_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc016_65d_2nd_derivatives_v016_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc017_75d_2nd_derivatives_v017_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc018_85d_2nd_derivatives_v018_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc019_95d_2nd_derivatives_v019_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc020_5d_2nd_derivatives_v020_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc021_15d_2nd_derivatives_v021_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc022_25d_2nd_derivatives_v022_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc023_35d_2nd_derivatives_v023_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc024_45d_2nd_derivatives_v024_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc025_55d_2nd_derivatives_v025_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc026_65d_2nd_derivatives_v026_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc027_75d_2nd_derivatives_v027_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc028_85d_2nd_derivatives_v028_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc029_95d_2nd_derivatives_v029_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc030_5d_2nd_derivatives_v030_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc031_15d_2nd_derivatives_v031_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc032_25d_2nd_derivatives_v032_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc033_35d_2nd_derivatives_v033_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc034_45d_2nd_derivatives_v034_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc035_55d_2nd_derivatives_v035_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc036_65d_2nd_derivatives_v036_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc037_75d_2nd_derivatives_v037_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc038_85d_2nd_derivatives_v038_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc039_95d_2nd_derivatives_v039_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc040_5d_2nd_derivatives_v040_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc041_15d_2nd_derivatives_v041_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc042_25d_2nd_derivatives_v042_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc043_35d_2nd_derivatives_v043_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc044_45d_2nd_derivatives_v044_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc045_55d_2nd_derivatives_v045_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc046_65d_2nd_derivatives_v046_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc047_75d_2nd_derivatives_v047_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc048_85d_2nd_derivatives_v048_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc049_95d_2nd_derivatives_v049_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc050_5d_2nd_derivatives_v050_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc051_15d_2nd_derivatives_v051_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc052_25d_2nd_derivatives_v052_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc053_35d_2nd_derivatives_v053_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc054_45d_2nd_derivatives_v054_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc055_55d_2nd_derivatives_v055_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc056_65d_2nd_derivatives_v056_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc057_75d_2nd_derivatives_v057_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc058_85d_2nd_derivatives_v058_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc059_95d_2nd_derivatives_v059_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc060_5d_2nd_derivatives_v060_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc061_15d_2nd_derivatives_v061_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc062_25d_2nd_derivatives_v062_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc063_35d_2nd_derivatives_v063_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc064_45d_2nd_derivatives_v064_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc065_55d_2nd_derivatives_v065_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc066_65d_2nd_derivatives_v066_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc067_75d_2nd_derivatives_v067_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc068_85d_2nd_derivatives_v068_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc069_95d_2nd_derivatives_v069_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc070_5d_2nd_derivatives_v070_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc071_15d_2nd_derivatives_v071_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc072_25d_2nd_derivatives_v072_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc073_35d_2nd_derivatives_v073_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc074_45d_2nd_derivatives_v074_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc075_55d_2nd_derivatives_v075_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc076_65d_2nd_derivatives_v076_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc077_75d_2nd_derivatives_v077_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc078_85d_2nd_derivatives_v078_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc079_95d_2nd_derivatives_v079_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc080_5d_2nd_derivatives_v080_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc081_15d_2nd_derivatives_v081_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc082_25d_2nd_derivatives_v082_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc083_35d_2nd_derivatives_v083_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc084_45d_2nd_derivatives_v084_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc085_55d_2nd_derivatives_v085_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc086_65d_2nd_derivatives_v086_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc087_75d_2nd_derivatives_v087_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc088_85d_2nd_derivatives_v088_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc089_95d_2nd_derivatives_v089_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc090_5d_2nd_derivatives_v090_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc091_15d_2nd_derivatives_v091_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc092_25d_2nd_derivatives_v092_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc093_35d_2nd_derivatives_v093_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc094_45d_2nd_derivatives_v094_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc095_55d_2nd_derivatives_v095_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc096_65d_2nd_derivatives_v096_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc097_75d_2nd_derivatives_v097_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc098_85d_2nd_derivatives_v098_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc099_95d_2nd_derivatives_v099_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc100_5d_2nd_derivatives_v100_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc101_15d_2nd_derivatives_v101_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc102_25d_2nd_derivatives_v102_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc103_35d_2nd_derivatives_v103_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc104_45d_2nd_derivatives_v104_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc105_55d_2nd_derivatives_v105_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc106_65d_2nd_derivatives_v106_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc107_75d_2nd_derivatives_v107_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc108_85d_2nd_derivatives_v108_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc109_95d_2nd_derivatives_v109_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc110_5d_2nd_derivatives_v110_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc111_15d_2nd_derivatives_v111_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc112_25d_2nd_derivatives_v112_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc113_35d_2nd_derivatives_v113_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc114_45d_2nd_derivatives_v114_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc115_55d_2nd_derivatives_v115_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc116_65d_2nd_derivatives_v116_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc117_75d_2nd_derivatives_v117_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc118_85d_2nd_derivatives_v118_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc119_95d_2nd_derivatives_v119_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc120_5d_2nd_derivatives_v120_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc121_15d_2nd_derivatives_v121_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc122_25d_2nd_derivatives_v122_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc123_35d_2nd_derivatives_v123_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc124_45d_2nd_derivatives_v124_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc125_55d_2nd_derivatives_v125_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc126_65d_2nd_derivatives_v126_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc127_75d_2nd_derivatives_v127_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc128_85d_2nd_derivatives_v128_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc129_95d_2nd_derivatives_v129_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc130_5d_2nd_derivatives_v130_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc131_15d_2nd_derivatives_v131_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc132_25d_2nd_derivatives_v132_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc133_35d_2nd_derivatives_v133_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc134_45d_2nd_derivatives_v134_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc135_55d_2nd_derivatives_v135_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc136_65d_2nd_derivatives_v136_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc137_75d_2nd_derivatives_v137_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc138_85d_2nd_derivatives_v138_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc139_95d_2nd_derivatives_v139_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc140_5d_2nd_derivatives_v140_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc141_15d_2nd_derivatives_v141_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc142_25d_2nd_derivatives_v142_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc143_35d_2nd_derivatives_v143_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc144_45d_2nd_derivatives_v144_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc145_55d_2nd_derivatives_v145_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc146_65d_2nd_derivatives_v146_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc147_75d_2nd_derivatives_v147_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc148_85d_2nd_derivatives_v148_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc149_95d_2nd_derivatives_v149_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43whl_f43_whale_concentration_calc150_5d_2nd_derivatives_v150_signal(sf3a_shares):
    res = _roc(_sma(sf3a_shares, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['sf3a_shares', 'marketcap', 'sf3b_shares']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f43whl_'))]
    
    print(f"Testing {{len(funcs)}} functions for f43_whale_concentration...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f43whl_'))]}

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
