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


def f35tinf_f35_tokenomics_inflation_calc001_15d_2nd_derivatives_v001_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc002_25d_2nd_derivatives_v002_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc003_35d_2nd_derivatives_v003_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc004_45d_2nd_derivatives_v004_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc005_55d_2nd_derivatives_v005_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc006_65d_2nd_derivatives_v006_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc007_75d_2nd_derivatives_v007_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc008_85d_2nd_derivatives_v008_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc009_95d_2nd_derivatives_v009_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc010_5d_2nd_derivatives_v010_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc011_15d_2nd_derivatives_v011_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc012_25d_2nd_derivatives_v012_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc013_35d_2nd_derivatives_v013_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc014_45d_2nd_derivatives_v014_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc015_55d_2nd_derivatives_v015_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc016_65d_2nd_derivatives_v016_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc017_75d_2nd_derivatives_v017_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc018_85d_2nd_derivatives_v018_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc019_95d_2nd_derivatives_v019_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc020_5d_2nd_derivatives_v020_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc021_15d_2nd_derivatives_v021_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc022_25d_2nd_derivatives_v022_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc023_35d_2nd_derivatives_v023_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc024_45d_2nd_derivatives_v024_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc025_55d_2nd_derivatives_v025_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc026_65d_2nd_derivatives_v026_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc027_75d_2nd_derivatives_v027_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc028_85d_2nd_derivatives_v028_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc029_95d_2nd_derivatives_v029_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc030_5d_2nd_derivatives_v030_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc031_15d_2nd_derivatives_v031_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc032_25d_2nd_derivatives_v032_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc033_35d_2nd_derivatives_v033_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc034_45d_2nd_derivatives_v034_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc035_55d_2nd_derivatives_v035_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc036_65d_2nd_derivatives_v036_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc037_75d_2nd_derivatives_v037_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc038_85d_2nd_derivatives_v038_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc039_95d_2nd_derivatives_v039_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc040_5d_2nd_derivatives_v040_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc041_15d_2nd_derivatives_v041_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc042_25d_2nd_derivatives_v042_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc043_35d_2nd_derivatives_v043_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc044_45d_2nd_derivatives_v044_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc045_55d_2nd_derivatives_v045_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc046_65d_2nd_derivatives_v046_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc047_75d_2nd_derivatives_v047_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc048_85d_2nd_derivatives_v048_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc049_95d_2nd_derivatives_v049_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc050_5d_2nd_derivatives_v050_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc051_15d_2nd_derivatives_v051_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc052_25d_2nd_derivatives_v052_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc053_35d_2nd_derivatives_v053_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc054_45d_2nd_derivatives_v054_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc055_55d_2nd_derivatives_v055_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc056_65d_2nd_derivatives_v056_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc057_75d_2nd_derivatives_v057_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc058_85d_2nd_derivatives_v058_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc059_95d_2nd_derivatives_v059_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc060_5d_2nd_derivatives_v060_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc061_15d_2nd_derivatives_v061_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc062_25d_2nd_derivatives_v062_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc063_35d_2nd_derivatives_v063_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc064_45d_2nd_derivatives_v064_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc065_55d_2nd_derivatives_v065_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc066_65d_2nd_derivatives_v066_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc067_75d_2nd_derivatives_v067_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc068_85d_2nd_derivatives_v068_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc069_95d_2nd_derivatives_v069_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc070_5d_2nd_derivatives_v070_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc071_15d_2nd_derivatives_v071_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc072_25d_2nd_derivatives_v072_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc073_35d_2nd_derivatives_v073_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc074_45d_2nd_derivatives_v074_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc075_55d_2nd_derivatives_v075_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc076_65d_2nd_derivatives_v076_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc077_75d_2nd_derivatives_v077_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc078_85d_2nd_derivatives_v078_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc079_95d_2nd_derivatives_v079_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc080_5d_2nd_derivatives_v080_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc081_15d_2nd_derivatives_v081_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc082_25d_2nd_derivatives_v082_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc083_35d_2nd_derivatives_v083_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc084_45d_2nd_derivatives_v084_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc085_55d_2nd_derivatives_v085_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc086_65d_2nd_derivatives_v086_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc087_75d_2nd_derivatives_v087_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc088_85d_2nd_derivatives_v088_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc089_95d_2nd_derivatives_v089_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc090_5d_2nd_derivatives_v090_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc091_15d_2nd_derivatives_v091_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc092_25d_2nd_derivatives_v092_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc093_35d_2nd_derivatives_v093_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc094_45d_2nd_derivatives_v094_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc095_55d_2nd_derivatives_v095_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc096_65d_2nd_derivatives_v096_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc097_75d_2nd_derivatives_v097_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc098_85d_2nd_derivatives_v098_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc099_95d_2nd_derivatives_v099_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc100_5d_2nd_derivatives_v100_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc101_15d_2nd_derivatives_v101_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc102_25d_2nd_derivatives_v102_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc103_35d_2nd_derivatives_v103_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc104_45d_2nd_derivatives_v104_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc105_55d_2nd_derivatives_v105_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc106_65d_2nd_derivatives_v106_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc107_75d_2nd_derivatives_v107_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc108_85d_2nd_derivatives_v108_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc109_95d_2nd_derivatives_v109_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc110_5d_2nd_derivatives_v110_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc111_15d_2nd_derivatives_v111_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc112_25d_2nd_derivatives_v112_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc113_35d_2nd_derivatives_v113_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc114_45d_2nd_derivatives_v114_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc115_55d_2nd_derivatives_v115_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc116_65d_2nd_derivatives_v116_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc117_75d_2nd_derivatives_v117_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc118_85d_2nd_derivatives_v118_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc119_95d_2nd_derivatives_v119_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc120_5d_2nd_derivatives_v120_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc121_15d_2nd_derivatives_v121_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc122_25d_2nd_derivatives_v122_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc123_35d_2nd_derivatives_v123_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc124_45d_2nd_derivatives_v124_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc125_55d_2nd_derivatives_v125_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc126_65d_2nd_derivatives_v126_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc127_75d_2nd_derivatives_v127_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc128_85d_2nd_derivatives_v128_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc129_95d_2nd_derivatives_v129_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc130_5d_2nd_derivatives_v130_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc131_15d_2nd_derivatives_v131_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc132_25d_2nd_derivatives_v132_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc133_35d_2nd_derivatives_v133_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc134_45d_2nd_derivatives_v134_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc135_55d_2nd_derivatives_v135_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc136_65d_2nd_derivatives_v136_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc137_75d_2nd_derivatives_v137_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc138_85d_2nd_derivatives_v138_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc139_95d_2nd_derivatives_v139_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc140_5d_2nd_derivatives_v140_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc141_15d_2nd_derivatives_v141_signal(sharesbas):
    res = _roc(_sma(sharesbas, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc142_25d_2nd_derivatives_v142_signal(sharesbas):
    res = _roc(_sma(sharesbas, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc143_35d_2nd_derivatives_v143_signal(sharesbas):
    res = _roc(_sma(sharesbas, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc144_45d_2nd_derivatives_v144_signal(sharesbas):
    res = _roc(_sma(sharesbas, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc145_55d_2nd_derivatives_v145_signal(sharesbas):
    res = _roc(_sma(sharesbas, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc146_65d_2nd_derivatives_v146_signal(sharesbas):
    res = _roc(_sma(sharesbas, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc147_75d_2nd_derivatives_v147_signal(sharesbas):
    res = _roc(_sma(sharesbas, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc148_85d_2nd_derivatives_v148_signal(sharesbas):
    res = _roc(_sma(sharesbas, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc149_95d_2nd_derivatives_v149_signal(sharesbas):
    res = _roc(_sma(sharesbas, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc150_5d_2nd_derivatives_v150_signal(sharesbas):
    res = _roc(_sma(sharesbas, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['sharesbas', 'revenue', 'equity']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f35tinf_'))]
    
    print(f"Testing {{len(funcs)}} functions for f35_tokenomics_inflation...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f35tinf_'))]}

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
