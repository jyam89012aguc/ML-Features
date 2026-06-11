import pandas as pd
import numpy as np
import inspect

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f05_platform_lifecycle_ebitdamargin_base_5d_v001_signal(ebitdamargin):
    res = _sma(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_5d_v002_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_5d_v003_signal(ebit):
    res = _sma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_5d_v004_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_10d_v005_signal(ebitdamargin):
    res = _sma(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_10d_v006_signal(ebitda):
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_10d_v007_signal(ebit):
    res = _sma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_10d_v008_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_21d_v009_signal(ebitdamargin):
    res = _sma(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_21d_v010_signal(ebitda):
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_21d_v011_signal(ebit):
    res = _sma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_21d_v012_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_42d_v013_signal(ebitdamargin):
    res = _sma(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_42d_v014_signal(ebitda):
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_42d_v015_signal(ebit):
    res = _sma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_42d_v016_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_63d_v017_signal(ebitdamargin):
    res = _sma(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_63d_v018_signal(ebitda):
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_63d_v019_signal(ebit):
    res = _sma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_63d_v020_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_126d_v021_signal(ebitdamargin):
    res = _sma(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_126d_v022_signal(ebitda):
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_126d_v023_signal(ebit):
    res = _sma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_126d_v024_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_252d_v025_signal(ebitdamargin):
    res = _sma(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_252d_v026_signal(ebitda):
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_252d_v027_signal(ebit):
    res = _sma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_252d_v028_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_504d_v029_signal(ebitdamargin):
    res = _sma(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_504d_v030_signal(ebitda):
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_504d_v031_signal(ebit):
    res = _sma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_504d_v032_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_756d_v033_signal(ebitdamargin):
    res = _sma(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_756d_v034_signal(ebitda):
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_756d_v035_signal(ebit):
    res = _sma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_756d_v036_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_1008d_v037_signal(ebitdamargin):
    res = _sma(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_1008d_v038_signal(ebitda):
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_1008d_v039_signal(ebit):
    res = _sma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_1008d_v040_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_base_1260d_v041_signal(ebitdamargin):
    res = _sma(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_base_1260d_v042_signal(ebitda):
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_base_1260d_v043_signal(ebit):
    res = _sma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_base_1260d_v044_signal(ebit, ebitda):
    res = _sma(_ratio(ebit, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_5d_v045_signal(ebitdamargin):
    res = _z(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_5d_v046_signal(ebitda):
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_5d_v047_signal(ebit):
    res = _z(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_5d_v048_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_10d_v049_signal(ebitdamargin):
    res = _z(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_10d_v050_signal(ebitda):
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_10d_v051_signal(ebit):
    res = _z(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_10d_v052_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_21d_v053_signal(ebitdamargin):
    res = _z(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_21d_v054_signal(ebitda):
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_21d_v055_signal(ebit):
    res = _z(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_21d_v056_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_42d_v057_signal(ebitdamargin):
    res = _z(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_42d_v058_signal(ebitda):
    res = _z(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_42d_v059_signal(ebit):
    res = _z(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_42d_v060_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_63d_v061_signal(ebitdamargin):
    res = _z(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_63d_v062_signal(ebitda):
    res = _z(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_63d_v063_signal(ebit):
    res = _z(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_63d_v064_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_126d_v065_signal(ebitdamargin):
    res = _z(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_126d_v066_signal(ebitda):
    res = _z(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_126d_v067_signal(ebit):
    res = _z(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_126d_v068_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_252d_v069_signal(ebitdamargin):
    res = _z(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_252d_v070_signal(ebitda):
    res = _z(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_252d_v071_signal(ebit):
    res = _z(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_252d_v072_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_504d_v073_signal(ebitdamargin):
    res = _z(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_504d_v074_signal(ebitda):
    res = _z(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_504d_v075_signal(ebit):
    res = _z(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 05...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        try:
            res = func(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            break
    print("Success.")
