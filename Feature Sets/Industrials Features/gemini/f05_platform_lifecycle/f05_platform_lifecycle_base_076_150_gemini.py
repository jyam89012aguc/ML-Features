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

def f05_platform_lifecycle_operating_leverage_z_504d_v076_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_756d_v077_signal(ebitdamargin):
    res = _z(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_756d_v078_signal(ebitda):
    res = _z(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_756d_v079_signal(ebit):
    res = _z(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_756d_v080_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_1008d_v081_signal(ebitdamargin):
    res = _z(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_1008d_v082_signal(ebitda):
    res = _z(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_1008d_v083_signal(ebit):
    res = _z(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_1008d_v084_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_z_1260d_v085_signal(ebitdamargin):
    res = _z(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_z_1260d_v086_signal(ebitda):
    res = _z(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_z_1260d_v087_signal(ebit):
    res = _z(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_z_1260d_v088_signal(ebit, ebitda):
    res = _z(_ratio(ebit, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_5d_v089_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_5d_v090_signal(ebitda):
    res = _drawdown(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_5d_v091_signal(ebit):
    res = _drawdown(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_5d_v092_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_10d_v093_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_10d_v094_signal(ebitda):
    res = _drawdown(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_10d_v095_signal(ebit):
    res = _drawdown(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_10d_v096_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_21d_v097_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_21d_v098_signal(ebitda):
    res = _drawdown(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_21d_v099_signal(ebit):
    res = _drawdown(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_21d_v100_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_42d_v101_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_42d_v102_signal(ebitda):
    res = _drawdown(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_42d_v103_signal(ebit):
    res = _drawdown(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_42d_v104_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_63d_v105_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_63d_v106_signal(ebitda):
    res = _drawdown(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_63d_v107_signal(ebit):
    res = _drawdown(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_63d_v108_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_126d_v109_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_126d_v110_signal(ebitda):
    res = _drawdown(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_126d_v111_signal(ebit):
    res = _drawdown(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_126d_v112_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_252d_v113_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_252d_v114_signal(ebitda):
    res = _drawdown(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_252d_v115_signal(ebit):
    res = _drawdown(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_252d_v116_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_504d_v117_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_504d_v118_signal(ebitda):
    res = _drawdown(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_504d_v119_signal(ebit):
    res = _drawdown(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_504d_v120_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_756d_v121_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_756d_v122_signal(ebitda):
    res = _drawdown(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_756d_v123_signal(ebit):
    res = _drawdown(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_756d_v124_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_1008d_v125_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_1008d_v126_signal(ebitda):
    res = _drawdown(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_1008d_v127_signal(ebit):
    res = _drawdown(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_1008d_v128_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_dd_1260d_v129_signal(ebitdamargin):
    res = _drawdown(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_dd_1260d_v130_signal(ebitda):
    res = _drawdown(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_dd_1260d_v131_signal(ebit):
    res = _drawdown(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_dd_1260d_v132_signal(ebit, ebitda):
    res = _drawdown(_ratio(ebit, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_rec_5d_v133_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_rec_5d_v134_signal(ebitda):
    res = _recovery(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_rec_5d_v135_signal(ebit):
    res = _recovery(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_rec_5d_v136_signal(ebit, ebitda):
    res = _recovery(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_rec_10d_v137_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_rec_10d_v138_signal(ebitda):
    res = _recovery(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_rec_10d_v139_signal(ebit):
    res = _recovery(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_rec_10d_v140_signal(ebit, ebitda):
    res = _recovery(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_rec_21d_v141_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_rec_21d_v142_signal(ebitda):
    res = _recovery(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_rec_21d_v143_signal(ebit):
    res = _recovery(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_rec_21d_v144_signal(ebit, ebitda):
    res = _recovery(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_rec_42d_v145_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_rec_42d_v146_signal(ebitda):
    res = _recovery(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_rec_42d_v147_signal(ebit):
    res = _recovery(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_rec_42d_v148_signal(ebit, ebitda):
    res = _recovery(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_rec_63d_v149_signal(ebitdamargin):
    res = _recovery(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_rec_63d_v150_signal(ebitda):
    res = _recovery(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 05...")
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
