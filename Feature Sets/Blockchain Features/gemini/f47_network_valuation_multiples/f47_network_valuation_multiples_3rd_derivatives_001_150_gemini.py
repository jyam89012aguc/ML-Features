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


def f47nvm_f47_network_valuation_multiples_calc001_15d_3rd_derivatives_v001_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc002_25d_3rd_derivatives_v002_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc003_35d_3rd_derivatives_v003_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc004_45d_3rd_derivatives_v004_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc005_55d_3rd_derivatives_v005_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc006_65d_3rd_derivatives_v006_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc007_75d_3rd_derivatives_v007_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc008_85d_3rd_derivatives_v008_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc009_95d_3rd_derivatives_v009_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc010_5d_3rd_derivatives_v010_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc011_15d_3rd_derivatives_v011_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc012_25d_3rd_derivatives_v012_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc013_35d_3rd_derivatives_v013_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc014_45d_3rd_derivatives_v014_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc015_55d_3rd_derivatives_v015_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc016_65d_3rd_derivatives_v016_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc017_75d_3rd_derivatives_v017_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc018_85d_3rd_derivatives_v018_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc019_95d_3rd_derivatives_v019_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc020_5d_3rd_derivatives_v020_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc021_15d_3rd_derivatives_v021_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc022_25d_3rd_derivatives_v022_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc023_35d_3rd_derivatives_v023_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc024_45d_3rd_derivatives_v024_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc025_55d_3rd_derivatives_v025_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc026_65d_3rd_derivatives_v026_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc027_75d_3rd_derivatives_v027_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc028_85d_3rd_derivatives_v028_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc029_95d_3rd_derivatives_v029_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc030_5d_3rd_derivatives_v030_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc031_15d_3rd_derivatives_v031_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc032_25d_3rd_derivatives_v032_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc033_35d_3rd_derivatives_v033_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc034_45d_3rd_derivatives_v034_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc035_55d_3rd_derivatives_v035_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc036_65d_3rd_derivatives_v036_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc037_75d_3rd_derivatives_v037_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc038_85d_3rd_derivatives_v038_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc039_95d_3rd_derivatives_v039_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc040_5d_3rd_derivatives_v040_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc041_15d_3rd_derivatives_v041_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc042_25d_3rd_derivatives_v042_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc043_35d_3rd_derivatives_v043_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc044_45d_3rd_derivatives_v044_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc045_55d_3rd_derivatives_v045_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc046_65d_3rd_derivatives_v046_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc047_75d_3rd_derivatives_v047_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc048_85d_3rd_derivatives_v048_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc049_95d_3rd_derivatives_v049_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc050_5d_3rd_derivatives_v050_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc051_15d_3rd_derivatives_v051_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc052_25d_3rd_derivatives_v052_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc053_35d_3rd_derivatives_v053_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc054_45d_3rd_derivatives_v054_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc055_55d_3rd_derivatives_v055_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc056_65d_3rd_derivatives_v056_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc057_75d_3rd_derivatives_v057_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc058_85d_3rd_derivatives_v058_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc059_95d_3rd_derivatives_v059_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc060_5d_3rd_derivatives_v060_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc061_15d_3rd_derivatives_v061_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc062_25d_3rd_derivatives_v062_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc063_35d_3rd_derivatives_v063_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc064_45d_3rd_derivatives_v064_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc065_55d_3rd_derivatives_v065_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc066_65d_3rd_derivatives_v066_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc067_75d_3rd_derivatives_v067_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc068_85d_3rd_derivatives_v068_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc069_95d_3rd_derivatives_v069_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc070_5d_3rd_derivatives_v070_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc071_15d_3rd_derivatives_v071_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc072_25d_3rd_derivatives_v072_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc073_35d_3rd_derivatives_v073_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc074_45d_3rd_derivatives_v074_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc075_55d_3rd_derivatives_v075_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc076_65d_3rd_derivatives_v076_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc077_75d_3rd_derivatives_v077_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc078_85d_3rd_derivatives_v078_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc079_95d_3rd_derivatives_v079_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc080_5d_3rd_derivatives_v080_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc081_15d_3rd_derivatives_v081_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc082_25d_3rd_derivatives_v082_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc083_35d_3rd_derivatives_v083_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc084_45d_3rd_derivatives_v084_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc085_55d_3rd_derivatives_v085_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc086_65d_3rd_derivatives_v086_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc087_75d_3rd_derivatives_v087_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc088_85d_3rd_derivatives_v088_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc089_95d_3rd_derivatives_v089_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc090_5d_3rd_derivatives_v090_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc091_15d_3rd_derivatives_v091_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc092_25d_3rd_derivatives_v092_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc093_35d_3rd_derivatives_v093_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc094_45d_3rd_derivatives_v094_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc095_55d_3rd_derivatives_v095_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc096_65d_3rd_derivatives_v096_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc097_75d_3rd_derivatives_v097_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc098_85d_3rd_derivatives_v098_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc099_95d_3rd_derivatives_v099_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc100_5d_3rd_derivatives_v100_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc101_15d_3rd_derivatives_v101_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc102_25d_3rd_derivatives_v102_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc103_35d_3rd_derivatives_v103_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc104_45d_3rd_derivatives_v104_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc105_55d_3rd_derivatives_v105_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc106_65d_3rd_derivatives_v106_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc107_75d_3rd_derivatives_v107_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc108_85d_3rd_derivatives_v108_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc109_95d_3rd_derivatives_v109_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc110_5d_3rd_derivatives_v110_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc111_15d_3rd_derivatives_v111_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc112_25d_3rd_derivatives_v112_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc113_35d_3rd_derivatives_v113_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc114_45d_3rd_derivatives_v114_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc115_55d_3rd_derivatives_v115_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc116_65d_3rd_derivatives_v116_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc117_75d_3rd_derivatives_v117_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc118_85d_3rd_derivatives_v118_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc119_95d_3rd_derivatives_v119_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc120_5d_3rd_derivatives_v120_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc121_15d_3rd_derivatives_v121_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc122_25d_3rd_derivatives_v122_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc123_35d_3rd_derivatives_v123_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc124_45d_3rd_derivatives_v124_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc125_55d_3rd_derivatives_v125_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc126_65d_3rd_derivatives_v126_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc127_75d_3rd_derivatives_v127_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc128_85d_3rd_derivatives_v128_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc129_95d_3rd_derivatives_v129_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc130_5d_3rd_derivatives_v130_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc131_15d_3rd_derivatives_v131_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc132_25d_3rd_derivatives_v132_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc133_35d_3rd_derivatives_v133_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc134_45d_3rd_derivatives_v134_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc135_55d_3rd_derivatives_v135_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc136_65d_3rd_derivatives_v136_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc137_75d_3rd_derivatives_v137_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc138_85d_3rd_derivatives_v138_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc139_95d_3rd_derivatives_v139_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc140_5d_3rd_derivatives_v140_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc141_15d_3rd_derivatives_v141_signal(pe):
    res = _roc(_roc(_sma(pe, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc142_25d_3rd_derivatives_v142_signal(pe):
    res = _roc(_roc(_sma(pe, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc143_35d_3rd_derivatives_v143_signal(pe):
    res = _roc(_roc(_sma(pe, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc144_45d_3rd_derivatives_v144_signal(pe):
    res = _roc(_roc(_sma(pe, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc145_55d_3rd_derivatives_v145_signal(pe):
    res = _roc(_roc(_sma(pe, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc146_65d_3rd_derivatives_v146_signal(pe):
    res = _roc(_roc(_sma(pe, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc147_75d_3rd_derivatives_v147_signal(pe):
    res = _roc(_roc(_sma(pe, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc148_85d_3rd_derivatives_v148_signal(pe):
    res = _roc(_roc(_sma(pe, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc149_95d_3rd_derivatives_v149_signal(pe):
    res = _roc(_roc(_sma(pe, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc150_5d_3rd_derivatives_v150_signal(pe):
    res = _roc(_roc(_sma(pe, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['pe', 'ps', 'pb', 'marketcap']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f47nvm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f47_network_valuation_multiples...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f47nvm_'))]}

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
