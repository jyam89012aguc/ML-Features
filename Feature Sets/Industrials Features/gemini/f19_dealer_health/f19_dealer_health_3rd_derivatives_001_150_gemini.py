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

def f19_dealer_health_revenue_mom_z_63d_v151_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_63d_v152_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_mom_z_126d_v153_signal(receivables):
    res = _z(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_mom_z_126d_v154_signal(inventory):
    res = _z(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_mom_z_126d_v155_signal(revenue):
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_126d_v156_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_mom_z_252d_v157_signal(receivables):
    res = _z(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_mom_z_252d_v158_signal(inventory):
    res = _z(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_mom_z_252d_v159_signal(revenue):
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_252d_v160_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_mom_z_504d_v161_signal(receivables):
    res = _z(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_mom_z_504d_v162_signal(inventory):
    res = _z(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_mom_z_504d_v163_signal(revenue):
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_504d_v164_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_mom_z_756d_v165_signal(receivables):
    res = _z(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_mom_z_756d_v166_signal(inventory):
    res = _z(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_mom_z_756d_v167_signal(revenue):
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_756d_v168_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_mom_z_1008d_v169_signal(receivables):
    res = _z(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_mom_z_1008d_v170_signal(inventory):
    res = _z(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_mom_z_1008d_v171_signal(revenue):
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_1008d_v172_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_mom_z_1260d_v173_signal(receivables):
    res = _z(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_mom_z_1260d_v174_signal(inventory):
    res = _z(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_mom_z_1260d_v175_signal(revenue):
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_mom_z_1260d_v176_signal(receivables, inventory):
    res = _z(_slope_pct(_ratio(receivables, inventory), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_5d_v177_signal(receivables):
    res = _std(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_5d_v178_signal(inventory):
    res = _std(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_5d_v179_signal(revenue):
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_5d_v180_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_10d_v181_signal(receivables):
    res = _std(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_10d_v182_signal(inventory):
    res = _std(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_10d_v183_signal(revenue):
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_10d_v184_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_21d_v185_signal(receivables):
    res = _std(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_21d_v186_signal(inventory):
    res = _std(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_21d_v187_signal(revenue):
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_21d_v188_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_42d_v189_signal(receivables):
    res = _std(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_42d_v190_signal(inventory):
    res = _std(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_42d_v191_signal(revenue):
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_42d_v192_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_63d_v193_signal(receivables):
    res = _std(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_63d_v194_signal(inventory):
    res = _std(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_63d_v195_signal(revenue):
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_63d_v196_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_126d_v197_signal(receivables):
    res = _std(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_126d_v198_signal(inventory):
    res = _std(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_126d_v199_signal(revenue):
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_126d_v200_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_252d_v201_signal(receivables):
    res = _std(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_252d_v202_signal(inventory):
    res = _std(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_252d_v203_signal(revenue):
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_252d_v204_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_504d_v205_signal(receivables):
    res = _std(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_504d_v206_signal(inventory):
    res = _std(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_504d_v207_signal(revenue):
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_504d_v208_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_756d_v209_signal(receivables):
    res = _std(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_756d_v210_signal(inventory):
    res = _std(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_756d_v211_signal(revenue):
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_756d_v212_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_1008d_v213_signal(receivables):
    res = _std(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_1008d_v214_signal(inventory):
    res = _std(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_1008d_v215_signal(revenue):
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_1008d_v216_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_receivables_vol_slope_1260d_v217_signal(receivables):
    res = _std(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_inventory_vol_slope_1260d_v218_signal(inventory):
    res = _std(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_revenue_vol_slope_1260d_v219_signal(revenue):
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_dealer_health_channel_stuffing_proxy_vol_slope_1260d_v220_signal(receivables, inventory):
    res = _std(_slope_pct(_ratio(receivables, inventory), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 19...")
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
