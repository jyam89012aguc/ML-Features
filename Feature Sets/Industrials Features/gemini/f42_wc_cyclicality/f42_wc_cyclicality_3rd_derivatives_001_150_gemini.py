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

def f42_wc_cyclicality_inventory_slope_diff_norm_756d_v151_signal(inventory):
    res = (_slope_pct(inventory, 756).diff(756) / _sma(inventory.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_756d_v152_signal(receivables):
    res = (_slope_pct(receivables, 756).diff(756) / _sma(receivables.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_756d_v153_signal(payables):
    res = (_slope_pct(payables, 756).diff(756) / _sma(payables.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_756d_v154_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_756d_v155_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 756).diff(756) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_1008d_v156_signal(inventory):
    res = (_slope_pct(inventory, 1008).diff(1008) / _sma(inventory.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_1008d_v157_signal(receivables):
    res = (_slope_pct(receivables, 1008).diff(1008) / _sma(receivables.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_1008d_v158_signal(payables):
    res = (_slope_pct(payables, 1008).diff(1008) / _sma(payables.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_1008d_v159_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_1008d_v160_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 1008).diff(1008) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_1260d_v161_signal(inventory):
    res = (_slope_pct(inventory, 1260).diff(1260) / _sma(inventory.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_1260d_v162_signal(receivables):
    res = (_slope_pct(receivables, 1260).diff(1260) / _sma(receivables.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_1260d_v163_signal(payables):
    res = (_slope_pct(payables, 1260).diff(1260) / _sma(payables.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_1260d_v164_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_1260d_v165_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 1260).diff(1260) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_5d_v166_signal(inventory):
    res = _z(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_5d_v167_signal(receivables):
    res = _z(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_5d_v168_signal(payables):
    res = _z(_slope_pct(payables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_5d_v169_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_5d_v170_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_10d_v171_signal(inventory):
    res = _z(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_10d_v172_signal(receivables):
    res = _z(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_10d_v173_signal(payables):
    res = _z(_slope_pct(payables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_10d_v174_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_10d_v175_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_21d_v176_signal(inventory):
    res = _z(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_21d_v177_signal(receivables):
    res = _z(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_21d_v178_signal(payables):
    res = _z(_slope_pct(payables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_21d_v179_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_21d_v180_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_42d_v181_signal(inventory):
    res = _z(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_42d_v182_signal(receivables):
    res = _z(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_42d_v183_signal(payables):
    res = _z(_slope_pct(payables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_42d_v184_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_42d_v185_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_63d_v186_signal(inventory):
    res = _z(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_63d_v187_signal(receivables):
    res = _z(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_63d_v188_signal(payables):
    res = _z(_slope_pct(payables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_63d_v189_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_63d_v190_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_126d_v191_signal(inventory):
    res = _z(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_126d_v192_signal(receivables):
    res = _z(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_126d_v193_signal(payables):
    res = _z(_slope_pct(payables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_126d_v194_signal(revenue):
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_126d_v195_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_252d_v196_signal(inventory):
    res = _z(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_252d_v197_signal(receivables):
    res = _z(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_252d_v198_signal(payables):
    res = _z(_slope_pct(payables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_252d_v199_signal(revenue):
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_252d_v200_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_504d_v201_signal(inventory):
    res = _z(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_504d_v202_signal(receivables):
    res = _z(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_504d_v203_signal(payables):
    res = _z(_slope_pct(payables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_504d_v204_signal(revenue):
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_504d_v205_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_756d_v206_signal(inventory):
    res = _z(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_756d_v207_signal(receivables):
    res = _z(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_756d_v208_signal(payables):
    res = _z(_slope_pct(payables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_756d_v209_signal(revenue):
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_756d_v210_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_1008d_v211_signal(inventory):
    res = _z(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_1008d_v212_signal(receivables):
    res = _z(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_1008d_v213_signal(payables):
    res = _z(_slope_pct(payables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_1008d_v214_signal(revenue):
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_1008d_v215_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_mom_z_1260d_v216_signal(inventory):
    res = _z(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_mom_z_1260d_v217_signal(receivables):
    res = _z(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_mom_z_1260d_v218_signal(payables):
    res = _z(_slope_pct(payables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_mom_z_1260d_v219_signal(revenue):
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_mom_z_1260d_v220_signal(inventory, receivables, payables, revenue):
    res = _z(_slope_pct(_ratio(inventory + receivables - payables, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_5d_v221_signal(inventory):
    res = _std(_slope_pct(inventory, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_5d_v222_signal(receivables):
    res = _std(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_5d_v223_signal(payables):
    res = _std(_slope_pct(payables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_5d_v224_signal(revenue):
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_5d_v225_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_10d_v226_signal(inventory):
    res = _std(_slope_pct(inventory, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_10d_v227_signal(receivables):
    res = _std(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_10d_v228_signal(payables):
    res = _std(_slope_pct(payables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_10d_v229_signal(revenue):
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_10d_v230_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_21d_v231_signal(inventory):
    res = _std(_slope_pct(inventory, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_21d_v232_signal(receivables):
    res = _std(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_21d_v233_signal(payables):
    res = _std(_slope_pct(payables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_21d_v234_signal(revenue):
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_21d_v235_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_42d_v236_signal(inventory):
    res = _std(_slope_pct(inventory, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_42d_v237_signal(receivables):
    res = _std(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_42d_v238_signal(payables):
    res = _std(_slope_pct(payables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_42d_v239_signal(revenue):
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_42d_v240_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_63d_v241_signal(inventory):
    res = _std(_slope_pct(inventory, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_63d_v242_signal(receivables):
    res = _std(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_63d_v243_signal(payables):
    res = _std(_slope_pct(payables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_63d_v244_signal(revenue):
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_63d_v245_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_126d_v246_signal(inventory):
    res = _std(_slope_pct(inventory, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_126d_v247_signal(receivables):
    res = _std(_slope_pct(receivables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_126d_v248_signal(payables):
    res = _std(_slope_pct(payables, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_126d_v249_signal(revenue):
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_126d_v250_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_252d_v251_signal(inventory):
    res = _std(_slope_pct(inventory, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_252d_v252_signal(receivables):
    res = _std(_slope_pct(receivables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_252d_v253_signal(payables):
    res = _std(_slope_pct(payables, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_252d_v254_signal(revenue):
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_252d_v255_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_504d_v256_signal(inventory):
    res = _std(_slope_pct(inventory, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_504d_v257_signal(receivables):
    res = _std(_slope_pct(receivables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_504d_v258_signal(payables):
    res = _std(_slope_pct(payables, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_504d_v259_signal(revenue):
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_504d_v260_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_756d_v261_signal(inventory):
    res = _std(_slope_pct(inventory, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_756d_v262_signal(receivables):
    res = _std(_slope_pct(receivables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_756d_v263_signal(payables):
    res = _std(_slope_pct(payables, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_756d_v264_signal(revenue):
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_756d_v265_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_1008d_v266_signal(inventory):
    res = _std(_slope_pct(inventory, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_1008d_v267_signal(receivables):
    res = _std(_slope_pct(receivables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_1008d_v268_signal(payables):
    res = _std(_slope_pct(payables, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_1008d_v269_signal(revenue):
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_1008d_v270_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_vol_slope_1260d_v271_signal(inventory):
    res = _std(_slope_pct(inventory, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_vol_slope_1260d_v272_signal(receivables):
    res = _std(_slope_pct(receivables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_vol_slope_1260d_v273_signal(payables):
    res = _std(_slope_pct(payables, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_vol_slope_1260d_v274_signal(revenue):
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_vol_slope_1260d_v275_signal(inventory, receivables, payables, revenue):
    res = _std(_slope_pct(_ratio(inventory + receivables - payables, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 42...")
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
