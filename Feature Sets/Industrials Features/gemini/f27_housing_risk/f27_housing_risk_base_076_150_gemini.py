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

def f27_housing_risk_rev_momentum_z_504d_v076_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_z_756d_v077_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_z_756d_v078_signal(inventory):
    res = _z(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_z_756d_v079_signal(receivables):
    res = _z(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_z_756d_v080_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_z_1008d_v081_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_z_1008d_v082_signal(inventory):
    res = _z(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_z_1008d_v083_signal(receivables):
    res = _z(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_z_1008d_v084_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_z_1260d_v085_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_z_1260d_v086_signal(inventory):
    res = _z(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_z_1260d_v087_signal(receivables):
    res = _z(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_z_1260d_v088_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_5d_v089_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_5d_v090_signal(inventory):
    res = _drawdown(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_5d_v091_signal(receivables):
    res = _drawdown(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_5d_v092_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_10d_v093_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_10d_v094_signal(inventory):
    res = _drawdown(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_10d_v095_signal(receivables):
    res = _drawdown(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_10d_v096_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_21d_v097_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_21d_v098_signal(inventory):
    res = _drawdown(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_21d_v099_signal(receivables):
    res = _drawdown(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_21d_v100_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_42d_v101_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_42d_v102_signal(inventory):
    res = _drawdown(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_42d_v103_signal(receivables):
    res = _drawdown(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_42d_v104_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_63d_v105_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_63d_v106_signal(inventory):
    res = _drawdown(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_63d_v107_signal(receivables):
    res = _drawdown(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_63d_v108_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_126d_v109_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_126d_v110_signal(inventory):
    res = _drawdown(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_126d_v111_signal(receivables):
    res = _drawdown(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_126d_v112_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_252d_v113_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_252d_v114_signal(inventory):
    res = _drawdown(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_252d_v115_signal(receivables):
    res = _drawdown(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_252d_v116_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_504d_v117_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_504d_v118_signal(inventory):
    res = _drawdown(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_504d_v119_signal(receivables):
    res = _drawdown(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_504d_v120_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_756d_v121_signal(revenue):
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_756d_v122_signal(inventory):
    res = _drawdown(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_756d_v123_signal(receivables):
    res = _drawdown(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_756d_v124_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_1008d_v125_signal(revenue):
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_1008d_v126_signal(inventory):
    res = _drawdown(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_1008d_v127_signal(receivables):
    res = _drawdown(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_1008d_v128_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_dd_1260d_v129_signal(revenue):
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_dd_1260d_v130_signal(inventory):
    res = _drawdown(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_dd_1260d_v131_signal(receivables):
    res = _drawdown(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_dd_1260d_v132_signal(revenue):
    res = _drawdown(_slope_pct(revenue, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_rec_5d_v133_signal(revenue):
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_rec_5d_v134_signal(inventory):
    res = _recovery(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_rec_5d_v135_signal(receivables):
    res = _recovery(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_rec_5d_v136_signal(revenue):
    res = _recovery(_slope_pct(revenue, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_rec_10d_v137_signal(revenue):
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_rec_10d_v138_signal(inventory):
    res = _recovery(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_rec_10d_v139_signal(receivables):
    res = _recovery(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_rec_10d_v140_signal(revenue):
    res = _recovery(_slope_pct(revenue, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_rec_21d_v141_signal(revenue):
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_rec_21d_v142_signal(inventory):
    res = _recovery(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_rec_21d_v143_signal(receivables):
    res = _recovery(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_rec_21d_v144_signal(revenue):
    res = _recovery(_slope_pct(revenue, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_rec_42d_v145_signal(revenue):
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_rec_42d_v146_signal(inventory):
    res = _recovery(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_receivables_rec_42d_v147_signal(receivables):
    res = _recovery(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_rev_momentum_rec_42d_v148_signal(revenue):
    res = _recovery(_slope_pct(revenue, 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_revenue_rec_63d_v149_signal(revenue):
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f27_housing_risk_inventory_rec_63d_v150_signal(inventory):
    res = _recovery(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 27...")
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
