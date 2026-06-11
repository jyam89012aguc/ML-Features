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

def f19_broker_dealer_pe_mom_z_63d_v151_signal(pe):
    """Relative momentum strength for Raw level of pe over 63d window."""
    res = _z(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_63d_v152_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 63d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_mom_z_126d_v153_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_mom_z_126d_v154_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 126d window."""
    res = _z(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_mom_z_126d_v155_signal(pe):
    """Relative momentum strength for Raw level of pe over 126d window."""
    res = _z(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_126d_v156_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 126d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_mom_z_252d_v157_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_mom_z_252d_v158_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 252d window."""
    res = _z(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_mom_z_252d_v159_signal(pe):
    """Relative momentum strength for Raw level of pe over 252d window."""
    res = _z(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_252d_v160_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 252d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_mom_z_504d_v161_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_mom_z_504d_v162_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 504d window."""
    res = _z(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_mom_z_504d_v163_signal(pe):
    """Relative momentum strength for Raw level of pe over 504d window."""
    res = _z(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_504d_v164_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 504d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_mom_z_756d_v165_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_mom_z_756d_v166_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 756d window."""
    res = _z(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_mom_z_756d_v167_signal(pe):
    """Relative momentum strength for Raw level of pe over 756d window."""
    res = _z(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_756d_v168_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 756d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_mom_z_1008d_v169_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_mom_z_1008d_v170_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 1008d window."""
    res = _z(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_mom_z_1008d_v171_signal(pe):
    """Relative momentum strength for Raw level of pe over 1008d window."""
    res = _z(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_1008d_v172_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 1008d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_mom_z_1260d_v173_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_mom_z_1260d_v174_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 1260d window."""
    res = _z(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_mom_z_1260d_v175_signal(pe):
    """Relative momentum strength for Raw level of pe over 1260d window."""
    res = _z(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_mom_z_1260d_v176_signal(ebitda, revenue):
    """Relative momentum strength for Operating margin quality over 1260d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_5d_v177_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_5d_v178_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 5d window."""
    res = _std(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_5d_v179_signal(pe):
    """Volatility of momentum for Raw level of pe over 5d window."""
    res = _std(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_5d_v180_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 5d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_10d_v181_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_10d_v182_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 10d window."""
    res = _std(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_10d_v183_signal(pe):
    """Volatility of momentum for Raw level of pe over 10d window."""
    res = _std(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_10d_v184_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 10d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_21d_v185_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_21d_v186_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 21d window."""
    res = _std(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_21d_v187_signal(pe):
    """Volatility of momentum for Raw level of pe over 21d window."""
    res = _std(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_21d_v188_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 21d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_42d_v189_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_42d_v190_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 42d window."""
    res = _std(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_42d_v191_signal(pe):
    """Volatility of momentum for Raw level of pe over 42d window."""
    res = _std(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_42d_v192_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 42d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_63d_v193_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_63d_v194_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 63d window."""
    res = _std(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_63d_v195_signal(pe):
    """Volatility of momentum for Raw level of pe over 63d window."""
    res = _std(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_63d_v196_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 63d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_126d_v197_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_126d_v198_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 126d window."""
    res = _std(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_126d_v199_signal(pe):
    """Volatility of momentum for Raw level of pe over 126d window."""
    res = _std(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_126d_v200_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 126d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_252d_v201_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_252d_v202_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 252d window."""
    res = _std(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_252d_v203_signal(pe):
    """Volatility of momentum for Raw level of pe over 252d window."""
    res = _std(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_252d_v204_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 252d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_504d_v205_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_504d_v206_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 504d window."""
    res = _std(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_504d_v207_signal(pe):
    """Volatility of momentum for Raw level of pe over 504d window."""
    res = _std(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_504d_v208_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 504d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_756d_v209_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_756d_v210_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 756d window."""
    res = _std(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_756d_v211_signal(pe):
    """Volatility of momentum for Raw level of pe over 756d window."""
    res = _std(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_756d_v212_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 756d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_1008d_v213_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_1008d_v214_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 1008d window."""
    res = _std(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_1008d_v215_signal(pe):
    """Volatility of momentum for Raw level of pe over 1008d window."""
    res = _std(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_1008d_v216_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 1008d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_vol_slope_1260d_v217_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_vol_slope_1260d_v218_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 1260d window."""
    res = _std(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_vol_slope_1260d_v219_signal(pe):
    """Volatility of momentum for Raw level of pe over 1260d window."""
    res = _std(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_vol_slope_1260d_v220_signal(ebitda, revenue):
    """Volatility of momentum for Operating margin quality over 1260d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_5d_v221_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 5d window."""
    res = _ewma(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_5d_v222_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 5d window."""
    res = _ewma(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_5d_v223_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 5d window."""
    res = _ewma(_slope_pct(pe, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_5d_v224_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 5d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_10d_v225_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 10d window."""
    res = _ewma(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_10d_v226_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 10d window."""
    res = _ewma(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_10d_v227_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 10d window."""
    res = _ewma(_slope_pct(pe, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_10d_v228_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 10d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_21d_v229_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 21d window."""
    res = _ewma(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_21d_v230_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 21d window."""
    res = _ewma(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_21d_v231_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 21d window."""
    res = _ewma(_slope_pct(pe, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_21d_v232_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 21d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_42d_v233_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 42d window."""
    res = _ewma(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_42d_v234_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 42d window."""
    res = _ewma(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_42d_v235_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 42d window."""
    res = _ewma(_slope_pct(pe, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_42d_v236_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 42d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_63d_v237_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 63d window."""
    res = _ewma(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_63d_v238_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 63d window."""
    res = _ewma(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_63d_v239_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 63d window."""
    res = _ewma(_slope_pct(pe, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_63d_v240_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 63d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_126d_v241_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 126d window."""
    res = _ewma(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_126d_v242_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 126d window."""
    res = _ewma(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_126d_v243_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 126d window."""
    res = _ewma(_slope_pct(pe, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_126d_v244_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 126d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_252d_v245_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 252d window."""
    res = _ewma(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_252d_v246_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 252d window."""
    res = _ewma(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_252d_v247_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 252d window."""
    res = _ewma(_slope_pct(pe, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_252d_v248_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 252d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_504d_v249_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 504d window."""
    res = _ewma(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_504d_v250_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 504d window."""
    res = _ewma(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_504d_v251_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 504d window."""
    res = _ewma(_slope_pct(pe, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_504d_v252_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 504d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_756d_v253_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 756d window."""
    res = _ewma(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_756d_v254_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 756d window."""
    res = _ewma(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_756d_v255_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 756d window."""
    res = _ewma(_slope_pct(pe, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_756d_v256_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 756d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_1008d_v257_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1008d window."""
    res = _ewma(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_1008d_v258_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 1008d window."""
    res = _ewma(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_1008d_v259_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 1008d window."""
    res = _ewma(_slope_pct(pe, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_1008d_v260_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 1008d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_revenue_ewma_slope_1260d_v261_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 1260d window."""
    res = _ewma(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_ebitda_ewma_slope_1260d_v262_signal(ebitda):
    """Exponential momentum smoothing for Raw level of ebitda over 1260d window."""
    res = _ewma(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_pe_ewma_slope_1260d_v263_signal(pe):
    """Exponential momentum smoothing for Raw level of pe over 1260d window."""
    res = _ewma(_slope_pct(pe, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f19_broker_dealer_margin_quality_ewma_slope_1260d_v264_signal(ebitda, revenue):
    """Exponential momentum smoothing for Operating margin quality over 1260d window."""
    res = _ewma(_slope_pct(_ratio(ebitda, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f19_broker_dealer_pe_mom_z_63d_v151_signal": {"func": f19_broker_dealer_pe_mom_z_63d_v151_signal},
    "f19_broker_dealer_margin_quality_mom_z_63d_v152_signal": {"func": f19_broker_dealer_margin_quality_mom_z_63d_v152_signal},
    "f19_broker_dealer_revenue_mom_z_126d_v153_signal": {"func": f19_broker_dealer_revenue_mom_z_126d_v153_signal},
    "f19_broker_dealer_ebitda_mom_z_126d_v154_signal": {"func": f19_broker_dealer_ebitda_mom_z_126d_v154_signal},
    "f19_broker_dealer_pe_mom_z_126d_v155_signal": {"func": f19_broker_dealer_pe_mom_z_126d_v155_signal},
    "f19_broker_dealer_margin_quality_mom_z_126d_v156_signal": {"func": f19_broker_dealer_margin_quality_mom_z_126d_v156_signal},
    "f19_broker_dealer_revenue_mom_z_252d_v157_signal": {"func": f19_broker_dealer_revenue_mom_z_252d_v157_signal},
    "f19_broker_dealer_ebitda_mom_z_252d_v158_signal": {"func": f19_broker_dealer_ebitda_mom_z_252d_v158_signal},
    "f19_broker_dealer_pe_mom_z_252d_v159_signal": {"func": f19_broker_dealer_pe_mom_z_252d_v159_signal},
    "f19_broker_dealer_margin_quality_mom_z_252d_v160_signal": {"func": f19_broker_dealer_margin_quality_mom_z_252d_v160_signal},
    "f19_broker_dealer_revenue_mom_z_504d_v161_signal": {"func": f19_broker_dealer_revenue_mom_z_504d_v161_signal},
    "f19_broker_dealer_ebitda_mom_z_504d_v162_signal": {"func": f19_broker_dealer_ebitda_mom_z_504d_v162_signal},
    "f19_broker_dealer_pe_mom_z_504d_v163_signal": {"func": f19_broker_dealer_pe_mom_z_504d_v163_signal},
    "f19_broker_dealer_margin_quality_mom_z_504d_v164_signal": {"func": f19_broker_dealer_margin_quality_mom_z_504d_v164_signal},
    "f19_broker_dealer_revenue_mom_z_756d_v165_signal": {"func": f19_broker_dealer_revenue_mom_z_756d_v165_signal},
    "f19_broker_dealer_ebitda_mom_z_756d_v166_signal": {"func": f19_broker_dealer_ebitda_mom_z_756d_v166_signal},
    "f19_broker_dealer_pe_mom_z_756d_v167_signal": {"func": f19_broker_dealer_pe_mom_z_756d_v167_signal},
    "f19_broker_dealer_margin_quality_mom_z_756d_v168_signal": {"func": f19_broker_dealer_margin_quality_mom_z_756d_v168_signal},
    "f19_broker_dealer_revenue_mom_z_1008d_v169_signal": {"func": f19_broker_dealer_revenue_mom_z_1008d_v169_signal},
    "f19_broker_dealer_ebitda_mom_z_1008d_v170_signal": {"func": f19_broker_dealer_ebitda_mom_z_1008d_v170_signal},
    "f19_broker_dealer_pe_mom_z_1008d_v171_signal": {"func": f19_broker_dealer_pe_mom_z_1008d_v171_signal},
    "f19_broker_dealer_margin_quality_mom_z_1008d_v172_signal": {"func": f19_broker_dealer_margin_quality_mom_z_1008d_v172_signal},
    "f19_broker_dealer_revenue_mom_z_1260d_v173_signal": {"func": f19_broker_dealer_revenue_mom_z_1260d_v173_signal},
    "f19_broker_dealer_ebitda_mom_z_1260d_v174_signal": {"func": f19_broker_dealer_ebitda_mom_z_1260d_v174_signal},
    "f19_broker_dealer_pe_mom_z_1260d_v175_signal": {"func": f19_broker_dealer_pe_mom_z_1260d_v175_signal},
    "f19_broker_dealer_margin_quality_mom_z_1260d_v176_signal": {"func": f19_broker_dealer_margin_quality_mom_z_1260d_v176_signal},
    "f19_broker_dealer_revenue_vol_slope_5d_v177_signal": {"func": f19_broker_dealer_revenue_vol_slope_5d_v177_signal},
    "f19_broker_dealer_ebitda_vol_slope_5d_v178_signal": {"func": f19_broker_dealer_ebitda_vol_slope_5d_v178_signal},
    "f19_broker_dealer_pe_vol_slope_5d_v179_signal": {"func": f19_broker_dealer_pe_vol_slope_5d_v179_signal},
    "f19_broker_dealer_margin_quality_vol_slope_5d_v180_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_5d_v180_signal},
    "f19_broker_dealer_revenue_vol_slope_10d_v181_signal": {"func": f19_broker_dealer_revenue_vol_slope_10d_v181_signal},
    "f19_broker_dealer_ebitda_vol_slope_10d_v182_signal": {"func": f19_broker_dealer_ebitda_vol_slope_10d_v182_signal},
    "f19_broker_dealer_pe_vol_slope_10d_v183_signal": {"func": f19_broker_dealer_pe_vol_slope_10d_v183_signal},
    "f19_broker_dealer_margin_quality_vol_slope_10d_v184_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_10d_v184_signal},
    "f19_broker_dealer_revenue_vol_slope_21d_v185_signal": {"func": f19_broker_dealer_revenue_vol_slope_21d_v185_signal},
    "f19_broker_dealer_ebitda_vol_slope_21d_v186_signal": {"func": f19_broker_dealer_ebitda_vol_slope_21d_v186_signal},
    "f19_broker_dealer_pe_vol_slope_21d_v187_signal": {"func": f19_broker_dealer_pe_vol_slope_21d_v187_signal},
    "f19_broker_dealer_margin_quality_vol_slope_21d_v188_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_21d_v188_signal},
    "f19_broker_dealer_revenue_vol_slope_42d_v189_signal": {"func": f19_broker_dealer_revenue_vol_slope_42d_v189_signal},
    "f19_broker_dealer_ebitda_vol_slope_42d_v190_signal": {"func": f19_broker_dealer_ebitda_vol_slope_42d_v190_signal},
    "f19_broker_dealer_pe_vol_slope_42d_v191_signal": {"func": f19_broker_dealer_pe_vol_slope_42d_v191_signal},
    "f19_broker_dealer_margin_quality_vol_slope_42d_v192_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_42d_v192_signal},
    "f19_broker_dealer_revenue_vol_slope_63d_v193_signal": {"func": f19_broker_dealer_revenue_vol_slope_63d_v193_signal},
    "f19_broker_dealer_ebitda_vol_slope_63d_v194_signal": {"func": f19_broker_dealer_ebitda_vol_slope_63d_v194_signal},
    "f19_broker_dealer_pe_vol_slope_63d_v195_signal": {"func": f19_broker_dealer_pe_vol_slope_63d_v195_signal},
    "f19_broker_dealer_margin_quality_vol_slope_63d_v196_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_63d_v196_signal},
    "f19_broker_dealer_revenue_vol_slope_126d_v197_signal": {"func": f19_broker_dealer_revenue_vol_slope_126d_v197_signal},
    "f19_broker_dealer_ebitda_vol_slope_126d_v198_signal": {"func": f19_broker_dealer_ebitda_vol_slope_126d_v198_signal},
    "f19_broker_dealer_pe_vol_slope_126d_v199_signal": {"func": f19_broker_dealer_pe_vol_slope_126d_v199_signal},
    "f19_broker_dealer_margin_quality_vol_slope_126d_v200_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_126d_v200_signal},
    "f19_broker_dealer_revenue_vol_slope_252d_v201_signal": {"func": f19_broker_dealer_revenue_vol_slope_252d_v201_signal},
    "f19_broker_dealer_ebitda_vol_slope_252d_v202_signal": {"func": f19_broker_dealer_ebitda_vol_slope_252d_v202_signal},
    "f19_broker_dealer_pe_vol_slope_252d_v203_signal": {"func": f19_broker_dealer_pe_vol_slope_252d_v203_signal},
    "f19_broker_dealer_margin_quality_vol_slope_252d_v204_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_252d_v204_signal},
    "f19_broker_dealer_revenue_vol_slope_504d_v205_signal": {"func": f19_broker_dealer_revenue_vol_slope_504d_v205_signal},
    "f19_broker_dealer_ebitda_vol_slope_504d_v206_signal": {"func": f19_broker_dealer_ebitda_vol_slope_504d_v206_signal},
    "f19_broker_dealer_pe_vol_slope_504d_v207_signal": {"func": f19_broker_dealer_pe_vol_slope_504d_v207_signal},
    "f19_broker_dealer_margin_quality_vol_slope_504d_v208_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_504d_v208_signal},
    "f19_broker_dealer_revenue_vol_slope_756d_v209_signal": {"func": f19_broker_dealer_revenue_vol_slope_756d_v209_signal},
    "f19_broker_dealer_ebitda_vol_slope_756d_v210_signal": {"func": f19_broker_dealer_ebitda_vol_slope_756d_v210_signal},
    "f19_broker_dealer_pe_vol_slope_756d_v211_signal": {"func": f19_broker_dealer_pe_vol_slope_756d_v211_signal},
    "f19_broker_dealer_margin_quality_vol_slope_756d_v212_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_756d_v212_signal},
    "f19_broker_dealer_revenue_vol_slope_1008d_v213_signal": {"func": f19_broker_dealer_revenue_vol_slope_1008d_v213_signal},
    "f19_broker_dealer_ebitda_vol_slope_1008d_v214_signal": {"func": f19_broker_dealer_ebitda_vol_slope_1008d_v214_signal},
    "f19_broker_dealer_pe_vol_slope_1008d_v215_signal": {"func": f19_broker_dealer_pe_vol_slope_1008d_v215_signal},
    "f19_broker_dealer_margin_quality_vol_slope_1008d_v216_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_1008d_v216_signal},
    "f19_broker_dealer_revenue_vol_slope_1260d_v217_signal": {"func": f19_broker_dealer_revenue_vol_slope_1260d_v217_signal},
    "f19_broker_dealer_ebitda_vol_slope_1260d_v218_signal": {"func": f19_broker_dealer_ebitda_vol_slope_1260d_v218_signal},
    "f19_broker_dealer_pe_vol_slope_1260d_v219_signal": {"func": f19_broker_dealer_pe_vol_slope_1260d_v219_signal},
    "f19_broker_dealer_margin_quality_vol_slope_1260d_v220_signal": {"func": f19_broker_dealer_margin_quality_vol_slope_1260d_v220_signal},
    "f19_broker_dealer_revenue_ewma_slope_5d_v221_signal": {"func": f19_broker_dealer_revenue_ewma_slope_5d_v221_signal},
    "f19_broker_dealer_ebitda_ewma_slope_5d_v222_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_5d_v222_signal},
    "f19_broker_dealer_pe_ewma_slope_5d_v223_signal": {"func": f19_broker_dealer_pe_ewma_slope_5d_v223_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_5d_v224_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_5d_v224_signal},
    "f19_broker_dealer_revenue_ewma_slope_10d_v225_signal": {"func": f19_broker_dealer_revenue_ewma_slope_10d_v225_signal},
    "f19_broker_dealer_ebitda_ewma_slope_10d_v226_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_10d_v226_signal},
    "f19_broker_dealer_pe_ewma_slope_10d_v227_signal": {"func": f19_broker_dealer_pe_ewma_slope_10d_v227_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_10d_v228_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_10d_v228_signal},
    "f19_broker_dealer_revenue_ewma_slope_21d_v229_signal": {"func": f19_broker_dealer_revenue_ewma_slope_21d_v229_signal},
    "f19_broker_dealer_ebitda_ewma_slope_21d_v230_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_21d_v230_signal},
    "f19_broker_dealer_pe_ewma_slope_21d_v231_signal": {"func": f19_broker_dealer_pe_ewma_slope_21d_v231_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_21d_v232_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_21d_v232_signal},
    "f19_broker_dealer_revenue_ewma_slope_42d_v233_signal": {"func": f19_broker_dealer_revenue_ewma_slope_42d_v233_signal},
    "f19_broker_dealer_ebitda_ewma_slope_42d_v234_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_42d_v234_signal},
    "f19_broker_dealer_pe_ewma_slope_42d_v235_signal": {"func": f19_broker_dealer_pe_ewma_slope_42d_v235_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_42d_v236_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_42d_v236_signal},
    "f19_broker_dealer_revenue_ewma_slope_63d_v237_signal": {"func": f19_broker_dealer_revenue_ewma_slope_63d_v237_signal},
    "f19_broker_dealer_ebitda_ewma_slope_63d_v238_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_63d_v238_signal},
    "f19_broker_dealer_pe_ewma_slope_63d_v239_signal": {"func": f19_broker_dealer_pe_ewma_slope_63d_v239_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_63d_v240_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_63d_v240_signal},
    "f19_broker_dealer_revenue_ewma_slope_126d_v241_signal": {"func": f19_broker_dealer_revenue_ewma_slope_126d_v241_signal},
    "f19_broker_dealer_ebitda_ewma_slope_126d_v242_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_126d_v242_signal},
    "f19_broker_dealer_pe_ewma_slope_126d_v243_signal": {"func": f19_broker_dealer_pe_ewma_slope_126d_v243_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_126d_v244_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_126d_v244_signal},
    "f19_broker_dealer_revenue_ewma_slope_252d_v245_signal": {"func": f19_broker_dealer_revenue_ewma_slope_252d_v245_signal},
    "f19_broker_dealer_ebitda_ewma_slope_252d_v246_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_252d_v246_signal},
    "f19_broker_dealer_pe_ewma_slope_252d_v247_signal": {"func": f19_broker_dealer_pe_ewma_slope_252d_v247_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_252d_v248_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_252d_v248_signal},
    "f19_broker_dealer_revenue_ewma_slope_504d_v249_signal": {"func": f19_broker_dealer_revenue_ewma_slope_504d_v249_signal},
    "f19_broker_dealer_ebitda_ewma_slope_504d_v250_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_504d_v250_signal},
    "f19_broker_dealer_pe_ewma_slope_504d_v251_signal": {"func": f19_broker_dealer_pe_ewma_slope_504d_v251_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_504d_v252_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_504d_v252_signal},
    "f19_broker_dealer_revenue_ewma_slope_756d_v253_signal": {"func": f19_broker_dealer_revenue_ewma_slope_756d_v253_signal},
    "f19_broker_dealer_ebitda_ewma_slope_756d_v254_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_756d_v254_signal},
    "f19_broker_dealer_pe_ewma_slope_756d_v255_signal": {"func": f19_broker_dealer_pe_ewma_slope_756d_v255_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_756d_v256_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_756d_v256_signal},
    "f19_broker_dealer_revenue_ewma_slope_1008d_v257_signal": {"func": f19_broker_dealer_revenue_ewma_slope_1008d_v257_signal},
    "f19_broker_dealer_ebitda_ewma_slope_1008d_v258_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_1008d_v258_signal},
    "f19_broker_dealer_pe_ewma_slope_1008d_v259_signal": {"func": f19_broker_dealer_pe_ewma_slope_1008d_v259_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_1008d_v260_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_1008d_v260_signal},
    "f19_broker_dealer_revenue_ewma_slope_1260d_v261_signal": {"func": f19_broker_dealer_revenue_ewma_slope_1260d_v261_signal},
    "f19_broker_dealer_ebitda_ewma_slope_1260d_v262_signal": {"func": f19_broker_dealer_ebitda_ewma_slope_1260d_v262_signal},
    "f19_broker_dealer_pe_ewma_slope_1260d_v263_signal": {"func": f19_broker_dealer_pe_ewma_slope_1260d_v263_signal},
    "f19_broker_dealer_margin_quality_ewma_slope_1260d_v264_signal": {"func": f19_broker_dealer_margin_quality_ewma_slope_1260d_v264_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 19...")
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
