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

def f50_insider_ltip_sbcomp_slope_diff_norm_756d_v151_signal(sbcomp):
    res = (_slope_pct(sbcomp, 756).diff(756) / _sma(sbcomp.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_756d_v152_signal(shareswa):
    res = (_slope_pct(shareswa, 756).diff(756) / _sma(shareswa.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_756d_v153_signal(netinc):
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_756d_v154_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 756).diff(756) / _sma(_ratio(sbcomp, netinc).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_756d_v155_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 756).diff(756) / _sma(_ratio(sbcomp, shareswa).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_1008d_v156_signal(sbcomp):
    res = (_slope_pct(sbcomp, 1008).diff(1008) / _sma(sbcomp.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_1008d_v157_signal(shareswa):
    res = (_slope_pct(shareswa, 1008).diff(1008) / _sma(shareswa.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_1008d_v158_signal(netinc):
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_1008d_v159_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 1008).diff(1008) / _sma(_ratio(sbcomp, netinc).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_1008d_v160_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 1008).diff(1008) / _sma(_ratio(sbcomp, shareswa).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_slope_diff_norm_1260d_v161_signal(sbcomp):
    res = (_slope_pct(sbcomp, 1260).diff(1260) / _sma(sbcomp.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_slope_diff_norm_1260d_v162_signal(shareswa):
    res = (_slope_pct(shareswa, 1260).diff(1260) / _sma(shareswa.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_slope_diff_norm_1260d_v163_signal(netinc):
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_slope_diff_norm_1260d_v164_signal(sbcomp, netinc):
    res = (_slope_pct(_ratio(sbcomp, netinc), 1260).diff(1260) / _sma(_ratio(sbcomp, netinc).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_slope_diff_norm_1260d_v165_signal(sbcomp, shareswa):
    res = (_slope_pct(_ratio(sbcomp, shareswa), 1260).diff(1260) / _sma(_ratio(sbcomp, shareswa).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_5d_v166_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_5d_v167_signal(shareswa):
    res = _z(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_5d_v168_signal(netinc):
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_5d_v169_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_5d_v170_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_10d_v171_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_10d_v172_signal(shareswa):
    res = _z(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_10d_v173_signal(netinc):
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_10d_v174_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_10d_v175_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_21d_v176_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_21d_v177_signal(shareswa):
    res = _z(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_21d_v178_signal(netinc):
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_21d_v179_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_21d_v180_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_42d_v181_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_42d_v182_signal(shareswa):
    res = _z(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_42d_v183_signal(netinc):
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_42d_v184_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_42d_v185_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_63d_v186_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_63d_v187_signal(shareswa):
    res = _z(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_63d_v188_signal(netinc):
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_63d_v189_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_63d_v190_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_126d_v191_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_126d_v192_signal(shareswa):
    res = _z(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_126d_v193_signal(netinc):
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_126d_v194_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_126d_v195_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_252d_v196_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_252d_v197_signal(shareswa):
    res = _z(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_252d_v198_signal(netinc):
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_252d_v199_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_252d_v200_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_504d_v201_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_504d_v202_signal(shareswa):
    res = _z(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_504d_v203_signal(netinc):
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_504d_v204_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_504d_v205_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_756d_v206_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_756d_v207_signal(shareswa):
    res = _z(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_756d_v208_signal(netinc):
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_756d_v209_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_756d_v210_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_1008d_v211_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_1008d_v212_signal(shareswa):
    res = _z(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_1008d_v213_signal(netinc):
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_1008d_v214_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_1008d_v215_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_mom_z_1260d_v216_signal(sbcomp):
    res = _z(_slope_pct(sbcomp, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_mom_z_1260d_v217_signal(shareswa):
    res = _z(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_mom_z_1260d_v218_signal(netinc):
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_mom_z_1260d_v219_signal(sbcomp, netinc):
    res = _z(_slope_pct(_ratio(sbcomp, netinc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_mom_z_1260d_v220_signal(sbcomp, shareswa):
    res = _z(_slope_pct(_ratio(sbcomp, shareswa), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_5d_v221_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_5d_v222_signal(shareswa):
    res = _std(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_5d_v223_signal(netinc):
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_5d_v224_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_5d_v225_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_10d_v226_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_10d_v227_signal(shareswa):
    res = _std(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_10d_v228_signal(netinc):
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_10d_v229_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_10d_v230_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_21d_v231_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_21d_v232_signal(shareswa):
    res = _std(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_21d_v233_signal(netinc):
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_21d_v234_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_21d_v235_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_42d_v236_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_42d_v237_signal(shareswa):
    res = _std(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_42d_v238_signal(netinc):
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_42d_v239_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_42d_v240_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_63d_v241_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_63d_v242_signal(shareswa):
    res = _std(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_63d_v243_signal(netinc):
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_63d_v244_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_63d_v245_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_126d_v246_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_126d_v247_signal(shareswa):
    res = _std(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_126d_v248_signal(netinc):
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_126d_v249_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_126d_v250_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_252d_v251_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_252d_v252_signal(shareswa):
    res = _std(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_252d_v253_signal(netinc):
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_252d_v254_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_252d_v255_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_504d_v256_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_504d_v257_signal(shareswa):
    res = _std(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_504d_v258_signal(netinc):
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_504d_v259_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_504d_v260_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_756d_v261_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_756d_v262_signal(shareswa):
    res = _std(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_756d_v263_signal(netinc):
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_756d_v264_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_756d_v265_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_1008d_v266_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_1008d_v267_signal(shareswa):
    res = _std(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_1008d_v268_signal(netinc):
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_1008d_v269_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_1008d_v270_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_sbcomp_vol_slope_1260d_v271_signal(sbcomp):
    res = _std(_slope_pct(sbcomp, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_shareswa_vol_slope_1260d_v272_signal(shareswa):
    res = _std(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_netinc_vol_slope_1260d_v273_signal(netinc):
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_ltip_to_netinc_vol_slope_1260d_v274_signal(sbcomp, netinc):
    res = _std(_slope_pct(_ratio(sbcomp, netinc), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_insider_ltip_dilution_proxy_vol_slope_1260d_v275_signal(sbcomp, shareswa):
    res = _std(_slope_pct(_ratio(sbcomp, shareswa), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 50...")
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
