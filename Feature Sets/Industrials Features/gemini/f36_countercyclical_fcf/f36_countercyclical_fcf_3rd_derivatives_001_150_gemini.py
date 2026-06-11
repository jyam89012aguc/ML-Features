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

def f36_countercyclical_fcf_fcf_slope_diff_norm_756d_v151_signal(fcf):
    res = (_slope_pct(fcf, 756).diff(756) / _sma(fcf.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_slope_diff_norm_756d_v152_signal(netinc):
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_slope_diff_norm_756d_v153_signal(ebitda):
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_slope_diff_norm_756d_v154_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 756).diff(756) / _sma(_ratio(fcf, netinc).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_slope_diff_norm_756d_v155_signal(fcf, ebitda):
    res = (_slope_pct(_ratio(fcf, ebitda), 756).diff(756) / _sma(_ratio(fcf, ebitda).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_slope_diff_norm_1008d_v156_signal(fcf):
    res = (_slope_pct(fcf, 1008).diff(1008) / _sma(fcf.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_slope_diff_norm_1008d_v157_signal(netinc):
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_slope_diff_norm_1008d_v158_signal(ebitda):
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_slope_diff_norm_1008d_v159_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 1008).diff(1008) / _sma(_ratio(fcf, netinc).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_slope_diff_norm_1008d_v160_signal(fcf, ebitda):
    res = (_slope_pct(_ratio(fcf, ebitda), 1008).diff(1008) / _sma(_ratio(fcf, ebitda).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_slope_diff_norm_1260d_v161_signal(fcf):
    res = (_slope_pct(fcf, 1260).diff(1260) / _sma(fcf.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_slope_diff_norm_1260d_v162_signal(netinc):
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_slope_diff_norm_1260d_v163_signal(ebitda):
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_slope_diff_norm_1260d_v164_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 1260).diff(1260) / _sma(_ratio(fcf, netinc).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_slope_diff_norm_1260d_v165_signal(fcf, ebitda):
    res = (_slope_pct(_ratio(fcf, ebitda), 1260).diff(1260) / _sma(_ratio(fcf, ebitda).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_5d_v166_signal(fcf):
    res = _z(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_5d_v167_signal(netinc):
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_5d_v168_signal(ebitda):
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_5d_v169_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_5d_v170_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_10d_v171_signal(fcf):
    res = _z(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_10d_v172_signal(netinc):
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_10d_v173_signal(ebitda):
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_10d_v174_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_10d_v175_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_21d_v176_signal(fcf):
    res = _z(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_21d_v177_signal(netinc):
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_21d_v178_signal(ebitda):
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_21d_v179_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_21d_v180_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_42d_v181_signal(fcf):
    res = _z(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_42d_v182_signal(netinc):
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_42d_v183_signal(ebitda):
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_42d_v184_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_42d_v185_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_63d_v186_signal(fcf):
    res = _z(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_63d_v187_signal(netinc):
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_63d_v188_signal(ebitda):
    res = _z(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_63d_v189_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_63d_v190_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_126d_v191_signal(fcf):
    res = _z(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_126d_v192_signal(netinc):
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_126d_v193_signal(ebitda):
    res = _z(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_126d_v194_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_126d_v195_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_252d_v196_signal(fcf):
    res = _z(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_252d_v197_signal(netinc):
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_252d_v198_signal(ebitda):
    res = _z(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_252d_v199_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_252d_v200_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_504d_v201_signal(fcf):
    res = _z(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_504d_v202_signal(netinc):
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_504d_v203_signal(ebitda):
    res = _z(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_504d_v204_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_504d_v205_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_756d_v206_signal(fcf):
    res = _z(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_756d_v207_signal(netinc):
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_756d_v208_signal(ebitda):
    res = _z(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_756d_v209_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_756d_v210_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_1008d_v211_signal(fcf):
    res = _z(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_1008d_v212_signal(netinc):
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_1008d_v213_signal(ebitda):
    res = _z(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_1008d_v214_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_1008d_v215_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_mom_z_1260d_v216_signal(fcf):
    res = _z(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_mom_z_1260d_v217_signal(netinc):
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_mom_z_1260d_v218_signal(ebitda):
    res = _z(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_mom_z_1260d_v219_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_mom_z_1260d_v220_signal(fcf, ebitda):
    res = _z(_slope_pct(_ratio(fcf, ebitda), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_5d_v221_signal(fcf):
    res = _std(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_5d_v222_signal(netinc):
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_5d_v223_signal(ebitda):
    res = _std(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_5d_v224_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_5d_v225_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_10d_v226_signal(fcf):
    res = _std(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_10d_v227_signal(netinc):
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_10d_v228_signal(ebitda):
    res = _std(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_10d_v229_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_10d_v230_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_21d_v231_signal(fcf):
    res = _std(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_21d_v232_signal(netinc):
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_21d_v233_signal(ebitda):
    res = _std(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_21d_v234_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_21d_v235_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_42d_v236_signal(fcf):
    res = _std(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_42d_v237_signal(netinc):
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_42d_v238_signal(ebitda):
    res = _std(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_42d_v239_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_42d_v240_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_63d_v241_signal(fcf):
    res = _std(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_63d_v242_signal(netinc):
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_63d_v243_signal(ebitda):
    res = _std(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_63d_v244_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_63d_v245_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_126d_v246_signal(fcf):
    res = _std(_slope_pct(fcf, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_126d_v247_signal(netinc):
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_126d_v248_signal(ebitda):
    res = _std(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_126d_v249_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_126d_v250_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_252d_v251_signal(fcf):
    res = _std(_slope_pct(fcf, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_252d_v252_signal(netinc):
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_252d_v253_signal(ebitda):
    res = _std(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_252d_v254_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_252d_v255_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_504d_v256_signal(fcf):
    res = _std(_slope_pct(fcf, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_504d_v257_signal(netinc):
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_504d_v258_signal(ebitda):
    res = _std(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_504d_v259_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_504d_v260_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_756d_v261_signal(fcf):
    res = _std(_slope_pct(fcf, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_756d_v262_signal(netinc):
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_756d_v263_signal(ebitda):
    res = _std(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_756d_v264_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_756d_v265_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_1008d_v266_signal(fcf):
    res = _std(_slope_pct(fcf, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_1008d_v267_signal(netinc):
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_1008d_v268_signal(ebitda):
    res = _std(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_1008d_v269_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_1008d_v270_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_vol_slope_1260d_v271_signal(fcf):
    res = _std(_slope_pct(fcf, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_netinc_vol_slope_1260d_v272_signal(netinc):
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_ebitda_vol_slope_1260d_v273_signal(ebitda):
    res = _std(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_conversion_vol_slope_1260d_v274_signal(fcf, netinc):
    res = _std(_slope_pct(_ratio(fcf, netinc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_countercyclical_fcf_fcf_yield_vol_slope_1260d_v275_signal(fcf, ebitda):
    res = _std(_slope_pct(_ratio(fcf, ebitda), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 36...")
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
