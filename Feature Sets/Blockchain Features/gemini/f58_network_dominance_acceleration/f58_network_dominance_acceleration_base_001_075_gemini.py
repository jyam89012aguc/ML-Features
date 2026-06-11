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


def f58nda_f58_network_dominance_acceleration_calc001_15d_base_v001_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc002_25d_base_v002_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc003_35d_base_v003_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc004_45d_base_v004_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc005_55d_base_v005_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc006_65d_base_v006_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc007_75d_base_v007_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc008_85d_base_v008_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc009_95d_base_v009_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc010_5d_base_v010_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc011_15d_base_v011_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc012_25d_base_v012_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc013_35d_base_v013_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc014_45d_base_v014_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc015_55d_base_v015_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc016_65d_base_v016_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc017_75d_base_v017_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc018_85d_base_v018_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc019_95d_base_v019_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc020_5d_base_v020_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc021_15d_base_v021_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc022_25d_base_v022_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc023_35d_base_v023_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc024_45d_base_v024_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc025_55d_base_v025_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc026_65d_base_v026_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc027_75d_base_v027_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc028_85d_base_v028_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc029_95d_base_v029_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc030_5d_base_v030_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc031_15d_base_v031_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc032_25d_base_v032_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc033_35d_base_v033_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc034_45d_base_v034_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc035_55d_base_v035_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc036_65d_base_v036_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc037_75d_base_v037_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc038_85d_base_v038_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc039_95d_base_v039_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc040_5d_base_v040_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc041_15d_base_v041_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc042_25d_base_v042_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc043_35d_base_v043_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc044_45d_base_v044_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc045_55d_base_v045_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc046_65d_base_v046_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc047_75d_base_v047_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc048_85d_base_v048_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc049_95d_base_v049_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc050_5d_base_v050_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc051_15d_base_v051_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc052_25d_base_v052_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc053_35d_base_v053_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc054_45d_base_v054_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc055_55d_base_v055_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc056_65d_base_v056_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc057_75d_base_v057_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc058_85d_base_v058_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc059_95d_base_v059_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc060_5d_base_v060_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc061_15d_base_v061_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc062_25d_base_v062_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc063_35d_base_v063_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc064_45d_base_v064_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc065_55d_base_v065_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc066_65d_base_v066_signal(marketcap):
    res = _roc(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc067_75d_base_v067_signal(marketcap):
    res = _roc(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc068_85d_base_v068_signal(marketcap):
    res = _roc(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc069_95d_base_v069_signal(marketcap):
    res = _roc(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc070_5d_base_v070_signal(marketcap):
    res = _roc(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc071_15d_base_v071_signal(marketcap):
    res = _roc(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc072_25d_base_v072_signal(marketcap):
    res = _roc(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc073_35d_base_v073_signal(marketcap):
    res = _roc(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc074_45d_base_v074_signal(marketcap):
    res = _roc(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f58nda_f58_network_dominance_acceleration_calc075_55d_base_v075_signal(marketcap):
    res = _roc(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['marketcap', 'ev', 'sf3a_shares']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f58nda_'))]
    
    print(f"Testing {len(funcs)} functions for f58_network_dominance_acceleration...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f58nda_'))]}
