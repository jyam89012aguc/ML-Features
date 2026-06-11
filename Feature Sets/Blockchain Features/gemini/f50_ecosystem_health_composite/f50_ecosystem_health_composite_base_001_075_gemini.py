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


def f50ehc_f50_ecosystem_health_composite_calc001_15d_base_v001_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc002_25d_base_v002_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc003_35d_base_v003_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc004_45d_base_v004_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc005_55d_base_v005_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc006_65d_base_v006_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc007_75d_base_v007_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc008_85d_base_v008_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc009_95d_base_v009_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc010_5d_base_v010_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc011_15d_base_v011_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc012_25d_base_v012_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc013_35d_base_v013_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc014_45d_base_v014_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc015_55d_base_v015_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc016_65d_base_v016_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc017_75d_base_v017_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc018_85d_base_v018_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc019_95d_base_v019_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc020_5d_base_v020_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc021_15d_base_v021_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc022_25d_base_v022_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc023_35d_base_v023_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc024_45d_base_v024_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc025_55d_base_v025_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc026_65d_base_v026_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc027_75d_base_v027_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc028_85d_base_v028_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc029_95d_base_v029_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc030_5d_base_v030_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc031_15d_base_v031_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc032_25d_base_v032_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc033_35d_base_v033_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc034_45d_base_v034_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc035_55d_base_v035_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc036_65d_base_v036_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc037_75d_base_v037_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc038_85d_base_v038_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc039_95d_base_v039_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc040_5d_base_v040_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc041_15d_base_v041_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc042_25d_base_v042_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc043_35d_base_v043_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc044_45d_base_v044_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc045_55d_base_v045_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc046_65d_base_v046_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc047_75d_base_v047_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc048_85d_base_v048_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc049_95d_base_v049_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc050_5d_base_v050_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc051_15d_base_v051_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc052_25d_base_v052_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc053_35d_base_v053_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc054_45d_base_v054_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc055_55d_base_v055_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc056_65d_base_v056_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc057_75d_base_v057_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc058_85d_base_v058_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc059_95d_base_v059_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc060_5d_base_v060_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc061_15d_base_v061_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc062_25d_base_v062_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc063_35d_base_v063_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc064_45d_base_v064_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc065_55d_base_v065_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc066_65d_base_v066_signal(marketcap):
    res = _sma(marketcap, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc067_75d_base_v067_signal(marketcap):
    res = _sma(marketcap, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc068_85d_base_v068_signal(marketcap):
    res = _sma(marketcap, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc069_95d_base_v069_signal(marketcap):
    res = _sma(marketcap, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc070_5d_base_v070_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc071_15d_base_v071_signal(marketcap):
    res = _sma(marketcap, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc072_25d_base_v072_signal(marketcap):
    res = _sma(marketcap, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc073_35d_base_v073_signal(marketcap):
    res = _sma(marketcap, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc074_45d_base_v074_signal(marketcap):
    res = _sma(marketcap, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f50ehc_f50_ecosystem_health_composite_calc075_55d_base_v075_signal(marketcap):
    res = _sma(marketcap, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['marketcap', 'sf3a_shares', 'revenue', 'pe']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f50ehc_'))]
    
    print(f"Testing {{len(funcs)}} functions for f50_ecosystem_health_composite...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f50ehc_'))]}
