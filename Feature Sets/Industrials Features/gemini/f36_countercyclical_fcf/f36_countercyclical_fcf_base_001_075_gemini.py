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

def f36_countercyclical_fcf_fcf_base_5d_v001_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_5d_v002_signal(netinc):
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_5d_v003_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_5d_v004_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_5d_v005_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_10d_v006_signal(fcf):
    res = _sma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_10d_v007_signal(netinc):
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_10d_v008_signal(ebitda):
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_10d_v009_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_10d_v010_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_21d_v011_signal(fcf):
    res = _sma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_21d_v012_signal(netinc):
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_21d_v013_signal(ebitda):
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_21d_v014_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_21d_v015_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_42d_v016_signal(fcf):
    res = _sma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_42d_v017_signal(netinc):
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_42d_v018_signal(ebitda):
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_42d_v019_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_42d_v020_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_63d_v021_signal(fcf):
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_63d_v022_signal(netinc):
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_63d_v023_signal(ebitda):
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_63d_v024_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_63d_v025_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_126d_v026_signal(fcf):
    res = _sma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_126d_v027_signal(netinc):
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_126d_v028_signal(ebitda):
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_126d_v029_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_126d_v030_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_252d_v031_signal(fcf):
    res = _sma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_252d_v032_signal(netinc):
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_252d_v033_signal(ebitda):
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_252d_v034_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_252d_v035_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_504d_v036_signal(fcf):
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_504d_v037_signal(netinc):
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_504d_v038_signal(ebitda):
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_504d_v039_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_504d_v040_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_756d_v041_signal(fcf):
    res = _sma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_756d_v042_signal(netinc):
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_756d_v043_signal(ebitda):
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_756d_v044_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_756d_v045_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_1008d_v046_signal(fcf):
    res = _sma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_1008d_v047_signal(netinc):
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_1008d_v048_signal(ebitda):
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_1008d_v049_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_1008d_v050_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_base_1260d_v051_signal(fcf):
    res = _sma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_base_1260d_v052_signal(netinc):
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_base_1260d_v053_signal(ebitda):
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_base_1260d_v054_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_base_1260d_v055_signal(fcf, ebitda):
    res = _sma(_ratio(fcf, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_5d_v056_signal(fcf):
    res = _z(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_5d_v057_signal(netinc):
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_5d_v058_signal(ebitda):
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_5d_v059_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_5d_v060_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_10d_v061_signal(fcf):
    res = _z(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_10d_v062_signal(netinc):
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_10d_v063_signal(ebitda):
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_10d_v064_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_10d_v065_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_21d_v066_signal(fcf):
    res = _z(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_21d_v067_signal(netinc):
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_21d_v068_signal(ebitda):
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_21d_v069_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_21d_v070_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_42d_v071_signal(fcf):
    res = _z(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_42d_v072_signal(netinc):
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_42d_v073_signal(ebitda):
    res = _z(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_42d_v074_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_42d_v075_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 36...")
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
