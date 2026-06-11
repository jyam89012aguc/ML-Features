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


def f64eeo_f64_ev_ebitda_oscillator_calc001_15d_3rd_derivatives_v001_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc002_25d_3rd_derivatives_v002_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc003_35d_3rd_derivatives_v003_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc004_45d_3rd_derivatives_v004_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc005_55d_3rd_derivatives_v005_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc006_65d_3rd_derivatives_v006_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc007_75d_3rd_derivatives_v007_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc008_85d_3rd_derivatives_v008_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc009_95d_3rd_derivatives_v009_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc010_5d_3rd_derivatives_v010_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc011_15d_3rd_derivatives_v011_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc012_25d_3rd_derivatives_v012_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc013_35d_3rd_derivatives_v013_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc014_45d_3rd_derivatives_v014_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc015_55d_3rd_derivatives_v015_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc016_65d_3rd_derivatives_v016_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc017_75d_3rd_derivatives_v017_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc018_85d_3rd_derivatives_v018_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc019_95d_3rd_derivatives_v019_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc020_5d_3rd_derivatives_v020_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc021_15d_3rd_derivatives_v021_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc022_25d_3rd_derivatives_v022_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc023_35d_3rd_derivatives_v023_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc024_45d_3rd_derivatives_v024_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc025_55d_3rd_derivatives_v025_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc026_65d_3rd_derivatives_v026_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc027_75d_3rd_derivatives_v027_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc028_85d_3rd_derivatives_v028_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc029_95d_3rd_derivatives_v029_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc030_5d_3rd_derivatives_v030_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc031_15d_3rd_derivatives_v031_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc032_25d_3rd_derivatives_v032_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc033_35d_3rd_derivatives_v033_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc034_45d_3rd_derivatives_v034_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc035_55d_3rd_derivatives_v035_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc036_65d_3rd_derivatives_v036_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc037_75d_3rd_derivatives_v037_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc038_85d_3rd_derivatives_v038_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc039_95d_3rd_derivatives_v039_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc040_5d_3rd_derivatives_v040_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc041_15d_3rd_derivatives_v041_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc042_25d_3rd_derivatives_v042_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc043_35d_3rd_derivatives_v043_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc044_45d_3rd_derivatives_v044_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc045_55d_3rd_derivatives_v045_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc046_65d_3rd_derivatives_v046_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc047_75d_3rd_derivatives_v047_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc048_85d_3rd_derivatives_v048_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc049_95d_3rd_derivatives_v049_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc050_5d_3rd_derivatives_v050_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc051_15d_3rd_derivatives_v051_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc052_25d_3rd_derivatives_v052_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc053_35d_3rd_derivatives_v053_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc054_45d_3rd_derivatives_v054_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc055_55d_3rd_derivatives_v055_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc056_65d_3rd_derivatives_v056_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc057_75d_3rd_derivatives_v057_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc058_85d_3rd_derivatives_v058_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc059_95d_3rd_derivatives_v059_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc060_5d_3rd_derivatives_v060_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc061_15d_3rd_derivatives_v061_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc062_25d_3rd_derivatives_v062_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc063_35d_3rd_derivatives_v063_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc064_45d_3rd_derivatives_v064_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc065_55d_3rd_derivatives_v065_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc066_65d_3rd_derivatives_v066_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc067_75d_3rd_derivatives_v067_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc068_85d_3rd_derivatives_v068_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc069_95d_3rd_derivatives_v069_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc070_5d_3rd_derivatives_v070_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc071_15d_3rd_derivatives_v071_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc072_25d_3rd_derivatives_v072_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc073_35d_3rd_derivatives_v073_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc074_45d_3rd_derivatives_v074_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc075_55d_3rd_derivatives_v075_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc076_65d_3rd_derivatives_v076_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc077_75d_3rd_derivatives_v077_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc078_85d_3rd_derivatives_v078_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc079_95d_3rd_derivatives_v079_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc080_5d_3rd_derivatives_v080_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc081_15d_3rd_derivatives_v081_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc082_25d_3rd_derivatives_v082_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc083_35d_3rd_derivatives_v083_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc084_45d_3rd_derivatives_v084_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc085_55d_3rd_derivatives_v085_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc086_65d_3rd_derivatives_v086_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc087_75d_3rd_derivatives_v087_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc088_85d_3rd_derivatives_v088_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc089_95d_3rd_derivatives_v089_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc090_5d_3rd_derivatives_v090_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc091_15d_3rd_derivatives_v091_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc092_25d_3rd_derivatives_v092_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc093_35d_3rd_derivatives_v093_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc094_45d_3rd_derivatives_v094_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc095_55d_3rd_derivatives_v095_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc096_65d_3rd_derivatives_v096_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc097_75d_3rd_derivatives_v097_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc098_85d_3rd_derivatives_v098_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc099_95d_3rd_derivatives_v099_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc100_5d_3rd_derivatives_v100_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc101_15d_3rd_derivatives_v101_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc102_25d_3rd_derivatives_v102_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc103_35d_3rd_derivatives_v103_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc104_45d_3rd_derivatives_v104_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc105_55d_3rd_derivatives_v105_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc106_65d_3rd_derivatives_v106_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc107_75d_3rd_derivatives_v107_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc108_85d_3rd_derivatives_v108_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc109_95d_3rd_derivatives_v109_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc110_5d_3rd_derivatives_v110_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc111_15d_3rd_derivatives_v111_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc112_25d_3rd_derivatives_v112_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc113_35d_3rd_derivatives_v113_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc114_45d_3rd_derivatives_v114_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc115_55d_3rd_derivatives_v115_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc116_65d_3rd_derivatives_v116_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc117_75d_3rd_derivatives_v117_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc118_85d_3rd_derivatives_v118_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc119_95d_3rd_derivatives_v119_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc120_5d_3rd_derivatives_v120_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc121_15d_3rd_derivatives_v121_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc122_25d_3rd_derivatives_v122_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc123_35d_3rd_derivatives_v123_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc124_45d_3rd_derivatives_v124_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc125_55d_3rd_derivatives_v125_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc126_65d_3rd_derivatives_v126_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc127_75d_3rd_derivatives_v127_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc128_85d_3rd_derivatives_v128_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc129_95d_3rd_derivatives_v129_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc130_5d_3rd_derivatives_v130_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc131_15d_3rd_derivatives_v131_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc132_25d_3rd_derivatives_v132_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc133_35d_3rd_derivatives_v133_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc134_45d_3rd_derivatives_v134_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc135_55d_3rd_derivatives_v135_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc136_65d_3rd_derivatives_v136_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc137_75d_3rd_derivatives_v137_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc138_85d_3rd_derivatives_v138_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc139_95d_3rd_derivatives_v139_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc140_5d_3rd_derivatives_v140_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc141_15d_3rd_derivatives_v141_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 15)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc142_25d_3rd_derivatives_v142_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 25)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc143_35d_3rd_derivatives_v143_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 35)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc144_45d_3rd_derivatives_v144_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 45)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc145_55d_3rd_derivatives_v145_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 55)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc146_65d_3rd_derivatives_v146_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 65)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc147_75d_3rd_derivatives_v147_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 75)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc148_85d_3rd_derivatives_v148_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 85)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc149_95d_3rd_derivatives_v149_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 95)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc150_5d_3rd_derivatives_v150_signal(ev, ebitda, close):
    res = _roc(_roc((ev / ebitda.replace(0, np.nan) * _roc(close, 5)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['ev', 'ebitda', 'close']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f64eeo_'))]
    
    print(f"Testing {len(funcs)} functions for f64_ev_ebitda_oscillator...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f64eeo_'))]}

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
