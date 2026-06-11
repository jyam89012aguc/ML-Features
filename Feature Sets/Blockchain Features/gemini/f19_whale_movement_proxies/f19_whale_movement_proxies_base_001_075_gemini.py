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


def f19wmp_f19_whale_movement_proxies_calc001_15d_base_v001_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc002_25d_base_v002_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc003_35d_base_v003_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc004_45d_base_v004_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc005_55d_base_v005_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc006_65d_base_v006_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc007_75d_base_v007_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc008_85d_base_v008_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc009_95d_base_v009_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc010_5d_base_v010_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc011_15d_base_v011_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc012_25d_base_v012_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc013_35d_base_v013_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc014_45d_base_v014_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc015_55d_base_v015_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc016_65d_base_v016_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc017_75d_base_v017_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc018_85d_base_v018_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc019_95d_base_v019_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc020_5d_base_v020_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc021_15d_base_v021_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc022_25d_base_v022_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc023_35d_base_v023_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc024_45d_base_v024_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc025_55d_base_v025_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc026_65d_base_v026_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc027_75d_base_v027_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc028_85d_base_v028_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc029_95d_base_v029_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc030_5d_base_v030_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc031_15d_base_v031_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc032_25d_base_v032_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc033_35d_base_v033_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc034_45d_base_v034_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc035_55d_base_v035_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc036_65d_base_v036_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc037_75d_base_v037_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc038_85d_base_v038_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc039_95d_base_v039_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc040_5d_base_v040_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc041_15d_base_v041_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc042_25d_base_v042_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc043_35d_base_v043_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc044_45d_base_v044_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc045_55d_base_v045_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc046_65d_base_v046_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc047_75d_base_v047_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc048_85d_base_v048_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc049_95d_base_v049_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc050_5d_base_v050_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc051_15d_base_v051_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc052_25d_base_v052_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc053_35d_base_v053_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc054_45d_base_v054_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc055_55d_base_v055_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc056_65d_base_v056_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc057_75d_base_v057_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc058_85d_base_v058_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc059_95d_base_v059_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc060_5d_base_v060_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc061_15d_base_v061_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc062_25d_base_v062_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc063_35d_base_v063_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc064_45d_base_v064_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc065_55d_base_v065_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc066_65d_base_v066_signal(volume, close, closeadj):
    res = (_sma(closeadj, 65) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc067_75d_base_v067_signal(volume, close, closeadj):
    res = (_sma(closeadj, 75) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc068_85d_base_v068_signal(volume, close, closeadj):
    res = (_sma(closeadj, 85) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc069_95d_base_v069_signal(volume, close, closeadj):
    res = (_sma(closeadj, 95) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc070_5d_base_v070_signal(volume, close):
    res = (_sma(close, 5) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc071_15d_base_v071_signal(volume, close):
    res = (_sma(close, 15) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc072_25d_base_v072_signal(volume, close, closeadj):
    res = (_sma(closeadj, 25) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc073_35d_base_v073_signal(volume, close, closeadj):
    res = (_sma(closeadj, 35) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc074_45d_base_v074_signal(volume, close, closeadj):
    res = (_sma(closeadj, 45) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f19wmp_f19_whale_movement_proxies_calc075_55d_base_v075_signal(volume, close, closeadj):
    res = (_sma(closeadj, 55) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['volume', 'close', 'closeadj']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f19wmp_'))]
    
    print(f"Testing {{len(funcs)}} functions for f19_whale_movement_proxies...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f19wmp_'))]}
