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

def f09_utility_capex_revenue_base_5d_v001_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_5d_v002_signal(capex):
    res = _sma(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_5d_v003_signal(assets):
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_5d_v004_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_5d_v005_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_10d_v006_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_10d_v007_signal(capex):
    res = _sma(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_10d_v008_signal(assets):
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_10d_v009_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_10d_v010_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_21d_v011_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_21d_v012_signal(capex):
    res = _sma(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_21d_v013_signal(assets):
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_21d_v014_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_21d_v015_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_42d_v016_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_42d_v017_signal(capex):
    res = _sma(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_42d_v018_signal(assets):
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_42d_v019_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_42d_v020_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_63d_v021_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_63d_v022_signal(capex):
    res = _sma(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_63d_v023_signal(assets):
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_63d_v024_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_63d_v025_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_126d_v026_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_126d_v027_signal(capex):
    res = _sma(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_126d_v028_signal(assets):
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_126d_v029_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_126d_v030_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_252d_v031_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_252d_v032_signal(capex):
    res = _sma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_252d_v033_signal(assets):
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_252d_v034_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_252d_v035_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_504d_v036_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_504d_v037_signal(capex):
    res = _sma(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_504d_v038_signal(assets):
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_504d_v039_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_504d_v040_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_756d_v041_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_756d_v042_signal(capex):
    res = _sma(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_756d_v043_signal(assets):
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_756d_v044_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_756d_v045_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_1008d_v046_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_1008d_v047_signal(capex):
    res = _sma(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_1008d_v048_signal(assets):
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_1008d_v049_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_1008d_v050_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_base_1260d_v051_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_base_1260d_v052_signal(capex):
    res = _sma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_base_1260d_v053_signal(assets):
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_base_1260d_v054_signal(capex, assets):
    res = _sma(_ratio(capex, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_base_1260d_v055_signal(capex, revenue):
    res = _sma(_ratio(capex, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_z_5d_v056_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_z_5d_v057_signal(capex):
    res = _z(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_z_5d_v058_signal(assets):
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_z_5d_v059_signal(capex, assets):
    res = _z(_ratio(capex, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_z_5d_v060_signal(capex, revenue):
    res = _z(_ratio(capex, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_z_10d_v061_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_z_10d_v062_signal(capex):
    res = _z(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_z_10d_v063_signal(assets):
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_z_10d_v064_signal(capex, assets):
    res = _z(_ratio(capex, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_z_10d_v065_signal(capex, revenue):
    res = _z(_ratio(capex, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_z_21d_v066_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_z_21d_v067_signal(capex):
    res = _z(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_z_21d_v068_signal(assets):
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_z_21d_v069_signal(capex, assets):
    res = _z(_ratio(capex, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_z_21d_v070_signal(capex, revenue):
    res = _z(_ratio(capex, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_revenue_z_42d_v071_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_z_42d_v072_signal(capex):
    res = _z(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_assets_z_42d_v073_signal(assets):
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_assets_z_42d_v074_signal(capex, assets):
    res = _z(_ratio(capex, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_utility_capex_capex_to_rev_z_42d_v075_signal(capex, revenue):
    res = _z(_ratio(capex, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 09...")
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
