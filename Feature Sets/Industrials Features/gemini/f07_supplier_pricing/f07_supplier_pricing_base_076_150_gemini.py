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

def f07_supplier_pricing_grossmargin_z_63d_v076_signal(grossmargin):
    res = _z(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_63d_v077_signal(cor):
    res = _z(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_63d_v078_signal(gp):
    res = _z(gp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_63d_v079_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_63d_v080_signal(gp, cor):
    res = _z(_ratio(gp, cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_126d_v081_signal(grossmargin):
    res = _z(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_126d_v082_signal(cor):
    res = _z(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_126d_v083_signal(gp):
    res = _z(gp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_126d_v084_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_126d_v085_signal(gp, cor):
    res = _z(_ratio(gp, cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_252d_v086_signal(grossmargin):
    res = _z(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_252d_v087_signal(cor):
    res = _z(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_252d_v088_signal(gp):
    res = _z(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_252d_v089_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_252d_v090_signal(gp, cor):
    res = _z(_ratio(gp, cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_504d_v091_signal(grossmargin):
    res = _z(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_504d_v092_signal(cor):
    res = _z(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_504d_v093_signal(gp):
    res = _z(gp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_504d_v094_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_504d_v095_signal(gp, cor):
    res = _z(_ratio(gp, cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_756d_v096_signal(grossmargin):
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_756d_v097_signal(cor):
    res = _z(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_756d_v098_signal(gp):
    res = _z(gp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_756d_v099_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_756d_v100_signal(gp, cor):
    res = _z(_ratio(gp, cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_1008d_v101_signal(grossmargin):
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_1008d_v102_signal(cor):
    res = _z(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_1008d_v103_signal(gp):
    res = _z(gp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_1008d_v104_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_1008d_v105_signal(gp, cor):
    res = _z(_ratio(gp, cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_z_1260d_v106_signal(grossmargin):
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_z_1260d_v107_signal(cor):
    res = _z(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_z_1260d_v108_signal(gp):
    res = _z(gp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_z_1260d_v109_signal(cor, gp):
    res = _z(_ratio(cor, gp + cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_z_1260d_v110_signal(gp, cor):
    res = _z(_ratio(gp, cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_5d_v111_signal(grossmargin):
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_5d_v112_signal(cor):
    res = _drawdown(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_5d_v113_signal(gp):
    res = _drawdown(gp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_5d_v114_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_5d_v115_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_10d_v116_signal(grossmargin):
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_10d_v117_signal(cor):
    res = _drawdown(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_10d_v118_signal(gp):
    res = _drawdown(gp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_10d_v119_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_10d_v120_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_21d_v121_signal(grossmargin):
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_21d_v122_signal(cor):
    res = _drawdown(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_21d_v123_signal(gp):
    res = _drawdown(gp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_21d_v124_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_21d_v125_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_42d_v126_signal(grossmargin):
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_42d_v127_signal(cor):
    res = _drawdown(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_42d_v128_signal(gp):
    res = _drawdown(gp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_42d_v129_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_42d_v130_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_63d_v131_signal(grossmargin):
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_63d_v132_signal(cor):
    res = _drawdown(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_63d_v133_signal(gp):
    res = _drawdown(gp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_63d_v134_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_63d_v135_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_126d_v136_signal(grossmargin):
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_126d_v137_signal(cor):
    res = _drawdown(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_126d_v138_signal(gp):
    res = _drawdown(gp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_126d_v139_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_126d_v140_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_252d_v141_signal(grossmargin):
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_252d_v142_signal(cor):
    res = _drawdown(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_252d_v143_signal(gp):
    res = _drawdown(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_252d_v144_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_252d_v145_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_dd_504d_v146_signal(grossmargin):
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_dd_504d_v147_signal(cor):
    res = _drawdown(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_dd_504d_v148_signal(gp):
    res = _drawdown(gp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_dd_504d_v149_signal(cor, gp):
    res = _drawdown(_ratio(cor, gp + cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_dd_504d_v150_signal(gp, cor):
    res = _drawdown(_ratio(gp, cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "gp": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 07...")
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
