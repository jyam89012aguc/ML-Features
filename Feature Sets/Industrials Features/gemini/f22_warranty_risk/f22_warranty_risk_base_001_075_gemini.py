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

def f22_warranty_risk_sgna_base_5d_v001_signal(sgna):
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_5d_v002_signal(revenue):
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_5d_v003_signal(netinc):
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_5d_v004_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_10d_v005_signal(sgna):
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_10d_v006_signal(revenue):
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_10d_v007_signal(netinc):
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_10d_v008_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_21d_v009_signal(sgna):
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_21d_v010_signal(revenue):
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_21d_v011_signal(netinc):
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_21d_v012_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_42d_v013_signal(sgna):
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_42d_v014_signal(revenue):
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_42d_v015_signal(netinc):
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_42d_v016_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_63d_v017_signal(sgna):
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_63d_v018_signal(revenue):
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_63d_v019_signal(netinc):
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_63d_v020_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_126d_v021_signal(sgna):
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_126d_v022_signal(revenue):
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_126d_v023_signal(netinc):
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_126d_v024_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_252d_v025_signal(sgna):
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_252d_v026_signal(revenue):
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_252d_v027_signal(netinc):
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_252d_v028_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_504d_v029_signal(sgna):
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_504d_v030_signal(revenue):
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_504d_v031_signal(netinc):
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_504d_v032_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_756d_v033_signal(sgna):
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_756d_v034_signal(revenue):
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_756d_v035_signal(netinc):
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_756d_v036_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_1008d_v037_signal(sgna):
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_1008d_v038_signal(revenue):
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_1008d_v039_signal(netinc):
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_1008d_v040_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_base_1260d_v041_signal(sgna):
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_base_1260d_v042_signal(revenue):
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_base_1260d_v043_signal(netinc):
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_base_1260d_v044_signal(sgna, revenue):
    res = _sma(_ratio(sgna, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_5d_v045_signal(sgna):
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_5d_v046_signal(revenue):
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_5d_v047_signal(netinc):
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_5d_v048_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_10d_v049_signal(sgna):
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_10d_v050_signal(revenue):
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_10d_v051_signal(netinc):
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_10d_v052_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_21d_v053_signal(sgna):
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_21d_v054_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_21d_v055_signal(netinc):
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_21d_v056_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_42d_v057_signal(sgna):
    res = _z(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_42d_v058_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_42d_v059_signal(netinc):
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_42d_v060_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_63d_v061_signal(sgna):
    res = _z(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_63d_v062_signal(revenue):
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_63d_v063_signal(netinc):
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_63d_v064_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_126d_v065_signal(sgna):
    res = _z(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_126d_v066_signal(revenue):
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_126d_v067_signal(netinc):
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_126d_v068_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_252d_v069_signal(sgna):
    res = _z(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_252d_v070_signal(revenue):
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_252d_v071_signal(netinc):
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_z_252d_v072_signal(sgna, revenue):
    res = _z(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_z_504d_v073_signal(sgna):
    res = _z(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_z_504d_v074_signal(revenue):
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_z_504d_v075_signal(netinc):
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 22...")
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
