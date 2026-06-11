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


def f53isv_f53_institutional_staking_velocity_calc001_15d_base_v001_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc002_25d_base_v002_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc003_35d_base_v003_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc004_45d_base_v004_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc005_55d_base_v005_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc006_65d_base_v006_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc007_75d_base_v007_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc008_85d_base_v008_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc009_95d_base_v009_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc010_5d_base_v010_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc011_15d_base_v011_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc012_25d_base_v012_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc013_35d_base_v013_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc014_45d_base_v014_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc015_55d_base_v015_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc016_65d_base_v016_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc017_75d_base_v017_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc018_85d_base_v018_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc019_95d_base_v019_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc020_5d_base_v020_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc021_15d_base_v021_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc022_25d_base_v022_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc023_35d_base_v023_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc024_45d_base_v024_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc025_55d_base_v025_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc026_65d_base_v026_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc027_75d_base_v027_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc028_85d_base_v028_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc029_95d_base_v029_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc030_5d_base_v030_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc031_15d_base_v031_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc032_25d_base_v032_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc033_35d_base_v033_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc034_45d_base_v034_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc035_55d_base_v035_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc036_65d_base_v036_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc037_75d_base_v037_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc038_85d_base_v038_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc039_95d_base_v039_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc040_5d_base_v040_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc041_15d_base_v041_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc042_25d_base_v042_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc043_35d_base_v043_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc044_45d_base_v044_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc045_55d_base_v045_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc046_65d_base_v046_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc047_75d_base_v047_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc048_85d_base_v048_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc049_95d_base_v049_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc050_5d_base_v050_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc051_15d_base_v051_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc052_25d_base_v052_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc053_35d_base_v053_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc054_45d_base_v054_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc055_55d_base_v055_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc056_65d_base_v056_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc057_75d_base_v057_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc058_85d_base_v058_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc059_95d_base_v059_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc060_5d_base_v060_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc061_15d_base_v061_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc062_25d_base_v062_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc063_35d_base_v063_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc064_45d_base_v064_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc065_55d_base_v065_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc066_65d_base_v066_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc067_75d_base_v067_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc068_85d_base_v068_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc069_95d_base_v069_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc070_5d_base_v070_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc071_15d_base_v071_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc072_25d_base_v072_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc073_35d_base_v073_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc074_45d_base_v074_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f53isv_f53_institutional_staking_velocity_calc075_55d_base_v075_signal(sf3a_value, marketcap):
    res = _roc(sf3a_value / marketcap.replace(0, np.nan), 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['sf3a_value', 'marketcap', 'sharesbas']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f53isv_'))]
    
    print(f"Testing {len(funcs)} functions for f53_institutional_staking_velocity...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f53isv_'))]}
