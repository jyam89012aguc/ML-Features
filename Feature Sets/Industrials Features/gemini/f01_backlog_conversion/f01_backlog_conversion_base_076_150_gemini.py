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

def f01_backlog_conversion_backlog_to_rev_z_10d_v076_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_10d_v077_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_10d_v078_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_21d_v079_signal(deferredrev):
    res = _z(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_21d_v080_signal(revenue):
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_21d_v081_signal(marketcap):
    res = _z(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_21d_v082_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_21d_v083_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_21d_v084_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_42d_v085_signal(deferredrev):
    res = _z(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_42d_v086_signal(revenue):
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_42d_v087_signal(marketcap):
    res = _z(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_42d_v088_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_42d_v089_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_42d_v090_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_63d_v091_signal(deferredrev):
    res = _z(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_63d_v092_signal(revenue):
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_63d_v093_signal(marketcap):
    res = _z(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_63d_v094_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_63d_v095_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_63d_v096_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_126d_v097_signal(deferredrev):
    res = _z(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_126d_v098_signal(revenue):
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_126d_v099_signal(marketcap):
    res = _z(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_126d_v100_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_126d_v101_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_126d_v102_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_252d_v103_signal(deferredrev):
    res = _z(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_252d_v104_signal(revenue):
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_252d_v105_signal(marketcap):
    res = _z(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_252d_v106_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_252d_v107_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_252d_v108_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_504d_v109_signal(deferredrev):
    res = _z(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_504d_v110_signal(revenue):
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_504d_v111_signal(marketcap):
    res = _z(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_504d_v112_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_504d_v113_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_504d_v114_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_756d_v115_signal(deferredrev):
    res = _z(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_756d_v116_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_756d_v117_signal(marketcap):
    res = _z(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_756d_v118_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_756d_v119_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_756d_v120_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_1008d_v121_signal(deferredrev):
    res = _z(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_1008d_v122_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_1008d_v123_signal(marketcap):
    res = _z(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_1008d_v124_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_1008d_v125_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_1008d_v126_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_z_1260d_v127_signal(deferredrev):
    res = _z(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_z_1260d_v128_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_z_1260d_v129_signal(marketcap):
    res = _z(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_z_1260d_v130_signal(deferredrev, revenue):
    res = _z(_ratio(deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_z_1260d_v131_signal(revenue, deferredrev):
    res = _z(_ratio(revenue, deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_z_1260d_v132_signal(deferredrev, marketcap):
    res = _z(_ratio(deferredrev, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_dd_5d_v133_signal(deferredrev):
    res = _drawdown(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_dd_5d_v134_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_dd_5d_v135_signal(marketcap):
    res = _drawdown(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_dd_5d_v136_signal(deferredrev, revenue):
    res = _drawdown(_ratio(deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_dd_5d_v137_signal(revenue, deferredrev):
    res = _drawdown(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_dd_5d_v138_signal(deferredrev, marketcap):
    res = _drawdown(_ratio(deferredrev, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_dd_10d_v139_signal(deferredrev):
    res = _drawdown(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_dd_10d_v140_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_dd_10d_v141_signal(marketcap):
    res = _drawdown(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_dd_10d_v142_signal(deferredrev, revenue):
    res = _drawdown(_ratio(deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_dd_10d_v143_signal(revenue, deferredrev):
    res = _drawdown(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_dd_10d_v144_signal(deferredrev, marketcap):
    res = _drawdown(_ratio(deferredrev, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_dd_21d_v145_signal(deferredrev):
    res = _drawdown(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_dd_21d_v146_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_dd_21d_v147_signal(marketcap):
    res = _drawdown(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_dd_21d_v148_signal(deferredrev, revenue):
    res = _drawdown(_ratio(deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_dd_21d_v149_signal(revenue, deferredrev):
    res = _drawdown(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_dd_21d_v150_signal(deferredrev, marketcap):
    res = _drawdown(_ratio(deferredrev, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 01...")
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
