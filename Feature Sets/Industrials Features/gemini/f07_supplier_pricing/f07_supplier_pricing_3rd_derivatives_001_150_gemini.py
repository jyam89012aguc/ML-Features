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

def f07_supplier_pricing_grossmargin_slope_diff_norm_756d_v151_signal(grossmargin):
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_756d_v152_signal(cor):
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_756d_v153_signal(gp):
    res = (_slope_pct(gp, 756).diff(756) / _sma(gp.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_756d_v154_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 756).diff(756) / _sma(_ratio(cor, gp + cor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_756d_v155_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 756).diff(756) / _sma(_ratio(gp, cor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_1008d_v156_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_1008d_v157_signal(cor):
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_1008d_v158_signal(gp):
    res = (_slope_pct(gp, 1008).diff(1008) / _sma(gp.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_1008d_v159_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 1008).diff(1008) / _sma(_ratio(cor, gp + cor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_1008d_v160_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 1008).diff(1008) / _sma(_ratio(gp, cor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_1260d_v161_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_1260d_v162_signal(cor):
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_1260d_v163_signal(gp):
    res = (_slope_pct(gp, 1260).diff(1260) / _sma(gp.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_1260d_v164_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 1260).diff(1260) / _sma(_ratio(cor, gp + cor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_1260d_v165_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 1260).diff(1260) / _sma(_ratio(gp, cor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_5d_v166_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_5d_v167_signal(cor):
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_5d_v168_signal(gp):
    res = _z(_slope_pct(gp, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_5d_v169_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_5d_v170_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_10d_v171_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_10d_v172_signal(cor):
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_10d_v173_signal(gp):
    res = _z(_slope_pct(gp, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_10d_v174_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_10d_v175_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_21d_v176_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_21d_v177_signal(cor):
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_21d_v178_signal(gp):
    res = _z(_slope_pct(gp, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_21d_v179_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_21d_v180_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_42d_v181_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_42d_v182_signal(cor):
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_42d_v183_signal(gp):
    res = _z(_slope_pct(gp, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_42d_v184_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_42d_v185_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_63d_v186_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_63d_v187_signal(cor):
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_63d_v188_signal(gp):
    res = _z(_slope_pct(gp, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_63d_v189_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_63d_v190_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_126d_v191_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_126d_v192_signal(cor):
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_126d_v193_signal(gp):
    res = _z(_slope_pct(gp, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_126d_v194_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_126d_v195_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_252d_v196_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_252d_v197_signal(cor):
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_252d_v198_signal(gp):
    res = _z(_slope_pct(gp, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_252d_v199_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_252d_v200_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_504d_v201_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_504d_v202_signal(cor):
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_504d_v203_signal(gp):
    res = _z(_slope_pct(gp, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_504d_v204_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_504d_v205_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_756d_v206_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_756d_v207_signal(cor):
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_756d_v208_signal(gp):
    res = _z(_slope_pct(gp, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_756d_v209_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_756d_v210_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_1008d_v211_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_1008d_v212_signal(cor):
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_1008d_v213_signal(gp):
    res = _z(_slope_pct(gp, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_1008d_v214_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_1008d_v215_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_mom_z_1260d_v216_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_mom_z_1260d_v217_signal(cor):
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_mom_z_1260d_v218_signal(gp):
    res = _z(_slope_pct(gp, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_mom_z_1260d_v219_signal(cor, gp):
    res = _z(_slope_pct(_ratio(cor, gp + cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_mom_z_1260d_v220_signal(gp, cor):
    res = _z(_slope_pct(_ratio(gp, cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_5d_v221_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_5d_v222_signal(cor):
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_5d_v223_signal(gp):
    res = _std(_slope_pct(gp, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_5d_v224_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_5d_v225_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_10d_v226_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_10d_v227_signal(cor):
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_10d_v228_signal(gp):
    res = _std(_slope_pct(gp, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_10d_v229_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_10d_v230_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_21d_v231_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_21d_v232_signal(cor):
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_21d_v233_signal(gp):
    res = _std(_slope_pct(gp, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_21d_v234_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_21d_v235_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_42d_v236_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_42d_v237_signal(cor):
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_42d_v238_signal(gp):
    res = _std(_slope_pct(gp, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_42d_v239_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_42d_v240_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_63d_v241_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_63d_v242_signal(cor):
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_63d_v243_signal(gp):
    res = _std(_slope_pct(gp, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_63d_v244_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_63d_v245_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_126d_v246_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_126d_v247_signal(cor):
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_126d_v248_signal(gp):
    res = _std(_slope_pct(gp, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_126d_v249_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_126d_v250_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_252d_v251_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_252d_v252_signal(cor):
    res = _std(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_252d_v253_signal(gp):
    res = _std(_slope_pct(gp, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_252d_v254_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_252d_v255_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_504d_v256_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_504d_v257_signal(cor):
    res = _std(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_504d_v258_signal(gp):
    res = _std(_slope_pct(gp, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_504d_v259_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_504d_v260_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_756d_v261_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_756d_v262_signal(cor):
    res = _std(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_756d_v263_signal(gp):
    res = _std(_slope_pct(gp, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_756d_v264_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_756d_v265_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_1008d_v266_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_1008d_v267_signal(cor):
    res = _std(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_1008d_v268_signal(gp):
    res = _std(_slope_pct(gp, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_1008d_v269_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_1008d_v270_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_vol_slope_1260d_v271_signal(grossmargin):
    res = _std(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_vol_slope_1260d_v272_signal(cor):
    res = _std(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_vol_slope_1260d_v273_signal(gp):
    res = _std(_slope_pct(gp, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_vol_slope_1260d_v274_signal(cor, gp):
    res = _std(_slope_pct(_ratio(cor, gp + cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_vol_slope_1260d_v275_signal(gp, cor):
    res = _std(_slope_pct(_ratio(gp, cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "gp": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 07...")
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
