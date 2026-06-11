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


def f54lrs_f54_liquidity_regime_skew_calc001_15d_base_v001_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc002_25d_base_v002_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc003_35d_base_v003_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc004_45d_base_v004_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc005_55d_base_v005_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc006_65d_base_v006_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc007_75d_base_v007_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc008_85d_base_v008_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc009_95d_base_v009_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc010_5d_base_v010_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc011_15d_base_v011_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc012_25d_base_v012_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc013_35d_base_v013_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc014_45d_base_v014_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc015_55d_base_v015_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc016_65d_base_v016_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc017_75d_base_v017_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc018_85d_base_v018_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc019_95d_base_v019_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc020_5d_base_v020_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc021_15d_base_v021_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc022_25d_base_v022_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc023_35d_base_v023_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc024_45d_base_v024_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc025_55d_base_v025_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc026_65d_base_v026_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc027_75d_base_v027_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc028_85d_base_v028_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc029_95d_base_v029_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc030_5d_base_v030_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc031_15d_base_v031_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc032_25d_base_v032_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc033_35d_base_v033_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc034_45d_base_v034_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc035_55d_base_v035_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc036_65d_base_v036_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc037_75d_base_v037_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc038_85d_base_v038_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc039_95d_base_v039_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc040_5d_base_v040_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc041_15d_base_v041_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc042_25d_base_v042_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc043_35d_base_v043_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc044_45d_base_v044_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc045_55d_base_v045_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc046_65d_base_v046_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc047_75d_base_v047_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc048_85d_base_v048_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc049_95d_base_v049_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc050_5d_base_v050_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc051_15d_base_v051_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc052_25d_base_v052_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc053_35d_base_v053_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc054_45d_base_v054_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc055_55d_base_v055_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc056_65d_base_v056_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc057_75d_base_v057_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc058_85d_base_v058_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc059_95d_base_v059_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc060_5d_base_v060_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc061_15d_base_v061_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc062_25d_base_v062_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc063_35d_base_v063_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc064_45d_base_v064_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc065_55d_base_v065_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc066_65d_base_v066_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc067_75d_base_v067_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc068_85d_base_v068_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc069_95d_base_v069_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc070_5d_base_v070_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc071_15d_base_v071_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc072_25d_base_v072_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc073_35d_base_v073_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc074_45d_base_v074_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f54lrs_f54_liquidity_regime_skew_calc075_55d_base_v075_signal(high, low, volume):
    res = ((high - low) / _sma(volume, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['high', 'low', 'volume', 'closeadj']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f54lrs_'))]
    
    print(f"Testing {len(funcs)} functions for f54_liquidity_regime_skew...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f54lrs_'))]}
