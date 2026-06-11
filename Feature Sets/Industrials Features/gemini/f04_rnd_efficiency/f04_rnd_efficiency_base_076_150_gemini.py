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

def f04_rnd_efficiency_rnd_z_63d_v076_signal(rnd):
    res = _z(rnd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_63d_v077_signal(revenue):
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_63d_v078_signal(ebit):
    res = _z(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_63d_v079_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_63d_v080_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_z_126d_v081_signal(rnd):
    res = _z(rnd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_126d_v082_signal(revenue):
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_126d_v083_signal(ebit):
    res = _z(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_126d_v084_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_126d_v085_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_z_252d_v086_signal(rnd):
    res = _z(rnd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_252d_v087_signal(revenue):
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_252d_v088_signal(ebit):
    res = _z(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_252d_v089_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_252d_v090_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_z_504d_v091_signal(rnd):
    res = _z(rnd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_504d_v092_signal(revenue):
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_504d_v093_signal(ebit):
    res = _z(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_504d_v094_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_504d_v095_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_z_756d_v096_signal(rnd):
    res = _z(rnd, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_756d_v097_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_756d_v098_signal(ebit):
    res = _z(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_756d_v099_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_756d_v100_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_z_1008d_v101_signal(rnd):
    res = _z(rnd, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_1008d_v102_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_1008d_v103_signal(ebit):
    res = _z(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_1008d_v104_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_1008d_v105_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_z_1260d_v106_signal(rnd):
    res = _z(rnd, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_z_1260d_v107_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_z_1260d_v108_signal(ebit):
    res = _z(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_z_1260d_v109_signal(rnd, revenue):
    res = _z(_ratio(rnd, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_z_1260d_v110_signal(rnd, ebit):
    res = _z(_ratio(rnd, ebit), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_5d_v111_signal(rnd):
    res = _drawdown(rnd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_5d_v112_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_5d_v113_signal(ebit):
    res = _drawdown(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_5d_v114_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_5d_v115_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_10d_v116_signal(rnd):
    res = _drawdown(rnd, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_10d_v117_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_10d_v118_signal(ebit):
    res = _drawdown(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_10d_v119_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_10d_v120_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_21d_v121_signal(rnd):
    res = _drawdown(rnd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_21d_v122_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_21d_v123_signal(ebit):
    res = _drawdown(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_21d_v124_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_21d_v125_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_42d_v126_signal(rnd):
    res = _drawdown(rnd, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_42d_v127_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_42d_v128_signal(ebit):
    res = _drawdown(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_42d_v129_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_42d_v130_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_63d_v131_signal(rnd):
    res = _drawdown(rnd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_63d_v132_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_63d_v133_signal(ebit):
    res = _drawdown(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_63d_v134_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_63d_v135_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_126d_v136_signal(rnd):
    res = _drawdown(rnd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_126d_v137_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_126d_v138_signal(ebit):
    res = _drawdown(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_126d_v139_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_126d_v140_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_252d_v141_signal(rnd):
    res = _drawdown(rnd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_252d_v142_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_252d_v143_signal(ebit):
    res = _drawdown(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_252d_v144_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_252d_v145_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_dd_504d_v146_signal(rnd):
    res = _drawdown(rnd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_dd_504d_v147_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_dd_504d_v148_signal(ebit):
    res = _drawdown(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_dd_504d_v149_signal(rnd, revenue):
    res = _drawdown(_ratio(rnd, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_dd_504d_v150_signal(rnd, ebit):
    res = _drawdown(_ratio(rnd, ebit), 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 04...")
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
