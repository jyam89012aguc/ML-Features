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


def f33mcs_f33_mining_cost_structure_calc001_15d_2nd_derivatives_v001_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc002_25d_2nd_derivatives_v002_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc003_35d_2nd_derivatives_v003_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc004_45d_2nd_derivatives_v004_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc005_55d_2nd_derivatives_v005_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc006_65d_2nd_derivatives_v006_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc007_75d_2nd_derivatives_v007_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc008_85d_2nd_derivatives_v008_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc009_95d_2nd_derivatives_v009_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc010_5d_2nd_derivatives_v010_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc011_15d_2nd_derivatives_v011_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc012_25d_2nd_derivatives_v012_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc013_35d_2nd_derivatives_v013_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc014_45d_2nd_derivatives_v014_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc015_55d_2nd_derivatives_v015_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc016_65d_2nd_derivatives_v016_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc017_75d_2nd_derivatives_v017_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc018_85d_2nd_derivatives_v018_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc019_95d_2nd_derivatives_v019_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc020_5d_2nd_derivatives_v020_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc021_15d_2nd_derivatives_v021_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc022_25d_2nd_derivatives_v022_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc023_35d_2nd_derivatives_v023_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc024_45d_2nd_derivatives_v024_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc025_55d_2nd_derivatives_v025_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc026_65d_2nd_derivatives_v026_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc027_75d_2nd_derivatives_v027_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc028_85d_2nd_derivatives_v028_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc029_95d_2nd_derivatives_v029_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc030_5d_2nd_derivatives_v030_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc031_15d_2nd_derivatives_v031_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc032_25d_2nd_derivatives_v032_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc033_35d_2nd_derivatives_v033_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc034_45d_2nd_derivatives_v034_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc035_55d_2nd_derivatives_v035_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc036_65d_2nd_derivatives_v036_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc037_75d_2nd_derivatives_v037_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc038_85d_2nd_derivatives_v038_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc039_95d_2nd_derivatives_v039_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc040_5d_2nd_derivatives_v040_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc041_15d_2nd_derivatives_v041_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc042_25d_2nd_derivatives_v042_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc043_35d_2nd_derivatives_v043_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc044_45d_2nd_derivatives_v044_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc045_55d_2nd_derivatives_v045_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc046_65d_2nd_derivatives_v046_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc047_75d_2nd_derivatives_v047_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc048_85d_2nd_derivatives_v048_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc049_95d_2nd_derivatives_v049_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc050_5d_2nd_derivatives_v050_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc051_15d_2nd_derivatives_v051_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc052_25d_2nd_derivatives_v052_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc053_35d_2nd_derivatives_v053_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc054_45d_2nd_derivatives_v054_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc055_55d_2nd_derivatives_v055_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc056_65d_2nd_derivatives_v056_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc057_75d_2nd_derivatives_v057_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc058_85d_2nd_derivatives_v058_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc059_95d_2nd_derivatives_v059_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc060_5d_2nd_derivatives_v060_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc061_15d_2nd_derivatives_v061_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc062_25d_2nd_derivatives_v062_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc063_35d_2nd_derivatives_v063_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc064_45d_2nd_derivatives_v064_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc065_55d_2nd_derivatives_v065_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc066_65d_2nd_derivatives_v066_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc067_75d_2nd_derivatives_v067_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc068_85d_2nd_derivatives_v068_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc069_95d_2nd_derivatives_v069_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc070_5d_2nd_derivatives_v070_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc071_15d_2nd_derivatives_v071_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc072_25d_2nd_derivatives_v072_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc073_35d_2nd_derivatives_v073_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc074_45d_2nd_derivatives_v074_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc075_55d_2nd_derivatives_v075_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc076_65d_2nd_derivatives_v076_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc077_75d_2nd_derivatives_v077_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc078_85d_2nd_derivatives_v078_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc079_95d_2nd_derivatives_v079_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc080_5d_2nd_derivatives_v080_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc081_15d_2nd_derivatives_v081_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc082_25d_2nd_derivatives_v082_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc083_35d_2nd_derivatives_v083_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc084_45d_2nd_derivatives_v084_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc085_55d_2nd_derivatives_v085_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc086_65d_2nd_derivatives_v086_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc087_75d_2nd_derivatives_v087_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc088_85d_2nd_derivatives_v088_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc089_95d_2nd_derivatives_v089_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc090_5d_2nd_derivatives_v090_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc091_15d_2nd_derivatives_v091_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc092_25d_2nd_derivatives_v092_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc093_35d_2nd_derivatives_v093_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc094_45d_2nd_derivatives_v094_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc095_55d_2nd_derivatives_v095_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc096_65d_2nd_derivatives_v096_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc097_75d_2nd_derivatives_v097_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc098_85d_2nd_derivatives_v098_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc099_95d_2nd_derivatives_v099_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc100_5d_2nd_derivatives_v100_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc101_15d_2nd_derivatives_v101_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc102_25d_2nd_derivatives_v102_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc103_35d_2nd_derivatives_v103_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc104_45d_2nd_derivatives_v104_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc105_55d_2nd_derivatives_v105_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc106_65d_2nd_derivatives_v106_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc107_75d_2nd_derivatives_v107_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc108_85d_2nd_derivatives_v108_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc109_95d_2nd_derivatives_v109_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc110_5d_2nd_derivatives_v110_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc111_15d_2nd_derivatives_v111_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc112_25d_2nd_derivatives_v112_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc113_35d_2nd_derivatives_v113_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc114_45d_2nd_derivatives_v114_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc115_55d_2nd_derivatives_v115_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc116_65d_2nd_derivatives_v116_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc117_75d_2nd_derivatives_v117_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc118_85d_2nd_derivatives_v118_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc119_95d_2nd_derivatives_v119_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc120_5d_2nd_derivatives_v120_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc121_15d_2nd_derivatives_v121_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc122_25d_2nd_derivatives_v122_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc123_35d_2nd_derivatives_v123_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc124_45d_2nd_derivatives_v124_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc125_55d_2nd_derivatives_v125_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc126_65d_2nd_derivatives_v126_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc127_75d_2nd_derivatives_v127_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc128_85d_2nd_derivatives_v128_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc129_95d_2nd_derivatives_v129_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc130_5d_2nd_derivatives_v130_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc131_15d_2nd_derivatives_v131_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc132_25d_2nd_derivatives_v132_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc133_35d_2nd_derivatives_v133_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc134_45d_2nd_derivatives_v134_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc135_55d_2nd_derivatives_v135_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc136_65d_2nd_derivatives_v136_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc137_75d_2nd_derivatives_v137_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc138_85d_2nd_derivatives_v138_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc139_95d_2nd_derivatives_v139_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc140_5d_2nd_derivatives_v140_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc141_15d_2nd_derivatives_v141_signal(opinc):
    res = _roc(_sma(opinc, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc142_25d_2nd_derivatives_v142_signal(opinc):
    res = _roc(_sma(opinc, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc143_35d_2nd_derivatives_v143_signal(opinc):
    res = _roc(_sma(opinc, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc144_45d_2nd_derivatives_v144_signal(opinc):
    res = _roc(_sma(opinc, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc145_55d_2nd_derivatives_v145_signal(opinc):
    res = _roc(_sma(opinc, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc146_65d_2nd_derivatives_v146_signal(opinc):
    res = _roc(_sma(opinc, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc147_75d_2nd_derivatives_v147_signal(opinc):
    res = _roc(_sma(opinc, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc148_85d_2nd_derivatives_v148_signal(opinc):
    res = _roc(_sma(opinc, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc149_95d_2nd_derivatives_v149_signal(opinc):
    res = _roc(_sma(opinc, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33mcs_f33_mining_cost_structure_calc150_5d_2nd_derivatives_v150_signal(opinc):
    res = _roc(_sma(opinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['opinc', 'revenue', 'ebitda']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f33mcs_'))]
    
    print(f"Testing {{len(funcs)}} functions for f33_mining_cost_structure...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f33mcs_'))]}

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
