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


def f22sce_f22_smart_contract_execution_calc001_15d_base_v001_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc002_25d_base_v002_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc003_35d_base_v003_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc004_45d_base_v004_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc005_55d_base_v005_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc006_65d_base_v006_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc007_75d_base_v007_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc008_85d_base_v008_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc009_95d_base_v009_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc010_5d_base_v010_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc011_15d_base_v011_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc012_25d_base_v012_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc013_35d_base_v013_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc014_45d_base_v014_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc015_55d_base_v015_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc016_65d_base_v016_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc017_75d_base_v017_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc018_85d_base_v018_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc019_95d_base_v019_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc020_5d_base_v020_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc021_15d_base_v021_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc022_25d_base_v022_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc023_35d_base_v023_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc024_45d_base_v024_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc025_55d_base_v025_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc026_65d_base_v026_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc027_75d_base_v027_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc028_85d_base_v028_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc029_95d_base_v029_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc030_5d_base_v030_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc031_15d_base_v031_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc032_25d_base_v032_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc033_35d_base_v033_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc034_45d_base_v034_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc035_55d_base_v035_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc036_65d_base_v036_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc037_75d_base_v037_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc038_85d_base_v038_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc039_95d_base_v039_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc040_5d_base_v040_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc041_15d_base_v041_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc042_25d_base_v042_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc043_35d_base_v043_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc044_45d_base_v044_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc045_55d_base_v045_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc046_65d_base_v046_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc047_75d_base_v047_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc048_85d_base_v048_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc049_95d_base_v049_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc050_5d_base_v050_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc051_15d_base_v051_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc052_25d_base_v052_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc053_35d_base_v053_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc054_45d_base_v054_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc055_55d_base_v055_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc056_65d_base_v056_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc057_75d_base_v057_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc058_85d_base_v058_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc059_95d_base_v059_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc060_5d_base_v060_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc061_15d_base_v061_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc062_25d_base_v062_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc063_35d_base_v063_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc064_45d_base_v064_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc065_55d_base_v065_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc066_65d_base_v066_signal(close):
    res = _sma(closeadj, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc067_75d_base_v067_signal(close):
    res = _sma(closeadj, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc068_85d_base_v068_signal(close):
    res = _sma(closeadj, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc069_95d_base_v069_signal(close):
    res = _sma(closeadj, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc070_5d_base_v070_signal(close):
    res = _sma(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc071_15d_base_v071_signal(close):
    res = _sma(close, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc072_25d_base_v072_signal(close):
    res = _sma(closeadj, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc073_35d_base_v073_signal(close):
    res = _sma(closeadj, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc074_45d_base_v074_signal(close):
    res = _sma(closeadj, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f22sce_f22_smart_contract_execution_calc075_55d_base_v075_signal(close):
    res = _sma(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['open', 'close', 'high', 'low']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f22sce_'))]
    
    print(f"Testing {{len(funcs)}} functions for f22_smart_contract_execution...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f22sce_'))]}
