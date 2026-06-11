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


def f57tvb_f57_treasury_volatility_buffer_calc001_15d_base_v001_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc002_25d_base_v002_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc003_35d_base_v003_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc004_45d_base_v004_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc005_55d_base_v005_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc006_65d_base_v006_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc007_75d_base_v007_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc008_85d_base_v008_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc009_95d_base_v009_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc010_5d_base_v010_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc011_15d_base_v011_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc012_25d_base_v012_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc013_35d_base_v013_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc014_45d_base_v014_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc015_55d_base_v015_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc016_65d_base_v016_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc017_75d_base_v017_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc018_85d_base_v018_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc019_95d_base_v019_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc020_5d_base_v020_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc021_15d_base_v021_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc022_25d_base_v022_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc023_35d_base_v023_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc024_45d_base_v024_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc025_55d_base_v025_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc026_65d_base_v026_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc027_75d_base_v027_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc028_85d_base_v028_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc029_95d_base_v029_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc030_5d_base_v030_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc031_15d_base_v031_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc032_25d_base_v032_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc033_35d_base_v033_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc034_45d_base_v034_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc035_55d_base_v035_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc036_65d_base_v036_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc037_75d_base_v037_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc038_85d_base_v038_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc039_95d_base_v039_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc040_5d_base_v040_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc041_15d_base_v041_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc042_25d_base_v042_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc043_35d_base_v043_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc044_45d_base_v044_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc045_55d_base_v045_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc046_65d_base_v046_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc047_75d_base_v047_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc048_85d_base_v048_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc049_95d_base_v049_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc050_5d_base_v050_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc051_15d_base_v051_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc052_25d_base_v052_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc053_35d_base_v053_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc054_45d_base_v054_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc055_55d_base_v055_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc056_65d_base_v056_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc057_75d_base_v057_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc058_85d_base_v058_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc059_95d_base_v059_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc060_5d_base_v060_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc061_15d_base_v061_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc062_25d_base_v062_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc063_35d_base_v063_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc064_45d_base_v064_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc065_55d_base_v065_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc066_65d_base_v066_signal(cash, marketcap):
    res = (cash / _std(marketcap, 65).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc067_75d_base_v067_signal(cash, marketcap):
    res = (cash / _std(marketcap, 75).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc068_85d_base_v068_signal(cash, marketcap):
    res = (cash / _std(marketcap, 85).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc069_95d_base_v069_signal(cash, marketcap):
    res = (cash / _std(marketcap, 95).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc070_5d_base_v070_signal(cash, marketcap):
    res = (cash / _std(marketcap, 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc071_15d_base_v071_signal(cash, marketcap):
    res = (cash / _std(marketcap, 15).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc072_25d_base_v072_signal(cash, marketcap):
    res = (cash / _std(marketcap, 25).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc073_35d_base_v073_signal(cash, marketcap):
    res = (cash / _std(marketcap, 35).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc074_45d_base_v074_signal(cash, marketcap):
    res = (cash / _std(marketcap, 45).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f57tvb_f57_treasury_volatility_buffer_calc075_55d_base_v075_signal(cash, marketcap):
    res = (cash / _std(marketcap, 55).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['cash', 'debt', 'marketcap']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f57tvb_'))]
    
    print(f"Testing {len(funcs)} functions for f57_treasury_volatility_buffer...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f57tvb_'))]}
