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


def f62rpm_f62_revenue_price_momentum_calc001_15d_base_v001_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc002_25d_base_v002_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc003_35d_base_v003_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc004_45d_base_v004_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc005_55d_base_v005_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc006_65d_base_v006_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc007_75d_base_v007_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc008_85d_base_v008_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc009_95d_base_v009_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc010_5d_base_v010_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc011_15d_base_v011_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc012_25d_base_v012_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc013_35d_base_v013_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc014_45d_base_v014_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc015_55d_base_v015_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc016_65d_base_v016_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc017_75d_base_v017_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc018_85d_base_v018_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc019_95d_base_v019_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc020_5d_base_v020_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc021_15d_base_v021_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc022_25d_base_v022_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc023_35d_base_v023_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc024_45d_base_v024_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc025_55d_base_v025_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc026_65d_base_v026_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc027_75d_base_v027_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc028_85d_base_v028_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc029_95d_base_v029_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc030_5d_base_v030_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc031_15d_base_v031_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc032_25d_base_v032_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc033_35d_base_v033_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc034_45d_base_v034_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc035_55d_base_v035_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc036_65d_base_v036_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc037_75d_base_v037_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc038_85d_base_v038_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc039_95d_base_v039_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc040_5d_base_v040_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc041_15d_base_v041_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc042_25d_base_v042_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc043_35d_base_v043_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc044_45d_base_v044_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc045_55d_base_v045_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc046_65d_base_v046_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc047_75d_base_v047_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc048_85d_base_v048_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc049_95d_base_v049_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc050_5d_base_v050_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc051_15d_base_v051_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc052_25d_base_v052_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc053_35d_base_v053_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc054_45d_base_v054_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc055_55d_base_v055_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc056_65d_base_v056_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc057_75d_base_v057_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc058_85d_base_v058_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc059_95d_base_v059_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc060_5d_base_v060_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc061_15d_base_v061_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc062_25d_base_v062_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc063_35d_base_v063_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc064_45d_base_v064_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc065_55d_base_v065_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc066_65d_base_v066_signal(revenue, closeadj):
    res = (_roc(closeadj, 65) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc067_75d_base_v067_signal(revenue, closeadj):
    res = (_roc(closeadj, 75) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc068_85d_base_v068_signal(revenue, closeadj):
    res = (_roc(closeadj, 85) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc069_95d_base_v069_signal(revenue, closeadj):
    res = (_roc(closeadj, 95) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc070_5d_base_v070_signal(revenue, closeadj):
    res = (_roc(closeadj, 5) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc071_15d_base_v071_signal(revenue, closeadj):
    res = (_roc(closeadj, 15) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc072_25d_base_v072_signal(revenue, closeadj):
    res = (_roc(closeadj, 25) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc073_35d_base_v073_signal(revenue, closeadj):
    res = (_roc(closeadj, 35) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc074_45d_base_v074_signal(revenue, closeadj):
    res = (_roc(closeadj, 45) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

def f62rpm_f62_revenue_price_momentum_calc075_55d_base_v075_signal(revenue, closeadj):
    res = (_roc(closeadj, 55) * revenue)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['revenue', 'closeadj', 'volume']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f62rpm_'))]
    
    print(f"Testing {len(funcs)} functions for f62_revenue_price_momentum...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f62rpm_'))]}
