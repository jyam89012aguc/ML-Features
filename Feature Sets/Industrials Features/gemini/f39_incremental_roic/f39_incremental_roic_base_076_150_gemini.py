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

def f39_incremental_roic_ebit_to_invcap_z_504d_v076_signal(ebit, invcap):
    res = _z(_ratio(ebit, invcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_z_756d_v077_signal(roic):
    res = _z(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_z_756d_v078_signal(ebit):
    res = _z(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_z_756d_v079_signal(invcap):
    res = _z(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_z_756d_v080_signal(ebit, invcap):
    res = _z(_ratio(ebit, invcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_z_1008d_v081_signal(roic):
    res = _z(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_z_1008d_v082_signal(ebit):
    res = _z(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_z_1008d_v083_signal(invcap):
    res = _z(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_z_1008d_v084_signal(ebit, invcap):
    res = _z(_ratio(ebit, invcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_z_1260d_v085_signal(roic):
    res = _z(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_z_1260d_v086_signal(ebit):
    res = _z(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_z_1260d_v087_signal(invcap):
    res = _z(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_z_1260d_v088_signal(ebit, invcap):
    res = _z(_ratio(ebit, invcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_5d_v089_signal(roic):
    res = _drawdown(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_5d_v090_signal(ebit):
    res = _drawdown(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_5d_v091_signal(invcap):
    res = _drawdown(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_5d_v092_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_10d_v093_signal(roic):
    res = _drawdown(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_10d_v094_signal(ebit):
    res = _drawdown(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_10d_v095_signal(invcap):
    res = _drawdown(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_10d_v096_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_21d_v097_signal(roic):
    res = _drawdown(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_21d_v098_signal(ebit):
    res = _drawdown(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_21d_v099_signal(invcap):
    res = _drawdown(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_21d_v100_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_42d_v101_signal(roic):
    res = _drawdown(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_42d_v102_signal(ebit):
    res = _drawdown(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_42d_v103_signal(invcap):
    res = _drawdown(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_42d_v104_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_63d_v105_signal(roic):
    res = _drawdown(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_63d_v106_signal(ebit):
    res = _drawdown(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_63d_v107_signal(invcap):
    res = _drawdown(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_63d_v108_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_126d_v109_signal(roic):
    res = _drawdown(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_126d_v110_signal(ebit):
    res = _drawdown(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_126d_v111_signal(invcap):
    res = _drawdown(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_126d_v112_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_252d_v113_signal(roic):
    res = _drawdown(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_252d_v114_signal(ebit):
    res = _drawdown(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_252d_v115_signal(invcap):
    res = _drawdown(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_252d_v116_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_504d_v117_signal(roic):
    res = _drawdown(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_504d_v118_signal(ebit):
    res = _drawdown(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_504d_v119_signal(invcap):
    res = _drawdown(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_504d_v120_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_756d_v121_signal(roic):
    res = _drawdown(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_756d_v122_signal(ebit):
    res = _drawdown(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_756d_v123_signal(invcap):
    res = _drawdown(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_756d_v124_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_1008d_v125_signal(roic):
    res = _drawdown(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_1008d_v126_signal(ebit):
    res = _drawdown(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_1008d_v127_signal(invcap):
    res = _drawdown(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_1008d_v128_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_dd_1260d_v129_signal(roic):
    res = _drawdown(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_dd_1260d_v130_signal(ebit):
    res = _drawdown(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_dd_1260d_v131_signal(invcap):
    res = _drawdown(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_dd_1260d_v132_signal(ebit, invcap):
    res = _drawdown(_ratio(ebit, invcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_rec_5d_v133_signal(roic):
    res = _recovery(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_rec_5d_v134_signal(ebit):
    res = _recovery(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_rec_5d_v135_signal(invcap):
    res = _recovery(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_rec_5d_v136_signal(ebit, invcap):
    res = _recovery(_ratio(ebit, invcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_rec_10d_v137_signal(roic):
    res = _recovery(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_rec_10d_v138_signal(ebit):
    res = _recovery(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_rec_10d_v139_signal(invcap):
    res = _recovery(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_rec_10d_v140_signal(ebit, invcap):
    res = _recovery(_ratio(ebit, invcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_rec_21d_v141_signal(roic):
    res = _recovery(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_rec_21d_v142_signal(ebit):
    res = _recovery(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_rec_21d_v143_signal(invcap):
    res = _recovery(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_rec_21d_v144_signal(ebit, invcap):
    res = _recovery(_ratio(ebit, invcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_rec_42d_v145_signal(roic):
    res = _recovery(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_rec_42d_v146_signal(ebit):
    res = _recovery(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_rec_42d_v147_signal(invcap):
    res = _recovery(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_rec_42d_v148_signal(ebit, invcap):
    res = _recovery(_ratio(ebit, invcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_rec_63d_v149_signal(roic):
    res = _recovery(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_rec_63d_v150_signal(ebit):
    res = _recovery(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 39...")
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
