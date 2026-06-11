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


def f41gov_f41_governance_overhead_calc001_15d_base_v001_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc002_25d_base_v002_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc003_35d_base_v003_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc004_45d_base_v004_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc005_55d_base_v005_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc006_65d_base_v006_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc007_75d_base_v007_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc008_85d_base_v008_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc009_95d_base_v009_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc010_5d_base_v010_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc011_15d_base_v011_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc012_25d_base_v012_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc013_35d_base_v013_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc014_45d_base_v014_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc015_55d_base_v015_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc016_65d_base_v016_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc017_75d_base_v017_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc018_85d_base_v018_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc019_95d_base_v019_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc020_5d_base_v020_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc021_15d_base_v021_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc022_25d_base_v022_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc023_35d_base_v023_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc024_45d_base_v024_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc025_55d_base_v025_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc026_65d_base_v026_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc027_75d_base_v027_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc028_85d_base_v028_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc029_95d_base_v029_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc030_5d_base_v030_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc031_15d_base_v031_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc032_25d_base_v032_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc033_35d_base_v033_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc034_45d_base_v034_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc035_55d_base_v035_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc036_65d_base_v036_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc037_75d_base_v037_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc038_85d_base_v038_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc039_95d_base_v039_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc040_5d_base_v040_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc041_15d_base_v041_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc042_25d_base_v042_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc043_35d_base_v043_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc044_45d_base_v044_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc045_55d_base_v045_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc046_65d_base_v046_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc047_75d_base_v047_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc048_85d_base_v048_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc049_95d_base_v049_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc050_5d_base_v050_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc051_15d_base_v051_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc052_25d_base_v052_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc053_35d_base_v053_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc054_45d_base_v054_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc055_55d_base_v055_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc056_65d_base_v056_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc057_75d_base_v057_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc058_85d_base_v058_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc059_95d_base_v059_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc060_5d_base_v060_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc061_15d_base_v061_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc062_25d_base_v062_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc063_35d_base_v063_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc064_45d_base_v064_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc065_55d_base_v065_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc066_65d_base_v066_signal(opinc):
    res = _sma(opinc, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc067_75d_base_v067_signal(opinc):
    res = _sma(opinc, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc068_85d_base_v068_signal(opinc):
    res = _sma(opinc, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc069_95d_base_v069_signal(opinc):
    res = _sma(opinc, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc070_5d_base_v070_signal(opinc):
    res = _sma(opinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc071_15d_base_v071_signal(opinc):
    res = _sma(opinc, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc072_25d_base_v072_signal(opinc):
    res = _sma(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc073_35d_base_v073_signal(opinc):
    res = _sma(opinc, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc074_45d_base_v074_signal(opinc):
    res = _sma(opinc, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f41gov_f41_governance_overhead_calc075_55d_base_v075_signal(opinc):
    res = _sma(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['opinc', 'revenue', 'ebitda']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f41gov_'))]
    
    print(f"Testing {{len(funcs)}} functions for f41_governance_overhead...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f41gov_'))]}
