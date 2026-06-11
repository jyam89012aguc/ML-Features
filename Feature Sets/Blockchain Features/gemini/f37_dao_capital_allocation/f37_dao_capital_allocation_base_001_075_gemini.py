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


def f37dca_f37_dao_capital_allocation_calc001_15d_base_v001_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc002_25d_base_v002_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc003_35d_base_v003_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc004_45d_base_v004_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc005_55d_base_v005_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc006_65d_base_v006_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc007_75d_base_v007_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc008_85d_base_v008_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc009_95d_base_v009_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc010_5d_base_v010_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc011_15d_base_v011_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc012_25d_base_v012_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc013_35d_base_v013_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc014_45d_base_v014_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc015_55d_base_v015_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc016_65d_base_v016_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc017_75d_base_v017_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc018_85d_base_v018_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc019_95d_base_v019_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc020_5d_base_v020_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc021_15d_base_v021_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc022_25d_base_v022_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc023_35d_base_v023_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc024_45d_base_v024_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc025_55d_base_v025_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc026_65d_base_v026_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc027_75d_base_v027_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc028_85d_base_v028_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc029_95d_base_v029_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc030_5d_base_v030_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc031_15d_base_v031_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc032_25d_base_v032_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc033_35d_base_v033_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc034_45d_base_v034_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc035_55d_base_v035_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc036_65d_base_v036_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc037_75d_base_v037_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc038_85d_base_v038_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc039_95d_base_v039_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc040_5d_base_v040_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc041_15d_base_v041_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc042_25d_base_v042_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc043_35d_base_v043_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc044_45d_base_v044_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc045_55d_base_v045_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc046_65d_base_v046_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc047_75d_base_v047_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc048_85d_base_v048_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc049_95d_base_v049_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc050_5d_base_v050_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc051_15d_base_v051_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc052_25d_base_v052_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc053_35d_base_v053_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc054_45d_base_v054_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc055_55d_base_v055_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc056_65d_base_v056_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc057_75d_base_v057_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc058_85d_base_v058_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc059_95d_base_v059_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc060_5d_base_v060_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc061_15d_base_v061_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc062_25d_base_v062_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc063_35d_base_v063_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc064_45d_base_v064_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc065_55d_base_v065_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc066_65d_base_v066_signal(capex):
    res = _sma(capex, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc067_75d_base_v067_signal(capex):
    res = _sma(capex, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc068_85d_base_v068_signal(capex):
    res = _sma(capex, 85)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc069_95d_base_v069_signal(capex):
    res = _sma(capex, 95)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc070_5d_base_v070_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc071_15d_base_v071_signal(capex):
    res = _sma(capex, 15)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc072_25d_base_v072_signal(capex):
    res = _sma(capex, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc073_35d_base_v073_signal(capex):
    res = _sma(capex, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc074_45d_base_v074_signal(capex):
    res = _sma(capex, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f37dca_f37_dao_capital_allocation_calc075_55d_base_v075_signal(capex):
    res = _sma(capex, 55)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['capex', 'revenue', 'assets']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f37dca_'))]
    
    print(f"Testing {{len(funcs)}} functions for f37_dao_capital_allocation...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{{func.__name__}} must return a Series"
        assert not res.isna().all(), f"{{func.__name__}} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f37dca_'))]}
