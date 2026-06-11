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

def f43_margin_volatility_revenue_mom_z_63d_v151_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_63d_v152_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_126d_v153_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_126d_v154_signal(cor):
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_126d_v155_signal(revenue):
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_126d_v156_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_252d_v157_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_252d_v158_signal(cor):
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_252d_v159_signal(revenue):
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_252d_v160_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_504d_v161_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_504d_v162_signal(cor):
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_504d_v163_signal(revenue):
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_504d_v164_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_756d_v165_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_756d_v166_signal(cor):
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_756d_v167_signal(revenue):
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_756d_v168_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_1008d_v169_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_1008d_v170_signal(cor):
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_1008d_v171_signal(revenue):
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_1008d_v172_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_1260d_v173_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_1260d_v174_signal(cor):
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_1260d_v175_signal(revenue):
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_1260d_v176_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_5d_v177_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_5d_v178_signal(cor):
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_5d_v179_signal(revenue):
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_5d_v180_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_10d_v181_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_10d_v182_signal(cor):
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_10d_v183_signal(revenue):
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_10d_v184_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_21d_v185_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_21d_v186_signal(cor):
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_21d_v187_signal(revenue):
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_21d_v188_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_42d_v189_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_42d_v190_signal(cor):
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_42d_v191_signal(revenue):
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_42d_v192_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_63d_v193_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_63d_v194_signal(cor):
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_63d_v195_signal(revenue):
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_63d_v196_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_126d_v197_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_126d_v198_signal(cor):
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_126d_v199_signal(revenue):
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_126d_v200_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_252d_v201_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_252d_v202_signal(cor):
    res = _std(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_252d_v203_signal(revenue):
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_252d_v204_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_504d_v205_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_504d_v206_signal(cor):
    res = _std(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_504d_v207_signal(revenue):
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_504d_v208_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_756d_v209_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_756d_v210_signal(cor):
    res = _std(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_756d_v211_signal(revenue):
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_756d_v212_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_1008d_v213_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_1008d_v214_signal(cor):
    res = _std(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_1008d_v215_signal(revenue):
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_1008d_v216_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_vol_slope_1260d_v217_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_vol_slope_1260d_v218_signal(cor):
    res = _std(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_vol_slope_1260d_v219_signal(revenue):
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_vol_slope_1260d_v220_signal(grossmargin):
    res = _std(_slope_pct(_std(grossmargin, 252), 1260), 1260)
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
