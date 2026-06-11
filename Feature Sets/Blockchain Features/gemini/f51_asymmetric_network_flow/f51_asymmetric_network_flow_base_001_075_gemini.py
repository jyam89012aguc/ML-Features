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


def f51anf_f51_asymmetric_network_flow_calc001_15d_base_v001_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc002_25d_base_v002_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc003_35d_base_v003_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc004_45d_base_v004_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc005_55d_base_v005_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc006_65d_base_v006_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc007_75d_base_v007_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc008_85d_base_v008_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc009_95d_base_v009_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc010_5d_base_v010_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc011_15d_base_v011_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc012_25d_base_v012_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc013_35d_base_v013_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc014_45d_base_v014_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc015_55d_base_v015_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc016_65d_base_v016_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc017_75d_base_v017_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc018_85d_base_v018_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc019_95d_base_v019_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc020_5d_base_v020_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc021_15d_base_v021_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc022_25d_base_v022_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc023_35d_base_v023_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc024_45d_base_v024_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc025_55d_base_v025_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc026_65d_base_v026_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc027_75d_base_v027_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc028_85d_base_v028_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc029_95d_base_v029_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc030_5d_base_v030_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc031_15d_base_v031_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc032_25d_base_v032_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc033_35d_base_v033_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc034_45d_base_v034_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc035_55d_base_v035_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc036_65d_base_v036_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc037_75d_base_v037_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc038_85d_base_v038_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc039_95d_base_v039_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc040_5d_base_v040_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc041_15d_base_v041_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc042_25d_base_v042_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc043_35d_base_v043_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc044_45d_base_v044_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc045_55d_base_v045_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc046_65d_base_v046_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc047_75d_base_v047_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc048_85d_base_v048_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc049_95d_base_v049_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc050_5d_base_v050_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc051_15d_base_v051_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc052_25d_base_v052_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc053_35d_base_v053_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc054_45d_base_v054_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc055_55d_base_v055_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc056_65d_base_v056_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc057_75d_base_v057_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc058_85d_base_v058_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc059_95d_base_v059_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc060_5d_base_v060_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc061_15d_base_v061_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc062_25d_base_v062_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc063_35d_base_v063_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc064_45d_base_v064_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc065_55d_base_v065_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc066_65d_base_v066_signal(close, volume):
    res = (_roc(closeadj, 65) * _sma(volume, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc067_75d_base_v067_signal(close, volume):
    res = (_roc(closeadj, 75) * _sma(volume, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc068_85d_base_v068_signal(close, volume):
    res = (_roc(closeadj, 85) * _sma(volume, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc069_95d_base_v069_signal(close, volume):
    res = (_roc(closeadj, 95) * _sma(volume, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc070_5d_base_v070_signal(close, volume):
    res = (_roc(close, 5) * _sma(volume, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc071_15d_base_v071_signal(close, volume):
    res = (_roc(close, 15) * _sma(volume, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc072_25d_base_v072_signal(close, volume):
    res = (_roc(closeadj, 25) * _sma(volume, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc073_35d_base_v073_signal(close, volume):
    res = (_roc(closeadj, 35) * _sma(volume, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc074_45d_base_v074_signal(close, volume):
    res = (_roc(closeadj, 45) * _sma(volume, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f51anf_f51_asymmetric_network_flow_calc075_55d_base_v075_signal(close, volume):
    res = (_roc(closeadj, 55) * _sma(volume, 55))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['close', 'volume', 'high', 'low']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f51anf_'))]
    
    print(f"Testing {len(funcs)} functions for f51_asymmetric_network_flow...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f51anf_'))]}
