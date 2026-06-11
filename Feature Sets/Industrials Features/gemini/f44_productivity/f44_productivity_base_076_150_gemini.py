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

def f44_productivity_ebit_per_sgna_z_504d_v076_signal(ebit, sgna):
    res = _z(_ratio(ebit, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_z_756d_v077_signal(ebit):
    res = _z(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_z_756d_v078_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_z_756d_v079_signal(sgna):
    res = _z(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_z_756d_v080_signal(ebit, sgna):
    res = _z(_ratio(ebit, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_z_1008d_v081_signal(ebit):
    res = _z(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_z_1008d_v082_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_z_1008d_v083_signal(sgna):
    res = _z(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_z_1008d_v084_signal(ebit, sgna):
    res = _z(_ratio(ebit, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_z_1260d_v085_signal(ebit):
    res = _z(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_z_1260d_v086_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_z_1260d_v087_signal(sgna):
    res = _z(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_z_1260d_v088_signal(ebit, sgna):
    res = _z(_ratio(ebit, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_5d_v089_signal(ebit):
    res = _drawdown(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_5d_v090_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_5d_v091_signal(sgna):
    res = _drawdown(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_5d_v092_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_10d_v093_signal(ebit):
    res = _drawdown(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_10d_v094_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_10d_v095_signal(sgna):
    res = _drawdown(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_10d_v096_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_21d_v097_signal(ebit):
    res = _drawdown(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_21d_v098_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_21d_v099_signal(sgna):
    res = _drawdown(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_21d_v100_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_42d_v101_signal(ebit):
    res = _drawdown(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_42d_v102_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_42d_v103_signal(sgna):
    res = _drawdown(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_42d_v104_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_63d_v105_signal(ebit):
    res = _drawdown(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_63d_v106_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_63d_v107_signal(sgna):
    res = _drawdown(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_63d_v108_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_126d_v109_signal(ebit):
    res = _drawdown(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_126d_v110_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_126d_v111_signal(sgna):
    res = _drawdown(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_126d_v112_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_252d_v113_signal(ebit):
    res = _drawdown(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_252d_v114_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_252d_v115_signal(sgna):
    res = _drawdown(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_252d_v116_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_504d_v117_signal(ebit):
    res = _drawdown(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_504d_v118_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_504d_v119_signal(sgna):
    res = _drawdown(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_504d_v120_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_756d_v121_signal(ebit):
    res = _drawdown(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_756d_v122_signal(revenue):
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_756d_v123_signal(sgna):
    res = _drawdown(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_756d_v124_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_1008d_v125_signal(ebit):
    res = _drawdown(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_1008d_v126_signal(revenue):
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_1008d_v127_signal(sgna):
    res = _drawdown(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_1008d_v128_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_dd_1260d_v129_signal(ebit):
    res = _drawdown(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_dd_1260d_v130_signal(revenue):
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_dd_1260d_v131_signal(sgna):
    res = _drawdown(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_dd_1260d_v132_signal(ebit, sgna):
    res = _drawdown(_ratio(ebit, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_rec_5d_v133_signal(ebit):
    res = _recovery(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_rec_5d_v134_signal(revenue):
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_rec_5d_v135_signal(sgna):
    res = _recovery(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_rec_5d_v136_signal(ebit, sgna):
    res = _recovery(_ratio(ebit, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_rec_10d_v137_signal(ebit):
    res = _recovery(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_rec_10d_v138_signal(revenue):
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_rec_10d_v139_signal(sgna):
    res = _recovery(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_rec_10d_v140_signal(ebit, sgna):
    res = _recovery(_ratio(ebit, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_rec_21d_v141_signal(ebit):
    res = _recovery(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_rec_21d_v142_signal(revenue):
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_rec_21d_v143_signal(sgna):
    res = _recovery(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_rec_21d_v144_signal(ebit, sgna):
    res = _recovery(_ratio(ebit, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_rec_42d_v145_signal(ebit):
    res = _recovery(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_rec_42d_v146_signal(revenue):
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_sgna_rec_42d_v147_signal(sgna):
    res = _recovery(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_per_sgna_rec_42d_v148_signal(ebit, sgna):
    res = _recovery(_ratio(ebit, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_ebit_rec_63d_v149_signal(ebit):
    res = _recovery(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f44_productivity_revenue_rec_63d_v150_signal(revenue):
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 44...")
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
