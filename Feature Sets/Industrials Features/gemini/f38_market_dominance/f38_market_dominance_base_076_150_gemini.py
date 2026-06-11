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

def f38_market_dominance_dominance_composite_z_504d_v076_signal(grossmargin, roic):
    res = _z(grossmargin * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_z_756d_v077_signal(grossmargin):
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_z_756d_v078_signal(ebitdamargin):
    res = _z(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_z_756d_v079_signal(roic):
    res = _z(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_z_756d_v080_signal(grossmargin, roic):
    res = _z(grossmargin * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_z_1008d_v081_signal(grossmargin):
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_z_1008d_v082_signal(ebitdamargin):
    res = _z(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_z_1008d_v083_signal(roic):
    res = _z(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_z_1008d_v084_signal(grossmargin, roic):
    res = _z(grossmargin * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_z_1260d_v085_signal(grossmargin):
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_z_1260d_v086_signal(ebitdamargin):
    res = _z(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_z_1260d_v087_signal(roic):
    res = _z(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_z_1260d_v088_signal(grossmargin, roic):
    res = _z(grossmargin * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_5d_v089_signal(grossmargin):
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_5d_v090_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_5d_v091_signal(roic):
    res = _drawdown(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_5d_v092_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_10d_v093_signal(grossmargin):
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_10d_v094_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_10d_v095_signal(roic):
    res = _drawdown(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_10d_v096_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_21d_v097_signal(grossmargin):
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_21d_v098_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_21d_v099_signal(roic):
    res = _drawdown(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_21d_v100_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_42d_v101_signal(grossmargin):
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_42d_v102_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_42d_v103_signal(roic):
    res = _drawdown(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_42d_v104_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_63d_v105_signal(grossmargin):
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_63d_v106_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_63d_v107_signal(roic):
    res = _drawdown(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_63d_v108_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_126d_v109_signal(grossmargin):
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_126d_v110_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_126d_v111_signal(roic):
    res = _drawdown(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_126d_v112_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_252d_v113_signal(grossmargin):
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_252d_v114_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_252d_v115_signal(roic):
    res = _drawdown(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_252d_v116_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_504d_v117_signal(grossmargin):
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_504d_v118_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_504d_v119_signal(roic):
    res = _drawdown(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_504d_v120_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_756d_v121_signal(grossmargin):
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_756d_v122_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_756d_v123_signal(roic):
    res = _drawdown(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_756d_v124_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_1008d_v125_signal(grossmargin):
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_1008d_v126_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_1008d_v127_signal(roic):
    res = _drawdown(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_1008d_v128_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_dd_1260d_v129_signal(grossmargin):
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_dd_1260d_v130_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_dd_1260d_v131_signal(roic):
    res = _drawdown(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_dd_1260d_v132_signal(grossmargin, roic):
    res = _drawdown(grossmargin * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_rec_5d_v133_signal(grossmargin):
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_rec_5d_v134_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_rec_5d_v135_signal(roic):
    res = _recovery(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_rec_5d_v136_signal(grossmargin, roic):
    res = _recovery(grossmargin * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_rec_10d_v137_signal(grossmargin):
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_rec_10d_v138_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_rec_10d_v139_signal(roic):
    res = _recovery(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_rec_10d_v140_signal(grossmargin, roic):
    res = _recovery(grossmargin * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_rec_21d_v141_signal(grossmargin):
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_rec_21d_v142_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_rec_21d_v143_signal(roic):
    res = _recovery(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_rec_21d_v144_signal(grossmargin, roic):
    res = _recovery(grossmargin * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_rec_42d_v145_signal(grossmargin):
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_rec_42d_v146_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_rec_42d_v147_signal(roic):
    res = _recovery(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_rec_42d_v148_signal(grossmargin, roic):
    res = _recovery(grossmargin * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_rec_63d_v149_signal(grossmargin):
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_rec_63d_v150_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 38...")
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
