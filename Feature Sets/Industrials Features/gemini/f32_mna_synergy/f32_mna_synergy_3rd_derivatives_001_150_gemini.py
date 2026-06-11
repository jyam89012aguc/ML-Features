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

def f32_mna_synergy_netinc_mom_z_63d_v151_signal(netinc):
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_63d_v152_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_mom_z_126d_v153_signal(sgna):
    res = _z(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_mom_z_126d_v154_signal(ebitda):
    res = _z(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_mom_z_126d_v155_signal(netinc):
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_126d_v156_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_mom_z_252d_v157_signal(sgna):
    res = _z(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_mom_z_252d_v158_signal(ebitda):
    res = _z(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_mom_z_252d_v159_signal(netinc):
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_252d_v160_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_mom_z_504d_v161_signal(sgna):
    res = _z(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_mom_z_504d_v162_signal(ebitda):
    res = _z(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_mom_z_504d_v163_signal(netinc):
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_504d_v164_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_mom_z_756d_v165_signal(sgna):
    res = _z(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_mom_z_756d_v166_signal(ebitda):
    res = _z(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_mom_z_756d_v167_signal(netinc):
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_756d_v168_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_mom_z_1008d_v169_signal(sgna):
    res = _z(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_mom_z_1008d_v170_signal(ebitda):
    res = _z(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_mom_z_1008d_v171_signal(netinc):
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_1008d_v172_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_mom_z_1260d_v173_signal(sgna):
    res = _z(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_mom_z_1260d_v174_signal(ebitda):
    res = _z(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_mom_z_1260d_v175_signal(netinc):
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_mom_z_1260d_v176_signal(sgna):
    res = _z(_slope_pct(_slope_pct(sgna, 252), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_5d_v177_signal(sgna):
    res = _std(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_5d_v178_signal(ebitda):
    res = _std(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_5d_v179_signal(netinc):
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_5d_v180_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_10d_v181_signal(sgna):
    res = _std(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_10d_v182_signal(ebitda):
    res = _std(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_10d_v183_signal(netinc):
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_10d_v184_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_21d_v185_signal(sgna):
    res = _std(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_21d_v186_signal(ebitda):
    res = _std(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_21d_v187_signal(netinc):
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_21d_v188_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_42d_v189_signal(sgna):
    res = _std(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_42d_v190_signal(ebitda):
    res = _std(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_42d_v191_signal(netinc):
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_42d_v192_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_63d_v193_signal(sgna):
    res = _std(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_63d_v194_signal(ebitda):
    res = _std(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_63d_v195_signal(netinc):
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_63d_v196_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_126d_v197_signal(sgna):
    res = _std(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_126d_v198_signal(ebitda):
    res = _std(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_126d_v199_signal(netinc):
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_126d_v200_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_252d_v201_signal(sgna):
    res = _std(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_252d_v202_signal(ebitda):
    res = _std(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_252d_v203_signal(netinc):
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_252d_v204_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_504d_v205_signal(sgna):
    res = _std(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_504d_v206_signal(ebitda):
    res = _std(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_504d_v207_signal(netinc):
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_504d_v208_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_756d_v209_signal(sgna):
    res = _std(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_756d_v210_signal(ebitda):
    res = _std(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_756d_v211_signal(netinc):
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_756d_v212_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_1008d_v213_signal(sgna):
    res = _std(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_1008d_v214_signal(ebitda):
    res = _std(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_1008d_v215_signal(netinc):
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_1008d_v216_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_vol_slope_1260d_v217_signal(sgna):
    res = _std(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_ebitda_vol_slope_1260d_v218_signal(ebitda):
    res = _std(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_netinc_vol_slope_1260d_v219_signal(netinc):
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f32_mna_synergy_sgna_reduction_vol_slope_1260d_v220_signal(sgna):
    res = _std(_slope_pct(_slope_pct(sgna, 252), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 32...")
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
