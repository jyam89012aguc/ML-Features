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

def f11_thrift_alpha_pb_mom_z_63d_v151_signal(pb):
    """Relative momentum strength for Raw level of pb over 63d window."""
    res = _z(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_63d_v152_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 63d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_mom_z_126d_v153_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 126d window."""
    res = _z(_slope_pct(tangibles, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_mom_z_126d_v154_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_mom_z_126d_v155_signal(pb):
    """Relative momentum strength for Raw level of pb over 126d window."""
    res = _z(_slope_pct(pb, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_126d_v156_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 126d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_mom_z_252d_v157_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 252d window."""
    res = _z(_slope_pct(tangibles, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_mom_z_252d_v158_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_mom_z_252d_v159_signal(pb):
    """Relative momentum strength for Raw level of pb over 252d window."""
    res = _z(_slope_pct(pb, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_252d_v160_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 252d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_mom_z_504d_v161_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 504d window."""
    res = _z(_slope_pct(tangibles, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_mom_z_504d_v162_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_mom_z_504d_v163_signal(pb):
    """Relative momentum strength for Raw level of pb over 504d window."""
    res = _z(_slope_pct(pb, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_504d_v164_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 504d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_mom_z_756d_v165_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 756d window."""
    res = _z(_slope_pct(tangibles, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_mom_z_756d_v166_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_mom_z_756d_v167_signal(pb):
    """Relative momentum strength for Raw level of pb over 756d window."""
    res = _z(_slope_pct(pb, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_756d_v168_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 756d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_mom_z_1008d_v169_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 1008d window."""
    res = _z(_slope_pct(tangibles, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_mom_z_1008d_v170_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_mom_z_1008d_v171_signal(pb):
    """Relative momentum strength for Raw level of pb over 1008d window."""
    res = _z(_slope_pct(pb, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_1008d_v172_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 1008d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_mom_z_1260d_v173_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 1260d window."""
    res = _z(_slope_pct(tangibles, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_mom_z_1260d_v174_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_mom_z_1260d_v175_signal(pb):
    """Relative momentum strength for Raw level of pb over 1260d window."""
    res = _z(_slope_pct(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_mom_z_1260d_v176_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible assets per market dollar over 1260d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_5d_v177_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 5d window."""
    res = _std(_slope_pct(tangibles, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_5d_v178_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_5d_v179_signal(pb):
    """Volatility of momentum for Raw level of pb over 5d window."""
    res = _std(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_5d_v180_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 5d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_10d_v181_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 10d window."""
    res = _std(_slope_pct(tangibles, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_10d_v182_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_10d_v183_signal(pb):
    """Volatility of momentum for Raw level of pb over 10d window."""
    res = _std(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_10d_v184_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 10d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_21d_v185_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 21d window."""
    res = _std(_slope_pct(tangibles, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_21d_v186_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_21d_v187_signal(pb):
    """Volatility of momentum for Raw level of pb over 21d window."""
    res = _std(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_21d_v188_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 21d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_42d_v189_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 42d window."""
    res = _std(_slope_pct(tangibles, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_42d_v190_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_42d_v191_signal(pb):
    """Volatility of momentum for Raw level of pb over 42d window."""
    res = _std(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_42d_v192_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 42d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_63d_v193_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 63d window."""
    res = _std(_slope_pct(tangibles, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_63d_v194_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_63d_v195_signal(pb):
    """Volatility of momentum for Raw level of pb over 63d window."""
    res = _std(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_63d_v196_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 63d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_126d_v197_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 126d window."""
    res = _std(_slope_pct(tangibles, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_126d_v198_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_126d_v199_signal(pb):
    """Volatility of momentum for Raw level of pb over 126d window."""
    res = _std(_slope_pct(pb, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_126d_v200_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 126d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_252d_v201_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 252d window."""
    res = _std(_slope_pct(tangibles, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_252d_v202_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 252d window."""
    res = _std(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_252d_v203_signal(pb):
    """Volatility of momentum for Raw level of pb over 252d window."""
    res = _std(_slope_pct(pb, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_252d_v204_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 252d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_504d_v205_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 504d window."""
    res = _std(_slope_pct(tangibles, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_504d_v206_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 504d window."""
    res = _std(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_504d_v207_signal(pb):
    """Volatility of momentum for Raw level of pb over 504d window."""
    res = _std(_slope_pct(pb, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_504d_v208_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 504d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_756d_v209_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 756d window."""
    res = _std(_slope_pct(tangibles, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_756d_v210_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 756d window."""
    res = _std(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_756d_v211_signal(pb):
    """Volatility of momentum for Raw level of pb over 756d window."""
    res = _std(_slope_pct(pb, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_756d_v212_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 756d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_1008d_v213_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 1008d window."""
    res = _std(_slope_pct(tangibles, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_1008d_v214_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 1008d window."""
    res = _std(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_1008d_v215_signal(pb):
    """Volatility of momentum for Raw level of pb over 1008d window."""
    res = _std(_slope_pct(pb, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_1008d_v216_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 1008d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_vol_slope_1260d_v217_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 1260d window."""
    res = _std(_slope_pct(tangibles, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_vol_slope_1260d_v218_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 1260d window."""
    res = _std(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_vol_slope_1260d_v219_signal(pb):
    """Volatility of momentum for Raw level of pb over 1260d window."""
    res = _std(_slope_pct(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_vol_slope_1260d_v220_signal(tangibles, marketcap):
    """Volatility of momentum for Tangible assets per market dollar over 1260d window."""
    res = _std(_slope_pct(_ratio(tangibles, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_5d_v221_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 5d window."""
    res = _ewma(_slope_pct(tangibles, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_5d_v222_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 5d window."""
    res = _ewma(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_5d_v223_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 5d window."""
    res = _ewma(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_5d_v224_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 5d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_10d_v225_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 10d window."""
    res = _ewma(_slope_pct(tangibles, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_10d_v226_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 10d window."""
    res = _ewma(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_10d_v227_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 10d window."""
    res = _ewma(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_10d_v228_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 10d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_21d_v229_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 21d window."""
    res = _ewma(_slope_pct(tangibles, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_21d_v230_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 21d window."""
    res = _ewma(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_21d_v231_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 21d window."""
    res = _ewma(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_21d_v232_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 21d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_42d_v233_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 42d window."""
    res = _ewma(_slope_pct(tangibles, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_42d_v234_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 42d window."""
    res = _ewma(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_42d_v235_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 42d window."""
    res = _ewma(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_42d_v236_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 42d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_63d_v237_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 63d window."""
    res = _ewma(_slope_pct(tangibles, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_63d_v238_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 63d window."""
    res = _ewma(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_63d_v239_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 63d window."""
    res = _ewma(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_63d_v240_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 63d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_126d_v241_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 126d window."""
    res = _ewma(_slope_pct(tangibles, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_126d_v242_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 126d window."""
    res = _ewma(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_126d_v243_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 126d window."""
    res = _ewma(_slope_pct(pb, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_126d_v244_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 126d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_252d_v245_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 252d window."""
    res = _ewma(_slope_pct(tangibles, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_252d_v246_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 252d window."""
    res = _ewma(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_252d_v247_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 252d window."""
    res = _ewma(_slope_pct(pb, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_252d_v248_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 252d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_504d_v249_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 504d window."""
    res = _ewma(_slope_pct(tangibles, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_504d_v250_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 504d window."""
    res = _ewma(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_504d_v251_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 504d window."""
    res = _ewma(_slope_pct(pb, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_504d_v252_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 504d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_756d_v253_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 756d window."""
    res = _ewma(_slope_pct(tangibles, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_756d_v254_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 756d window."""
    res = _ewma(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_756d_v255_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 756d window."""
    res = _ewma(_slope_pct(pb, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_756d_v256_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 756d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_1008d_v257_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 1008d window."""
    res = _ewma(_slope_pct(tangibles, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_1008d_v258_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 1008d window."""
    res = _ewma(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_1008d_v259_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 1008d window."""
    res = _ewma(_slope_pct(pb, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_1008d_v260_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 1008d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_slope_1260d_v261_signal(tangibles):
    """Exponential momentum smoothing for Raw level of tangibles over 1260d window."""
    res = _ewma(_slope_pct(tangibles, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_slope_1260d_v262_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 1260d window."""
    res = _ewma(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_slope_1260d_v263_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 1260d window."""
    res = _ewma(_slope_pct(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_slope_1260d_v264_signal(tangibles, marketcap):
    """Exponential momentum smoothing for Tangible assets per market dollar over 1260d window."""
    res = _ewma(_slope_pct(_ratio(tangibles, marketcap), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f11_thrift_alpha_pb_mom_z_63d_v151_signal": {"func": f11_thrift_alpha_pb_mom_z_63d_v151_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_63d_v152_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_63d_v152_signal},
    "f11_thrift_alpha_tangibles_mom_z_126d_v153_signal": {"func": f11_thrift_alpha_tangibles_mom_z_126d_v153_signal},
    "f11_thrift_alpha_marketcap_mom_z_126d_v154_signal": {"func": f11_thrift_alpha_marketcap_mom_z_126d_v154_signal},
    "f11_thrift_alpha_pb_mom_z_126d_v155_signal": {"func": f11_thrift_alpha_pb_mom_z_126d_v155_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_126d_v156_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_126d_v156_signal},
    "f11_thrift_alpha_tangibles_mom_z_252d_v157_signal": {"func": f11_thrift_alpha_tangibles_mom_z_252d_v157_signal},
    "f11_thrift_alpha_marketcap_mom_z_252d_v158_signal": {"func": f11_thrift_alpha_marketcap_mom_z_252d_v158_signal},
    "f11_thrift_alpha_pb_mom_z_252d_v159_signal": {"func": f11_thrift_alpha_pb_mom_z_252d_v159_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_252d_v160_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_252d_v160_signal},
    "f11_thrift_alpha_tangibles_mom_z_504d_v161_signal": {"func": f11_thrift_alpha_tangibles_mom_z_504d_v161_signal},
    "f11_thrift_alpha_marketcap_mom_z_504d_v162_signal": {"func": f11_thrift_alpha_marketcap_mom_z_504d_v162_signal},
    "f11_thrift_alpha_pb_mom_z_504d_v163_signal": {"func": f11_thrift_alpha_pb_mom_z_504d_v163_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_504d_v164_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_504d_v164_signal},
    "f11_thrift_alpha_tangibles_mom_z_756d_v165_signal": {"func": f11_thrift_alpha_tangibles_mom_z_756d_v165_signal},
    "f11_thrift_alpha_marketcap_mom_z_756d_v166_signal": {"func": f11_thrift_alpha_marketcap_mom_z_756d_v166_signal},
    "f11_thrift_alpha_pb_mom_z_756d_v167_signal": {"func": f11_thrift_alpha_pb_mom_z_756d_v167_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_756d_v168_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_756d_v168_signal},
    "f11_thrift_alpha_tangibles_mom_z_1008d_v169_signal": {"func": f11_thrift_alpha_tangibles_mom_z_1008d_v169_signal},
    "f11_thrift_alpha_marketcap_mom_z_1008d_v170_signal": {"func": f11_thrift_alpha_marketcap_mom_z_1008d_v170_signal},
    "f11_thrift_alpha_pb_mom_z_1008d_v171_signal": {"func": f11_thrift_alpha_pb_mom_z_1008d_v171_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_1008d_v172_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_1008d_v172_signal},
    "f11_thrift_alpha_tangibles_mom_z_1260d_v173_signal": {"func": f11_thrift_alpha_tangibles_mom_z_1260d_v173_signal},
    "f11_thrift_alpha_marketcap_mom_z_1260d_v174_signal": {"func": f11_thrift_alpha_marketcap_mom_z_1260d_v174_signal},
    "f11_thrift_alpha_pb_mom_z_1260d_v175_signal": {"func": f11_thrift_alpha_pb_mom_z_1260d_v175_signal},
    "f11_thrift_alpha_tangible_yield_mom_z_1260d_v176_signal": {"func": f11_thrift_alpha_tangible_yield_mom_z_1260d_v176_signal},
    "f11_thrift_alpha_tangibles_vol_slope_5d_v177_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_5d_v177_signal},
    "f11_thrift_alpha_marketcap_vol_slope_5d_v178_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_5d_v178_signal},
    "f11_thrift_alpha_pb_vol_slope_5d_v179_signal": {"func": f11_thrift_alpha_pb_vol_slope_5d_v179_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_5d_v180_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_5d_v180_signal},
    "f11_thrift_alpha_tangibles_vol_slope_10d_v181_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_10d_v181_signal},
    "f11_thrift_alpha_marketcap_vol_slope_10d_v182_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_10d_v182_signal},
    "f11_thrift_alpha_pb_vol_slope_10d_v183_signal": {"func": f11_thrift_alpha_pb_vol_slope_10d_v183_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_10d_v184_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_10d_v184_signal},
    "f11_thrift_alpha_tangibles_vol_slope_21d_v185_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_21d_v185_signal},
    "f11_thrift_alpha_marketcap_vol_slope_21d_v186_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_21d_v186_signal},
    "f11_thrift_alpha_pb_vol_slope_21d_v187_signal": {"func": f11_thrift_alpha_pb_vol_slope_21d_v187_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_21d_v188_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_21d_v188_signal},
    "f11_thrift_alpha_tangibles_vol_slope_42d_v189_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_42d_v189_signal},
    "f11_thrift_alpha_marketcap_vol_slope_42d_v190_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_42d_v190_signal},
    "f11_thrift_alpha_pb_vol_slope_42d_v191_signal": {"func": f11_thrift_alpha_pb_vol_slope_42d_v191_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_42d_v192_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_42d_v192_signal},
    "f11_thrift_alpha_tangibles_vol_slope_63d_v193_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_63d_v193_signal},
    "f11_thrift_alpha_marketcap_vol_slope_63d_v194_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_63d_v194_signal},
    "f11_thrift_alpha_pb_vol_slope_63d_v195_signal": {"func": f11_thrift_alpha_pb_vol_slope_63d_v195_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_63d_v196_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_63d_v196_signal},
    "f11_thrift_alpha_tangibles_vol_slope_126d_v197_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_126d_v197_signal},
    "f11_thrift_alpha_marketcap_vol_slope_126d_v198_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_126d_v198_signal},
    "f11_thrift_alpha_pb_vol_slope_126d_v199_signal": {"func": f11_thrift_alpha_pb_vol_slope_126d_v199_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_126d_v200_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_126d_v200_signal},
    "f11_thrift_alpha_tangibles_vol_slope_252d_v201_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_252d_v201_signal},
    "f11_thrift_alpha_marketcap_vol_slope_252d_v202_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_252d_v202_signal},
    "f11_thrift_alpha_pb_vol_slope_252d_v203_signal": {"func": f11_thrift_alpha_pb_vol_slope_252d_v203_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_252d_v204_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_252d_v204_signal},
    "f11_thrift_alpha_tangibles_vol_slope_504d_v205_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_504d_v205_signal},
    "f11_thrift_alpha_marketcap_vol_slope_504d_v206_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_504d_v206_signal},
    "f11_thrift_alpha_pb_vol_slope_504d_v207_signal": {"func": f11_thrift_alpha_pb_vol_slope_504d_v207_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_504d_v208_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_504d_v208_signal},
    "f11_thrift_alpha_tangibles_vol_slope_756d_v209_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_756d_v209_signal},
    "f11_thrift_alpha_marketcap_vol_slope_756d_v210_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_756d_v210_signal},
    "f11_thrift_alpha_pb_vol_slope_756d_v211_signal": {"func": f11_thrift_alpha_pb_vol_slope_756d_v211_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_756d_v212_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_756d_v212_signal},
    "f11_thrift_alpha_tangibles_vol_slope_1008d_v213_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_1008d_v213_signal},
    "f11_thrift_alpha_marketcap_vol_slope_1008d_v214_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_1008d_v214_signal},
    "f11_thrift_alpha_pb_vol_slope_1008d_v215_signal": {"func": f11_thrift_alpha_pb_vol_slope_1008d_v215_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_1008d_v216_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_1008d_v216_signal},
    "f11_thrift_alpha_tangibles_vol_slope_1260d_v217_signal": {"func": f11_thrift_alpha_tangibles_vol_slope_1260d_v217_signal},
    "f11_thrift_alpha_marketcap_vol_slope_1260d_v218_signal": {"func": f11_thrift_alpha_marketcap_vol_slope_1260d_v218_signal},
    "f11_thrift_alpha_pb_vol_slope_1260d_v219_signal": {"func": f11_thrift_alpha_pb_vol_slope_1260d_v219_signal},
    "f11_thrift_alpha_tangible_yield_vol_slope_1260d_v220_signal": {"func": f11_thrift_alpha_tangible_yield_vol_slope_1260d_v220_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_5d_v221_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_5d_v221_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_5d_v222_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_5d_v222_signal},
    "f11_thrift_alpha_pb_ewma_slope_5d_v223_signal": {"func": f11_thrift_alpha_pb_ewma_slope_5d_v223_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_5d_v224_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_5d_v224_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_10d_v225_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_10d_v225_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_10d_v226_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_10d_v226_signal},
    "f11_thrift_alpha_pb_ewma_slope_10d_v227_signal": {"func": f11_thrift_alpha_pb_ewma_slope_10d_v227_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_10d_v228_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_10d_v228_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_21d_v229_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_21d_v229_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_21d_v230_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_21d_v230_signal},
    "f11_thrift_alpha_pb_ewma_slope_21d_v231_signal": {"func": f11_thrift_alpha_pb_ewma_slope_21d_v231_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_21d_v232_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_21d_v232_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_42d_v233_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_42d_v233_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_42d_v234_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_42d_v234_signal},
    "f11_thrift_alpha_pb_ewma_slope_42d_v235_signal": {"func": f11_thrift_alpha_pb_ewma_slope_42d_v235_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_42d_v236_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_42d_v236_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_63d_v237_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_63d_v237_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_63d_v238_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_63d_v238_signal},
    "f11_thrift_alpha_pb_ewma_slope_63d_v239_signal": {"func": f11_thrift_alpha_pb_ewma_slope_63d_v239_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_63d_v240_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_63d_v240_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_126d_v241_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_126d_v241_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_126d_v242_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_126d_v242_signal},
    "f11_thrift_alpha_pb_ewma_slope_126d_v243_signal": {"func": f11_thrift_alpha_pb_ewma_slope_126d_v243_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_126d_v244_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_126d_v244_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_252d_v245_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_252d_v245_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_252d_v246_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_252d_v246_signal},
    "f11_thrift_alpha_pb_ewma_slope_252d_v247_signal": {"func": f11_thrift_alpha_pb_ewma_slope_252d_v247_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_252d_v248_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_252d_v248_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_504d_v249_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_504d_v249_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_504d_v250_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_504d_v250_signal},
    "f11_thrift_alpha_pb_ewma_slope_504d_v251_signal": {"func": f11_thrift_alpha_pb_ewma_slope_504d_v251_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_504d_v252_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_504d_v252_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_756d_v253_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_756d_v253_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_756d_v254_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_756d_v254_signal},
    "f11_thrift_alpha_pb_ewma_slope_756d_v255_signal": {"func": f11_thrift_alpha_pb_ewma_slope_756d_v255_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_756d_v256_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_756d_v256_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_1008d_v257_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_1008d_v257_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_1008d_v258_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_1008d_v258_signal},
    "f11_thrift_alpha_pb_ewma_slope_1008d_v259_signal": {"func": f11_thrift_alpha_pb_ewma_slope_1008d_v259_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_1008d_v260_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_1008d_v260_signal},
    "f11_thrift_alpha_tangibles_ewma_slope_1260d_v261_signal": {"func": f11_thrift_alpha_tangibles_ewma_slope_1260d_v261_signal},
    "f11_thrift_alpha_marketcap_ewma_slope_1260d_v262_signal": {"func": f11_thrift_alpha_marketcap_ewma_slope_1260d_v262_signal},
    "f11_thrift_alpha_pb_ewma_slope_1260d_v263_signal": {"func": f11_thrift_alpha_pb_ewma_slope_1260d_v263_signal},
    "f11_thrift_alpha_tangible_yield_ewma_slope_1260d_v264_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 11...")
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
