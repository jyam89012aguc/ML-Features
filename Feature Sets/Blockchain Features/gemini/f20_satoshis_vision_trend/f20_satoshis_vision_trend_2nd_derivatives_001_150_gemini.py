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


def f20svt_f20_satoshis_vision_trend_calc001_15d_2nd_derivatives_v001_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc002_25d_2nd_derivatives_v002_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc003_35d_2nd_derivatives_v003_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc004_45d_2nd_derivatives_v004_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc005_55d_2nd_derivatives_v005_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc006_65d_2nd_derivatives_v006_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc007_75d_2nd_derivatives_v007_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc008_85d_2nd_derivatives_v008_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc009_95d_2nd_derivatives_v009_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc010_5d_2nd_derivatives_v010_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc011_15d_2nd_derivatives_v011_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc012_25d_2nd_derivatives_v012_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc013_35d_2nd_derivatives_v013_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc014_45d_2nd_derivatives_v014_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc015_55d_2nd_derivatives_v015_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc016_65d_2nd_derivatives_v016_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc017_75d_2nd_derivatives_v017_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc018_85d_2nd_derivatives_v018_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc019_95d_2nd_derivatives_v019_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc020_5d_2nd_derivatives_v020_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc021_15d_2nd_derivatives_v021_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc022_25d_2nd_derivatives_v022_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc023_35d_2nd_derivatives_v023_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc024_45d_2nd_derivatives_v024_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc025_55d_2nd_derivatives_v025_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc026_65d_2nd_derivatives_v026_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc027_75d_2nd_derivatives_v027_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc028_85d_2nd_derivatives_v028_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc029_95d_2nd_derivatives_v029_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc030_5d_2nd_derivatives_v030_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc031_15d_2nd_derivatives_v031_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc032_25d_2nd_derivatives_v032_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc033_35d_2nd_derivatives_v033_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc034_45d_2nd_derivatives_v034_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc035_55d_2nd_derivatives_v035_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc036_65d_2nd_derivatives_v036_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc037_75d_2nd_derivatives_v037_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc038_85d_2nd_derivatives_v038_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc039_95d_2nd_derivatives_v039_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc040_5d_2nd_derivatives_v040_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc041_15d_2nd_derivatives_v041_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc042_25d_2nd_derivatives_v042_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc043_35d_2nd_derivatives_v043_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc044_45d_2nd_derivatives_v044_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc045_55d_2nd_derivatives_v045_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc046_65d_2nd_derivatives_v046_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc047_75d_2nd_derivatives_v047_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc048_85d_2nd_derivatives_v048_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc049_95d_2nd_derivatives_v049_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc050_5d_2nd_derivatives_v050_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc051_15d_2nd_derivatives_v051_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc052_25d_2nd_derivatives_v052_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc053_35d_2nd_derivatives_v053_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc054_45d_2nd_derivatives_v054_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc055_55d_2nd_derivatives_v055_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc056_65d_2nd_derivatives_v056_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc057_75d_2nd_derivatives_v057_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc058_85d_2nd_derivatives_v058_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc059_95d_2nd_derivatives_v059_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc060_5d_2nd_derivatives_v060_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc061_15d_2nd_derivatives_v061_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc062_25d_2nd_derivatives_v062_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc063_35d_2nd_derivatives_v063_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc064_45d_2nd_derivatives_v064_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc065_55d_2nd_derivatives_v065_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc066_65d_2nd_derivatives_v066_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc067_75d_2nd_derivatives_v067_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc068_85d_2nd_derivatives_v068_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc069_95d_2nd_derivatives_v069_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc070_5d_2nd_derivatives_v070_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc071_15d_2nd_derivatives_v071_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc072_25d_2nd_derivatives_v072_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc073_35d_2nd_derivatives_v073_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc074_45d_2nd_derivatives_v074_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc075_55d_2nd_derivatives_v075_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc076_65d_2nd_derivatives_v076_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc077_75d_2nd_derivatives_v077_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc078_85d_2nd_derivatives_v078_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc079_95d_2nd_derivatives_v079_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc080_5d_2nd_derivatives_v080_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc081_15d_2nd_derivatives_v081_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc082_25d_2nd_derivatives_v082_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc083_35d_2nd_derivatives_v083_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc084_45d_2nd_derivatives_v084_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc085_55d_2nd_derivatives_v085_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc086_65d_2nd_derivatives_v086_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc087_75d_2nd_derivatives_v087_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc088_85d_2nd_derivatives_v088_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc089_95d_2nd_derivatives_v089_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc090_5d_2nd_derivatives_v090_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc091_15d_2nd_derivatives_v091_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc092_25d_2nd_derivatives_v092_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc093_35d_2nd_derivatives_v093_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc094_45d_2nd_derivatives_v094_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc095_55d_2nd_derivatives_v095_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc096_65d_2nd_derivatives_v096_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc097_75d_2nd_derivatives_v097_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc098_85d_2nd_derivatives_v098_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc099_95d_2nd_derivatives_v099_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc100_5d_2nd_derivatives_v100_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc101_15d_2nd_derivatives_v101_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc102_25d_2nd_derivatives_v102_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc103_35d_2nd_derivatives_v103_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc104_45d_2nd_derivatives_v104_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc105_55d_2nd_derivatives_v105_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc106_65d_2nd_derivatives_v106_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc107_75d_2nd_derivatives_v107_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc108_85d_2nd_derivatives_v108_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc109_95d_2nd_derivatives_v109_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc110_5d_2nd_derivatives_v110_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc111_15d_2nd_derivatives_v111_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc112_25d_2nd_derivatives_v112_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc113_35d_2nd_derivatives_v113_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc114_45d_2nd_derivatives_v114_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc115_55d_2nd_derivatives_v115_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc116_65d_2nd_derivatives_v116_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc117_75d_2nd_derivatives_v117_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc118_85d_2nd_derivatives_v118_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc119_95d_2nd_derivatives_v119_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc120_5d_2nd_derivatives_v120_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc121_15d_2nd_derivatives_v121_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc122_25d_2nd_derivatives_v122_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc123_35d_2nd_derivatives_v123_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc124_45d_2nd_derivatives_v124_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc125_55d_2nd_derivatives_v125_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc126_65d_2nd_derivatives_v126_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc127_75d_2nd_derivatives_v127_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc128_85d_2nd_derivatives_v128_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc129_95d_2nd_derivatives_v129_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc130_5d_2nd_derivatives_v130_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc131_15d_2nd_derivatives_v131_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc132_25d_2nd_derivatives_v132_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc133_35d_2nd_derivatives_v133_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc134_45d_2nd_derivatives_v134_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc135_55d_2nd_derivatives_v135_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc136_65d_2nd_derivatives_v136_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc137_75d_2nd_derivatives_v137_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc138_85d_2nd_derivatives_v138_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc139_95d_2nd_derivatives_v139_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc140_5d_2nd_derivatives_v140_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc141_15d_2nd_derivatives_v141_signal(close):
    res = _roc(_sma(close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc142_25d_2nd_derivatives_v142_signal(close, closeadj):
    res = _roc(_sma(closeadj, 25), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc143_35d_2nd_derivatives_v143_signal(close, closeadj):
    res = _roc(_sma(closeadj, 35), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc144_45d_2nd_derivatives_v144_signal(close, closeadj):
    res = _roc(_sma(closeadj, 45), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc145_55d_2nd_derivatives_v145_signal(close, closeadj):
    res = _roc(_sma(closeadj, 55), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc146_65d_2nd_derivatives_v146_signal(close, closeadj):
    res = _roc(_sma(closeadj, 65), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc147_75d_2nd_derivatives_v147_signal(close, closeadj):
    res = _roc(_sma(closeadj, 75), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc148_85d_2nd_derivatives_v148_signal(close, closeadj):
    res = _roc(_sma(closeadj, 85), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc149_95d_2nd_derivatives_v149_signal(close, closeadj):
    res = _roc(_sma(closeadj, 95), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20svt_f20_satoshis_vision_trend_calc150_5d_2nd_derivatives_v150_signal(close):
    res = _roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['close', 'closeadj']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f20svt_'))]
    
    print(f"Testing {{len(funcs)}} functions for f20_satoshis_vision_trend...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f20svt_'))]}

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
