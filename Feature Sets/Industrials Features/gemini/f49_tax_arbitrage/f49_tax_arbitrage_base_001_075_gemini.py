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

def f49_tax_arbitrage_taxexp_base_5d_v001_signal(taxexp):
    res = _sma(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_5d_v002_signal(ebt):
    res = _sma(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_5d_v003_signal(netinc):
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_5d_v004_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_10d_v005_signal(taxexp):
    res = _sma(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_10d_v006_signal(ebt):
    res = _sma(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_10d_v007_signal(netinc):
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_10d_v008_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_21d_v009_signal(taxexp):
    res = _sma(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_21d_v010_signal(ebt):
    res = _sma(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_21d_v011_signal(netinc):
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_21d_v012_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_42d_v013_signal(taxexp):
    res = _sma(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_42d_v014_signal(ebt):
    res = _sma(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_42d_v015_signal(netinc):
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_42d_v016_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_63d_v017_signal(taxexp):
    res = _sma(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_63d_v018_signal(ebt):
    res = _sma(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_63d_v019_signal(netinc):
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_63d_v020_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_126d_v021_signal(taxexp):
    res = _sma(taxexp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_126d_v022_signal(ebt):
    res = _sma(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_126d_v023_signal(netinc):
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_126d_v024_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_252d_v025_signal(taxexp):
    res = _sma(taxexp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_252d_v026_signal(ebt):
    res = _sma(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_252d_v027_signal(netinc):
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_252d_v028_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_504d_v029_signal(taxexp):
    res = _sma(taxexp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_504d_v030_signal(ebt):
    res = _sma(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_504d_v031_signal(netinc):
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_504d_v032_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_756d_v033_signal(taxexp):
    res = _sma(taxexp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_756d_v034_signal(ebt):
    res = _sma(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_756d_v035_signal(netinc):
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_756d_v036_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_1008d_v037_signal(taxexp):
    res = _sma(taxexp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_1008d_v038_signal(ebt):
    res = _sma(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_1008d_v039_signal(netinc):
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_1008d_v040_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_base_1260d_v041_signal(taxexp):
    res = _sma(taxexp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_base_1260d_v042_signal(ebt):
    res = _sma(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_base_1260d_v043_signal(netinc):
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_base_1260d_v044_signal(taxexp, ebt):
    res = _sma(_ratio(taxexp, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_5d_v045_signal(taxexp):
    res = _z(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_5d_v046_signal(ebt):
    res = _z(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_5d_v047_signal(netinc):
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_5d_v048_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_10d_v049_signal(taxexp):
    res = _z(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_10d_v050_signal(ebt):
    res = _z(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_10d_v051_signal(netinc):
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_10d_v052_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_21d_v053_signal(taxexp):
    res = _z(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_21d_v054_signal(ebt):
    res = _z(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_21d_v055_signal(netinc):
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_21d_v056_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_42d_v057_signal(taxexp):
    res = _z(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_42d_v058_signal(ebt):
    res = _z(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_42d_v059_signal(netinc):
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_42d_v060_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_63d_v061_signal(taxexp):
    res = _z(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_63d_v062_signal(ebt):
    res = _z(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_63d_v063_signal(netinc):
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_63d_v064_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_126d_v065_signal(taxexp):
    res = _z(taxexp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_126d_v066_signal(ebt):
    res = _z(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_126d_v067_signal(netinc):
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_126d_v068_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_252d_v069_signal(taxexp):
    res = _z(taxexp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_252d_v070_signal(ebt):
    res = _z(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_252d_v071_signal(netinc):
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_effective_tax_z_252d_v072_signal(taxexp, ebt):
    res = _z(_ratio(taxexp, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_taxexp_z_504d_v073_signal(taxexp):
    res = _z(taxexp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_ebt_z_504d_v074_signal(ebt):
    res = _z(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_tax_arbitrage_netinc_z_504d_v075_signal(netinc):
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 49...")
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
