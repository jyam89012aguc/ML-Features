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

def f42_wc_cyclicality_inventory_base_5d_v001_signal(inventory):
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_5d_v002_signal(receivables):
    res = _sma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_5d_v003_signal(payables):
    res = _sma(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_5d_v004_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_5d_v005_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_10d_v006_signal(inventory):
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_10d_v007_signal(receivables):
    res = _sma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_10d_v008_signal(payables):
    res = _sma(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_10d_v009_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_10d_v010_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_21d_v011_signal(inventory):
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_21d_v012_signal(receivables):
    res = _sma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_21d_v013_signal(payables):
    res = _sma(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_21d_v014_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_21d_v015_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_42d_v016_signal(inventory):
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_42d_v017_signal(receivables):
    res = _sma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_42d_v018_signal(payables):
    res = _sma(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_42d_v019_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_42d_v020_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_63d_v021_signal(inventory):
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_63d_v022_signal(receivables):
    res = _sma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_63d_v023_signal(payables):
    res = _sma(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_63d_v024_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_63d_v025_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_126d_v026_signal(inventory):
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_126d_v027_signal(receivables):
    res = _sma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_126d_v028_signal(payables):
    res = _sma(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_126d_v029_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_126d_v030_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_252d_v031_signal(inventory):
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_252d_v032_signal(receivables):
    res = _sma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_252d_v033_signal(payables):
    res = _sma(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_252d_v034_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_252d_v035_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_504d_v036_signal(inventory):
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_504d_v037_signal(receivables):
    res = _sma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_504d_v038_signal(payables):
    res = _sma(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_504d_v039_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_504d_v040_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_756d_v041_signal(inventory):
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_756d_v042_signal(receivables):
    res = _sma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_756d_v043_signal(payables):
    res = _sma(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_756d_v044_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_756d_v045_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_1008d_v046_signal(inventory):
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_1008d_v047_signal(receivables):
    res = _sma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_1008d_v048_signal(payables):
    res = _sma(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_1008d_v049_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_1008d_v050_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_base_1260d_v051_signal(inventory):
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_base_1260d_v052_signal(receivables):
    res = _sma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_base_1260d_v053_signal(payables):
    res = _sma(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_base_1260d_v054_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_base_1260d_v055_signal(inventory, receivables, payables, revenue):
    res = _sma(_ratio(inventory + receivables - payables, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_z_5d_v056_signal(inventory):
    res = _z(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_z_5d_v057_signal(receivables):
    res = _z(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_z_5d_v058_signal(payables):
    res = _z(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_z_5d_v059_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_z_5d_v060_signal(inventory, receivables, payables, revenue):
    res = _z(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_z_10d_v061_signal(inventory):
    res = _z(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_z_10d_v062_signal(receivables):
    res = _z(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_z_10d_v063_signal(payables):
    res = _z(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_z_10d_v064_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_z_10d_v065_signal(inventory, receivables, payables, revenue):
    res = _z(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_z_21d_v066_signal(inventory):
    res = _z(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_z_21d_v067_signal(receivables):
    res = _z(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_z_21d_v068_signal(payables):
    res = _z(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_z_21d_v069_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_z_21d_v070_signal(inventory, receivables, payables, revenue):
    res = _z(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_z_42d_v071_signal(inventory):
    res = _z(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_z_42d_v072_signal(receivables):
    res = _z(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_z_42d_v073_signal(payables):
    res = _z(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_z_42d_v074_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_z_42d_v075_signal(inventory, receivables, payables, revenue):
    res = _z(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 42...")
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
