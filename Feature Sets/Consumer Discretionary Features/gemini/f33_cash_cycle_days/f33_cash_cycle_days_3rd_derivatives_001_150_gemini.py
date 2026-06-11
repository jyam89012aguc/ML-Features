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

def f33_cash_cycle_days_receivables_slope_diff_norm_756d_v151_signal(receivables):
    """Normalized slope change for Raw level of receivables over 756d window."""
    res = (_slope_pct(receivables, 756).diff(756) / _sma(receivables.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_slope_diff_norm_756d_v152_signal(inventory):
    """Normalized slope change for Raw level of inventory over 756d window."""
    res = (_slope_pct(inventory, 756).diff(756) / _sma(inventory.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_slope_diff_norm_756d_v153_signal(payables):
    """Normalized slope change for Raw level of payables over 756d window."""
    res = (_slope_pct(payables, 756).diff(756) / _sma(payables.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_slope_diff_norm_756d_v154_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_slope_diff_norm_756d_v155_signal(receivables, inventory, payables, cor):
    """Normalized slope change for Full cash conversion cycle in days over 756d window."""
    res = (_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 756).diff(756) / _sma(_ratio(receivables + inventory - payables, cor) * 365.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_slope_diff_norm_1008d_v156_signal(receivables):
    """Normalized slope change for Raw level of receivables over 1008d window."""
    res = (_slope_pct(receivables, 1008).diff(1008) / _sma(receivables.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_slope_diff_norm_1008d_v157_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1008d window."""
    res = (_slope_pct(inventory, 1008).diff(1008) / _sma(inventory.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_slope_diff_norm_1008d_v158_signal(payables):
    """Normalized slope change for Raw level of payables over 1008d window."""
    res = (_slope_pct(payables, 1008).diff(1008) / _sma(payables.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_slope_diff_norm_1008d_v159_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_slope_diff_norm_1008d_v160_signal(receivables, inventory, payables, cor):
    """Normalized slope change for Full cash conversion cycle in days over 1008d window."""
    res = (_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 1008).diff(1008) / _sma(_ratio(receivables + inventory - payables, cor) * 365.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_slope_diff_norm_1260d_v161_signal(receivables):
    """Normalized slope change for Raw level of receivables over 1260d window."""
    res = (_slope_pct(receivables, 1260).diff(1260) / _sma(receivables.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_slope_diff_norm_1260d_v162_signal(inventory):
    """Normalized slope change for Raw level of inventory over 1260d window."""
    res = (_slope_pct(inventory, 1260).diff(1260) / _sma(inventory.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_slope_diff_norm_1260d_v163_signal(payables):
    """Normalized slope change for Raw level of payables over 1260d window."""
    res = (_slope_pct(payables, 1260).diff(1260) / _sma(payables.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_slope_diff_norm_1260d_v164_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_slope_diff_norm_1260d_v165_signal(receivables, inventory, payables, cor):
    """Normalized slope change for Full cash conversion cycle in days over 1260d window."""
    res = (_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 1260).diff(1260) / _sma(_ratio(receivables + inventory - payables, cor) * 365.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_5d_v166_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 5d window."""
    res = _z(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_5d_v167_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 5d window."""
    res = _z(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_5d_v168_signal(payables):
    """Relative momentum strength for Raw level of payables over 5d window."""
    res = _z(_slope_pct(payables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_5d_v169_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_5d_v170_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 5d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_10d_v171_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 10d window."""
    res = _z(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_10d_v172_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 10d window."""
    res = _z(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_10d_v173_signal(payables):
    """Relative momentum strength for Raw level of payables over 10d window."""
    res = _z(_slope_pct(payables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_10d_v174_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_10d_v175_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 10d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_21d_v176_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 21d window."""
    res = _z(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_21d_v177_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 21d window."""
    res = _z(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_21d_v178_signal(payables):
    """Relative momentum strength for Raw level of payables over 21d window."""
    res = _z(_slope_pct(payables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_21d_v179_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_21d_v180_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 21d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_42d_v181_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 42d window."""
    res = _z(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_42d_v182_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 42d window."""
    res = _z(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_42d_v183_signal(payables):
    """Relative momentum strength for Raw level of payables over 42d window."""
    res = _z(_slope_pct(payables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_42d_v184_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_42d_v185_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 42d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_63d_v186_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 63d window."""
    res = _z(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_63d_v187_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 63d window."""
    res = _z(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_63d_v188_signal(payables):
    """Relative momentum strength for Raw level of payables over 63d window."""
    res = _z(_slope_pct(payables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_63d_v189_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_63d_v190_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 63d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_126d_v191_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 126d window."""
    res = _z(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_126d_v192_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 126d window."""
    res = _z(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_126d_v193_signal(payables):
    """Relative momentum strength for Raw level of payables over 126d window."""
    res = _z(_slope_pct(payables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_126d_v194_signal(cor):
    """Relative momentum strength for Raw level of cor over 126d window."""
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_126d_v195_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 126d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_252d_v196_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 252d window."""
    res = _z(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_252d_v197_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 252d window."""
    res = _z(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_252d_v198_signal(payables):
    """Relative momentum strength for Raw level of payables over 252d window."""
    res = _z(_slope_pct(payables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_252d_v199_signal(cor):
    """Relative momentum strength for Raw level of cor over 252d window."""
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_252d_v200_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 252d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_504d_v201_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 504d window."""
    res = _z(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_504d_v202_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 504d window."""
    res = _z(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_504d_v203_signal(payables):
    """Relative momentum strength for Raw level of payables over 504d window."""
    res = _z(_slope_pct(payables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_504d_v204_signal(cor):
    """Relative momentum strength for Raw level of cor over 504d window."""
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_504d_v205_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 504d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_756d_v206_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 756d window."""
    res = _z(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_756d_v207_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 756d window."""
    res = _z(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_756d_v208_signal(payables):
    """Relative momentum strength for Raw level of payables over 756d window."""
    res = _z(_slope_pct(payables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_756d_v209_signal(cor):
    """Relative momentum strength for Raw level of cor over 756d window."""
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_756d_v210_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 756d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_1008d_v211_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 1008d window."""
    res = _z(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_1008d_v212_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 1008d window."""
    res = _z(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_1008d_v213_signal(payables):
    """Relative momentum strength for Raw level of payables over 1008d window."""
    res = _z(_slope_pct(payables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_1008d_v214_signal(cor):
    """Relative momentum strength for Raw level of cor over 1008d window."""
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_1008d_v215_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 1008d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_mom_z_1260d_v216_signal(receivables):
    """Relative momentum strength for Raw level of receivables over 1260d window."""
    res = _z(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_mom_z_1260d_v217_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 1260d window."""
    res = _z(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_mom_z_1260d_v218_signal(payables):
    """Relative momentum strength for Raw level of payables over 1260d window."""
    res = _z(_slope_pct(payables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_mom_z_1260d_v219_signal(cor):
    """Relative momentum strength for Raw level of cor over 1260d window."""
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_mom_z_1260d_v220_signal(receivables, inventory, payables, cor):
    """Relative momentum strength for Full cash conversion cycle in days over 1260d window."""
    res = _z(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_5d_v221_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 5d window."""
    res = _std(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_5d_v222_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 5d window."""
    res = _std(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_5d_v223_signal(payables):
    """Volatility of the momentum for Raw level of payables over 5d window."""
    res = _std(_slope_pct(payables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_5d_v224_signal(cor):
    """Volatility of the momentum for Raw level of cor over 5d window."""
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_5d_v225_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 5d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_10d_v226_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 10d window."""
    res = _std(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_10d_v227_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 10d window."""
    res = _std(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_10d_v228_signal(payables):
    """Volatility of the momentum for Raw level of payables over 10d window."""
    res = _std(_slope_pct(payables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_10d_v229_signal(cor):
    """Volatility of the momentum for Raw level of cor over 10d window."""
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_10d_v230_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 10d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_21d_v231_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 21d window."""
    res = _std(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_21d_v232_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 21d window."""
    res = _std(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_21d_v233_signal(payables):
    """Volatility of the momentum for Raw level of payables over 21d window."""
    res = _std(_slope_pct(payables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_21d_v234_signal(cor):
    """Volatility of the momentum for Raw level of cor over 21d window."""
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_21d_v235_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 21d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_42d_v236_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 42d window."""
    res = _std(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_42d_v237_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 42d window."""
    res = _std(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_42d_v238_signal(payables):
    """Volatility of the momentum for Raw level of payables over 42d window."""
    res = _std(_slope_pct(payables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_42d_v239_signal(cor):
    """Volatility of the momentum for Raw level of cor over 42d window."""
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_42d_v240_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 42d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_63d_v241_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 63d window."""
    res = _std(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_63d_v242_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 63d window."""
    res = _std(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_63d_v243_signal(payables):
    """Volatility of the momentum for Raw level of payables over 63d window."""
    res = _std(_slope_pct(payables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_63d_v244_signal(cor):
    """Volatility of the momentum for Raw level of cor over 63d window."""
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_63d_v245_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 63d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_126d_v246_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 126d window."""
    res = _std(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_126d_v247_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 126d window."""
    res = _std(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_126d_v248_signal(payables):
    """Volatility of the momentum for Raw level of payables over 126d window."""
    res = _std(_slope_pct(payables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_126d_v249_signal(cor):
    """Volatility of the momentum for Raw level of cor over 126d window."""
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_126d_v250_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 126d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_252d_v251_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 252d window."""
    res = _std(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_252d_v252_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 252d window."""
    res = _std(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_252d_v253_signal(payables):
    """Volatility of the momentum for Raw level of payables over 252d window."""
    res = _std(_slope_pct(payables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_252d_v254_signal(cor):
    """Volatility of the momentum for Raw level of cor over 252d window."""
    res = _std(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_252d_v255_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 252d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_504d_v256_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 504d window."""
    res = _std(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_504d_v257_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 504d window."""
    res = _std(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_504d_v258_signal(payables):
    """Volatility of the momentum for Raw level of payables over 504d window."""
    res = _std(_slope_pct(payables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_504d_v259_signal(cor):
    """Volatility of the momentum for Raw level of cor over 504d window."""
    res = _std(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_504d_v260_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 504d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_756d_v261_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 756d window."""
    res = _std(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_756d_v262_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 756d window."""
    res = _std(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_756d_v263_signal(payables):
    """Volatility of the momentum for Raw level of payables over 756d window."""
    res = _std(_slope_pct(payables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_756d_v264_signal(cor):
    """Volatility of the momentum for Raw level of cor over 756d window."""
    res = _std(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_756d_v265_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 756d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_1008d_v266_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 1008d window."""
    res = _std(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_1008d_v267_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 1008d window."""
    res = _std(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_1008d_v268_signal(payables):
    """Volatility of the momentum for Raw level of payables over 1008d window."""
    res = _std(_slope_pct(payables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_1008d_v269_signal(cor):
    """Volatility of the momentum for Raw level of cor over 1008d window."""
    res = _std(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_1008d_v270_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 1008d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_receivables_vol_slope_1260d_v271_signal(receivables):
    """Volatility of the momentum for Raw level of receivables over 1260d window."""
    res = _std(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_inventory_vol_slope_1260d_v272_signal(inventory):
    """Volatility of the momentum for Raw level of inventory over 1260d window."""
    res = _std(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_payables_vol_slope_1260d_v273_signal(payables):
    """Volatility of the momentum for Raw level of payables over 1260d window."""
    res = _std(_slope_pct(payables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cor_vol_slope_1260d_v274_signal(cor):
    """Volatility of the momentum for Raw level of cor over 1260d window."""
    res = _std(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_cash_cycle_days_cash_cycle_vol_slope_1260d_v275_signal(receivables, inventory, payables, cor):
    """Volatility of the momentum for Full cash conversion cycle in days over 1260d window."""
    res = _std(_slope_pct(_ratio(receivables + inventory - payables, cor) * 365, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f33_cash_cycle_days_receivables_slope_diff_norm_756d_v151_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_slope_diff_norm_756d_v151_signal},    "f33_cash_cycle_days_inventory_slope_diff_norm_756d_v152_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_slope_diff_norm_756d_v152_signal},    "f33_cash_cycle_days_payables_slope_diff_norm_756d_v153_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_slope_diff_norm_756d_v153_signal},    "f33_cash_cycle_days_cor_slope_diff_norm_756d_v154_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_slope_diff_norm_756d_v154_signal},    "f33_cash_cycle_days_cash_cycle_slope_diff_norm_756d_v155_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_slope_diff_norm_756d_v155_signal},    "f33_cash_cycle_days_receivables_slope_diff_norm_1008d_v156_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_slope_diff_norm_1008d_v156_signal},    "f33_cash_cycle_days_inventory_slope_diff_norm_1008d_v157_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_slope_diff_norm_1008d_v157_signal},    "f33_cash_cycle_days_payables_slope_diff_norm_1008d_v158_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_slope_diff_norm_1008d_v158_signal},    "f33_cash_cycle_days_cor_slope_diff_norm_1008d_v159_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_slope_diff_norm_1008d_v159_signal},    "f33_cash_cycle_days_cash_cycle_slope_diff_norm_1008d_v160_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_slope_diff_norm_1008d_v160_signal},    "f33_cash_cycle_days_receivables_slope_diff_norm_1260d_v161_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_slope_diff_norm_1260d_v161_signal},    "f33_cash_cycle_days_inventory_slope_diff_norm_1260d_v162_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_slope_diff_norm_1260d_v162_signal},    "f33_cash_cycle_days_payables_slope_diff_norm_1260d_v163_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_slope_diff_norm_1260d_v163_signal},    "f33_cash_cycle_days_cor_slope_diff_norm_1260d_v164_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_slope_diff_norm_1260d_v164_signal},    "f33_cash_cycle_days_cash_cycle_slope_diff_norm_1260d_v165_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_slope_diff_norm_1260d_v165_signal},    "f33_cash_cycle_days_receivables_mom_z_5d_v166_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_5d_v166_signal},    "f33_cash_cycle_days_inventory_mom_z_5d_v167_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_5d_v167_signal},    "f33_cash_cycle_days_payables_mom_z_5d_v168_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_5d_v168_signal},    "f33_cash_cycle_days_cor_mom_z_5d_v169_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_5d_v169_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_5d_v170_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_5d_v170_signal},    "f33_cash_cycle_days_receivables_mom_z_10d_v171_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_10d_v171_signal},    "f33_cash_cycle_days_inventory_mom_z_10d_v172_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_10d_v172_signal},    "f33_cash_cycle_days_payables_mom_z_10d_v173_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_10d_v173_signal},    "f33_cash_cycle_days_cor_mom_z_10d_v174_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_10d_v174_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_10d_v175_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_10d_v175_signal},    "f33_cash_cycle_days_receivables_mom_z_21d_v176_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_21d_v176_signal},    "f33_cash_cycle_days_inventory_mom_z_21d_v177_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_21d_v177_signal},    "f33_cash_cycle_days_payables_mom_z_21d_v178_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_21d_v178_signal},    "f33_cash_cycle_days_cor_mom_z_21d_v179_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_21d_v179_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_21d_v180_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_21d_v180_signal},    "f33_cash_cycle_days_receivables_mom_z_42d_v181_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_42d_v181_signal},    "f33_cash_cycle_days_inventory_mom_z_42d_v182_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_42d_v182_signal},    "f33_cash_cycle_days_payables_mom_z_42d_v183_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_42d_v183_signal},    "f33_cash_cycle_days_cor_mom_z_42d_v184_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_42d_v184_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_42d_v185_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_42d_v185_signal},    "f33_cash_cycle_days_receivables_mom_z_63d_v186_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_63d_v186_signal},    "f33_cash_cycle_days_inventory_mom_z_63d_v187_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_63d_v187_signal},    "f33_cash_cycle_days_payables_mom_z_63d_v188_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_63d_v188_signal},    "f33_cash_cycle_days_cor_mom_z_63d_v189_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_63d_v189_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_63d_v190_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_63d_v190_signal},    "f33_cash_cycle_days_receivables_mom_z_126d_v191_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_126d_v191_signal},    "f33_cash_cycle_days_inventory_mom_z_126d_v192_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_126d_v192_signal},    "f33_cash_cycle_days_payables_mom_z_126d_v193_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_126d_v193_signal},    "f33_cash_cycle_days_cor_mom_z_126d_v194_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_126d_v194_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_126d_v195_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_126d_v195_signal},    "f33_cash_cycle_days_receivables_mom_z_252d_v196_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_252d_v196_signal},    "f33_cash_cycle_days_inventory_mom_z_252d_v197_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_252d_v197_signal},    "f33_cash_cycle_days_payables_mom_z_252d_v198_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_252d_v198_signal},    "f33_cash_cycle_days_cor_mom_z_252d_v199_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_252d_v199_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_252d_v200_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_252d_v200_signal},    "f33_cash_cycle_days_receivables_mom_z_504d_v201_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_504d_v201_signal},    "f33_cash_cycle_days_inventory_mom_z_504d_v202_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_504d_v202_signal},    "f33_cash_cycle_days_payables_mom_z_504d_v203_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_504d_v203_signal},    "f33_cash_cycle_days_cor_mom_z_504d_v204_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_504d_v204_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_504d_v205_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_504d_v205_signal},    "f33_cash_cycle_days_receivables_mom_z_756d_v206_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_756d_v206_signal},    "f33_cash_cycle_days_inventory_mom_z_756d_v207_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_756d_v207_signal},    "f33_cash_cycle_days_payables_mom_z_756d_v208_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_756d_v208_signal},    "f33_cash_cycle_days_cor_mom_z_756d_v209_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_756d_v209_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_756d_v210_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_756d_v210_signal},    "f33_cash_cycle_days_receivables_mom_z_1008d_v211_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_1008d_v211_signal},    "f33_cash_cycle_days_inventory_mom_z_1008d_v212_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_1008d_v212_signal},    "f33_cash_cycle_days_payables_mom_z_1008d_v213_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_1008d_v213_signal},    "f33_cash_cycle_days_cor_mom_z_1008d_v214_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_1008d_v214_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_1008d_v215_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_1008d_v215_signal},    "f33_cash_cycle_days_receivables_mom_z_1260d_v216_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_mom_z_1260d_v216_signal},    "f33_cash_cycle_days_inventory_mom_z_1260d_v217_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_mom_z_1260d_v217_signal},    "f33_cash_cycle_days_payables_mom_z_1260d_v218_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_mom_z_1260d_v218_signal},    "f33_cash_cycle_days_cor_mom_z_1260d_v219_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_mom_z_1260d_v219_signal},    "f33_cash_cycle_days_cash_cycle_mom_z_1260d_v220_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_mom_z_1260d_v220_signal},    "f33_cash_cycle_days_receivables_vol_slope_5d_v221_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_5d_v221_signal},    "f33_cash_cycle_days_inventory_vol_slope_5d_v222_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_5d_v222_signal},    "f33_cash_cycle_days_payables_vol_slope_5d_v223_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_5d_v223_signal},    "f33_cash_cycle_days_cor_vol_slope_5d_v224_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_5d_v224_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_5d_v225_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_5d_v225_signal},    "f33_cash_cycle_days_receivables_vol_slope_10d_v226_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_10d_v226_signal},    "f33_cash_cycle_days_inventory_vol_slope_10d_v227_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_10d_v227_signal},    "f33_cash_cycle_days_payables_vol_slope_10d_v228_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_10d_v228_signal},    "f33_cash_cycle_days_cor_vol_slope_10d_v229_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_10d_v229_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_10d_v230_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_10d_v230_signal},    "f33_cash_cycle_days_receivables_vol_slope_21d_v231_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_21d_v231_signal},    "f33_cash_cycle_days_inventory_vol_slope_21d_v232_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_21d_v232_signal},    "f33_cash_cycle_days_payables_vol_slope_21d_v233_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_21d_v233_signal},    "f33_cash_cycle_days_cor_vol_slope_21d_v234_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_21d_v234_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_21d_v235_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_21d_v235_signal},    "f33_cash_cycle_days_receivables_vol_slope_42d_v236_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_42d_v236_signal},    "f33_cash_cycle_days_inventory_vol_slope_42d_v237_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_42d_v237_signal},    "f33_cash_cycle_days_payables_vol_slope_42d_v238_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_42d_v238_signal},    "f33_cash_cycle_days_cor_vol_slope_42d_v239_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_42d_v239_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_42d_v240_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_42d_v240_signal},    "f33_cash_cycle_days_receivables_vol_slope_63d_v241_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_63d_v241_signal},    "f33_cash_cycle_days_inventory_vol_slope_63d_v242_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_63d_v242_signal},    "f33_cash_cycle_days_payables_vol_slope_63d_v243_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_63d_v243_signal},    "f33_cash_cycle_days_cor_vol_slope_63d_v244_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_63d_v244_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_63d_v245_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_63d_v245_signal},    "f33_cash_cycle_days_receivables_vol_slope_126d_v246_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_126d_v246_signal},    "f33_cash_cycle_days_inventory_vol_slope_126d_v247_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_126d_v247_signal},    "f33_cash_cycle_days_payables_vol_slope_126d_v248_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_126d_v248_signal},    "f33_cash_cycle_days_cor_vol_slope_126d_v249_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_126d_v249_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_126d_v250_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_126d_v250_signal},    "f33_cash_cycle_days_receivables_vol_slope_252d_v251_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_252d_v251_signal},    "f33_cash_cycle_days_inventory_vol_slope_252d_v252_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_252d_v252_signal},    "f33_cash_cycle_days_payables_vol_slope_252d_v253_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_252d_v253_signal},    "f33_cash_cycle_days_cor_vol_slope_252d_v254_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_252d_v254_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_252d_v255_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_252d_v255_signal},    "f33_cash_cycle_days_receivables_vol_slope_504d_v256_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_504d_v256_signal},    "f33_cash_cycle_days_inventory_vol_slope_504d_v257_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_504d_v257_signal},    "f33_cash_cycle_days_payables_vol_slope_504d_v258_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_504d_v258_signal},    "f33_cash_cycle_days_cor_vol_slope_504d_v259_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_504d_v259_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_504d_v260_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_504d_v260_signal},    "f33_cash_cycle_days_receivables_vol_slope_756d_v261_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_756d_v261_signal},    "f33_cash_cycle_days_inventory_vol_slope_756d_v262_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_756d_v262_signal},    "f33_cash_cycle_days_payables_vol_slope_756d_v263_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_756d_v263_signal},    "f33_cash_cycle_days_cor_vol_slope_756d_v264_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_756d_v264_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_756d_v265_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_756d_v265_signal},    "f33_cash_cycle_days_receivables_vol_slope_1008d_v266_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_1008d_v266_signal},    "f33_cash_cycle_days_inventory_vol_slope_1008d_v267_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_1008d_v267_signal},    "f33_cash_cycle_days_payables_vol_slope_1008d_v268_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_1008d_v268_signal},    "f33_cash_cycle_days_cor_vol_slope_1008d_v269_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_1008d_v269_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_1008d_v270_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_1008d_v270_signal},    "f33_cash_cycle_days_receivables_vol_slope_1260d_v271_signal": {"inputs": [], "func": f33_cash_cycle_days_receivables_vol_slope_1260d_v271_signal},    "f33_cash_cycle_days_inventory_vol_slope_1260d_v272_signal": {"inputs": [], "func": f33_cash_cycle_days_inventory_vol_slope_1260d_v272_signal},    "f33_cash_cycle_days_payables_vol_slope_1260d_v273_signal": {"inputs": [], "func": f33_cash_cycle_days_payables_vol_slope_1260d_v273_signal},    "f33_cash_cycle_days_cor_vol_slope_1260d_v274_signal": {"inputs": [], "func": f33_cash_cycle_days_cor_vol_slope_1260d_v274_signal},    "f33_cash_cycle_days_cash_cycle_vol_slope_1260d_v275_signal": {"inputs": [], "func": f33_cash_cycle_days_cash_cycle_vol_slope_1260d_v275_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 33...")
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
