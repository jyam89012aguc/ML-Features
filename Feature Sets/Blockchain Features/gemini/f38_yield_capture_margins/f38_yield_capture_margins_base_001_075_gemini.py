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


def f38ycm_f38_yield_capture_margins_calc001_15d_base_v001_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc002_25d_base_v002_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc003_35d_base_v003_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc004_45d_base_v004_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc005_55d_base_v005_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc006_65d_base_v006_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc007_75d_base_v007_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc008_85d_base_v008_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc009_95d_base_v009_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc010_5d_base_v010_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc011_15d_base_v011_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc012_25d_base_v012_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc013_35d_base_v013_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc014_45d_base_v014_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc015_55d_base_v015_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc016_65d_base_v016_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc017_75d_base_v017_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc018_85d_base_v018_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc019_95d_base_v019_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc020_5d_base_v020_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc021_15d_base_v021_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc022_25d_base_v022_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc023_35d_base_v023_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc024_45d_base_v024_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc025_55d_base_v025_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc026_65d_base_v026_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc027_75d_base_v027_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc028_85d_base_v028_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc029_95d_base_v029_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc030_5d_base_v030_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc031_15d_base_v031_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc032_25d_base_v032_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc033_35d_base_v033_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc034_45d_base_v034_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc035_55d_base_v035_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc036_65d_base_v036_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc037_75d_base_v037_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc038_85d_base_v038_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc039_95d_base_v039_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc040_5d_base_v040_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc041_15d_base_v041_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc042_25d_base_v042_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc043_35d_base_v043_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc044_45d_base_v044_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc045_55d_base_v045_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc046_65d_base_v046_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc047_75d_base_v047_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc048_85d_base_v048_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc049_95d_base_v049_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc050_5d_base_v050_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc051_15d_base_v051_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc052_25d_base_v052_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc053_35d_base_v053_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc054_45d_base_v054_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc055_55d_base_v055_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc056_65d_base_v056_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc057_75d_base_v057_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc058_85d_base_v058_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc059_95d_base_v059_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc060_5d_base_v060_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc061_15d_base_v061_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc062_25d_base_v062_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc063_35d_base_v063_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc064_45d_base_v064_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc065_55d_base_v065_signal(ebitda):
    res = _sma(ebitda, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc066_65d_base_v066_signal(ebitda):
    res = _sma(ebitda, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc067_75d_base_v067_signal(ebitda):
    res = _sma(ebitda, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc068_85d_base_v068_signal(ebitda):
    res = _sma(ebitda, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc069_95d_base_v069_signal(ebitda):
    res = _sma(ebitda, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc070_5d_base_v070_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc071_15d_base_v071_signal(ebitda):
    res = _sma(ebitda, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc072_25d_base_v072_signal(ebitda):
    res = _sma(ebitda, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc073_35d_base_v073_signal(ebitda):
    res = _sma(ebitda, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc074_45d_base_v074_signal(ebitda):
    res = _sma(ebitda, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f38ycm_f38_yield_capture_margins_calc075_55d_base_v075_signal(ebitda):
    res = _sma(ebitda, 55)
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
