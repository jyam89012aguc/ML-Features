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

def f45_pension_drag_netinc_base_5d_v001_signal(netinc):
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_5d_v002_signal(assets):
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_5d_v003_signal(debt):
    res = _sma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_5d_v004_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_10d_v005_signal(netinc):
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_10d_v006_signal(assets):
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_10d_v007_signal(debt):
    res = _sma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_10d_v008_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_21d_v009_signal(netinc):
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_21d_v010_signal(assets):
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_21d_v011_signal(debt):
    res = _sma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_21d_v012_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_42d_v013_signal(netinc):
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_42d_v014_signal(assets):
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_42d_v015_signal(debt):
    res = _sma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_42d_v016_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_63d_v017_signal(netinc):
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_63d_v018_signal(assets):
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_63d_v019_signal(debt):
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_63d_v020_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_126d_v021_signal(netinc):
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_126d_v022_signal(assets):
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_126d_v023_signal(debt):
    res = _sma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_126d_v024_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_252d_v025_signal(netinc):
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_252d_v026_signal(assets):
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_252d_v027_signal(debt):
    res = _sma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_252d_v028_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_504d_v029_signal(netinc):
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_504d_v030_signal(assets):
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_504d_v031_signal(debt):
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_504d_v032_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_756d_v033_signal(netinc):
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_756d_v034_signal(assets):
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_756d_v035_signal(debt):
    res = _sma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_756d_v036_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_1008d_v037_signal(netinc):
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_1008d_v038_signal(assets):
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_1008d_v039_signal(debt):
    res = _sma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_1008d_v040_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_base_1260d_v041_signal(netinc):
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_base_1260d_v042_signal(assets):
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_base_1260d_v043_signal(debt):
    res = _sma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_base_1260d_v044_signal(debt, assets):
    res = _sma(_ratio(debt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_5d_v045_signal(netinc):
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_5d_v046_signal(assets):
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_5d_v047_signal(debt):
    res = _z(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_5d_v048_signal(debt, assets):
    res = _z(_ratio(debt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_10d_v049_signal(netinc):
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_10d_v050_signal(assets):
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_10d_v051_signal(debt):
    res = _z(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_10d_v052_signal(debt, assets):
    res = _z(_ratio(debt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_21d_v053_signal(netinc):
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_21d_v054_signal(assets):
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_21d_v055_signal(debt):
    res = _z(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_21d_v056_signal(debt, assets):
    res = _z(_ratio(debt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_42d_v057_signal(netinc):
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_42d_v058_signal(assets):
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_42d_v059_signal(debt):
    res = _z(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_42d_v060_signal(debt, assets):
    res = _z(_ratio(debt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_63d_v061_signal(netinc):
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_63d_v062_signal(assets):
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_63d_v063_signal(debt):
    res = _z(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_63d_v064_signal(debt, assets):
    res = _z(_ratio(debt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_126d_v065_signal(netinc):
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_126d_v066_signal(assets):
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_126d_v067_signal(debt):
    res = _z(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_126d_v068_signal(debt, assets):
    res = _z(_ratio(debt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_252d_v069_signal(netinc):
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_252d_v070_signal(assets):
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_252d_v071_signal(debt):
    res = _z(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_z_252d_v072_signal(debt, assets):
    res = _z(_ratio(debt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_z_504d_v073_signal(netinc):
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_z_504d_v074_signal(assets):
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_z_504d_v075_signal(debt):
    res = _z(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 45...")
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
