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


def f60cba_f60_composite_blockchain_alpha_calc001_15d_3rd_derivatives_v001_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc002_25d_3rd_derivatives_v002_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc003_35d_3rd_derivatives_v003_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc004_45d_3rd_derivatives_v004_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc005_55d_3rd_derivatives_v005_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc006_65d_3rd_derivatives_v006_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc007_75d_3rd_derivatives_v007_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc008_85d_3rd_derivatives_v008_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc009_95d_3rd_derivatives_v009_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc010_5d_3rd_derivatives_v010_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc011_15d_3rd_derivatives_v011_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc012_25d_3rd_derivatives_v012_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc013_35d_3rd_derivatives_v013_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc014_45d_3rd_derivatives_v014_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc015_55d_3rd_derivatives_v015_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc016_65d_3rd_derivatives_v016_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc017_75d_3rd_derivatives_v017_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc018_85d_3rd_derivatives_v018_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc019_95d_3rd_derivatives_v019_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc020_5d_3rd_derivatives_v020_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc021_15d_3rd_derivatives_v021_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc022_25d_3rd_derivatives_v022_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc023_35d_3rd_derivatives_v023_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc024_45d_3rd_derivatives_v024_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc025_55d_3rd_derivatives_v025_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc026_65d_3rd_derivatives_v026_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc027_75d_3rd_derivatives_v027_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc028_85d_3rd_derivatives_v028_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc029_95d_3rd_derivatives_v029_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc030_5d_3rd_derivatives_v030_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc031_15d_3rd_derivatives_v031_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc032_25d_3rd_derivatives_v032_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc033_35d_3rd_derivatives_v033_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc034_45d_3rd_derivatives_v034_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc035_55d_3rd_derivatives_v035_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc036_65d_3rd_derivatives_v036_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc037_75d_3rd_derivatives_v037_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc038_85d_3rd_derivatives_v038_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc039_95d_3rd_derivatives_v039_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc040_5d_3rd_derivatives_v040_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc041_15d_3rd_derivatives_v041_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc042_25d_3rd_derivatives_v042_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc043_35d_3rd_derivatives_v043_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc044_45d_3rd_derivatives_v044_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc045_55d_3rd_derivatives_v045_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc046_65d_3rd_derivatives_v046_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc047_75d_3rd_derivatives_v047_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc048_85d_3rd_derivatives_v048_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc049_95d_3rd_derivatives_v049_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc050_5d_3rd_derivatives_v050_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc051_15d_3rd_derivatives_v051_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc052_25d_3rd_derivatives_v052_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc053_35d_3rd_derivatives_v053_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc054_45d_3rd_derivatives_v054_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc055_55d_3rd_derivatives_v055_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc056_65d_3rd_derivatives_v056_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc057_75d_3rd_derivatives_v057_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc058_85d_3rd_derivatives_v058_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc059_95d_3rd_derivatives_v059_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc060_5d_3rd_derivatives_v060_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc061_15d_3rd_derivatives_v061_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc062_25d_3rd_derivatives_v062_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc063_35d_3rd_derivatives_v063_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc064_45d_3rd_derivatives_v064_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc065_55d_3rd_derivatives_v065_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc066_65d_3rd_derivatives_v066_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc067_75d_3rd_derivatives_v067_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc068_85d_3rd_derivatives_v068_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc069_95d_3rd_derivatives_v069_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc070_5d_3rd_derivatives_v070_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc071_15d_3rd_derivatives_v071_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc072_25d_3rd_derivatives_v072_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc073_35d_3rd_derivatives_v073_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc074_45d_3rd_derivatives_v074_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc075_55d_3rd_derivatives_v075_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc076_65d_3rd_derivatives_v076_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc077_75d_3rd_derivatives_v077_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc078_85d_3rd_derivatives_v078_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc079_95d_3rd_derivatives_v079_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc080_5d_3rd_derivatives_v080_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc081_15d_3rd_derivatives_v081_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc082_25d_3rd_derivatives_v082_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc083_35d_3rd_derivatives_v083_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc084_45d_3rd_derivatives_v084_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc085_55d_3rd_derivatives_v085_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc086_65d_3rd_derivatives_v086_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc087_75d_3rd_derivatives_v087_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc088_85d_3rd_derivatives_v088_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc089_95d_3rd_derivatives_v089_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc090_5d_3rd_derivatives_v090_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc091_15d_3rd_derivatives_v091_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc092_25d_3rd_derivatives_v092_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc093_35d_3rd_derivatives_v093_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc094_45d_3rd_derivatives_v094_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc095_55d_3rd_derivatives_v095_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc096_65d_3rd_derivatives_v096_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc097_75d_3rd_derivatives_v097_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc098_85d_3rd_derivatives_v098_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc099_95d_3rd_derivatives_v099_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc100_5d_3rd_derivatives_v100_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc101_15d_3rd_derivatives_v101_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc102_25d_3rd_derivatives_v102_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc103_35d_3rd_derivatives_v103_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc104_45d_3rd_derivatives_v104_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc105_55d_3rd_derivatives_v105_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc106_65d_3rd_derivatives_v106_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc107_75d_3rd_derivatives_v107_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc108_85d_3rd_derivatives_v108_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc109_95d_3rd_derivatives_v109_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc110_5d_3rd_derivatives_v110_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc111_15d_3rd_derivatives_v111_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc112_25d_3rd_derivatives_v112_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc113_35d_3rd_derivatives_v113_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc114_45d_3rd_derivatives_v114_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc115_55d_3rd_derivatives_v115_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc116_65d_3rd_derivatives_v116_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc117_75d_3rd_derivatives_v117_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc118_85d_3rd_derivatives_v118_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc119_95d_3rd_derivatives_v119_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc120_5d_3rd_derivatives_v120_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc121_15d_3rd_derivatives_v121_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc122_25d_3rd_derivatives_v122_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc123_35d_3rd_derivatives_v123_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc124_45d_3rd_derivatives_v124_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc125_55d_3rd_derivatives_v125_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc126_65d_3rd_derivatives_v126_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc127_75d_3rd_derivatives_v127_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc128_85d_3rd_derivatives_v128_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc129_95d_3rd_derivatives_v129_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc130_5d_3rd_derivatives_v130_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc131_15d_3rd_derivatives_v131_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc132_25d_3rd_derivatives_v132_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc133_35d_3rd_derivatives_v133_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc134_45d_3rd_derivatives_v134_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc135_55d_3rd_derivatives_v135_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc136_65d_3rd_derivatives_v136_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc137_75d_3rd_derivatives_v137_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc138_85d_3rd_derivatives_v138_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc139_95d_3rd_derivatives_v139_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc140_5d_3rd_derivatives_v140_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc141_15d_3rd_derivatives_v141_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 15) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc142_25d_3rd_derivatives_v142_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 25) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc143_35d_3rd_derivatives_v143_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 35) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc144_45d_3rd_derivatives_v144_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 45) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc145_55d_3rd_derivatives_v145_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 55) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc146_65d_3rd_derivatives_v146_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 65) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc147_75d_3rd_derivatives_v147_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 75) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc148_85d_3rd_derivatives_v148_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 85) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc149_95d_3rd_derivatives_v149_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 95) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f60cba_f60_composite_blockchain_alpha_calc150_5d_3rd_derivatives_v150_signal(marketcap, revenue, sf3a_value):
    res = _roc(_roc(((_roc(revenue, 5) * sf3a_value) / marketcap.replace(0, np.nan)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['marketcap', 'revenue', 'sf3a_value', 'volume']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f60cba_'))]
    
    print(f"Testing {len(funcs)} functions for f60_composite_blockchain_alpha...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f60cba_'))]}
