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


def f57tvb_f57_treasury_volatility_buffer_calc001_15d_2nd_derivatives_v001_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc002_25d_2nd_derivatives_v002_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc003_35d_2nd_derivatives_v003_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc004_45d_2nd_derivatives_v004_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc005_55d_2nd_derivatives_v005_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc006_65d_2nd_derivatives_v006_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc007_75d_2nd_derivatives_v007_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc008_85d_2nd_derivatives_v008_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc009_95d_2nd_derivatives_v009_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc010_5d_2nd_derivatives_v010_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc011_15d_2nd_derivatives_v011_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc012_25d_2nd_derivatives_v012_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc013_35d_2nd_derivatives_v013_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc014_45d_2nd_derivatives_v014_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc015_55d_2nd_derivatives_v015_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc016_65d_2nd_derivatives_v016_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc017_75d_2nd_derivatives_v017_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc018_85d_2nd_derivatives_v018_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc019_95d_2nd_derivatives_v019_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc020_5d_2nd_derivatives_v020_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc021_15d_2nd_derivatives_v021_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc022_25d_2nd_derivatives_v022_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc023_35d_2nd_derivatives_v023_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc024_45d_2nd_derivatives_v024_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc025_55d_2nd_derivatives_v025_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc026_65d_2nd_derivatives_v026_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc027_75d_2nd_derivatives_v027_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc028_85d_2nd_derivatives_v028_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc029_95d_2nd_derivatives_v029_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc030_5d_2nd_derivatives_v030_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc031_15d_2nd_derivatives_v031_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc032_25d_2nd_derivatives_v032_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc033_35d_2nd_derivatives_v033_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc034_45d_2nd_derivatives_v034_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc035_55d_2nd_derivatives_v035_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc036_65d_2nd_derivatives_v036_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc037_75d_2nd_derivatives_v037_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc038_85d_2nd_derivatives_v038_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc039_95d_2nd_derivatives_v039_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc040_5d_2nd_derivatives_v040_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc041_15d_2nd_derivatives_v041_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc042_25d_2nd_derivatives_v042_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc043_35d_2nd_derivatives_v043_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc044_45d_2nd_derivatives_v044_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc045_55d_2nd_derivatives_v045_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc046_65d_2nd_derivatives_v046_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc047_75d_2nd_derivatives_v047_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc048_85d_2nd_derivatives_v048_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc049_95d_2nd_derivatives_v049_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc050_5d_2nd_derivatives_v050_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc051_15d_2nd_derivatives_v051_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc052_25d_2nd_derivatives_v052_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc053_35d_2nd_derivatives_v053_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc054_45d_2nd_derivatives_v054_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc055_55d_2nd_derivatives_v055_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc056_65d_2nd_derivatives_v056_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc057_75d_2nd_derivatives_v057_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc058_85d_2nd_derivatives_v058_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc059_95d_2nd_derivatives_v059_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc060_5d_2nd_derivatives_v060_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc061_15d_2nd_derivatives_v061_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc062_25d_2nd_derivatives_v062_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc063_35d_2nd_derivatives_v063_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc064_45d_2nd_derivatives_v064_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc065_55d_2nd_derivatives_v065_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc066_65d_2nd_derivatives_v066_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc067_75d_2nd_derivatives_v067_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc068_85d_2nd_derivatives_v068_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc069_95d_2nd_derivatives_v069_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc070_5d_2nd_derivatives_v070_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc071_15d_2nd_derivatives_v071_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc072_25d_2nd_derivatives_v072_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc073_35d_2nd_derivatives_v073_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc074_45d_2nd_derivatives_v074_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc075_55d_2nd_derivatives_v075_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc076_65d_2nd_derivatives_v076_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc077_75d_2nd_derivatives_v077_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc078_85d_2nd_derivatives_v078_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc079_95d_2nd_derivatives_v079_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc080_5d_2nd_derivatives_v080_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc081_15d_2nd_derivatives_v081_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc082_25d_2nd_derivatives_v082_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc083_35d_2nd_derivatives_v083_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc084_45d_2nd_derivatives_v084_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc085_55d_2nd_derivatives_v085_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc086_65d_2nd_derivatives_v086_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc087_75d_2nd_derivatives_v087_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc088_85d_2nd_derivatives_v088_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc089_95d_2nd_derivatives_v089_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc090_5d_2nd_derivatives_v090_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc091_15d_2nd_derivatives_v091_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc092_25d_2nd_derivatives_v092_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc093_35d_2nd_derivatives_v093_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc094_45d_2nd_derivatives_v094_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc095_55d_2nd_derivatives_v095_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc096_65d_2nd_derivatives_v096_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc097_75d_2nd_derivatives_v097_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc098_85d_2nd_derivatives_v098_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc099_95d_2nd_derivatives_v099_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc100_5d_2nd_derivatives_v100_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc101_15d_2nd_derivatives_v101_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc102_25d_2nd_derivatives_v102_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc103_35d_2nd_derivatives_v103_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc104_45d_2nd_derivatives_v104_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc105_55d_2nd_derivatives_v105_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc106_65d_2nd_derivatives_v106_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc107_75d_2nd_derivatives_v107_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc108_85d_2nd_derivatives_v108_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc109_95d_2nd_derivatives_v109_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc110_5d_2nd_derivatives_v110_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc111_15d_2nd_derivatives_v111_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc112_25d_2nd_derivatives_v112_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc113_35d_2nd_derivatives_v113_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc114_45d_2nd_derivatives_v114_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc115_55d_2nd_derivatives_v115_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc116_65d_2nd_derivatives_v116_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc117_75d_2nd_derivatives_v117_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc118_85d_2nd_derivatives_v118_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc119_95d_2nd_derivatives_v119_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc120_5d_2nd_derivatives_v120_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc121_15d_2nd_derivatives_v121_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc122_25d_2nd_derivatives_v122_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc123_35d_2nd_derivatives_v123_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc124_45d_2nd_derivatives_v124_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc125_55d_2nd_derivatives_v125_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc126_65d_2nd_derivatives_v126_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc127_75d_2nd_derivatives_v127_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc128_85d_2nd_derivatives_v128_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc129_95d_2nd_derivatives_v129_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc130_5d_2nd_derivatives_v130_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc131_15d_2nd_derivatives_v131_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc132_25d_2nd_derivatives_v132_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc133_35d_2nd_derivatives_v133_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc134_45d_2nd_derivatives_v134_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc135_55d_2nd_derivatives_v135_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc136_65d_2nd_derivatives_v136_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc137_75d_2nd_derivatives_v137_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc138_85d_2nd_derivatives_v138_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc139_95d_2nd_derivatives_v139_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc140_5d_2nd_derivatives_v140_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc141_15d_2nd_derivatives_v141_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 15).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc142_25d_2nd_derivatives_v142_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 25).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc143_35d_2nd_derivatives_v143_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 35).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc144_45d_2nd_derivatives_v144_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 45).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc145_55d_2nd_derivatives_v145_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 55).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc146_65d_2nd_derivatives_v146_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 65).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc147_75d_2nd_derivatives_v147_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 75).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc148_85d_2nd_derivatives_v148_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 85).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc149_95d_2nd_derivatives_v149_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 95).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc150_5d_2nd_derivatives_v150_signal(cash, marketcap):
    res = _roc((cash / _std(marketcap, 5).replace(0, np.nan)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['cash', 'debt', 'marketcap']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f57tvb_'))]
    
    print(f"Testing {len(funcs)} functions for f57_treasury_volatility_buffer...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f57tvb_'))]}

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
