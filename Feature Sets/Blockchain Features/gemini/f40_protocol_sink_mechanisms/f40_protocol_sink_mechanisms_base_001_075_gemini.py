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


def f40psm_f40_protocol_sink_mechanisms_calc001_15d_base_v001_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc002_25d_base_v002_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc003_35d_base_v003_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc004_45d_base_v004_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc005_55d_base_v005_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc006_65d_base_v006_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc007_75d_base_v007_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc008_85d_base_v008_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc009_95d_base_v009_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc010_5d_base_v010_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc011_15d_base_v011_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc012_25d_base_v012_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc013_35d_base_v013_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc014_45d_base_v014_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc015_55d_base_v015_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc016_65d_base_v016_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc017_75d_base_v017_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc018_85d_base_v018_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc019_95d_base_v019_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc020_5d_base_v020_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc021_15d_base_v021_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc022_25d_base_v022_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc023_35d_base_v023_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc024_45d_base_v024_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc025_55d_base_v025_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc026_65d_base_v026_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc027_75d_base_v027_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc028_85d_base_v028_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc029_95d_base_v029_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc030_5d_base_v030_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc031_15d_base_v031_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc032_25d_base_v032_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc033_35d_base_v033_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc034_45d_base_v034_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc035_55d_base_v035_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc036_65d_base_v036_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc037_75d_base_v037_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc038_85d_base_v038_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc039_95d_base_v039_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc040_5d_base_v040_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc041_15d_base_v041_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc042_25d_base_v042_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc043_35d_base_v043_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc044_45d_base_v044_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc045_55d_base_v045_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc046_65d_base_v046_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc047_75d_base_v047_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc048_85d_base_v048_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc049_95d_base_v049_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc050_5d_base_v050_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc051_15d_base_v051_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc052_25d_base_v052_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc053_35d_base_v053_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc054_45d_base_v054_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc055_55d_base_v055_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc056_65d_base_v056_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc057_75d_base_v057_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc058_85d_base_v058_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc059_95d_base_v059_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc060_5d_base_v060_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc061_15d_base_v061_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc062_25d_base_v062_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc063_35d_base_v063_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc064_45d_base_v064_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc065_55d_base_v065_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc066_65d_base_v066_signal(fcf):
    res = _sma(fcf, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc067_75d_base_v067_signal(fcf):
    res = _sma(fcf, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc068_85d_base_v068_signal(fcf):
    res = _sma(fcf, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc069_95d_base_v069_signal(fcf):
    res = _sma(fcf, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc070_5d_base_v070_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc071_15d_base_v071_signal(fcf):
    res = _sma(fcf, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc072_25d_base_v072_signal(fcf):
    res = _sma(fcf, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc073_35d_base_v073_signal(fcf):
    res = _sma(fcf, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc074_45d_base_v074_signal(fcf):
    res = _sma(fcf, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40psm_f40_protocol_sink_mechanisms_calc075_55d_base_v075_signal(fcf):
    res = _sma(fcf, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['fcf', 'revenue', 'netinc']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f40psm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f40_protocol_sink_mechanisms...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f40psm_'))]}
