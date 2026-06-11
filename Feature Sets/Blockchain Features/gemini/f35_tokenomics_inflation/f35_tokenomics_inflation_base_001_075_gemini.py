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


def f35tinf_f35_tokenomics_inflation_calc001_15d_base_v001_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc002_25d_base_v002_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc003_35d_base_v003_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc004_45d_base_v004_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc005_55d_base_v005_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc006_65d_base_v006_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc007_75d_base_v007_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc008_85d_base_v008_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc009_95d_base_v009_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc010_5d_base_v010_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc011_15d_base_v011_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc012_25d_base_v012_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc013_35d_base_v013_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc014_45d_base_v014_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc015_55d_base_v015_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc016_65d_base_v016_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc017_75d_base_v017_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc018_85d_base_v018_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc019_95d_base_v019_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc020_5d_base_v020_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc021_15d_base_v021_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc022_25d_base_v022_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc023_35d_base_v023_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc024_45d_base_v024_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc025_55d_base_v025_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc026_65d_base_v026_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc027_75d_base_v027_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc028_85d_base_v028_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc029_95d_base_v029_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc030_5d_base_v030_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc031_15d_base_v031_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc032_25d_base_v032_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc033_35d_base_v033_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc034_45d_base_v034_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc035_55d_base_v035_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc036_65d_base_v036_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc037_75d_base_v037_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc038_85d_base_v038_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc039_95d_base_v039_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc040_5d_base_v040_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc041_15d_base_v041_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc042_25d_base_v042_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc043_35d_base_v043_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc044_45d_base_v044_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc045_55d_base_v045_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc046_65d_base_v046_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc047_75d_base_v047_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc048_85d_base_v048_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc049_95d_base_v049_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc050_5d_base_v050_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc051_15d_base_v051_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc052_25d_base_v052_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc053_35d_base_v053_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc054_45d_base_v054_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc055_55d_base_v055_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc056_65d_base_v056_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc057_75d_base_v057_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc058_85d_base_v058_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc059_95d_base_v059_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc060_5d_base_v060_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc061_15d_base_v061_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc062_25d_base_v062_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc063_35d_base_v063_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc064_45d_base_v064_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc065_55d_base_v065_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc066_65d_base_v066_signal(sharesbas):
    res = _sma(sharesbas, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc067_75d_base_v067_signal(sharesbas):
    res = _sma(sharesbas, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc068_85d_base_v068_signal(sharesbas):
    res = _sma(sharesbas, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc069_95d_base_v069_signal(sharesbas):
    res = _sma(sharesbas, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc070_5d_base_v070_signal(sharesbas):
    res = _sma(sharesbas, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc071_15d_base_v071_signal(sharesbas):
    res = _sma(sharesbas, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc072_25d_base_v072_signal(sharesbas):
    res = _sma(sharesbas, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc073_35d_base_v073_signal(sharesbas):
    res = _sma(sharesbas, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc074_45d_base_v074_signal(sharesbas):
    res = _sma(sharesbas, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f35tinf_f35_tokenomics_inflation_calc075_55d_base_v075_signal(sharesbas):
    res = _sma(sharesbas, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['sharesbas', 'revenue', 'equity']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f35tinf_'))]
    
    print(f"Testing {{len(funcs)}} functions for f35_tokenomics_inflation...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f35tinf_'))]}
