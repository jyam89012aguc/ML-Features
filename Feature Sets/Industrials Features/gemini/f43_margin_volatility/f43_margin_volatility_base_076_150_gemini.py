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

def f43_margin_volatility_margin_vol_z_504d_v076_signal(grossmargin):
    res = _z(_std(grossmargin, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_z_756d_v077_signal(grossmargin):
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_z_756d_v078_signal(cor):
    res = _z(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_z_756d_v079_signal(revenue):
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_z_756d_v080_signal(grossmargin):
    res = _z(_std(grossmargin, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_z_1008d_v081_signal(grossmargin):
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_z_1008d_v082_signal(cor):
    res = _z(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_z_1008d_v083_signal(revenue):
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_z_1008d_v084_signal(grossmargin):
    res = _z(_std(grossmargin, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_z_1260d_v085_signal(grossmargin):
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_z_1260d_v086_signal(cor):
    res = _z(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_z_1260d_v087_signal(revenue):
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_z_1260d_v088_signal(grossmargin):
    res = _z(_std(grossmargin, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_5d_v089_signal(grossmargin):
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_5d_v090_signal(cor):
    res = _drawdown(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_5d_v091_signal(revenue):
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_5d_v092_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_10d_v093_signal(grossmargin):
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_10d_v094_signal(cor):
    res = _drawdown(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_10d_v095_signal(revenue):
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_10d_v096_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_21d_v097_signal(grossmargin):
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_21d_v098_signal(cor):
    res = _drawdown(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_21d_v099_signal(revenue):
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_21d_v100_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_42d_v101_signal(grossmargin):
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_42d_v102_signal(cor):
    res = _drawdown(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_42d_v103_signal(revenue):
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_42d_v104_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_63d_v105_signal(grossmargin):
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_63d_v106_signal(cor):
    res = _drawdown(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_63d_v107_signal(revenue):
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_63d_v108_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_126d_v109_signal(grossmargin):
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_126d_v110_signal(cor):
    res = _drawdown(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_126d_v111_signal(revenue):
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_126d_v112_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_252d_v113_signal(grossmargin):
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_252d_v114_signal(cor):
    res = _drawdown(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_252d_v115_signal(revenue):
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_252d_v116_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_504d_v117_signal(grossmargin):
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_504d_v118_signal(cor):
    res = _drawdown(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_504d_v119_signal(revenue):
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_504d_v120_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_756d_v121_signal(grossmargin):
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_756d_v122_signal(cor):
    res = _drawdown(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_756d_v123_signal(revenue):
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_756d_v124_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_1008d_v125_signal(grossmargin):
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_1008d_v126_signal(cor):
    res = _drawdown(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_1008d_v127_signal(revenue):
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_1008d_v128_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_dd_1260d_v129_signal(grossmargin):
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_dd_1260d_v130_signal(cor):
    res = _drawdown(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_dd_1260d_v131_signal(revenue):
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_dd_1260d_v132_signal(grossmargin):
    res = _drawdown(_std(grossmargin, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_rec_5d_v133_signal(grossmargin):
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_rec_5d_v134_signal(cor):
    res = _recovery(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_rec_5d_v135_signal(revenue):
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_rec_5d_v136_signal(grossmargin):
    res = _recovery(_std(grossmargin, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_rec_10d_v137_signal(grossmargin):
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_rec_10d_v138_signal(cor):
    res = _recovery(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_rec_10d_v139_signal(revenue):
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_rec_10d_v140_signal(grossmargin):
    res = _recovery(_std(grossmargin, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_rec_21d_v141_signal(grossmargin):
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_rec_21d_v142_signal(cor):
    res = _recovery(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_rec_21d_v143_signal(revenue):
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_rec_21d_v144_signal(grossmargin):
    res = _recovery(_std(grossmargin, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_rec_42d_v145_signal(grossmargin):
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_rec_42d_v146_signal(cor):
    res = _recovery(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_rec_42d_v147_signal(revenue):
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_rec_42d_v148_signal(grossmargin):
    res = _recovery(_std(grossmargin, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_rec_63d_v149_signal(grossmargin):
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_rec_63d_v150_signal(cor):
    res = _recovery(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 43...")
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
