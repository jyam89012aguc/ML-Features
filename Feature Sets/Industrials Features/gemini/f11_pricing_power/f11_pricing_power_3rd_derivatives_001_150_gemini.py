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

def f11_pricing_power_grossmargin_slope_diff_norm_756d_v151_signal(grossmargin):
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_slope_diff_norm_756d_v152_signal(cor):
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_slope_diff_norm_756d_v153_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_slope_diff_norm_756d_v154_signal(grossmargin):
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_slope_diff_norm_756d_v155_signal(grossmargin, cor):
    res = (_slope_pct(_ratio(grossmargin, cor), 756).diff(756) / _sma(_ratio(grossmargin, cor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_slope_diff_norm_1008d_v156_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_slope_diff_norm_1008d_v157_signal(cor):
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_slope_diff_norm_1008d_v158_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_slope_diff_norm_1008d_v159_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_slope_diff_norm_1008d_v160_signal(grossmargin, cor):
    res = (_slope_pct(_ratio(grossmargin, cor), 1008).diff(1008) / _sma(_ratio(grossmargin, cor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_slope_diff_norm_1260d_v161_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_slope_diff_norm_1260d_v162_signal(cor):
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_slope_diff_norm_1260d_v163_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_slope_diff_norm_1260d_v164_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_slope_diff_norm_1260d_v165_signal(grossmargin, cor):
    res = (_slope_pct(_ratio(grossmargin, cor), 1260).diff(1260) / _sma(_ratio(grossmargin, cor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_5d_v166_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_5d_v167_signal(cor):
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_5d_v168_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_5d_v169_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_5d_v170_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_10d_v171_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_10d_v172_signal(cor):
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_10d_v173_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_10d_v174_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_10d_v175_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_21d_v176_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_21d_v177_signal(cor):
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_21d_v178_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_21d_v179_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_21d_v180_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_42d_v181_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_42d_v182_signal(cor):
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_42d_v183_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_42d_v184_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_42d_v185_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_63d_v186_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_63d_v187_signal(cor):
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_63d_v188_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_63d_v189_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_63d_v190_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_126d_v191_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_126d_v192_signal(cor):
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_126d_v193_signal(revenue):
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_126d_v194_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_126d_v195_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_252d_v196_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_252d_v197_signal(cor):
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_252d_v198_signal(revenue):
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_252d_v199_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_252d_v200_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_504d_v201_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_504d_v202_signal(cor):
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_504d_v203_signal(revenue):
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_504d_v204_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_504d_v205_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_756d_v206_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_756d_v207_signal(cor):
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_756d_v208_signal(revenue):
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_756d_v209_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_756d_v210_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_1008d_v211_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_1008d_v212_signal(cor):
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_1008d_v213_signal(revenue):
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_1008d_v214_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_1008d_v215_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_mom_z_1260d_v216_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_mom_z_1260d_v217_signal(cor):
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_mom_z_1260d_v218_signal(revenue):
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_mom_z_1260d_v219_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_mom_z_1260d_v220_signal(grossmargin, cor):
    res = _z(_slope_pct(_ratio(grossmargin, cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_5d_v221_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_5d_v222_signal(cor):
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_5d_v223_signal(revenue):
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_5d_v224_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_5d_v225_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_10d_v226_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_10d_v227_signal(cor):
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_10d_v228_signal(revenue):
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_10d_v229_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_10d_v230_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_21d_v231_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_21d_v232_signal(cor):
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_21d_v233_signal(revenue):
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_21d_v234_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_21d_v235_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_42d_v236_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_42d_v237_signal(cor):
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_42d_v238_signal(revenue):
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_42d_v239_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_42d_v240_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_63d_v241_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_63d_v242_signal(cor):
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_63d_v243_signal(revenue):
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_63d_v244_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_63d_v245_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_126d_v246_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_126d_v247_signal(cor):
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_126d_v248_signal(revenue):
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_126d_v249_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_126d_v250_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_252d_v251_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_252d_v252_signal(cor):
    res = _std(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_252d_v253_signal(revenue):
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_252d_v254_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_252d_v255_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_504d_v256_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_504d_v257_signal(cor):
    res = _std(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_504d_v258_signal(revenue):
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_504d_v259_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_504d_v260_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_756d_v261_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_756d_v262_signal(cor):
    res = _std(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_756d_v263_signal(revenue):
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_756d_v264_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_756d_v265_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_1008d_v266_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_1008d_v267_signal(cor):
    res = _std(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_1008d_v268_signal(revenue):
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_1008d_v269_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_1008d_v270_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_grossmargin_vol_slope_1260d_v271_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_cor_vol_slope_1260d_v272_signal(cor):
    res = _std(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_revenue_vol_slope_1260d_v273_signal(revenue):
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_gross_margin_vol_slope_1260d_v274_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_pricing_power_margin_vs_cost_vol_slope_1260d_v275_signal(grossmargin, cor):
    res = _std(_slope_pct(_ratio(grossmargin, cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 11...")
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
