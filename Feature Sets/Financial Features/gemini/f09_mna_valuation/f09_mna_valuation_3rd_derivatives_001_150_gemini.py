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

def f09_mna_valuation_pb_slope_diff_norm_756d_v151_signal(pb):
    """Normalized slope change for Raw level of pb over 756d window."""
    res = (_slope_pct(pb, 756).diff(756) / _sma(pb.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_756d_v152_signal(pe):
    """Normalized slope change for Raw level of pe over 756d window."""
    res = (_slope_pct(pe, 756).diff(756) / _sma(pe.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_756d_v153_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_756d_v154_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 756d window."""
    res = (_slope_pct(pb * pe, 756).diff(756) / _sma(pb * pe.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_756d_v155_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 756d window."""
    res = (_slope_pct(1 / marketcap, 756).diff(756) / _sma(1 / marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_1008d_v156_signal(pb):
    """Normalized slope change for Raw level of pb over 1008d window."""
    res = (_slope_pct(pb, 1008).diff(1008) / _sma(pb.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_1008d_v157_signal(pe):
    """Normalized slope change for Raw level of pe over 1008d window."""
    res = (_slope_pct(pe, 1008).diff(1008) / _sma(pe.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_1008d_v158_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_1008d_v159_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 1008d window."""
    res = (_slope_pct(pb * pe, 1008).diff(1008) / _sma(pb * pe.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_1008d_v160_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 1008d window."""
    res = (_slope_pct(1 / marketcap, 1008).diff(1008) / _sma(1 / marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_slope_diff_norm_1260d_v161_signal(pb):
    """Normalized slope change for Raw level of pb over 1260d window."""
    res = (_slope_pct(pb, 1260).diff(1260) / _sma(pb.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_slope_diff_norm_1260d_v162_signal(pe):
    """Normalized slope change for Raw level of pe over 1260d window."""
    res = (_slope_pct(pe, 1260).diff(1260) / _sma(pe.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_slope_diff_norm_1260d_v163_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_slope_diff_norm_1260d_v164_signal(pb, pe):
    """Normalized slope change for Combined P/B and P/E valuation metric over 1260d window."""
    res = (_slope_pct(pb * pe, 1260).diff(1260) / _sma(pb * pe.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_slope_diff_norm_1260d_v165_signal(marketcap):
    """Normalized slope change for Size-based discount factor over 1260d window."""
    res = (_slope_pct(1 / marketcap, 1260).diff(1260) / _sma(1 / marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_5d_v166_signal(pb):
    """Relative momentum strength for Raw level of pb over 5d window."""
    res = _z(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_5d_v167_signal(pe):
    """Relative momentum strength for Raw level of pe over 5d window."""
    res = _z(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_5d_v168_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_5d_v169_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 5d window."""
    res = _z(_slope_pct(pb * pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_5d_v170_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 5d window."""
    res = _z(_slope_pct(1 / marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_10d_v171_signal(pb):
    """Relative momentum strength for Raw level of pb over 10d window."""
    res = _z(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_10d_v172_signal(pe):
    """Relative momentum strength for Raw level of pe over 10d window."""
    res = _z(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_10d_v173_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_10d_v174_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 10d window."""
    res = _z(_slope_pct(pb * pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_10d_v175_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 10d window."""
    res = _z(_slope_pct(1 / marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_21d_v176_signal(pb):
    """Relative momentum strength for Raw level of pb over 21d window."""
    res = _z(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_21d_v177_signal(pe):
    """Relative momentum strength for Raw level of pe over 21d window."""
    res = _z(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_21d_v178_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_21d_v179_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 21d window."""
    res = _z(_slope_pct(pb * pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_21d_v180_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 21d window."""
    res = _z(_slope_pct(1 / marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_42d_v181_signal(pb):
    """Relative momentum strength for Raw level of pb over 42d window."""
    res = _z(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_42d_v182_signal(pe):
    """Relative momentum strength for Raw level of pe over 42d window."""
    res = _z(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_42d_v183_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_42d_v184_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 42d window."""
    res = _z(_slope_pct(pb * pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_42d_v185_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 42d window."""
    res = _z(_slope_pct(1 / marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_63d_v186_signal(pb):
    """Relative momentum strength for Raw level of pb over 63d window."""
    res = _z(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_63d_v187_signal(pe):
    """Relative momentum strength for Raw level of pe over 63d window."""
    res = _z(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_63d_v188_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_63d_v189_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 63d window."""
    res = _z(_slope_pct(pb * pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_63d_v190_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 63d window."""
    res = _z(_slope_pct(1 / marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_126d_v191_signal(pb):
    """Relative momentum strength for Raw level of pb over 126d window."""
    res = _z(_slope_pct(pb, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_126d_v192_signal(pe):
    """Relative momentum strength for Raw level of pe over 126d window."""
    res = _z(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_126d_v193_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_126d_v194_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 126d window."""
    res = _z(_slope_pct(pb * pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_126d_v195_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 126d window."""
    res = _z(_slope_pct(1 / marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_252d_v196_signal(pb):
    """Relative momentum strength for Raw level of pb over 252d window."""
    res = _z(_slope_pct(pb, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_252d_v197_signal(pe):
    """Relative momentum strength for Raw level of pe over 252d window."""
    res = _z(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_252d_v198_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_252d_v199_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 252d window."""
    res = _z(_slope_pct(pb * pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_252d_v200_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 252d window."""
    res = _z(_slope_pct(1 / marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_504d_v201_signal(pb):
    """Relative momentum strength for Raw level of pb over 504d window."""
    res = _z(_slope_pct(pb, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_504d_v202_signal(pe):
    """Relative momentum strength for Raw level of pe over 504d window."""
    res = _z(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_504d_v203_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_504d_v204_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 504d window."""
    res = _z(_slope_pct(pb * pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_504d_v205_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 504d window."""
    res = _z(_slope_pct(1 / marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_756d_v206_signal(pb):
    """Relative momentum strength for Raw level of pb over 756d window."""
    res = _z(_slope_pct(pb, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_756d_v207_signal(pe):
    """Relative momentum strength for Raw level of pe over 756d window."""
    res = _z(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_756d_v208_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_756d_v209_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 756d window."""
    res = _z(_slope_pct(pb * pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_756d_v210_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 756d window."""
    res = _z(_slope_pct(1 / marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_1008d_v211_signal(pb):
    """Relative momentum strength for Raw level of pb over 1008d window."""
    res = _z(_slope_pct(pb, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_1008d_v212_signal(pe):
    """Relative momentum strength for Raw level of pe over 1008d window."""
    res = _z(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_1008d_v213_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_1008d_v214_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 1008d window."""
    res = _z(_slope_pct(pb * pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_1008d_v215_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 1008d window."""
    res = _z(_slope_pct(1 / marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_mom_z_1260d_v216_signal(pb):
    """Relative momentum strength for Raw level of pb over 1260d window."""
    res = _z(_slope_pct(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_mom_z_1260d_v217_signal(pe):
    """Relative momentum strength for Raw level of pe over 1260d window."""
    res = _z(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_mom_z_1260d_v218_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_mom_z_1260d_v219_signal(pb, pe):
    """Relative momentum strength for Combined P/B and P/E valuation metric over 1260d window."""
    res = _z(_slope_pct(pb * pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_mom_z_1260d_v220_signal(marketcap):
    """Relative momentum strength for Size-based discount factor over 1260d window."""
    res = _z(_slope_pct(1 / marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_5d_v221_signal(pb):
    """Volatility of momentum for Raw level of pb over 5d window."""
    res = _std(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_5d_v222_signal(pe):
    """Volatility of momentum for Raw level of pe over 5d window."""
    res = _std(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_5d_v223_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_5d_v224_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 5d window."""
    res = _std(_slope_pct(pb * pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_5d_v225_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 5d window."""
    res = _std(_slope_pct(1 / marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_10d_v226_signal(pb):
    """Volatility of momentum for Raw level of pb over 10d window."""
    res = _std(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_10d_v227_signal(pe):
    """Volatility of momentum for Raw level of pe over 10d window."""
    res = _std(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_10d_v228_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_10d_v229_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 10d window."""
    res = _std(_slope_pct(pb * pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_10d_v230_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 10d window."""
    res = _std(_slope_pct(1 / marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_21d_v231_signal(pb):
    """Volatility of momentum for Raw level of pb over 21d window."""
    res = _std(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_21d_v232_signal(pe):
    """Volatility of momentum for Raw level of pe over 21d window."""
    res = _std(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_21d_v233_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_21d_v234_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 21d window."""
    res = _std(_slope_pct(pb * pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_21d_v235_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 21d window."""
    res = _std(_slope_pct(1 / marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_42d_v236_signal(pb):
    """Volatility of momentum for Raw level of pb over 42d window."""
    res = _std(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_42d_v237_signal(pe):
    """Volatility of momentum for Raw level of pe over 42d window."""
    res = _std(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_42d_v238_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_42d_v239_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 42d window."""
    res = _std(_slope_pct(pb * pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_42d_v240_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 42d window."""
    res = _std(_slope_pct(1 / marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_63d_v241_signal(pb):
    """Volatility of momentum for Raw level of pb over 63d window."""
    res = _std(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_63d_v242_signal(pe):
    """Volatility of momentum for Raw level of pe over 63d window."""
    res = _std(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_63d_v243_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_63d_v244_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 63d window."""
    res = _std(_slope_pct(pb * pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_63d_v245_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 63d window."""
    res = _std(_slope_pct(1 / marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_126d_v246_signal(pb):
    """Volatility of momentum for Raw level of pb over 126d window."""
    res = _std(_slope_pct(pb, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_126d_v247_signal(pe):
    """Volatility of momentum for Raw level of pe over 126d window."""
    res = _std(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_126d_v248_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_126d_v249_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 126d window."""
    res = _std(_slope_pct(pb * pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_126d_v250_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 126d window."""
    res = _std(_slope_pct(1 / marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_252d_v251_signal(pb):
    """Volatility of momentum for Raw level of pb over 252d window."""
    res = _std(_slope_pct(pb, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_252d_v252_signal(pe):
    """Volatility of momentum for Raw level of pe over 252d window."""
    res = _std(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_252d_v253_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 252d window."""
    res = _std(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_252d_v254_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 252d window."""
    res = _std(_slope_pct(pb * pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_252d_v255_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 252d window."""
    res = _std(_slope_pct(1 / marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_504d_v256_signal(pb):
    """Volatility of momentum for Raw level of pb over 504d window."""
    res = _std(_slope_pct(pb, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_504d_v257_signal(pe):
    """Volatility of momentum for Raw level of pe over 504d window."""
    res = _std(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_504d_v258_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 504d window."""
    res = _std(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_504d_v259_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 504d window."""
    res = _std(_slope_pct(pb * pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_504d_v260_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 504d window."""
    res = _std(_slope_pct(1 / marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_756d_v261_signal(pb):
    """Volatility of momentum for Raw level of pb over 756d window."""
    res = _std(_slope_pct(pb, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_756d_v262_signal(pe):
    """Volatility of momentum for Raw level of pe over 756d window."""
    res = _std(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_756d_v263_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 756d window."""
    res = _std(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_756d_v264_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 756d window."""
    res = _std(_slope_pct(pb * pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_756d_v265_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 756d window."""
    res = _std(_slope_pct(1 / marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_1008d_v266_signal(pb):
    """Volatility of momentum for Raw level of pb over 1008d window."""
    res = _std(_slope_pct(pb, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_1008d_v267_signal(pe):
    """Volatility of momentum for Raw level of pe over 1008d window."""
    res = _std(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_1008d_v268_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 1008d window."""
    res = _std(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_1008d_v269_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 1008d window."""
    res = _std(_slope_pct(pb * pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_1008d_v270_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 1008d window."""
    res = _std(_slope_pct(1 / marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_vol_slope_1260d_v271_signal(pb):
    """Volatility of momentum for Raw level of pb over 1260d window."""
    res = _std(_slope_pct(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_vol_slope_1260d_v272_signal(pe):
    """Volatility of momentum for Raw level of pe over 1260d window."""
    res = _std(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_vol_slope_1260d_v273_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 1260d window."""
    res = _std(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_vol_slope_1260d_v274_signal(pb, pe):
    """Volatility of momentum for Combined P/B and P/E valuation metric over 1260d window."""
    res = _std(_slope_pct(pb * pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_vol_slope_1260d_v275_signal(marketcap):
    """Volatility of momentum for Size-based discount factor over 1260d window."""
    res = _std(_slope_pct(1 / marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_slope_5d_v276_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 5d window."""
    res = _ewma(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_slope_5d_v277_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 5d window."""
    res = _ewma(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_slope_5d_v278_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 5d window."""
    res = _ewma(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_slope_5d_v279_signal(pb, pe):
    """Exponential momentum smoothing for Combined P/B and P/E valuation metric over 5d window."""
    res = _ewma(_slope_pct(pb * pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_slope_5d_v280_signal(marketcap):
    """Exponential momentum smoothing for Size-based discount factor over 5d window."""
    res = _ewma(_slope_pct(1 / marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_slope_10d_v281_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 10d window."""
    res = _ewma(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_slope_10d_v282_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 10d window."""
    res = _ewma(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_slope_10d_v283_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 10d window."""
    res = _ewma(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_slope_10d_v284_signal(pb, pe):
    """Exponential momentum smoothing for Combined P/B and P/E valuation metric over 10d window."""
    res = _ewma(_slope_pct(pb * pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_slope_10d_v285_signal(marketcap):
    """Exponential momentum smoothing for Size-based discount factor over 10d window."""
    res = _ewma(_slope_pct(1 / marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_slope_21d_v286_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 21d window."""
    res = _ewma(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_slope_21d_v287_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 21d window."""
    res = _ewma(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_slope_21d_v288_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 21d window."""
    res = _ewma(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_slope_21d_v289_signal(pb, pe):
    """Exponential momentum smoothing for Combined P/B and P/E valuation metric over 21d window."""
    res = _ewma(_slope_pct(pb * pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_slope_21d_v290_signal(marketcap):
    """Exponential momentum smoothing for Size-based discount factor over 21d window."""
    res = _ewma(_slope_pct(1 / marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_slope_42d_v291_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 42d window."""
    res = _ewma(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_slope_42d_v292_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 42d window."""
    res = _ewma(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_slope_42d_v293_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 42d window."""
    res = _ewma(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_slope_42d_v294_signal(pb, pe):
    """Exponential momentum smoothing for Combined P/B and P/E valuation metric over 42d window."""
    res = _ewma(_slope_pct(pb * pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_slope_42d_v295_signal(marketcap):
    """Exponential momentum smoothing for Size-based discount factor over 42d window."""
    res = _ewma(_slope_pct(1 / marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_slope_63d_v296_signal(pb):
    """Exponential momentum smoothing for Raw level of pb over 63d window."""
    res = _ewma(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_slope_63d_v297_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 63d window."""
    res = _ewma(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_slope_63d_v298_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 63d window."""
    res = _ewma(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_slope_63d_v299_signal(pb, pe):
    """Exponential momentum smoothing for Combined P/B and P/E valuation metric over 63d window."""
    res = _ewma(_slope_pct(pb * pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_slope_63d_v300_signal(marketcap):
    """Exponential momentum smoothing for Size-based discount factor over 63d window."""
    res = _ewma(_slope_pct(1 / marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f09_mna_valuation_pb_slope_diff_norm_756d_v151_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_756d_v151_signal},
    "f09_mna_valuation_pe_slope_diff_norm_756d_v152_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_756d_v152_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_756d_v153_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_756d_v153_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_756d_v154_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_756d_v154_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_756d_v155_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_756d_v155_signal},
    "f09_mna_valuation_pb_slope_diff_norm_1008d_v156_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_1008d_v156_signal},
    "f09_mna_valuation_pe_slope_diff_norm_1008d_v157_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_1008d_v157_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_1008d_v158_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_1008d_v158_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_1008d_v159_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_1008d_v159_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_1008d_v160_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_1008d_v160_signal},
    "f09_mna_valuation_pb_slope_diff_norm_1260d_v161_signal": {"func": f09_mna_valuation_pb_slope_diff_norm_1260d_v161_signal},
    "f09_mna_valuation_pe_slope_diff_norm_1260d_v162_signal": {"func": f09_mna_valuation_pe_slope_diff_norm_1260d_v162_signal},
    "f09_mna_valuation_marketcap_slope_diff_norm_1260d_v163_signal": {"func": f09_mna_valuation_marketcap_slope_diff_norm_1260d_v163_signal},
    "f09_mna_valuation_valuation_composite_slope_diff_norm_1260d_v164_signal": {"func": f09_mna_valuation_valuation_composite_slope_diff_norm_1260d_v164_signal},
    "f09_mna_valuation_size_factor_slope_diff_norm_1260d_v165_signal": {"func": f09_mna_valuation_size_factor_slope_diff_norm_1260d_v165_signal},
    "f09_mna_valuation_pb_mom_z_5d_v166_signal": {"func": f09_mna_valuation_pb_mom_z_5d_v166_signal},
    "f09_mna_valuation_pe_mom_z_5d_v167_signal": {"func": f09_mna_valuation_pe_mom_z_5d_v167_signal},
    "f09_mna_valuation_marketcap_mom_z_5d_v168_signal": {"func": f09_mna_valuation_marketcap_mom_z_5d_v168_signal},
    "f09_mna_valuation_valuation_composite_mom_z_5d_v169_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_5d_v169_signal},
    "f09_mna_valuation_size_factor_mom_z_5d_v170_signal": {"func": f09_mna_valuation_size_factor_mom_z_5d_v170_signal},
    "f09_mna_valuation_pb_mom_z_10d_v171_signal": {"func": f09_mna_valuation_pb_mom_z_10d_v171_signal},
    "f09_mna_valuation_pe_mom_z_10d_v172_signal": {"func": f09_mna_valuation_pe_mom_z_10d_v172_signal},
    "f09_mna_valuation_marketcap_mom_z_10d_v173_signal": {"func": f09_mna_valuation_marketcap_mom_z_10d_v173_signal},
    "f09_mna_valuation_valuation_composite_mom_z_10d_v174_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_10d_v174_signal},
    "f09_mna_valuation_size_factor_mom_z_10d_v175_signal": {"func": f09_mna_valuation_size_factor_mom_z_10d_v175_signal},
    "f09_mna_valuation_pb_mom_z_21d_v176_signal": {"func": f09_mna_valuation_pb_mom_z_21d_v176_signal},
    "f09_mna_valuation_pe_mom_z_21d_v177_signal": {"func": f09_mna_valuation_pe_mom_z_21d_v177_signal},
    "f09_mna_valuation_marketcap_mom_z_21d_v178_signal": {"func": f09_mna_valuation_marketcap_mom_z_21d_v178_signal},
    "f09_mna_valuation_valuation_composite_mom_z_21d_v179_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_21d_v179_signal},
    "f09_mna_valuation_size_factor_mom_z_21d_v180_signal": {"func": f09_mna_valuation_size_factor_mom_z_21d_v180_signal},
    "f09_mna_valuation_pb_mom_z_42d_v181_signal": {"func": f09_mna_valuation_pb_mom_z_42d_v181_signal},
    "f09_mna_valuation_pe_mom_z_42d_v182_signal": {"func": f09_mna_valuation_pe_mom_z_42d_v182_signal},
    "f09_mna_valuation_marketcap_mom_z_42d_v183_signal": {"func": f09_mna_valuation_marketcap_mom_z_42d_v183_signal},
    "f09_mna_valuation_valuation_composite_mom_z_42d_v184_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_42d_v184_signal},
    "f09_mna_valuation_size_factor_mom_z_42d_v185_signal": {"func": f09_mna_valuation_size_factor_mom_z_42d_v185_signal},
    "f09_mna_valuation_pb_mom_z_63d_v186_signal": {"func": f09_mna_valuation_pb_mom_z_63d_v186_signal},
    "f09_mna_valuation_pe_mom_z_63d_v187_signal": {"func": f09_mna_valuation_pe_mom_z_63d_v187_signal},
    "f09_mna_valuation_marketcap_mom_z_63d_v188_signal": {"func": f09_mna_valuation_marketcap_mom_z_63d_v188_signal},
    "f09_mna_valuation_valuation_composite_mom_z_63d_v189_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_63d_v189_signal},
    "f09_mna_valuation_size_factor_mom_z_63d_v190_signal": {"func": f09_mna_valuation_size_factor_mom_z_63d_v190_signal},
    "f09_mna_valuation_pb_mom_z_126d_v191_signal": {"func": f09_mna_valuation_pb_mom_z_126d_v191_signal},
    "f09_mna_valuation_pe_mom_z_126d_v192_signal": {"func": f09_mna_valuation_pe_mom_z_126d_v192_signal},
    "f09_mna_valuation_marketcap_mom_z_126d_v193_signal": {"func": f09_mna_valuation_marketcap_mom_z_126d_v193_signal},
    "f09_mna_valuation_valuation_composite_mom_z_126d_v194_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_126d_v194_signal},
    "f09_mna_valuation_size_factor_mom_z_126d_v195_signal": {"func": f09_mna_valuation_size_factor_mom_z_126d_v195_signal},
    "f09_mna_valuation_pb_mom_z_252d_v196_signal": {"func": f09_mna_valuation_pb_mom_z_252d_v196_signal},
    "f09_mna_valuation_pe_mom_z_252d_v197_signal": {"func": f09_mna_valuation_pe_mom_z_252d_v197_signal},
    "f09_mna_valuation_marketcap_mom_z_252d_v198_signal": {"func": f09_mna_valuation_marketcap_mom_z_252d_v198_signal},
    "f09_mna_valuation_valuation_composite_mom_z_252d_v199_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_252d_v199_signal},
    "f09_mna_valuation_size_factor_mom_z_252d_v200_signal": {"func": f09_mna_valuation_size_factor_mom_z_252d_v200_signal},
    "f09_mna_valuation_pb_mom_z_504d_v201_signal": {"func": f09_mna_valuation_pb_mom_z_504d_v201_signal},
    "f09_mna_valuation_pe_mom_z_504d_v202_signal": {"func": f09_mna_valuation_pe_mom_z_504d_v202_signal},
    "f09_mna_valuation_marketcap_mom_z_504d_v203_signal": {"func": f09_mna_valuation_marketcap_mom_z_504d_v203_signal},
    "f09_mna_valuation_valuation_composite_mom_z_504d_v204_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_504d_v204_signal},
    "f09_mna_valuation_size_factor_mom_z_504d_v205_signal": {"func": f09_mna_valuation_size_factor_mom_z_504d_v205_signal},
    "f09_mna_valuation_pb_mom_z_756d_v206_signal": {"func": f09_mna_valuation_pb_mom_z_756d_v206_signal},
    "f09_mna_valuation_pe_mom_z_756d_v207_signal": {"func": f09_mna_valuation_pe_mom_z_756d_v207_signal},
    "f09_mna_valuation_marketcap_mom_z_756d_v208_signal": {"func": f09_mna_valuation_marketcap_mom_z_756d_v208_signal},
    "f09_mna_valuation_valuation_composite_mom_z_756d_v209_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_756d_v209_signal},
    "f09_mna_valuation_size_factor_mom_z_756d_v210_signal": {"func": f09_mna_valuation_size_factor_mom_z_756d_v210_signal},
    "f09_mna_valuation_pb_mom_z_1008d_v211_signal": {"func": f09_mna_valuation_pb_mom_z_1008d_v211_signal},
    "f09_mna_valuation_pe_mom_z_1008d_v212_signal": {"func": f09_mna_valuation_pe_mom_z_1008d_v212_signal},
    "f09_mna_valuation_marketcap_mom_z_1008d_v213_signal": {"func": f09_mna_valuation_marketcap_mom_z_1008d_v213_signal},
    "f09_mna_valuation_valuation_composite_mom_z_1008d_v214_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_1008d_v214_signal},
    "f09_mna_valuation_size_factor_mom_z_1008d_v215_signal": {"func": f09_mna_valuation_size_factor_mom_z_1008d_v215_signal},
    "f09_mna_valuation_pb_mom_z_1260d_v216_signal": {"func": f09_mna_valuation_pb_mom_z_1260d_v216_signal},
    "f09_mna_valuation_pe_mom_z_1260d_v217_signal": {"func": f09_mna_valuation_pe_mom_z_1260d_v217_signal},
    "f09_mna_valuation_marketcap_mom_z_1260d_v218_signal": {"func": f09_mna_valuation_marketcap_mom_z_1260d_v218_signal},
    "f09_mna_valuation_valuation_composite_mom_z_1260d_v219_signal": {"func": f09_mna_valuation_valuation_composite_mom_z_1260d_v219_signal},
    "f09_mna_valuation_size_factor_mom_z_1260d_v220_signal": {"func": f09_mna_valuation_size_factor_mom_z_1260d_v220_signal},
    "f09_mna_valuation_pb_vol_slope_5d_v221_signal": {"func": f09_mna_valuation_pb_vol_slope_5d_v221_signal},
    "f09_mna_valuation_pe_vol_slope_5d_v222_signal": {"func": f09_mna_valuation_pe_vol_slope_5d_v222_signal},
    "f09_mna_valuation_marketcap_vol_slope_5d_v223_signal": {"func": f09_mna_valuation_marketcap_vol_slope_5d_v223_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_5d_v224_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_5d_v224_signal},
    "f09_mna_valuation_size_factor_vol_slope_5d_v225_signal": {"func": f09_mna_valuation_size_factor_vol_slope_5d_v225_signal},
    "f09_mna_valuation_pb_vol_slope_10d_v226_signal": {"func": f09_mna_valuation_pb_vol_slope_10d_v226_signal},
    "f09_mna_valuation_pe_vol_slope_10d_v227_signal": {"func": f09_mna_valuation_pe_vol_slope_10d_v227_signal},
    "f09_mna_valuation_marketcap_vol_slope_10d_v228_signal": {"func": f09_mna_valuation_marketcap_vol_slope_10d_v228_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_10d_v229_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_10d_v229_signal},
    "f09_mna_valuation_size_factor_vol_slope_10d_v230_signal": {"func": f09_mna_valuation_size_factor_vol_slope_10d_v230_signal},
    "f09_mna_valuation_pb_vol_slope_21d_v231_signal": {"func": f09_mna_valuation_pb_vol_slope_21d_v231_signal},
    "f09_mna_valuation_pe_vol_slope_21d_v232_signal": {"func": f09_mna_valuation_pe_vol_slope_21d_v232_signal},
    "f09_mna_valuation_marketcap_vol_slope_21d_v233_signal": {"func": f09_mna_valuation_marketcap_vol_slope_21d_v233_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_21d_v234_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_21d_v234_signal},
    "f09_mna_valuation_size_factor_vol_slope_21d_v235_signal": {"func": f09_mna_valuation_size_factor_vol_slope_21d_v235_signal},
    "f09_mna_valuation_pb_vol_slope_42d_v236_signal": {"func": f09_mna_valuation_pb_vol_slope_42d_v236_signal},
    "f09_mna_valuation_pe_vol_slope_42d_v237_signal": {"func": f09_mna_valuation_pe_vol_slope_42d_v237_signal},
    "f09_mna_valuation_marketcap_vol_slope_42d_v238_signal": {"func": f09_mna_valuation_marketcap_vol_slope_42d_v238_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_42d_v239_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_42d_v239_signal},
    "f09_mna_valuation_size_factor_vol_slope_42d_v240_signal": {"func": f09_mna_valuation_size_factor_vol_slope_42d_v240_signal},
    "f09_mna_valuation_pb_vol_slope_63d_v241_signal": {"func": f09_mna_valuation_pb_vol_slope_63d_v241_signal},
    "f09_mna_valuation_pe_vol_slope_63d_v242_signal": {"func": f09_mna_valuation_pe_vol_slope_63d_v242_signal},
    "f09_mna_valuation_marketcap_vol_slope_63d_v243_signal": {"func": f09_mna_valuation_marketcap_vol_slope_63d_v243_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_63d_v244_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_63d_v244_signal},
    "f09_mna_valuation_size_factor_vol_slope_63d_v245_signal": {"func": f09_mna_valuation_size_factor_vol_slope_63d_v245_signal},
    "f09_mna_valuation_pb_vol_slope_126d_v246_signal": {"func": f09_mna_valuation_pb_vol_slope_126d_v246_signal},
    "f09_mna_valuation_pe_vol_slope_126d_v247_signal": {"func": f09_mna_valuation_pe_vol_slope_126d_v247_signal},
    "f09_mna_valuation_marketcap_vol_slope_126d_v248_signal": {"func": f09_mna_valuation_marketcap_vol_slope_126d_v248_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_126d_v249_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_126d_v249_signal},
    "f09_mna_valuation_size_factor_vol_slope_126d_v250_signal": {"func": f09_mna_valuation_size_factor_vol_slope_126d_v250_signal},
    "f09_mna_valuation_pb_vol_slope_252d_v251_signal": {"func": f09_mna_valuation_pb_vol_slope_252d_v251_signal},
    "f09_mna_valuation_pe_vol_slope_252d_v252_signal": {"func": f09_mna_valuation_pe_vol_slope_252d_v252_signal},
    "f09_mna_valuation_marketcap_vol_slope_252d_v253_signal": {"func": f09_mna_valuation_marketcap_vol_slope_252d_v253_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_252d_v254_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_252d_v254_signal},
    "f09_mna_valuation_size_factor_vol_slope_252d_v255_signal": {"func": f09_mna_valuation_size_factor_vol_slope_252d_v255_signal},
    "f09_mna_valuation_pb_vol_slope_504d_v256_signal": {"func": f09_mna_valuation_pb_vol_slope_504d_v256_signal},
    "f09_mna_valuation_pe_vol_slope_504d_v257_signal": {"func": f09_mna_valuation_pe_vol_slope_504d_v257_signal},
    "f09_mna_valuation_marketcap_vol_slope_504d_v258_signal": {"func": f09_mna_valuation_marketcap_vol_slope_504d_v258_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_504d_v259_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_504d_v259_signal},
    "f09_mna_valuation_size_factor_vol_slope_504d_v260_signal": {"func": f09_mna_valuation_size_factor_vol_slope_504d_v260_signal},
    "f09_mna_valuation_pb_vol_slope_756d_v261_signal": {"func": f09_mna_valuation_pb_vol_slope_756d_v261_signal},
    "f09_mna_valuation_pe_vol_slope_756d_v262_signal": {"func": f09_mna_valuation_pe_vol_slope_756d_v262_signal},
    "f09_mna_valuation_marketcap_vol_slope_756d_v263_signal": {"func": f09_mna_valuation_marketcap_vol_slope_756d_v263_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_756d_v264_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_756d_v264_signal},
    "f09_mna_valuation_size_factor_vol_slope_756d_v265_signal": {"func": f09_mna_valuation_size_factor_vol_slope_756d_v265_signal},
    "f09_mna_valuation_pb_vol_slope_1008d_v266_signal": {"func": f09_mna_valuation_pb_vol_slope_1008d_v266_signal},
    "f09_mna_valuation_pe_vol_slope_1008d_v267_signal": {"func": f09_mna_valuation_pe_vol_slope_1008d_v267_signal},
    "f09_mna_valuation_marketcap_vol_slope_1008d_v268_signal": {"func": f09_mna_valuation_marketcap_vol_slope_1008d_v268_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_1008d_v269_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_1008d_v269_signal},
    "f09_mna_valuation_size_factor_vol_slope_1008d_v270_signal": {"func": f09_mna_valuation_size_factor_vol_slope_1008d_v270_signal},
    "f09_mna_valuation_pb_vol_slope_1260d_v271_signal": {"func": f09_mna_valuation_pb_vol_slope_1260d_v271_signal},
    "f09_mna_valuation_pe_vol_slope_1260d_v272_signal": {"func": f09_mna_valuation_pe_vol_slope_1260d_v272_signal},
    "f09_mna_valuation_marketcap_vol_slope_1260d_v273_signal": {"func": f09_mna_valuation_marketcap_vol_slope_1260d_v273_signal},
    "f09_mna_valuation_valuation_composite_vol_slope_1260d_v274_signal": {"func": f09_mna_valuation_valuation_composite_vol_slope_1260d_v274_signal},
    "f09_mna_valuation_size_factor_vol_slope_1260d_v275_signal": {"func": f09_mna_valuation_size_factor_vol_slope_1260d_v275_signal},
    "f09_mna_valuation_pb_ewma_slope_5d_v276_signal": {"func": f09_mna_valuation_pb_ewma_slope_5d_v276_signal},
    "f09_mna_valuation_pe_ewma_slope_5d_v277_signal": {"func": f09_mna_valuation_pe_ewma_slope_5d_v277_signal},
    "f09_mna_valuation_marketcap_ewma_slope_5d_v278_signal": {"func": f09_mna_valuation_marketcap_ewma_slope_5d_v278_signal},
    "f09_mna_valuation_valuation_composite_ewma_slope_5d_v279_signal": {"func": f09_mna_valuation_valuation_composite_ewma_slope_5d_v279_signal},
    "f09_mna_valuation_size_factor_ewma_slope_5d_v280_signal": {"func": f09_mna_valuation_size_factor_ewma_slope_5d_v280_signal},
    "f09_mna_valuation_pb_ewma_slope_10d_v281_signal": {"func": f09_mna_valuation_pb_ewma_slope_10d_v281_signal},
    "f09_mna_valuation_pe_ewma_slope_10d_v282_signal": {"func": f09_mna_valuation_pe_ewma_slope_10d_v282_signal},
    "f09_mna_valuation_marketcap_ewma_slope_10d_v283_signal": {"func": f09_mna_valuation_marketcap_ewma_slope_10d_v283_signal},
    "f09_mna_valuation_valuation_composite_ewma_slope_10d_v284_signal": {"func": f09_mna_valuation_valuation_composite_ewma_slope_10d_v284_signal},
    "f09_mna_valuation_size_factor_ewma_slope_10d_v285_signal": {"func": f09_mna_valuation_size_factor_ewma_slope_10d_v285_signal},
    "f09_mna_valuation_pb_ewma_slope_21d_v286_signal": {"func": f09_mna_valuation_pb_ewma_slope_21d_v286_signal},
    "f09_mna_valuation_pe_ewma_slope_21d_v287_signal": {"func": f09_mna_valuation_pe_ewma_slope_21d_v287_signal},
    "f09_mna_valuation_marketcap_ewma_slope_21d_v288_signal": {"func": f09_mna_valuation_marketcap_ewma_slope_21d_v288_signal},
    "f09_mna_valuation_valuation_composite_ewma_slope_21d_v289_signal": {"func": f09_mna_valuation_valuation_composite_ewma_slope_21d_v289_signal},
    "f09_mna_valuation_size_factor_ewma_slope_21d_v290_signal": {"func": f09_mna_valuation_size_factor_ewma_slope_21d_v290_signal},
    "f09_mna_valuation_pb_ewma_slope_42d_v291_signal": {"func": f09_mna_valuation_pb_ewma_slope_42d_v291_signal},
    "f09_mna_valuation_pe_ewma_slope_42d_v292_signal": {"func": f09_mna_valuation_pe_ewma_slope_42d_v292_signal},
    "f09_mna_valuation_marketcap_ewma_slope_42d_v293_signal": {"func": f09_mna_valuation_marketcap_ewma_slope_42d_v293_signal},
    "f09_mna_valuation_valuation_composite_ewma_slope_42d_v294_signal": {"func": f09_mna_valuation_valuation_composite_ewma_slope_42d_v294_signal},
    "f09_mna_valuation_size_factor_ewma_slope_42d_v295_signal": {"func": f09_mna_valuation_size_factor_ewma_slope_42d_v295_signal},
    "f09_mna_valuation_pb_ewma_slope_63d_v296_signal": {"func": f09_mna_valuation_pb_ewma_slope_63d_v296_signal},
    "f09_mna_valuation_pe_ewma_slope_63d_v297_signal": {"func": f09_mna_valuation_pe_ewma_slope_63d_v297_signal},
    "f09_mna_valuation_marketcap_ewma_slope_63d_v298_signal": {"func": f09_mna_valuation_marketcap_ewma_slope_63d_v298_signal},
    "f09_mna_valuation_valuation_composite_ewma_slope_63d_v299_signal": {"func": f09_mna_valuation_valuation_composite_ewma_slope_63d_v299_signal},
    "f09_mna_valuation_size_factor_ewma_slope_63d_v300_signal": {"func": f09_mna_valuation_size_factor_ewma_slope_63d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 09...")
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
