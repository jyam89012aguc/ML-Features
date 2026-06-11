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

def f19_dealer_health_receivables_base_5d_v001_signal(receivables):
    res = _sma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_5d_v002_signal(inventory):
    res = _sma(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_5d_v003_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_5d_v004_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_10d_v005_signal(receivables):
    res = _sma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_10d_v006_signal(inventory):
    res = _sma(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_10d_v007_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_10d_v008_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_21d_v009_signal(receivables):
    res = _sma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_21d_v010_signal(inventory):
    res = _sma(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_21d_v011_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_21d_v012_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_42d_v013_signal(receivables):
    res = _sma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_42d_v014_signal(inventory):
    res = _sma(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_42d_v015_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_42d_v016_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_63d_v017_signal(receivables):
    res = _sma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_63d_v018_signal(inventory):
    res = _sma(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_63d_v019_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_63d_v020_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_126d_v021_signal(receivables):
    res = _sma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_126d_v022_signal(inventory):
    res = _sma(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_126d_v023_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_126d_v024_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_252d_v025_signal(receivables):
    res = _sma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_252d_v026_signal(inventory):
    res = _sma(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_252d_v027_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_252d_v028_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_504d_v029_signal(receivables):
    res = _sma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_504d_v030_signal(inventory):
    res = _sma(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_504d_v031_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_504d_v032_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_756d_v033_signal(receivables):
    res = _sma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_756d_v034_signal(inventory):
    res = _sma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_756d_v035_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_756d_v036_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_1008d_v037_signal(receivables):
    res = _sma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_1008d_v038_signal(inventory):
    res = _sma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_1008d_v039_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_1008d_v040_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_base_1260d_v041_signal(receivables):
    res = _sma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_base_1260d_v042_signal(inventory):
    res = _sma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_base_1260d_v043_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_base_1260d_v044_signal(receivables, inventory):
    res = _sma(_ratio(receivables, inventory), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_5d_v045_signal(receivables):
    res = _z(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_5d_v046_signal(inventory):
    res = _z(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_5d_v047_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_5d_v048_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_10d_v049_signal(receivables):
    res = _z(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_10d_v050_signal(inventory):
    res = _z(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_10d_v051_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_10d_v052_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_21d_v053_signal(receivables):
    res = _z(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_21d_v054_signal(inventory):
    res = _z(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_21d_v055_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_21d_v056_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_42d_v057_signal(receivables):
    res = _z(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_42d_v058_signal(inventory):
    res = _z(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_42d_v059_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_42d_v060_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_63d_v061_signal(receivables):
    res = _z(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_63d_v062_signal(inventory):
    res = _z(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_63d_v063_signal(revenue):
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_63d_v064_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_126d_v065_signal(receivables):
    res = _z(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_126d_v066_signal(inventory):
    res = _z(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_126d_v067_signal(revenue):
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_126d_v068_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_252d_v069_signal(receivables):
    res = _z(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_252d_v070_signal(inventory):
    res = _z(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_252d_v071_signal(revenue):
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_z_252d_v072_signal(receivables, inventory):
    res = _z(_ratio(receivables, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_z_504d_v073_signal(receivables):
    res = _z(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_z_504d_v074_signal(inventory):
    res = _z(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_z_504d_v075_signal(revenue):
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 19...")
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
