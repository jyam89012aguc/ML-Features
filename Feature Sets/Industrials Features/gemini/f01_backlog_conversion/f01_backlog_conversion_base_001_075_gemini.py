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

def f01_backlog_conversion_deferredrev_base_5d_v001_signal(deferredrev):
    res = _sma(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_5d_v002_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_5d_v003_signal(marketcap):
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_5d_v004_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_5d_v005_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_5d_v006_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_10d_v007_signal(deferredrev):
    res = _sma(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_10d_v008_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_10d_v009_signal(marketcap):
    res = _sma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_10d_v010_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_10d_v011_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_10d_v012_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_21d_v013_signal(deferredrev):
    res = _sma(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_21d_v014_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_21d_v015_signal(marketcap):
    res = _sma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_21d_v016_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_21d_v017_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_21d_v018_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_42d_v019_signal(deferredrev):
    res = _sma(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_42d_v020_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_42d_v021_signal(marketcap):
    res = _sma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_42d_v022_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_42d_v023_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_42d_v024_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_63d_v025_signal(deferredrev):
    res = _sma(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_63d_v026_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_63d_v027_signal(marketcap):
    res = _sma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_63d_v028_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_63d_v029_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_63d_v030_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_126d_v031_signal(deferredrev):
    res = _sma(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_126d_v032_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_126d_v033_signal(marketcap):
    res = _sma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_126d_v034_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_126d_v035_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_126d_v036_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_252d_v037_signal(deferredrev):
    res = _sma(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_252d_v038_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_252d_v039_signal(marketcap):
    res = _sma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_252d_v040_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_252d_v041_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_252d_v042_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_504d_v043_signal(deferredrev):
    res = _sma(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_504d_v044_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_504d_v045_signal(marketcap):
    res = _sma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_504d_v046_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_504d_v047_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_504d_v048_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_756d_v049_signal(deferredrev):
    res = _sma(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_756d_v050_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_756d_v051_signal(marketcap):
    res = _sma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_756d_v052_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_756d_v053_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_756d_v054_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_1008d_v055_signal(deferredrev):
    res = _sma(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_1008d_v056_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_1008d_v057_signal(marketcap):
    res = _sma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_1008d_v058_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_1008d_v059_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_1008d_v060_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_base_1260d_v061_signal(deferredrev):
    res = _sma(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_base_1260d_v062_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_base_1260d_v063_signal(marketcap):
    res = _sma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_base_1260d_v064_signal(deferredrev, revenue):
    res = _sma(_ratio(deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_base_1260d_v065_signal(revenue, deferredrev):
    res = _sma(_ratio(revenue, deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_base_1260d_v066_signal(deferredrev, marketcap):
    res = _sma(_ratio(deferredrev, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_5d_v067_signal(deferredrev):
    res = _z(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_5d_v068_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_5d_v069_signal(marketcap):
    res = _z(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_5d_v070_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_5d_v071_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_5d_v072_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_10d_v073_signal(deferredrev):
    res = _z(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_10d_v074_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_10d_v075_signal(marketcap):
    res = _z(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 01...")
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
