import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
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

def f08_same_store_proxy_deferredrev_mom_z_63d_v151_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 63d window."""
    res = _z(_slope_pct(deferredrev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_63d_v152_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_mom_z_126d_v153_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_mom_z_126d_v154_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 126d window."""
    res = _z(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_mom_z_126d_v155_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 126d window."""
    res = _z(_slope_pct(deferredrev, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_126d_v156_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_mom_z_252d_v157_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_mom_z_252d_v158_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 252d window."""
    res = _z(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_mom_z_252d_v159_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 252d window."""
    res = _z(_slope_pct(deferredrev, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_252d_v160_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_mom_z_504d_v161_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_mom_z_504d_v162_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 504d window."""
    res = _z(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_mom_z_504d_v163_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 504d window."""
    res = _z(_slope_pct(deferredrev, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_504d_v164_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_mom_z_756d_v165_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_mom_z_756d_v166_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 756d window."""
    res = _z(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_mom_z_756d_v167_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 756d window."""
    res = _z(_slope_pct(deferredrev, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_756d_v168_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_mom_z_1008d_v169_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_mom_z_1008d_v170_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 1008d window."""
    res = _z(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_mom_z_1008d_v171_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 1008d window."""
    res = _z(_slope_pct(deferredrev, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_1008d_v172_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_mom_z_1260d_v173_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_mom_z_1260d_v174_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 1260d window."""
    res = _z(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_mom_z_1260d_v175_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 1260d window."""
    res = _z(_slope_pct(deferredrev, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_mom_z_1260d_v176_signal(revenue, receivables, deferredrev):
    """Relative momentum strength for Cash-realized organic growth proxy over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, receivables + deferredrev), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_5d_v177_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_5d_v178_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 5d window."""
    res = _std(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_5d_v179_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 5d window."""
    res = _std(_slope_pct(deferredrev, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_5d_v180_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_10d_v181_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_10d_v182_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 10d window."""
    res = _std(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_10d_v183_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 10d window."""
    res = _std(_slope_pct(deferredrev, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_10d_v184_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_21d_v185_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_21d_v186_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 21d window."""
    res = _std(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_21d_v187_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 21d window."""
    res = _std(_slope_pct(deferredrev, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_21d_v188_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_42d_v189_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_42d_v190_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 42d window."""
    res = _std(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_42d_v191_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 42d window."""
    res = _std(_slope_pct(deferredrev, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_42d_v192_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_63d_v193_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_63d_v194_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 63d window."""
    res = _std(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_63d_v195_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 63d window."""
    res = _std(_slope_pct(deferredrev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_63d_v196_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_126d_v197_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_126d_v198_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 126d window."""
    res = _std(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_126d_v199_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 126d window."""
    res = _std(_slope_pct(deferredrev, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_126d_v200_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_252d_v201_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_252d_v202_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 252d window."""
    res = _std(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_252d_v203_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 252d window."""
    res = _std(_slope_pct(deferredrev, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_252d_v204_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_504d_v205_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_504d_v206_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 504d window."""
    res = _std(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_504d_v207_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 504d window."""
    res = _std(_slope_pct(deferredrev, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_504d_v208_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_756d_v209_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_756d_v210_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 756d window."""
    res = _std(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_756d_v211_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 756d window."""
    res = _std(_slope_pct(deferredrev, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_756d_v212_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_1008d_v213_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_1008d_v214_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 1008d window."""
    res = _std(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_1008d_v215_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 1008d window."""
    res = _std(_slope_pct(deferredrev, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_1008d_v216_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_vol_slope_1260d_v217_signal(revenue):
    """Volatility of the momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_vol_slope_1260d_v218_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 1260d window."""
    res = _std(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_vol_slope_1260d_v219_signal(deferredrev):
    """Volatility of the momentum for Raw level of deferredrev over 1260d window."""
    res = _std(_slope_pct(deferredrev, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_vol_slope_1260d_v220_signal(revenue, receivables, deferredrev):
    """Volatility of the momentum for Cash-realized organic growth proxy over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, receivables + deferredrev), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f08_same_store_proxy_deferredrev_mom_z_63d_v151_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_63d_v151_signal},    "f08_same_store_proxy_organic_momentum_mom_z_63d_v152_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_63d_v152_signal},    "f08_same_store_proxy_revenue_mom_z_126d_v153_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_mom_z_126d_v153_signal},    "f08_same_store_proxy_receivables_mom_z_126d_v154_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_mom_z_126d_v154_signal},    "f08_same_store_proxy_deferredrev_mom_z_126d_v155_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_126d_v155_signal},    "f08_same_store_proxy_organic_momentum_mom_z_126d_v156_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_126d_v156_signal},    "f08_same_store_proxy_revenue_mom_z_252d_v157_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_mom_z_252d_v157_signal},    "f08_same_store_proxy_receivables_mom_z_252d_v158_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_mom_z_252d_v158_signal},    "f08_same_store_proxy_deferredrev_mom_z_252d_v159_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_252d_v159_signal},    "f08_same_store_proxy_organic_momentum_mom_z_252d_v160_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_252d_v160_signal},    "f08_same_store_proxy_revenue_mom_z_504d_v161_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_mom_z_504d_v161_signal},    "f08_same_store_proxy_receivables_mom_z_504d_v162_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_mom_z_504d_v162_signal},    "f08_same_store_proxy_deferredrev_mom_z_504d_v163_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_504d_v163_signal},    "f08_same_store_proxy_organic_momentum_mom_z_504d_v164_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_504d_v164_signal},    "f08_same_store_proxy_revenue_mom_z_756d_v165_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_mom_z_756d_v165_signal},    "f08_same_store_proxy_receivables_mom_z_756d_v166_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_mom_z_756d_v166_signal},    "f08_same_store_proxy_deferredrev_mom_z_756d_v167_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_756d_v167_signal},    "f08_same_store_proxy_organic_momentum_mom_z_756d_v168_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_756d_v168_signal},    "f08_same_store_proxy_revenue_mom_z_1008d_v169_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_mom_z_1008d_v169_signal},    "f08_same_store_proxy_receivables_mom_z_1008d_v170_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_mom_z_1008d_v170_signal},    "f08_same_store_proxy_deferredrev_mom_z_1008d_v171_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_1008d_v171_signal},    "f08_same_store_proxy_organic_momentum_mom_z_1008d_v172_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_1008d_v172_signal},    "f08_same_store_proxy_revenue_mom_z_1260d_v173_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_mom_z_1260d_v173_signal},    "f08_same_store_proxy_receivables_mom_z_1260d_v174_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_mom_z_1260d_v174_signal},    "f08_same_store_proxy_deferredrev_mom_z_1260d_v175_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_mom_z_1260d_v175_signal},    "f08_same_store_proxy_organic_momentum_mom_z_1260d_v176_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_mom_z_1260d_v176_signal},    "f08_same_store_proxy_revenue_vol_slope_5d_v177_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_5d_v177_signal},    "f08_same_store_proxy_receivables_vol_slope_5d_v178_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_5d_v178_signal},    "f08_same_store_proxy_deferredrev_vol_slope_5d_v179_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_5d_v179_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_5d_v180_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_5d_v180_signal},    "f08_same_store_proxy_revenue_vol_slope_10d_v181_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_10d_v181_signal},    "f08_same_store_proxy_receivables_vol_slope_10d_v182_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_10d_v182_signal},    "f08_same_store_proxy_deferredrev_vol_slope_10d_v183_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_10d_v183_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_10d_v184_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_10d_v184_signal},    "f08_same_store_proxy_revenue_vol_slope_21d_v185_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_21d_v185_signal},    "f08_same_store_proxy_receivables_vol_slope_21d_v186_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_21d_v186_signal},    "f08_same_store_proxy_deferredrev_vol_slope_21d_v187_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_21d_v187_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_21d_v188_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_21d_v188_signal},    "f08_same_store_proxy_revenue_vol_slope_42d_v189_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_42d_v189_signal},    "f08_same_store_proxy_receivables_vol_slope_42d_v190_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_42d_v190_signal},    "f08_same_store_proxy_deferredrev_vol_slope_42d_v191_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_42d_v191_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_42d_v192_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_42d_v192_signal},    "f08_same_store_proxy_revenue_vol_slope_63d_v193_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_63d_v193_signal},    "f08_same_store_proxy_receivables_vol_slope_63d_v194_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_63d_v194_signal},    "f08_same_store_proxy_deferredrev_vol_slope_63d_v195_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_63d_v195_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_63d_v196_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_63d_v196_signal},    "f08_same_store_proxy_revenue_vol_slope_126d_v197_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_126d_v197_signal},    "f08_same_store_proxy_receivables_vol_slope_126d_v198_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_126d_v198_signal},    "f08_same_store_proxy_deferredrev_vol_slope_126d_v199_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_126d_v199_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_126d_v200_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_126d_v200_signal},    "f08_same_store_proxy_revenue_vol_slope_252d_v201_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_252d_v201_signal},    "f08_same_store_proxy_receivables_vol_slope_252d_v202_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_252d_v202_signal},    "f08_same_store_proxy_deferredrev_vol_slope_252d_v203_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_252d_v203_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_252d_v204_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_252d_v204_signal},    "f08_same_store_proxy_revenue_vol_slope_504d_v205_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_504d_v205_signal},    "f08_same_store_proxy_receivables_vol_slope_504d_v206_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_504d_v206_signal},    "f08_same_store_proxy_deferredrev_vol_slope_504d_v207_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_504d_v207_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_504d_v208_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_504d_v208_signal},    "f08_same_store_proxy_revenue_vol_slope_756d_v209_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_756d_v209_signal},    "f08_same_store_proxy_receivables_vol_slope_756d_v210_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_756d_v210_signal},    "f08_same_store_proxy_deferredrev_vol_slope_756d_v211_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_756d_v211_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_756d_v212_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_756d_v212_signal},    "f08_same_store_proxy_revenue_vol_slope_1008d_v213_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_1008d_v213_signal},    "f08_same_store_proxy_receivables_vol_slope_1008d_v214_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_1008d_v214_signal},    "f08_same_store_proxy_deferredrev_vol_slope_1008d_v215_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_1008d_v215_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_1008d_v216_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_1008d_v216_signal},    "f08_same_store_proxy_revenue_vol_slope_1260d_v217_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_vol_slope_1260d_v217_signal},    "f08_same_store_proxy_receivables_vol_slope_1260d_v218_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_vol_slope_1260d_v218_signal},    "f08_same_store_proxy_deferredrev_vol_slope_1260d_v219_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_vol_slope_1260d_v219_signal},    "f08_same_store_proxy_organic_momentum_vol_slope_1260d_v220_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 08...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
