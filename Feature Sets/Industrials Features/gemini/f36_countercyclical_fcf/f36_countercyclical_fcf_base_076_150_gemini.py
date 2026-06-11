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

def f36_countercyclical_fcf_fcf_z_63d_v076_signal(fcf):
    res = _z(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_63d_v077_signal(netinc):
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_63d_v078_signal(ebitda):
    res = _z(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_63d_v079_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_63d_v080_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_126d_v081_signal(fcf):
    res = _z(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_126d_v082_signal(netinc):
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_126d_v083_signal(ebitda):
    res = _z(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_126d_v084_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_126d_v085_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_252d_v086_signal(fcf):
    res = _z(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_252d_v087_signal(netinc):
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_252d_v088_signal(ebitda):
    res = _z(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_252d_v089_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_252d_v090_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_504d_v091_signal(fcf):
    res = _z(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_504d_v092_signal(netinc):
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_504d_v093_signal(ebitda):
    res = _z(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_504d_v094_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_504d_v095_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_756d_v096_signal(fcf):
    res = _z(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_756d_v097_signal(netinc):
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_756d_v098_signal(ebitda):
    res = _z(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_756d_v099_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_756d_v100_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_1008d_v101_signal(fcf):
    res = _z(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_1008d_v102_signal(netinc):
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_1008d_v103_signal(ebitda):
    res = _z(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_1008d_v104_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_1008d_v105_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_z_1260d_v106_signal(fcf):
    res = _z(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_z_1260d_v107_signal(netinc):
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_z_1260d_v108_signal(ebitda):
    res = _z(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_z_1260d_v109_signal(fcf, netinc):
    res = _z(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_z_1260d_v110_signal(fcf, ebitda):
    res = _z(_ratio(fcf, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_5d_v111_signal(fcf):
    res = _drawdown(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_5d_v112_signal(netinc):
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_5d_v113_signal(ebitda):
    res = _drawdown(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_5d_v114_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_5d_v115_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_10d_v116_signal(fcf):
    res = _drawdown(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_10d_v117_signal(netinc):
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_10d_v118_signal(ebitda):
    res = _drawdown(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_10d_v119_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_10d_v120_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_21d_v121_signal(fcf):
    res = _drawdown(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_21d_v122_signal(netinc):
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_21d_v123_signal(ebitda):
    res = _drawdown(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_21d_v124_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_21d_v125_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_42d_v126_signal(fcf):
    res = _drawdown(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_42d_v127_signal(netinc):
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_42d_v128_signal(ebitda):
    res = _drawdown(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_42d_v129_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_42d_v130_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_63d_v131_signal(fcf):
    res = _drawdown(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_63d_v132_signal(netinc):
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_63d_v133_signal(ebitda):
    res = _drawdown(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_63d_v134_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_63d_v135_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_126d_v136_signal(fcf):
    res = _drawdown(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_126d_v137_signal(netinc):
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_126d_v138_signal(ebitda):
    res = _drawdown(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_126d_v139_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_126d_v140_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_252d_v141_signal(fcf):
    res = _drawdown(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_252d_v142_signal(netinc):
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_252d_v143_signal(ebitda):
    res = _drawdown(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_252d_v144_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_252d_v145_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_dd_504d_v146_signal(fcf):
    res = _drawdown(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_dd_504d_v147_signal(netinc):
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_dd_504d_v148_signal(ebitda):
    res = _drawdown(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_dd_504d_v149_signal(fcf, netinc):
    res = _drawdown(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_dd_504d_v150_signal(fcf, ebitda):
    res = _drawdown(_ratio(fcf, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 36...")
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
