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

def f50_insider_ltip_sbcomp_base_5d_v001_signal(sbcomp):
    res = _sma(sbcomp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_5d_v002_signal(shareswa):
    res = _sma(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_5d_v003_signal(netinc):
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_5d_v004_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_5d_v005_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_10d_v006_signal(sbcomp):
    res = _sma(sbcomp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_10d_v007_signal(shareswa):
    res = _sma(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_10d_v008_signal(netinc):
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_10d_v009_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_10d_v010_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_21d_v011_signal(sbcomp):
    res = _sma(sbcomp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_21d_v012_signal(shareswa):
    res = _sma(shareswa, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_21d_v013_signal(netinc):
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_21d_v014_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_21d_v015_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_42d_v016_signal(sbcomp):
    res = _sma(sbcomp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_42d_v017_signal(shareswa):
    res = _sma(shareswa, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_42d_v018_signal(netinc):
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_42d_v019_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_42d_v020_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_63d_v021_signal(sbcomp):
    res = _sma(sbcomp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_63d_v022_signal(shareswa):
    res = _sma(shareswa, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_63d_v023_signal(netinc):
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_63d_v024_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_63d_v025_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_126d_v026_signal(sbcomp):
    res = _sma(sbcomp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_126d_v027_signal(shareswa):
    res = _sma(shareswa, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_126d_v028_signal(netinc):
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_126d_v029_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_126d_v030_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_252d_v031_signal(sbcomp):
    res = _sma(sbcomp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_252d_v032_signal(shareswa):
    res = _sma(shareswa, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_252d_v033_signal(netinc):
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_252d_v034_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_252d_v035_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_504d_v036_signal(sbcomp):
    res = _sma(sbcomp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_504d_v037_signal(shareswa):
    res = _sma(shareswa, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_504d_v038_signal(netinc):
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_504d_v039_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_504d_v040_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_756d_v041_signal(sbcomp):
    res = _sma(sbcomp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_756d_v042_signal(shareswa):
    res = _sma(shareswa, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_756d_v043_signal(netinc):
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_756d_v044_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_756d_v045_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_1008d_v046_signal(sbcomp):
    res = _sma(sbcomp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_1008d_v047_signal(shareswa):
    res = _sma(shareswa, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_1008d_v048_signal(netinc):
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_1008d_v049_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_1008d_v050_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_base_1260d_v051_signal(sbcomp):
    res = _sma(sbcomp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_base_1260d_v052_signal(shareswa):
    res = _sma(shareswa, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_base_1260d_v053_signal(netinc):
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_base_1260d_v054_signal(sbcomp, netinc):
    res = _sma(_ratio(sbcomp, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_base_1260d_v055_signal(sbcomp, shareswa):
    res = _sma(_ratio(sbcomp, shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_5d_v056_signal(sbcomp):
    res = _z(sbcomp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_5d_v057_signal(shareswa):
    res = _z(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_5d_v058_signal(netinc):
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_5d_v059_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_5d_v060_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_10d_v061_signal(sbcomp):
    res = _z(sbcomp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_10d_v062_signal(shareswa):
    res = _z(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_10d_v063_signal(netinc):
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_10d_v064_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_10d_v065_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_21d_v066_signal(sbcomp):
    res = _z(sbcomp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_21d_v067_signal(shareswa):
    res = _z(shareswa, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_21d_v068_signal(netinc):
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_21d_v069_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_21d_v070_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_42d_v071_signal(sbcomp):
    res = _z(sbcomp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_42d_v072_signal(shareswa):
    res = _z(shareswa, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_42d_v073_signal(netinc):
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_42d_v074_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_42d_v075_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 50...")
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
