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


def f36tmgt_f36_treasury_management_calc001_15d_2nd_derivatives_v001_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc002_25d_2nd_derivatives_v002_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc003_35d_2nd_derivatives_v003_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc004_45d_2nd_derivatives_v004_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc005_55d_2nd_derivatives_v005_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc006_65d_2nd_derivatives_v006_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc007_75d_2nd_derivatives_v007_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc008_85d_2nd_derivatives_v008_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc009_95d_2nd_derivatives_v009_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc010_5d_2nd_derivatives_v010_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc011_15d_2nd_derivatives_v011_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc012_25d_2nd_derivatives_v012_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc013_35d_2nd_derivatives_v013_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc014_45d_2nd_derivatives_v014_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc015_55d_2nd_derivatives_v015_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc016_65d_2nd_derivatives_v016_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc017_75d_2nd_derivatives_v017_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc018_85d_2nd_derivatives_v018_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc019_95d_2nd_derivatives_v019_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc020_5d_2nd_derivatives_v020_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc021_15d_2nd_derivatives_v021_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc022_25d_2nd_derivatives_v022_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc023_35d_2nd_derivatives_v023_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc024_45d_2nd_derivatives_v024_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc025_55d_2nd_derivatives_v025_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc026_65d_2nd_derivatives_v026_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc027_75d_2nd_derivatives_v027_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc028_85d_2nd_derivatives_v028_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc029_95d_2nd_derivatives_v029_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc030_5d_2nd_derivatives_v030_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc031_15d_2nd_derivatives_v031_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc032_25d_2nd_derivatives_v032_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc033_35d_2nd_derivatives_v033_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc034_45d_2nd_derivatives_v034_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc035_55d_2nd_derivatives_v035_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc036_65d_2nd_derivatives_v036_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc037_75d_2nd_derivatives_v037_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc038_85d_2nd_derivatives_v038_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc039_95d_2nd_derivatives_v039_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc040_5d_2nd_derivatives_v040_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc041_15d_2nd_derivatives_v041_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc042_25d_2nd_derivatives_v042_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc043_35d_2nd_derivatives_v043_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc044_45d_2nd_derivatives_v044_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc045_55d_2nd_derivatives_v045_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc046_65d_2nd_derivatives_v046_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc047_75d_2nd_derivatives_v047_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc048_85d_2nd_derivatives_v048_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc049_95d_2nd_derivatives_v049_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc050_5d_2nd_derivatives_v050_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc051_15d_2nd_derivatives_v051_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc052_25d_2nd_derivatives_v052_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc053_35d_2nd_derivatives_v053_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc054_45d_2nd_derivatives_v054_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc055_55d_2nd_derivatives_v055_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc056_65d_2nd_derivatives_v056_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc057_75d_2nd_derivatives_v057_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc058_85d_2nd_derivatives_v058_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc059_95d_2nd_derivatives_v059_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc060_5d_2nd_derivatives_v060_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc061_15d_2nd_derivatives_v061_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc062_25d_2nd_derivatives_v062_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc063_35d_2nd_derivatives_v063_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc064_45d_2nd_derivatives_v064_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc065_55d_2nd_derivatives_v065_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc066_65d_2nd_derivatives_v066_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc067_75d_2nd_derivatives_v067_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc068_85d_2nd_derivatives_v068_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc069_95d_2nd_derivatives_v069_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc070_5d_2nd_derivatives_v070_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc071_15d_2nd_derivatives_v071_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc072_25d_2nd_derivatives_v072_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc073_35d_2nd_derivatives_v073_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc074_45d_2nd_derivatives_v074_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc075_55d_2nd_derivatives_v075_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc076_65d_2nd_derivatives_v076_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc077_75d_2nd_derivatives_v077_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc078_85d_2nd_derivatives_v078_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc079_95d_2nd_derivatives_v079_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc080_5d_2nd_derivatives_v080_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc081_15d_2nd_derivatives_v081_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc082_25d_2nd_derivatives_v082_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc083_35d_2nd_derivatives_v083_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc084_45d_2nd_derivatives_v084_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc085_55d_2nd_derivatives_v085_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc086_65d_2nd_derivatives_v086_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc087_75d_2nd_derivatives_v087_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc088_85d_2nd_derivatives_v088_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc089_95d_2nd_derivatives_v089_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc090_5d_2nd_derivatives_v090_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc091_15d_2nd_derivatives_v091_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc092_25d_2nd_derivatives_v092_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc093_35d_2nd_derivatives_v093_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc094_45d_2nd_derivatives_v094_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc095_55d_2nd_derivatives_v095_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc096_65d_2nd_derivatives_v096_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc097_75d_2nd_derivatives_v097_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc098_85d_2nd_derivatives_v098_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc099_95d_2nd_derivatives_v099_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc100_5d_2nd_derivatives_v100_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc101_15d_2nd_derivatives_v101_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc102_25d_2nd_derivatives_v102_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc103_35d_2nd_derivatives_v103_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc104_45d_2nd_derivatives_v104_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc105_55d_2nd_derivatives_v105_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc106_65d_2nd_derivatives_v106_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc107_75d_2nd_derivatives_v107_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc108_85d_2nd_derivatives_v108_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc109_95d_2nd_derivatives_v109_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc110_5d_2nd_derivatives_v110_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc111_15d_2nd_derivatives_v111_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc112_25d_2nd_derivatives_v112_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc113_35d_2nd_derivatives_v113_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc114_45d_2nd_derivatives_v114_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc115_55d_2nd_derivatives_v115_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc116_65d_2nd_derivatives_v116_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc117_75d_2nd_derivatives_v117_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc118_85d_2nd_derivatives_v118_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc119_95d_2nd_derivatives_v119_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc120_5d_2nd_derivatives_v120_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc121_15d_2nd_derivatives_v121_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc122_25d_2nd_derivatives_v122_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc123_35d_2nd_derivatives_v123_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc124_45d_2nd_derivatives_v124_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc125_55d_2nd_derivatives_v125_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc126_65d_2nd_derivatives_v126_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc127_75d_2nd_derivatives_v127_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc128_85d_2nd_derivatives_v128_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc129_95d_2nd_derivatives_v129_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc130_5d_2nd_derivatives_v130_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc131_15d_2nd_derivatives_v131_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc132_25d_2nd_derivatives_v132_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc133_35d_2nd_derivatives_v133_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc134_45d_2nd_derivatives_v134_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc135_55d_2nd_derivatives_v135_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc136_65d_2nd_derivatives_v136_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc137_75d_2nd_derivatives_v137_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc138_85d_2nd_derivatives_v138_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc139_95d_2nd_derivatives_v139_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc140_5d_2nd_derivatives_v140_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc141_15d_2nd_derivatives_v141_signal(fcf):
    res = _roc(_sma(fcf, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc142_25d_2nd_derivatives_v142_signal(fcf):
    res = _roc(_sma(fcf, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc143_35d_2nd_derivatives_v143_signal(fcf):
    res = _roc(_sma(fcf, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc144_45d_2nd_derivatives_v144_signal(fcf):
    res = _roc(_sma(fcf, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc145_55d_2nd_derivatives_v145_signal(fcf):
    res = _roc(_sma(fcf, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc146_65d_2nd_derivatives_v146_signal(fcf):
    res = _roc(_sma(fcf, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc147_75d_2nd_derivatives_v147_signal(fcf):
    res = _roc(_sma(fcf, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc148_85d_2nd_derivatives_v148_signal(fcf):
    res = _roc(_sma(fcf, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc149_95d_2nd_derivatives_v149_signal(fcf):
    res = _roc(_sma(fcf, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36tmgt_f36_treasury_management_calc150_5d_2nd_derivatives_v150_signal(fcf):
    res = _roc(_sma(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['fcf', 'debt', 'ncfo']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f36tmgt_'))]
    
    print(f"Testing {{len(funcs)}} functions for f36_treasury_management...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f36tmgt_'))]}

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

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
