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


def f47nvm_f47_network_valuation_multiples_calc001_15d_base_v001_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc002_25d_base_v002_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc003_35d_base_v003_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc004_45d_base_v004_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc005_55d_base_v005_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc006_65d_base_v006_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc007_75d_base_v007_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc008_85d_base_v008_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc009_95d_base_v009_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc010_5d_base_v010_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc011_15d_base_v011_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc012_25d_base_v012_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc013_35d_base_v013_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc014_45d_base_v014_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc015_55d_base_v015_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc016_65d_base_v016_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc017_75d_base_v017_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc018_85d_base_v018_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc019_95d_base_v019_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc020_5d_base_v020_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc021_15d_base_v021_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc022_25d_base_v022_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc023_35d_base_v023_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc024_45d_base_v024_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc025_55d_base_v025_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc026_65d_base_v026_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc027_75d_base_v027_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc028_85d_base_v028_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc029_95d_base_v029_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc030_5d_base_v030_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc031_15d_base_v031_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc032_25d_base_v032_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc033_35d_base_v033_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc034_45d_base_v034_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc035_55d_base_v035_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc036_65d_base_v036_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc037_75d_base_v037_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc038_85d_base_v038_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc039_95d_base_v039_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc040_5d_base_v040_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc041_15d_base_v041_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc042_25d_base_v042_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc043_35d_base_v043_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc044_45d_base_v044_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc045_55d_base_v045_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc046_65d_base_v046_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc047_75d_base_v047_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc048_85d_base_v048_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc049_95d_base_v049_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc050_5d_base_v050_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc051_15d_base_v051_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc052_25d_base_v052_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc053_35d_base_v053_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc054_45d_base_v054_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc055_55d_base_v055_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc056_65d_base_v056_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc057_75d_base_v057_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc058_85d_base_v058_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc059_95d_base_v059_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc060_5d_base_v060_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc061_15d_base_v061_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc062_25d_base_v062_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc063_35d_base_v063_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc064_45d_base_v064_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc065_55d_base_v065_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc066_65d_base_v066_signal(pe):
    res = _sma(pe, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc067_75d_base_v067_signal(pe):
    res = _sma(pe, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc068_85d_base_v068_signal(pe):
    res = _sma(pe, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc069_95d_base_v069_signal(pe):
    res = _sma(pe, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc070_5d_base_v070_signal(pe):
    res = _sma(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc071_15d_base_v071_signal(pe):
    res = _sma(pe, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc072_25d_base_v072_signal(pe):
    res = _sma(pe, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc073_35d_base_v073_signal(pe):
    res = _sma(pe, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc074_45d_base_v074_signal(pe):
    res = _sma(pe, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f47nvm_f47_network_valuation_multiples_calc075_55d_base_v075_signal(pe):
    res = _sma(pe, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['pe', 'ps', 'pb', 'marketcap']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f47nvm_'))]
    
    print(f"Testing {{len(funcs)}} functions for f47_network_valuation_multiples...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f47nvm_'))]}
