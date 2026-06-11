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

def f07_supplier_pricing_grossmargin_base_5d_v001_signal(grossmargin):
    res = _sma(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_5d_v002_signal(cor):
    res = _sma(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_5d_v003_signal(gp):
    res = _sma(gp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_5d_v004_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_5d_v005_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_10d_v006_signal(grossmargin):
    res = _sma(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_10d_v007_signal(cor):
    res = _sma(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_10d_v008_signal(gp):
    res = _sma(gp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_10d_v009_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_10d_v010_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_21d_v011_signal(grossmargin):
    res = _sma(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_21d_v012_signal(cor):
    res = _sma(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_21d_v013_signal(gp):
    res = _sma(gp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_21d_v014_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_21d_v015_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_42d_v016_signal(grossmargin):
    res = _sma(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_42d_v017_signal(cor):
    res = _sma(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_42d_v018_signal(gp):
    res = _sma(gp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_42d_v019_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_42d_v020_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_63d_v021_signal(grossmargin):
    res = _sma(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_63d_v022_signal(cor):
    res = _sma(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_63d_v023_signal(gp):
    res = _sma(gp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_63d_v024_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_63d_v025_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_126d_v026_signal(grossmargin):
    res = _sma(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_126d_v027_signal(cor):
    res = _sma(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_126d_v028_signal(gp):
    res = _sma(gp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_126d_v029_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_126d_v030_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_252d_v031_signal(grossmargin):
    res = _sma(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_252d_v032_signal(cor):
    res = _sma(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_252d_v033_signal(gp):
    res = _sma(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_252d_v034_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_252d_v035_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_504d_v036_signal(grossmargin):
    res = _sma(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_504d_v037_signal(cor):
    res = _sma(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_504d_v038_signal(gp):
    res = _sma(gp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_504d_v039_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_504d_v040_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_756d_v041_signal(grossmargin):
    res = _sma(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_756d_v042_signal(cor):
    res = _sma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_756d_v043_signal(gp):
    res = _sma(gp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_756d_v044_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_756d_v045_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_1008d_v046_signal(grossmargin):
    res = _sma(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_1008d_v047_signal(cor):
    res = _sma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_1008d_v048_signal(gp):
    res = _sma(gp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_1008d_v049_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_1008d_v050_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_base_1260d_v051_signal(grossmargin):
    res = _sma(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_base_1260d_v052_signal(cor):
    res = _sma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_base_1260d_v053_signal(gp):
    res = _sma(gp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_base_1260d_v054_signal(cor, gp):
    res = _sma(_ratio(cor, gp + cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_base_1260d_v055_signal(gp, cor):
    res = _sma(_ratio(gp, cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_5d_v056_signal(grossmargin):
    res = _z(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_5d_v057_signal(cor):
    res = _z(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_5d_v058_signal(gp):
    res = _z(gp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_5d_v059_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_5d_v060_signal(gp, cor):
    res = _z(_ratio(gp, cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_10d_v061_signal(grossmargin):
    res = _z(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_10d_v062_signal(cor):
    res = _z(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_10d_v063_signal(gp):
    res = _z(gp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_10d_v064_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_10d_v065_signal(gp, cor):
    res = _z(_ratio(gp, cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_21d_v066_signal(grossmargin):
    res = _z(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_21d_v067_signal(cor):
    res = _z(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_21d_v068_signal(gp):
    res = _z(gp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_21d_v069_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_21d_v070_signal(gp, cor):
    res = _z(_ratio(gp, cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_42d_v071_signal(grossmargin):
    res = _z(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_42d_v072_signal(cor):
    res = _z(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_42d_v073_signal(gp):
    res = _z(gp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_42d_v074_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_42d_v075_signal(gp, cor):
    res = _z(_ratio(gp, cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "gp": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 07...")
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
