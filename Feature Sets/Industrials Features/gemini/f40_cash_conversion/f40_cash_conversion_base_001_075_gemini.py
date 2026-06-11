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

def f40_cash_conversion_fcf_base_5d_v001_signal(fcf):
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_5d_v002_signal(netinc):
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_5d_v003_signal(ebitda):
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_5d_v004_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_10d_v005_signal(fcf):
    res = _sma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_10d_v006_signal(netinc):
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_10d_v007_signal(ebitda):
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_10d_v008_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_21d_v009_signal(fcf):
    res = _sma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_21d_v010_signal(netinc):
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_21d_v011_signal(ebitda):
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_21d_v012_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_42d_v013_signal(fcf):
    res = _sma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_42d_v014_signal(netinc):
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_42d_v015_signal(ebitda):
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_42d_v016_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_63d_v017_signal(fcf):
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_63d_v018_signal(netinc):
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_63d_v019_signal(ebitda):
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_63d_v020_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_126d_v021_signal(fcf):
    res = _sma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_126d_v022_signal(netinc):
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_126d_v023_signal(ebitda):
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_126d_v024_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_252d_v025_signal(fcf):
    res = _sma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_252d_v026_signal(netinc):
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_252d_v027_signal(ebitda):
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_252d_v028_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_504d_v029_signal(fcf):
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_504d_v030_signal(netinc):
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_504d_v031_signal(ebitda):
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_504d_v032_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_756d_v033_signal(fcf):
    res = _sma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_756d_v034_signal(netinc):
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_756d_v035_signal(ebitda):
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_756d_v036_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_1008d_v037_signal(fcf):
    res = _sma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_1008d_v038_signal(netinc):
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_1008d_v039_signal(ebitda):
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_1008d_v040_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_base_1260d_v041_signal(fcf):
    res = _sma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_base_1260d_v042_signal(netinc):
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_base_1260d_v043_signal(ebitda):
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_base_1260d_v044_signal(fcf, netinc):
    res = _sma(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_5d_v045_signal(fcf):
    res = _z(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_5d_v046_signal(netinc):
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_5d_v047_signal(ebitda):
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_5d_v048_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_10d_v049_signal(fcf):
    res = _z(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_10d_v050_signal(netinc):
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_10d_v051_signal(ebitda):
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_10d_v052_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_21d_v053_signal(fcf):
    res = _z(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_21d_v054_signal(netinc):
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_21d_v055_signal(ebitda):
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_21d_v056_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_42d_v057_signal(fcf):
    res = _z(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_42d_v058_signal(netinc):
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_42d_v059_signal(ebitda):
    res = _z(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_42d_v060_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_63d_v061_signal(fcf):
    res = _z(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_63d_v062_signal(netinc):
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_63d_v063_signal(ebitda):
    res = _z(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_63d_v064_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_126d_v065_signal(fcf):
    res = _z(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_126d_v066_signal(netinc):
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_126d_v067_signal(ebitda):
    res = _z(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_126d_v068_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_252d_v069_signal(fcf):
    res = _z(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_252d_v070_signal(netinc):
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_252d_v071_signal(ebitda):
    res = _z(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_z_252d_v072_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_z_504d_v073_signal(fcf):
    res = _z(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_z_504d_v074_signal(netinc):
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_z_504d_v075_signal(ebitda):
    res = _z(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 40...")
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
