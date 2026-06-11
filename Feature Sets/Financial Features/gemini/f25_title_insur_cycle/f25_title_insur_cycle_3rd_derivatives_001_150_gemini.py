import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
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

def f25_title_insur_cycle_cor_mom_z_63d_v151_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_63d_v152_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 63d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_126d_v153_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_126d_v154_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 126d window."""
    res = _z(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_126d_v155_signal(cor):
    """Relative momentum strength for Raw level of cor over 126d window."""
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_126d_v156_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 126d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_252d_v157_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_252d_v158_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 252d window."""
    res = _z(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_252d_v159_signal(cor):
    """Relative momentum strength for Raw level of cor over 252d window."""
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_252d_v160_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 252d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_504d_v161_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_504d_v162_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 504d window."""
    res = _z(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_504d_v163_signal(cor):
    """Relative momentum strength for Raw level of cor over 504d window."""
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_504d_v164_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 504d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_756d_v165_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_756d_v166_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 756d window."""
    res = _z(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_756d_v167_signal(cor):
    """Relative momentum strength for Raw level of cor over 756d window."""
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_756d_v168_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 756d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_1008d_v169_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_1008d_v170_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 1008d window."""
    res = _z(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_1008d_v171_signal(cor):
    """Relative momentum strength for Raw level of cor over 1008d window."""
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_1008d_v172_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 1008d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_mom_z_1260d_v173_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_mom_z_1260d_v174_signal(inventory):
    """Relative momentum strength for Raw level of inventory over 1260d window."""
    res = _z(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_mom_z_1260d_v175_signal(cor):
    """Relative momentum strength for Raw level of cor over 1260d window."""
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_mom_z_1260d_v176_signal(revenue):
    """Relative momentum strength for Revenue relative to long-term cycle over 1260d window."""
    res = _z(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_5d_v177_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_5d_v178_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 5d window."""
    res = _std(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_5d_v179_signal(cor):
    """Volatility of momentum for Raw level of cor over 5d window."""
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_5d_v180_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 5d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_10d_v181_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_10d_v182_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 10d window."""
    res = _std(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_10d_v183_signal(cor):
    """Volatility of momentum for Raw level of cor over 10d window."""
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_10d_v184_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 10d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_21d_v185_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_21d_v186_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 21d window."""
    res = _std(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_21d_v187_signal(cor):
    """Volatility of momentum for Raw level of cor over 21d window."""
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_21d_v188_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 21d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_42d_v189_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_42d_v190_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 42d window."""
    res = _std(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_42d_v191_signal(cor):
    """Volatility of momentum for Raw level of cor over 42d window."""
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_42d_v192_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 42d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_63d_v193_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_63d_v194_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 63d window."""
    res = _std(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_63d_v195_signal(cor):
    """Volatility of momentum for Raw level of cor over 63d window."""
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_63d_v196_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 63d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_126d_v197_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_126d_v198_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 126d window."""
    res = _std(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_126d_v199_signal(cor):
    """Volatility of momentum for Raw level of cor over 126d window."""
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_126d_v200_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 126d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_252d_v201_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_252d_v202_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 252d window."""
    res = _std(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_252d_v203_signal(cor):
    """Volatility of momentum for Raw level of cor over 252d window."""
    res = _std(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_252d_v204_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 252d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_504d_v205_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_504d_v206_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 504d window."""
    res = _std(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_504d_v207_signal(cor):
    """Volatility of momentum for Raw level of cor over 504d window."""
    res = _std(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_504d_v208_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 504d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_756d_v209_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_756d_v210_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 756d window."""
    res = _std(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_756d_v211_signal(cor):
    """Volatility of momentum for Raw level of cor over 756d window."""
    res = _std(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_756d_v212_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 756d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_1008d_v213_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_1008d_v214_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 1008d window."""
    res = _std(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_1008d_v215_signal(cor):
    """Volatility of momentum for Raw level of cor over 1008d window."""
    res = _std(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_1008d_v216_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 1008d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_vol_slope_1260d_v217_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_vol_slope_1260d_v218_signal(inventory):
    """Volatility of momentum for Raw level of inventory over 1260d window."""
    res = _std(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_vol_slope_1260d_v219_signal(cor):
    """Volatility of momentum for Raw level of cor over 1260d window."""
    res = _std(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_vol_slope_1260d_v220_signal(revenue):
    """Volatility of momentum for Revenue relative to long-term cycle over 1260d window."""
    res = _std(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_5d_v221_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 5d window."""
    res = _ewma(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_5d_v222_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 5d window."""
    res = _ewma(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_5d_v223_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 5d window."""
    res = _ewma(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_5d_v224_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 5d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_10d_v225_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 10d window."""
    res = _ewma(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_10d_v226_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 10d window."""
    res = _ewma(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_10d_v227_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 10d window."""
    res = _ewma(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_10d_v228_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 10d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_21d_v229_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 21d window."""
    res = _ewma(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_21d_v230_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 21d window."""
    res = _ewma(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_21d_v231_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 21d window."""
    res = _ewma(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_21d_v232_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 21d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_42d_v233_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 42d window."""
    res = _ewma(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_42d_v234_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 42d window."""
    res = _ewma(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_42d_v235_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 42d window."""
    res = _ewma(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_42d_v236_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 42d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_63d_v237_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 63d window."""
    res = _ewma(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_63d_v238_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 63d window."""
    res = _ewma(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_63d_v239_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 63d window."""
    res = _ewma(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_63d_v240_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 63d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_126d_v241_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 126d window."""
    res = _ewma(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_126d_v242_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 126d window."""
    res = _ewma(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_126d_v243_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 126d window."""
    res = _ewma(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_126d_v244_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 126d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_252d_v245_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 252d window."""
    res = _ewma(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_252d_v246_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 252d window."""
    res = _ewma(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_252d_v247_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 252d window."""
    res = _ewma(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_252d_v248_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 252d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_504d_v249_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 504d window."""
    res = _ewma(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_504d_v250_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 504d window."""
    res = _ewma(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_504d_v251_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 504d window."""
    res = _ewma(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_504d_v252_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 504d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_756d_v253_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 756d window."""
    res = _ewma(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_756d_v254_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 756d window."""
    res = _ewma(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_756d_v255_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 756d window."""
    res = _ewma(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_756d_v256_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 756d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_1008d_v257_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1008d window."""
    res = _ewma(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_1008d_v258_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 1008d window."""
    res = _ewma(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_1008d_v259_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 1008d window."""
    res = _ewma(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_1008d_v260_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 1008d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_slope_1260d_v261_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1260d window."""
    res = _ewma(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_slope_1260d_v262_signal(inventory):
    """Exponential momentum smoothing for Raw level of inventory over 1260d window."""
    res = _ewma(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_slope_1260d_v263_signal(cor):
    """Exponential momentum smoothing for Raw level of cor over 1260d window."""
    res = _ewma(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_slope_1260d_v264_signal(revenue):
    """Exponential momentum smoothing for Revenue relative to long-term cycle over 1260d window."""
    res = _ewma(_slope_pct(_ratio(revenue, _sma(revenue, 1260)), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f25_title_insur_cycle_cor_mom_z_63d_v151_signal": {"func": f25_title_insur_cycle_cor_mom_z_63d_v151_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_63d_v152_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_63d_v152_signal},
    "f25_title_insur_cycle_revenue_mom_z_126d_v153_signal": {"func": f25_title_insur_cycle_revenue_mom_z_126d_v153_signal},
    "f25_title_insur_cycle_inventory_mom_z_126d_v154_signal": {"func": f25_title_insur_cycle_inventory_mom_z_126d_v154_signal},
    "f25_title_insur_cycle_cor_mom_z_126d_v155_signal": {"func": f25_title_insur_cycle_cor_mom_z_126d_v155_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_126d_v156_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_126d_v156_signal},
    "f25_title_insur_cycle_revenue_mom_z_252d_v157_signal": {"func": f25_title_insur_cycle_revenue_mom_z_252d_v157_signal},
    "f25_title_insur_cycle_inventory_mom_z_252d_v158_signal": {"func": f25_title_insur_cycle_inventory_mom_z_252d_v158_signal},
    "f25_title_insur_cycle_cor_mom_z_252d_v159_signal": {"func": f25_title_insur_cycle_cor_mom_z_252d_v159_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_252d_v160_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_252d_v160_signal},
    "f25_title_insur_cycle_revenue_mom_z_504d_v161_signal": {"func": f25_title_insur_cycle_revenue_mom_z_504d_v161_signal},
    "f25_title_insur_cycle_inventory_mom_z_504d_v162_signal": {"func": f25_title_insur_cycle_inventory_mom_z_504d_v162_signal},
    "f25_title_insur_cycle_cor_mom_z_504d_v163_signal": {"func": f25_title_insur_cycle_cor_mom_z_504d_v163_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_504d_v164_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_504d_v164_signal},
    "f25_title_insur_cycle_revenue_mom_z_756d_v165_signal": {"func": f25_title_insur_cycle_revenue_mom_z_756d_v165_signal},
    "f25_title_insur_cycle_inventory_mom_z_756d_v166_signal": {"func": f25_title_insur_cycle_inventory_mom_z_756d_v166_signal},
    "f25_title_insur_cycle_cor_mom_z_756d_v167_signal": {"func": f25_title_insur_cycle_cor_mom_z_756d_v167_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_756d_v168_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_756d_v168_signal},
    "f25_title_insur_cycle_revenue_mom_z_1008d_v169_signal": {"func": f25_title_insur_cycle_revenue_mom_z_1008d_v169_signal},
    "f25_title_insur_cycle_inventory_mom_z_1008d_v170_signal": {"func": f25_title_insur_cycle_inventory_mom_z_1008d_v170_signal},
    "f25_title_insur_cycle_cor_mom_z_1008d_v171_signal": {"func": f25_title_insur_cycle_cor_mom_z_1008d_v171_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_1008d_v172_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_1008d_v172_signal},
    "f25_title_insur_cycle_revenue_mom_z_1260d_v173_signal": {"func": f25_title_insur_cycle_revenue_mom_z_1260d_v173_signal},
    "f25_title_insur_cycle_inventory_mom_z_1260d_v174_signal": {"func": f25_title_insur_cycle_inventory_mom_z_1260d_v174_signal},
    "f25_title_insur_cycle_cor_mom_z_1260d_v175_signal": {"func": f25_title_insur_cycle_cor_mom_z_1260d_v175_signal},
    "f25_title_insur_cycle_revenue_cycle_mom_z_1260d_v176_signal": {"func": f25_title_insur_cycle_revenue_cycle_mom_z_1260d_v176_signal},
    "f25_title_insur_cycle_revenue_vol_slope_5d_v177_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_5d_v177_signal},
    "f25_title_insur_cycle_inventory_vol_slope_5d_v178_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_5d_v178_signal},
    "f25_title_insur_cycle_cor_vol_slope_5d_v179_signal": {"func": f25_title_insur_cycle_cor_vol_slope_5d_v179_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_5d_v180_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_5d_v180_signal},
    "f25_title_insur_cycle_revenue_vol_slope_10d_v181_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_10d_v181_signal},
    "f25_title_insur_cycle_inventory_vol_slope_10d_v182_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_10d_v182_signal},
    "f25_title_insur_cycle_cor_vol_slope_10d_v183_signal": {"func": f25_title_insur_cycle_cor_vol_slope_10d_v183_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_10d_v184_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_10d_v184_signal},
    "f25_title_insur_cycle_revenue_vol_slope_21d_v185_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_21d_v185_signal},
    "f25_title_insur_cycle_inventory_vol_slope_21d_v186_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_21d_v186_signal},
    "f25_title_insur_cycle_cor_vol_slope_21d_v187_signal": {"func": f25_title_insur_cycle_cor_vol_slope_21d_v187_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_21d_v188_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_21d_v188_signal},
    "f25_title_insur_cycle_revenue_vol_slope_42d_v189_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_42d_v189_signal},
    "f25_title_insur_cycle_inventory_vol_slope_42d_v190_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_42d_v190_signal},
    "f25_title_insur_cycle_cor_vol_slope_42d_v191_signal": {"func": f25_title_insur_cycle_cor_vol_slope_42d_v191_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_42d_v192_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_42d_v192_signal},
    "f25_title_insur_cycle_revenue_vol_slope_63d_v193_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_63d_v193_signal},
    "f25_title_insur_cycle_inventory_vol_slope_63d_v194_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_63d_v194_signal},
    "f25_title_insur_cycle_cor_vol_slope_63d_v195_signal": {"func": f25_title_insur_cycle_cor_vol_slope_63d_v195_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_63d_v196_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_63d_v196_signal},
    "f25_title_insur_cycle_revenue_vol_slope_126d_v197_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_126d_v197_signal},
    "f25_title_insur_cycle_inventory_vol_slope_126d_v198_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_126d_v198_signal},
    "f25_title_insur_cycle_cor_vol_slope_126d_v199_signal": {"func": f25_title_insur_cycle_cor_vol_slope_126d_v199_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_126d_v200_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_126d_v200_signal},
    "f25_title_insur_cycle_revenue_vol_slope_252d_v201_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_252d_v201_signal},
    "f25_title_insur_cycle_inventory_vol_slope_252d_v202_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_252d_v202_signal},
    "f25_title_insur_cycle_cor_vol_slope_252d_v203_signal": {"func": f25_title_insur_cycle_cor_vol_slope_252d_v203_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_252d_v204_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_252d_v204_signal},
    "f25_title_insur_cycle_revenue_vol_slope_504d_v205_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_504d_v205_signal},
    "f25_title_insur_cycle_inventory_vol_slope_504d_v206_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_504d_v206_signal},
    "f25_title_insur_cycle_cor_vol_slope_504d_v207_signal": {"func": f25_title_insur_cycle_cor_vol_slope_504d_v207_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_504d_v208_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_504d_v208_signal},
    "f25_title_insur_cycle_revenue_vol_slope_756d_v209_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_756d_v209_signal},
    "f25_title_insur_cycle_inventory_vol_slope_756d_v210_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_756d_v210_signal},
    "f25_title_insur_cycle_cor_vol_slope_756d_v211_signal": {"func": f25_title_insur_cycle_cor_vol_slope_756d_v211_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_756d_v212_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_756d_v212_signal},
    "f25_title_insur_cycle_revenue_vol_slope_1008d_v213_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_1008d_v213_signal},
    "f25_title_insur_cycle_inventory_vol_slope_1008d_v214_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_1008d_v214_signal},
    "f25_title_insur_cycle_cor_vol_slope_1008d_v215_signal": {"func": f25_title_insur_cycle_cor_vol_slope_1008d_v215_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_1008d_v216_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_1008d_v216_signal},
    "f25_title_insur_cycle_revenue_vol_slope_1260d_v217_signal": {"func": f25_title_insur_cycle_revenue_vol_slope_1260d_v217_signal},
    "f25_title_insur_cycle_inventory_vol_slope_1260d_v218_signal": {"func": f25_title_insur_cycle_inventory_vol_slope_1260d_v218_signal},
    "f25_title_insur_cycle_cor_vol_slope_1260d_v219_signal": {"func": f25_title_insur_cycle_cor_vol_slope_1260d_v219_signal},
    "f25_title_insur_cycle_revenue_cycle_vol_slope_1260d_v220_signal": {"func": f25_title_insur_cycle_revenue_cycle_vol_slope_1260d_v220_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_5d_v221_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_5d_v221_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_5d_v222_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_5d_v222_signal},
    "f25_title_insur_cycle_cor_ewma_slope_5d_v223_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_5d_v223_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_5d_v224_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_5d_v224_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_10d_v225_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_10d_v225_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_10d_v226_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_10d_v226_signal},
    "f25_title_insur_cycle_cor_ewma_slope_10d_v227_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_10d_v227_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_10d_v228_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_10d_v228_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_21d_v229_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_21d_v229_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_21d_v230_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_21d_v230_signal},
    "f25_title_insur_cycle_cor_ewma_slope_21d_v231_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_21d_v231_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_21d_v232_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_21d_v232_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_42d_v233_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_42d_v233_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_42d_v234_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_42d_v234_signal},
    "f25_title_insur_cycle_cor_ewma_slope_42d_v235_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_42d_v235_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_42d_v236_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_42d_v236_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_63d_v237_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_63d_v237_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_63d_v238_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_63d_v238_signal},
    "f25_title_insur_cycle_cor_ewma_slope_63d_v239_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_63d_v239_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_63d_v240_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_63d_v240_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_126d_v241_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_126d_v241_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_126d_v242_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_126d_v242_signal},
    "f25_title_insur_cycle_cor_ewma_slope_126d_v243_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_126d_v243_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_126d_v244_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_126d_v244_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_252d_v245_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_252d_v245_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_252d_v246_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_252d_v246_signal},
    "f25_title_insur_cycle_cor_ewma_slope_252d_v247_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_252d_v247_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_252d_v248_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_252d_v248_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_504d_v249_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_504d_v249_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_504d_v250_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_504d_v250_signal},
    "f25_title_insur_cycle_cor_ewma_slope_504d_v251_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_504d_v251_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_504d_v252_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_504d_v252_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_756d_v253_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_756d_v253_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_756d_v254_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_756d_v254_signal},
    "f25_title_insur_cycle_cor_ewma_slope_756d_v255_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_756d_v255_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_756d_v256_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_756d_v256_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_1008d_v257_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_1008d_v257_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_1008d_v258_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_1008d_v258_signal},
    "f25_title_insur_cycle_cor_ewma_slope_1008d_v259_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_1008d_v259_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_1008d_v260_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_1008d_v260_signal},
    "f25_title_insur_cycle_revenue_ewma_slope_1260d_v261_signal": {"func": f25_title_insur_cycle_revenue_ewma_slope_1260d_v261_signal},
    "f25_title_insur_cycle_inventory_ewma_slope_1260d_v262_signal": {"func": f25_title_insur_cycle_inventory_ewma_slope_1260d_v262_signal},
    "f25_title_insur_cycle_cor_ewma_slope_1260d_v263_signal": {"func": f25_title_insur_cycle_cor_ewma_slope_1260d_v263_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_slope_1260d_v264_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 25...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
