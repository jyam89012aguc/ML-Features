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

def f50_insider_ltip_sbcomp_z_63d_v076_signal(sbcomp):
    res = _z(sbcomp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_63d_v077_signal(shareswa):
    res = _z(shareswa, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_63d_v078_signal(netinc):
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_63d_v079_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_63d_v080_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_126d_v081_signal(sbcomp):
    res = _z(sbcomp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_126d_v082_signal(shareswa):
    res = _z(shareswa, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_126d_v083_signal(netinc):
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_126d_v084_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_126d_v085_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_252d_v086_signal(sbcomp):
    res = _z(sbcomp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_252d_v087_signal(shareswa):
    res = _z(shareswa, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_252d_v088_signal(netinc):
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_252d_v089_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_252d_v090_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_504d_v091_signal(sbcomp):
    res = _z(sbcomp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_504d_v092_signal(shareswa):
    res = _z(shareswa, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_504d_v093_signal(netinc):
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_504d_v094_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_504d_v095_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_756d_v096_signal(sbcomp):
    res = _z(sbcomp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_756d_v097_signal(shareswa):
    res = _z(shareswa, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_756d_v098_signal(netinc):
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_756d_v099_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_756d_v100_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_1008d_v101_signal(sbcomp):
    res = _z(sbcomp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_1008d_v102_signal(shareswa):
    res = _z(shareswa, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_1008d_v103_signal(netinc):
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_1008d_v104_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_1008d_v105_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_z_1260d_v106_signal(sbcomp):
    res = _z(sbcomp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_z_1260d_v107_signal(shareswa):
    res = _z(shareswa, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_z_1260d_v108_signal(netinc):
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_z_1260d_v109_signal(sbcomp, netinc):
    res = _z(_ratio(sbcomp, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_z_1260d_v110_signal(sbcomp, shareswa):
    res = _z(_ratio(sbcomp, shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_5d_v111_signal(sbcomp):
    res = _drawdown(sbcomp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_5d_v112_signal(shareswa):
    res = _drawdown(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_5d_v113_signal(netinc):
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_5d_v114_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_5d_v115_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_10d_v116_signal(sbcomp):
    res = _drawdown(sbcomp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_10d_v117_signal(shareswa):
    res = _drawdown(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_10d_v118_signal(netinc):
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_10d_v119_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_10d_v120_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_21d_v121_signal(sbcomp):
    res = _drawdown(sbcomp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_21d_v122_signal(shareswa):
    res = _drawdown(shareswa, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_21d_v123_signal(netinc):
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_21d_v124_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_21d_v125_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_42d_v126_signal(sbcomp):
    res = _drawdown(sbcomp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_42d_v127_signal(shareswa):
    res = _drawdown(shareswa, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_42d_v128_signal(netinc):
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_42d_v129_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_42d_v130_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_63d_v131_signal(sbcomp):
    res = _drawdown(sbcomp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_63d_v132_signal(shareswa):
    res = _drawdown(shareswa, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_63d_v133_signal(netinc):
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_63d_v134_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_63d_v135_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_126d_v136_signal(sbcomp):
    res = _drawdown(sbcomp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_126d_v137_signal(shareswa):
    res = _drawdown(shareswa, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_126d_v138_signal(netinc):
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_126d_v139_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_126d_v140_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_252d_v141_signal(sbcomp):
    res = _drawdown(sbcomp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_252d_v142_signal(shareswa):
    res = _drawdown(shareswa, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_252d_v143_signal(netinc):
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_252d_v144_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_252d_v145_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_dd_504d_v146_signal(sbcomp):
    res = _drawdown(sbcomp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_dd_504d_v147_signal(shareswa):
    res = _drawdown(shareswa, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_dd_504d_v148_signal(netinc):
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_dd_504d_v149_signal(sbcomp, netinc):
    res = _drawdown(_ratio(sbcomp, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_dd_504d_v150_signal(sbcomp, shareswa):
    res = _drawdown(_ratio(sbcomp, shareswa), 504)
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
