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


def f38ycm_f38_yield_capture_margins_calc001_15d_3rd_derivatives_v001_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc002_25d_3rd_derivatives_v002_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc003_35d_3rd_derivatives_v003_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc004_45d_3rd_derivatives_v004_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc005_55d_3rd_derivatives_v005_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc006_65d_3rd_derivatives_v006_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc007_75d_3rd_derivatives_v007_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc008_85d_3rd_derivatives_v008_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc009_95d_3rd_derivatives_v009_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc010_5d_3rd_derivatives_v010_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc011_15d_3rd_derivatives_v011_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc012_25d_3rd_derivatives_v012_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc013_35d_3rd_derivatives_v013_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc014_45d_3rd_derivatives_v014_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc015_55d_3rd_derivatives_v015_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc016_65d_3rd_derivatives_v016_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc017_75d_3rd_derivatives_v017_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc018_85d_3rd_derivatives_v018_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc019_95d_3rd_derivatives_v019_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc020_5d_3rd_derivatives_v020_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc021_15d_3rd_derivatives_v021_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc022_25d_3rd_derivatives_v022_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc023_35d_3rd_derivatives_v023_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc024_45d_3rd_derivatives_v024_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc025_55d_3rd_derivatives_v025_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc026_65d_3rd_derivatives_v026_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc027_75d_3rd_derivatives_v027_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc028_85d_3rd_derivatives_v028_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc029_95d_3rd_derivatives_v029_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc030_5d_3rd_derivatives_v030_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc031_15d_3rd_derivatives_v031_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc032_25d_3rd_derivatives_v032_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc033_35d_3rd_derivatives_v033_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc034_45d_3rd_derivatives_v034_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc035_55d_3rd_derivatives_v035_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc036_65d_3rd_derivatives_v036_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc037_75d_3rd_derivatives_v037_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc038_85d_3rd_derivatives_v038_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc039_95d_3rd_derivatives_v039_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc040_5d_3rd_derivatives_v040_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc041_15d_3rd_derivatives_v041_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc042_25d_3rd_derivatives_v042_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc043_35d_3rd_derivatives_v043_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc044_45d_3rd_derivatives_v044_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc045_55d_3rd_derivatives_v045_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc046_65d_3rd_derivatives_v046_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc047_75d_3rd_derivatives_v047_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc048_85d_3rd_derivatives_v048_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc049_95d_3rd_derivatives_v049_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc050_5d_3rd_derivatives_v050_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc051_15d_3rd_derivatives_v051_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc052_25d_3rd_derivatives_v052_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc053_35d_3rd_derivatives_v053_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc054_45d_3rd_derivatives_v054_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc055_55d_3rd_derivatives_v055_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc056_65d_3rd_derivatives_v056_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc057_75d_3rd_derivatives_v057_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc058_85d_3rd_derivatives_v058_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc059_95d_3rd_derivatives_v059_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc060_5d_3rd_derivatives_v060_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc061_15d_3rd_derivatives_v061_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc062_25d_3rd_derivatives_v062_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc063_35d_3rd_derivatives_v063_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc064_45d_3rd_derivatives_v064_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc065_55d_3rd_derivatives_v065_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc066_65d_3rd_derivatives_v066_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc067_75d_3rd_derivatives_v067_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc068_85d_3rd_derivatives_v068_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc069_95d_3rd_derivatives_v069_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc070_5d_3rd_derivatives_v070_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc071_15d_3rd_derivatives_v071_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc072_25d_3rd_derivatives_v072_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc073_35d_3rd_derivatives_v073_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc074_45d_3rd_derivatives_v074_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc075_55d_3rd_derivatives_v075_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc076_65d_3rd_derivatives_v076_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc077_75d_3rd_derivatives_v077_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc078_85d_3rd_derivatives_v078_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc079_95d_3rd_derivatives_v079_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc080_5d_3rd_derivatives_v080_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc081_15d_3rd_derivatives_v081_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc082_25d_3rd_derivatives_v082_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc083_35d_3rd_derivatives_v083_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc084_45d_3rd_derivatives_v084_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc085_55d_3rd_derivatives_v085_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc086_65d_3rd_derivatives_v086_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc087_75d_3rd_derivatives_v087_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc088_85d_3rd_derivatives_v088_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc089_95d_3rd_derivatives_v089_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc090_5d_3rd_derivatives_v090_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc091_15d_3rd_derivatives_v091_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc092_25d_3rd_derivatives_v092_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc093_35d_3rd_derivatives_v093_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc094_45d_3rd_derivatives_v094_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc095_55d_3rd_derivatives_v095_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc096_65d_3rd_derivatives_v096_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc097_75d_3rd_derivatives_v097_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc098_85d_3rd_derivatives_v098_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc099_95d_3rd_derivatives_v099_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc100_5d_3rd_derivatives_v100_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc101_15d_3rd_derivatives_v101_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc102_25d_3rd_derivatives_v102_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc103_35d_3rd_derivatives_v103_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc104_45d_3rd_derivatives_v104_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc105_55d_3rd_derivatives_v105_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc106_65d_3rd_derivatives_v106_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc107_75d_3rd_derivatives_v107_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc108_85d_3rd_derivatives_v108_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc109_95d_3rd_derivatives_v109_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc110_5d_3rd_derivatives_v110_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc111_15d_3rd_derivatives_v111_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc112_25d_3rd_derivatives_v112_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc113_35d_3rd_derivatives_v113_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc114_45d_3rd_derivatives_v114_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc115_55d_3rd_derivatives_v115_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc116_65d_3rd_derivatives_v116_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc117_75d_3rd_derivatives_v117_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc118_85d_3rd_derivatives_v118_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc119_95d_3rd_derivatives_v119_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc120_5d_3rd_derivatives_v120_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc121_15d_3rd_derivatives_v121_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc122_25d_3rd_derivatives_v122_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc123_35d_3rd_derivatives_v123_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc124_45d_3rd_derivatives_v124_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc125_55d_3rd_derivatives_v125_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc126_65d_3rd_derivatives_v126_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc127_75d_3rd_derivatives_v127_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc128_85d_3rd_derivatives_v128_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc129_95d_3rd_derivatives_v129_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc130_5d_3rd_derivatives_v130_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc131_15d_3rd_derivatives_v131_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc132_25d_3rd_derivatives_v132_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc133_35d_3rd_derivatives_v133_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc134_45d_3rd_derivatives_v134_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc135_55d_3rd_derivatives_v135_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc136_65d_3rd_derivatives_v136_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc137_75d_3rd_derivatives_v137_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc138_85d_3rd_derivatives_v138_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc139_95d_3rd_derivatives_v139_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc140_5d_3rd_derivatives_v140_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc141_15d_3rd_derivatives_v141_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc142_25d_3rd_derivatives_v142_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc143_35d_3rd_derivatives_v143_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc144_45d_3rd_derivatives_v144_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc145_55d_3rd_derivatives_v145_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc146_65d_3rd_derivatives_v146_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc147_75d_3rd_derivatives_v147_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc148_85d_3rd_derivatives_v148_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc149_95d_3rd_derivatives_v149_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc150_5d_3rd_derivatives_v150_signal(ebitda):
    res = _roc(_roc(_sma(ebitda, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['ebitda', 'revenue', 'gp']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f38ycm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f38_yield_capture_margins...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f38ycm_'))]}

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
