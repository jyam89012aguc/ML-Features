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


def f42sth_f42_scaling_throughput_calc001_15d_3rd_derivatives_v001_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc002_25d_3rd_derivatives_v002_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc003_35d_3rd_derivatives_v003_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc004_45d_3rd_derivatives_v004_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc005_55d_3rd_derivatives_v005_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc006_65d_3rd_derivatives_v006_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc007_75d_3rd_derivatives_v007_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc008_85d_3rd_derivatives_v008_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc009_95d_3rd_derivatives_v009_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc010_5d_3rd_derivatives_v010_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc011_15d_3rd_derivatives_v011_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc012_25d_3rd_derivatives_v012_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc013_35d_3rd_derivatives_v013_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc014_45d_3rd_derivatives_v014_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc015_55d_3rd_derivatives_v015_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc016_65d_3rd_derivatives_v016_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc017_75d_3rd_derivatives_v017_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc018_85d_3rd_derivatives_v018_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc019_95d_3rd_derivatives_v019_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc020_5d_3rd_derivatives_v020_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc021_15d_3rd_derivatives_v021_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc022_25d_3rd_derivatives_v022_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc023_35d_3rd_derivatives_v023_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc024_45d_3rd_derivatives_v024_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc025_55d_3rd_derivatives_v025_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc026_65d_3rd_derivatives_v026_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc027_75d_3rd_derivatives_v027_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc028_85d_3rd_derivatives_v028_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc029_95d_3rd_derivatives_v029_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc030_5d_3rd_derivatives_v030_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc031_15d_3rd_derivatives_v031_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc032_25d_3rd_derivatives_v032_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc033_35d_3rd_derivatives_v033_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc034_45d_3rd_derivatives_v034_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc035_55d_3rd_derivatives_v035_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc036_65d_3rd_derivatives_v036_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc037_75d_3rd_derivatives_v037_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc038_85d_3rd_derivatives_v038_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc039_95d_3rd_derivatives_v039_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc040_5d_3rd_derivatives_v040_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc041_15d_3rd_derivatives_v041_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc042_25d_3rd_derivatives_v042_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc043_35d_3rd_derivatives_v043_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc044_45d_3rd_derivatives_v044_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc045_55d_3rd_derivatives_v045_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc046_65d_3rd_derivatives_v046_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc047_75d_3rd_derivatives_v047_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc048_85d_3rd_derivatives_v048_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc049_95d_3rd_derivatives_v049_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc050_5d_3rd_derivatives_v050_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc051_15d_3rd_derivatives_v051_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc052_25d_3rd_derivatives_v052_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc053_35d_3rd_derivatives_v053_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc054_45d_3rd_derivatives_v054_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc055_55d_3rd_derivatives_v055_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc056_65d_3rd_derivatives_v056_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc057_75d_3rd_derivatives_v057_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc058_85d_3rd_derivatives_v058_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc059_95d_3rd_derivatives_v059_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc060_5d_3rd_derivatives_v060_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc061_15d_3rd_derivatives_v061_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc062_25d_3rd_derivatives_v062_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc063_35d_3rd_derivatives_v063_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc064_45d_3rd_derivatives_v064_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc065_55d_3rd_derivatives_v065_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc066_65d_3rd_derivatives_v066_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc067_75d_3rd_derivatives_v067_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc068_85d_3rd_derivatives_v068_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc069_95d_3rd_derivatives_v069_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc070_5d_3rd_derivatives_v070_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc071_15d_3rd_derivatives_v071_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc072_25d_3rd_derivatives_v072_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc073_35d_3rd_derivatives_v073_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc074_45d_3rd_derivatives_v074_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc075_55d_3rd_derivatives_v075_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc076_65d_3rd_derivatives_v076_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc077_75d_3rd_derivatives_v077_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc078_85d_3rd_derivatives_v078_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc079_95d_3rd_derivatives_v079_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc080_5d_3rd_derivatives_v080_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc081_15d_3rd_derivatives_v081_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc082_25d_3rd_derivatives_v082_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc083_35d_3rd_derivatives_v083_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc084_45d_3rd_derivatives_v084_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc085_55d_3rd_derivatives_v085_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc086_65d_3rd_derivatives_v086_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc087_75d_3rd_derivatives_v087_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc088_85d_3rd_derivatives_v088_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc089_95d_3rd_derivatives_v089_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc090_5d_3rd_derivatives_v090_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc091_15d_3rd_derivatives_v091_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc092_25d_3rd_derivatives_v092_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc093_35d_3rd_derivatives_v093_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc094_45d_3rd_derivatives_v094_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc095_55d_3rd_derivatives_v095_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc096_65d_3rd_derivatives_v096_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc097_75d_3rd_derivatives_v097_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc098_85d_3rd_derivatives_v098_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc099_95d_3rd_derivatives_v099_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc100_5d_3rd_derivatives_v100_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc101_15d_3rd_derivatives_v101_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc102_25d_3rd_derivatives_v102_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc103_35d_3rd_derivatives_v103_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc104_45d_3rd_derivatives_v104_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc105_55d_3rd_derivatives_v105_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc106_65d_3rd_derivatives_v106_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc107_75d_3rd_derivatives_v107_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc108_85d_3rd_derivatives_v108_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc109_95d_3rd_derivatives_v109_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc110_5d_3rd_derivatives_v110_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc111_15d_3rd_derivatives_v111_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc112_25d_3rd_derivatives_v112_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc113_35d_3rd_derivatives_v113_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc114_45d_3rd_derivatives_v114_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc115_55d_3rd_derivatives_v115_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc116_65d_3rd_derivatives_v116_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc117_75d_3rd_derivatives_v117_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc118_85d_3rd_derivatives_v118_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc119_95d_3rd_derivatives_v119_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc120_5d_3rd_derivatives_v120_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc121_15d_3rd_derivatives_v121_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc122_25d_3rd_derivatives_v122_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc123_35d_3rd_derivatives_v123_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc124_45d_3rd_derivatives_v124_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc125_55d_3rd_derivatives_v125_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc126_65d_3rd_derivatives_v126_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc127_75d_3rd_derivatives_v127_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc128_85d_3rd_derivatives_v128_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc129_95d_3rd_derivatives_v129_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc130_5d_3rd_derivatives_v130_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc131_15d_3rd_derivatives_v131_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc132_25d_3rd_derivatives_v132_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc133_35d_3rd_derivatives_v133_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc134_45d_3rd_derivatives_v134_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc135_55d_3rd_derivatives_v135_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc136_65d_3rd_derivatives_v136_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc137_75d_3rd_derivatives_v137_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc138_85d_3rd_derivatives_v138_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc139_95d_3rd_derivatives_v139_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc140_5d_3rd_derivatives_v140_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc141_15d_3rd_derivatives_v141_signal(revenue):
    res = _roc(_roc(_sma(revenue, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc142_25d_3rd_derivatives_v142_signal(revenue):
    res = _roc(_roc(_sma(revenue, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc143_35d_3rd_derivatives_v143_signal(revenue):
    res = _roc(_roc(_sma(revenue, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc144_45d_3rd_derivatives_v144_signal(revenue):
    res = _roc(_roc(_sma(revenue, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc145_55d_3rd_derivatives_v145_signal(revenue):
    res = _roc(_roc(_sma(revenue, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc146_65d_3rd_derivatives_v146_signal(revenue):
    res = _roc(_roc(_sma(revenue, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc147_75d_3rd_derivatives_v147_signal(revenue):
    res = _roc(_roc(_sma(revenue, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc148_85d_3rd_derivatives_v148_signal(revenue):
    res = _roc(_roc(_sma(revenue, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc149_95d_3rd_derivatives_v149_signal(revenue):
    res = _roc(_roc(_sma(revenue, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc150_5d_3rd_derivatives_v150_signal(revenue):
    res = _roc(_roc(_sma(revenue, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['revenue', 'assets', 'ebitda']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f42sth_'))]
    
    print(f"Testing {{len(funcs)}} functions for f42_scaling_throughput...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f42sth_'))]}

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
