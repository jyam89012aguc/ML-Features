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


def f64eeo_f64_ev_ebitda_oscillator_calc001_15d_base_v001_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc002_25d_base_v002_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc003_35d_base_v003_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc004_45d_base_v004_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc005_55d_base_v005_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc006_65d_base_v006_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc007_75d_base_v007_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc008_85d_base_v008_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc009_95d_base_v009_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc010_5d_base_v010_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc011_15d_base_v011_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc012_25d_base_v012_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc013_35d_base_v013_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc014_45d_base_v014_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc015_55d_base_v015_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc016_65d_base_v016_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc017_75d_base_v017_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc018_85d_base_v018_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc019_95d_base_v019_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc020_5d_base_v020_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc021_15d_base_v021_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc022_25d_base_v022_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc023_35d_base_v023_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc024_45d_base_v024_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc025_55d_base_v025_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc026_65d_base_v026_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc027_75d_base_v027_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc028_85d_base_v028_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc029_95d_base_v029_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc030_5d_base_v030_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc031_15d_base_v031_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc032_25d_base_v032_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc033_35d_base_v033_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc034_45d_base_v034_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc035_55d_base_v035_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc036_65d_base_v036_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc037_75d_base_v037_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc038_85d_base_v038_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc039_95d_base_v039_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc040_5d_base_v040_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc041_15d_base_v041_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc042_25d_base_v042_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc043_35d_base_v043_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc044_45d_base_v044_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc045_55d_base_v045_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc046_65d_base_v046_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc047_75d_base_v047_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc048_85d_base_v048_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc049_95d_base_v049_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc050_5d_base_v050_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc051_15d_base_v051_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc052_25d_base_v052_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc053_35d_base_v053_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc054_45d_base_v054_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc055_55d_base_v055_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc056_65d_base_v056_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc057_75d_base_v057_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc058_85d_base_v058_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc059_95d_base_v059_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc060_5d_base_v060_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc061_15d_base_v061_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc062_25d_base_v062_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc063_35d_base_v063_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc064_45d_base_v064_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc065_55d_base_v065_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc066_65d_base_v066_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 65))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc067_75d_base_v067_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 75))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc068_85d_base_v068_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 85))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc069_95d_base_v069_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 95))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc070_5d_base_v070_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc071_15d_base_v071_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc072_25d_base_v072_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 25))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc073_35d_base_v073_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 35))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc074_45d_base_v074_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 45))
    return res.replace([np.inf, -np.inf], np.nan)

def f64eeo_f64_ev_ebitda_oscillator_calc075_55d_base_v075_signal(ev, ebitda, close):
    res = (ev / ebitda.replace(0, np.nan) * _roc(close, 55))
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    cols = ['ev', 'ebitda', 'close']
    df = pd.DataFrame({col: np.random.normal(100, 10, n).cumsum() for col in cols})
    for col in cols: df[col] = df[col].abs() + 1
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith('f64eeo_'))]
    
    print(f"Testing {len(funcs)} functions for f64_ev_ebitda_oscillator...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        res = func(*args)
        assert isinstance(res, pd.Series), f"{func.__name__} must return a Series"
        assert not res.isna().all(), f"{func.__name__} is all NaN"
    
    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith('f64eeo_'))]}
