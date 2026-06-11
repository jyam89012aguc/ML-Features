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


def f51anf_f51_asymmetric_network_flow_calc001_15d_3rd_derivatives_v001_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc002_25d_3rd_derivatives_v002_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc003_35d_3rd_derivatives_v003_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc004_45d_3rd_derivatives_v004_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc005_55d_3rd_derivatives_v005_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc006_65d_3rd_derivatives_v006_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc007_75d_3rd_derivatives_v007_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc008_85d_3rd_derivatives_v008_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc009_95d_3rd_derivatives_v009_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc010_5d_3rd_derivatives_v010_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc011_15d_3rd_derivatives_v011_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc012_25d_3rd_derivatives_v012_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc013_35d_3rd_derivatives_v013_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc014_45d_3rd_derivatives_v014_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc015_55d_3rd_derivatives_v015_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc016_65d_3rd_derivatives_v016_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc017_75d_3rd_derivatives_v017_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc018_85d_3rd_derivatives_v018_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc019_95d_3rd_derivatives_v019_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc020_5d_3rd_derivatives_v020_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc021_15d_3rd_derivatives_v021_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc022_25d_3rd_derivatives_v022_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc023_35d_3rd_derivatives_v023_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc024_45d_3rd_derivatives_v024_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc025_55d_3rd_derivatives_v025_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc026_65d_3rd_derivatives_v026_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc027_75d_3rd_derivatives_v027_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc028_85d_3rd_derivatives_v028_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc029_95d_3rd_derivatives_v029_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc030_5d_3rd_derivatives_v030_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc031_15d_3rd_derivatives_v031_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc032_25d_3rd_derivatives_v032_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc033_35d_3rd_derivatives_v033_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc034_45d_3rd_derivatives_v034_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc035_55d_3rd_derivatives_v035_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc036_65d_3rd_derivatives_v036_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc037_75d_3rd_derivatives_v037_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc038_85d_3rd_derivatives_v038_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc039_95d_3rd_derivatives_v039_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc040_5d_3rd_derivatives_v040_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc041_15d_3rd_derivatives_v041_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc042_25d_3rd_derivatives_v042_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc043_35d_3rd_derivatives_v043_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc044_45d_3rd_derivatives_v044_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc045_55d_3rd_derivatives_v045_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc046_65d_3rd_derivatives_v046_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc047_75d_3rd_derivatives_v047_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc048_85d_3rd_derivatives_v048_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc049_95d_3rd_derivatives_v049_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc050_5d_3rd_derivatives_v050_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc051_15d_3rd_derivatives_v051_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc052_25d_3rd_derivatives_v052_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc053_35d_3rd_derivatives_v053_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc054_45d_3rd_derivatives_v054_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc055_55d_3rd_derivatives_v055_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc056_65d_3rd_derivatives_v056_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc057_75d_3rd_derivatives_v057_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc058_85d_3rd_derivatives_v058_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc059_95d_3rd_derivatives_v059_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc060_5d_3rd_derivatives_v060_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc061_15d_3rd_derivatives_v061_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc062_25d_3rd_derivatives_v062_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc063_35d_3rd_derivatives_v063_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc064_45d_3rd_derivatives_v064_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc065_55d_3rd_derivatives_v065_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc066_65d_3rd_derivatives_v066_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc067_75d_3rd_derivatives_v067_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc068_85d_3rd_derivatives_v068_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc069_95d_3rd_derivatives_v069_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc070_5d_3rd_derivatives_v070_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc071_15d_3rd_derivatives_v071_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc072_25d_3rd_derivatives_v072_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc073_35d_3rd_derivatives_v073_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc074_45d_3rd_derivatives_v074_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc075_55d_3rd_derivatives_v075_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc076_65d_3rd_derivatives_v076_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc077_75d_3rd_derivatives_v077_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc078_85d_3rd_derivatives_v078_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc079_95d_3rd_derivatives_v079_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc080_5d_3rd_derivatives_v080_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc081_15d_3rd_derivatives_v081_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc082_25d_3rd_derivatives_v082_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc083_35d_3rd_derivatives_v083_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc084_45d_3rd_derivatives_v084_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc085_55d_3rd_derivatives_v085_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc086_65d_3rd_derivatives_v086_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc087_75d_3rd_derivatives_v087_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc088_85d_3rd_derivatives_v088_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc089_95d_3rd_derivatives_v089_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc090_5d_3rd_derivatives_v090_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc091_15d_3rd_derivatives_v091_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc092_25d_3rd_derivatives_v092_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc093_35d_3rd_derivatives_v093_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc094_45d_3rd_derivatives_v094_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc095_55d_3rd_derivatives_v095_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc096_65d_3rd_derivatives_v096_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc097_75d_3rd_derivatives_v097_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc098_85d_3rd_derivatives_v098_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc099_95d_3rd_derivatives_v099_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc100_5d_3rd_derivatives_v100_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc101_15d_3rd_derivatives_v101_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc102_25d_3rd_derivatives_v102_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc103_35d_3rd_derivatives_v103_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc104_45d_3rd_derivatives_v104_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc105_55d_3rd_derivatives_v105_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc106_65d_3rd_derivatives_v106_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc107_75d_3rd_derivatives_v107_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc108_85d_3rd_derivatives_v108_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc109_95d_3rd_derivatives_v109_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc110_5d_3rd_derivatives_v110_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc111_15d_3rd_derivatives_v111_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc112_25d_3rd_derivatives_v112_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc113_35d_3rd_derivatives_v113_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc114_45d_3rd_derivatives_v114_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc115_55d_3rd_derivatives_v115_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc116_65d_3rd_derivatives_v116_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc117_75d_3rd_derivatives_v117_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc118_85d_3rd_derivatives_v118_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc119_95d_3rd_derivatives_v119_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc120_5d_3rd_derivatives_v120_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc121_15d_3rd_derivatives_v121_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc122_25d_3rd_derivatives_v122_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc123_35d_3rd_derivatives_v123_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc124_45d_3rd_derivatives_v124_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc125_55d_3rd_derivatives_v125_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc126_65d_3rd_derivatives_v126_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc127_75d_3rd_derivatives_v127_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc128_85d_3rd_derivatives_v128_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc129_95d_3rd_derivatives_v129_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc130_5d_3rd_derivatives_v130_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc131_15d_3rd_derivatives_v131_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc132_25d_3rd_derivatives_v132_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc133_35d_3rd_derivatives_v133_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc134_45d_3rd_derivatives_v134_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc135_55d_3rd_derivatives_v135_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc136_65d_3rd_derivatives_v136_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc137_75d_3rd_derivatives_v137_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc138_85d_3rd_derivatives_v138_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc139_95d_3rd_derivatives_v139_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc140_5d_3rd_derivatives_v140_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc141_15d_3rd_derivatives_v141_signal(close, volume):
    res = _roc(_roc((_roc(close, 15) * _sma(volume, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc142_25d_3rd_derivatives_v142_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 25) * _sma(volume, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc143_35d_3rd_derivatives_v143_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 35) * _sma(volume, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc144_45d_3rd_derivatives_v144_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 45) * _sma(volume, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc145_55d_3rd_derivatives_v145_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 55) * _sma(volume, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc146_65d_3rd_derivatives_v146_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 65) * _sma(volume, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc147_75d_3rd_derivatives_v147_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 75) * _sma(volume, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc148_85d_3rd_derivatives_v148_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 85) * _sma(volume, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc149_95d_3rd_derivatives_v149_signal(close, volume):
    res = _roc(_roc((_roc(closeadj, 95) * _sma(volume, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc150_5d_3rd_derivatives_v150_signal(close, volume):
    res = _roc(_roc((_roc(close, 5) * _sma(volume, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['close', 'volume', 'high', 'low']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f51anf_'))]
    
    print(f"Testing {len(funcs)} functions for f51_asymmetric_network_flow...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f51anf_'))]}

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
