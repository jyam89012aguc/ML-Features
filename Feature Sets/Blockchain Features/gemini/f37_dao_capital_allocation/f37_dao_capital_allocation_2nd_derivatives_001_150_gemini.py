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


def f37dca_f37_dao_capital_allocation_calc001_15d_2nd_derivatives_v001_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc002_25d_2nd_derivatives_v002_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc003_35d_2nd_derivatives_v003_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc004_45d_2nd_derivatives_v004_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc005_55d_2nd_derivatives_v005_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc006_65d_2nd_derivatives_v006_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc007_75d_2nd_derivatives_v007_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc008_85d_2nd_derivatives_v008_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc009_95d_2nd_derivatives_v009_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc010_5d_2nd_derivatives_v010_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc011_15d_2nd_derivatives_v011_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc012_25d_2nd_derivatives_v012_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc013_35d_2nd_derivatives_v013_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc014_45d_2nd_derivatives_v014_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc015_55d_2nd_derivatives_v015_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc016_65d_2nd_derivatives_v016_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc017_75d_2nd_derivatives_v017_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc018_85d_2nd_derivatives_v018_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc019_95d_2nd_derivatives_v019_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc020_5d_2nd_derivatives_v020_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc021_15d_2nd_derivatives_v021_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc022_25d_2nd_derivatives_v022_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc023_35d_2nd_derivatives_v023_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc024_45d_2nd_derivatives_v024_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc025_55d_2nd_derivatives_v025_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc026_65d_2nd_derivatives_v026_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc027_75d_2nd_derivatives_v027_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc028_85d_2nd_derivatives_v028_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc029_95d_2nd_derivatives_v029_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc030_5d_2nd_derivatives_v030_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc031_15d_2nd_derivatives_v031_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc032_25d_2nd_derivatives_v032_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc033_35d_2nd_derivatives_v033_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc034_45d_2nd_derivatives_v034_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc035_55d_2nd_derivatives_v035_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc036_65d_2nd_derivatives_v036_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc037_75d_2nd_derivatives_v037_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc038_85d_2nd_derivatives_v038_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc039_95d_2nd_derivatives_v039_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc040_5d_2nd_derivatives_v040_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc041_15d_2nd_derivatives_v041_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc042_25d_2nd_derivatives_v042_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc043_35d_2nd_derivatives_v043_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc044_45d_2nd_derivatives_v044_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc045_55d_2nd_derivatives_v045_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc046_65d_2nd_derivatives_v046_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc047_75d_2nd_derivatives_v047_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc048_85d_2nd_derivatives_v048_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc049_95d_2nd_derivatives_v049_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc050_5d_2nd_derivatives_v050_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc051_15d_2nd_derivatives_v051_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc052_25d_2nd_derivatives_v052_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc053_35d_2nd_derivatives_v053_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc054_45d_2nd_derivatives_v054_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc055_55d_2nd_derivatives_v055_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc056_65d_2nd_derivatives_v056_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc057_75d_2nd_derivatives_v057_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc058_85d_2nd_derivatives_v058_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc059_95d_2nd_derivatives_v059_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc060_5d_2nd_derivatives_v060_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc061_15d_2nd_derivatives_v061_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc062_25d_2nd_derivatives_v062_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc063_35d_2nd_derivatives_v063_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc064_45d_2nd_derivatives_v064_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc065_55d_2nd_derivatives_v065_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc066_65d_2nd_derivatives_v066_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc067_75d_2nd_derivatives_v067_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc068_85d_2nd_derivatives_v068_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc069_95d_2nd_derivatives_v069_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc070_5d_2nd_derivatives_v070_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc071_15d_2nd_derivatives_v071_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc072_25d_2nd_derivatives_v072_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc073_35d_2nd_derivatives_v073_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc074_45d_2nd_derivatives_v074_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc075_55d_2nd_derivatives_v075_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc076_65d_2nd_derivatives_v076_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc077_75d_2nd_derivatives_v077_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc078_85d_2nd_derivatives_v078_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc079_95d_2nd_derivatives_v079_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc080_5d_2nd_derivatives_v080_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc081_15d_2nd_derivatives_v081_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc082_25d_2nd_derivatives_v082_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc083_35d_2nd_derivatives_v083_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc084_45d_2nd_derivatives_v084_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc085_55d_2nd_derivatives_v085_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc086_65d_2nd_derivatives_v086_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc087_75d_2nd_derivatives_v087_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc088_85d_2nd_derivatives_v088_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc089_95d_2nd_derivatives_v089_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc090_5d_2nd_derivatives_v090_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc091_15d_2nd_derivatives_v091_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc092_25d_2nd_derivatives_v092_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc093_35d_2nd_derivatives_v093_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc094_45d_2nd_derivatives_v094_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc095_55d_2nd_derivatives_v095_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc096_65d_2nd_derivatives_v096_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc097_75d_2nd_derivatives_v097_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc098_85d_2nd_derivatives_v098_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc099_95d_2nd_derivatives_v099_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc100_5d_2nd_derivatives_v100_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc101_15d_2nd_derivatives_v101_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc102_25d_2nd_derivatives_v102_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc103_35d_2nd_derivatives_v103_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc104_45d_2nd_derivatives_v104_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc105_55d_2nd_derivatives_v105_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc106_65d_2nd_derivatives_v106_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc107_75d_2nd_derivatives_v107_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc108_85d_2nd_derivatives_v108_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc109_95d_2nd_derivatives_v109_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc110_5d_2nd_derivatives_v110_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc111_15d_2nd_derivatives_v111_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc112_25d_2nd_derivatives_v112_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc113_35d_2nd_derivatives_v113_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc114_45d_2nd_derivatives_v114_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc115_55d_2nd_derivatives_v115_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc116_65d_2nd_derivatives_v116_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc117_75d_2nd_derivatives_v117_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc118_85d_2nd_derivatives_v118_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc119_95d_2nd_derivatives_v119_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc120_5d_2nd_derivatives_v120_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc121_15d_2nd_derivatives_v121_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc122_25d_2nd_derivatives_v122_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc123_35d_2nd_derivatives_v123_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc124_45d_2nd_derivatives_v124_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc125_55d_2nd_derivatives_v125_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc126_65d_2nd_derivatives_v126_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc127_75d_2nd_derivatives_v127_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc128_85d_2nd_derivatives_v128_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc129_95d_2nd_derivatives_v129_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc130_5d_2nd_derivatives_v130_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc131_15d_2nd_derivatives_v131_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc132_25d_2nd_derivatives_v132_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc133_35d_2nd_derivatives_v133_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc134_45d_2nd_derivatives_v134_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc135_55d_2nd_derivatives_v135_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc136_65d_2nd_derivatives_v136_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc137_75d_2nd_derivatives_v137_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc138_85d_2nd_derivatives_v138_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc139_95d_2nd_derivatives_v139_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc140_5d_2nd_derivatives_v140_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc141_15d_2nd_derivatives_v141_signal(capex):
    res = _roc(_sma(capex, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc142_25d_2nd_derivatives_v142_signal(capex):
    res = _roc(_sma(capex, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc143_35d_2nd_derivatives_v143_signal(capex):
    res = _roc(_sma(capex, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc144_45d_2nd_derivatives_v144_signal(capex):
    res = _roc(_sma(capex, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc145_55d_2nd_derivatives_v145_signal(capex):
    res = _roc(_sma(capex, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc146_65d_2nd_derivatives_v146_signal(capex):
    res = _roc(_sma(capex, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc147_75d_2nd_derivatives_v147_signal(capex):
    res = _roc(_sma(capex, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc148_85d_2nd_derivatives_v148_signal(capex):
    res = _roc(_sma(capex, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc149_95d_2nd_derivatives_v149_signal(capex):
    res = _roc(_sma(capex, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc150_5d_2nd_derivatives_v150_signal(capex):
    res = _roc(_sma(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['capex', 'revenue', 'assets']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f37dca_'))]
    
    print(f"Testing {{len(funcs)}} functions for f37_dao_capital_allocation...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f37dca_'))]}

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
