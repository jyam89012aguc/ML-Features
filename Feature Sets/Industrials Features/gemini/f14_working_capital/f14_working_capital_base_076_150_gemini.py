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

def f14_working_capital_receivables_z_63d_v076_signal(receivables):
    res = _z(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_63d_v077_signal(inventory):
    res = _z(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_63d_v078_signal(payables):
    res = _z(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_63d_v079_signal(revenue):
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_63d_v080_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_z_126d_v081_signal(receivables):
    res = _z(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_126d_v082_signal(inventory):
    res = _z(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_126d_v083_signal(payables):
    res = _z(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_126d_v084_signal(revenue):
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_126d_v085_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_z_252d_v086_signal(receivables):
    res = _z(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_252d_v087_signal(inventory):
    res = _z(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_252d_v088_signal(payables):
    res = _z(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_252d_v089_signal(revenue):
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_252d_v090_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_z_504d_v091_signal(receivables):
    res = _z(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_504d_v092_signal(inventory):
    res = _z(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_504d_v093_signal(payables):
    res = _z(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_504d_v094_signal(revenue):
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_504d_v095_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_z_756d_v096_signal(receivables):
    res = _z(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_756d_v097_signal(inventory):
    res = _z(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_756d_v098_signal(payables):
    res = _z(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_756d_v099_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_756d_v100_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_z_1008d_v101_signal(receivables):
    res = _z(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_1008d_v102_signal(inventory):
    res = _z(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_1008d_v103_signal(payables):
    res = _z(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_1008d_v104_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_1008d_v105_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_z_1260d_v106_signal(receivables):
    res = _z(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_z_1260d_v107_signal(inventory):
    res = _z(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_z_1260d_v108_signal(payables):
    res = _z(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_z_1260d_v109_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_z_1260d_v110_signal(receivables, inventory, payables, revenue):
    res = _z(_ratio(receivables + inventory - payables, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_5d_v111_signal(receivables):
    res = _drawdown(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_5d_v112_signal(inventory):
    res = _drawdown(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_5d_v113_signal(payables):
    res = _drawdown(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_5d_v114_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_5d_v115_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_10d_v116_signal(receivables):
    res = _drawdown(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_10d_v117_signal(inventory):
    res = _drawdown(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_10d_v118_signal(payables):
    res = _drawdown(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_10d_v119_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_10d_v120_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_21d_v121_signal(receivables):
    res = _drawdown(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_21d_v122_signal(inventory):
    res = _drawdown(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_21d_v123_signal(payables):
    res = _drawdown(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_21d_v124_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_21d_v125_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_42d_v126_signal(receivables):
    res = _drawdown(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_42d_v127_signal(inventory):
    res = _drawdown(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_42d_v128_signal(payables):
    res = _drawdown(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_42d_v129_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_42d_v130_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_63d_v131_signal(receivables):
    res = _drawdown(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_63d_v132_signal(inventory):
    res = _drawdown(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_63d_v133_signal(payables):
    res = _drawdown(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_63d_v134_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_63d_v135_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_126d_v136_signal(receivables):
    res = _drawdown(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_126d_v137_signal(inventory):
    res = _drawdown(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_126d_v138_signal(payables):
    res = _drawdown(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_126d_v139_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_126d_v140_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_252d_v141_signal(receivables):
    res = _drawdown(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_252d_v142_signal(inventory):
    res = _drawdown(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_252d_v143_signal(payables):
    res = _drawdown(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_252d_v144_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_252d_v145_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_receivables_dd_504d_v146_signal(receivables):
    res = _drawdown(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_inventory_dd_504d_v147_signal(inventory):
    res = _drawdown(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_payables_dd_504d_v148_signal(payables):
    res = _drawdown(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_revenue_dd_504d_v149_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_working_capital_nwc_to_rev_dd_504d_v150_signal(receivables, inventory, payables, revenue):
    res = _drawdown(_ratio(receivables + inventory - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 14...")
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
