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


def f49pdm_f49_protocol_dominance_metrics_calc001_15d_3rd_derivatives_v001_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc002_25d_3rd_derivatives_v002_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc003_35d_3rd_derivatives_v003_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc004_45d_3rd_derivatives_v004_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc005_55d_3rd_derivatives_v005_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc006_65d_3rd_derivatives_v006_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc007_75d_3rd_derivatives_v007_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc008_85d_3rd_derivatives_v008_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc009_95d_3rd_derivatives_v009_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc010_5d_3rd_derivatives_v010_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc011_15d_3rd_derivatives_v011_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc012_25d_3rd_derivatives_v012_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc013_35d_3rd_derivatives_v013_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc014_45d_3rd_derivatives_v014_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc015_55d_3rd_derivatives_v015_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc016_65d_3rd_derivatives_v016_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc017_75d_3rd_derivatives_v017_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc018_85d_3rd_derivatives_v018_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc019_95d_3rd_derivatives_v019_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc020_5d_3rd_derivatives_v020_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc021_15d_3rd_derivatives_v021_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc022_25d_3rd_derivatives_v022_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc023_35d_3rd_derivatives_v023_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc024_45d_3rd_derivatives_v024_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc025_55d_3rd_derivatives_v025_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc026_65d_3rd_derivatives_v026_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc027_75d_3rd_derivatives_v027_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc028_85d_3rd_derivatives_v028_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc029_95d_3rd_derivatives_v029_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc030_5d_3rd_derivatives_v030_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc031_15d_3rd_derivatives_v031_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc032_25d_3rd_derivatives_v032_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc033_35d_3rd_derivatives_v033_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc034_45d_3rd_derivatives_v034_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc035_55d_3rd_derivatives_v035_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc036_65d_3rd_derivatives_v036_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc037_75d_3rd_derivatives_v037_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc038_85d_3rd_derivatives_v038_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc039_95d_3rd_derivatives_v039_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc040_5d_3rd_derivatives_v040_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc041_15d_3rd_derivatives_v041_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc042_25d_3rd_derivatives_v042_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc043_35d_3rd_derivatives_v043_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc044_45d_3rd_derivatives_v044_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc045_55d_3rd_derivatives_v045_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc046_65d_3rd_derivatives_v046_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc047_75d_3rd_derivatives_v047_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc048_85d_3rd_derivatives_v048_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc049_95d_3rd_derivatives_v049_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc050_5d_3rd_derivatives_v050_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc051_15d_3rd_derivatives_v051_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc052_25d_3rd_derivatives_v052_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc053_35d_3rd_derivatives_v053_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc054_45d_3rd_derivatives_v054_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc055_55d_3rd_derivatives_v055_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc056_65d_3rd_derivatives_v056_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc057_75d_3rd_derivatives_v057_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc058_85d_3rd_derivatives_v058_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc059_95d_3rd_derivatives_v059_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc060_5d_3rd_derivatives_v060_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc061_15d_3rd_derivatives_v061_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc062_25d_3rd_derivatives_v062_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc063_35d_3rd_derivatives_v063_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc064_45d_3rd_derivatives_v064_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc065_55d_3rd_derivatives_v065_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc066_65d_3rd_derivatives_v066_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc067_75d_3rd_derivatives_v067_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc068_85d_3rd_derivatives_v068_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc069_95d_3rd_derivatives_v069_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc070_5d_3rd_derivatives_v070_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc071_15d_3rd_derivatives_v071_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc072_25d_3rd_derivatives_v072_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc073_35d_3rd_derivatives_v073_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc074_45d_3rd_derivatives_v074_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc075_55d_3rd_derivatives_v075_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc076_65d_3rd_derivatives_v076_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc077_75d_3rd_derivatives_v077_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc078_85d_3rd_derivatives_v078_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc079_95d_3rd_derivatives_v079_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc080_5d_3rd_derivatives_v080_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc081_15d_3rd_derivatives_v081_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc082_25d_3rd_derivatives_v082_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc083_35d_3rd_derivatives_v083_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc084_45d_3rd_derivatives_v084_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc085_55d_3rd_derivatives_v085_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc086_65d_3rd_derivatives_v086_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc087_75d_3rd_derivatives_v087_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc088_85d_3rd_derivatives_v088_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc089_95d_3rd_derivatives_v089_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc090_5d_3rd_derivatives_v090_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc091_15d_3rd_derivatives_v091_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc092_25d_3rd_derivatives_v092_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc093_35d_3rd_derivatives_v093_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc094_45d_3rd_derivatives_v094_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc095_55d_3rd_derivatives_v095_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc096_65d_3rd_derivatives_v096_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc097_75d_3rd_derivatives_v097_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc098_85d_3rd_derivatives_v098_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc099_95d_3rd_derivatives_v099_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc100_5d_3rd_derivatives_v100_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc101_15d_3rd_derivatives_v101_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc102_25d_3rd_derivatives_v102_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc103_35d_3rd_derivatives_v103_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc104_45d_3rd_derivatives_v104_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc105_55d_3rd_derivatives_v105_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc106_65d_3rd_derivatives_v106_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc107_75d_3rd_derivatives_v107_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc108_85d_3rd_derivatives_v108_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc109_95d_3rd_derivatives_v109_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc110_5d_3rd_derivatives_v110_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc111_15d_3rd_derivatives_v111_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc112_25d_3rd_derivatives_v112_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc113_35d_3rd_derivatives_v113_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc114_45d_3rd_derivatives_v114_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc115_55d_3rd_derivatives_v115_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc116_65d_3rd_derivatives_v116_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc117_75d_3rd_derivatives_v117_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc118_85d_3rd_derivatives_v118_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc119_95d_3rd_derivatives_v119_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc120_5d_3rd_derivatives_v120_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc121_15d_3rd_derivatives_v121_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc122_25d_3rd_derivatives_v122_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc123_35d_3rd_derivatives_v123_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc124_45d_3rd_derivatives_v124_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc125_55d_3rd_derivatives_v125_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc126_65d_3rd_derivatives_v126_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc127_75d_3rd_derivatives_v127_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc128_85d_3rd_derivatives_v128_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc129_95d_3rd_derivatives_v129_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc130_5d_3rd_derivatives_v130_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc131_15d_3rd_derivatives_v131_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc132_25d_3rd_derivatives_v132_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc133_35d_3rd_derivatives_v133_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc134_45d_3rd_derivatives_v134_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc135_55d_3rd_derivatives_v135_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc136_65d_3rd_derivatives_v136_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc137_75d_3rd_derivatives_v137_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc138_85d_3rd_derivatives_v138_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc139_95d_3rd_derivatives_v139_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc140_5d_3rd_derivatives_v140_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc141_15d_3rd_derivatives_v141_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 15), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc142_25d_3rd_derivatives_v142_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 25), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc143_35d_3rd_derivatives_v143_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 35), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc144_45d_3rd_derivatives_v144_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 45), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc145_55d_3rd_derivatives_v145_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 55), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc146_65d_3rd_derivatives_v146_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 65), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc147_75d_3rd_derivatives_v147_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 75), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc148_85d_3rd_derivatives_v148_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 85), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc149_95d_3rd_derivatives_v149_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 95), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49pdm_f49_protocol_dominance_metrics_calc150_5d_3rd_derivatives_v150_signal(marketcap):
    res = _roc(_roc(_sma(marketcap, 5), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['marketcap', 'ev', 'ps']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f49pdm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f49_protocol_dominance_metrics...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f49pdm_'))]}

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
