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

def f01_backlog_conversion_deferredrev_slope_diff_norm_42d_v151_signal(deferredrev):
    res = (_slope_pct(deferredrev, 42).diff(42) / _sma(deferredrev.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_42d_v152_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_42d_v153_signal(marketcap):
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_42d_v154_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 42).diff(42) / _sma(_ratio(deferredrev, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_42d_v155_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 42).diff(42) / _sma(_ratio(revenue, deferredrev).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_42d_v156_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 42).diff(42) / _sma(_ratio(deferredrev, marketcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_63d_v157_signal(deferredrev):
    res = (_slope_pct(deferredrev, 63).diff(63) / _sma(deferredrev.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_63d_v158_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_63d_v159_signal(marketcap):
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_63d_v160_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 63).diff(63) / _sma(_ratio(deferredrev, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_63d_v161_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 63).diff(63) / _sma(_ratio(revenue, deferredrev).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_63d_v162_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 63).diff(63) / _sma(_ratio(deferredrev, marketcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_126d_v163_signal(deferredrev):
    res = (_slope_pct(deferredrev, 126).diff(126) / _sma(deferredrev.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_126d_v164_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_126d_v165_signal(marketcap):
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_126d_v166_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 126).diff(126) / _sma(_ratio(deferredrev, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_126d_v167_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 126).diff(126) / _sma(_ratio(revenue, deferredrev).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_126d_v168_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 126).diff(126) / _sma(_ratio(deferredrev, marketcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_252d_v169_signal(deferredrev):
    res = (_slope_pct(deferredrev, 252).diff(252) / _sma(deferredrev.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_252d_v170_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_252d_v171_signal(marketcap):
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_252d_v172_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 252).diff(252) / _sma(_ratio(deferredrev, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_252d_v173_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 252).diff(252) / _sma(_ratio(revenue, deferredrev).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_252d_v174_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 252).diff(252) / _sma(_ratio(deferredrev, marketcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_504d_v175_signal(deferredrev):
    res = (_slope_pct(deferredrev, 504).diff(504) / _sma(deferredrev.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_504d_v176_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_504d_v177_signal(marketcap):
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_504d_v178_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 504).diff(504) / _sma(_ratio(deferredrev, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_504d_v179_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 504).diff(504) / _sma(_ratio(revenue, deferredrev).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_504d_v180_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 504).diff(504) / _sma(_ratio(deferredrev, marketcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_756d_v181_signal(deferredrev):
    res = (_slope_pct(deferredrev, 756).diff(756) / _sma(deferredrev.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_756d_v182_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_756d_v183_signal(marketcap):
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_756d_v184_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 756).diff(756) / _sma(_ratio(deferredrev, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_756d_v185_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 756).diff(756) / _sma(_ratio(revenue, deferredrev).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_756d_v186_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 756).diff(756) / _sma(_ratio(deferredrev, marketcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_1008d_v187_signal(deferredrev):
    res = (_slope_pct(deferredrev, 1008).diff(1008) / _sma(deferredrev.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_1008d_v188_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_1008d_v189_signal(marketcap):
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_1008d_v190_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 1008).diff(1008) / _sma(_ratio(deferredrev, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_1008d_v191_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 1008).diff(1008) / _sma(_ratio(revenue, deferredrev).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_1008d_v192_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 1008).diff(1008) / _sma(_ratio(deferredrev, marketcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_1260d_v193_signal(deferredrev):
    res = (_slope_pct(deferredrev, 1260).diff(1260) / _sma(deferredrev.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_1260d_v194_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_1260d_v195_signal(marketcap):
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_1260d_v196_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 1260).diff(1260) / _sma(_ratio(deferredrev, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_1260d_v197_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 1260).diff(1260) / _sma(_ratio(revenue, deferredrev).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_1260d_v198_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 1260).diff(1260) / _sma(_ratio(deferredrev, marketcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_5d_v199_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_5d_v200_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_5d_v201_signal(marketcap):
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_5d_v202_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_5d_v203_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_5d_v204_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_10d_v205_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_10d_v206_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_10d_v207_signal(marketcap):
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_10d_v208_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_10d_v209_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_10d_v210_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_21d_v211_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_21d_v212_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_21d_v213_signal(marketcap):
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_21d_v214_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_21d_v215_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_21d_v216_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_42d_v217_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_42d_v218_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_42d_v219_signal(marketcap):
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_42d_v220_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_42d_v221_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_42d_v222_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_63d_v223_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_63d_v224_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_63d_v225_signal(marketcap):
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_63d_v226_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_63d_v227_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_63d_v228_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_126d_v229_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_126d_v230_signal(revenue):
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_126d_v231_signal(marketcap):
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_126d_v232_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_126d_v233_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_126d_v234_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_252d_v235_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_252d_v236_signal(revenue):
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_252d_v237_signal(marketcap):
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_252d_v238_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_252d_v239_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_252d_v240_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_504d_v241_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_504d_v242_signal(revenue):
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_504d_v243_signal(marketcap):
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_504d_v244_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_504d_v245_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_504d_v246_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_756d_v247_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_756d_v248_signal(revenue):
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_756d_v249_signal(marketcap):
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_756d_v250_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_756d_v251_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_756d_v252_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_1008d_v253_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_1008d_v254_signal(revenue):
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_1008d_v255_signal(marketcap):
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_1008d_v256_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_1008d_v257_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_1008d_v258_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_mom_z_1260d_v259_signal(deferredrev):
    res = _z(_slope_pct(deferredrev, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_mom_z_1260d_v260_signal(revenue):
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_mom_z_1260d_v261_signal(marketcap):
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_mom_z_1260d_v262_signal(deferredrev, revenue):
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_mom_z_1260d_v263_signal(revenue, deferredrev):
    res = _z(_slope_pct(_ratio(revenue, deferredrev), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_mom_z_1260d_v264_signal(deferredrev, marketcap):
    res = _z(_slope_pct(_ratio(deferredrev, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_vol_slope_5d_v265_signal(deferredrev):
    res = _std(_slope_pct(deferredrev, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_vol_slope_5d_v266_signal(revenue):
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_vol_slope_5d_v267_signal(marketcap):
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_vol_slope_5d_v268_signal(deferredrev, revenue):
    res = _std(_slope_pct(_ratio(deferredrev, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_vol_slope_5d_v269_signal(revenue, deferredrev):
    res = _std(_slope_pct(_ratio(revenue, deferredrev), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_vol_slope_5d_v270_signal(deferredrev, marketcap):
    res = _std(_slope_pct(_ratio(deferredrev, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_vol_slope_10d_v271_signal(deferredrev):
    res = _std(_slope_pct(deferredrev, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_vol_slope_10d_v272_signal(revenue):
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_vol_slope_10d_v273_signal(marketcap):
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_vol_slope_10d_v274_signal(deferredrev, revenue):
    res = _std(_slope_pct(_ratio(deferredrev, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_vol_slope_10d_v275_signal(revenue, deferredrev):
    res = _std(_slope_pct(_ratio(revenue, deferredrev), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_vol_slope_10d_v276_signal(deferredrev, marketcap):
    res = _std(_slope_pct(_ratio(deferredrev, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_vol_slope_21d_v277_signal(deferredrev):
    res = _std(_slope_pct(deferredrev, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_vol_slope_21d_v278_signal(revenue):
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_vol_slope_21d_v279_signal(marketcap):
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_vol_slope_21d_v280_signal(deferredrev, revenue):
    res = _std(_slope_pct(_ratio(deferredrev, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_vol_slope_21d_v281_signal(revenue, deferredrev):
    res = _std(_slope_pct(_ratio(revenue, deferredrev), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_vol_slope_21d_v282_signal(deferredrev, marketcap):
    res = _std(_slope_pct(_ratio(deferredrev, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_vol_slope_42d_v283_signal(deferredrev):
    res = _std(_slope_pct(deferredrev, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_vol_slope_42d_v284_signal(revenue):
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_vol_slope_42d_v285_signal(marketcap):
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_vol_slope_42d_v286_signal(deferredrev, revenue):
    res = _std(_slope_pct(_ratio(deferredrev, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_vol_slope_42d_v287_signal(revenue, deferredrev):
    res = _std(_slope_pct(_ratio(revenue, deferredrev), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_vol_slope_42d_v288_signal(deferredrev, marketcap):
    res = _std(_slope_pct(_ratio(deferredrev, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_vol_slope_63d_v289_signal(deferredrev):
    res = _std(_slope_pct(deferredrev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_vol_slope_63d_v290_signal(revenue):
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_vol_slope_63d_v291_signal(marketcap):
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_vol_slope_63d_v292_signal(deferredrev, revenue):
    res = _std(_slope_pct(_ratio(deferredrev, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_vol_slope_63d_v293_signal(revenue, deferredrev):
    res = _std(_slope_pct(_ratio(revenue, deferredrev), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_vol_slope_63d_v294_signal(deferredrev, marketcap):
    res = _std(_slope_pct(_ratio(deferredrev, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_vol_slope_126d_v295_signal(deferredrev):
    res = _std(_slope_pct(deferredrev, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_vol_slope_126d_v296_signal(revenue):
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_vol_slope_126d_v297_signal(marketcap):
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_vol_slope_126d_v298_signal(deferredrev, revenue):
    res = _std(_slope_pct(_ratio(deferredrev, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_vol_slope_126d_v299_signal(revenue, deferredrev):
    res = _std(_slope_pct(_ratio(revenue, deferredrev), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_vol_slope_126d_v300_signal(deferredrev, marketcap):
    res = _std(_slope_pct(_ratio(deferredrev, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 01...")
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
