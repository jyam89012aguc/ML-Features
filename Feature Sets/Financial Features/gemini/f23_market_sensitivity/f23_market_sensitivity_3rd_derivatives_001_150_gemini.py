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

def f23_market_sensitivity_pe_mom_z_63d_v151_signal(pe):
    """Relative momentum strength for Raw level of pe over 63d window."""
    res = _z(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_63d_v152_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 63d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_mom_z_126d_v153_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 126d window."""
    res = _z(_slope_pct(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_mom_z_126d_v154_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_mom_z_126d_v155_signal(pe):
    """Relative momentum strength for Raw level of pe over 126d window."""
    res = _z(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_126d_v156_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 126d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_mom_z_252d_v157_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 252d window."""
    res = _z(_slope_pct(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_mom_z_252d_v158_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_mom_z_252d_v159_signal(pe):
    """Relative momentum strength for Raw level of pe over 252d window."""
    res = _z(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_252d_v160_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 252d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_mom_z_504d_v161_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 504d window."""
    res = _z(_slope_pct(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_mom_z_504d_v162_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_mom_z_504d_v163_signal(pe):
    """Relative momentum strength for Raw level of pe over 504d window."""
    res = _z(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_504d_v164_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 504d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_mom_z_756d_v165_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 756d window."""
    res = _z(_slope_pct(closeadj, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_mom_z_756d_v166_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_mom_z_756d_v167_signal(pe):
    """Relative momentum strength for Raw level of pe over 756d window."""
    res = _z(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_756d_v168_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 756d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_mom_z_1008d_v169_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 1008d window."""
    res = _z(_slope_pct(closeadj, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_mom_z_1008d_v170_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_mom_z_1008d_v171_signal(pe):
    """Relative momentum strength for Raw level of pe over 1008d window."""
    res = _z(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_1008d_v172_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 1008d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_mom_z_1260d_v173_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 1260d window."""
    res = _z(_slope_pct(closeadj, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_mom_z_1260d_v174_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_mom_z_1260d_v175_signal(pe):
    """Relative momentum strength for Raw level of pe over 1260d window."""
    res = _z(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_mom_z_1260d_v176_signal(closeadj):
    """Relative momentum strength for Short-to-medium term volatility interaction over 1260d window."""
    res = _z(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_5d_v177_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 5d window."""
    res = _std(_slope_pct(closeadj, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_5d_v178_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 5d window."""
    res = _std(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_5d_v179_signal(pe):
    """Volatility of momentum for Raw level of pe over 5d window."""
    res = _std(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_5d_v180_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 5d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_10d_v181_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 10d window."""
    res = _std(_slope_pct(closeadj, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_10d_v182_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 10d window."""
    res = _std(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_10d_v183_signal(pe):
    """Volatility of momentum for Raw level of pe over 10d window."""
    res = _std(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_10d_v184_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 10d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_21d_v185_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 21d window."""
    res = _std(_slope_pct(closeadj, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_21d_v186_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 21d window."""
    res = _std(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_21d_v187_signal(pe):
    """Volatility of momentum for Raw level of pe over 21d window."""
    res = _std(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_21d_v188_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 21d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_42d_v189_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 42d window."""
    res = _std(_slope_pct(closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_42d_v190_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 42d window."""
    res = _std(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_42d_v191_signal(pe):
    """Volatility of momentum for Raw level of pe over 42d window."""
    res = _std(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_42d_v192_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 42d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_63d_v193_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 63d window."""
    res = _std(_slope_pct(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_63d_v194_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 63d window."""
    res = _std(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_63d_v195_signal(pe):
    """Volatility of momentum for Raw level of pe over 63d window."""
    res = _std(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_63d_v196_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 63d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_126d_v197_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 126d window."""
    res = _std(_slope_pct(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_126d_v198_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 126d window."""
    res = _std(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_126d_v199_signal(pe):
    """Volatility of momentum for Raw level of pe over 126d window."""
    res = _std(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_126d_v200_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 126d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_252d_v201_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 252d window."""
    res = _std(_slope_pct(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_252d_v202_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 252d window."""
    res = _std(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_252d_v203_signal(pe):
    """Volatility of momentum for Raw level of pe over 252d window."""
    res = _std(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_252d_v204_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 252d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_504d_v205_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 504d window."""
    res = _std(_slope_pct(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_504d_v206_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 504d window."""
    res = _std(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_504d_v207_signal(pe):
    """Volatility of momentum for Raw level of pe over 504d window."""
    res = _std(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_504d_v208_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 504d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_756d_v209_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 756d window."""
    res = _std(_slope_pct(closeadj, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_756d_v210_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 756d window."""
    res = _std(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_756d_v211_signal(pe):
    """Volatility of momentum for Raw level of pe over 756d window."""
    res = _std(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_756d_v212_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 756d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_1008d_v213_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 1008d window."""
    res = _std(_slope_pct(closeadj, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_1008d_v214_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 1008d window."""
    res = _std(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_1008d_v215_signal(pe):
    """Volatility of momentum for Raw level of pe over 1008d window."""
    res = _std(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_1008d_v216_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 1008d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_vol_slope_1260d_v217_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 1260d window."""
    res = _std(_slope_pct(closeadj, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_vol_slope_1260d_v218_signal(marketcap):
    """Volatility of momentum for Raw level of marketcap over 1260d window."""
    res = _std(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_vol_slope_1260d_v219_signal(pe):
    """Volatility of momentum for Raw level of pe over 1260d window."""
    res = _std(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_vol_slope_1260d_v220_signal(closeadj):
    """Volatility of momentum for Short-to-medium term volatility interaction over 1260d window."""
    res = _std(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_5d_v221_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 5d window."""
    res = _ewma(_slope_pct(closeadj, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_5d_v222_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 5d window."""
    res = _ewma(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_5d_v223_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 5d window."""
    res = _ewma(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_5d_v224_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 5d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_10d_v225_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 10d window."""
    res = _ewma(_slope_pct(closeadj, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_10d_v226_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 10d window."""
    res = _ewma(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_10d_v227_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 10d window."""
    res = _ewma(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_10d_v228_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 10d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_21d_v229_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 21d window."""
    res = _ewma(_slope_pct(closeadj, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_21d_v230_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 21d window."""
    res = _ewma(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_21d_v231_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 21d window."""
    res = _ewma(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_21d_v232_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 21d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_42d_v233_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 42d window."""
    res = _ewma(_slope_pct(closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_42d_v234_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 42d window."""
    res = _ewma(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_42d_v235_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 42d window."""
    res = _ewma(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_42d_v236_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 42d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_63d_v237_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 63d window."""
    res = _ewma(_slope_pct(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_63d_v238_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 63d window."""
    res = _ewma(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_63d_v239_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 63d window."""
    res = _ewma(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_63d_v240_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 63d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_126d_v241_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 126d window."""
    res = _ewma(_slope_pct(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_126d_v242_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 126d window."""
    res = _ewma(_slope_pct(marketcap, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_126d_v243_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 126d window."""
    res = _ewma(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_126d_v244_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 126d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_252d_v245_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 252d window."""
    res = _ewma(_slope_pct(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_252d_v246_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 252d window."""
    res = _ewma(_slope_pct(marketcap, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_252d_v247_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 252d window."""
    res = _ewma(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_252d_v248_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 252d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_504d_v249_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 504d window."""
    res = _ewma(_slope_pct(closeadj, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_504d_v250_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 504d window."""
    res = _ewma(_slope_pct(marketcap, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_504d_v251_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 504d window."""
    res = _ewma(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_504d_v252_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 504d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_756d_v253_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 756d window."""
    res = _ewma(_slope_pct(closeadj, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_756d_v254_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 756d window."""
    res = _ewma(_slope_pct(marketcap, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_756d_v255_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 756d window."""
    res = _ewma(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_756d_v256_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 756d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_1008d_v257_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 1008d window."""
    res = _ewma(_slope_pct(closeadj, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_1008d_v258_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 1008d window."""
    res = _ewma(_slope_pct(marketcap, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_1008d_v259_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 1008d window."""
    res = _ewma(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_1008d_v260_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 1008d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_closeadj_ewma_slope_1260d_v261_signal(closeadj):
    """Exponential momentum smoothing for Raw level of closeadj over 1260d window."""
    res = _ewma(_slope_pct(closeadj, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_marketcap_ewma_slope_1260d_v262_signal(marketcap):
    """Exponential momentum smoothing for Raw level of marketcap over 1260d window."""
    res = _ewma(_slope_pct(marketcap, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_pe_ewma_slope_1260d_v263_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 1260d window."""
    res = _ewma(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f23_market_sensitivity_vol_premium_ewma_slope_1260d_v264_signal(closeadj):
    """Exponential momentum smoothing for Short-to-medium term volatility interaction over 1260d window."""
    res = _ewma(_slope_pct(_std(closeadj, 21) / _std(closeadj, 126), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f23_market_sensitivity_pe_mom_z_63d_v151_signal": {"func": f23_market_sensitivity_pe_mom_z_63d_v151_signal},
    "f23_market_sensitivity_vol_premium_mom_z_63d_v152_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_63d_v152_signal},
    "f23_market_sensitivity_closeadj_mom_z_126d_v153_signal": {"func": f23_market_sensitivity_closeadj_mom_z_126d_v153_signal},
    "f23_market_sensitivity_marketcap_mom_z_126d_v154_signal": {"func": f23_market_sensitivity_marketcap_mom_z_126d_v154_signal},
    "f23_market_sensitivity_pe_mom_z_126d_v155_signal": {"func": f23_market_sensitivity_pe_mom_z_126d_v155_signal},
    "f23_market_sensitivity_vol_premium_mom_z_126d_v156_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_126d_v156_signal},
    "f23_market_sensitivity_closeadj_mom_z_252d_v157_signal": {"func": f23_market_sensitivity_closeadj_mom_z_252d_v157_signal},
    "f23_market_sensitivity_marketcap_mom_z_252d_v158_signal": {"func": f23_market_sensitivity_marketcap_mom_z_252d_v158_signal},
    "f23_market_sensitivity_pe_mom_z_252d_v159_signal": {"func": f23_market_sensitivity_pe_mom_z_252d_v159_signal},
    "f23_market_sensitivity_vol_premium_mom_z_252d_v160_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_252d_v160_signal},
    "f23_market_sensitivity_closeadj_mom_z_504d_v161_signal": {"func": f23_market_sensitivity_closeadj_mom_z_504d_v161_signal},
    "f23_market_sensitivity_marketcap_mom_z_504d_v162_signal": {"func": f23_market_sensitivity_marketcap_mom_z_504d_v162_signal},
    "f23_market_sensitivity_pe_mom_z_504d_v163_signal": {"func": f23_market_sensitivity_pe_mom_z_504d_v163_signal},
    "f23_market_sensitivity_vol_premium_mom_z_504d_v164_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_504d_v164_signal},
    "f23_market_sensitivity_closeadj_mom_z_756d_v165_signal": {"func": f23_market_sensitivity_closeadj_mom_z_756d_v165_signal},
    "f23_market_sensitivity_marketcap_mom_z_756d_v166_signal": {"func": f23_market_sensitivity_marketcap_mom_z_756d_v166_signal},
    "f23_market_sensitivity_pe_mom_z_756d_v167_signal": {"func": f23_market_sensitivity_pe_mom_z_756d_v167_signal},
    "f23_market_sensitivity_vol_premium_mom_z_756d_v168_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_756d_v168_signal},
    "f23_market_sensitivity_closeadj_mom_z_1008d_v169_signal": {"func": f23_market_sensitivity_closeadj_mom_z_1008d_v169_signal},
    "f23_market_sensitivity_marketcap_mom_z_1008d_v170_signal": {"func": f23_market_sensitivity_marketcap_mom_z_1008d_v170_signal},
    "f23_market_sensitivity_pe_mom_z_1008d_v171_signal": {"func": f23_market_sensitivity_pe_mom_z_1008d_v171_signal},
    "f23_market_sensitivity_vol_premium_mom_z_1008d_v172_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_1008d_v172_signal},
    "f23_market_sensitivity_closeadj_mom_z_1260d_v173_signal": {"func": f23_market_sensitivity_closeadj_mom_z_1260d_v173_signal},
    "f23_market_sensitivity_marketcap_mom_z_1260d_v174_signal": {"func": f23_market_sensitivity_marketcap_mom_z_1260d_v174_signal},
    "f23_market_sensitivity_pe_mom_z_1260d_v175_signal": {"func": f23_market_sensitivity_pe_mom_z_1260d_v175_signal},
    "f23_market_sensitivity_vol_premium_mom_z_1260d_v176_signal": {"func": f23_market_sensitivity_vol_premium_mom_z_1260d_v176_signal},
    "f23_market_sensitivity_closeadj_vol_slope_5d_v177_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_5d_v177_signal},
    "f23_market_sensitivity_marketcap_vol_slope_5d_v178_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_5d_v178_signal},
    "f23_market_sensitivity_pe_vol_slope_5d_v179_signal": {"func": f23_market_sensitivity_pe_vol_slope_5d_v179_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_5d_v180_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_5d_v180_signal},
    "f23_market_sensitivity_closeadj_vol_slope_10d_v181_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_10d_v181_signal},
    "f23_market_sensitivity_marketcap_vol_slope_10d_v182_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_10d_v182_signal},
    "f23_market_sensitivity_pe_vol_slope_10d_v183_signal": {"func": f23_market_sensitivity_pe_vol_slope_10d_v183_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_10d_v184_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_10d_v184_signal},
    "f23_market_sensitivity_closeadj_vol_slope_21d_v185_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_21d_v185_signal},
    "f23_market_sensitivity_marketcap_vol_slope_21d_v186_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_21d_v186_signal},
    "f23_market_sensitivity_pe_vol_slope_21d_v187_signal": {"func": f23_market_sensitivity_pe_vol_slope_21d_v187_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_21d_v188_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_21d_v188_signal},
    "f23_market_sensitivity_closeadj_vol_slope_42d_v189_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_42d_v189_signal},
    "f23_market_sensitivity_marketcap_vol_slope_42d_v190_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_42d_v190_signal},
    "f23_market_sensitivity_pe_vol_slope_42d_v191_signal": {"func": f23_market_sensitivity_pe_vol_slope_42d_v191_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_42d_v192_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_42d_v192_signal},
    "f23_market_sensitivity_closeadj_vol_slope_63d_v193_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_63d_v193_signal},
    "f23_market_sensitivity_marketcap_vol_slope_63d_v194_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_63d_v194_signal},
    "f23_market_sensitivity_pe_vol_slope_63d_v195_signal": {"func": f23_market_sensitivity_pe_vol_slope_63d_v195_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_63d_v196_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_63d_v196_signal},
    "f23_market_sensitivity_closeadj_vol_slope_126d_v197_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_126d_v197_signal},
    "f23_market_sensitivity_marketcap_vol_slope_126d_v198_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_126d_v198_signal},
    "f23_market_sensitivity_pe_vol_slope_126d_v199_signal": {"func": f23_market_sensitivity_pe_vol_slope_126d_v199_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_126d_v200_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_126d_v200_signal},
    "f23_market_sensitivity_closeadj_vol_slope_252d_v201_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_252d_v201_signal},
    "f23_market_sensitivity_marketcap_vol_slope_252d_v202_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_252d_v202_signal},
    "f23_market_sensitivity_pe_vol_slope_252d_v203_signal": {"func": f23_market_sensitivity_pe_vol_slope_252d_v203_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_252d_v204_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_252d_v204_signal},
    "f23_market_sensitivity_closeadj_vol_slope_504d_v205_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_504d_v205_signal},
    "f23_market_sensitivity_marketcap_vol_slope_504d_v206_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_504d_v206_signal},
    "f23_market_sensitivity_pe_vol_slope_504d_v207_signal": {"func": f23_market_sensitivity_pe_vol_slope_504d_v207_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_504d_v208_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_504d_v208_signal},
    "f23_market_sensitivity_closeadj_vol_slope_756d_v209_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_756d_v209_signal},
    "f23_market_sensitivity_marketcap_vol_slope_756d_v210_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_756d_v210_signal},
    "f23_market_sensitivity_pe_vol_slope_756d_v211_signal": {"func": f23_market_sensitivity_pe_vol_slope_756d_v211_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_756d_v212_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_756d_v212_signal},
    "f23_market_sensitivity_closeadj_vol_slope_1008d_v213_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_1008d_v213_signal},
    "f23_market_sensitivity_marketcap_vol_slope_1008d_v214_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_1008d_v214_signal},
    "f23_market_sensitivity_pe_vol_slope_1008d_v215_signal": {"func": f23_market_sensitivity_pe_vol_slope_1008d_v215_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_1008d_v216_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_1008d_v216_signal},
    "f23_market_sensitivity_closeadj_vol_slope_1260d_v217_signal": {"func": f23_market_sensitivity_closeadj_vol_slope_1260d_v217_signal},
    "f23_market_sensitivity_marketcap_vol_slope_1260d_v218_signal": {"func": f23_market_sensitivity_marketcap_vol_slope_1260d_v218_signal},
    "f23_market_sensitivity_pe_vol_slope_1260d_v219_signal": {"func": f23_market_sensitivity_pe_vol_slope_1260d_v219_signal},
    "f23_market_sensitivity_vol_premium_vol_slope_1260d_v220_signal": {"func": f23_market_sensitivity_vol_premium_vol_slope_1260d_v220_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_5d_v221_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_5d_v221_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_5d_v222_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_5d_v222_signal},
    "f23_market_sensitivity_pe_ewma_slope_5d_v223_signal": {"func": f23_market_sensitivity_pe_ewma_slope_5d_v223_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_5d_v224_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_5d_v224_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_10d_v225_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_10d_v225_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_10d_v226_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_10d_v226_signal},
    "f23_market_sensitivity_pe_ewma_slope_10d_v227_signal": {"func": f23_market_sensitivity_pe_ewma_slope_10d_v227_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_10d_v228_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_10d_v228_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_21d_v229_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_21d_v229_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_21d_v230_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_21d_v230_signal},
    "f23_market_sensitivity_pe_ewma_slope_21d_v231_signal": {"func": f23_market_sensitivity_pe_ewma_slope_21d_v231_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_21d_v232_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_21d_v232_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_42d_v233_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_42d_v233_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_42d_v234_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_42d_v234_signal},
    "f23_market_sensitivity_pe_ewma_slope_42d_v235_signal": {"func": f23_market_sensitivity_pe_ewma_slope_42d_v235_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_42d_v236_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_42d_v236_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_63d_v237_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_63d_v237_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_63d_v238_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_63d_v238_signal},
    "f23_market_sensitivity_pe_ewma_slope_63d_v239_signal": {"func": f23_market_sensitivity_pe_ewma_slope_63d_v239_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_63d_v240_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_63d_v240_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_126d_v241_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_126d_v241_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_126d_v242_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_126d_v242_signal},
    "f23_market_sensitivity_pe_ewma_slope_126d_v243_signal": {"func": f23_market_sensitivity_pe_ewma_slope_126d_v243_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_126d_v244_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_126d_v244_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_252d_v245_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_252d_v245_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_252d_v246_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_252d_v246_signal},
    "f23_market_sensitivity_pe_ewma_slope_252d_v247_signal": {"func": f23_market_sensitivity_pe_ewma_slope_252d_v247_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_252d_v248_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_252d_v248_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_504d_v249_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_504d_v249_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_504d_v250_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_504d_v250_signal},
    "f23_market_sensitivity_pe_ewma_slope_504d_v251_signal": {"func": f23_market_sensitivity_pe_ewma_slope_504d_v251_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_504d_v252_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_504d_v252_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_756d_v253_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_756d_v253_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_756d_v254_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_756d_v254_signal},
    "f23_market_sensitivity_pe_ewma_slope_756d_v255_signal": {"func": f23_market_sensitivity_pe_ewma_slope_756d_v255_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_756d_v256_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_756d_v256_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_1008d_v257_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_1008d_v257_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_1008d_v258_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_1008d_v258_signal},
    "f23_market_sensitivity_pe_ewma_slope_1008d_v259_signal": {"func": f23_market_sensitivity_pe_ewma_slope_1008d_v259_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_1008d_v260_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_1008d_v260_signal},
    "f23_market_sensitivity_closeadj_ewma_slope_1260d_v261_signal": {"func": f23_market_sensitivity_closeadj_ewma_slope_1260d_v261_signal},
    "f23_market_sensitivity_marketcap_ewma_slope_1260d_v262_signal": {"func": f23_market_sensitivity_marketcap_ewma_slope_1260d_v262_signal},
    "f23_market_sensitivity_pe_ewma_slope_1260d_v263_signal": {"func": f23_market_sensitivity_pe_ewma_slope_1260d_v263_signal},
    "f23_market_sensitivity_vol_premium_ewma_slope_1260d_v264_signal": {"func": f23_market_sensitivity_vol_premium_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 23...")
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
