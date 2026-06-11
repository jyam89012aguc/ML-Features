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


def f42sth_f42_scaling_throughput_calc001_15d_base_v001_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc002_25d_base_v002_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc003_35d_base_v003_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc004_45d_base_v004_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc005_55d_base_v005_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc006_65d_base_v006_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc007_75d_base_v007_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc008_85d_base_v008_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc009_95d_base_v009_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc010_5d_base_v010_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc011_15d_base_v011_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc012_25d_base_v012_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc013_35d_base_v013_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc014_45d_base_v014_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc015_55d_base_v015_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc016_65d_base_v016_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc017_75d_base_v017_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc018_85d_base_v018_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc019_95d_base_v019_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc020_5d_base_v020_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc021_15d_base_v021_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc022_25d_base_v022_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc023_35d_base_v023_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc024_45d_base_v024_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc025_55d_base_v025_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc026_65d_base_v026_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc027_75d_base_v027_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc028_85d_base_v028_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc029_95d_base_v029_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc030_5d_base_v030_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc031_15d_base_v031_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc032_25d_base_v032_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc033_35d_base_v033_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc034_45d_base_v034_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc035_55d_base_v035_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc036_65d_base_v036_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc037_75d_base_v037_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc038_85d_base_v038_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc039_95d_base_v039_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc040_5d_base_v040_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc041_15d_base_v041_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc042_25d_base_v042_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc043_35d_base_v043_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc044_45d_base_v044_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc045_55d_base_v045_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc046_65d_base_v046_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc047_75d_base_v047_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc048_85d_base_v048_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc049_95d_base_v049_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc050_5d_base_v050_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc051_15d_base_v051_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc052_25d_base_v052_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc053_35d_base_v053_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc054_45d_base_v054_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc055_55d_base_v055_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc056_65d_base_v056_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc057_75d_base_v057_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc058_85d_base_v058_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc059_95d_base_v059_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc060_5d_base_v060_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc061_15d_base_v061_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc062_25d_base_v062_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc063_35d_base_v063_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc064_45d_base_v064_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc065_55d_base_v065_signal(revenue):
    res = _sma(revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc066_65d_base_v066_signal(revenue):
    res = _sma(revenue, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc067_75d_base_v067_signal(revenue):
    res = _sma(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc068_85d_base_v068_signal(revenue):
    res = _sma(revenue, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc069_95d_base_v069_signal(revenue):
    res = _sma(revenue, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc070_5d_base_v070_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc071_15d_base_v071_signal(revenue):
    res = _sma(revenue, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc072_25d_base_v072_signal(revenue):
    res = _sma(revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc073_35d_base_v073_signal(revenue):
    res = _sma(revenue, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc074_45d_base_v074_signal(revenue):
    res = _sma(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f42sth_f42_scaling_throughput_calc075_55d_base_v075_signal(revenue):
    res = _sma(revenue, 55)
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
