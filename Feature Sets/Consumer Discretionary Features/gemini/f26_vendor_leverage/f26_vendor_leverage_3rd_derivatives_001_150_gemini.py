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

def f26_vendor_leverage_cor_mom_z_63d_v151_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_63d_v152_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 63d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_mom_z_126d_v153_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 126d window."""
    res = _z(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_mom_z_126d_v154_signal(payables):
    """Relative momentum strength for Raw level of payables over 126d window."""
    res = _z(_slope_pct(payables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_mom_z_126d_v155_signal(cor):
    """Relative momentum strength for Raw level of cor over 126d window."""
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_126d_v156_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 126d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_mom_z_252d_v157_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 252d window."""
    res = _z(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_mom_z_252d_v158_signal(payables):
    """Relative momentum strength for Raw level of payables over 252d window."""
    res = _z(_slope_pct(payables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_mom_z_252d_v159_signal(cor):
    """Relative momentum strength for Raw level of cor over 252d window."""
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_252d_v160_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 252d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_mom_z_504d_v161_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 504d window."""
    res = _z(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_mom_z_504d_v162_signal(payables):
    """Relative momentum strength for Raw level of payables over 504d window."""
    res = _z(_slope_pct(payables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_mom_z_504d_v163_signal(cor):
    """Relative momentum strength for Raw level of cor over 504d window."""
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_504d_v164_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 504d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_mom_z_756d_v165_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 756d window."""
    res = _z(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_mom_z_756d_v166_signal(payables):
    """Relative momentum strength for Raw level of payables over 756d window."""
    res = _z(_slope_pct(payables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_mom_z_756d_v167_signal(cor):
    """Relative momentum strength for Raw level of cor over 756d window."""
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_756d_v168_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 756d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_mom_z_1008d_v169_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 1008d window."""
    res = _z(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_mom_z_1008d_v170_signal(payables):
    """Relative momentum strength for Raw level of payables over 1008d window."""
    res = _z(_slope_pct(payables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_mom_z_1008d_v171_signal(cor):
    """Relative momentum strength for Raw level of cor over 1008d window."""
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_1008d_v172_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 1008d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_mom_z_1260d_v173_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 1260d window."""
    res = _z(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_mom_z_1260d_v174_signal(payables):
    """Relative momentum strength for Raw level of payables over 1260d window."""
    res = _z(_slope_pct(payables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_mom_z_1260d_v175_signal(cor):
    """Relative momentum strength for Raw level of cor over 1260d window."""
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_mom_z_1260d_v176_signal(payables, inventory):
    """Relative momentum strength for Percentage of inventory financed by vendors over 1260d window."""
    res = _z(_slope_pct(_ratio(payables, inventory), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_5d_v177_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 5d window."""
    res = _std(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_5d_v178_signal(payables):
    """Volatility of the momentum for Raw level of payables over 5d window."""
    res = _std(_slope_pct(payables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_5d_v179_signal(cor):
    """Volatility of the momentum for Raw level of cor over 5d window."""
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_5d_v180_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 5d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_10d_v181_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 10d window."""
    res = _std(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_10d_v182_signal(payables):
    """Volatility of the momentum for Raw level of payables over 10d window."""
    res = _std(_slope_pct(payables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_10d_v183_signal(cor):
    """Volatility of the momentum for Raw level of cor over 10d window."""
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_10d_v184_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 10d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_21d_v185_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 21d window."""
    res = _std(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_21d_v186_signal(payables):
    """Volatility of the momentum for Raw level of payables over 21d window."""
    res = _std(_slope_pct(payables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_21d_v187_signal(cor):
    """Volatility of the momentum for Raw level of cor over 21d window."""
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_21d_v188_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 21d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_42d_v189_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 42d window."""
    res = _std(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_42d_v190_signal(payables):
    """Volatility of the momentum for Raw level of payables over 42d window."""
    res = _std(_slope_pct(payables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_42d_v191_signal(cor):
    """Volatility of the momentum for Raw level of cor over 42d window."""
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_42d_v192_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 42d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_63d_v193_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 63d window."""
    res = _std(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_63d_v194_signal(payables):
    """Volatility of the momentum for Raw level of payables over 63d window."""
    res = _std(_slope_pct(payables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_63d_v195_signal(cor):
    """Volatility of the momentum for Raw level of cor over 63d window."""
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_63d_v196_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 63d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_126d_v197_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 126d window."""
    res = _std(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_126d_v198_signal(payables):
    """Volatility of the momentum for Raw level of payables over 126d window."""
    res = _std(_slope_pct(payables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_126d_v199_signal(cor):
    """Volatility of the momentum for Raw level of cor over 126d window."""
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_126d_v200_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 126d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_252d_v201_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 252d window."""
    res = _std(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_252d_v202_signal(payables):
    """Volatility of the momentum for Raw level of payables over 252d window."""
    res = _std(_slope_pct(payables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_252d_v203_signal(cor):
    """Volatility of the momentum for Raw level of cor over 252d window."""
    res = _std(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_252d_v204_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 252d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_504d_v205_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 504d window."""
    res = _std(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_504d_v206_signal(payables):
    """Volatility of the momentum for Raw level of payables over 504d window."""
    res = _std(_slope_pct(payables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_504d_v207_signal(cor):
    """Volatility of the momentum for Raw level of cor over 504d window."""
    res = _std(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_504d_v208_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 504d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_756d_v209_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 756d window."""
    res = _std(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_756d_v210_signal(payables):
    """Volatility of the momentum for Raw level of payables over 756d window."""
    res = _std(_slope_pct(payables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_756d_v211_signal(cor):
    """Volatility of the momentum for Raw level of cor over 756d window."""
    res = _std(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_756d_v212_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 756d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_1008d_v213_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 1008d window."""
    res = _std(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_1008d_v214_signal(payables):
    """Volatility of the momentum for Raw level of payables over 1008d window."""
    res = _std(_slope_pct(payables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_1008d_v215_signal(cor):
    """Volatility of the momentum for Raw level of cor over 1008d window."""
    res = _std(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_1008d_v216_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 1008d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_vol_slope_1260d_v217_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 1260d window."""
    res = _std(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_vol_slope_1260d_v218_signal(payables):
    """Volatility of the momentum for Raw level of payables over 1260d window."""
    res = _std(_slope_pct(payables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_vol_slope_1260d_v219_signal(cor):
    """Volatility of the momentum for Raw level of cor over 1260d window."""
    res = _std(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_vol_slope_1260d_v220_signal(payables, inventory):
    """Volatility of the momentum for Percentage of inventory financed by vendors over 1260d window."""
    res = _std(_slope_pct(_ratio(payables, inventory), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f26_vendor_leverage_cor_mom_z_63d_v151_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_63d_v151_signal},    "f26_vendor_leverage_financing_moat_mom_z_63d_v152_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_63d_v152_signal},    "f26_vendor_leverage_inventory_mom_z_126d_v153_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_mom_z_126d_v153_signal},    "f26_vendor_leverage_payables_mom_z_126d_v154_signal": {"inputs": [], "func": f26_vendor_leverage_payables_mom_z_126d_v154_signal},    "f26_vendor_leverage_cor_mom_z_126d_v155_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_126d_v155_signal},    "f26_vendor_leverage_financing_moat_mom_z_126d_v156_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_126d_v156_signal},    "f26_vendor_leverage_inventory_mom_z_252d_v157_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_mom_z_252d_v157_signal},    "f26_vendor_leverage_payables_mom_z_252d_v158_signal": {"inputs": [], "func": f26_vendor_leverage_payables_mom_z_252d_v158_signal},    "f26_vendor_leverage_cor_mom_z_252d_v159_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_252d_v159_signal},    "f26_vendor_leverage_financing_moat_mom_z_252d_v160_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_252d_v160_signal},    "f26_vendor_leverage_inventory_mom_z_504d_v161_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_mom_z_504d_v161_signal},    "f26_vendor_leverage_payables_mom_z_504d_v162_signal": {"inputs": [], "func": f26_vendor_leverage_payables_mom_z_504d_v162_signal},    "f26_vendor_leverage_cor_mom_z_504d_v163_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_504d_v163_signal},    "f26_vendor_leverage_financing_moat_mom_z_504d_v164_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_504d_v164_signal},    "f26_vendor_leverage_inventory_mom_z_756d_v165_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_mom_z_756d_v165_signal},    "f26_vendor_leverage_payables_mom_z_756d_v166_signal": {"inputs": [], "func": f26_vendor_leverage_payables_mom_z_756d_v166_signal},    "f26_vendor_leverage_cor_mom_z_756d_v167_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_756d_v167_signal},    "f26_vendor_leverage_financing_moat_mom_z_756d_v168_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_756d_v168_signal},    "f26_vendor_leverage_inventory_mom_z_1008d_v169_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_mom_z_1008d_v169_signal},    "f26_vendor_leverage_payables_mom_z_1008d_v170_signal": {"inputs": [], "func": f26_vendor_leverage_payables_mom_z_1008d_v170_signal},    "f26_vendor_leverage_cor_mom_z_1008d_v171_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_1008d_v171_signal},    "f26_vendor_leverage_financing_moat_mom_z_1008d_v172_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_1008d_v172_signal},    "f26_vendor_leverage_inventory_mom_z_1260d_v173_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_mom_z_1260d_v173_signal},    "f26_vendor_leverage_payables_mom_z_1260d_v174_signal": {"inputs": [], "func": f26_vendor_leverage_payables_mom_z_1260d_v174_signal},    "f26_vendor_leverage_cor_mom_z_1260d_v175_signal": {"inputs": [], "func": f26_vendor_leverage_cor_mom_z_1260d_v175_signal},    "f26_vendor_leverage_financing_moat_mom_z_1260d_v176_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_mom_z_1260d_v176_signal},    "f26_vendor_leverage_inventory_vol_slope_5d_v177_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_5d_v177_signal},    "f26_vendor_leverage_payables_vol_slope_5d_v178_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_5d_v178_signal},    "f26_vendor_leverage_cor_vol_slope_5d_v179_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_5d_v179_signal},    "f26_vendor_leverage_financing_moat_vol_slope_5d_v180_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_5d_v180_signal},    "f26_vendor_leverage_inventory_vol_slope_10d_v181_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_10d_v181_signal},    "f26_vendor_leverage_payables_vol_slope_10d_v182_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_10d_v182_signal},    "f26_vendor_leverage_cor_vol_slope_10d_v183_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_10d_v183_signal},    "f26_vendor_leverage_financing_moat_vol_slope_10d_v184_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_10d_v184_signal},    "f26_vendor_leverage_inventory_vol_slope_21d_v185_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_21d_v185_signal},    "f26_vendor_leverage_payables_vol_slope_21d_v186_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_21d_v186_signal},    "f26_vendor_leverage_cor_vol_slope_21d_v187_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_21d_v187_signal},    "f26_vendor_leverage_financing_moat_vol_slope_21d_v188_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_21d_v188_signal},    "f26_vendor_leverage_inventory_vol_slope_42d_v189_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_42d_v189_signal},    "f26_vendor_leverage_payables_vol_slope_42d_v190_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_42d_v190_signal},    "f26_vendor_leverage_cor_vol_slope_42d_v191_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_42d_v191_signal},    "f26_vendor_leverage_financing_moat_vol_slope_42d_v192_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_42d_v192_signal},    "f26_vendor_leverage_inventory_vol_slope_63d_v193_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_63d_v193_signal},    "f26_vendor_leverage_payables_vol_slope_63d_v194_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_63d_v194_signal},    "f26_vendor_leverage_cor_vol_slope_63d_v195_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_63d_v195_signal},    "f26_vendor_leverage_financing_moat_vol_slope_63d_v196_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_63d_v196_signal},    "f26_vendor_leverage_inventory_vol_slope_126d_v197_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_126d_v197_signal},    "f26_vendor_leverage_payables_vol_slope_126d_v198_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_126d_v198_signal},    "f26_vendor_leverage_cor_vol_slope_126d_v199_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_126d_v199_signal},    "f26_vendor_leverage_financing_moat_vol_slope_126d_v200_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_126d_v200_signal},    "f26_vendor_leverage_inventory_vol_slope_252d_v201_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_252d_v201_signal},    "f26_vendor_leverage_payables_vol_slope_252d_v202_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_252d_v202_signal},    "f26_vendor_leverage_cor_vol_slope_252d_v203_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_252d_v203_signal},    "f26_vendor_leverage_financing_moat_vol_slope_252d_v204_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_252d_v204_signal},    "f26_vendor_leverage_inventory_vol_slope_504d_v205_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_504d_v205_signal},    "f26_vendor_leverage_payables_vol_slope_504d_v206_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_504d_v206_signal},    "f26_vendor_leverage_cor_vol_slope_504d_v207_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_504d_v207_signal},    "f26_vendor_leverage_financing_moat_vol_slope_504d_v208_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_504d_v208_signal},    "f26_vendor_leverage_inventory_vol_slope_756d_v209_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_756d_v209_signal},    "f26_vendor_leverage_payables_vol_slope_756d_v210_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_756d_v210_signal},    "f26_vendor_leverage_cor_vol_slope_756d_v211_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_756d_v211_signal},    "f26_vendor_leverage_financing_moat_vol_slope_756d_v212_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_756d_v212_signal},    "f26_vendor_leverage_inventory_vol_slope_1008d_v213_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_1008d_v213_signal},    "f26_vendor_leverage_payables_vol_slope_1008d_v214_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_1008d_v214_signal},    "f26_vendor_leverage_cor_vol_slope_1008d_v215_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_1008d_v215_signal},    "f26_vendor_leverage_financing_moat_vol_slope_1008d_v216_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_1008d_v216_signal},    "f26_vendor_leverage_inventory_vol_slope_1260d_v217_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_vol_slope_1260d_v217_signal},    "f26_vendor_leverage_payables_vol_slope_1260d_v218_signal": {"inputs": [], "func": f26_vendor_leverage_payables_vol_slope_1260d_v218_signal},    "f26_vendor_leverage_cor_vol_slope_1260d_v219_signal": {"inputs": [], "func": f26_vendor_leverage_cor_vol_slope_1260d_v219_signal},    "f26_vendor_leverage_financing_moat_vol_slope_1260d_v220_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_vol_slope_1260d_v220_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 26...")
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
